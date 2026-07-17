# SBOM Summary Report — SampleCodebase

- **Source file:** `SampleCodebase-cyclonedx-identified.json`
- **Scan timestamp:** 2026-07-15T09:44:48.937Z
- **Report generated:** 2026-07-17T08:17:01.400559+00:00
- **Total component entries:** 13
- **Unique package names:** 13
- **Vulnerability data present:** No

## Overview

SampleCodebase's SBOM catalogs 13 component entries, each a distinct package name with no duplicate or multi-version instances detected, so there's no version sprawl to worry about here. The dependencies are drawn primarily from GitHub-hosted sources and Maven, with a small number of packages sourced from netfilter.org and madler, indicating a moderately diverse but manageable supply chain. Licensing is where this bill of materials warrants closer attention: while Apache-2.0 dominates and BSD/GPL variants are common and generally well-understood, the presence of GPL-2.0-only, GPL-3.0-or-later, and niche or unusual licenses such as OpenSSL, w3m, and Apache-1.1 introduces a mixed compliance landscape that should be reviewed against the project's distribution and licensing obligations. Notably, no vulnerability data has been incorporated into this SBOM, which means the security posture of these components remains unassessed and should be treated as a priority follow-up before this report can inform risk decisions. Overall, the footprint is small and cleanly versioned, but the license heterogeneity and absence of vulnerability scanning are the two items most deserving of reviewer scrutiny.

## Ecosystem Breakdown

| Ecosystem | Entries | % of Total |
|---|---|---|
| github | 5 | 38.5% |
| maven | 4 | 30.8% |
| github.com | 2 | 15.4% |
| netfilter.org | 1 | 7.7% |
| madler | 1 | 7.7% |

## License Breakdown

| License (SPDX) | Entries | % of Total |
|---|---|---|
| Apache-2.0 | 5 | 38.5% |
| BSD-3-Clause | 2 | 15.4% |
| GPL-2.0-only | 2 | 15.4% |
| OpenSSL | 1 | 7.7% |
| BSD-2-Clause | 1 | 7.7% |
| w3m | 1 | 7.7% |
| MPL-2.0 | 1 | 7.7% |
| MIT | 1 | 7.7% |
| GPL-2.0 | 1 | 7.7% |
| GPL-3.0-or-later | 1 | 7.7% |
| Apache-1.1 | 1 | 7.7% |

## Version Sprawl (Top 10)

No packages with multiple versions detected.
