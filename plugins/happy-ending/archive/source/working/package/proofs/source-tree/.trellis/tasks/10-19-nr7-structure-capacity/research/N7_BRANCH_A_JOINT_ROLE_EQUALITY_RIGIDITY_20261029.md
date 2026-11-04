# Primary A: joint-role equality and an actual residual subconfiguration

Date: 2026-10-29, new research turn after the H50/R30 support-barrier note. **Mathematical generation, unreviewed/unaccepted.** No external review, scientific code, enumeration, solver, local test, or proof replay was used. This fresh file is the only artifact owned by this branch; prior notes are historical and unchanged.

The final main deduction is the parameterized capacity relation proved in section 8. For any actual 767 configuration with canonical decomposition X=H disjoint union R and |H|=2b, set S=Src_R6(X), T_6=End_R6(X), D=X minus (S union T_6), and C=Src_R5(D) intersect End_R5(D). Under the inherited valid-b capacity premises,

\[
\boxed{|R|+|C|\le b+5,\qquad |X|\le3b+5-|C|.} \tag{A}
\]

In the full X80 case with b=25 this forces w=|C|=0, independently of j+m'=25. The proof constructs the actual D7 residual S union C; it does not presume an exchange or charge individual suppliers. Section 8 gives the full proof and the audit showing that a second full core H' is unnecessary for the parameterized statement. The surviving C-empty class is not excluded, and the global working chain 40/50/80/81 does not change.

Sections 2--7 preserve this turn's derivation history: the blue-free union and Hall observations, the earlier weaker bounds j+q+w<=25 and t+q+w<=25, and the failed stronger closures. Those weaker exclusions are superseded by section 8, not independent additional numerical gains. Their references to the main or strongest result describe the intermediate stage only; the final result is (A).

## 1. Sources, exact objects, and inherited facts

Primary sources read directly include [the latest main support-barrier note](N7_H50_R30_COMMON_SATURATION_AND_FULL_SUPPORT_BARRIERS_20261029.md), its three branch sources [A](N7_BRANCH_A_H50_R30_JOINT_EQUALITY_20261029.md), [B](N7_BRANCH_B_TIGHT_MISSING_CORNER_JOINT_SUPPORT_20261029.md), and [C](N7_BRANCH_C_MUS_DESCENT_AND_SIMULTANEOUS_REPAIR_20261029.md), [R25 sections 3--6](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md), [R23 full saturation](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md), [R20 canonical closure](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md), and [R7 residual theorem](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md). Their evidence levels are not upgraded. The earlier [full-pair-fan note](N7_FULL_PAIR_FAN_BOUNDARY_AND_TIGHT_CORE_DICHOTOMY_20261029.md) and its strict-Hall branch section 7 remain inherited work.

Fix one actual complete ordered rank-3 signotope X80, with no B6, R7, or weak7. Paths count vertices; weak7 compares opposite-color paths with the same actual endpoints and length sum at least nine. The four-point packet has at most one sign change. All induced paths and states are internal to the indicated actual subsets.

Use ambient red-six source and terminal sets

\[
S=\operatorname{Src}_{R6}(X),\quad T_6=\operatorname{End}_{R6}(X),\quad
H=X\setminus S,\quad H'=X\setminus T_6.
\]

The canonical equality results give |S|=|T_6|=30, |H|=|H'|=50. No point of H starts an ambient R6 and no point of H' ends one. Put

\[
I=S\cap T_6,\quad P=S\setminus T_6,\quad Q=T_6\setminus S,
\quad D=X\setminus(S\cup T_6),
\]

with |I|=5+q, |P|=|Q|=25-q, |D|=25+q and 1<=q<=10. Here Q is a point set, not the global N767 number.

Let U_D=Src_R5(D), V_D=End_R5(D), each of size q, and let

\[
C_0=U_D\cap V_D,\qquad w=|C_0|,\qquad 1\le q-w\le q.
\]

The notation C_0 is local to this note and means this intersection; some older sources use C0 for D minus the union instead. No formulas from those differently named sets are substituted here.

Inside H', write K'=Src_R5(H'), F'=End_R5(H'), L'=Src_B5(H'), E'=End_B5(H'). Full saturation gives K' disjoint-union E'=H'=L' disjoint-union F', each set of size25. In particular

\[
K'=P\sqcup U_D,\qquad E'=D\setminus U_D.
\]

Let J=P intersect Src_B5(X), j=|J|; its reverse counterpart is J_T=Q intersect End_B5(X), t=|J_T|. R25 gives j,t>=15 and the ambient role exclusion

\[
S\cap\operatorname{End}_{R5}(X)\cap\operatorname{Src}_{B5}(X)=\varnothing. \tag{1}
\]

Consequently J contains no ambient red-five terminal. Let m'=|K' intersect F'|, with m the corresponding red-through population in H. The inherited range is m,m' in {9,10}, j,t in {15,16}, and j+m'<=25, t+m<=25. In the primary equality j+m'=25,

\[
J=K'\setminus F',\qquad U_D\subseteq F',\qquad
K'\cap F'=(P\setminus J)\sqcup U_D. \tag{2}
\]

Thus every U_D point has red-five incoming and outgoing suppliers in H'. These are ambient-to-H' roles, not automatic internal attainment in K'.

## 2. The missing global blue-terminal fact

**Lemma.** No point of S union U_D is an ambient B5 terminal.

For s in S, take an actual R6 starting at s. If a B5 ended at s, the bridge between its penultimate vertex, s, and the red path's second vertex would be blue or red. Blue appends a vertex to B5 and gives B6; red prepends a vertex to R6 and gives R7. Both are impossible.

For b in U_D, take an actual R5(b,d2,d3,d4,d5) entirely in D. If a B5 ended at b, a blue bridge gives B6. A red bridge gives an actual R6 ending at d5 in D, impossible because D contains no ambient red-six terminal. This argument applies to every actual incoming blue path and every indicated outgoing red supplier. QED.

The U_D conclusion is also consistent with the old R25 identity End_B5(X)=E_H union E': U_D is contained in K_H and so avoids E_H, and E'=D minus U_D. The direct proof above makes the exact source of the global prohibition explicit.

This corrects an unnecessary possibility left open in the preceding support-barrier note: its mixed B5 paths were localized to end in U_D, but that global terminal role is itself impossible. The historical note is not edited here.

## 3. Full common-P union: all mixed violations are red-six

Choose the canonical five-point endpoint transversal Z subset I of R=S, and put

\[
A_0=I\setminus Z,\qquad B_0=U_D,\qquad
Y=P\sqcup A_0,\quad K'=P\sqcup B_0,\quad
\mathcal U=P\sqcup A_0\sqcup B_0.
\]

Both Y and K' are actual 756 cores of size25; |A_0|=|B_0|=q. The previous mixed-path endpoint classification remains valid, but Lemma 2 strengthens it:

* U has no B5 at all, since none of its vertices can be an ambient B5 terminal.
* Every R6 in U meets both A_0 and B_0, because deleting either part leaves a 756 core.
* Every such R6 ends in A_0; its B_0 vertices are internal. P does not meet T_6, and D contains no R6 source or terminal.
* For every a in A_0, K'+a has26 points and no B5, so it has an R6 ending at a. For every b in B_0, Y+b has26 points and no B5, so it has an R6 with b internal. Both statements retain all alternatives and all other mixed paths.

The R6 transversal number of U is exactly q. A transversal F leaves a no-B5/no-R6/no-weak7 configuration, giving 25+q-|F|<=25. Deleting A_0 or B_0 supplies the matching upper bound.

Define the actual incidence graph on A_0 by B_0: b is a neighbor of a precisely when some actual R6 in U ends at a and contains b. For any A subset A_0, (A_0 minus A) union N(A) hits every R6 in U. Therefore q-|A|+|N(A)|>=q, proving Hall. The graph has a perfect matching, every matched incidence has b<a, and in increasing order

\[
b_i<a_i\qquad(1\le i\le q). \tag{3}
\]

For the last assertion, if b_i>=a_i then the first i vertices of A_0 would have fewer than i possible earlier B_0 neighbors. This is an incidence matching, not a collection of internally disjoint paths and not a matching of actual R6 first endpoints.

Equivalently, for every cut c the induced configuration P union (A_0 at or before c) union (B_0 after c) has no R6 by the endpoint order restriction, and no B5 by Lemma 2. Capacity gives the same prefix inequality #A_0<=c <= #B_0<=c. This restatement does not add another capacity charge.

## 4. Main theorem: restore all five transversal points and build a residual set

The first version of this argument used J union A_0 union C_0. The stronger construction restores **all** five points Z and uses

\[
\boxed{W=J\sqcup I\sqcup C_0.} \tag{4}
\]

It is an actual induced subset of X. Its size is j+5+q+w. Lemma 2 applies to all its vertices, because J and I lie in S and C_0 lies in U_D. Thus W has no B5; more strongly, none of its vertices can be the terminal of an ambient B5.

**Claim: no point of I starts a B4 contained in W.** Take i in I, an ambient R6 ending at i, and suppose B4(i,x,y,z) lies in W. Let r be the incoming red path's penultimate vertex. If chi(r,i,x) is red, appending x gives R7. If blue, (r,i,x,y,z) is an ambient B5 ending at z in W, contrary to Lemma 2. Both colors are impossible. Only one new consecutive triple is used in either extension.

**Claim: no point of C_0 starts a B4 contained in W.** For c in C_0 subset V_D, take an actual R5 entirely in D ending at c, with penultimate vertex r. A proposed B4(c,x,y,z) in W has a bridge chi(r,c,x). Blue gives an ambient B5 ending at z in W. Red appends x to the D-red-five path, giving an ambient R6 whose first vertex lies in D. Global source closure excludes it. Again both colors are impossible, and no assumption about x's role is needed.

Finally no point of J ends any ambient R5, by (1). Every point of W is in exactly one of these three sets. Hence W contains no point that simultaneously ends an internal R5 and starts an internal B4. It inherits no weak7 and no R7 from X. Therefore W satisfies the **exact R7 residual D7 hypotheses**: no B5, no weak7, and the internal R5-terminal/B4-source prohibition.

R7's bound D7<=b+5=30 applies, and gives

\[
j+5+q+w=|W|\le30,\qquad\boxed{j+q+w\le25}. \tag{5}
\]

This proof treats every possible internal path in W, including paths meeting several restored Z points or mixing J,I,C_0. It is not a proof about a convenient list of private paths. The required support information is global and actual: outgoing D-red-five supplies exclude blue-five terminals, and incoming D-red-five supplies then exclude blue-four starts on C_0.

For completeness, the residual bound used here has the following short mechanism. Let E be the internal R6 terminal set of a D7 configuration. If e in E began an internal B3, the bridge from its incoming R6 either gives R7 or gives an internal B4 beginning at the R5 prefix terminal, forbidden by the residual condition. Thus every e is a right red root, E is a red chain, and |E|<=6. If |E|<=5, delete E. If E={e1<...<e6}, every R6 ending at e2 starts at e1: a later start permits prepending e1 to make R7; an earlier start forces the red triple through e1,e2 by same-endpoint weak7 and then prepends that start to the red E chain to make R7. Deleting E minus {e2} therefore hits all R6. The remainder is a 756 core of size at most b, proving D7<=b+5. No external certificate beyond the inherited b bound is introduced by this use.

Reverse the actual order while retaining colors and apply the same theorem to the reversed configuration. Sources and terminals exchange, U_D and V_D exchange, and J becomes J_T. This proves

\[
\boxed{t+q+w\le25}. \tag{6}
\]

The proof does not require j+m'=25, although that equality supplies the requested stronger interpretation below.

## 5. Exact excluded classes and the equality interpretation

Equations (5)--(6) give

\[
q+w\le25-\max(j,t)\le10.
\]

If j=16 or t=16, the right side is at most nine. Together with q-w>=1, this implies 2w+1<=10, hence w<=4.

Under the primary equality j+m'=25,

\[
\boxed{q+w\le m',\qquad |P\setminus J|=m'-q\ge w.} \tag{7}
\]

The latter is a cardinality consequence of the proved actual residual configuration, not a pairing of individual owners or of missing states. If the reverse equality also holds, q+w<=min(m,m'). No injection from C_0 to P minus J, no unique supplier, and no exclusive support allocation is asserted.

Thus joint instances with q+w>m' are impossible in the primary equality class. In particular q=10 forces w=0 and j=t=15; q=9 allows w<=1 when j=t=15 and forces w=0 if either count is16. These exclusions cover all actual colorings and alternative paths under the stated canonical premises, rather than only a template of private witnesses.

The displayed old scalar inequalities did not imply (7). For example, the formal tuple m=m'=10, j=t=15, q=6, w=5 satisfies the previously listed numerical constraints, including q-w>=1 and the old m+m'+q-w>=15, but violates (5). This tuple is only a witness to the difference between scalar constraint sets; it is not asserted to be realized by a signotope. No claim of literature-wide novelty is made.

## 6. Failed stronger attempts and the remaining equality branch

Three genuinely different stronger closures were attempted before the residual construction.

**Direct through-supplier gluing.** For b in B_0 under (2), R23 gives pure incoming R5(L'^4,b), whose source belongs to K' intersect L'=J, and pure outgoing R5(b,E'^4), which lies wholly in D. For any incoming penultimate r and outgoing second vertex u, chi(r,b,u)=B because the two red suppliers lie in the R6-free H'. More generally chi(r,b,z)=B for every later z in H', since red would create an R6 ending in H'; and chi(v,b,u)=B for every earlier v in H, since red would create an R6 starting in H. These full fans are valid, but the neighboring vertices of a mixed carrier need not belong to the supplier families. The incoming r is a blue-five source in H', not a certified blue-five terminal; u is a blue-five terminal, not a certified source. Using those roles in the wrong direction does not yield B6.

**Full50 replacement.** The natural candidate H*=(H' minus B_0) union A_0=Y union E' has50 points. The classification of paths in U does not prove H* is R6-free, because E' lies outside U. A red-six path may start in P, end in A_0, and use E' while avoiding B_0. Until all those actual paths are hit, H* is not a certified full766 core, so the R25 recomputed role-cover argument cannot be invoked there.

**Internal attainment and private-only matching.** Deleting the internal b from any R6 in Y+b gives an actual Y-red-five path with the same A_0 terminal. Deleting the terminal a from any R6 in K'+a gives an actual K'-red-five path ending at a through owner in (P minus J) union B_0. These are valid individual attainment statements. They do not prove that every B_0 vertex is an internal K' red-five terminal, nor that every A_0 vertex is a Y red-five terminal. Paths containing several B_0 points can end at an A_0 point not covered by the singleton deletion statement. The Hall graph in section 3 includes those paths and cannot be replaced without proof by a private-only graph.

The cardinality-support collaborator checked the accepted proof's scope: injection and bad-cell exclusions give missing=e at a full25 core, not an ownerwise charging map or a prescribed ordinary catalog. H'-through identity cannot be transported to K'-internal attainment. No such unsupported state rigidity is used in (5).

The residual construction also has a sharp current limitation. It uses C_0=U_D intersect V_D, not all B_0. For b in U_D minus V_D, equality provides an incoming H'-red-five supply, but its source can lie in J subset S. A red bridge then creates an allowed R6 beginning in S and ending in I; it is not the forbidden D-origin R6 used in section 4. Thus replacing C_0 by all B_0 in W is not justified. The still-live cases satisfying q+w<=m' are not eliminated by the current proof.

## 7. Status and attribution

The new hard use is the legal actual residual set W and the resulting restrictions (5)--(7). It combines the existing canonical closure, the old R25 mixed-role theorem, and the old R7 residual capacity with both actual D-through supplier directions. Packet/path heredity supports the inherited framework; the new bridge checks explicitly use no B6, no R7, and the ambient source/terminal closure. No presumed exchange, exclusive charge, or transported state was used.

The union correction and incidence matching are supporting results; Hall itself and capacity-to-matching are inherited methods. The generic full X80 exclusion remains open, and the stricter equality j+m'<25 is not asserted. Working global bounds remain 40/50/80/81. All new deductions remain unreviewed/unaccepted despite the within-generation cross-challenges; external review calls and scientific execution are zero.

## 8. Same-turn strengthening, 2026-10-29: the D-through intersection is empty

### 8.1 Parameterized capacity relation before specializing the population

The main generator subsequently sharpened the scope. Let b be a valid capacity for the 756 class and its color dual, with the inherited bounds C_7<=2b and D_7<=b+5 and the resulting full2b role-cover theorem. Let X be any actual 767 configuration whose R7 canonical decomposition X=H disjoint union R has |H|=2b. Define S=Src_R6(X), T_6=End_R6(X), D=X minus (S union T_6), and C=Src_R5(D) intersect End_R5(D). Then

\[
\boxed{|R|+|C|\le b+5,\qquad |X|\le3b+5-|C|.} \tag{8}
\]

Here D need not have the earlier q-parameterized size, and no second full core H' or equality j+m'=b is assumed.

The exact dependency audit is as follows. R20 sections 5.2--5.6 at deficit d=2b-|H|=0 give no ambient R6 starting in H and S=R. For every r in R, capacity forces an R6 in H+r; its source must be r, so its remaining five vertices lie in H. This supplies the pure H tail needed in the R25 swap proof independently of |R|.

To see that the mixed-role exclusion also persists, suppose a in S ends an ambient R5 and starts an ambient B5. The R7 three-chain theorem forces the terminal of every outgoing R6 to equal the second vertex of every outgoing B5. Call this common point h; the pure H tail makes h belong to H. The actual swap H_a=(H minus {h}) union {a} is R6-free: old H points cannot start ambient R6 and all R6 from a end at the deleted h. It is a full2b 766 core, and a cannot start an internal B5 because all such ambient paths use h as second vertex. The recomputed full-core cover therefore gives an internal R5 ending at a. With any B5(a,h,...), a blue joining triple prepends that R5's penultimate vertex to give B6; a red joining triple appends h to the R5 and gives an ambient R6 starting in old H. Both are impossible. Thus S intersect End_R5(X) intersect Src_B5(X) is empty under these weaker premises.

The path argument below now applies verbatim to W*=S union C, using U*=S union Src_R5(D), the actual ambient T_6, and the unrestricted canonical fan. It proves W* is an actual D7 residual. Since C is contained in D and S=R, its capacity is exactly (8). In particular |X|=3b+5 forces C empty; at b=25 this is the w=0 theorem below. Formula (8) is conditional on a canonical full2b H, and does not imply an unconditional Q_7<=3b+4 because C may be empty.

### 8.2 Complete path proof and specialization to X80

After the preceding argument was written, the main generator supplied a stronger residual construction. The unrestricted ambient extension fan in R7 section 2 is essential here: every blue path whose terminal belongs to canonical P_+ can append the actual p(terminal), with no condition on the earlier path vertices. Direct inspection of that source confirms this quantifier. The argument below supersedes the weaker exclusion q+w<=m' as this note's strongest conclusion. It remains mathematical generation, unreviewed/unaccepted.

**Theorem.** Under the actual joint X80 premises of section 1, U_D intersect V_D is empty, so w=0. The equality j+m'=25 is not needed.

**Proof.** Set U*=S union U_D and W*=S union C_0, where C_0=U_D intersect V_D. Section 2 proves that no point of U* is an ambient blue-five terminal. In particular W* is blue-five-free.

First, every ambient blue-four path ending at a point v of U* extends to an ambient blue-five path, preserving its source. If v belongs to S, then v belongs to canonical P_+: otherwise the R7 fan for P_- would prepend a point to an ambient red-six starting at v, producing a forbidden red-seven. The unrestricted P_+ fan therefore appends p(v) to the given blue-four. Its other vertices may lie anywhere in X, including C_0 in D.

If v belongs to U_D, choose any actual D-red-five (v,u,u_2,u_3,d). Let r be the penultimate vertex of the blue-four ending at v. If chi(r,v,u) is red, (r,v,u,u_2,u_3,d) is an ambient red-six ending at d in D, contradicting D disjoint from T_6. Therefore this bridge is blue and appending u extends the blue-four. All vertices occur in the required strict order r<v<u<u_2<u_3<d. This proves the extension claim for all ambient blue-four paths with terminal in U*, not only paths in S.

Consequently every source of an internal W*-blue-four is an ambient blue-five source: its terminal is in W* subset U*, and the extension just proved applies.

No c in C_0 can be an ambient blue-five source. Indeed c in V_D has an incoming actual D-red-five (d_1,d_2,d_3,r,c). An ambient blue-five starting (c,x,...) has bridge chi(r,c,x). A red bridge gives a red-six (d_1,d_2,d_3,r,c,x) starting in D, impossible because D is disjoint from S. A blue bridge prepends r to that blue-five, giving a forbidden blue-six. Thus C_0 contains no source of an internal W*-blue-four.

If an internal W*-blue-four instead starts at s in S, the extension claim makes s an ambient blue-five source. R25's actual swap exclusion S intersect End_R5(X) intersect Src_B5(X)=empty then forbids s from ending even an ambient red-five, hence also an internal W*-red-five.

We have proved that W* has no internal red-five terminal that is also an internal blue-four source. It is blue-five-free and inherits no weak-seven from X. Thus it satisfies the exact D_7 residual hypotheses, and the inherited residual bound gives |W*|<=b+5=30. Since S and C_0 are disjoint and |S|=30, |W*|=30+w, forcing w=0. This completes the proof.

This excludes every actual joint instance with w>=1, without assuming role equality, selecting private paths, or allocating supports exclusively. It does not exclude the still-live w=0 joint class. Under primary equality, (7) now reduces to q<=m'; this does not assert additional internal state attainment. The earlier formal scalar example remains evidence that the previous scalar constraints did not themselves force the new conclusion. No global numerical bound is changed.
