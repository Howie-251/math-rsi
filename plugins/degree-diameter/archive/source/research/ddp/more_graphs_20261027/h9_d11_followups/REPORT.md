# Degree11 finite follow-up batch:37629 ->37630 ->37631

Starting from the independently checked37629 graph, exactly the remaining frozen pool indices4..23 were considered once in the pins-lexicographic order used by complete11.py. Old failed indices0..2 were not revisited and index3 was already used. frozen_pool_order.json records all24 positions and their original source indices.

Two items were accepted:

| pool index | new order | full new-neighbor list |
|---:|---:|---|
| 17 | 37630 | 947,24390,25310,26311,26519,27439,28431,28855,29775,30779,37123 |
| 21 | 37631 | 8261,31641,31791,31850,31924,32071,32135,32172,32315,32372,37345 |

Both use ten mandatory Q-line pins plus one anchor. Every listed pin had degree at most10 in its actual insertion base. Before each insertion, an actual multisourceR4 pass in that current graph covered all current old vertices. Thus each step has a complete single-vertex D5 extension certificate from the previous D5 graph. No intermediate graph was selected by a smaller bad-pair score.

The other18 entries had no exact one-anchor completion on the base present when they were examined. Their failures are not claims about the final37631 base: later additions can change coverage. The batch does not assert maximality or a complete impossibility for all further insertions. There was no second anchor, extra round, return to earlier records or expansion of the frozen pool.

## Exact incremental R4 cache

The old37628 cache was checked against the actual source metadata and complete ascending eligible2504 vertex list. It was then updated after the known37629 insertion and each new accepted insertion. It was not used unchanged as a necessary rejection condition on the larger bases.

Suppose currentG gains z adjacent to S. For an existing available anchor a, let k=d_G(a,S). A shortest path of length<=4 which newly uses z reaches S in k steps, traverses two edges through z, then reaches its old target within2-k steps of S. Hence its new old-target part is exactly R_(2-k)^G(S) when k<=2. Also z itself is in its newR4ball iff k<=3. Thus

    R4_(G+z)(a) = R4_G(a) union R_(2-k)^G(S) when k<=2,
                  also union {z} when k<=3.

No extra old targets arise for k>=3. The new vertex's own ball is {z} union R3_G(S). These formulas remain valid when G contains earlier added vertices; the distances/layers are computed in that actual G. Degree-saturated anchors are removed, and a newly added vertex would be admitted to the available set if its degree were below11. The two actual additions have degree11.

Each positive insertion also received a direct currentgraph R4 coverage check, so the positive witness does not rely solely on this cache implementation. The known37629 starting graph was compared edge-by-edge with its existing independently checked edge table, without repeating BFS.

## Complete objects and verification scope

graph_d11_D5_n37630.edges is the complete accepted prefix with37630vertices/205318edges. graph_d11_D5_n37631.edges is the final complete graph with37631vertices/205329edges, simple and maximum degree11 by producer checks. The original37629 independent artifact is unchanged. parameters.json and accepted_sequence.json contain every literal adjacency addition and geometric witness. generate.py reproduces either acceptedprefix from the original37628source; it refuses to overwrite the protected independently checked/final artifacts.

Only root performs the final strongest all-source BFS. The producer did not perform any all-source BFS on an intermediate graph. Until its independent result arrives, this batch records the complete objects and their per-insertion coverage proofs, not a completed new all-source acceptance for37631.

The fixed20-item batch used 0.513024 CPU seconds on one worker;2positive currentR4 checks plus one initial depth3update were performed. All-source BFS0, solvers0, new seeds0, extra rounds0. The batch is terminal and does not automatically reopen earlier failed entries.
