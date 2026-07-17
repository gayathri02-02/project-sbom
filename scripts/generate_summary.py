#!/usr/bin/env python3
"""
Generate a Markdown summary report for each CycloneDX SBOM JSON file
found in the input directory.

The ecosystem / license / version-sprawl numbers below are computed
directly from the SBOM data — deterministic, no AI involved. Those
numbers are then handed to the Claude API, which writes a short
narrative "Overview" section calling out what a reviewer should notice
first. If ANTHROPIC_API_KEY isn't set, or the API call fails for any
reason, the script still writes the full report — it just skips that
one section rather than failing the whole run.

Usage:
    python3 generate_summary.py <sbom_input_dir> <report_output_dir>
"""
import json
import os
import re
import sys
import collections
from pathlib import Path
from datetime import datetime, timezone

import anthropic

# claude-sonnet-5 is plenty for a few sentences of prose per SBOM.
# Swap to "claude-haiku-4-5-20251001" if you want to cut cost further.
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5")


def build_overview_prompt(app_name: str, stats: dict) -> str:
    return f"""You are writing the opening "Overview" section of an SBOM (Software Bill of Materials) summary report for "{app_name}".

Here is the structured data already computed from the SBOM (ground truth — do not invent numbers beyond these):

{json.dumps(stats, indent=2)}

Write 3-5 sentences of plain prose (no headers, no bullet points, no
Markdown tables) that a reviewer would read first: what the dependency
footprint looks like, whether the license mix looks straightforward or
worth a closer look, and whether version sprawl or missing vulnerability
data is worth flagging. Do not repeat the raw tables — those follow
this section separately. Output only the prose, nothing else."""


def generate_ai_overview(app_name: str, stats: dict) -> str | None:
    """Ask Claude for a short narrative overview. Returns None (never
    raises) if there's no API key or the call fails, so a missing/broken
    key degrades the report instead of breaking the pipeline."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(f"  (no ANTHROPIC_API_KEY set — skipping AI overview for {app_name})", file=sys.stderr)
        return None
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model=MODEL,
            max_tokens=512,
            messages=[{"role": "user", "content": build_overview_prompt(app_name, stats)}],
        )
        return "".join(block.text for block in message.content if block.type == "text").strip()
    except Exception as exc:  # noqa: BLE001 — never let the AI step break the report
        print(f"  (Claude API call failed for {app_name}: {exc} — skipping AI overview)", file=sys.stderr)
        return None


def summarize(sbom_path: Path) -> str:
    with open(sbom_path) as f:
        data = json.load(f)

    comps = data.get("components", [])
    meta = data.get("metadata", {})
    app_name = meta.get("component", {}).get("name", sbom_path.stem)
    scan_ts = meta.get("timestamp", "unknown")

    eco_counter = collections.Counter()
    license_counter = collections.Counter()
    name_versions = collections.defaultdict(set)

    for c in comps:
        purl = c.get("purl", "")
        m = re.match(r"pkg:([^/]+)/", purl)
        eco_counter[m.group(1) if m else "unknown"] += 1
        seen = set()
        for lic in c.get("licenses", []) or []:
            lid = lic.get("license", {}).get("id") or lic.get("license", {}).get("name")
            if lid and lid not in seen:
                license_counter[lid] += 1
                seen.add(lid)
        name_versions[c.get("name")].add(c.get("version"))

    total = len(comps)
    unique_names = len(name_versions)
    dupes = {k: v for k, v in name_versions.items() if len(v) > 1}
    top_dupes = sorted(dupes.items(), key=lambda x: -len(x[1]))[:10]
    has_vulns = "vulnerabilities" in data

    # Structured stats handed to Claude as ground truth — same numbers
    # that go into the tables below, just gathered in one place.
    stats = {
        "total_component_entries": total,
        "unique_package_names": unique_names,
        "ecosystem_breakdown": dict(eco_counter.most_common()),
        "license_breakdown": dict(license_counter.most_common()),
        "packages_with_multiple_versions": {k: sorted(v) for k, v in top_dupes},
        "vulnerability_data_present": has_vulns,
    }
    ai_overview = generate_ai_overview(app_name, stats)

    lines = []
    lines.append(f"# SBOM Summary Report — {app_name}")
    lines.append("")
    lines.append(f"- **Source file:** `{sbom_path.name}`")
    lines.append(f"- **Scan timestamp:** {scan_ts}")
    lines.append(f"- **Report generated:** {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"- **Total component entries:** {total}")
    lines.append(f"- **Unique package names:** {unique_names}")
    lines.append(f"- **Vulnerability data present:** {'Yes' if has_vulns else 'No'}")
    lines.append("")

    if ai_overview:
        lines.append("## Overview")
        lines.append("")
        lines.append(ai_overview)
        lines.append("")

    lines.append("## Ecosystem Breakdown")
    lines.append("")
    lines.append("| Ecosystem | Entries | % of Total |")
    lines.append("|---|---|---|")
    for eco, count in eco_counter.most_common():
        pct = (count / total * 100) if total else 0
        lines.append(f"| {eco} | {count} | {pct:.1f}% |")
    lines.append("")

    lines.append("## License Breakdown")
    lines.append("")
    lines.append("| License (SPDX) | Entries | % of Total |")
    lines.append("|---|---|---|")
    for lic, count in license_counter.most_common():
        pct = (count / total * 100) if total else 0
        lines.append(f"| {lic} | {count} | {pct:.1f}% |")
    lines.append("")

    lines.append("## Version Sprawl (Top 10)")
    lines.append("")
    if top_dupes:
        lines.append("| Package | Distinct Versions |")
        lines.append("|---|---|")
        for name, versions in top_dupes:
            lines.append(f"| {name} | {len(versions)} |")
    else:
        lines.append("No packages with multiple versions detected.")
    lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 generate_summary.py <sbom_input_dir> <report_output_dir>")
        sys.exit(1)

    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(parents=True, exist_ok=True)

    sbom_files = sorted(input_dir.glob("*.json"))
    if not sbom_files:
        print(f"No SBOM JSON files found in {input_dir}")
        sys.exit(1)

    for sbom_path in sbom_files:
        report_md = summarize(sbom_path)
        out_path = output_dir / f"{sbom_path.stem}-summary.md"
        out_path.write_text(report_md)
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
