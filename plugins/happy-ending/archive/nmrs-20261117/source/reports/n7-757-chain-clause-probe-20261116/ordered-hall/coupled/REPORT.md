# Coupled red/blue matching and shared-pair-cell relaxation

The free occupancy formula and every c=0,1,2,3,4 branch remain SAT after
simultaneously enforcing 28 red perfect matchings, 28 blue deficiency-at-most-one
matchings, one actual cell per used ordered pair, same-endpoint span weak7
prohibitions, four fixed outer-fan bans, and an independent endpoint-DAG order T.
All six complete assignments pass clause and semantic audits. This is still
a necessary-constraint relaxation; it is not a signotope, a set of actual
monochrome paths, or a counterexample to the original 40-point exclusion.
No external review or acceptance is claimed.

## Blue transpose and matching coverage

For every original boundary word W of size three, define
W'=sort({9-t:t in [8] minus W}), of size five. Its inverse is explicitly
checked for all 56 states. For each original coordinate pair i<j, the
transposed coordinates are 9-j < 9-i. The source side is still B_i minus B_j,
and the target side still B_j minus B_i. Their occupied size m is equal
because every coordinate has degree 15.

The two complementary 25-point covers for actual blue fours have common
part of size 25-m. Since an actual blue-four transversal has size at least
40-16=24, deleting that common part leaves a bipartite vertex-cover lower
bound 24-(25-m)=m-1. König therefore gives a matching of size at least m-1.
The encoding lets each side have at most one unmatched occupied vertex;
every other occupied vertex has exactly one selected edge. Unoccupied
vertices cannot carry an edge or an unmatched flag. If m=0, no edge is needed.

A selected blue edge u->v requires the one shared physical order u<v and
r'=h_(9-j)(u)<s'=h_(9-i)(v), computed from W' with one-based boundary ranks.
Its actual pair cell must have blue coordinate in [r'+1,s']. Every selected
red edge retains its red-coordinate interval [r+1,s]. For each physical
ordered pair, a single one-hot cell from D(v) minus D(u) simultaneously
satisfies every selected red and blue use. Thus the empty label intersections
observed in the preceding layer are now excluded by construction and audit.

For every red/blue use of the same pair, selected spans dR and dB must satisfy
dR+dB<7. Otherwise their same-endpoint paths have total vertex count at least
9 and yield the prohibited weak7. The four fixed pairs are exactly
{123,124} x {578,678}; they cannot carry a selected blue span at least two.
Conditional third-point outer fans are not included.

## Shared endpoint DAG

A separate total order T is placed on the 30 potential states containing
exactly one of coordinates 1 and 8. It is independent of physical time.
Selected pure-A->pure-B red edges of span five are forward in T; selected
blue edges of span three are reverse in T. Transitivity forbids every
alternating directed cycle. On coordinates (1,8), the red perfect matching
and blue deficient matching therefore form one alternating Hamilton path
on all 2(15-c) occupied pure-end states. This graph path is additionally
reconstructed and checked independently in `endpoint-Hamilton-audit.json`.

The inherited occupancy, ideal-order, physical first/last/third roles and
both boundary pure-source inequalities remain enforced. The free coupled
formula has 51740 variables and 211548 clauses.
All runs used controlled external production AE Kissat on Linux `ubun`.

| Profile | c | Outcome | Solver seconds | Early/late boundary counts |
|---|---:|---|---:|---|
| free_occupancy | 4 | audited SAT | 1.118 | [5, 4] |
| c0 | 0 | audited SAT | 1.218 | [5, 5] |
| c1 | 1 | audited SAT | 1.067 | [5, 5] |
| c2 | 2 | audited SAT | 1.719 | [5, 5] |
| c3 | 3 | audited SAT | 1.067 | [5, 5] |
| c4 | 4 | audited SAT | 2.070 | [5, 4] |

The free model's occupied physical order is:

`123 124 125 126 127 134 135 136 145 236 245 246 345 346 137 237 148 247 347 156 238 158 168 257 356 178 248 357 258 267 467 458 368 468 378 567 568 478 578 678`

Its independent alternating endpoint-graph order is:

`156 248 136 258 145 238 135 568 137 368 134 378 123 458 124 468 125 478 126 578 127 678`

These are different mathematical orders. Each full model supplies all
56 physical states, all 28 red matchings and all 28 blue matchings, each
selected common pair cell, and T. Every CNF clause, coordinate degree,
full-side coverage, blue deficiency, inverse transpose, span interval,
common label, same-pair weak ban, fixed fan and DAG implication is checked.

## Evidence, limitations and reproduction

Read `summary.json`, `ledger.json`, each profile's `result.json` and
`model-audit.json`, and `endpoint-Hamilton-audit.json`. Formula and source
hashes are recorded per profile; `MANIFEST.json` binds retained files.
The `.drat` files are outputs of SAT runs and are not UNSAT certificates.
No checker success is claimed for this layer. The previous layer's
fixed-old-occupancy checked UNSAT remains separately bound and unchanged.

The model does not provide actual internal vertices of the required red/blue
path witnesses, all-pair longest-path recurrences, or rank-3 packet constraints.
Matching edges with acceptable cells do not suffice to assert those paths
exist. It remains possible for additional shared realization conditions to
exclude these SAT objects.

Reproduce only on Linux in a fresh sibling copy retaining the preceding
layer's source and formula: run
`/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B build_run.py`.
It solves the free formula and, when SAT, each exact-c branch, using a
600-second process-group limit per solve and optional proof check.
No run reached that limit. Windows performed source edits and SSH/SFTP
transport only. Preserve all completed predecessor and current bindings.
