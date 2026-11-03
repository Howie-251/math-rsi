# Rebuild and representation

Use the original `formal/` project, pinned Lean4.24, existing cached imports and
saved FORMAL_ENV_COMMAND.json LEAN_PATH. compile.py invokes the pinned binary
with-j1 and child CPU entry/exit subtraction. No lake dependency resolution,
installation, upgrade, hashes or old-source/cache rebuild is performed.

New generic order: OppositeIncidenceSpreadSlots→Family→independent genericAudit.
These import the unchanged generic graph/Walk/slot/lower modules originally
proved during6160; they do not import the6160 numeric graph or its finite data.
The generic final interface is conditional; it does not assert geometry exists
for arbitrary a,b. The concrete caller must discharge all hypotheses.

Concrete order: OppositeGQ44SpreadDefinitions→Incidence→InputInterface→85 rows
00..84→Inputs→Exact→independent OppositeGQ44SpreadAudit. Initially rows00/84 were
compiled serially for actual costs3.849872/6.374317CPU; then83 remaining modules
ran as a single bounded3-j1 batch. Original typed source bodies were retained;
there was no flat-array redesign or recompile of successful rows.

All input geometry is literal PARAMETERS data. linePoint and pointLine are
85×5 typed vectors from the start; spread17 and owner85 are typed vectors in
original order. Input incidence is literal finite membership. Every supplied
numeral is in its Fin bounds, so no modulo encoding changes the data.
The arbitrary old-label equivalence preserves old85*p+l exactly; new j is7225+j.

Projection rows use original6800 nonincident(q,m) witness records and425 trivial
incident choices(q=p,m=l). Each pair becomes3Fin5 indices. Shared pointLine_sound
supplies p∈m; q∈target is definitional; one point equality certifies q∈m.
Kernel reduction proves all7225 actual point-line obligations. No witness file
validity assumption remains in the final theorem and no graph BFS is used.

Budget1000CPU includes the previously completed6.322335CPU generic substage;
generic modules had60CPU limits, concrete modules115CPU. Bounded row dispatch
monitors aggregate CPU with20CPU reserved for final assembly, stops new work on
first failure, and never automatically retries. All per-module/aggregate handles
and receipts are saved. The final receipt reports measured Lean child CPU.

check_binding.py is a separate external source readback: exact850 incidence
values,17 spread IDs,85 owner indices,425 ordered pin labels with original new
indices, plus direct formula equality to all90525 literal edges. It does no
shortest-distance traversal and is not an ASCII-parser theorem or independent
candidate acceptance. Independent acceptance is under ../independent_acceptance/.
