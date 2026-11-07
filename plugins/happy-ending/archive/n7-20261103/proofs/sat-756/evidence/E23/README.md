# Semantic equivalence audit, 2026-09-27

## Result and scope

The proposed architecture preserves the existential projection onto complete
triple colorings, provided counting predicates retain exact definitions and
one-way outer-path witnesses are used only for prohibitions. It does **not**
preserve every assignment to the old auxiliary variables, unit propagation,
model counts over all variables, learned clauses, or existing DRAT files.

The bounded audit passed **46/46** tests: **37 checked UNSAT queries**, **9
independently replayed SAT controls**, and **0 UNKNOWN**. These checks support
the general mathematical argument below; they are not an all-order machine
proof or production acceptance of a replacement encoder.

No production source, C5 CNF, running process, or acceptance receipt was
changed. The only solver runs were the bounded research queries in this audit.

## Exact equivalence claim

For every registered cell, set `N=26+e-r`. Let `x` be a complete assignment
to all triple-color variables, and let `a,b` be the respective auxiliary
variables. The intended contract is

\[
\forall x:\quad
(\exists a\,\Phi^{old}_{r,e}(x,a))
\iff
(\exists b\,\Phi^{new}_{r,e}(x,b)).
\]

This is stronger than obtaining the same overall SAT/UNSAT result twice.
The theorem applies in the existing `(7,5,6)` signotope scope; it is not a
permission to weaken arbitrary consumers of the general `etv` API.

### A. Domain projection

Every actual blue/red path forces its corresponding one-way witness:
length-three witnesses are the signed triple variables; induction on path
length uses appending for blue and prepending for the flipped red family.
Witness-to-outer-endpoint implications then force every actual outer path.
The blue-5/red-6 negative units and the shared-outer-endpoint cap4/cup5
clauses therefore exclude all actual forbidden configurations.

Conversely, given a valid coloring, assign every outer-path witness its
actual path-existence value. All forward rules and prohibitions hold.
The retained outer-endpoint monotonicity holds because signotope packets
allow shortening a monochromatic path while preserving its outer endpoints.
Thus arbitrary choices of unsupported auxiliary witnesses are unnecessary:
every valid coloring has a canonical satisfying extension.

The remaining target pairs in the old no-7 layer involve cap5 or cup6,
already false by their units. Dropping these target assertions is safe.

### B. Exact exceptional predicates

Keep full equivalences for terminal-path recurrence and for

\[
F_v\leftrightarrow
\left(\bigvee_{u<v} B_4(u,v)\right)
\land
\left(\bigvee_{u<v} R_5(u,v)\right).
\]

The blue/red existential choices may have different starting vertices and
different penultimate vertices. Shared right endpoints alone are not the
weak-7 target. Empty disjunctions are false; a two-vertex path is true.

In the 3-by-4 state box, exceptional means bounding width 3 and height 4,
equivalently `h1=4 and h3>=1`. These are precisely the two conditions in F.
This does not require the cell `(3,4)` to belong to the state.

### C. Removing state-type occupancy and the second counter

For `u<v`, the terminal profile `sigma(u,v)` lies in `D(v)`. For every
`t<u`, the color of `(t,u,v)` extends one coordinate of `sigma(t,u)` by at
least one. Thus no generator of `D(u)` dominates `sigma(u,v)`, and
`sigma(u,v)` does not lie in `D(u)`. The states are distinct. The two path
bounds ensure all states lie in the canonical 35-state box.

Consequently the number of exceptional occupied **types** equals
`sum(F_v)`, and the number of occupied ordinary types equals `N-sum(F_v)`.
For a registered cell, `sum(F_v)=e` gives `m=25-N+e=r-1` exactly.

For old-to-new lifting, compute the exact terminal predicates and F from
the coloring, and choose satisfying auxiliaries of the new exact counter.
For new-to-old lifting, recompute the canonical states and occupancy from
the coloring, then choose auxiliaries for the two old exact counters.
Totalizer auxiliaries need not have unique values; only extension existence
is required in either direction.

### D. Short clauses and bridge lemmas

Replacing an isolated asserted `(p AND s) => q` expression by
`[-p,-s,q]` existentially eliminates its private AND gate. Do not drop the
gate definition if another consumer still uses that gate.

For a precisely defined cell predicate, the bridge

\[
\neg C[u,a,b]\lor B_{a+2}(u,v)\lor R_{b+2}(u,v)
\]

follows from the same path-extension argument. B5/R6 are false only because
the corresponding path bounds remain present. Cell predicates must retain
their exact definitions. These bridges are optional entailed constraints.

## What was checked by SAT

For each `N=5,6,7,8,9`:

1. The new base admits a SAT model (nonvacuity).
2. New base plus a violation of the independently enumerated domain is UNSAT.
3. Enumerated domain plus canonical auxiliary definitions plus a violation of
   the new base is UNSAT.
4. Old base plus a violation of the enumerated domain is UNSAT.
5. Enumerated domain plus old definitions plus a violation of an old domain
   assertion is UNSAT.
6. Exact terminal thresholds disagreeing with explicit path enumeration are
   UNSAT, even without domain restrictions on the coloring.
7. New exceptional flags disagreeing with old state-based flags are UNSAT.
8. A violated bridge clause under the old base is UNSAT.

The oracle enumerates complete vertex-subset paths, all forbidden signotope
packet truth assignments, and pairs of paths sharing both outer endpoints.
It does not reuse either encoder's dynamic-programming recurrence.

The old builder's definitions/assertions split is checked by exact clause
multiset equality against a fresh unchanged build. Canonical definitions
extend every coloring by the acyclic path and Boolean definitions; this
existence argument is essential to interpreting tests 3 and 5 as lifting,
rather than mistaking an inconsistent auxiliary extension for equivalence.

At N=7 and N=9, additional proof queries reject every attainable mismatch
in either `e=sum(F)` or `m=25+sum(F)-N`. They use independent exact/upper/lower
cardinality constraints, not the negation of arbitrary totalizer auxiliary
assignments.

Four N=7 controls check old/new exceptional nonvacuity, unsafe one-way
counting, and omission of the weak target. All returned SAT as intended.

All 37 negative queries retain AE DRAT proofs, checked by the repaired
checker with return code zero and exactly one `s VERIFIED`. All nine SAT
models satisfy every query clause; their triple projections were separately
checked for packet axioms, path bounds, weak targets, and distinct states.

## Concrete counterexample to the unsafe variant

On seven vertices, color exactly the triples wholly contained in
`{3,4,5,6,7}` red and all other triples blue.

This is a legal signotope satisfying both path bounds and weak-7-freeness.
Its true exceptional endpoint set is `{7}`. A satisfying assignment to the
one-way outer witnesses can nevertheless make the unsafe flag set `{6,7}`.

Therefore one-way outer witnesses must never feed exact exceptional counting,
path-existence reports, endpoint-start classification, or other consumers
that assume actual path existence. Decode those facts from the coloring or
from separate exact predicates. The audited prototype uses exact terminal
predicates and does not make this substitution.

## Reproducibility and retained artifacts

Authoritative server root:

```text
/data/ktqiu_hdd/math_agent/res/state_charging/20260927_semantic_equivalence_audit_v1
```

The runtime is the immutable C5 snapshot, with `forktqiu3` Python 3.12. Each
AE run has a 20-second internal limit and a 30-second process limit; checkers
have separate limits. Processes run sequentially in owned process groups.

- [audit.py](audit.py): standalone prototype and queries; SHA-256
  `fb46e74be6734571ac77eb0355a887697c73c1a61637f493243c40756b0a21c6`.
- [manifest.json](manifest.json): source, solver, and checker hashes.
- [results.json](results.json): all 46 query results; SHA-256
  `d303ae2528c7b063f8081f80d00f7c664eb668052504220b0ed2f7cb0bf26a37`.
- [summary.json](summary.json): aggregate, scope, and actual prototype sizes.
- [independent_sat_replay.json](independent_sat_replay.json): semantic controls.
- [inventory.json](inventory.json): 317 retained server files, 78,519,075 bytes;
  includes CNFs, DRAT proofs, full models, and logs. The inventory excludes
  itself. Only lightweight evidence was copied locally.

The prototype was actually materialized in memory at N=26 and N=31, without
a production solve: 229,476/457,041 clauses and 30,911/52,741 variables before
the new exact counter. These confirm the earlier static clause budgets.

## Production boundary

No production entry point was changed. Introducing the audited design into
production still requires an explicit new encoder interface, deterministic
variable metadata, semantic model replay that distinguishes exact predicates
from one-way witnesses, and fresh CNF/proof binding under a new campaign seal.
Existing cap/cup consumers cannot silently acquire one-way semantics.

No runtime speedup, C6 result, or new C5 acceptance follows from this audit.
