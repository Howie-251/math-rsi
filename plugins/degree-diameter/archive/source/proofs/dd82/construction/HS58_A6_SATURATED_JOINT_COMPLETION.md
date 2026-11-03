# Joint completion of the 56 saturated no-cross a6 cores

Date: 2026-10-12. **CHECKED_UNSAT:** the entire 56-template saturated
no-cross a6 domain has no completion, with the full auxiliary graph and
all ports variable. This is a new input built from the finite
saturated-core reduction, rather than a restart of the previous broad
addition-count input or a query about the failed seed's palettes.

## Exact scope and finite old-core domain

Fix the standard HS50 Q and D={01,10-11}. Consider an eight-regular
58-vertex extension of Q-D with exactly six original-nonedge old
additions, in which all four deletion endpoints have two new neighbors.
The proof in
[HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md](HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md)
puts every such addition set into four zero-set cases and 56 labeled
six-edge matchings. Its separate no-cross deletion-orbit normalization
allows the result to be transported to other no-cross D; this query
itself fixes D in the stated coordinates.

Each zero set contains 25,26,35,41 and one alternating half of each
listed eight-cycle. The two additions 25-26 and 35-41 are forced.
The remaining edges are arbitrary bijections between the selected
T0/T1 cells and between the selected T10/T11 cells. Their sizes give
24,4,4,24 matchings in the four cases.

The source generates exactly those 56 templates. A separate property
and count pass within the preparer checks against actual Q neighborhoods
that each is a matching of six original nonedges avoiding the deletion
endpoints, its twelve endpoints are Q-independent, and every partner
pair has opposite deletion-neighbor cells under tau=(0 1)(10 11).
It also checks four zero sets, 56 distinct addition sets, and counts
24,4,4,24. Distinct admissible matchings reaching the factorial count in
each case give the entire stated domain. All templates are saved in
`hs58_a6_saturated_joint_run/addition_domain.json`.

The prior complete degree-correct graph with 89 bad pairs is retained
in `hs58_a6_saturated_seed_run/seed.json`. It supplies a concrete failed
object in this old-core domain; none of its port labels or auxiliary
edges is imposed on the joint query.

## Variables and exact constraints

There are 56 old-core selectors, 34 indicators for the union of all
possible old added edges, all 400 old-new incidence variables B[x,a],
and all 28 auxiliary edge variables H[a,b]. The selectors choose exactly
one template. Each added-edge indicator is equivalent in both directions
to the disjunction of selectors whose templates contain that edge.
All original HS edges outside D are fixed present; D and all other
old nonedges outside the template union are fixed absent.

At old vertex x the exact-degree constraint is

\[
\sum_{e\in A:x\in e} A_e+\sum_a B[x,a]=1+d_D(x).
\]

At new vertex a it is

\[
\sum_x B[x,a]+\sum_{b\ne a}H[a,b]=8.
\]

Thus the four deletion endpoints have exactly two ports, the selected
twelve zero vertices have none, and every other old vertex has one.
There are 42 old-new incidences. Summing the new degrees forces
2|E(H)|=64-42=22, hence eleven auxiliary edges; no H catalog is used.

For each unordered vertex pair x,y the coverage formula is exactly

\[
E(x,y)\ \lor\ \bigvee_{z=0}^{57}(E(x,z)\land E(z,y)).
\]

Here E is the corresponding fixed edge value, addition indicator,
port variable, or auxiliary edge variable. A variable conjunction is
defined by the standard three clauses for equivalence to an AND.
Fixed false terms are removed and fixed true paths discharge a pair.
The 1,199 pairs already covered by fixed retained HS edges are recorded
in `encoding.json`; the remaining clauses cover 26 old-old, 400 old-new,
and 28 new-new pairs. These counts sum to all 1,653 pairs.

All cardinality constraints use the existing bidirectional unary
threshold recurrence in the project's archived `n62_ab_cnf.py` helper.
This reuses a CNF utility only; no n62 mathematical restrictions or
n62 computation are involved.

The sole normalization is

\[
d_H(0)\ge d_H(1)\ge\cdots\ge d_H(7).
\]

It is encoded as implications between exact degree thresholds.
Any candidate admits a permutation of its eight new labels with this
property. The old-core domain does not reference new labels, so sorting
cannot remove a candidate. No specific degree sequence, endpoint
palette, zero-row color, neighborhood inequality, or other obstruction
is imposed.

## Candidate preservation and decoding

Given a target in the stated scope, the saturated-core theorem supplies
one of the 56 selectors. Set its addition indicators, sort the new
labels by H degree, and take B and H from the graph. Its degree and
diameter conditions satisfy the exact sums and every pair clause.
Threshold and AND variables extend this assignment by their definitions.
Therefore an UNSAT certificate for this input excludes every target
in the stated saturated scope.

Conversely, any satisfying assignment selects a genuine six-edge old
matching, has precisely the fixed two HS deletions, and defines a simple
58-vertex graph. Exact degrees give 232 edges and degree eight everywhere;
the coverage clauses give diameter at most two. The runner expands the
full edge table if SAT and invokes the independent edge-list BFS verifier.
The code does not assume that a satisfying CNF model is already a
verified graph.

## Actual input and bounded run

Source: `computations/dd82/construction/hs58_a6_saturated_joint.py`.
All artifacts are under
`computations/dd82/construction/hs58_a6_saturated_joint_run/`.

The actual CNF has **10,699 variables and 35,325 clauses**. Preparation
used 0.084942 CPU seconds and 0.092802 wall seconds. `encoding.json`
records complete variable maps, all fixed HS edges, the discharged pair
list, counts, and scope; `input.cnf` is the exact solver input.

One CaDiCaL run is authorized, pinned to one CPU, with 180 CPU seconds,
8 GiB address space, and a 768 MiB proof-file limit. SAT triggers expanded
graph verification; UNSAT triggers the independent `lrat-trim --no-trim`
checker. UNKNOWN or a resource limit ends this query without a restart.
The single solver run returned UNSAT after **25.221077 CPU seconds**
and **25.325460 wall seconds**. Independent `lrat-trim --no-trim`
returned exit code 20 and `s VERIFIED`, using **1.111608 CPU seconds**
and **1.167755 wall seconds**. Therefore `result.json` reports
`CHECKED_UNSAT`. The exact proof is `proof.lrat`; solver and checker
outputs are `solver.log` and `certificate_check.log`.

Together with candidate preservation above, this excludes every target
in the fixed-D saturated a6 scope. The already established no-cross
deletion normalization transports that result to every no-cross
deletion pair with all four endpoints saturated. The query does not
constrain or exclude unsaturated endpoint patterns. There was no
second run, enlarged budget, new H catalog, or additional search.
