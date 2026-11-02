# Fresh audit: Brown eight-deletion obstruction

Verdict: **PASS**, same-family review, provisional acceptance. No mathematical
gap or counterexample was found. All 23 obligations in `PROOF_SKELETON.md` are
discharged within the stated finite-graph scope.

For every simple undirected graph G on the 57 labelled vertices of the fixed
Brown graph B plus a new vertex, maximum degree at most 8 and diameter at most 2
imply at least nine net Brown-edge deletions. The number of added old-old edges
equals the number of deletions. The new proof excludes exactly eight deletions;
the checked dependency excludes at most seven. This gives no obstruction for
nine or more deletions and no nonexistence theorem for arbitrary order-58 graphs.

## Review provenance and authorized scope

Fresh reviewer task: `/root/proof_review_brown8`. The parent reports that the
spawn request accepted `gpt-6-astra`, reasoning effort `ultra`, with
`fork_turns=none`. This records requested/accepted configuration; no independent
backend model or reasoning attestation was exposed. No distinct numeric agent
identifier was exposed. The review is OpenAI same-family and remains provisional;
it is not a cross-family acceptance or a Lean theorem.

The project-local `proof-checker` skill and root `AGENTS.md` were read. Inputs
were the new eight-deletion proof, its extension and Brown57 proof dependencies,
`brown_eight_delete_facts.py`, its JSON, `brown57.py`, and the explicit edge list.
No prior review verdict was read. No source proof or computation was modified.
The requested overrides suppress hashes, TeX/PDF/HTML, wiki writes and heavy
search. Only audit files in this directory were written.

## Main reasoning checks

**Regularity and triangle budget.** A vertex with degree at most seven has
radius-two ball of size at most 57, so a putative G is 8-regular. Its 232 edges
include exactly eight new-vertex edges; therefore its old induced graph has
224 edges, just as B does. At a vertex of G, each triangle consumes two of the
56 outward incidences from neighbors. The radius-two bound 58<=65-2t permits
at most three triangles. Every I vertex must therefore lose at least one of its
four old triangles, irrespective of arbitrary added edges.

**Exhaustiveness, proof lines 48--62.** Since each old edge belongs to at most
one triangle, eight deleted edges destroy at most eight distinct triangles.
Covering I gives 3a+b>=21, while a+b<=8; hence a is seven or eight. The a=8 case
contains exactly one deletion in each of eight distinct III triangles. For
a=7, choosing one deletion in each of the seven distinct III triangles leaves
one edge. The four edge classes II,CE,IE,EE exhaust the edge list. If that extra
II edge belonged to a new III triangle, it would be case A, so case B correctly
restricts it to an already selected triangle.

**Resource accounting, lines 31--46.** At s in S, the degree equation is
number of added old-edge incidences = d_s + indicator(s in C) - 1. Thus sigma
counts incidences, not distinct edges. There are exactly j+e members of C
outside S. A member not covered by a surviving old edge needs an added edge
from S, and distinct uncovered C targets require distinct edges/incidences.
An added edge inside S consumes two of the budgeted incidences but reaches no
new vertex outside S. An edge from S to a new I target uses one incidence.
Therefore subtraction of the missing-C budget is valid for arbitrary additions,
including S--S additions, overlaps, and additions that serve no needed target.
These cases only waste resources and cannot violate the upper bounds.

**Case A, lines 64--76.** Twenty-four III incidences cover twenty-one I vertices,
with multiplicity at most two, giving exactly three repeated triangle vertices.
Deleted-edge endpoint repetition is a subset of that repetition. With no E
deficit, e=0 and old S-C coverage is zero. C requires j additions, while sigma
is at most j. Equality forces all selected I to have deficit two and j<=3.
Their two surviving I neighbors plus themselves cover at most 3j<=9 I points.

**Case B, lines 78--88.** With no IEE triangle destroyed, the seven selected III
triangles partition I. Their chosen edges form a matching. The distinct extra
edge in one of those triangles shares exactly one endpoint with its base edge.
There is just one possible spare incidence; the C requirement forces j<=1 and
uses the whole budget when j=1. The selected I then has two lost II edges, so
covers at most three I vertices. The j=0 boundary cannot reach I either.

**Case C, lines 90--102.** There is at most one deficient E, with no spare
incidence, and at most one spare incidence on C. The deficient E lost a C
neighbor, so it covers at most one C by old edges. Consequently C needs at least
j additions, j<=1, and the I bound 4j+3e+sigma-j is at most seven.

**Case D, lines 104--130.** One destroyed IEE triangle can account for only one
I vertex; the seven III triangles cover at least twenty, hence have at most one
repeated vertex. Base edge repetitions are bounded accordingly. The exact
identity sigma=sum d_i^0+epsilon-j remains valid when the I endpoint of the
extra IE edge had base deficit zero. That endpoint can be selected precisely
because the extra edge gives it positive deficit; the formula does not assume
d_i^0>=1 on every selected I. Thus sigma<=2, e<=1, and C coverage forces j<=3.
The reachability expression reduces to
4j+2e+epsilon-max(0,j-e), at most thirteen. In the branch j<e, one has
j=0,e=1 and necessarily epsilon=0, so the quoted bound two is correct.

**Case E, lines 132--148.** The same triangle argument gives at most one base
repeated endpoint. There are at most two deficient E vertices and at most one
spare incidence, so j<=e+1<=3. EE deletion preserves their three I neighbors.
The expression 4j+3e-max(0,j-e) is at most seventeen for j>=e and at most ten
for j<e. Both are strictly below twenty-one.

**Imported <=7 obstruction.** Rechecked the full five-step proof. Coverage of
the twenty-one I vertices forces r>=7. Equality forces seven disjoint III
triangles and a deletion matching on fourteen I vertices. Every available
deficit is then one, so selected S vertices have no added old-edge incidence.
Reaching the C vertices forces S=C, which cannot reach I in two steps.
Therefore r>=8, and the new proof yields r>=9 without circular dependence.

## Finite evidence and counterexample attempts

`independent_finite_check.py` reads the supplied edge list without importing or
executing the provided generator/checker and writes no source files. A run under
`timeout 30s` used one Python process and completed in approximately 0.022 s.
Its output is `independent_finite_check.json`.

- The list has 224 distinct normalized edges on 57 vertices and matches the
  F_7 orthogonality rule exactly. Degree counts are 8 vertices of degree 7 and
  49 of degree 8. Every unordered pair has distance at most two.
- The C/I/E sizes, all neighbor counts and triangle premises are verified.
  There are 42 II,56 CE,84 IE,42 EE edges, with precisely the stated triangle
  containment. Every I belongs to two III and two IEE triangles.
- All 3432 seven-III subsets and 3003 eight-III subsets were inspected for the
  coverage reductions. The only seven-subsets covering at least twenty I
  vertices are two partitions covering all twenty-one; there are fourteen
  eight-subsets covering all twenty-one, each with three repeated vertices.
  The stronger seven-subset fact is not used to fill any proof gap.
- Small integer enumeration independently confirms the relaxed C/D/E coverage
  maxima 7,13,17. This verifies arithmetic only, not existence of extremizers.
- Adversarial boundary cases checked symbolically: zero selected I; zero
  selected E; the extra IE endpoint absent from all base deletion endpoints;
  repeated triangle vertices omitted by a base edge choice; S--S additions;
  added S-C edges whose C endpoint is already in S; and overlapping old I
  neighborhoods. None produces a counterexample. Upper bounds either remain
  equal or become looser in these cases.

There are no open FATAL, CRITICAL, MAJOR or MINOR issues, no verified
counterexamples, no source fixes, and no changes to assumptions. Analytic
interchanges, probability modes and asymptotic uniformity are inapplicable.

## Remaining mathematical scope

The complete graph-class problem, the existence or exclusion of Brown
extensions with at least nine deletions, and a Lean formalization remain open.
The deterministic finite computations are reproducible checks of local premises
and arithmetic; semantic acceptance of the paper argument is provisional.
