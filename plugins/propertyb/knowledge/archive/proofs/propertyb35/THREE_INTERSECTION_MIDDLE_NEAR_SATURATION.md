# Three-intersection outer pairs with at least14 common middle edges

## 1. Actual statement

Let H be a simple five-uniform hypergraph on21 vertices, with35 distinct original edges and full point-pair coverage. Let G,J be two original edges intersecting in three points, and put A=G\J={a,b}, B=J\G={c,d}. Assume the four points in A∪B have degree at most9, their six point-pair codegrees are at most4, and at most one of the four points has degree7.

Let c(G,J) count original middle edges F with F∩G and F∩J different singleton sets. **If c(G,J)≥14, then H has Property B.** The actual reduced-A1 role satisfies the degree/codegree hypotheses after its already-proved strong-pair reductions. Consequently every non-B reduced-A1 input has

    c(G,J)≤13 for every three-intersection outer pair,
    C3≤13n3.

This statement concerns original edges of the same H. It does not require every cross-trace edge to be a valid middle edge, or assume a coloring of an unspecified completion.

## 2. The complete necessary near-saturation domain

Use bits0,1 for A and bits2,3 for B. For each trace T⊆A∪B, let μT be its exact original-edge count. The distinguished G and J supply

    μ3≥1, μ12≥1.

Every valid middle has one point of A and one of B and no other selected point: an attachment in G∩J would belong to both singleton intersections and violate their distinctness. Its exact trace is therefore one of the four cross pairs

    5,9,6,10.

Write aij for these four exact counts and t=Σaij. It is possible that a cross edge is not a valid middle because it meets the original common three-set; thus only t≥c(G,J) is claimed. Point-pair codegree at most4 gives each aij≤4, so14≤t≤16.

Each cross row and column has sum at least t−8≥6. Adding its distinguished same-side outer edge shows that each selected point has degree at least7. The actual selected degrees thus belong to{7,8,9}, with at most one7 by hypothesis.

The two distinguished traces consume four selected-point incidences, and the t cross traces consume2t. Since the selected degree sum is at most36, every remaining noncross occurrence together consumes at most

    36−4−2t≤4                                                   (1)

selected incidences. The remaining nonempty trace types are the four singletons, additional copies of A or B, four triples, and the full quadruple. Their costs in (1) are their cardinalities. We retain the individual degree cap9, all six inclusive pair caps4, the selected degree condition, and nonnegative empty count35−Σnonempty μ. This is a necessary relaxation; realization of every retained inventory is not asserted.

The domain has a particularly short independent description. The total cross spare capacity is

    Σcross (4−aij)=16−t≤2.

A triple occurrence consumes two cross-pair slots, and a quad occurrence consumes four. Therefore no quad occurs and there is at most one triple occurrence. Each same-side exact trace is at most3, since at most four residual incidences are available. After choosing the four cross counts, the optional triple, and μA,μB∈{1,2,3}, the singleton counts are uniquely recovered from the actual four degrees; the empty count is then uniquely recovered from35 edges.

There are167 complete labeled inventories:

|Exact cross total t|Labeled inventories|Marked-pair orbits|
|---|---:|---:|
|14|150|30|
|15|16|3|
|16|1|1|
|Total|167|34|

The allowed relabeling group has order8: independently swap the two points within each side, and optionally swap the two sides. It preserves the unordered marked pair{A,B}. Degrees are transported with the points and the full inventory; they are not held fixed while a different degree's counts are moved into a label. Canonicalization compares the transported degree tuple and then the transported inventory. This gives a legitimate original-H relabeling even when the four degrees are unequal.

## 3. Exact strict certificates and original coloring

Use the existing [conditional permutation probability theorem](../PROBABILITY_LEMMAS.md). For each of the34 representatives, RESULT.json saves a fixed four-lock layout and its exact rational bound

    Σ_{k=1}^{21}min(Ak,Bk,Ck−lk).

The remaining17 vertices are uniformly permuted without replacement. Ak and Bk count original edge endpoint events; Ck bounds the same critical ordered distinct original-edge pairs through their trace types. Point-pair coverage provides the link-overlap quota ceil((4di−20)/3), namely3,4,6 for degree7,8,9. Every selected singleton trace has count at most2, so all pure singleton quotas are zero; only the total quota is used. It is paid with the least nonnegative bidirectional weights among unused actual incident unordered edge-pair slots, preserving each original pair's finite capacity.

All34 certificates are strict:

|t|Maximum bound|
|---|---:|
|14|88204/109395|
|15|1349/2145|
|16|250309/437580|

Thus the uniform maximum is88204/109395<1. The conditional permutation theorem supplies an actual original-H permutation with no greedy failure. Its algorithm starts all red and processes the vertices in that permutation, turning the current vertex blue when it is the last vertex of an edge still wholly red. Outside the bounded critical event, every original edge contains both colors. This is a proper coloring of H itself, not merely of the trace representative.

Given actual G,J with c≥14, their exact inventory lies in the complete domain of §2. Relabel it to its marked-pair representative, use that fixed layout on the same actual H, and invoke the strict bound. This proves the statement in §1.

## 4. Independent completeness and arithmetic checks

The evidence directory is [a1_middle_near_saturation_20261020](../../context/propertyb35-paper/round01/middle/a1_middle_near_saturation_20261020/REPORT.md). All JSON and script filenames below refer to this directory.

GENERATE.py enumerates only the15 possible four-cross count vectors with total14..16, then recursively allocates the at most four residual selected incidences among the11 noncross trace types. It applies the actual degree and inclusive-pair conditions and groups by the marked-pair action. It does not generate free vertices or H.

VERIFY.py does not import GENERATE or SubsetEngine. It starts with each degree tuple in{7,8,9}^4 containing at most one7, chooses the cross vector, uses the independently proved no-quad/at-most-one-triple representation, chooses the two same-side counts, and recovers singleton/empty counts. All167 full keys agree exactly with the discovery domain. It separately constructs the order8 group by three binary choices and verifies all34 transported representatives.

Finally it expands each representative into35 distinct original edge indices and invokes a different implementation of the no-replacement injection probabilities. For each saved fixed layout it checks1190 ordered distinct edge-index pairs,21 rows and all quota deductions, obtaining the same rational bound. VERIFY.json is PASS. Runtime is about0.46 CPU seconds for discovery and0.32 for the independent complete domain/replay. There is no H, q2-general-core or negative-layout enumeration.

These are same-family/provisional mathematical and deterministic checks; new designated cross-family review is separately controlled by the main project. This theorem is a separate extension of the shared-middle criterion; its underlying saved evidence is unchanged.

## 5. Actual payoff and exact remaining objective

The completed gate justifies C3≤13n3 in the same two-flip calculation. Keeping the already-proved shared budget P≤(132n1+594)/5 gives the stronger actual non-B necessary condition

    494n3+1175n4−313τ≥21538.

The coefficient follows by replacing the C3 multiplier15 by13: L becomes5016n1+2520n2+4368n3+3192n4+7128, then substituting the original A1 intersection moments and dividing by24 with upward integer rounding. With the separate [n4≤11 theorem](TWENTYONE_A1_BALANCED_STAR_FOREST.md), this gives445τ≤4546+561n4 and henceτ≤24. These inequalities do not close A1.

TARGET.py uses exactly the prior common-P/threshold-degree relaxation, changing only a hypothetical uniform C3 multiplier. Monotonicity permits complete filtering of its219 saved15-cap survivors; no excluded profile can return at a smaller cap. Results are:

    multiplier15/14/13/12/11/10/9/8/7
    survivors 219/135/80/48/26/13/7/2/0.

Only multiplier13 is newly justified by this gate. The smaller multipliers remain hypothetical targets, not theorems. Thus this gate alone does not eliminate the whole necessary domain. The full80 surviving13-cap profiles are in RESIDUAL_CAP13.json; their minimum n3 is22 and minimum n3+n4 is33. A minimum-high aggregate witness is

    n=(32,522,8,22,11), τ=0, Pupper=13208,
    C=(0,12686,192,286,44), L=2735352≥2722720.

This is an aggregate relaxation witness, not an H. Purely lowering the uniform cap would need7 to eliminate this particular entire relaxation. Proving c≥8 always repairable would enter much larger incidence-defect domains and can introduce selected six-degree points; it is not a justified continuation of this at-most-four-defect proof. No t≤13 domain has been generated. A further common capacity that prevents simultaneous saturation of the C2/C3/C4 and P bounds is an alternative exact obligation, rather than an invitation to continue uniform-cap tables without a new argument.
