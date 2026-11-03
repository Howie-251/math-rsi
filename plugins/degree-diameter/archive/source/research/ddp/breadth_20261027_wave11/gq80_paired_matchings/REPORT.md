# W(3,3) incidence plus two perfect matchings: one complete finite MILP

Status: **UNKNOWN, no incumbent**. One unsymmetrized feasibility MILP reached its configured 15-second time limit. It returned no matching pair, no 80-point candidate graph, and no infeasibility conclusion. No extra time, restart, seed, symmetry restriction, or second production call was used. This does not exclude the template.

## Definition and target

The target is Delta=5, D=3, n=80, compared with saved lower bound 72 (2026-10-26 portfolio snapshot). This is the q=3,r=1 necessary-capacity survivor from ../gq_internal_capacity/RESULT.json, and a different exact coverage model from the existing q=5,r=2 finite search.

Construct W(3,3) from the 1-dimensional subspaces of F3^4 with alternating form

    omega(x,y) = x0*y1 - x1*y0 + x2*y3 - x3*y2 mod 3.

Normalize each nonzero point vector so its first nonzero coordinate is 1; sort lexicographically. Lines are the 2-dimensional totally isotropic subspaces, represented by their sorted four projective point IDs and sorted lexicographically. This gives 40 points, 40 lines, and 160 incidence edges, with incidence degree 4. Vertex IDs are points 0..39 and lines 40..79. Retain all incidence edges. Add one arbitrary perfect matching of the point side and one arbitrary perfect matching of the line side. A feasible result would therefore have 80 vertices, 200 edges, and degree exactly 5.

`geometry.json` saves the complete normalized point coordinates, line point sets, and point-to-line incidence lists. Generation checks the counts, the 13-element closed collinearity sets, their pairwise 4-element intersections, and the GQ unique-collinear-point property. These checks do not perform graph BFS.

## Exact binary model

There is one binary variable for every unordered pair within either 40-vertex side: 2*C(40,2)=1560 variables. Eighty degree equations require each point or line to lie in exactly one selected internal edge. No edge is preselected, and no group symmetry, orbit constraint, or canonical matching is imposed. The objective is identically zero, so the solver seeks feasibility only.

For each same-side noncollinear pair {x,y}, a D3 route exists precisely when at least one of the following variables is selected:

- A same-side edge {x,z} with z in C(y), or {y,z} with z in C(x), where C is the closed collinearity set.
- An opposite-side matching edge {L,M}, with L incident to x and M incident to y.

For a far pair, x is not in C(y) and y is not in C(x), so both first sets contain 13 valid nonloop variables, with exactly the shared variable {x,y}. They therefore give 25 distinct same-side variables. The two incident neighborhoods have size 4 and are disjoint, giving 16 distinct opposite-side variables. The clause has exactly 41 distinct variables. The line-side clauses are the dual version.

There are 40*27/2=540 unordered far pairs per side and 1080 cover inequalities in total, each requiring its 41-variable sum to be at least 1. Together with the 80 equalities, the model has 1160 rows and 47400 nonzero coefficients. The complete variables and all constraint rows are saved in `model.json`; `constraint_schema.json` explains their interpretation.

## Why the cover clauses are equivalent to D3

All opposite-side pairs already have an incidence-only path of length at most 3, and collinear same-side pairs already have an incidence-only path of length at most 2. The only remaining pairs are the same-side far pairs in the clauses.

A same-side path of length at most 3 uses either zero or two incidence edges. With two incidence edges and one matching edge, the matching edge is first, last, or in the middle; these cases are exactly the two own-side terms and the opposite-side term above. With no incidence edges, all steps stay in a perfect matching, so any odd-length path ends at the matched neighbor and any even-length path returns to the root. The direct matched-neighbor possibility is already represented by {x,y} in the own-side term. There is no other path type to omit. Thus under the degree equations, all 1080 clauses hold if and only if the augmented graph has D<=3.

## The one production window

The installed stack was SciPy 1.15.3 with HiGHS 1.8.0. The call used `scipy.optimize.milp` with binary integrality, bounds [0,1], presolve enabled, zero objective, one solver thread, and `time_limit=15.0`. Solver heuristics were left at defaults; no random seed was added. The process had a hard RLIMIT_CPU of 20 seconds. A driver recorded the process exit and enforced a wall fallback; it did not launch another solver call.

Result: SciPy status 1, HiGHS model status Time limit reached, primal status None. The solver's report showed no finite primal bound, zero completed branch-and-bound nodes, and 3884 LP iterations, including its default internal heuristic work. It returned no incumbent vector. There is consequently no candidate.edges or candidate.matchings.json to send for final BFS. No inference of UNSAT is made.

Configured solver limit: 15.000 seconds. Measured solver wall time: 15.056630 seconds; solver CPU: 15.055620 seconds. The solver returned about 0.057 seconds after the configured limit while completing its internal stop. Measured whole-process CPU: 15.481300 seconds, below the hard 20-second limit. No replacement window was run.

## Evidence, limits, and terminal action

- `run.py`: full coordinate construction, all binary variables/clauses, the one MILP call, and feasible-incumbent export logic.
- `driver.py`: the one process launch and budget/exit bookkeeping.
- `geometry.json`, `incidence.edges`: the generated source geometry and its complete incidence edge table.
- `model.json`, `constraint_schema.json`: all variables and complete matching/coverage constraints.
- `production.log`, `result.json`, `terminal.json`: solver output and terminal UNKNOWN status.

Graph generations of the augmented target: 0. BFS calls: 0. Production MILP calls: 1. Exported feasible candidates: 0. New lower bounds: 0. The source incidence graph is not a target success. This finite window is closed; no continuation follows from the UNKNOWN result. The exact 41-variable coverage model remains reusable if a separately authorized structural advance or new complete bounded task justifies reopening it.
