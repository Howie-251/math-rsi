# Direct CNF review: exact encoding, no numerical rerun

Verdict: **VALID**. The actual [worker.py](worker.py) and [driver.py](driver.py) were read once. No encoding or witness-indexing bug was found. This review runs no solver, BFS, matching enumeration, or geometry reconstruction.

The input is the unchanged old1560-variable [model](../../../breadth_20261027_wave11/gq80_paired_matchings/model.json), whose full finite-family equivalence is explained in [the original report](../../../breadth_20261027_wave11/gq80_paired_matchings/REPORT.md). It represents all780 unordered point pairs and all780 unordered line pairs, with no preselected edge or symmetry restriction.

## Exactly-one and variable indexing

Each of the80 vertices has39 possible internal matching edges. The worker writes one positive39-literal at-least-one clause and all C(39,2)=741 negative pairwise at-most-one clauses for that vertex. Thus all80 degree equations are encoded exactly, with80 ALO and59280 AMO clauses. Because each edge variable belongs to both of its endpoint degree equations, a satisfying assignment is precisely one perfect matching of each40-vertex side.

Every occurrence of old zero-based variable ID v is written as DIMACS v+1. The header p cnf1560 60440 matches80+59280+1080 clauses. The1080 old positive41-variable coverage rows are written as ordinary positive OR clauses, exactly equivalent to their binary sum being at least1. No clause or variable family is dropped.

## Why these clauses are equivalent to D<=3

All opposite-side pairs have an incidence-only path of length1 or3. All same-side collinear pairs have an incidence-only path of length2. The only missing cases are540 unordered far pairs on each side, giving1080 constraints.

For same-side far points x,y, a path of length at most3 contains zero or two incidence edges. With two incidences, its one matching edge can only be first, last, or middle:

* point matching x-z with z in C(y);
* point matching y-z with z in C(x);
* line matching L-M with L incident with x and M incident with y.

The first two families have13 variables each and share only xy, giving25 distinct own-side variables. The two disjoint four-line incident sets give16 opposite-side variables, for41 total. A path with no incidence edge remains within a single matching edge and adds only the directly matched-neighbor possibility, already represented by xy. The dual argument covers far line pairs. There is no additional same-side path type of length at most3.

Consequently, under the exactly-one constraints, all1080 coverage clauses hold if and only if the full augmented80-vertex graph has D<=3. This is the arbitrary-two-perfect-matchings family, rather than a fixed matching or restricted orbit family.

## SAT witness and graph export

The worker accepts SAT only with solver exit10 and the SATISFIABLE status line. It decodes positive/negative DIMACS literals into bits indexed1..1560, then selects old IDs i using bits[i+1]. It checks all60440 literal clauses, all80 old degree equations, and all1080 original coverage rows. It additionally checks all3120 saved route-overlap cuts; these are valid integer consequences, as established in [ANALYSIS_CUT_REVIEW.md](../ANALYSIS_CUT_REVIEW.md).

Omitting those3120 cuts from the CNF does not relax the intended binary model: they are redundant for its integer feasible set. Their witness check does not add a geometric restriction.

Export maps point matching IDs directly to vertices0..39 and line matching IDs to40..79 by adding40. The worker retains the160 old incidence edges, adds20 edges per side, and checks200 distinct nonloop edges with degree5 at every vertex. A new positive candidate is left for the parent's one independent full80-root check; this review does not perform that check or claim a candidate exists.

## Negative and incomplete statuses

The code has one solver launch and no restart loop. Exit20 plus the UNSATISFIABLE status is recorded as RAW_UNSAT_NO_PROOF_NOT_CERTIFIED. No UNSAT proof is requested or checked, so such a result must not be recorded as a strictly certified exclusion of all matching pairs. Other solver exits or interrupted workers produce UNKNOWN, not a graph distance or an infeasibility result.

The mathematical encoding equivalence is established by this review. Solver outcome, performance, candidate existence, and graph verification are separate producer/parent evidence. This file adds no new experiment or independent method.
