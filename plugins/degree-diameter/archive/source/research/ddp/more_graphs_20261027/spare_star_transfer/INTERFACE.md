# Reuse on the already-downloaded degree15 source

The source must be a complete, already-bound undirected edge list. Its first line may be "n m" or "# n m"; following lines are the m edges. No new download, BFS or arbitrary coverage search is needed.

Run the existing pure-standard-library interface in the degree15 task's own output directory:

    python research/ddp/more_graphs_20261027/spare_star_transfer/scan.py --source COMPLETE_EDGEFILE --degree 15 --out D15_OWN_OUTPUT_DIRECTORY

The importable function is:

    scan_source(source, degree, out, expected_n=None, expected_m=None, deadline=None)

It scans complete open-neighborhoods only, exports the lexicographically first fullfalse-twin hit if one exists, and saves all prototype labels, actual original neighbor degrees, saturated-neighbor histogram and per-vertex uint8 counts. A no-hit is a complete closure only for this literal rule/current source. A deadline interruption is UNKNOWN.

If the expert's native source profile already holds its edges and degrees, the same exact test can be applied there without parsing the file again. Initialize saturated-neighbor counts tozero. For each edgeuv, incrementcount[v] ifdeg(u)=15 and incrementcount[u] ifdeg(v)=15. Every nonisolatedv withcount[v]=0 is a legal prototype, since allofN(v) hasdegree<15. This is the full test, with no heuristic ranking or R4 calculation.

Any new graph keeps all source edges and adds a vertex connected to the prototype's complete old open-neighborhood; its sourceD5 routes are inherited. Root owns the one first-new-parameter acceptance. Partial download files are not inputs to this completed-source rule. Do not continue by deleting saturated neighbors when the exact rule is empty.
