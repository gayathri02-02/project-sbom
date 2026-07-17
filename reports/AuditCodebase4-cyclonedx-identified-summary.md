# SBOM Summary Report — AuditCodebase4

- **Source file:** `AuditCodebase4-cyclonedx-identified.json`
- **Scan timestamp:** 2026-07-15T06:03:10.121Z
- **Report generated:** 2026-07-17T11:24:52.394260+00:00
- **Total component entries:** 41
- **Unique package names:** 34
- **Vulnerability data present:** No

## Overview

This SBOM for AuditCodebase4 catalogs 41 component entries covering 34 unique packages, with the footprint dominated by GitHub-sourced dependencies (25 entries across github and github.com) alongside smaller contributions from Maven, npm, NuGet, PyPI, and a handful of other ecosystems. The license mix is worth a closer look: while MIT and Apache-2.0 account for the bulk of entries, there's a notable presence of copyleft licenses—13 entries under AGPL-3.0 variants plus GPL-2.0 and GPL-3.0 entries—which introduces compliance considerations that a purely permissive stack wouldn't raise, and a few ambiguous or non-standard identifiers (LicenseRef entries) may need manual review. Version sprawl is limited but present, most notably servicestack/servicestack tracked across six versions, suggesting either gradual upgrades left unconsolidated or genuine need for multiple releases in different contexts. No vulnerability data is included in this SBOM, which is a gap reviewers should flag, since license and dependency composition alone can't confirm the security posture of these components. Overall, the dependency set is moderate in size and manageable, but the copyleft license concentration and absent vulnerability scan results are the two points most deserving of follow-up.

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
