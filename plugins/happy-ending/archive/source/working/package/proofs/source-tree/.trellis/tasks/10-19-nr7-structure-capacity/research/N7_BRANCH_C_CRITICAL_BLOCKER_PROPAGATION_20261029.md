# Branch C: critical blocker repair and its unresolved descent

Date: 2026-10-29. Theoretical generation only, unreviewed and unaccepted. No new global bound is proved. No scientific enumeration, solver, research-code execution, countermodel construction, or independent review was used. This note changes no historical evidence, task pointers, or acceptance status.

## 1. Exact setting and retained source lemma

Let X be an actual complete ordered rank-3 signotope with no blue six-vertex path, no red seven-vertex path, and no weak seven. Four-point packets in the order abc, abd, acd, bcd change color at most once. Paths are actual monochromatic vertex sets, and weak seven uses the same actual endpoints for two opposite-color paths whose lengths sum to nine (longer paths may be shortened with endpoints preserved).

For a partition X = K disjoint-union Y, each actual red six-path must meet both roles; each actual blue five-path must meet K. Let F be an inclusion-minimal unsatisfiable family of these complete path requirements. A red path's two role requirements remain one bundled member of F.

The starting sources are the 2026-10-28 notes `N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md`, `N7_UNIFORM_TAIL_INTERVAL_STABILITY_20261028.md`, and `N7_FULL_CAPACITY_INTERNAL_INSERTIONS_AND_PATH_EXCHANGE_BARRIER_20261028.md`, together with `RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md`, all in this directory. Their historical claims and acceptance levels are not changed. In particular, this note does not adopt a universal global z <= 5 proof from the older uniform-tail note: that proof is absent from the present branch.

Suppose Q = (q1 < ... < q5) is a blue path in F. Fix one assignment sigma satisfying F minus Q. It must put all Q in Y. Flipping just qi to K satisfies Q, cannot damage another blue requirement, and cannot create an all-Y red path. Unsatisfiability therefore produces a red Ri in F with

\[
R_i\cap Y=\{q_i\},\qquad R_i\cap Q=\{q_i\}.
\]

The five chosen paths are distinct. For i < j their shared support inside (qi,qj) satisfies

\[
|(R_i\cap R_j)\cap(q_i,q_j)|\le 5-(j-i).
\]

For completeness, if this intersection H has at least two points, Ri makes qi plus H red and Rj makes H plus qj red. For each h in H choose another h'; the packet on qi, min(h,h'), max(h,h'), qj has red first and last entries, hence all four entries red. This supplies every missing triple qi,h,qj. Thus qi,H,qj is an actual red path, while the Q subpath from qi to qj is blue with the identical endpoints. Their lengths sum to |H|+j-i+3, at most eight by no weak seven. When |H| <= 1 the claimed bound is automatic. This verifies the old lemma without combining different critical assignments.

## 2. Repair all old blockers, not just a selected witness

Fix q in Q and keep the single assignment sigma throughout. Define the full critical family

\[
\mathcal A_q=\{A\in F:A\text{ is red six and }A\cap Y=\{q\}\}.
\]

It is nonempty. Its K-traces A minus {q} all have five vertices. Select any S contained in K and change q to K and every point of S to Y. Call this assignment sigma_S.

**Exact repair criterion.** The assignment sigma_S satisfies F if and only if both conditions hold:

1. S meets A minus {q} for every A in the full family A_q.
2. There is no T in F avoiding q whose nonempty original K-trace is contained in S, where T may be a red six-path or a blue five-path.

Proof. Q is repaired because q is now K. A red path can newly become all K precisely when its original Y-trace was {q} and none of its original K-points was flipped: these are exactly the failures in condition 1. A red path can newly become all Y precisely when it avoids q and all its original K-points belong to S. Its original K-trace is nonempty because sigma satisfied it. Another blue path can fail precisely under the same latter condition; its original K-trace was likewise nonempty. These exhaust all path types and both possible red violations. No ambient path outside F is silently assumed to satisfy sigma.

Since F is unsatisfiable, every transversal S from condition 1 must fail condition 2. This is a Boolean consequence of genuine unsatisfiability, rather than an exchange assumed legal by definition. Minimality of F supplied sigma; no individual CNF clauses were counted as paths.

**Minimal-transversal propagation lemma.** Let S be an inclusion-minimal transversal of all the K-traces in A_q. Then there is a path T in F with

\[
q\notin T,\qquad\varnothing\ne T\cap K\subseteq S.
\]

It becomes all Y under sigma_S. For each x in S, minimality supplies an actual red six-path A_x in A_q with A_x intersect S = {x}. Consequently

\[
A_x\cap T=\{x\}\quad(x\in T\cap K),
\qquad A_x\cap T=\varnothing\quad(x\in S\setminus T).
\]

Indeed A_x has no original Y-point except q, which T avoids; every original K-point of T belongs to S. Distinct x require distinct private witnesses A_x. The whole statement uses the same sigma and one simultaneous q/S repair.

A swap with a single x is justified only if x belongs to every K-trace in A_q. Repairing one chosen Ri is insufficient: another member of A_q can remain all K. Turning multiple Q-points to K without repairing their full blocker families is likewise uninformative.

## 3. Actual support and weak restrictions on the forced red exit

If the forced T is red, set t = |T intersect K|, so 1 <= t <= 5. Since Q is blue and T is red, they share at most two actual vertices: three shared vertices would have both colors. Thus

\[
|T\cap(Y\setminus Q)|\ge \max\{0,4-t\}.
\]

A singleton repair, when it exists, therefore forces at least three original Y-points outside Q if its exit is red. For t = 2 or 3 the lower bounds are two or one. These are counts in the original common assignment; they are not exclusive costs chargeable across several repairs.

If T contains qa and qb with a < b, the actual red subpath between them and the actual blue Q subpath have identical endpoints. Let r_T(v) denote the ordered position in T. No weak seven gives

\[
r_T(q_b)-r_T(q_a)\le6-(b-a).
\]

In particular, if T contains both q1 and q5, their positions in T differ by at most two. This applies only when those intersections occur; no argument here forces them to occur.

The retained interval bound in section 1 uses packet closure essentially. The new exact repair lemma is combinatorial; this section applies actual triple colors and weak restrictions to its forced exit. Neither stage creates a common pair between A_x and T: their intersection is exactly the singleton x. The rectangle gluing used in the separate saturated-interface branch therefore has no input here. Its two perfect matchings and full fan partitions are also not available in the present 767 MUS setting.

## 4. Pure-red six-path branch

Suppose instead F contains only red six-path requirements. Remove any Q in F and choose sigma satisfying F minus Q. The unsatisfied Q is monochromatic. Global role reversal preserves every pure-red requirement, so choose the orientation with Q entirely in Y.

For each of its six vertices q, flipping q to K repairs Q (its other five points remain Y). The identical full family A_q is nonempty. For every inclusion-minimal transversal S of its K-traces, the same proof gives a red T avoiding q with nonempty T intersect K contained in S, and private A_x meeting T exactly at x for x in T intersect K. This is the exact same repair framework, with six initial critical vertices and no blue exit type.

However Q is now red. The bound |T intersect Q| <= 2 and the opposite-color same-endpoint rank bound from section 3 no longer apply. Two red paths may share more vertices; no red-seven prohibition alone turns their union into a red path. The no-blue-six and no-weak-seven hypotheses are still ambient assumptions, but this derivation has not extracted a contradiction from them. The pure-red MUS branch is **not ruled out** by this note, and no existence assertion for such an actual MUS is made.

## 5. First unresolved steps and honest outcome

The repair theorem is an intermediate lemma, not a descent theorem. The missing steps are explicit:

- The transversal S is not proved small, and even a small chosen Ri does not hit every member of A_q. There is no bound here forcing t <= 3.
- A forced exit can be blue; section 3 then provides no positive fresh-support count. Even red exits need not be the only violations.
- The new assignment sigma_S need not satisfy F minus {T}. Several paths may become all Y simultaneously. T is therefore not automatically a new critical deleted path. Reapplying the initial five-blocker argument at T would require another justified assignment and would lose the present common-assignment accounting.
- Private A_x/T intersections are singletons, so packet arguments needing two common ordered points do not close. Private witnesses can overlap elsewhere, and there is no proof of disjoint resources or monotone progress under repeated repairs.
- The pure-red framework has no blue seed and presently yields no contradiction or new support transversal bound.

Generation cross-challenge with the strict-interface branch found no transferable common-pair argument. This is collaboration, not independent review. The exact criterion, propagation lemma, and actual red-exit restrictions are the results; global support descent, exclusion of pure-red MUS, and any improved z or capacity bound remain unresolved. No new global numerical decrease is claimed.
