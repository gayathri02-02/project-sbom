# SBOM Summary Report — ops-master

- **Source file:** `ops-master-cyclonedx-identified.json`
- **Scan timestamp:** 2026-07-13T04:54:23.175Z
- **Report generated:** 2026-07-17T11:18:04.108227+00:00
- **Total component entries:** 932
- **Unique package names:** 363
- **Vulnerability data present:** No

## Overview

This SBOM for ops-master catalogs 932 component entries spanning 363 unique package names, and the footprint is overwhelmingly Go-centric: 921 of 932 entries come from the golang ecosystem, with only a handful of github, npm, and maven packages rounding things out. The license mix is largely permissive and low-risk, dominated by BSD-3-Clause, Apache-2.0, and MIT (together covering the vast majority of entries), with a long tail of single-instance licenses like GooglePatentClause, UPL-1.0, and CC-BY-SA-4.0 that are worth a quick look but unlikely to pose material concern. Version sprawl is notable and worth flagging for cleanup: core transitive dependencies such as golang.org/x/sys, golang.org/x/tools, golang.org/x/net, and google.golang.org/genproto each appear pinned across dozens of distinct pseudo-versions, suggesting inconsistent dependency resolution or vendoring drift across the codebase rather than deliberate multi-version support. Finally, no vulnerability scan data is included in this SBOM, so this report should not be read as a security assessment — a follow-up scan against a vulnerability database is recommended before drawing conclusions about risk exposure.

## Ecosystem Breakdown

| Ecosystem | Entries | % of Total |
|---|---|---|
| golang | 921 | 98.8% |
| github | 9 | 1.0% |
| npm | 1 | 0.1% |
| maven | 1 | 0.1% |

## License Breakdown

| License (SPDX) | Entries | % of Total |
|---|---|---|
| BSD-3-Clause | 390 | 41.8% |
| Apache-2.0 | 342 | 36.7% |
| MIT | 180 | 19.3% |
| MPL-2.0 | 21 | 2.3% |
| BSD-2-Clause | 16 | 1.7% |
| ISC | 4 | 0.4% |
| CC0-1.0 | 1 | 0.1% |
| GooglePatentClause | 1 | 0.1% |
| UPL-1.0 | 1 | 0.1% |
| CC-BY-SA-4.0 | 1 | 0.1% |

## Version Sprawl (Top 10)

| Package | Distinct Versions |
|---|---|
| pkg:golang/golang.org/x/sys | 64 |
| pkg:golang/golang.org/x/tools | 53 |
| pkg:golang/google.golang.org/genproto | 38 |
| pkg:golang/golang.org/x/net | 38 |
| pkg:golang/cloud.google.com/go | 23 |
| pkg:golang/google.golang.org/api | 23 |
| pkg:golang/google.golang.org/grpc | 21 |
| pkg:golang/golang.org/x/crypto | 19 |
| pkg:golang/github.com/golang/protobuf | 18 |
| pkg:golang/google.golang.org/protobuf | 14 |
