The concrete new-direction route prediction was supported for both sources. One algebraic search used only controller0, its self-controller arc first, and the prescribed total word lengths3/4. The selected word,p,M,W and predicted counts were saved in ROUTE_COSSET_PREDICTION.json before enumerating any concrete endpoint sets.

| Actual source | First selected controller word | New free direction p | Old canonical v0 | Old endpoints | New endpoints | Intersection |
|---|---|---|---|---:|---:|---:|
|15552, F3^4|0→0→11→46|(0,0,1,1)|(1,2,1,0)|27|81|27|
|102060, F3^5|0→0→90→192→172|(0,0,1,2,0)|(1,2,1,2,1)|81|243|81|

Each comparison uses the same cost3 port sets {0,±p} and {0,±v0}. The selected endpoint form is M*x+W with rank(W)=d−1, M*v0∈W and M*p∉W. Thus the old inputs give one hyperplane coset, while the new inputs give all three cosets and the entire final fibre. Direct enumeration of the certified three-neighbor relation along that one word matched every predicted count, adding54/162 endpoints outside the old word's endpoint set.

For15552, one explicit added route is36→32→918→3729. For102060, the completed-relation route63→63→22016→46709→41797 loses its virtual stay and becomes the actual source route63→22016→46709→41797. Any virtual diagonal stay in these enumerations can be removed, so endpoints are reachable by actual source walks of length at most3/4.

This is an exact same-word complementarity statement. An endpoint outside the old word's set might still be reached from the old ports by another word; no strict inclusion or improvement of their complete R3/R4 balls is claimed. No full-target cover or new graph was produced. Coverage optimization remains the producer's separate task.

The one worker used0.025301759 CPU seconds. It computed no new ball, BFS, solver or graph. Evidence: ROUTE_COSSET_SEARCH_PREDICTION.json, route_cosset_probe.py, ROUTE_COSSET_PREDICTION.json and ROUTE_COSSET_RESULT.json. The last file retains the complete selected-word endpoint sets and literal route witnesses.
