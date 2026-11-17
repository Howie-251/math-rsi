# Twenty-two-point outer-arm projection remains SAT

**Verified SAT.** The 6/6 extraction with real outer R5 arms remains
compatible. This is the requested stopping point; no further solver model
was launched. It gives no improvement from center-selection fee 11 to 10.

Physical order is L=1..4 < U=5..10 < r=11 < s=12 < V=13..18 < R=19..22.
The two frozen paths are R5(1,2,3,4,5) and R5(18,19,20,21,22).
[SCOPE.md](SCOPE.md) gives the complete exact predicates. In particular,
source/terminal row locks apply only to R6 wholly within the original
14-point domain 5..18; added L/R points are not incorrectly excluded as
other matched rows. All hats and the ambient U-to-V R5 ban use the full
22-point domain. The mixed B4 ban applies only inside the original U union V.

The [frozen 1,540-triple coloring](6-6/colors.tsv) has maximum red/blue path
lengths 6/5. It passes [independent physical verification](6-6/independent-verification.json)
over **all 4,194,281 subsets of sizes 2 through 22**, including exact
same-endpoint weak7 checks. Its actual red path counts at lengths 2..6 are
231,965,1605,1152,294; blue counts at lengths 2..5 are 231,575,487,87.
The [full path and endpoint witness](6-6/physical-witness.json) is retained.

[Independent complete schema reconstruction](6-6/schema-audit.json) passed
with zero missing/extra clauses. The [CNF](6-6/formula.cnf) has 2,233 variables
and 453,859 distinct clauses. It uses 1,540 physical colors followed by
693 R4/R5/R6 endpoint flags. Those flags are used only for weak7 prohibitions:
real red paths imply their flags, and each corresponding blue path is
incompatible with its flag. Any admissible coloring extends by setting flags
to actual path existence; no exact counts or physical roles are inferred
from a one-way flag.

All scientific execution was on the authoritative Linux host. A controlled
external Kissat with a 60-second solver budget returned exit 10 in 9.6462
seconds; independent schema and physical checks exited 0 in 6.9038 and
24.5941 seconds. [Raw result/source/formula bindings](6-6/result.json),
[runtime and binary hashes](runtime.json), [solver output](6-6/solve.stdout),
and [launch receipt](launch-receipt.json) are preserved. The SAT-run DRAT
trace is not an UNSAT certificate and was not presented as one.

Formula SHA256: `11c68ba81ec430cd90663c69ef0055270c78e14c17802c22f567cb071edfc8e2`.
Coloring SHA256: `085e21845efe55fb5175e6320ab9d66c0c9b7acfac4f7dc6a2c70a4abe25cf41`.

This establishes compatibility only of the specified necessary extracted
domain. The other five left and right ambient rows and full B5/R6 supplies
are not constructed, so it is not an ambient 6/6 example or a geometric
realization. Any general rank exclusion needs additional proved consequences.
No external review or general-bound acceptance is claimed.
