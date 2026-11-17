# Single outer root26: audited SAT

One default external AE Kissat invocation on authoritative Linux returned SAT
(exit10), wall2.476505804s, CPU2.450296s, maximum RSS43208KiB. The authorized
limits were CPU/wall120s and address space3GiB. The owned process group ended.
No retry, fallback, additional order or proof-checker invocation occurred.

The complete order26 coloring has zero-based selected point **a=5**. Concrete
R6 witnesses are incoming `(0,1,2,3,4,5)` and outgoing `(5,6,9,10,11,17)`.
They meet only at a. All265 actual R6 were enumerated; every one contains a,
and a is the unique one-point transversal. Every190 right-root triple at a
is red. The deletion Y has25 points, local-to-ambient map
`[0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]`,
no actual R6 and recomputed **e=m=2**, with state injection and defect identity.

The full formula has50717 variables and404847 clauses. The solver assignment
is complete; every clause was checked. Color-only checks inspect all2600
triples and14950 packets, recompute red/blue longest paths (6/4), all actual
EndR5 and SrcB4, shared-endpoint color-path sums (maximum8), and the absence
of bad packets, weak7, B5, R7 and the forbidden EndR5/SrcB4 intersection.
All19510 exact recurrence auxiliaries agree with independent subset-path
enumeration. All15520 deletion-negative predicates were checked for the
required actual-path-to-flag direction for all16 selectors. Y25 colors,
all terminal profiles, vertex states, occupancy and missing states are saved.

Deterministic controls passed before the solve: all colorings at N3..5,
20 fixtures per N6..8, and one N11 arbitrary-color recurrence fixture which
has the positive incoming/outgoing/deletion pattern. This last fixture is
only an encoder control and is not asserted D7. There are1103 fixtures,
209315 canonical-clause checks,64736 rejected single-gate flips,799 semantic
selector cases,518 local iff truth cases, and all65536 N26 selector masks.
The exact AND/OR truth tables and induction on length justify canonical
recurrence lifting; the bounded controls supplement that argument.

The unchanged base source is invoked at N26. Its historical static schema
and packet-label metadata still mention order30; binding.json explicitly
records actual N26/14950 packets and hashes the actual base/full CNFs.
No old one-way flag is used for positive existence or exact counts. Selected
right-root clauses are explicitly recorded as redundant. No endpoint count,
tau5, b25, e/m type, favorable path or non-exhaustive position was imposed.

Primary evidence: result.json, binding.json, controls.json, solver_launch.json,
complete_solver_assignment.json, sat_colors.json, sat_semantic_result.json,
Y25_colors.json, Y25_full_profile.json, variable_ledger.json, query.cnf and
the raw solver streams. The retained query.drat is a5374485-byte proof stream
from a SAT run; it is not an UNSAT certificate. Its SHA256 is recorded.
The final file-consistency inventory checks only bindings and terminal bytes.

The result refutes the specified single-outer-root candidate. It grants no
E6 exclusion, E5 conclusion, full D<=29 bound, independent mathematical
review, production acceptance or campaign upgrade. Executor role was
requested as native gpt-6.1-sol/high; actual backend/effort is not independently
reported by the tool evidence and remains unverifiable.

Linux result root:
`/data/ktqiu_hdd/math_agent/tmp/d7_joint_extensions_hr_20261027/single_root26`.
Local mirror is the same project-relative directory. Initial transport
preflights found that bare python and the remote Trellis context helper were
unavailable. Scientific execution then used the established absolute Python
3.12 runtime; no scientific code or solver ran on Windows.
