# SBOM Summary Report — ops-master

- **Source file:** `ops-master-cyclonedx-identified.json`
- **Scan timestamp:** 2026-07-13T04:54:23.175Z
- **Report generated:** 2026-07-17T08:17:07.282707+00:00
- **Total component entries:** 932
- **Unique package names:** 363
- **Vulnerability data present:** No

## Overview

This SBOM for ops-master catalogs 932 component entries across 363 unique package names, overwhelmingly dominated by the Go ecosystem (921 golang packages, with only a handful of github, npm, and maven entries rounding out the mix). The license landscape is largely permissive and low-risk—BSD-3-Clause, Apache-2.0, and MIT together account for the vast majority of entries—though a long tail of one-off licenses (GooglePatentClause, UPL-1.0, CC-BY-SA-4.0, CC0-1.0) warrants a quick manual check to confirm none introduce unexpected obligations. Version sprawl is notable: several core Go dependencies (golang.org/x/sys, golang.org/x/tools, golang.org/x/net, google.golang.org/genproto, and others) each carry dozens of pseudo-versioned historical entries, suggesting the SBOM reflects accumulated transitive resolution history rather than a clean, deduplicated dependency tree—this is worth normalizing before drawing conclusions about actual runtime versions in use. Finally, no vulnerability data is present in this SBOM, so this report should not be read as a security assessment; a separate vulnerability scan against these resolved packages is recommended before any risk sign-off.

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
