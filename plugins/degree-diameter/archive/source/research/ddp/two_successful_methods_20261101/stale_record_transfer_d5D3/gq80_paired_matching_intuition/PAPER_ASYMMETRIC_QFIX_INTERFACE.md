# One fixed C5 line matching and unrestricted point matching: paper audit

This audits the new rule in `asym_once.py` and its saved-counter dependency. It does not execute the model, reselect Q, rebuild CNF, run a solver, recompute geometry or perform BFS. This is not a continuation of the old simultaneous symmetric matching search.

## Scope and necessary Q profile

Q is chosen from the actual65625 C5-invariant line matchings. For a line root L let i_Q(L) count Q edges with both endpoints in its13-line closed concurrency set. For a point root p let j_Q(p) count Q edges with both endpoints in its four-line pencil. The unrestricted root proof in `PAPER_INTERFACE.md` gives i_x+3j_x≤3 for every root of any D3 completion, with no girth assumption.

Hence every eligible fixed Q must have i_Q(L)≤3 for all lines and j_Q(p)≤1 for all points. The code computes these integer sums from each selected block's five actual edges, retaining multiplicities rather than treating a block as one edge. Checking one representative of each eight-orbit family suffices for invariant Q and invariant geometry; the finally selected Q is also checked at all40 roots.

These profile conditions are necessary, not sufficient. The specified deterministic selection chooses maximum saved coverage and then minimum old matching index among eligible Q. It selects one concrete Q; it does not solve all eligible Q choices. The actual saved selection is oldQ index1361, with20 line edges, coverage113 and five concurrent-edge triangles. No second Q is implicit in the mathematical review.

## Exact residual P model

There is a variable x_e for every unordered point pair,780 in total, including collinear pairs. Forty exactly-one vertex conditions make a point perfect matching. Fixed Q already supplies one line matching neighbor per line, so every complete assignment would give the intended degree5 graph on80 vertices without further symmetry assumptions on P.

For each original41-edge far clause, if a selected Q variable occurs, the clause is already true and may be deleted. Otherwise set every fixed-Q variable false and retain its positive P literals. On point-far rows these are own-P witnesses; on line-far rows they are opposite-P relays. Both types must remain. The code iterates all original far rows, not merely a C5 quotient, since P is allowed to break the action. Under the matching equations, these simplified clauses are exactly equivalent to the original far coverage for this fixed Q.

Thus a satisfying point matching has all old mixed/near routes and all remaining far routes. A positive must still be materialized and independently accepted, but the symbolic residual formulation itself is exact. A negative for this one Q cannot exclude other eligible Q or arbitrary paired matchings.

## Full-valid route cuts

At point root p, i_P(p)+3j_Q(p)≤3 becomes

i_P(p)≤3-3j_Q(p).

The right side is0 or3 after the valid Q profile filter. i_P counts selected edges among all C(13,2)=78 unordered pairs in the closed set C(p); the code uses exactly these variables, not just the12-neighbor set and not a triangle-free54-variable subset. Bound0 is encoded by negative units and bound3 by the saved sequential-unary counter.

At line root L, i_Q(L)+3j_P(L)≤3 becomes

j_P(L)≤floor((3-i_Q(L))/3).

That bound is0 or1. j_P counts the six possible P edges among the four points on L. Negative units or pairwise at-most-one clauses encode it exactly. These consequences preserve collinear choices wherever the fixed Q and the valid inequality permit them; they do not impose girth≥5 or arbitrary preselected triangle bans.

The saved `atmost_three` counter is generically sound for n≥1, including78. Its forward implications require s(i,j) whenever the first i inputs contain at least j true bits; the clause not(x_i) or not(s(i-1,3)) forbids a fourth true input. Conversely any input of weight≤3 extends by setting s(i,j) exactly when the prefix count is≥j. Auxiliary equivalences are unnecessary. The code advances `next_id` past the reported last auxiliary, so these groups do not collide with the noninvariance witnesses. No new numerical counter calibration is required for this paper argument.

## Exact non-C5 boundary by existential witnesses

Let g be the actual point permutation of the bound C5 generator, acting on all780 unordered point-edge variables, including near pairs. Introduce one auxiliary w_e with

w_e⇒x_e,  w_e⇒not(x_{g(e)}),  and OR_e w_e.

Any extension satisfying these clauses has a selected edge whose image is unselected, so P is not g-invariant. Conversely, if P is not invariant, some finite edge-permutation cycle has nonconstant0/1 values. Such a cyclic binary sequence necessarily has a1→0 transition. Select that edge's w_e and set the others false to obtain an auxiliary extension. Hence the projection of the auxiliary CNF is exactly P noninvariant; the missing reverse implications are intentional and harmless.

The action has no fixed unordered point pair because it is free of prime order5 on points, so the code's image-not-equal assertion is valid. Sorting the two image endpoints before `eid` gives the correct unordered edge. Invariance under the generator is equivalent to invariance under its generated C5.

Since fixed Q is invariant, an invariant P would lie in the already completely excluded common-C5 family. Excluding that boundary therefore loses no possible successful completion. It does not exclude P merely because it has some other symmetry, and it does not assume arbitrary successful P is symmetric. This is a genuine relaxation of the old symmetric rule.

## Execution and conclusion boundaries

The initial `asym_once.py` parent hardCPU6 could not be raised to20 by a child preexec function. That launch failed before solver execution; it is an execution-interface failure, not a combinatorial result. The separate launch script reuses the same fixed Q and CNF while preserving that failed cost. A later invocation rejecting an invalid CLI option likewise does not constitute a searched-model timeout or UNSAT. These distinctions do not change the audited CNF mathematics.

A real SAT result must be checked against every CNF clause, all80 original matching equations and all1080 original far rows, then materialized as the actual80/200 edge table with explicit ≤3 paths before fresh acceptance. The export code performs these checks for a positive. A solver timeout remains UNKNOWN for this Q. A raw UNSAT without a checked proof remains a raw solver claim for the selected fixed-Q model; it must not be promoted by this paper into a certified unrestricted exclusion. No Q2, new timer or different solver follows automatically.

The review found no logical issue in the Q profiles, residual original rows, unrestricted78/6-variable cuts, auxiliary ID scheme or noninvariance projection. All source geometry/field and old full enumeration inputs are inherited. No numeric or solver process was run by this paper task.


## Actual selected-Q terminal (read-only, separate from C5 proof)

The corrected legal invocation uses separate arguments `-t`, `19`, reuses the same Q1361 and prepared CNF, and actually returns exit20 with `s UNSATISFIABLE`. Its output reports parsing the9750-variable/51436-clause input,18 conflicts and87 decisions. `ASYM_SOLVER_RESULT.json` records child0.016967CPU and cumulative4.886162516/30CPU, preserving both the preexec-limit failure and invalid combined-option failure. There is no second Q, model rebuild, source validation or candidate graph. The fixed-Q residual has515 far clauses;450 of the780 P variables are explicit negative units, leaving330 initially unrestricted by those units.

This is an actual raw solver UNSAT for the selected-Q/free-P model, not a timeout and not the earlier CLI rejection. No formal UNSAT proof was logged or checked. It remains separate from the exhaustive combinatorial C5 join, whose complete finite NO is established by saved full-domain bitset queries. Other fixed-Q/free-P choices and the arbitrary two-matching family remain untested. The paper review runs neither that solver nor a new validation process.
