# Appended final port consequences

Source delta only; no preparation or solver result is asserted here.
The root owns execution and records the reused local source-delta review.

The two saved parent inputs remain complete original-A models. Their
variables, all original degree and distance-two coverage clauses, and all
previous port conditions are preserved. Preparation copies the original CNF
body verbatim, changes only its clause-count header, and appends proved
conditions on already exact actual-B threshold bits from `constraints.json`.
No new variable, regenerated baseline, new graph labeling, or chosen port is
introduced. The old source, inputs, UNKNOWN results and proof traces remain
untouched in the parent directories.

For `r1_h0_b0`, the universal h=0 theorem applies also to the consecutive
double triple v,u,z whenever B_uz=2. Its common-neighbor inclusion forces
the unique T parent of z into U; the w/W condition is analogous. Append
negative units for the exact second-threshold bits at the other 33 positions
per endpoint. There are 66 pre-simplification conditions; the actual saved
mapping has 66 nonconstant, distinct bits. This uses
`INTERNAL_DOUBLE_COMMON_ATTACHMENT_EXCLUSION.md`, whose proof includes the
checked r0_h1_b0 contradiction. The selected triple's former h=0 assumption
alone would not justify the new constraints.

For `r2_h0_b1`, retain all three configurations proved in
`INTERNAL_DOUBLE_SHARED_TWO_PORTS.md`: the ordered endpoint ports are
(q0,p0), in O_c × O_d, or in O_d × O_c. Each existing endpoint domain has
eleven members. Append exactly 70 binary clauses for the forbidden pairs
among all 121 ordered choices, retaining exactly 51 allowed choices. No
matching interface or particular endpoint port is frozen.

The combined delta proof is
`proofs/dd82/n61/INTERNAL_DOUBLE_FINAL_PORT_CONSEQUENCES.md`. Excluding one
refined input excludes only its local type, conditional on the inherited
proof and complete original-graph reduction. Both remaining types are needed
to close the internal-double target, together with the existing checked r0
case. This would still not be a whole-order61 exclusion.

Commands use the same interface as the parent, with only the two open cases:

```
python encode.py prepare --case r1_h0_b0
python runner.py prepare --case r1_h0_b0 --cpu CPU_ID
python runner.py solve --case r1_h0_b0 --cpu CPU_ID
python runner.py check --case r1_h0_b0 --cpu CPU_ID
```

Use either direct preparation or bounded runner preparation once, not both.
Preparation verifies each new unit's Boolean truth condition and every one
of the r2 121 one-hot endpoint choices, then compares every parent body line
as bytes against the new prefix and every appended line against the planned
clause. It emits `delta_constraints.json` and `delta_sanity.json`, preserves
all variable IDs, and copies only the edge map and normalization needed by
decode/review. Existing baseline semantic evidence is referenced rather than
misrepresented as a new full-graph sanity run. No hashes are used.

The runner imports the existing process handling and changes only the output
directory and allowed case names. Limits stay 60 CPU seconds, 90 wall
seconds, 4 GiB address space and 512 MiB per output file; no automatic retry
or budget increase is introduced. SAT decoding checks the actual complete
refined CNF and restores every original edge before separate independent
BFS. Raw UNSAT remains distinct from the actual refined-input LRAT check.
