# Local proof and finite-coverage check: false twins / f9 C7

Parent run: dd82-v3-f9-c7-20261013-0749. Date: 2026-10-13.
Reviewer: /root/cyclic_lift58_60; review_independence: same-family;
acceptance_status: provisional. The scoped local check found no unresolved
proof or coverage issue. Gemini review belongs to the parent workflow and
is not claimed here.

This applies the project-local proof-checker to the V3 mathematical task:
actual theorem hypotheses, reduction completeness, implementation and one
independent complete-graph check. Paper formatting, HTML, hashes, new review
agents and shared-wiki changes are omitted under the explicit V3/task scope.
This is not a second research experiment or a re-enumeration of the domain.

## Inputs actually read

- proofs/dd82/construction/FALSE_TWINS58_EIGHT_SIX_FIBERS.md, all sections.
- proofs/dd82/construction/CYCLIC7_EIGHT_ORBITS58_SEED.md, fixed-layer proof.
- computations/dd82/construction/false_twins58_f9_domain_prepare.py and its
  existing complete result.json.
- computations/dd82/construction/false_twins58_f9_coverage.py, complete source,
  and actual coverage_run/result.json and candidate.best.parameters.json.
- The saved candidate.best.edges, read by the independent BFS implementation
  described below. No matrix or generator routine is imported into it.

## Load-bearing obligations checked

1. **Regularity and false-twin saturation.** At order 58 the radius-two bound
   1+8d forces degree eight. The false twins have B_uv=7, exactly the full
   nonnegative row budget. This forces their eight common neighbours S to
   be independent and every remaining vertex to have exactly one S parent.

2. **Eight six-fibres.** Each parent uses two twin edges and six remaining
   edges. The seven other S vertices exhaust its B budget, forcing its own
   fibre independent and precisely one neighbour in every other fibre.
   The resulting 28 interfaces are perfect matchings; no unmentioned
   internal or extra-parent edges remain.

3. **Exact converse.** All pairs except those in different six-fibres are
   automatically covered by a parent, twin, or identity/matching route.
   For different fibres the displayed direct matching and six intermediate
   fibres enumerate every route of length at most two. Each K_ij has row
   and column sums seven, making K_ij>=J equivalent to K_ij-J being a
   permutation matrix. Necessity and sufficiency concern the same full graph.

4. **f9 structural import.** The order-seven fixed graph is K1,8; seven
   nonfixed orbits must receive eight leaf attachments, with exactly one
   doubled attachment. Its two leaves are false twins. Their common
   neighbourhood is h plus the doubled seven-orbit. The fibre of h consists
   of six individually fixed leaves; the other seven six-fibres are cycled.

5. **Simultaneous coordinate normalization.** Labelling each outer vertex
   by its unique fixed-fibre neighbour makes all seven hub interfaces I.
   These labels are preserved by the order-seven action, so outer interfaces
   depend only on cyclic difference. This is a relabelling, not an extra
   restriction. Three arbitrary S6 permutations supply all interfaces.

6. **The four coverage matrices.** The row-source convention applies P_e
   first, then P_(d-e), so array composition is ps[d-e][ps[e][x]]. All terms
   in the three displayed expansions were checked. Distances 4,5,6 are
   transposes of 3,2,1. Seven translates of each d=1,2,3 fibre pair are
   disjoint unordered pair sets, justifying the sevenfold zero-entry count.

7. **Hub normalization loses no target.** F=K_infinity-J is symmetric and
   a permutation matrix. Its diagonal is twice the number of fixing
   permutations, so A,B,C are derangements and F is a fixed-point-free
   involution. Simultaneous conjugation in all eight fibres puts F into
   (01)(23)(45), preserving the normalized hub interfaces and all coverage.
   No residual symmetry or graph-isomorphism quotient is silently applied.

8. **Complete residual enumeration.** Every nonnegative residual has zero
   diagonal and row sum two. Its connected components are double edges or
   simple cycles. A double edge supplies one two-cycle; each longer cycle
   supplies its two orientations, independently. The source enumerates all
   ordered derangement pairs, rejects only negative residuals, and outputs
   every orientation. The complete saved counts are 70,225 pairs, 4,568
   residuals and 10,080 ordered triples. The four possible component types
   2+2+2, 2+4, 3+3 and 6 include every boundary case.

9. **Actual coverage implementation.** It reads 10,080 distinct full
   triples, checks all hub equations, and computes all three outer matrices
   with exact integer route counts. It does not prune by an extra graph
   property. The actual result is complete, with all 10,080 evaluated,
   no targets and minimum 105 bad pairs (288 parameter ties). Each individual
   outer block has zero passing triples. No timeout is used as evidence.

Counterexample-oriented checks focused on shared-parent extra routes,
transpose/composition reversal, fixed points in the hub defect permutation,
double-edge residuals, and simultaneous rather than independent gauge
choices. The explicit hypotheses and constructions resolve these possible
failure modes. There are no analytic limits or asymptotic assumptions here.

## Independent expanded-graph BFS

Source: computations/dd82/construction/false_twins58_f9_independent_bfs.py.
Input: false_twins58_f9_coverage_run/candidate.best.edges.
Output: false_twins58_f9_coverage_run/independent_bfs.json.

The standalone script imports only Python standard-library containers,
paths, JSON and timing. It validates raw edge endpoints, absence of loops
and duplicate edges, reconstructs adjacency sets, then runs a queue BFS
from every vertex. It does not read the permutations or coverage matrices.
Only after BFS completed was its bad-pair list compared to the saved
prediction; all 105 unordered pairs match exactly.

Actual result: 58 vertices, 232 edges, all degrees eight, connected,
diameter three. Unordered distance counts are 232 at distance one,
1,316 at distance two and 105 at distance three. All bad pairs and their
common neighbours are saved. Internal BFS CPU is 0.002198166 seconds,
wall 0.002198257 seconds; this excludes interpreter startup.

The checked example is domain line 704, with
A=(1,2,0,4,5,3), B=(3,5,4,2,1,0), C=(4,0,3,1,5,2).
The independent BFS certifies this complete failed example. Domain
completeness instead comes from obligations 4–9 and the actual complete
finite run, not from checking a single example.

## Exact conclusion and remaining boundary

The local mathematical/computational chain excludes a 58-vertex target
with an order-seven automorphism fixing exactly nine vertices. It does
not exclude the general false-twin eight-fibre family, the order-seven
f=2 branch, or arbitrary 58-vertex graphs. The representation theorem
for arbitrary false twins remains exact, with its larger matching
coverage obligation open. No valid graph above 57 was found.

No source correction was needed. This report is a same-family provisional
review and independent object check, not a Gemini verdict or Lean proof.
