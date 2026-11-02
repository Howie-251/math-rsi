# Independent complete-graph acceptance

This proof is linked to fresh literal-input validation, not producer certificates. The verifier independently implements GF(9)=GF(3)[w]/(w²+1), with code a+3b for a+bw. Its finite field laws and all nonzero inverses were checked. It independently rebuilds controller78 from the explicit three-base Z26 rules and parameters (2,6,17,5,10), then checks equality with the declared controller table. It reads only the declared eight matrices and six directions from the earlier cross-port parameter file; it does not import producer graph-check caches.

## 1. Literal graph and definition agree exactly

For controller dart u,p→v,q, write T for its declared matrix and ell_p/ell_q for the source/target port directions. The vertex labels are 729u+x0+9x1+81x2. Define the neighbors of (u,x) over this dart by

    (v,T*x+t*ell_q), t∈GF(9).

The verifier checks T*ell_p=ell_q, and the reverse dart matrix is the literal inverse of T. Reversing an edge uses noise −t. The six controller neighbors are distinct and exclude u, and ell_q is nonzero. Thus each vertex has exactly 6×9=54 distinct neighbors, the definition is simple and undirected, and it has 56862 vertices and 1535274 edges.

The verifier reads every one of the 1535274 literal edges. It checks valid labels, strict lexicographic order, smaller endpoint first, no duplicate edges or loops, and independently tests the affine formula above on every edge. Every one of the 56862 literal degrees is exactly54. Since the literal relation is included in the formula relation, and both relations have exactly54 neighbors at every vertex, they are equal. This is a complete edge-table binding, not a sampled binding.

## 2. Same/nonadjacent controller pairs

For each actual ordered pair u,v, the verifier recomputes length-three controller words by literal table traversal. All6084 pairs are covered. For the5616 same/nonadjacent pairs, it selects an actual nonbacktracking word with darts p1,p2,p3. Write Ti for the corresponding three actual matrices and qi for reverse(pi). For arbitrary source coordinate x, after three edges the target coordinate is

    T3*T2*T1*x + T3*T2*ell_q1*t1 + T3*ell_q2*t2 + ell_q3*t3.

After applying T3 inverse to the target-minus-center, the noise columns are

    [T2*ell_q1, ell_q2, ell_p3].

Nonbacktracking gives q1≠p2 and p3≠q2. The verifier checks all200 such central-turn determinants for the eight actual chart types and also checks the determinant on each of the5616 selected actual routes. All are nonzero. Over the checked field GF(9), each resulting 3×3 linear map is invertible, so t1,t2,t3 can realize every target coordinate. This argument applies to arbitrary x,y; it requires no coordinate translation automorphism or identity holonomy.

## 3. Adjacent controller pairs

For an adjacent dart u,p→v,q with matrix T, the paths u→a→u→v (a any other source port) yield all offsets in

    span(T*ell_a,ell_q)

from the common center T*x. The paths u→v→b→v (b any other target port) yield all offsets in

    span(ell_q,ell_b).

True inverse matrices cause the first/last backtracking edge pair to cancel its linear center exactly. The independent verifier enumerates the ten planes for every one of the eight chart types and checks their union is all729 offsets. Consequently all468 adjacent ordered controller pairs cover every target coordinate in three actual graph steps. The self-port sign is chosen separately at the actual labeled dart; no deck automorphism is assumed.

Sections2 and3 give a length-three actual graph walk for every pair of vertices, hence diameter at most3. The Moore radius2 bound for degree54 is 1+54+54×53=2917, which is less than56862. The diameter is therefore exactly3.

## 4. Falsifiable predictions and direct checks

PRED.md predates execution. All its local-rank, inverse, pencil and controller predictions were supported. In addition, the verifier tested806 distinct literal BFS roots: all729 coordinates in controller0 and coordinate0 in the other77 controllers. Before each BFS it independently generated the formula radius2 ball and predicted the four distance-class sizes. Each literal BFS exactly matched that prediction and reached all56862 vertices by distance3. Detailed rows are in BFS_PREDICTION_VS_ACTUAL.csv; the distribution of histograms is in BFS_HISTOGRAMS.tsv.

This is806 literal roots, not all56862 roots. The all-pairs conclusion rests on the complete finite premises and the argument above. No Lean completion, public novelty, priority or global-record certification is asserted here.

## 5. Execution and limits

TERMINAL.json records the single executable validation batch:1.740401167 measured CPU seconds including input-header preparation, compilation, complete literal validation, BFS predictions/checks and aggregation, below the120CPU cap. All processes terminated. Before this batch, an initial driver invocation failed at path lookup because the controller directory used parents[2] instead of parents[1]; no compiler or validator started. The path was corrected. That prelaunch source-preparation error is outside the measured executable-batch boundary and does not represent a second graph-validation run. There was one actual compile and one actual graph-validator execution. No old graph, solver, install, hash, Lean or repeated BFS audit was run.
