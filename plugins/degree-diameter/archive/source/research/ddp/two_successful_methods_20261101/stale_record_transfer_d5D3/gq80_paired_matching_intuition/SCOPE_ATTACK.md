# Scope attack: saved GQ80 paired-matchings model

This is a read-only attack on the exact node `ddp-wave11-gq80-paired-matchings`
and its linked reports/code. No solver, field/geometry generation, graph,
matching enumeration or BFS is run. The source/geometry and prior numerical
receipts are inherited. This note does not reopen a time window.

1. The original model is the full, unsymmetrized fixed-template model.

The retained source is W(3,3)'s40+40 incidence graph,160edges. Adding one point
perfectmatching P and one line perfectmatching Q gives the proposed80/200,
5regular graph. `breadth_20261027_wave11/gq80_paired_matchings/run.py` creates all
1560 same-side pair variables; its saved schema has `preassigned_edges=[]` and
`symmetry_constraints=[]`. It does not fix one matching or forbid collinear
point edges. A statement that this original run broke symmetry by restricting
P to noncollinear pairs would be false.

2. The matching/coverage rows are sufficient as well as necessary for D3.

Under binary perfectmatching equations, cross-side targets already have old
incidence paths of length<=3, and same-side collinear targets have length<=2.
Only540far pairs per side remain. A same-side walk of length<=3 has zero or two
incidence steps. Zero incidence steps stay in one matchingedge; repeated
matching steps cancel. With two incidence steps the single matchingedge can
be first,last,or middle. These are exactly the own-side25 and opposite-side16
choices in each41-variable cover row. The1080 complete far rows plus80matching
equalities therefore express D<=3 exactly, rather than a necessary relaxation.
They only express that fact for binary matchings; a fractional LP vector is
not a graph. Individual budget/cut conditions do not replace all1080 rows.

3. Later girth restrictions are genuine subfamilies,not proved symmetry WLOG.

Noncollinear P pairs and nonintersecting Q pairs remove triangles. The6480
mixed-rectangle clauses remove the remaining4cycles. Within those restrictions
all1080 filtered cover rows (29literals=17own+12relay) still express D3 exactly.
But the read `ANALYSIS_GIRTH_SCOPE.md` does not prove that every D3 solution of
the unrestricted template must have girth>=5. The triangular choices are not
mapped away by relabeling: collinearity is preserved by incidence automorphisms.
Thus a proof or UNSAT result for this restricted family would not by itself
settle the original1560-variable family. No actual D3 counterexample with
triangles is claimed here; the objection is the missing WLOG proof.

4. The later valid constraints do not constitute a family exclusion.

The3120 conditional overlap cuts are proved valid for arbitrary P/Q,including
prospective collinear edges. They leave the original integer graph family
unchanged. In the girth5 family the known a_x<=3 counters likewise preserve
that restricted integer domain. Existing paper already establishes
E_x=6-2a_x+delta_x and sum(E_x)=80+sum(delta_x),with sum(a_x)=80 on eachside.
Those are inherited identities,not new results of this reread. Their displayed
arithmetic profile a_x=2,E_x=2 is consistent with the budgets but is not an
actual graph. Average2 does not force a root with a_x=3. No proof of the needed
forced global excess or simultaneous P/Q incompatibility was found in these
linked analyses. What is excluded is violating a valid cut/budget within its
premises,not the full pairedmatching family or even allgirth5 choices.

5. The five actual windows are UNKNOWN without a saved target witness.

Original15s MILP,overlap-cut MILP,unrestricted directCNF,girth5CNF and
local-budget girth5CNF all ended UNKNOWN with no incumbent/assignment. The
original HiGHS status1 is time limit,not infeasible; the later SAT time-window
status is not a checked UNSAT proof. Existing reports say zero80-point target
graphs and zeroBFS. `incidence.edges` is the4regular80/160 oldsource,not a
5regular80/200 target; model matrices,CNF and variable maps are not distance
graphs. There is no saved full candidate,near-miss distance matrix,actual badpair
count or root histogram on which to base a local repair. Do not invent one.

The exact original template and its girth5 subfamily both remain unresolved by
these five windows. A later experiment needs a new structural question or a
concrete P/Q rule. Repeating a timer,calling alloldnecessary inequalities a new
obstruction,or silently promoting girth5 to WLOG would not answer that gap.

Read evidence: the specified Wiki node; original REPORT.md/run.py and the five
result receipts; linked ANALYSIS_CUT_REVIEW.md,ANALYSIS_GIRTH_SCOPE.md and
ANALYSIS_GLOBAL_ROUTE_BUDGET.md. Large model.json was accidentally included in
one read output; it was not executed or used to regenerate geometry,matrices,
CNF or graphs. No broad Wiki search or extra validation followed.

CPU accounting for f9 shared readgate: conservative prior local reads/preparation0.100000000 plus this metadata-summary/note process0.000656307 = 0.100656307 seconds. No numerical solver/graph/field/Lean/review cost.

Exact saved terminal statuses: original MILP status1/time-limit/noincumbent; overlap-cut window process_returncode−9 with no returned solver result; directCNF,girth5CNF,and local-budget girth5CNF all solver_exit_code0/UNKNOWN with no assignment. None is UNSAT or a saved failed target graph.

Root's proposed C5/order5-invariant matching restriction was not imposed by the old original model (no fixededges/symmetry constraints). Its feasibility is not excluded by the old UNKNOWN windows. It is a restricted candidate domain,not a proven WLOG reduction of the full pairedmatching problem. No C5 source matrix,orbit or constraint was constructed or searched by this note.

Final scope-attack conservative/actual read accounting including this small appendix: 0.100792823 CPU seconds, for f9 shared5CPU readgate. All work terminal.
