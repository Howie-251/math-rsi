# Prepared single-point acceptance interface — not run

The global full-neighborhood clone attempt supplied no new center set.
The earlier fullclone checker remains unused. This interface is for a
different rule: retain the actual accepted16416 source, and attach one
new vertex16416 to a set S of at most16 currently available old pins.
It does not require S to be any frozen complete neighborhood.

Only ROOT may start the new data suite after observing a complete actual
candidate and assigning a fresh CPU budget. No candidate, pin list or graph
has been parsed during this preparation. No acceptance PASS is created.

Future entry:

```
python verify_single_extension.py \
  --source /absolute/repo/research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/graph_d16_D4_n16416.edges \
  --candidate /absolute/new-case/graph_d16_D4_n16417.edges \
  --pins /absolute/new-case/actual_pins.json \
  --out /absolute/new-case/independent_acceptance \
  --cpu-budget ROOT_ASSIGNED_SECONDS
```

Pins input is an integer list or `{"pins": [...]}`. The source and candidate
have `n m` headers and strict lex `u<v` bodies. The checker reads each edge
file once, binds all129240 old edges, exactly S new edges, no other changes,
all pointwise degrees<=16, and sourcedegree(pin)<16. It never imports the
searcher's coverage masks.

The only BFS runs are on the new final candidate: newZ to all16416 old
targets, then one preselected old root0. The newZ predecessor tree yields
OLD_R3_PARENT_DEPTH.tsv in the OLD source and proves the generic
SingleExtension radius3 premise. The old source D4 is inherited from the
already accepted concrete kernel; old-old pairs need no repeated suite.
The single old0 measurement supplies a real distance4 witness. This is
not the fullclone case: no collapse homomorphism is asserted for arbitrary S.

The old42343 all-source verifier and the old650 radius-coverage template
were read as references only. Neither is invoked; especially no old source,
all-root, field, Lean or remote review is run. The prepared code has not
been executed or runtime-tested; actual checks belong to the future budget.
If no16417 candidate is produced, the interface stays unexecuted.
