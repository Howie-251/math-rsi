# C9 with length-three secant chords: three positive classes, but a uniform T-root obstruction

The three declared positive coverage guarantees are **VALID**. The complete construction nevertheless cannot have D3, because one point in the full T fibre reaches at most eight of the nine E vertices within three steps. This is a paper obstruction for every allowed A-S shift and eligible port completion in the stated rule. No geometry/label binding, INPUT, CNF, decoder, SAT call, chosen graph, or BFS was produced by the new producer before preparation stopped; see [PREPARATION_STATE.json](PREPARATION_STATE.json).

The proposal and chronology are in [PREDICTION.json](PREDICTION.json). The proof below does not assume an ungenerated new vertex-label map. It uses the proposed abstract indices i modulo9 and the retained A/S incidence structure.

## Rule and degree bookkeeping

Retain the twelve A-S base-edge C3 lifts and the nine S-S matching pairs. Choose the absolute base point T=8. Every S-S pair contains exactly one endpoint whose base is adjacent to T; orient it as s_i-s'_i with s_i on that T side. The old class sizes remain12 A,18 S and9 E vertices. The concrete proposal fixes the three base S-S matchings to identity and allows the12 A-S edge shifts; no claim of gauge completeness for broader rewritten-E rules is needed here.

Replace all E-E edges by a cycle E_0,...,E_8. Reassign all eighteen E-S edges as

    E_i-s_i,   s'_i-E_(i+4),   i modulo9.

Before helper insertion there are36 A-S edges,9 S-S edges,9 cycle edges and18 E-S edges, giving72 edges. A vertices have degree3. Every S has its two old A neighbors, its S mate and one E neighbor, hence degree4. Every E has two cycle neighbors and the two secant incidences s_i and s'_(i-4), hence degree4.

Delete E_0-s_0 and E_4-s'_0. This frees one slot at each of E_0,E_4,s_0,s'_0 in addition to the12 original A slots. Add helpers a-b-c, with a adjacent to E_0,E_4 and one A, b to two A, and c to all three T lifts. The six A spokes leave six A ports. Each freed S takes one eligible A port, and the remaining four A ports form two edges. Eligibility must avoid an already existing A-S edge and respect every port's capacity1.

Thus16 old slots are used by eight helper spokes and four old-old edges. Edge count is72-2+2+8+4=84 on42 vertices, all degree4. These correct degree counts do not guarantee a valid diameter.

This rule genuinely changes the old E-S projection: paired S vertices now lead to E_i and E_(i+4), rather than one old external base fibre. The earlier cross-E triangle-cover obstruction cannot simply be inherited.

## Positive guarantee1: every E-E pair is within3

On C9, distances1,2,3 are already available along the cycle. The remaining pairs have cyclic difference4 or-4. Pair i supplies the length-three chord E_i-s_i-s'_i-E_(i+4). All such chords except pair0 survive the deletion. Pair0 is replaced by E_0-a-E_4, of length2. Hence every pair of the nine E vertices has distance at most3 for all structural assignments.

## Positive guarantee2: c covers all42 vertices within3

Because c is adjacent to the entire three-point T fibre, all nine T-side secants s_i are within2 steps. Their S mates s'_i are within3. All old A vertices are also within3: any two distinct absolute base points share a secant neighbor, so a retained two-edge A-S-A base route lifts bijectively from the full T fibre to every target A fibre. T itself is directly adjacent to c.

For i!=0, c reaches E_i through c-T-s_i-E_i within3. The only removed route of that form is E_0-s_0; c-b-a-E_0 replaces it with another three-step route. The second deleted edge E_4-s'_0 does not remove c's route through s_4. The helper targets a,b are reached by c-b-a and c-b. Thus c's complete radius3 guarantee is valid independently of all remaining shifts and ports.

This is a guarantee for c as root, not a claim that all old roots may use c and still remain within3.

## Positive guarantee3: a covers all E within3

The two cycle radius2 sets are

    R2_C9(E_0) = {E_7,E_8,E_0,E_1,E_2},
    R2_C9(E_4) = {E_2,E_3,E_4,E_5,E_6}.

Their union is all nine E vertices. Since a is adjacent to E_0 and E_4, a reaches that entire class within3. This says nothing by itself about a's remaining A/S targets.

## Uniform negative root: the T lift adjacent to s_0

Exactly one old point t in the T fibre is adjacent to s_0: an A-S lift is locally bijective, and the base T is adjacent to the base of s_0. The root t has exactly four neighbors: s_0, two other T-side secants s_j,s_k, and c. The full T fibre already uses its one added slot on c, so no port completion adds another neighbor to t.

Consider all possible paths of length at most3 from t to E, classified by their first step. Using simple paths loses no shortest route.

* Through s_0: the direct E edge was deleted, and its S mate s'_0 also lost its E edge. The other old neighbor and the newly matched neighbor of s_0 are A vertices, which have no direct E neighbor. Thus this whole branch supplies zero E targets within3.
* Through c: within two further steps, c can reach only A, S or helpers. Its neighbors are T points and b; no A or b has a direct E neighbor. In particular t-c-b-a ends at a, and needs a fourth step to enter E. This branch also supplies zero E targets within3.
* Through either other secant s_i: its direct E_i is reached in2 steps. A third step through E_i supplies its two cycle neighbors. The route through s'_i supplies E_(i+4) in3 steps. The remaining A neighbor has no E neighbor. Hence there are at most four E targets from each of these two branches.

The new E_0/E_4-a edges do not add an omitted route here: if a third step from an already reached E goes to a, the endpoint is a helper, and a further E target would need a fourth step. A port that is attached to a helper cannot also be given another new edge; every new A edge still joins A, S or a helper, never E.

The total number of E targets within3 of t is therefore at most

    0 + 0 + 4 + 4 = 8 < 9.

At least one E vertex is outside t's radius3 ball for every A-S voltage assignment and every degree-legal declared port completion. The identity of t and of a missing E may depend on those choices, which is harmless: the statement is that every graph has some failing old root. It is not a measured count of graph bad pairs.

The contradiction can coexist with all three positive guarantees. The full-fibre helper c may choose a different T starting point for each old target. A particular T point cannot borrow that choice through c in the same three-step budget: its first step to c leaves only two steps, while c's E routes require three.

## Scope, execution, and stop

The joint D3 existence question is excluded for the declared C9/offset4 chord rule, double removal of both E edges of one S-S pair, helper P3, full T attachment to c, two E attachments to a, and the stated freed-S/A completions. The proof uses no specific numeric A-S shifts or special port choice and no pair-index detail beyond the T-side orientation. It does not classify arbitrary42-vertex graphs, other sources, single-endpoint deletions, different helper attachments, or other relaxations of these premises.

The preliminary a-to-A tight-budget argument is not needed and is not counted as a completed result here. No further necessary-condition chase, compilation, parameter enumeration, or solver follows from this batch. Preparation stopped before any new INPUT/CNF/decoder was generated. Actual target order, exact diameter and ordinary bad-pair totals remain null; this is a strict structural paper exclusion, not a numerical failed graph or solver UNSAT. The overall construction Goal remains open.
