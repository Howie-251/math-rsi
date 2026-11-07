# Tight missing corners: three actual paths and the unresolved extension gates

Date: 2026-10-29, later user-authorized generation turn. **Unreviewed/unaccepted. No new global bound and no new complete critical subclass exclusion were obtained.** This note owns only this new file. Earlier notes, source, evidence, acceptance, configuration, task state, and pointers are unchanged. No code, enumeration, solver, proof checker, external review, or external-review authorization request was used.

The useful result of this branch is an exact account of the attempted three-path extension and its failure: a proposed cap-six proof omitted one new consecutive triple. The corrected argument yields red-gate propagation across all alternative witnesses, but no forced collision. It must not be reported as a missing-corner theorem or as a proof that every actual edge belongs to a perfect matching.

## 1. Fixed actual setting and source boundaries

Work in one complete ordered rank-3 signotope X with 50 vertices, no B6, no R6, and no weak7. A weak7 uses the same actual endpoints and opposite-color lengths totaling nine; internal disjointness is not required. Packet order is abc, abd, acd, bcd, with at most one color change. The effective 756 capacity is b=25.

Retain the four actual saturated atoms L,D,T_R,T_B and the internally recomputed graphs H_B in Y_B=X minus T_B and H_R in Y_R=X minus T_R. Their two sides L,D have k=25-m vertices, with 12<=k<=16 and 9<=m<=13 at the inherited research level. All actual induced B5 paths are included in H_B, including paths with internal L and D vertices. The graph has a perfect matching.

Primary current sources are [the full-pair-fan manuscript](N7_FULL_PAIR_FAN_BOUNDARY_AND_TIGHT_CORE_DICHOTOMY_20261029.md), [the earlier tight-core branch](N7_BRANCH_A_HALL_TIGHT_CORES_20261029.md), [the strict-Hall branch including its Section 7 complete e=1 dichotomy](N7_BRANCH_B_STRICT_HALL_SUPPORTS_20261029.md), and [the blocker branch](N7_BRANCH_C_CRITICAL_BLOCKER_PROPAGATION_20261029.md). The older structural sources are [the October 28 interfaces](N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md), [R23](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md), [R20](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md), and [R7](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md).

[R3 Section 6.3](RESET_R3_BIDIRECTIONAL_IDEAL_INTERVALS.md) already owns same-endpoint support rectangles and reliable gluing along an actual common middle edge. [R22 Section 5.1](RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md) already owns the full-path transversal-to-endpoint-matching argument and explicitly permits shared internal supports. Neither tool is claimed new here. The full-fan identity and its e<=1 conclusions are also earlier results, not new output of this turn.

## 2. Full tight core and all three witness families

Let (l,d) be an actual H_B edge belonging to no perfect matching, and let P be any actual B5 from l to d in Y_B. The standard exact graph barrier supplies a tight set U with

    l not in U,  d in N(U),  |N(U)|=|U|.

Here N is the H_B neighborhood. The actual induced configuration

    W=U union T_R union (D minus N(U))

has 25 vertices and no B5. Capacity and endpoint localization produce the full nonempty families

    Q: B5 from l to d', d' in D minus N(U), Q contained in W plus l;
    R: B5 from l' to d, l' in U,             R contained in W plus d.

Every such path has the indicated endpoint. A Q path starting in U, or an R path ending in D minus N(U), would give the forbidden corner in H_B. The source and terminal of every B5 in W lie in U and D minus N(U), respectively, so no actual B5 from l' to d' lies wholly in W.

No choice of a convenient Q or R replaces these full families. The original P can use vertices outside W besides l,d. Its internal vertices are not automatically eligible for a path contained in W. Tight-set closure under union and intersection does not make path supports laminar or independent.

The earlier common-triple fact remains valid: if Q and R share three vertices strictly between l' and d', packet gluing gives B5(l',common triple,d') in W. Thus they cannot do so. A common pair x<y only gives B4(l',x,y,d'), which is allowed in W. This is the starting gap, not the new conclusion.

## 3. Attempt one: use P to certify the fifth vertex

Add explicit actual conditions: Q and R share x<y; P is (l,x,z,y,d); and z belongs to W. The last condition is an additional membership premise, not a consequence of P being in Y_B. Then

    l'<x<z<y<d',

because x,y are internal to Q and R and z lies between them. Define two actual gate colors

    alpha=chi(l',x,z),  gamma=chi(z,y,d').

The candidate sequence (l',x,z,y,d') lies in W. Its three consecutive triples are alpha, chi(x,z,y), gamma. The middle triple is blue because it lies in P. Therefore the candidate is B5 if and only if both gates are blue. Since W is B5-free,

    alpha=R or gamma=R.                                (1)

This is an exact reduction of this particular extension attempt. It is not a forced contradiction. The packet axiom gives the full local form of each obstruction:

- If alpha=R, the packet (l',x,z,y) is RBBB, since its second entry chi(l',x,y) and last entry chi(x,z,y) are blue.
- If gamma=R, the packet (x,z,y,d') is BBBR, since its first entry chi(x,z,y) and third entry chi(x,y,d') are blue.

Both patterns are packet-legal individually. This statement is local only; it is not an actual X50 construction or a claim that both patterns extend to a complete critical configuration.

The extra fact introduced in this attempt was P's actual blue triple x,z,y. It changes the problem from finding an arbitrary third shared point to closing two specific mixed gates. The first gap is that P does not determine either mixed gate.

## 4. Attempt two: use the length-six cap to close the gates

The second attempt used a genuinely additional constraint, no B6, and nested endpoint order. It initially appeared to close both gates; the root collaborator identified an omitted consecutive triple. The proposed proof was withdrawn before being recorded as a result.

For the left side, suppose l<l'<x and Q has x as its second vertex:

    Q=(l,x,q3,q4,d').

If alpha=R, the packet (l,l',x,z), with its third entry chi(l,x,z)=B and last entry alpha=R, forces its first two entries blue. In particular chi(l,l',x)=B. But inserting l' into Q gives the candidate six-sequence

    (l,l',x,q3,q4,d').

Its two new consecutive triples are chi(l,l',x) AND chi(l',x,q3). The first being blue is insufficient. The other old consecutive triples are blue, so no B6 forces precisely

    alpha=R implies chi(l',x,q3)=R                    (2)

for every actual Q having first pair (l,x). This is the corrected conclusion, rather than a contradiction.

For the right side, suppose y<d'<d and R has y as its penultimate vertex:

    R=(l',r2,r3,y,d).

If gamma=R, packet (z,y,d',d), using chi(z,y,d)=B, forces chi(y,d',d)=B. Inserting d' into R yields two new triples chi(r3,y,d') and chi(y,d',d). The second is blue, so no B6 forces

    gamma=R implies chi(r3,y,d')=R                   (3)

for every actual R having final pair (y,d).

Equations (2)-(3) propagate a red gate to the entire relevant family of third or antepenultimate vertices. They retain all alternatives. They do not force these red triples to coincide with known blue triples. Capacity alone does not force the first-pair or final-pair positioning premises, either.

This also explains why a proposed shortcut asserting that a private endpoint's next path vertex must be its immediate neighbor in W is unjustified. Replacing an endpoint and inserting a new point are different operations; the packet pattern BBBR can block the replacement triple even when another insertion triple is blue. No such immediate-neighbor theorem is asserted.

## 5. Attempt three: close the propagated gates by shared supports

The third attempt introduced an explicit extra support intersection. If some Q third vertex q3 has a separately certified blue triple chi(l',x,q3), then (2) excludes alpha=R. Likewise a certified blue triple chi(r3,y,d') closes gamma through (3). If both gates close, Section 3 gives the missing-corner contradiction.

However, the natural ways to certify these triples from Q and R themselves reduce to previously known obstructions. For example, if

    Q=(l,x,y,q,d'),  R=(l',r,x,y,d),

then their actual common consecutive pair x,y already glues into

    (l',r,x,y,q,d'),

an actual B6. The four consecutive triples come, in order, from R,R,Q,Q, and the point order is strict. P is unnecessary. This is the old reliable shared-edge gluing, not a new three-path theorem.

Other direct certifications use a third common internal vertex, giving the already known missing-corner B5. Neither case proves that arbitrary full witness families must contain such a certification. Hence this attempted switch did not produce a new excluded critical subclass beyond the previously available common-edge/common-triple exclusions.

The remaining obstruction is exact: the families of propagated red gates can avoid the known blue-gate supports, and the present argument has not shown that all four saturated cores prevent this. It is not legitimate to insert P's extra owner without proving the two new mixed triples.

## 6. Boundary-theorem coverage remains limited

The earlier full-fan result uses

    e(x,y)=|L at or after x|+|D at or before y|.

When e=0 all L precedes x and all D follows y. When e=1 there is only one total endpoint exception to that separation. The full-fan theorem correctly handles every actual carrier that meets this condition, including the two slack branches of e=1 without an extendability assumption. It does not prove that any actual carrier pair satisfying e<=1 exists in every critical configuration.

Even a future proof that every actual endpoint edge is allowed would not by itself force such a pair. In particular, it would not complete C<=49 or lower the 40/50/80/81 chain. The actual support-density entry remains a distinct missing premise. This branch neither repeats the full-fan identity as new nor treats this coverage issue as a technicality.

## 7. Transfer to the canonical H50 plus R30 branch

After the failed closure, this branch returned its exact gap and the consecutive-triple warning to the canonical branch rather than proliferating endpoint classifications.

The actual canonical setting is a 767 mother, with no B6, no R7, no weak7, and X=H disjoint-union R, |H|=50, |R|=30. R7 supplies the five-point red-six transversal and the 25-point core Y=R minus T. R20's parameterized zero-deficit argument supplies an actual R6(t,H,H,H,H,H) for every t in R, with no H-origin R6. These are inherited tools, not a result of this branch.

For an endpointized private R6 in Y plus t, let its penultimate vertex be u. Every actual H-tail R6 beginning at t, with first H vertex h, forces chi(u,t,h)=B: red would append h to the private path and create R7. R20 Section 6.3 further places every H-tail of u wholly inside (u,t). Thus the canonical branch has an H red-five tail before t and an H red-five tail after t, along with same-t blue bridge triples. This statement retains all actual alternatives.

The support lesson from Sections 3-5 is that these bridge triples cannot be silently inserted into a longer blue path. One must check both new consecutive triples, or use a genuinely shared consecutive edge. Appending h to the private red-six path, in contrast, really adds only one triple and the preceding bridge proof is valid. The two H tails are separated by t; they need not share a pair, and interval nesting across different t does not give disjoint capacity charges. This branch found no additional packet identity that closes that missing step. It does not override the canonical branch's further work or claim a new bound on T.

### 7.1 Additional R25 role accounting and two full25 cores on one common part

The parent redirected the final exploration to [R25 Sections 3-5](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md). Its mixed-role exclusion is inherited:

    Src_R6(X) intersection End_R5(X) intersection Src_B5(X) is empty.

Use R25's S=Src_R6(X)=R, global terminal set T_global=End_R6(X), P=S minus T_global, I=S intersection T_global, and |I|=5+q. Let T_small be R7's endpoint transversal, of size five; then T_small is contained in I. This separates the two different meanings of T.

No member of T_global can start an ambient B5: joining an incoming R6 and an outgoing B5 at that point, its bridge triple gives either R7 or B6. In particular T_small contains no ambient B5 source. R25's set J=P intersection Src_B5(X), with j>=15, is therefore wholly contained in Y=R minus T_small. The mixed-role exclusion gives

    End_R5(Y) contained in Y minus J,
    |End_R5(Y)|<=25-j<=10.                             (4)

If j=16, the upper bound is nine. The classical lower bound is only five: deleting all red-five terminals leaves a no-B5/no-R5 configuration of size at most twenty. Thus the remaining interval is 5 through 10, or 5 through 9 when j=16. This is bookkeeping from old role theorems, not a new population contradiction.

There is also an exact common-part identity retaining actual cores. With D=X minus (S union T_global), R25 gives U_D=Src_R5(D), |U_D|=q, and the full H'=X minus T_global source core

    K'=Src_R5(H')=P union U_D.

Meanwhile

    Y=P union (I minus T_small).

Both have 25 vertices and no B5 or R6, and their intersection is exactly P, of size 25-q. Hence the q through-red-six points of Y outside P and the q actual D red-five sources of K' outside P are two different actual completions of the same common part. This identity is a real shared-support constraint, not an authorization to exchange arbitrary subsets between the two cores. Their union need not remain B5-free or R6-free. No packet-certified replacement between the q-point parts was obtained.

These consequences were passed to the canonical branch. They identify the sharper endpoint threshold and preserve an additional full core, but do not force eleven red-five terminals in Y, close a same-t extension, or rule out the remaining m=9,10 possibilities. The combination of older R25 m<=10 and older Joint17 m>=9 is not counted as a new result of this turn.

## 8. Outcome

Proved here are the exact two-gate formulation (1), the corrected all-alternative gate propagation (2)-(3) under their explicit positional premises, and the audit that the simplest apparent closures reduce to old common-edge or common-triple contradictions. These are local deductions useful for checking an attempted proof. They do not constitute a new all-class restriction or a new critical-interface exclusion beyond those older mechanisms.

Not proved: that all actual H_B/H_R edges are allowed; that a third common point is forced; that the gates collide across full witness families; that an e<=1 carrier must exist; or that the canonical same-t supplies yield a positive deficit. No actual critical X50 or X80 counterexample was constructed.

The numerical chain remains 40/50/80/81. New global decrease: zero. All work remains mathematical generation, unreviewed/unaccepted, with zero scientific and external-review calls.
