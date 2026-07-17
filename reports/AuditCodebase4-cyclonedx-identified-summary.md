# SBOM Summary Report — AuditCodebase4

- **Source file:** `AuditCodebase4-cyclonedx-identified.json`
- **Scan timestamp:** 2026-07-15T06:03:10.121Z
- **Report generated:** 2026-07-17T11:17:57.796761+00:00
- **Total component entries:** 41
- **Unique package names:** 34
- **Vulnerability data present:** No

## Overview

This SBOM for AuditCodebase4 catalogs 41 component entries covering 34 unique package names, drawn predominantly from GitHub-based sources (25 entries across "github" and "github.com" identifiers) with smaller contributions from Maven, npm, NuGet, PyPI, Bitbucket, StackOverflow, and a few standalone ecosystems. The license landscape, while led by permissive MIT and Apache-2.0 terms, is worth a closer look given the notable presence of copyleft licenses—AGPL-3.0 in three variants totaling 15 entries plus GPL-2.0 and GPL-3.0 instances—alongside a handful of less common or reference-style license identifiers that may warrant legal review depending on distribution intent. Version sprawl is evident in at least three packages, most notably servicestack/servicestack with six distinct tagged versions in use, which suggests fragmented dependency management and potential inconsistency in patch or feature parity across the codebase. Finally, no vulnerability data is present in this SBOM, meaning security posture cannot be assessed from this document alone and should be flagged as a gap requiring a separate scan or enrichment pass before this report can inform risk decisions.

## Ecosystem Breakdown

| Ecosystem | Entries | % of Total |
|---|---|---|
| github | 21 | 51.2% |
| github.com | 4 | 9.8% |
| maven | 4 | 9.8% |
| stackoverflow | 2 | 4.9% |
| pypi | 2 | 4.9% |
| bitbucket | 2 | 4.9% |
| npm | 2 | 4.9% |
| nuget | 2 | 4.9% |
| generic | 1 | 2.4% |
| jquery | 1 | 2.4% |

## License Breakdown

| License (SPDX) | Entries | % of Total |
|---|---|---|
| MIT | 20 | 48.8% |
| Apache-2.0 | 8 | 19.5% |
| AGPL-3.0-only | 7 | 17.1% |
| MS-PL | 7 | 17.1% |
| AGPL-3.0-or-later | 6 | 14.6% |
| BSD-3-Clause | 4 | 9.8% |
| CC-BY-SA-3.0 | 2 | 4.9% |
| AGPL-3.0 | 2 | 4.9% |
| GPL-2.0-only | 2 | 4.9% |
| GPL-2.0-or-later | 2 | 4.9% |
| LGPL-2.1 | 1 | 2.4% |
| 0BSD | 1 | 2.4% |
| LicenseRef-bsd-3--clause-license | 1 | 2.4% |
| GPL-3.0-only | 1 | 2.4% |
| CC-BY-4.0 | 1 | 2.4% |
| LicenseRef-scancode-free-unknown | 1 | 2.4% |

## Version Sprawl (Top 10)

| Package | Distinct Versions |
|---|---|
| pkg:github/servicestack/servicestack | 6 |
| pkg:github/malihu/malihu-custom-scrollbar-plugin | 2 |
| pkg:github/pandas-dev/pandas | 2 |
