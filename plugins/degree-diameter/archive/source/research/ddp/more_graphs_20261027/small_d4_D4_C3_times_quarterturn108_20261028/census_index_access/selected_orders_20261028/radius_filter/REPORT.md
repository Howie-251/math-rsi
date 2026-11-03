# Complete selected quartic Cayley census filter

**All69 selected members were processed:23,619 simple4-regular literal graphs,23,619 root0 target-radius failures, zero passes, zero positive graphs, and zero untested graph records.** The frozen existence prediction is refuted. The worker process used4.182995 CPU seconds and its driver0.001692075 seconds, below the45-second aggregate allowance; no compilation or solver was used. Session83084 exited0 and has no live handle.

|Target|Current bound|Orders|Members|Graphs checked|Radius failures|
|---|---:|---|---:|---:|---:|
|degree4, diameter3|41|42..53|12|671|671|
|degree4, diameter4|104|105..161|57|22948|22948|

The downloaded69 members total9318753 uncompressed bytes. Each graph line was decoded exactly once for the actual filter, with its vertex count bound to the filename order, no loops or repeated edges, all degrees exactly4, and exactly2n edges. Every physical graph line reached by each completed member is accounted for in[MEMBER_RECEIPTS.json](MEMBER_RECEIPTS.json) and[CASES.jsonl](CASES.jsonl). ZIP metadata does not provide a separate expected graph count per order, so those external counts remain null; this result uses complete member bytes and complete line parsing, without inventing an independent count.

The custom sparse6 decoder follows the installed NetworkX implementation's padding rule: stop when x>=n or v>=n. The first literal graphs at orders42,108 and128 were compared once with NetworkX, giving exact adjacency matches across short/extended order encoding and a power-of-two boundary. This calibration performed zero graph-distance checks. See[PARSER_CALIBRATION.json](PARSER_CALIBRATION.json). The actual negative filter performed23,619 root-radius traversals, not zero BFS. The legacy source_BFS=0 counter means no re-audit of an old baseline graph over all roots; it excludes this explicitly counted catalogue work.

A missing target from one root rules out the requested diameter without relying on vertex transitivity. Every graph failed that test, so no all-root positive validation or exported candidate was necessary. Negative exact global diameters and ordinary bad-pair totals remain null. In particular, the23,619 failures count catalogue graphs, not unordered vertex pairs.

## Inherited completeness and consequence

Evans-Potocnik's [A census of Cayley graphs](https://arxiv.org/abs/2512.05406) and the[authors' census site](https://graphsym.net/) state completeness for connected simple quartic Cayley graphs through order1025. The selected members come from their[official sparse6 archive](https://atlas.graphsym.net/Cay4val/Cay4valUpTo1025.zip). The published completeness claim is inherited, rather than established by this project. See[ANALYSIS_SCOPE.md](../ANALYSIS_SCOPE.md) and the earlier[LITERATURE_SCOPE.md](../../../LITERATURE_SCOPE.md).

The degree4 Moore bounds are53 for diameter3 and161 for diameter4. Degree at most3 has the smaller bounds22 and46. Thus any Cayley graph improving41 or104 in these two cells must occur in the selected quartic order intervals. Conditional on the published complete census and these complete literal receipts, no Cayley graph can improve either current bound. This neither rules out general non-Cayley graphs nor gives a new classification theorem or an exact Cayley extremum below the current general bounds.

The downloader made the authorized exact-member requests and the separately authorized single repair of order110. Its[merged COMPLETE_DOWNLOAD receipt](../DOWNLOAD_RECEIPT.json),[original partial receipt](../INITIAL_BATCH_RECEIPT.json) and[one-member retry receipt](../RETRY_110_RECEIPT.json) preserve that history. The filter made no network request. The two previous explicit order108 groups were not re-enumerated; the census's order108 file was processed only as part of this newly authorized complete catalogue filter.

The appropriate research decision is to stop small-group quartic Cayley searches for these two cells and use the census conclusion when choosing later mechanisms. General graphs remain outside this exclusion. No further groups, orders, solver calls or audit layers were started.
