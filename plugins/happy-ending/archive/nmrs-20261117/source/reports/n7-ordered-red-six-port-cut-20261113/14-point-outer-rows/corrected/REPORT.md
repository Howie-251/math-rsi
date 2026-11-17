# Fourteen-point outer-row projection is SAT

**Verified SAT.** U=1..6 < r=7 < s=8 < V=9..14 satisfies the exact
[necessary projection](SCOPE.md). Its source/terminal locks refer to the
endpoints of entire R6 paths and impose no penultimate/second uniqueness.
The 12-point pool predicates are applied only inside U union V.

The [complete coloring](6-6/colors.tsv), [all-path physical witness](6-6/physical-witness.json),
[independent schema reconstruction](6-6/schema-audit.json),
[independent physical verification](6-6/independent-verification.json), and
[raw solver/check receipts](6-6/result.json) are frozen. Kissat exited 10
after 9.1377 seconds; both independent checks exited 0. Scientific execution
was on the authoritative Linux host with a controlled external solver.

This corrected create-only attempt follows the preserved failed parent
attempt: its builder reused the name s in a weak-path loop and raised
KeyError before producing a CNF or invoking a solver. The correction uses
begin/end loop variables. Parent sources and failure receipts were preserved;
no failed result was relabeled as SAT. The subsequent authorized 22-point
test is separately sealed in [its report](../../22-point-outer-arms/REPORT.md).

SAT proves necessary-projection compatibility only, without an ambient
extension, geometric realization, fee improvement or external review.
