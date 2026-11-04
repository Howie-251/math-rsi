# Scoped independent finite-input audit and proof review

Date: 2026-11-01. Reviewer task: /root/t15_sameface_zero_audit.
ARIS proof-checker applied. **same-family / provisional** semantic assurance.
This dedicated report does not change a global proof state or closure ledger.

## Verdict

PASS relative to the explicit imported T44_5 theorem. The exact scoped
statement is: for every arbitrary complete-graph matching on Q5 with six
holes of parity type 1+5, every specified two majority holes may be omitted
in a short-new-edge 30-cycle, provided some coordinate cut contains all six
holes in one face and has zero required matching crossings.

The nonadjacent branch is proved directly from this audit's Q4 finite
certificates. The adjacent branch imports T44_5 with every hypothesis
discharged by adding a short edge between two nonforbidden holes.
This does not establish full Q5 T15 or full P6.

## Independent deterministic evidence

T15_SAMEFACE_ZERO_CROSSING_check.py imports no producer and no previous
checker. It independently generates all 945 matchings of the ten covered
vertices in each of four residual families, checks unique exact coverage,
and validates every positive path's support, root, endpoint, mandatory edges,
and new-edge shortness. All 3780 records and 22260 positive paths pass.

Exactly 210 triangular records give four listed endpoints and contain all
four vertices at distance three from the root. All 3570 other records give
the entire six-element allowed odd endpoint set. These are positive lower
sets, so the proof does not require certifying nonlisted endpoints as bad.
All four record histograms agree with the generation metadata. The C++
producer is hashed and read for format only, not trusted for coverage or
proof validity. Its search completeness is immaterial to these positive
witness conclusions.

The checker independently partitions all 560 marked root-zero hole
geometries: 520 have an available neighboring majority hole, and the other
40 split uniquely into four coordinate-permutation orbits of sizes
12,12,4,12. The common automorphism on both faces transports arbitrary
long matching edges and preserves both omitted labels. Translation covers
every root and either minority parity.

The Q4 perfect endpoint input is independently rederived from the two
complete opposite-hole tables. Their 270270 distinct valid matching rows
cover both 13!! universes; all 270166 positive circles pass. Each of 104
negative rows has every disjoint complementary short perfect matching
enumerated and every resulting 2-factor checked disconnected. All 5824
negative inverse instances produce 4708 distinct candidate perfect
matchings; their entire forward bad-endpoint rows agree with the saved
JSON. The maximum bad count is four, and the minimum good distance-three
count is one. Outside the inverse universe only the root's odd partner
can be bad. Thus the finite exceptional audit has a proof of universal
coverage, not merely agreement with an unproved saved list.

## Semantic obligations and hypothesis discharge

1. **Actual cut implies a perfect B matching:** zero required crossings and
   absence of B holes leave every B vertex matched internally, including
   arbitrary long and same-parity internal edges.
2. **Adjacent reduction:** choose b among the three nonforbidden majority
   holes, require a--b short, and add it. The resulting matching has exactly
   four same-parity holes, still including both forbidden vertices. T44_5
   applies on Q5. The added ab edge is short relative to the original input.
3. **Residual orbit reduction:** all three available majority holes are
   nonneighbors of the minority root, so in Q4 they are three weight-three
   vertices after translation. The coordinate action realizes precisely the
   four audited families and is applied identically on the two faces.
4. **Endpoint compatibility:** nontriangular A lower sets have size six;
   B has at least four good odd endpoints in a universe of eight. Their
   intersection has size at least two. Triangular A lower sets contain all
   four distance-three endpoints; B has at least one of these. The proof
   uses both B bounds. A size-four bound alone would be insufficient for
   the triangular case.
5. **Two distinct short bridges:** q has parity opposite to root 0, hence
   q is distinct from 0. Face supports are disjoint. The bridges join
   corresponding vertices, so both are cube edges regardless of the shared
   local automorphism or the original cut coordinate.
6. **One simple 30-cycle:** traversing the A path, the q bridge, the B path
   backwards, and the root bridge is an explicit cyclic order on exactly
   the 14+16 retained vertices. All required edges lie on the paths and all
   other edges are short. Both prescribed forbidden holes lie outside it.
7. **No cycle-obstruction misapplication:** the old triangle obstruction
   concerns an A cycle. Here A is an open path rooted at the minority hole;
   its root has only one path edge. All triangular path records are checked
   directly, so the obstructed A-cycle theorem is not invoked.

There are no analytic inequalities, limits, probability modes, asymptotics,
or parameter-dependent constants. The only inequalities used are finite
set cardinalities, with their common eight-element universe explicit.
The dependency DAG is acyclic: Q4 finite data and imported T44_5 feed this
scoped gluing lemma; neither depends here on unrestricted T15 or P6.

## Counterexample pass and boundary checks

The review specifically tested the possible gaps: triangular A inputs;
an omitted distance-three vertex; coincidence of the two bridge endpoints;
a bridge attached at a forbidden vertex; odd/even minority reversal;
long and same-parity required edges; saved-negative incompleteness;
nonexceptional perfect matchings; duplicate and missing certificate rows;
and disconnected glued 2-factors. The explicit hypotheses, direct finite
checks, and cyclic traversal discharge these concerns. In the triangle
case both omitted vertices are neighbors, so no distance-three endpoint
used there is forbidden.

No counterexample was found to the stated scoped result. Dropping the cut
or zero-crossing hypotheses would be an unsupported scope extension: this
proof would then lose its perfect B matching or its decomposition of all
required edges into the two internal paths.

## Imports, assurance, and open obligations

The T44_Q5_CLOSURE_DRAFT.md theorem is imported only for the adjacent
subbranch. Its reviewed draft hash is checked against the current file and
its saved review verdict is PASS; this package does not rerun the full T44
proof or all of its dependencies. Its same-family/provisional assurance
propagates to the scoped theorem. The independently validated data may be
treated as deterministic checks, but semantic acceptance still requires a
cross-family overlay for stronger assurance.

This audit is the independent delegated input audit; the accompanying
scoped proof was written during the audit. No additional fresh subreviewer
or cross-family semantic overlay was invoked in this task. The parent
review may independently inspect that proof. This limitation is recorded
without misrepresenting the current review as cross-family acceptance.

Open: all other Q5 T15 branches, including any unhandled positive-crossing
cases and hole geometries without such a face; full P6. No global status,
prior result file, original certificate, or existing checker output is
edited. Reproduce only the dedicated checker and inspect its dedicated
JSON for the complete declared input hashes and finite evidence.
