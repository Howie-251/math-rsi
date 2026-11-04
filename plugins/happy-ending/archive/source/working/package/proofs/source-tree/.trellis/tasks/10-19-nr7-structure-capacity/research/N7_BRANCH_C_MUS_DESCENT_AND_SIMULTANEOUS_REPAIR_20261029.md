# Branch C: simultaneous repair, rollback obstruction, and the descent stop

Date: 2026-10-29. Mathematical generation only; **unreviewed / unaccepted**. No new support exclusion, no improved deletion bound, and no new global numerical bound. No scientific enumeration, solver, proof checker, external review, or export request. This fresh note does not change historical artifacts, configuration, acceptance records, or task pointers.

## 1. Exact scope and inherited starting point

X is one actual complete ordered rank-3 signotope with no B6, R7, or weak7. A weak7 uses opposite-color paths with the same actual endpoints and total length at least nine. F is an inclusion-minimal unsatisfiable family of complete path requirements: every R6 meets both K and Y; every B5 meets K. The two requirements on a red path remain bundled.

Fix a blue Q in F and one assignment sigma satisfying F minus Q. Thus Q is entirely Y. Fix q in Q and let A_q consist of ALL red paths A in F with A intersect Y = {q}. Choose an inclusion-minimal transversal S of their five-point K-traces. The prior note proves that after q moves to K and S moves to Y, all old all-K blockers are repaired, and the complete violation family is

\[
\mathcal V(S)=\{T\in F:q\notin T,\quad\varnothing\ne T\cap K\subseteq S\}.
\]

Members may be red or blue; all are now entirely Y. Unsatisfiability gives V(S) nonempty, not singleton. For every x in S, a private actual red A_x satisfies

\[
A_x\cap Y=\{q\},\qquad A_x\cap S=\{x\}.
\]

These witnesses are distinct. For any T in V(S), A_x meets T in {x} if x belongs to T, and otherwise is disjoint from T. This setup and exact first repair criterion are inherited from [the previous C note](N7_BRANCH_C_CRITICAL_BLOCKER_PROPAGATION_20261029.md), not claimed as new here. The current question is whether one can repair **all** V(S) and descend while preserving an actual common assignment.

## 2. First attempt: minimize the complete violation family

Select S among minimal transversals to minimize |V(S)|, with any deterministic secondary choice. This is a well-defined finite minimization. To obtain an actual next critical assignment, one would need to prove |V(S)|=1 or construct another assignment satisfying every member of F except one specified exit.

Neither conclusion follows from the minimization: a strict reduction requires a different transversal whose entire violation family has been compared. Minimality of F supplies a satisfying assignment after deleting a specified T, but that assignment need not preserve any of the K/Y traces, private witnesses, or q/S accounting of sigma. Selecting a critical assignment separately therefore does not implement the proposed descent.

**First gap C1:** no transversal-preserving move has been proved to decrease the complete violation family. No claim that a counterexample exists is made; this is the missing implication in the proof attempt.

## 3. Second attempt: repair all exits by a second simultaneous move

### 3.1 Restoring points from S necessarily reopens old blockers

Keep q in K. If a nonempty U contained in S is moved back to K, then every A_u for u in U becomes entirely K: its only original Y-point q remains in K, its only point of S was u, and u has now returned to K. Thus this rollback reopens at least |U| distinct complete red requirements.

Consequently a second move consisting only of restoring points from S cannot yield a satisfying assignment. This statement handles all private witnesses simultaneously and is valid for actual paths. It does not say the total number of violations cannot decrease: restoring one vertex could repair several exits while reopening one or more old blockers. It therefore does not establish an acyclic repair process or rule out more elaborate exchanges.

### 3.2 Recruiting original Y-points exposes previously absent blocker families

Instead keep S in Y and choose U contained in Y minus {q}, moving all U to K. Put P={q} union U. Relative to the original sigma, the new roles are

\[
K'=(K\setminus S)\cup P,\qquad
Y'=(Y\setminus P)\cup S.
\]

The exact complete all-K red violation family is

\[
\mathcal K(P,S)=
\{A\in F:A\text{ red},\ A\cap Y\subseteq P,
\ A\cap K\cap S=\varnothing\}.
\tag{1}
\]

The exact complete all-Y red-or-blue violation family is

\[
\mathcal Y(P,S)=
\{T\in F:T\cap K\subseteq S,\ T\cap P=\varnothing\}.
\tag{2}
\]

Proof: each equality simply checks every original K-point and every original Y-point of the whole path against the displayed new partition. For (2), Q is absent since q belongs to Q intersect P. All other members of F originally had a nonempty K-trace, because sigma satisfied them. There are no other kinds of violated requirements. Since P contains q, (2) is precisely the subfamily of V(S) avoided by U.

Hence choosing U to hit ALL V(S) repairs every all-Y exit, but it is insufficient: (1) can contain paths with several original Y-points, all contained in P. Such paths were not members of A_q and therefore were not necessarily hit by S. A candidate proof must simultaneously rule out every member of (1), rather than repair one selected new blocker.

**First gap C2:** no actual-support theorem makes an all-exit hitting U compatible with emptiness of (1). Recruiting further K-points to Y merely starts another enlarged pair of complete families; no strictly decreasing measure has been proved. These equalities are bookkeeping for the attempted iteration, not a new descent theorem.

## 4. Third attempt: actual endpoint fans and endpoint barriers

The actual geometry gives more than the set intersections above. If an actual R6 has endpoints a<b, then

\[
\chi(a,z,b)=R\qquad(a<z<b)
\tag{3}
\]

for every actual point z, including points outside F: a blue triple with these endpoints would form weak7 with the red six-path.

A related endpoint barrier, already used in [R20 section 6.3](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md), applies without its saturation assumption. If an actual R6 ends with u<v, every actual R6 starting at u has endpoint at most v. Otherwise let its endpoint be h>v. No R7 forces chi(u,v,h)=B, since a red connecting triple would append h to the first R6. But this blue triple and the second R6 have the same endpoints u,h, contradicting weak7. Reversing order gives the dual statement: if an R6 begins u<v, every R6 ending at v begins at least u.

Both facts hold simultaneously for every private A_x and every red exit, and (3) tests all actual intermediate points rather than only selected witnesses. However, the private singleton intersection does not force x to be the endpoint/penultimate point needed by the barrier. Nor does (3) alone supply all connecting triples needed to insert an arbitrary point into a red six-path. No incompatible pair of forced fan colors has been derived for the complete families (1)-(2). Blue exits remain possible and require their own control.

**First gap C3:** actual endpoint information is available, but the critical-assignment hypotheses do not force the positional incidences needed to turn it into a contradiction. No arbitrary two-path example or abstract hypergraph is offered as an actual MUS counterexample.

## 5. Pure-red case and generation cross-challenge

If F is pure red, delete a red Q and reverse the two roles if necessary so Q is entirely Y. For each q in Q the same transversal, rollback, and enlarged-family analysis applies; q moving to K repairs Q, whose other vertices stay Y. All exits are red. The orientation reversal is legitimate for this pure-red family only. The absence of blue Q removes the opposite-color intersection bounds used in the preceding C note. No argument here excludes a pure-red MUS.

In generation cross-challenge, the strict-branch collaborator checked the private-witness rollback accounting and confirmed that the saturated four-core matching restrictions need extra hypotheses unavailable for a general MUS. The collaborator independently pointed to the actual endpoint fan (3), but supplied no forced incompatible fan entry. This is mathematical collaboration, not independent review and not acceptance.

The stopped labels are: **C1 complete-family descent unproved; C2 enlarged simultaneous repair unclosed; C3 actual positional forcing absent; pure-red MUS exclusion open.** The inherited global z<=5 baseline is unchanged. No z<=4 or smaller support transversal follows here.

## 6. Transfer of remaining effort to canonical H50 plus R30

The parent task requests priority transfer to the actual saturated canonical decomposition, with a 25-point Y and a five-point minimum T. The independent MUS assignment must not be identified with this canonical partition.

One exact splice check illustrates the first gap on that stronger input. Suppose an insertion supply actually has the orientation

\[
P_t=(t,y_1,y_2,y_3,y_4,y_5)
\]

red, with all y_i in Y, and an H-tail for the same t begins at h_1, where t<h_1<y_1. Saturation's absence of any H-source ambient R6 forces chi(h_1,y_1,y_2)=B: otherwise h_1 followed by all five y_i would be such a path. The packet on t,h_1,y_1,y_2 has third entry R and last entry B, so its first two entries are R. Thus

\[
\chi(t,h_1,y_1)=\chi(t,h_1,y_2)=R,
\qquad\chi(h_1,y_1,y_2)=B.
\]

This gives a valid actual cross-support orientation, but the last blue triple prevents the proposed naive red splice. It does not give R7, B6, or weak7. The conclusion is conditional on the stated orientation of the insertion supply; no claim that all insertion supplies start at t is made. This observation was returned to the parent for the higher-priority canonical branch, without changing another agent's files.

Primary sources read for this continuation include the preceding C note, [the full-pair fan synthesis](N7_FULL_PAIR_FAN_BOUNDARY_AND_TIGHT_CORE_DICHOTOMY_20261029.md), [the saturated-interface note](N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md), [the uniform-tail note](N7_UNIFORM_TAIL_INTERVAL_STABILITY_20261028.md), and the relevant canonical portions of [R7](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) and R20. Their prior evidence status is preserved.
