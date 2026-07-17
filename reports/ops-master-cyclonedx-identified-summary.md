# SBOM Summary Report — ops-master

- **Source file:** `ops-master-cyclonedx-identified.json`
- **Scan timestamp:** 2026-07-13T04:54:23.175Z
- **Report generated:** 2026-07-17T11:24:59.473766+00:00
- **Total component entries:** 932
- **Unique package names:** 363
- **Vulnerability data present:** No

## Overview

This SBOM for ops-master catalogs 932 component entries covering 363 unique package names, and the footprint is overwhelmingly Go-based, with 921 golang packages against only 9 github, 1 npm, and 1 maven entries — a dependency graph dominated almost entirely by the Go module ecosystem. The license mix is largely permissive and low-risk, led by BSD-3-Clause, Apache-2.0, and MIT, though a handful of one-off licenses (GooglePatentClause, UPL-1.0, CC-BY-SA-4.0, CC0-1.0) appear only once each and warrant a quick legal glance to confirm they don't conflict with distribution terms. Version sprawl is notable and worth flagging: core Go dependencies such as golang.org/x/sys, golang.org/x/tools, golang.org/x/net, google.golang.org/genproto, google.golang.org/api, and google.golang.org/grpc each appear in a dozen-plus to several dozen distinct pseudo-versions, suggesting transitive dependency accumulation over time rather than deliberate pinning, and consolidation could reduce both audit overhead and drift risk. Finally, no vulnerability scan data is present in this SBOM, so no security posture conclusions can be drawn from this report alone — a separate vulnerability assessment should be run before this is treated as a complete risk picture.

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
