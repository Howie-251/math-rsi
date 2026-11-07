# Branch A: residual equality, exact endpoint count, and full blue-four supports

Date: 2026-10-29. Mathematical generation only, **unreviewed/unaccepted**. This fresh note is the sole file owned by this branch in this turn. No scientific code, enumeration, SAT, solver, proof replay, external review, or independent review was performed. Other generators' cross-challenges do not change that status.

The main result is that an actual common-equality X80 must have exactly five internal red-six endpoints in its canonical residual S. The previously possible six-endpoint branch is excluded by an actual residual deletion that retains all mixed blue-four paths. More precisely, an all-support second-vertex graph satisfies Hall, and its full deletion produces a second actual 30-point residual with the same five endpoints. A further order consequence makes the last two endpoints the last two vertices of S union U_D. None of these conclusions excludes the remaining five-endpoint common realization or changes 40/50/80/81.

## 1. Sources and exact scope

Read sources include [the latest main note](N7_NEUTRAL_THROUGH_RESIDUAL_AUGMENTATION_AND_MUS_SUPPORT_20261029.md), [the prior A note, final parameterized section 8](N7_BRANCH_A_JOINT_ROLE_EQUALITY_RIGIDITY_20261029.md), [R7 sections 2 and 3](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md), [R20 sections 5.2--5.6](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md), [R23](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md), [R25 sections 3.1--3.2](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md), and [R5's actual support and point-pair comparison mechanisms](RESET_R5_COVER_AUGMENTATION_CAPACITY.md). Historical scope and acceptance are unchanged.

Work in one actual ordered rank-3 signotope X of size80, with no B6, R7, or weak7. Paths count vertices. Weak7 compares opposite-color paths with the same actual endpoints and length sum at least nine. All induced roles below are recomputed in their stated sets.

Use S=Src_R6(X), T=End_R6(X), H=X minus S, H'=X minus T. Canonical equality gives |S|=|T|=30, |H|=|H'|=50. S is the actual R7 residual: no B5 and no internal End_R5/ Src_B4 intersection. Let

\[
I=S\cap T,\quad P=S\setminus T,\quad
D=X\setminus(S\cup T),\quad
U_D=\operatorname{Src}_{R5}(D),\quad V_D=\operatorname{End}_{R5}(D).
\]

Inherited identities give |I|=5+q, |P|=25-q, |U_D|=|V_D|=q, and the actual full756 core K'=P disjoint union U_D. The prior turn's residual augmentation forces U_D intersect V_D empty. This exclusion is inherited, not a new result of this note.

Set

\[
\mathcal U^*=S\sqcup U_D,\qquad
E=\operatorname{End}_{R6}(S).
\]

Here E always means the internal S red-six endpoint set, not the old H blue-five terminal notation. E is a subset of I. The inherited R7 argument gives |E|<=6 and every e in E is a right-red root in S: chi(e,x,y)=R for all e<x<y in S. The residual five-transversal bound and the full756 capacity imply tau_R6(S)=5: deleting fewer points would leave more than25 points with neither B5 nor R6. Hence |E| is either5 or6. Every five-point transversal Z of all S-red-six paths leaves an actual full756 set S minus Z. No claim that all such Z are endpoint sets is made.

We use three inherited ambient facts, proved for all paths in the prior main note:

1. No point of S union U_D ends an ambient B5. Thus U* is B5-free.
2. Every ambient B4 whose terminal belongs to U* extends to an ambient B5, preserving its source. At S terminals this is the unrestricted canonical fan; at U_D terminals it uses an actual D-red-five successor and excludes an R6 ending in D.
3. S intersect End_R5(X) intersect Src_B5(X) is empty, by the R25 actual full-core swap.

## 2. This turn's full junction attainment and all-support second vertices

The B collaborator and main generator supplied the following new residual-deletion observation. It is included with proof because its full-path quantifier is essential here.

Compute G=End_R5(U*) intersect Src_B4(U*) internally. Every internal B4 extends ambiently by fact2. Thus an element of G in S would contradict fact3; consequently G is a subset of U_D. The induced U* minus G has no internal R5-terminal/B4-source intersection, since any such surviving intersection would already belong to G. It is B5-free and inherits no weak7, so is an actual D7 residual. Its size is 30+q-|G|, and the inherited D7 capacity30 forces |G|>=q. Therefore

\[
G=U_D. \tag{1}
\]

The same proof applied separately to S plus {u}, for each u in U_D, gives actual pure supplies R5(S^4,u) and B4(u,S^3). These singleton supplies do not replace the complete families in U*; they merely certify existence. In particular all paths meeting several U_D points remain in scope.

Fix u in U_D and any actual B4(u,t,x,y) in U*. Pair it with any actual incoming R5 in U* ending at u, with penultimate vertex r. A blue chi(r,u,t) prepends r to the B4 and makes a B5 ending in U*, impossible by fact1. Hence the bridge is red, and appending t to that R5 gives R6. Since t belongs to U* intersect T, it lies in I. Thus

\[
\text{every U*-blue-four from U_D has its second vertex in I.} \tag{2}
\]

This is valid for every choice of incoming and outgoing support; it assigns no exclusive resource to either.

## 3. Internal residual endpoints are right-red roots throughout U*

**Lemma.** Every e in E satisfies chi(e,x,y)=R whenever e<x<y lie in U*.

**Proof.** Choose an actual R6 wholly in S ending at e, with penultimate vertex r. Then r belongs to S and ends an ambient R5. Suppose B3(e,x,y) lies in U*. If chi(r,e,x) is red, append x to that R6 to get R7. If it is blue, (r,e,x,y) is a B4 ending in U*, so fact2 extends it to an ambient B5 starting at r. This contradicts fact3 at r. Both cases are impossible. This proof permits x or y to lie in U_D. It does not assume that a right-root identity is preserved merely by enlarging its induced set. QED.

Combining this lemma with (2), every U*-B4(u,t,x,y) with u in U_D has

\[
t\in I\setminus E. \tag{3}
\]

## 4. Actual residual deletion gives Hall and excludes E6

Define a bipartite graph on U_D and I minus E by putting an edge u--t exactly when an actual B4(u,t,x,y) exists in U*. Include all witnesses, including every mixed or multi-U_D path. For A subset U_D, write N(A) for all its second-vertex neighbors and form the actual induced set

\[
W_A=(S\setminus N(A))\sqcup A.
\]

It is B5-free. Any internal R5-terminal/B4-source intersection would already be such an intersection in U*, hence lie in U_D by (1), and therefore in A. But a B4 from any point of A must have second vertex in N(A), all of which have been removed. Thus W_A is an actual D7 residual. Its capacity yields

\[
30-|N(A)|+|A|\le30,
\qquad |N(A)|\ge|A| \quad\text{for every } A\subseteq U_D. \tag{4}
\]

Taking A=U_D gives

\[
q\le|I\setminus E|=5+q-|E|,
\]

so |E|<=5. Since tau_R6(S)=5 and E itself is a transversal, |E|>=5. Consequently

\[
\boxed{|\operatorname{End}_{R6}(S)|=5.} \tag{5}
\]

This excludes the entire actual E6 branch. The root's equivalent proof deletes the whole set I minus E at once; (4) additionally retains the all-subsets support consequence.

Write A_0=I minus E. It has q points. Hall gives a perfect matching from U_D to A_0. Each matched pair u--t has u<t. Consequently, listing both sets in increasing order u_1<...<u_q and a_1<...<a_q gives u_i<a_i for every i. Every a in A_0 occurs as the second vertex of at least one actual U*-B4 starting in U_D. The matching concerns second vertices, not internal disjointness of the full blue paths or distinct red suppliers.

For A=U_D, (4) and equal population give N(A)=A_0. Hence

\[
W_0=(S\setminus A_0)\sqcup U_D=K'\sqcup E
\]

is an actual D7 residual of size30. Its red-six endpoints are exactly E. They are contained in E because U_D and P avoid ambient T. Conversely, for each e in E, the26-point B5-free set K' plus {e} must contain an R6, necessarily ending at e. Thus E is a minimum five-transversal in both S and W_0. Those K'+e paths may lie in P+e; they are not required to use U_D.

## 5. Sharpened endpoint-order restriction using the old extended root path

Write E={e_1<e_2<e_3<e_4<e_5}. Then

\[
\boxed{\mathcal U^*\cap(e_4,\infty)=\{e_5\},\qquad
U_D\cup A_0\subset(-\infty,e_4).} \tag{6}
\]

Thus e_4,e_5 are the last two vertices of U*. In particular every point of P, including J=P intersect Src_B5(X), also precedes e_4. The initial version of this section allowed at most one P minus J point between e_4 and e_5. The following same-turn refinement, supplied by the main generator and C collaborator, eliminates that possibility using the old extended root path from [R21 section 2.4](RESET_R21_GLOBAL_CAPACITY_AND_SUPPLY_REALIZABILITY.md).

For completeness, reconstruct the actual old path. E is a minimum five-transversal of all S-red-six paths, so E minus {e_2} fails to hit at least one such path. Choose any e_2-private R6. Its endpoint must be e_2, and it avoids e_1 and the other three endpoints. Let a be its source. If a>e_1, right-root e_1 can be prepended, giving R7. Since a is not e_1, necessarily a<e_1. A blue triple (a,e_1,e_2) would share its endpoints with that actual R6 and form weak7. Hence chi(a,e_1,e_2)=R. Together with the root chain E this gives the actual R6

\[
(a,e_1,e_2,e_3,e_4,e_5). \tag{7}
\]

If z in U* satisfies e_4<z<e_5, insert it into (7) to obtain (a,e_1,e_2,e_3,e_4,z,e_5). Exactly two new consecutive triples occur: (e_3,e_4,z) and (e_4,z,e_5). They are both red by section3's lifted right-root property, so this is a forbidden R7. If z>e_5, append z to (7); its only new consecutive triple (e_4,e_5,z) is red for the same reason. Thus no U* point lies after e_4 except e_5, proving (6). All supplies and the inserted point are actual, and no unique private path is required.

This does not place every non-E point before e_2. Inserting z immediately after e_2 into (7) would introduce three new consecutive triples, including (z,e_3,e_4). The lifted right-root property proves the other two but does not determine this third triple. In particular the local packet on (e_2,z,e_3,e_4) may be R,R,R,B. The stronger early-cut claim was considered and retracted; it is not a consequence of the argument above.

## 6. Alternative transversals and limits of further closure

The proof uses E as the actual endpoint set, never as an arbitrary chosen five-transversal. Every alternative minimum transversal Z still leaves a full756 S minus Z, and all mixed paths meeting several Z points were retained in U*. However its points need not be incoming S-R6 endpoints. Replacing E by Z in section3 would lose the incoming R6 and the penultimate S red-five terminal used there. No uniqueness of E as a minimum transversal is proved.

Three attempted mechanisms have distinct stopping points. First, counting singleton B4 second vertices would leave the E6 case unresolved because many U_D points can share one second vertex. The actual residual deletion (4), applied to all U* paths, repairs this and proves Hall. Second, merely extending the S right-root identity to U* would be invalid; the incoming R6 bridge and ambient extension in section3 provide the missing proof. Third, turning W_0 into a replacement canonical S is unjustified: U_D points are not ambient R6 sources. The old canonical root-source closure and mixed-role theorem cannot be reapplied with W_0 in place of S. It is a legal D7 residual, not a new canonical decomposition.

R5's point-pair potential does not by itself turn this matching into a contradiction. A u--a edge provides B4 from u with second point a, while the accompanying red-six from section2 starts at the source of an incoming R5 to u and ends at a. The red-six does not start at u. Thus these are not the same actual endpoint incidences required for the old alternating support cycle comparison. Nor does Hall provide a reverse u--a edge or an alternating closed walk. Arbitrary support overlap remains allowed.

The new restrictions leave an actual five-endpoint class with common residuals S and K' union E, and ordered matching U_D to I minus E. No proof that this class is empty is supplied. In particular no C49, Q79, or F80 conclusion follows. All new deductions remain unreviewed/unaccepted.
