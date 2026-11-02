# Actual GQ80 paired-matchings interface and a C5-symmetric next model

This is a paper/read-only task. It generates no field, geometry, matching, graph, BFS, solver model or Lean proof. Earlier bounded solver windows remain terminal UNKNOWN; no old timer or seed is resumed.

## Actual inherited source and older scope

The canonical entry is `research-wiki/experiments/ddp-wave11-gq80-paired-matchings.md`. Its original source/model proof is `research/ddp/breadth_20261027_wave11/gq80_paired_matchings/REPORT.md`; the exact model and schema are saved beside it. The source is the W(3,3) symplectic quadrangle:40 points P,40 lines L, four incidences per point/line,160 incidence edges, incidence-graph diameter4 and girth8. Its actual coordinates use omega(x,y)=x0*y1-x1*y0+x2*y3-x3*y2 over F3. The old source generation, collinearity/design checks and cached point/line lists are inherited, not rerun.

Add a perfect matching M_P of P and a perfect matching M_L of L, retaining every incidence edge. The proposed graph would be5-regular on80vertices with200edges. All mixed point–line pairs already have incidence distance1 or3, and same-side collinear/concurrent pairs already have distance≤2. Thus only the540 unordered far pairs per side need new routes.

The unrestricted original model has1560 individual within-side edge variables,80 matching equations and1080 exact far-pair clauses. Its original15-second MILP and the subsequent overlap-cut/direct-CNF/girth-five/local-budget windows all ended without an incumbent or exclusion. In particular the later45-second configured overlap call was terminated by its process CPU bound without a returned solver result; it is not a completed exhaustive45-second NO. The exact accumulated history is retained by the canonical entry and source owner's new read-only gate.

The previous girth-five paper and global-budget identities are inherited from `research/ddp/more_graphs_20261027/small_d5_D3_gq80_route_overlap_cuts_20261028/girth5_cnf_20261028/ANALYSIS_GIRTH_SCOPE.md` and `.../girth5_local_budget_cnf_20261028/ANALYSIS_GLOBAL_ROUTE_BUDGET.md`. The old a_x≤3 and sums/five-cycle identities are not rediscovered as a new method here. The source/history owner found no existing common-C5 matching experiment in the five original code/model/report windows; their symmetry constraints were empty. No actual order-five matrix or label permutations were located in the cache, so the compressed numeric instance still needs that new small binding before execution.

## Exact route classification

Write C(x) for the closed old same-side collinearity/concurrency set; it has13 elements. Let I(x) be its four opposite-side incidences. For distinct same-side x,y, all walks of length≤3 have either zero or two incidence steps. With zero incidence steps, the walk stays in the unique same-side matching: M^2=id and M^3=M. Three matching steps therefore cancel to the direct mate and supply no new endpoint.

With two incidence steps, the one matching step is first,last or middle. Hence the only additional same-side route types are

M I I,  I I M,  I M_opposite I.

In particular for a far point pair x,y (and dually for lines), distance≤3 holds exactly when

M_P(x) in C(y), or M_P(y) in C(x), or
there are L in I(x), N in I(y) with M_L(L)=N.

The closed C convention correctly includes a direct mate: if M_P(x)=y, it is already in the first/last families. The original individual-edge clause contains13+13-1=25 own-side variables and4*4=16 opposite-side variables, hence41 distinct variables. The matching equations plus all1080 far clauses are necessary and sufficient for diameter≤3, not merely necessary route counts. They already cover cooperation between the two matchings. Nothing justifies demanding that the own-side matching cover all far pairs alone.

## Noncollinear matching is a restriction, not WLOG

A point matching edge joining collinear points closes a triangle with their unique old joining line. Dually a concurrent line matching edge closes a triangle with its intersection point. There are no other triangle types, since a matching alone has no cycle and an incidence-only source has girth8.

Thus forbidding all collinear/concurrent matching edges is exactly a triangle-free restriction. It is not established as a necessary condition for an80-vertex diameter-three completion. Adding the old mixed-rectangle clauses further imposes girth≥5. Those are legitimate explicitly restricted subfamilies, but their UNKNOWN results do not replace the unrestricted question. The new C5 model below should initially retain the collinear/concurrent blocks rather than silently imposing this old restriction again.

## An unrestricted root budget that permits, but tightly organizes, triangles

This is a direct paper consequence of the exact route families, not an independent new construction method or a claim that the original integer-feasible set changes. It uses the inherited fact that |C(u) intersect C(v)|=4 for every two distinct same-side vertices, whether they are collinear or far.

For any root x on one side, put y=M(x). Define

- i_x: the number of own-side matching edges with both endpoints in C(x);
- j_x: the number of opposite-side matching edges with both endpoints in the four-element pencil I(x).

The27 old far targets are outside C(x). The matching-first endpoints are A_x=C(y) minus C(x), exactly9. The matching-last endpoints are B_x=M(C(x)) minus C(x), exactly13-2*i_x: each internal C(x) matching edge uses two of its thirteen images.

For the middle-matching routes, an incident opposite object paired to another member of I(x) contributes no far endpoint. Each such internal pair accounts for two of the four objects. Every other matched opposite object is nonincident to x and, by the GQ unique-projection property, has exactly three old far neighbors. Thus the relay multiset has exactly12-6*j_x occurrences. Repeated endpoints may further reduce its support; they must not be counted as independent coverage.

Consequently D3 necessarily satisfies

27 ≤ 9+(13-2*i_x)+(12-6*j_x),
2*i_x+6*j_x ≤7, equivalently i_x+3*j_x≤3 because the latter sum is an integer.

So i_x≤3, j_x≤1, and j_x=1 forces i_x=0. In that tight case x's mate y is far, both A_x and B_x contain y, and the total occurrence count is28. Complete coverage requires that y be the sole repeated occurrence: A_x intersect B_x={y}, while the six relay endpoints are distinct and disjoint from A_x union B_x. This is a precise, falsifiable complementary-routing prediction; a single extra overlap defeats that root. It is not assumed that some root must have j_x=1.

Every new triangle is either x's own collinear-mate triangle or one of the j_x opposite-matching triangles. An own collinear mate already makes i_x≥1, whereas j_x=1 requires i_x=0. Together with j_x≤1, this shows that in any D3 completion **all triangles must be vertex-disjoint**, not necessarily absent.

There is also a useful block-count consequence. Every selected own matching edge lies in C(x) for exactly four roots, so sum over40 roots of i_x=20*4=80, with no triangle-free assumption. Each concurrent opposite-side matching edge contributes one to j at its unique intersection root. Since j≤1, these roots are distinct and have i=0; all other roots have i≤3. If c is the number of such concurrent opposite matching edges, then80≤3*(40-c), giving c≤13. The dual bound holds for collinear point matching edges.

These constraints may already be consequences of the existing exact rows and earlier cuts. Their value is to organize a new symmetric generation model, not to count a new theorem or to infer an80-vertex witness. The old girth-five a_x budgets alone do not provide this unrestricted triangle classification; there j_x was already zero by assumption.

## A genuinely different bounded model: common C5 invariance

Let A be an actual order-five element of Sp4(F3), preserving the exact cached alternating form. Existence of order-five elements follows abstractly from the standard group order; this is not an actual matrix/label binding. Since3 has order4 modulo5, the nontrivial fifth-cyclotomic polynomial is irreducible over F3. A nonidentity order-five linear action in dimension4 therefore has no invariant proper nonzero subspace. It fixes no projective point and no2-dimensional isotropic subspace. Thus both the forty point and forty line labels split into eight free5-orbits, once a literal A and its induced incidence-preserving permutations are bound.

Now restrict both matchings to commute with this common C5 action. This is an additional family restriction, not WLOG for arbitrary paired matchings. Within a single5-orbit an equivariant matching would be a shift r with2r=0 mod5; only r=0 is possible, which is a forbidden loop. Therefore each matching pairs the eight orbits into four orbit pairs. For every unordered orbit pair there are five equivariant shifts, giving C(8,2)*5=140 block variables per side. Eight orbit-degree equations select exactly one block incident with each orbit. The two sides together give280 binary variables and16 matching equations, exactly encoding all matchings in this C5-invariant family.

The action on unordered far pairs is free: a nonidentity element fixing a two-element set would act on it via a homomorphism C5→S2, which is trivial, so it would fix both individual points, impossible. Hence each side's540 far pairs has108 orbits, or216 far-clause orbits in total. For one representative per orbit, substitute each original individual matching-edge variable by its block variable, set within-single-orbit matching edges false, and deduplicate the remaining positive block IDs in the41-variable OR. Incidence and matching invariance make this representative clause exact for all five orbit members.

Deduplication applies to a positive OR clause. If importing an existing **linear** overlap/counter inequality, substitute edge variables and add their coefficients within each block instead. A block selects five linked edges, not five independent choices; deleting multiplicity coefficients from a counting inequality or treating repeated block literals as independent edges changes its meaning. No old girth-five-only inequality may be imported without its extra hypotheses.

The unrestricted triangle budget gives symmetry-compatible optional valid cuts. A block is entirely collinear/concurrent or entirely far, because A preserves incidence. Its five edges then contribute five triangles or none. The c≤13 bound makes at most two selected collinear blocks possible per side. Moreover each triangle-block uses two same-side vertex-orbits and its unique opposite intersection/join orbit; selected triangle-blocks must have disjoint such vertex-orbit supports. These are consequences of D3 and preserve any feasible C5-invariant paired completion. They permit triangles and avoid incorrectly treating triangle-free as WLOG.

## Selected next step and stopping boundary

The proposed next change is the common-C5 orbit-block model with all collinear/concurrent blocks retained, the exact216 orbit-cover clauses, and only valid triangle-disjointness/block-count consequences. It is not another time extension of the old1560-variable model, and not a list of unrelated templates. Before any numerical call, one actual symplectic order-five matrix and the two literal40-label permutations must be newly bound to the cached geometry. The expected280/16/216 dimensions are conditional until then; no actual compressed model or matching is generated by this paper.

A positive matching pair would still require a full actual80-vertex graph and fresh D3 acceptance. A negative compressed model would close only the chosen C5-invariant family, leaving arbitrary paired matchings open. A timeout remains UNKNOWN. No old45-second production process, seed, encoding or solver is resumed here. Graph/parameter/Lean counts stay unchanged.
