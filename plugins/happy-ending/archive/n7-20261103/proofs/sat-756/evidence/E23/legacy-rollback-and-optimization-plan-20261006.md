# Legacy restoration and revised optimization proposals

Date: 2026-10-06, UTC+8. Scope: restore the original working encoder and
propose experiments; no new long SAT benchmark is launched.

## Completed restoration

The September 27 compact implementation was additive. The original
`lib/erdos.py`, `lib/downset_state_cnf.py`, `lib/sat_tseitin.py`,
`state_charging/cardinality_layers.py`, and campaign helpers were never
replaced. Twelve relevant source files on both desktop and authoritative
Linux match the original sealed C5 runtime. Its seal SHA-256 is
`8e4d53797b63fa95a983c470358653f111a37eb22db36838650316dcbd1b4d5b`.

The two compact modules and their dedicated test were archived, with hashes,
under [retired-compact-20261006](retired-compact-20261006/manifest.json), then
removed from active `lib/`, `state_charging/`, and `tests/` on both hosts.
The original compact documentation is archived as well; active documentation
now selects the legacy API. Historical compact imports remain available in
their sealed campaign runtimes. No sealed runtime, proof, checker binary or
running campaign was changed. The repaired checker remains in use.

Linux `forktqiu3` verification:

- 29 existing down-set, cardinality-layer and campaign regressions passed;
  zero errors, failures or skips.
- Fresh processes cannot find either compact module in active imports.
- Fresh legacy A[6,9] construction: 515,919 variables / 1,882,748 clauses;
  CNF SHA-256 `8c61ba655bb7da947d0cccfe5b8cfa807ee254300ae2b7003c871305eec3032b`.
- Fresh legacy A[6,10] construction: 593,929 variables / 2,163,502 clauses;
  CNF SHA-256 `2f7d6e765e353a7cd14dd8041328ebfbc3730c56299f2e0c8d1510645c481603`.
- Both hashes and byte sizes exactly match the old-encoding controls.

Evidence: [server source bindings](retired-compact-20261006/server-manifest.json),
[validation receipt](retired-compact-20261006/validation.json),
[test log](retired-compact-20261006/regressions.log).
No new implementation was introduced into the legacy formula builder, so
there is no new Python implementation requiring an additional linter/type
configuration; relevant existing tests and byte-identical regeneration were
used as the rollback gate.

## What the comparison establishes

See [the retained comparison record](c6-legacy-comparison-20261004.md).
Times below are the completed proof-solver stage, excluding generation,
SAT-first, proof hashing and checking.

| Quantity | A[6,9] legacy | A[6,9] compact | A[6,10] legacy | A[6,10] compact |
|---|---:|---:|---:|---:|
| Solve hours | 33.099636 | 35.696538 | 10.778466 | 75.928424 |
| Input variables | 515,919 | 43,359 | 593,929 | 48,041 |
| Input clauses | 1,882,748 | 352,965 | 2,163,502 | 403,047 |
| Conflicts | 182,545,763 | 241,442,922 | 67,426,427 | 409,902,304 |
| Decisions | 584,055,992 | 686,794,390 | 229,458,913 | 1,185,541,087 |
| Propagations | 421,800,384,136 | 295,558,731,307 | 170,318,908,977 | 574,787,131,026 |
| Peak RSS bytes | 602,607,616 | 92,098,560 | 384,073,728 | 93,478,912 |

Compact took 1.078457 and 7.044456 times the legacy solve durations. Both
A[6,10] proofs and compact A[6,9] passed checking; legacy A[6,9] checking
was still running at 11:53 UTC+8. This restoration does not grant independent
theorem acceptance.

CPU closely matches wall time in all four solves. Compact reduced memory,
but no memory-capacity bottleneck was demonstrated for these legacy runs.
A[6,9] compact performs fewer propagations yet more conflicts/decisions and
takes longer: even a smaller propagation total is not an adequate objective.
A[6,10] compact has about 6.08 times as many conflicts and a lower conflict
throughput. These are search-effort proxies, not counts of distinct triple
colorings or directly comparable mathematical search-space cardinalities.

The previous change simultaneously altered packet gates, outer-path
definitions, state/occupancy variables and counting. The comparison cannot
identify a single causal culprit. In particular, semantic equivalence does
not imply equivalent unit propagation, learning vocabulary, preprocessing,
branching, or proof length.

## Preserve inexpensive semantic structure

Fresh A[6,10] legacy clause-group counts are:

| Group | Clauses | Share of full CNF |
|---|---:|---:|
| Two outer-path layers | 1,362,396 | 62.97% |
| Signotope packet expressions | 657,720 | 30.40% |
| Down-set state layer, including exact terminal recurrence | 138,430 | 6.40% |
| Weak-target layer | 4,108 | 0.19% |
| Supplemental exact e/m counters | 848 | 0.04% |

Do not remove the state interface and both small counters as the first size
optimization. `S[v,H]` gives a named exact state, `O[H]` exposes occupancy,
and the original per-vertex one-hot constraints already exist. They allow
learned clauses to express mathematical obstructions succinctly.

For A[6,10], all ten exceptional `O[H]` are forced true by the old counter.
For A[6,9], exactly one is false. Compact's vertex-only count entails the
same type coverage through injection, but does not expose those type-level
facts as direct counting consequences. Losing this shortcut is a hypothesis
worth isolating, not an established explanation of the regression.

## Candidate 1: direct state-to-path pruning bridges

Start from the unchanged legacy formula and add an optional clause group.
Let `C(u,a,b)` mean that the down-set of vertex u contains cell (a,b), and
`B_l(u,v)` / `R_l(u,v)` be the **exact terminal-pair** predicates for a
blue/red path of l vertices whose last two vertices are u,v. For u<v:

```text
C(u,a,b) => B_(a+2)(u,v) OR R_(b+2)(u,v)
```

Proof: the cell has a common terminal predecessor w<u supporting a blue
path of a+1 and a red path of b+1 ending at (w,u). The color of (w,u,v)
extends one of them. Forbidden blue-5/red-6 terms are false and are omitted
at a=3/b=4, respectively. This yields clauses of width at most three, with
no new variables. At most `12 * binomial(N,2)` clauses are needed: **4,872
at N=29, 5,220 at N=30**, before deduplicating boundary units.

These clauses bypass chains through extension witnesses and disjunctions.
The earlier compact bridge option used this mathematical relation, but the
production compact runs had bridges disabled. The proposed experiment adds
it to the **legacy** baseline as a single isolated change. It is a low-cost
first candidate; runtime improvement remains unmeasured.

## Candidate 2: make ordered state incompatibility explicit

A stronger form of injection is

```text
u < v  =>  H(v) is not a subset of H(u).
```

Here subset is componentwise comparison of the three row heights, not an
arbitrary order on state IDs. To see this, let a+1 and b+1 be the maximum
blue/red path lengths ending at (u,v). The cell (a,b) lies in H(v). If it
lay in H(u), Candidate 1 would extend a path beyond one of these maxima,
a contradiction. Hence it witnesses H(v) minus H(u). This argument uses
the path bounds and exact down-set meaning, without assuming the desired
C6 theorem or using the target UNSAT result.

Possible isolated variants:

1. Add only explicit all-different clauses `not S[u,H] OR not S[v,H]`.
   The existing one-hot clauses compare **different states at one vertex**;
   these compare **the same state at different vertices**. At N=30 this is
   15,225 binary clauses and no new variables.
2. Add every ordered forbidden pair:
   `not S[u,G] OR not S[v,H]` whenever H is a subset of G and u<v.
   The 35-state catalog has 490 ordered comparable pairs including equality;
   this gives **198,940 / 213,150** binary clauses at N=29/30. This roughly
   10% increase over the old CNF must earn its cost through reduced search.
3. First add selected long-distance pairs or domain units, then measure
   whether the full family adds useful propagation. Do not combine all
   variants in the first benchmark.

An immediate domain consequence: the full rectangle `(4,4,4)` can appear
only at the last vertex. Since A[6,10] requires every exceptional state,
it forces `S[N,(4,4,4)]`. This removes state/placement branches before
color branching, without deleting any vertices or weakening the formula.

For a state H at position v, earlier states must be outside its upper set,
and later states outside its lower set. Necessary domain conditions include
`v-1 <= 35-|Up(H)|` and `N-v <= 35-|Down(H)|`. Refine these by exceptional
and ordinary availability: if e exceptional and N-e ordinary states are
occupied, the predecessor capacity is at most

```text
min(e - is_exceptional(H), |E outside Up(H)|)
+ min(N-e - is_ordinary(H), |O outside Up(H)|).
```

Use the analogous lower-set bound for successors. Violating a necessary
capacity gives a unit `not S[v,H]`. These bounds are deductions, not
assumptions that relabel arbitrary vertices as symmetric.

The general derivations above require separate encoding and regression
checks before production use. An independent direct-path enumeration checked
both the bridge relation and ordered non-containment on **all 1,024 five-point
and 1,048,576 six-point colorings**, filtering only the blue-5/red-6 bounds.
All **896 / 516,096** retained colorings passed, without requiring signotope
or weak-target constraints. See the [bounded-check receipt](retired-compact-20261006/pruning-bounded-check.json).
This is a small-order mathematical sanity check, not a solver benchmark or
a stand-alone certificate for every order. It does not validate an as-yet
unimplemented optional CNF group.

## Candidate 3: compress local expression gates, keep exact path semantics

Retain exact outer paths (both directions), terminal paths, state/occupancy
interfaces, explicit one-hot clauses and both old counters. First change
only the six signotope implications per quadruple from private Tseitin
conjunction gates to their six direct ternary clauses.

The current packet group has 24 clauses per quadruple. Direct encoding
reduces it to six. At N=30, this reduces the packet group from 657,720 to
164,430 clauses, saving **493,290 clauses**, about **22.8% of the entire old
CNF**, without deleting state-level facts or reverse path definitions.
At N=29 the analogous saving is 427,518 clauses.

This exact local truth-table rewrite is a much narrower size experiment than
the retired compact package. It is still not guaranteed faster: removed
gates may have helped learning or preprocessing. For clean ablation preserve
unchanged semantic variable IDs/iteration order where practical and record
renumbering. Evaluate post-preprocessing size, not only generator output.

Only after this isolated test consider flattening private AND/OR chains in
path recurrences. Preserve exact witness support and reverse implications;
do not repeat wholesale conversion to one-way closure markers. Mixed
exact/one-way path families need their own projection proof and lifting.

## Candidate 4: strengthen counting and domains instead of replacing them

Keep the exact 10-type exceptional and 25-type missing-ordinary counters.
Test adding a redundant exact vertex counter `sum(F_v)=e`, where each F_v
already means an exceptional exact state. Injection makes this counter
entailed. Local path facts could then propagate through vertex capacity while
type occupancy propagates through the existing counters. This adds work per
propagation and must be measured independently.

For stronger variants use small, structured state-domain capacity cuts. If
k vertices can only use k remaining types, those types are unavailable to
other vertices; fewer than k types is a contradiction. Start with prefix/
suffix regions and the ordered incompatibility above. Do not enumerate all
Hall subsets or all five-missing-ordinary masks (`binomial(25,5)=53,130`).
For dynamic conditional domains, encode the implication and its support;
never turn a conditional domain reduction into an unconditional global unit.
Generic GAC results motivate this direction but do not establish GAC for
the proposed state encoding. [Bacchus, GAC via Unit Propagation](https://www.cs.toronto.edu/~fbacchus/Papers/B-CP2007.pdf)
describes how alternative CNF representations can expose stronger propagation.

## Candidate 5: small mathematical case decomposition

For A[6,9], branch on which of the ten exceptional types is missing. Exactly
nine occupied types makes these **ten disjoint, exhaustive** branches; fixing
the one missing type propagates the other nine occupied types. A[6,10] has
one such mask, so this split gives it no gain. For that cell, derive the
forced full-state endpoint before considering any placement split.

This is a semantic reduction within each case, not just increasing process
parallelism. Measure **total CPU, hardest branch, proof-check cost and total
proof volume** against the monolithic solver. Ten jobs can duplicate learned
work and be worse. Each branch needs a fresh bound proof and explicit cover
verification; no single branch proves the original cell. Do not delete an
endpoint and equate the remaining coloring with a smaller registered cell:
deletion changes path states and requires a separate reduction theorem.

## Proposed next experiment order and acceptance gate

1. R0: restored unchanged legacy baseline.
2. R1: R0 plus Candidate 1 bridges only.
3. R2: R0 plus ordered-state domain units / all-different, separately from R1.
4. R3: R0 plus packet-only compression, separately from R1/R2.
5. Test full ordered incompatibilities or dual counting only after the
   cheaper candidates; combine individually successful changes afterward.

Correctness comes first: analytic entailment/projection proofs, nonvacuous
small-order tests with independent path/state recomputation, and proof-bound
fresh exports. An UNSAT query against an already UNSAT full C6 cell alone
does not demonstrate that a proposed pruning clause is a valid local theorem.

Screen propagation using matched partial triple assignments and exact shared
predicates. Count shared facts forced, contradictions found and propagation
cost. This screening is diagnostic and cannot predict complete solve times.
Then run paired seeds (for example 0,1,2) with the same AE binary, proof mode,
cell and controlled resources. Use both A[6,9] and A[6,10], plus a separately
chosen held-out cell. Short/censored runs are not completed timing wins.

Record original and post-preprocessing variables/clauses, wall and CPU time,
conflicts, decisions, propagations, peak RSS, learned-clause information when
available, proof bytes, checker time and final checked result. Promote a
variant based on complete solve/check cost across the chosen cases/seeds,
with any regression stated. Do not replace the baseline based on clause
count, initial throughput or one favorable seed.

This objective agrees with published observations that encoding size alone
is unreliable: [Wynn's cardinality-encoding comparison](https://arxiv.org/abs/1810.12975)
found markedly different behavior across representations and little runtime
effect from some added clauses. [Haberlandt, Green and Heule](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SAT.2023.11)
show that useful auxiliary structure can matter beyond formula-size
reduction. These papers motivate hypotheses; they do not predict a speedup
for this project's proposed variants.
