# Owner-c4 checked finite obstruction and reduced replay

The preferred machine supplement is `reduced/`: CHECKED_UNSAT for a fresh
formula containing only the frozen occupancy constraints, c=4, one owner
of each kind, one common physical order, one red endpoint perfect matching,
and the disjoint C-free owner intervals of at least six occupied points.
It contains no blue matching, endpoint DAG, other 27 red matchings,
historical boundary pure-source filters, third-position roles, six-object
representative conditions, or later slot units. The caller's separate
`reports/n7-owner-intervals-20261116/PROOF.md` now provides a direct mathematical
proof; the finite certificate is supplementary evidence and does not confer
external acceptance on mathematical imports.

| Profile | Actual outcome | Variables | Clauses | Kissat seconds |
|---|---|---:|---:|---:|
| . | SAT_AUDITED_OWNER_CARDINALITY_ONLY | 51764 | 211604 | 1.017 |
| intervals | CHECKED_UNSAT | 83514 | 289379 | 1.268 |
| cheap | CHECKED_UNSAT | 51764 | 211610 | 0.867 |
| reduced | CHECKED_UNSAT | 36743 | 142117 | 0.366 |
| reduced-bare | SAT_AUDITED_REDUCED_RELAXATION | 36743 | 141630 | 0.366 |

All UNSAT outcomes have an actual successful external drat-trim run and
exact CNF/DRAT SHA256 bindings in their `result.json`. The two owner equalities
alone were SAT with all occupancy choices free. The final bare experiment
removed all original 336 chain bans, 120 row clauses, four extreme units and
two literal pairs, plus the 25 redundant same-owner-edge units, and was SAT.
Thus the machine record does not claim that cardinalities and intervals
alone suffice; the preferred reduced proof retains the old occupancy facts.

Preferred CNF SHA256: `6e98aa18204e531f12cebb6f5e3253a21f45342c951d08f9b0c088523bf66253`.

Preferred DRAT SHA256: `4d904fb0fb49a29ac90898acd4a9a62fc13721b1683cc3b6cabfd2e61a23e1c2`.

Read `SOUNDNESS.md` for each actual-object-to-CNF extension, exact owner
state lists, auxiliary semantics, removed dependencies and retained imports.
Read `encoding-audit.json` for exhaustive small auxiliary-extension/truth-table
checks, exact prefix/subtraction checks and independent proof-binding hashes.
These checks ran on Linux, as did all scientific work; Windows only edited,
transported, extracted and hashed artifacts.

`reduced/solver.log`, `reduced/checker.log`, `reduced/formula.cnf`,
`reduced/proof.drat` and `reduced/result.json` are the preferred raw evidence.
The original coupled c4 CNF and every predecessor artifact are unchanged.
Both owner pools were selected freely, not fixed to a previous SAT model.
No external review was invoked, and `accepted=false` is preserved.

For replay, preserve this task's existing parent layout and run Linux Python
`/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B reduced.py` in a fresh copy.
The script reads the original frozen `projected/relaxation.cnf`; its identical
bytes are included as `inherited-occupancy.cnf`. `run.py`, `intervals.py`,
`cheap.py`, `reduced.py`, `bare.py`, and `audit_encoding.py` retain every stage.
Each controlled external solve and proof check has a 600-second process-group
limit; no reported run timed out.

The complete Linux archive retains all profiles including unused SAT-run
proof outputs. `preferred-replay.tgz` contains all source/ledger/result/log
and mathematical-interface documentation plus the complete preferred CNF
and DRAT, without large nonpreferred raw formulas/proofs. The full manifest
states their hashes and remote retention. This separation changes no sealed
formula or proof binding.
