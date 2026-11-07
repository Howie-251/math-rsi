# Primary A: same-root supplies in the actual H50 plus R30 equality case

Date: 2026-10-29, subsequent user turn. Mathematical generation only; **unreviewed/unaccepted**. No external or Claude review was requested or attempted in this turn. No science code, enumeration, solver, test, or proof replay was run. Only this fresh note is owned by this branch; previous branch notes and all historical/configuration/task/acceptance files remain unchanged.

The intended target is exclusion of an actual 767 configuration X80 with its canonical H50 and R30. Such an exclusion would imply Q<=79 and, through the inherited exact root reduction, F<=80; it would not prove C<=49. This note does **not** complete that exclusion. It records the audited entry, full same-root families, a forced three-block consequence, and the precise failures of the attempted closure. No new global bound or new entire parameter-branch exclusion is claimed.

## 1. Sources and notation that must not be conflated

The primary canonical sources are [R7, sections 2--3.3](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md), [R20, sections 5--6](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md), [R21, sections 2--3](RESET_R21_GLOBAL_CAPACITY_AND_SUPPLY_REALIZABILITY.md), [R24, section 7](RESET_R24_GLOBAL_COMPATIBILITY_AND_EXTREMAL_REALIZATION.md), and [R25, sections 3--8](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md). Their original evidence status is preserved; historical numerical substitutions in R20/R21 are read through their stated general-b arguments, now using b=25.

Also read were [R23](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md), [Oct28 saturated interfaces](N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md), [the latest full-pair-fan main note](N7_FULL_PAIR_FAN_BOUNDARY_AND_TIGHT_CORE_DICHOTOMY_20261029.md), and all three preceding Oct29 branch notes: [tight cores](N7_BRANCH_A_HALL_TIGHT_CORES_20261029.md), [strict Hall, including section 7](N7_BRANCH_B_STRICT_HALL_SUPPORTS_20261029.md), and [critical blockers](N7_BRANCH_C_CRITICAL_BLOCKER_PROPAGATION_20261029.md). The Through14/Joint17 inputs retain the limitations stated in [common assignment](BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md) and [the global frame](N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md).

X is one complete ordered rank-3 signotope with no B6, R7, or weak7. Paths count vertices. Weak7 compares opposite-color paths with the same actual endpoints and length sum at least nine. Four-point packet order is abc, abd, acd, bcd, with at most one color change. All induced paths and identities are recomputed in the actual indicated subset.

To avoid a serious notation collision, write

\[
S=\operatorname{Src}_{R6}(X),\qquad T_6=\operatorname{End}_{R6}(X),
\]

for the two ambient thirty-point sets, and write **Z** for a five-point minimum transversal of R6 inside R=S. Thus Y=R\Z. Z is the small transversal called T in the task request; it is never T_6.

## 2. Legal canonical entry: R really has no B5

R7 chooses the global minimum-pair map p and its two sign classes P_+,P_-. A B5 lying inside P_+ has its last vertex in P_+ and can be extended by p(last) to an ambient B6. Hence P_+ has no B5. With G the specified internal mixed-role subset, the canonical partition is

\[
H=P_-\cup G,\qquad R=P_+\setminus G.
\]

Therefore R has no B5; this does not follow merely from X having no B6. R also inherits the residual prohibition that a point cannot simultaneously end an internal R5 and start an internal B4. R7's residual five-point transversal proof applies on these exact premises and gives tau_R6(R)<=5.

For a minimum transversal Z, Y=R\Z has no B5, R6, or weak7. Thus |Y|<=b=25. At |R|=30 this gives |Z|>=5, hence

\[
|Z|=5,\quad |Y|=25,
\quad \operatorname{End}_{R5}(Y)\cap\operatorname{Src}_{B4}(Y)=\varnothing. \tag{1}
\]

The last condition is inherited from R, and must not be dropped by treating Y as an arbitrary full756 core.

R20's full-path endpoint closure and zero-deficit arguments, with |H|=2b=50, give

\[
S=R,\quad |S|=30,
\qquad\text{no ambient R6 starts in H}. \tag{2}
\]

In particular, for every v in R, H+v has an R6 by C<=2b; every such R6 starts at v and its five remaining vertices lie in H. This statement is valid for all alternatives, including paths whose endpoint varies. Its endpoint conclusion comes from (2), not from capacity alone.

For each fixed z in the **same** Z, retain the complete families

\[
\mathcal P_z=\{P\subseteq Y+z:P\text{ is an actual R6}\},\qquad
\mathcal Q_z=\{Q\subseteq H+z:Q\text{ is an actual R6}\}.
\]

Both are nonempty. For P_z this follows from minimum-transversal private-path reasoning: if no R6 met Z exactly at z, removing z from Z would still hit every R6. Every P in P_z meets Z exactly at z; there is initially no restriction on z's position. Every Q in Q_z starts at z by (2). The two paths share only z, because Y and H are disjoint. No common-pair gluing is available from this fact alone.

These are retained full families, not an assertion that singleton traces suffice for an exchange. Paths meeting several points of Z, paths mixing H and Y, and all alternative private paths remain ambient constraints. They are not deleted from the problem because the notation displays the singleton families.

## 3. A special legal minimum transversal with terminal localization

Let E=End_R6(R). R7 proves that E has no internally starting B3, that it is a red chain, and that |E|<=6. Since E hits all R6 and tau=5, |E| is five or six.

If E={e1<...<e5}, choose Z=E. Every private path in P_ei ends at ei: its terminal belongs to E and it meets E only at ei. Thus **all five** same-root families are endpoint-localized.

If E={e1<...<e6}, R7 proves that every R6 ending at e2 starts at e1 and that Z=E\{e2} is a transversal. It has size five and is minimum. For z in {e3,e4,e5,e6}, a private path cannot end at e2, because that would require the excluded e1 in addition to z. It cannot end at another member of Z. Therefore every such private path ends at z. A private path for z=e1 can end at e1 or e2; both alternatives must be retained. Thus **at least four**, not automatically five, roots are endpoint-localized in this case.

This argument is special to the chosen endpoint transversal. It does not endpointize every private family for every minimum transversal, and it does not overwrite the general full-core insertion barriers in the previous sources.

For any endpoint-localized z, choose any P in P_z, and let u be its penultimate vertex. Choose any Q in Q_z, and let h be its second vertex. Then u<z<h, and

\[
\chi(u,z,h)=B. \tag{3}
\]

Indeed a red bridge would extend the actual P to an R7. It would also prepend u to the actual Q. This is a universal constraint on all such same-z pairs of alternatives. It provides a B3, not a B6 or a weak7 with certified common endpoints.

The full R6 endpoint fan is also useful but has a precise limit: any actual R6 from a to b forces

\[
\chi(a,x,b)=R\quad\text{for every actual }a<x<b, \tag{4}
\]

because a blue triple would be a same-endpoint B3 against R6. It includes intermediate vertices outside that particular path.

## 4. All H tails of a private penultimate point, and three ordered R5 blocks

R20 section 6.3 supplies a stronger full-family localization than (3). For any R6 inside R with penultimate u and last vertex z, **every** ambient R6 starting at u ends at or before z. To see this directly, an R6 from u to h>z would force chi(u,z,h)=B to avoid extending the original R6 to R7. That B3 would have the same endpoints u,h as the second R6, contradicting weak7.

Since u belongs to R, it has an H-tail R6(u,H^5). Its endpoint lies in H and cannot equal z in R. Hence every such H-tail lies wholly inside (u,z). Its five H vertices form an actual R5. By contrast, every H-tail from z lies after z. These two supports are genuinely disjoint by order; supports belonging to different roots need not be disjoint.

Combining this with the old five/six-root construction gives a further necessary consequence for the entire joint class:

**Three-block consequence.** H contains three actual R5 paths A<B<C, with every vertex of A before every vertex of B and every vertex of B before every vertex of C.

For |E|=5, use a private path ending at e1 and its penultimate u. An H-tail of u supplies A inside (u,e1). R21 section 2.4 supplies an actual R6(a,e1,e2,e3,e4,e5) with a<e1. Its penultimate e4 forces an H-tail B of e4 inside (e4,e5). An H-tail C of e5 lies after e5. These intervals are disjoint and ordered.

For |E|=6, use a private path ending at e3 for Z=E\{e2}; its penultimate u has an H-tail A before e3. E itself is an R6, so an H-tail B of e5 lies in (e5,e6). An H-tail C of e6 lies after e6. Again A<B<C. This proves the assertion in both canonical endpoint cases, without assigning distinct supports to all five roots.

This is a necessary support structure obtained from the same X, not a claim that a full H50 with this structure exists. It is not yet an exclusion. A failed final attempt tried to derive B6 from these three ordered red blocks. No R6 gives B4 on the last pair of A and the first pair of B, and another B4 on the last pair of B and the first pair of C. The two middle pairs are different. To concatenate into B6 one needs a single actual pair x<y in B such that both chi(last(A),x,y) and chi(x,y,first(C)) are blue. Neither displayed B4 guarantees that. The missing common middle pair is the exact gap.

The Through14 input also does not repair this gap automatically. A red block's first vertex is a red-five source and its last vertex is a red-five terminal; they are not thereby vertices having both roles. No fourteen distinct actual through vertices were obtained. Consequently the three-block consequence is not counted as a new critical-case exclusion or a numerical improvement.

## 5. Joint equality has the narrower inherited m range

The reversed canonical decomposition gives |T_6|=30 and H'=X\T_6 of size50. Put

\[
I=S\cap T_6,\quad |I|=5+q,\qquad
P=S\setminus T_6,\quad Q=T_6\setminus S,\quad
D=X\setminus(S\cup T_6).
\]

Then |P|=|Q|=25-q and |D|=25+q. R21 and R24 give 1<=q<=10. The symbol D here is the common neutral configuration, not the double-terminal atom of an individual fifty-point core.

Use R25's names K,E_H,L,F for the four size25 source/terminal sets in H, and their primed versions in H'. Define m=|K intersect F| and m'=|K' intersect F'|. R25's actual swap theorem says

\[
S\cap\operatorname{End}_{R5}(X)\cap\operatorname{Src}_{B5}(X)=\varnothing,
\]

with the reversed dual. Let J=P intersect Src_B5(X), j=|J|. The inherited ambient blue-source count gives j>=15, and R25 gives j<=25-m'. The analogous terminal quantity j_T satisfies 15<=j_T<=25-m.

Combining these old joint-class inequalities with the later Joint17 lower bound m,m'>=9 yields

\[
m,m'\in\{9,10\},\qquad j,j_T\in\{15,16\}. \tag{5}
\]

In particular j=16 forces m'=9, and m'=10 forces j=15. This is a combination of inherited results, not a newly proved branch exclusion here. Independent H50 still has the previously stated wider 9..13 range; (5) uses its joint embedding into X80.

Every penultimate u from section 3 belongs to End_R5(Y), hence to End_R5(X), and to S=R. The swap theorem makes u a non-source of ambient B5. This is a genuine identity restriction, but different private paths or different roots can have the same u.

## 6. Two actual full25 cores with a common P, and the terminal-count gap

For the canonical small transversal Z, one has Z subset E subset I. Since no point of T_6 starts an ambient B5, J avoids Z and lies entirely in Y. Therefore

\[
\operatorname{End}_{R5}(Y)\subseteq Y\setminus J.
\]

Deleting all R5 terminals from Y leaves no B5 or R5, so the classical (4,4) capacity20 gives the exact safe interval

\[
5\le |\operatorname{End}_{R5}(Y)|\le25-j\le10. \tag{6}
\]

For j=16 the upper bound is nine. There is no proof here that a general full Y has eleven red-five terminals, or even that equality holds at the upper end of (6). The residual condition (1) restricts their internal B4-source status but does not on its own supply that missing lower bound.

There is a real second full25 core sharing all P. R21/R25 give U_D=Src_R5(D), |U_D|=q, and

\[
Y=P\sqcup(I\setminus Z),\qquad K'=P\sqcup U_D.
\]

Both have size25 and no B5/R6/weak7, internally recomputed. This is a replacement of q actual owners, not an asserted legal exchange taking intermediate configurations through the capacity class. When j+m'=25, J is exactly K'\F', so U_D is contained in F' and

\[
K'\cap F'=(P\setminus J)\sqcup U_D.
\]

The corresponding possible terminal container in Y is (P\J) union (I\Z), of the same size m'. Actual R5 terminals of Y lie in that container; they have not been proved to fill it. If j+m'<25, its slack is one in the remaining range, and that equality argument must not be used.

In particular, the union Y union K'=P union (I\Z) union U_D is not proved to remain a 756 core. A new path can use vertices from both replacement sets, and neither individual full25 core tests that mixed support. Deleting some owners to accommodate the union must hit all such actual mixed paths as well as the old private families. No permitted repartition or common-path transversal follows from the shared P alone.

For comparison, V=End_R5(R) satisfies 10<=|V|<=30-j<=15: the lower bound follows by deleting V and using classical capacity20, and the upper bound follows from the swap theorem. This weaker residual count does not manufacture independent costs in addition to (6).

## 7. Final same-j supply attempt through the actual blue-source configuration

R25 constructs the actual induced W_B=Src_B5(X)=L disjoint-union J, now of size40 or41 by (5). It proves internally

\[
\operatorname{Src}_{R5}(W_B)=J,
\qquad \operatorname{End}_{R5}(W_B)=M_-,
\]

and gives two full25 cores L and L'. Thus every same j in J has at least one R5 tail in W_B ending at some z in M_-, with all alternatives retained.

Every ambient B5 **from that z** has its second vertex in T_6: adjoining it to any actual R5 ending at z gives R6. If the B5 is chosen inside H, as is possible because z belongs to L, its second vertex q0 also belongs to H and therefore lies in Q. In particular the W_B R5 from j extends to an actual R6 from the same j to q0 for every such H-internal blue supply. This is an existing full-supply fact of R25. Ambient blue supplies need not have their second vertex in Q; the H-internal qualifier is essential. Nor can it be restated as “every B5 from j has second vertex in Q”: j lacks the incoming R5 hypothesis needed for that conclusion.

The attempt was to join such same-j tails to the private extensions of Y and force a point of End_R5(Y) to start an internal B4, violating (1), or to make a member of J end an ambient R5, violating the swap theorem. No such joint was proved. J is large enough that internal R4s are forced, but an incoming R4 is one vertex short of the incoming R5 required by the existing three-chain/swap argument. A single new bridge does not certify the two consecutive triples needed for an insertion or the same actual endpoints needed for weak7. The W_B red supply may use other J owners internally and need not share a pair with any private Y+z supply.

Equations (3)--(4), the two full25 cores, and the W_B supplies are simultaneous actual restrictions. They are not an existence proof for a repartition, and they do not eliminate multi-Z or mixed H/Y witnesses. The first unresolved step is an actual common-support or extension theorem joining these separately guaranteed paths. No such theorem was obtained in the concentrated attempt.

## 8. Outcome

The full canonical entry is legal and the same-root H supply is endpoint-localized for the correct reason. A canonical endpoint transversal additionally localizes all private families in the five-endpoint case and four of them in the six-endpoint case. Together with R21/R20 it forces three ordered disjoint H red-five blocks. This is an old-derived support corollary; genuinely new hard exclusion in this branch: **none**. The joint-class parameter range is m,m' in {9,10}, inherited from the indicated source combination. The terminal counts and the two actual shared-P cores further specify the remaining equality case.

None of these deductions closes H50 plus R30. No claim is made that the remaining patterns are realized by an actual X80, and no abstract support family is offered as such a counterexample. New global decrease: zero. Q<=79, F<=80, and C<=49 remain unproved by this note. All generation remains unreviewed/unaccepted, with zero external review calls this turn.
