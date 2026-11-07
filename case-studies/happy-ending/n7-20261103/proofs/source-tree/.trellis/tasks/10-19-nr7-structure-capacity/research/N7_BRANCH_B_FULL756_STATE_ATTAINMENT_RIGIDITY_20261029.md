# Support B: what full756 equality does and does not rigidify

Date: 2026-10-29, subsequent generation turn. **Unreviewed/unaccepted.** This is support for the primary actual X80 joint-core argument, not an independent bound route or a classification of full25 configurations. No scientific computation, enumeration, solver, checker, external review, or acceptance change was performed. Only this fresh note is owned by this branch.

The principal finding is a precise obstacle: the accepted capacity proof has no pointwise charging equality from which to infer attainment at a named owner. Full25 yields equality of two counts. The shared-core comparison below retains actual witness information, but does not convert that equality into internal R5 suppliers at B0 or identical states on P.

## 1. Accepted theorem and exact dependency scope

The current [cardinality-layer theorem](../../09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md) works on complete ordered rank-3 signotopes with no B5, R6, or weak7. Its 35-state catalog consists of 25 ordinary and 10 exceptional states. Injection gives

    |V|=25+e(V)-m_miss(V).

The accepted rows C1 through C10 give m_miss>=e. The [October 26 C8 human acceptance](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md) and its [accepted certificate](../../09-03-35-state-cardinality-charging/research/evidence/c8-accepted-20261026/cardinality_c8_accepted_certificate.json) identify all ten accepted row anchors. C8 uses accepted C7 and checked A[8,8], A[8,9], A[8,10]. C7 in turn retains accepted C1--C6 and four checked historical cells. The [C9/C10 acceptance](../../09-03-35-state-cardinality-charging/research/c9-c10-formal-acceptance-20261022.md) has its own accepted C7-based dependency DAG and does not retroactively rely on full C8. These scopes are stated in the current theorem and the acceptance artifacts, not reconstructed from row numbers alone.

The earlier C7 and C9/C10 numerical bounds are historical checkpoints. The current combined scoped bound is 25. Their human acceptance and same-family/provisional assurance remain as recorded; exact reviewer backend/model/effort remain unverifiable. This branch read the theorem, the C8/C9-C10/C7 acceptance records and the current C8 certificate's dependency anchors. It did not recheck proof bodies, execute a reconstruction, hash sealed objects, or upgrade any accepted evidence.

For an actual full25 configuration, the counting identity itself forces

    m_miss=e.                                          (1)

The cardinality theorem establishes that larger configurations cannot exist in its domain. It does not assert e=0, a fixed occupied catalog, or an owner-level map from exceptional states to missing ordinary states.

## 2. Where equality occurs in the actual proof

The proof has three relevant stages.

1. Exact terminal-path recurrence proves state injection. This is an inequality-free distinction statement between different owners, not a bound with an owner slack.
2. The occupied-state partition gives the exact identity |V|=25+e-m_miss.
3. Each layer C_r excludes a global bad-cell class with e>=r and m_miss=r-1, by the earlier layers and the corresponding proof-qualified UNSAT cells. Applying C_e gives m_miss>=e.

At |V|=25, stage 2 gives (1). Stage 3 does not present m_miss-e as a sum of nonnegative local quantities. Nor does it provide an injection pairing each exceptional owner with a particular missing ordinary state. Its canonical state variables are determined by the actual coloring, but uniqueness of those variables for one coloring is not uniqueness across different induced configurations.

Indeed, on the stated domain and under the exact counting identity, the scalar assertions m_miss>=e and |V|<=25 are mathematically equivalent. This observation concerns their conclusion, not the qualification or acceptance of any individual serialized cell or historical proof DAG. Thus the scalar charging conclusion alone carries no extra equality-case information beyond the capacity bound.

Setting m_miss-e=0 cannot legitimately set unspecified local terms to zero. In particular it does not force every available ordinary state to occur, any named red-five terminal to attain a full internal pair rank, or a named B0 owner to have an R5 inside K'. This is a limitation of the available theorem interface; no assertion is made that a stronger mathematical equality theorem is impossible.

## 3. Actual joint cores and internal-state domains

Use the same X80 setting and notation as [the latest main manuscript](N7_H50_R30_COMMON_SATURATION_AND_FULL_SUPPORT_BARRIERS_20261029.md) and [primary A](N7_BRANCH_A_H50_R30_JOINT_EQUALITY_20261029.md). From [R25 Sections 3--6](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md), restrict to the primary equality case j+m'=25. Then

    Y=P disjoint-union A0,
    K'=P disjoint-union B0,
    |A0|=|B0|=q,
    J=K' minus F',  B0=U_D contained in F'.

Both Y and K' are actual full25 756 cores inside the same X, with the same triple colors on their common part P. They have different predecessor domains. B0 is red-five-through in H': it belongs to K'=Src_R5(H') and F'=End_R5(H'). This does not place either of those H' suppliers inside K'. In particular the red-five prefix ending at a B0 point may use H' minus K'.

Write D_V(v) for the incoming state recomputed in the actual induced configuration V. For v in P, heredity gives exactly

    D_P(v) contained in D_Y(v) intersection D_K'(v).     (2)

Neither inclusion D_Y(v) contained in D_K'(v), nor the reverse, follows from (2). Both compare with the common smaller domain, not with each other. Equal sizes of the two cores do not change this fact.

## 4. All-witness consequences that really survive comparison

For a common actual terminal pair u<v in P, let L_c^V(u,v) be the maximum color-c path length ending with that pair, recomputed in V. Deleting all A0 points from a Y path preserves u,v as its final pair and preserves monochromaticity, by packet heredity. At most q vertices are deleted. Hence

    L_c^P(u,v) <= L_c^Y(u,v) <= L_c^P(u,v)+q,
    L_c^P(u,v) <= L_c^K'(u,v) <= L_c^P(u,v)+q,
    |L_c^Y(u,v)-L_c^K'(u,v)| <= q.                     (3)

If L_c^Y(u,v)>L_c^K'(u,v), every Y path attaining the larger length uses A0. Otherwise that path would lie in P and already occur in K'. The symmetric assertion holds for B0. This applies to all attaining paths, not one convenient witness. It gives no distinct replacement owner for different pairs: one actual replacement point may participate in many paths and many state changes.

For a state cell g in D_Y(v) minus D_K'(v), choose any terminal pair (u,v) whose two-coordinate label dominates g, and any two color paths attaining sufficient lengths at that same terminal pair. Their union must meet A0. If u is in A0 this is immediate. Otherwise u lies in P; if both paths avoided A0 they would both lie in P, putting g in D_P(v), contrary to (2). This is a statement about the union of two actual witnesses: the red and blue coordinate maxima may be attained by different paths. It is not valid to say that each of the two paths must meet A0, or that one simultaneous monochromatic path attains both coordinates.

There is a genuine initial-segment rigidity: if v in P precedes every point of A0 union B0, the predecessor configurations are identical, so D_Y(v)=D_K'(v)=D_P(v). Later owners need not have identical predecessor domains. Selecting the earliest B0 point does not ensure this hypothesis if some A0 points precede it.

These are hereditary support restrictions, not a new capacity deficit. They do not prove internal R5 attainment at B0.

## 5. What the large common J does constrain

R25's mixed-role exclusion says that a member of J cannot end any ambient R5. Therefore it cannot end an internal R5 in either Y or K'. Both cores forbid B5. Every J owner consequently has its incoming state in the 3-by-3 low subcatalog, consisting of twenty ordinary states. This statement does not turn J into an internal blue-five source set of Y; Y has no B5 at all.

For each V in {Y,K'}, its exceptional owners are thus confined to V minus J, which has m' points. Therefore

    e(Y)<=m',  e(K')<=m'.                              (4)

In the remaining primary cases m' is nine or ten. Equation (4) rules out an e=10 catalog for these cores when m'=9; at m'=10 it only recovers the catalog maximum. It does not fix the catalog or show that any particular owner outside J is exceptional. Internal R5 terminals are also confined to V minus J, but being in that container is not an attainment statement.

This is a direct role-and-catalog consequence, not a new hard exclusion of an X80 parameter branch. The shared J states need not be equal between the two cores. Twenty possible low states and fifteen or sixteen distinct J owners do not imply a particular injection or an identical image set in both cores.

## 6. A real rigidity proof in R23, and why its hypotheses are absent here

[R23 Section 11.2](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md) contains an actual pointwise rigidity argument for a different setup. In its hypothetical extension of the fixed X7 construction, the old seven exceptional states form a fixed seven-state up-set E7. Old states grow monotonically under insertion, their new images remain inside the same E7, and injection gives a bijection of E7 with itself. The sum of state areas is unchanged, while each owner's area is nondecreasing. Therefore each owner's state is fixed.

This is a finite-poset equality argument with explicit prerequisites: monotonicity, the same finite image set, and a bijection. The present Y/K' replacement has none of those three conclusions merely from full capacity. Equation (2) supplies only monotonicity from P separately into the two cores. Equation (1) supplies only equality of missing and exceptional counts within each core, not a common occupied image set across them.

A conditional version is valid: if one independently proved an owner bijection between two cores, state inclusion at every paired owner, and equality of their occupied catalog sets, then equal total area would force every paired state equal. In particular, two e=0 full25 cores both occupy all ordinary states, but one would still need the ownerwise inclusion/bijection premise. No such premise is proved in the primary equality case.

R23 Section 9 explicitly supplies actual full25 examples with e=m_miss equal to 0,7,8,10. These are actual 756 examples in their stated scope, not examples of the present X80 embedding. They are sufficient to invalidate an inference from full25 alone to the all-ordinary or a fixed-exceptional-catalog premise. Their existence and their acceptance level are not upgraded by reading them here.

## 7. Attempts and precise stopping points

First attempt: apply equality in the accepted charging proof to each shared owner. It fails at the proof-interface level: no ownerwise nonnegative decomposition or matching of missing states is present.

Second attempt: use common P and actual state growth to compare Y and K'. This introduces genuine shared coloring, and yields (2)-(3) and the all-witness support condition. It stops because adding disjoint alternative sets gives two independent increases from P, not a direction of comparison between the completed cores. Reused replacement owners cannot be counted as separate capacity charges.

Third attempt: use j+m'=25 and B0 contained in F' to force attainment at B0. This introduces actual ambient role information and yields the exceptional-owner confinement (4). It stops because F' is defined in H', while states and paths of K' are internal to K'. Every red-five-through role cannot simply be transported into the smaller source core.

Fourth attempt: reuse the actual R23 fixed-state argument. Its exact proof works, but the shared-image and monotone-bijection hypotheses have not been obtained for Y/K'. Full25 diversity prevents substituting an all-ordinary hypothesis for them.

An additional speculative question was communicated but not adopted: whether every full75625 core must contain a red-five terminal that has no internal blue-four ending there (one of the tall ordinary states). If proved under the joint premises it could sharpen (4). Neither the accepted cardinality theorem nor the present reasoning proves that existence statement. Earliest-red-five-terminal selection does not by itself align the red and blue source endpoints for weak7. It is not a result of this note.

## 8. Support delivered to primary A

The present capacity certificate cannot supply the desired pointwise attainment rigidity through an equality-case step that is not in its proof. Primary A must establish a new actual-witness statement, for example a justified internal supplier, a monotone common-state correspondence with a fixed image, or a direct mixed-support obstruction. Equation (1) alone does none of these.

All existing canonical, residual, same-root, and mixed-role restrictions from R7/R20/R25 remain in force. This note does not weaken them and does not claim the replacement cores are jointly realizable beyond the standing hypothetical X80. No actual counterexample was constructed, no complete parameter branch was excluded, and no bound changed. Current chain: 40/50/80/81. All new deductions and proof-interface analysis remain unreviewed/unaccepted.

## 9. Same-turn continuation: the union is actually blue-five-free

Primary A subsequently supplied a stronger actual fact, which changes the available support information. Set

    U=P union A0 union B0,  |U|=25+q.

For b in B0=U_D there is an actual R5 beginning at b and continuing in D. If an ambient B5 ended at b, its last predecessor w and that R5's first successor d would give a bridge chi(w,b,d). A blue bridge extends the B5 to B6. A red bridge prepends w to the R5, giving an ambient R6 ending in D, impossible by D's definition. Thus no B0 point ends an ambient B5. No point of S=P union A0 ends an ambient B5 either, by the earlier source/terminal exclusion. Therefore U has no B5.

Every R6 in U ends in A0: P lies outside the ambient R6 terminal set, and B0 lies in D. It contains a point of B0 because Y is R6-free. Every such B0 point is internal: B0 has neither the ambient R6 source nor terminal role. The following universal insertions now hold:

- Every K' plus a, for a in A0, has 26 vertices and no B5, so it contains an R6, necessarily ending at a.
- Every Y plus b, for b in B0, has 26 vertices and no B5, so it contains an R6, necessarily using b internally and ending at a point of A0.

These conclusions use the actual union's colors and the valid capacity bound. U itself is not a 756 configuration: it has R6. The 35-state capacity theorem must not be applied to U.

## 10. Actual transversal matching, and exactly what its witnesses attain

Since deleting either A0 or B0 leaves a full756 core, both are R6 transversals of U. Conversely deleting any R6 transversal Z from the blue-five-free U leaves a 756 configuration, so |Z|>=q. Therefore tau_R6(U)=q.

Form the actual graph G on A0 by B0, with edge a--b if some actual R6 in U ends at a and contains b. For A contained in A0, the set (A0 minus A) union N_G(A) hits every R6: those ending outside A hit the first part; those ending in A contain B0 vertices, all of which belong to N_G(A). Its size is q-|A|+|N_G(A)|, hence Hall gives |N_G(A)|>=|A|. G has a perfect matching. Every matched pair has b<a along its actual witness. Consequently the sorted lists satisfy b_i<a_i, and at every actual cut the number of B0 points already passed is at least the number of A0 points already passed.

This is Primary A/root's actual-support matching, not an independent claim of this branch. It does give a precise new state-attainment distinction. For every a in A0, the pure K'+a insertion supplies an R6 ending at a, and no R7 exists. Therefore a's incoming red maximum in U is exactly six. Every point v in K' has incoming red maximum at most five in U, because it is not an ambient R6 terminal. Since U has no B5, all incoming blue maxima are at most four. Thus:

    A0 owners have U-states of red height five;
    K' owners have U-states lying inside the old 3-by-4 box.

The G matching relates B0 vertices to these height-five owners by actual R6 incidence. It does not say that the matched B0 vertex is essential to the owner's maximum rank, or that the matched witness lies in K'+a. A general G witness can contain several A0 and several B0 vertices. In particular this incidence matching is not a bijective state-attainment transport from B0 to A0.

There are exactly 25 K' owners and their U-states remain injective. Consequently those 25 ambient labels have missing-ordinary count equal to exceptional count as a counting identity. They need not be the internal states D_K'(v). This equality is not an application of accepted charging to an induced core with those labels; no such realization has been proved. They can grow monotonically from D_K'(v) while changing their occupied catalog.

## 11. Pure insertions do attain internal red-five states, without a matched-owner theorem

Take any pure Y+b R6. Deleting its internal b leaves an actual R5 in Y, with the same terminal a in A0. Thus for every b there is some actual a in A0 intersection End_R5(Y) obtained this way. This establishes actual internal attainment, rather than merely an ambient role. It does not establish distinct a's for distinct b's.

Similarly, deleting the final a from any R6 in K'+a leaves an actual R5 in K', ending at that R6's penultimate vertex. This owner lies in K' minus J, by the mixed-role exclusion. It need not be the matched b, or any B0 vertex: the penultimate point can lie in P minus J.

One tempting strengthening would define a graph using only the pure Y+b insertions and demand a perfect matching to distinct internally attained terminals in A0. The proof in Section 10 does not establish Hall for that smaller graph. When several B0 points are admitted simultaneously, an R6 can use several of them and end at a terminal unavailable to every single-b insertion. Deleting the terminal neighbors of the single-b graph need not hit such mixed paths. Likewise, the general G matching cannot be silently restricted to pure K'+a witnesses.

Even for q=1, where every U R6 is simultaneously a pure insertion witness on both sides, deleting b gives a red-five terminal at a in Y, while deleting a gives a red-five terminal at some predecessor in K'. The predecessor need not be b: b may occur earlier internally. Hence a new proof is still needed to promote the H' through role of b to an internal K' terminal state.

## 12. Revised support conclusion

The union theorem supplies real additional information: blue-five-freeness of U, two minimum q-transversals, an actual R6-incidence matching with b<a, exact height-five attainment at every A0 owner in U, and internal red-five attainment for each pure insertion after deleting its unique outside point. These conclusions strengthen the earlier certificate-only obstacle and have been sent to Primary A.

They still do not prove a matched internal-state correspondence on Y/K', essential ownership of rank attainment, or a fixed occupied catalog on the common P. Sorted domination of the replacement sets is a statement about positions, not about the mixed triple colors required to transport a monochromatic path. The first common-state transport step remains unproved. No new global bound, acceptance, or scientific execution follows from this continuation.

## 13. Primary A's stronger residual subset: a real shared-core restriction

During continued generation, Primary A found a stronger way to use the actual role constraints. This branch checked the complete bridge argument and the population calculation. It is not independent review and is attributed to Primary A, rather than to the earlier charging-equality analysis.

Let C0=U_D intersection V_D and w=|C0|. Use all of I=S intersection T6, not merely A0=I minus Z. Define the actual induced subset

    W=J disjoint-union I disjoint-union C0.

Its size is j+5+q+w. No owner in W ends any ambient B5: J and I lie in S, and C0 lies in U_D, for which Section 9 proved this exclusion. Thus W has no B5.

No I owner can start a B4 inside W. Given such a B4 starting at a, take any ambient R6 ending at a with penultimate u. The bridge from u,a to the B4's second point, if red, extends R6 to R7; if blue, prepends u to B4 and gives an ambient B5 ending at a vertex of W. Both are impossible.

No C0 owner can start a B4 inside W either. It has an incoming R5 lying wholly in D because it belongs to V_D. If the bridge from this R5's penultimate point through the C0 owner to the B4's second point is red, it gives an ambient R6 whose source lies in D, impossible. If blue, it gives an ambient B5 ending at a vertex of W, also impossible.

Finally, no J owner ends an ambient R5 by R25. Every owner of W is therefore either unable to end an internal R5 or unable to start an internal B4. Along with no B5 and inherited no weak7, this is precisely the R7 residual D7 class, with no internal End_R5/Start_B4 junction. Its established bound is b+5=30. Consequently

    j+q+w<=25.                                        (5)

The reversed argument gives j_T+q+w<=25. In the primary equality case j+m'=25, (5) gives

    q+w<=m',  equivalently |P minus J|>=w.             (6)

The minimum transversal Z is not needed for this argument. Restoring its five points from A0 to I is essential to the stronger constant in (5); stopping at J union A0 union C0 would give only the weaker j+q+w<=30.

This is an actual induced-class restriction, not a reformulation of m_miss=e. For example, in the m'=10 equality case it excludes q=10 with w>=1; the previous q<=m' and q-w>=1 alone did not do so. It does not eliminate every q,m,m' case or improve the global 40/50/80/81 chain.

Equation (6) also says that the w common-D red-five-through owners require at least w further H' through owners in P minus J, in addition to the q owners B0 already in that role. This is a cardinality statement following from the actual residual subset. It is not a proved injective pairing of these owners and does not identify matching internal states or attaining paths. The charging-equality obstacle and the witness-transport distinctions above therefore remain relevant even after this genuine primary progress.

## 14. Root strengthening: conditional joint capacity from a full canonical H

The root subsequently found a stronger residual set and asked for a fresh scope check. The argument below was checked within mathematical generation. It supersedes the need to restrict the residual set to J, and does not use j+m'=25 or a full reversed H'. Attribution is to the root strengthening; no independent review or acceptance occurred.

Let X be any actual 767 configuration with its R7 canonical partition X=H disjoint-union R and |H|=2b, where b is an effective 756 bound. R20's general-b zero-deficit argument gives

    S=Src_R6(X)=R,
    no ambient R6 starts in H,
    every r in R has an R6(r,H,H,H,H,H).

Put T6=End_R6(X), D=X minus (S union T6), and

    U_D=Src_R5(D),  V_D=End_R5(D),  C=U_D intersection V_D.

No formula for |U_D|, |V_D|, j, q, or a reversed core is required in this section.

### 14.1 The mixed-role swap does not require a full reversed core

The needed R25 statement is S intersection End_R5(X) intersection Src_B5(X)=empty. Its proof under the present assumptions is as follows. Suppose a has all three roles. The R7 three-chain lemma, applied to any incoming R5, any outgoing R6, and any outgoing B5, forces the endpoint of every outgoing R6 and the second vertex of every outgoing B5 to be one common vertex h. A pure H tail ensures h belongs to H.

The actual set H_a=(H minus {h}) union {a} has size 2b. Its R6 could not start at an old H point, and one starting at a would require its deleted endpoint h. Thus it is a 766 configuration. All B5 starting at a would require h as second vertex, so a is not an internal B5 source of H_a. The full2b partition Src_B5(H_a) disjoint-union End_R5(H_a)=H_a therefore gives an internal R5 ending at a, with all four preceding vertices in old H. If u is its penultimate vertex, the bridge chi(u,a,h) must be red: blue would prepend u to an ambient B5(a,h,...), giving B6. The red bridge appends h to the internal R5 and gives an ambient R6 starting in old H, a contradiction.

This proof uses the full H and R20 closure, but no full H', X80 population, or j-count. It also recomputes the swapped core internally.

### 14.2 Every B4 ending in S union U_D has an ambient extension

For s in S=R, canonical membership R contained in P_+ is essential. R7 Section 2 states that p(s)>s and chi(v,s,p(s))=B for every v<s. Hence any actual B4 ending at s can append p(s) to become an ambient B5. Earlier vertices of the path need not lie in P_+; the original fan proof explicitly has this ambient scope.

For b in U_D, take an actual D-internal R5 starting at b, with first successor d. Given any B4 ending at b with penultimate v, a red chi(v,b,d) would prepend v to that R5 and produce an ambient R6 ending in D, impossible. The bridge is blue, so the B4 appends d to an ambient B5. Thus any source of a B4 lying inside S union U_D is an ambient B5 source.

No S point ends an ambient B5: an incoming B5 and an outgoing R6 at that point bridge to B6 or R7. No U_D point ends an ambient B5 either: the analogous bridge with its D-internal outgoing R5 gives B6 or an R6 ending in D. Finally, no V_D point starts an ambient B5: its incoming D-internal R5 and an outgoing B5 bridge to an R6 starting in D or B6.

### 14.3 An actual residual enlargement and the conditional inequality

Consider the actual induced configuration

    W*=S disjoint-union C.

It has no B5, because none of its vertices is an ambient B5 terminal. If a point starts a B4 internally in W*, Section 14.2 makes it an ambient B5 source. Such a point cannot lie in C contained in V_D. If it lies in S, Section 14.1 prevents it from ending any ambient R5. Therefore W* has no internal owner simultaneously ending R5 and starting B4. It inherits weak7-freeness from X. These are exactly the R7 residual D7 premises, so its established bound is b+5. Consequently

    |R|+|C|<=b+5,
    |X|<=3b+5-|C|, provided the canonical |H|=2b.       (7)

In particular, an actual joint equality |X|=3b+5 forces C empty. At b=25 this says that a hypothetical X80 must satisfy U_D intersection V_D=empty, or w=0 in the earlier notation. No j+m'=25 assumption is needed. For configurations with full canonical H50 and a nonempty common-D through set, (7) gives |X|<=79; more generally the conditional loss equals |C|.

This is a genuine conditional joint-capacity relation established through an actual residual enlargement. It does not prove that C is nonempty in every candidate, does not assert that canonical H is full in every smaller configuration, and does not yield an unconditional new global bound. The surviving empty-C equality case remains to be excluded. No 25-state equality or state-attainment transport is used to obtain (7), and none is inferred from it.
