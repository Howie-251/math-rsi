# Branch A: support-sensitive compatibility of Hall-tight real cores

Date: 2026-10-29. Mathematical generation only; **unreviewed/unaccepted**. The final cross-branch conclusion is in Section 11: an actual path carrying a pair with zero exterior L/D vertices must use a nonallowed matching edge and triggers two actual full tight cores; with one exterior vertex, an allowed carrying edge forces a full tight core in the opposite color. The earlier three-slot inequality is retained as a necessary condition, not a successful elimination. This note does not exclude every tight interface, any entire value of m, or the mixed case in which only one color has a proper tight set. No numerical bound changes.

The generation collaborator owns only this new note. No scientific program, enumeration, solver, proof checker, external review, source modification, metadata change, or historical edit was performed.

## 1. Actual ambient assumptions and inherited facts

Let X be one complete ordered rank-3 signotope with no R6, B6, or weak7, and |X|=2b, b=25. A weak7 uses opposite-color paths with the same actual endpoints and total length 9; internal disjointness is not required. Four-point packets have at most one color change, in abc, abd, acd, bcd order. Paths are hereditary monochromatic sets, equivalently consecutive-triple paths under the packet axiom.

Use the four saturated ambient atoms L,D,T_R,T_B, with |L|=|D|=k=b-m and |T_R|=|T_B|=m. The range 9<=m<=13 is inherited from research-level, unreviewed semantic transfers and is not needed in the proofs below. Actual B5 sources lie in L union T_B and actual B5 terminals lie in D union T_B. H_B is the endpoint graph of all actual B5 paths in the induced configuration Y_B=X minus T_B, on L by D. It has a perfect matching. H_R is defined with colors exchanged in Y_R=X minus T_R; it also has a perfect matching and its edges are disjoint from H_B.

These are assumptions inherited from [the saturated-interface manuscript](N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md), based on [R23](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md), [the global deficit manuscript](N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md), and [the common-assignment manuscript](BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md). Their status is not upgraded here.

Write N(U)=N_HB(U). A tight set U is a subset of L with |N(U)|=|U|; the empty set and L are allowed as boundary cases. Its actual induced core is

    W_U = U union T_R union (D minus N(U)).

It has b vertices and no B5: a B5 in it would start in U and terminate in D minus N(U), contradicting the definition of N(U). It inherits no R6 and no weak7. It is therefore a full actual 756 core. No ambient state is transported into this core.

## 2. Tight sets need not be laminar

If U and V are tight, their union and intersection are tight, and

    N(U union V) = N(U) union N(V),
    N(U intersection V) = N(U) intersection N(V).

Proof. The first equality holds for every graph. Neighborhood inclusion gives N(U intersection V) contained in N(U) intersection N(V). Hall and the two tight equalities yield

    |U|+|V|
      = |N(U) union N(V)| + |N(U) intersection N(V)|
      >= |N(U union V)| + |N(U intersection V)|
      >= |U union V| + |U intersection V|
      = |U|+|V|.

All inequalities are equalities. The finite-set inclusion is consequently equality, and both derived sets are tight. This is ordinary matching uncrossing, not a new packet theorem and not a proof of laminarity.

For nested tight sets U contained in V, put

    A = V minus U,  B = N(V) minus N(U),  r=|A|=|B|,
    Z = V union T_R union (D minus N(U)) = W_U union W_V.

Then |Z|=b+r. The common part of the two full cores has b-r vertices. For incomparable tight sets U_0,V_0, their union of real cores is the same Z obtained from U=U_0 intersection V_0 and V=U_0 union V_0; in that case r=|U_0 symmetric-difference V_0|. Thus the subsequent restriction also applies to crossing tight sets.

## 3. Endpoint localization is an entry, not the claimed gain

For tight U and l in L minus U, every B5 in W_U union {l} starts at l. Otherwise its source is in U and terminal in D minus N(U), an impossible H_B edge. For d in N(U), every B5 in W_U union {d} ends at d, by the same argument. Capacity supplies at least one path in either b+1-point configuration.

This valid localization is special to these ambient endpoint-defined cores. It does not apply to arbitrary full cores. It does not contradict [the genuine full25 internal-insertion example](N7_FULL_CAPACITY_INTERNAL_INSERTIONS_AND_PATH_EXCHANGE_BARRIER_20261028.md). Existence of a private insertion obstruction alone is old content, as audited in [the near-capacity manuscript](N7_NEAR_CAPACITY_COMPATIBILITY_AND_BIDIRECTIONAL_REPARTITION_20261028.md), and is not claimed as this branch's new conclusion.

The useful simultaneous-insertion statement is stronger in scope: **every actual B5 in Z has its source in A and terminal in B.** Indeed, its source lies in V and its terminal lies outside N(U). A source in U is impossible. A source in V forces its terminal to belong to N(V). Hence the endpoint claim. Internal vertices may belong to any part of Z and may be shared by many paths.

For every F contained in Z, let H_F be the endpoint graph of all B5 paths actually contained in Z minus F, on (A minus F) by (B minus F). Recompute this graph internally; do not merely delete endpoint vertices from H_B. Then

    matching_number(H_F) >= max(0,r-|F|).                 (1)

Proof. Any endpoint vertex cover C of H_F meets every B5 in Z minus F, so Z minus (F union C) is a genuine no-B5/no-R6/no-weak7 induced configuration. Since F and C are disjoint,

    b+r-|F|-|C| <= b,

and |C|>=r-|F|. In a finite bipartite graph the minimum cover size equals the maximum matching size: take a maximum matching, follow alternating paths from unmatched left vertices, and choose the unreached left vertices together with the reached right vertices. This covers every edge and has the matching's size. Applying this argument proves (1). For F empty, the graph has a perfect matching on A by B and the actual B5 transversal number of Z is exactly r; deleting A attains the capacity lower bound.

The capacity-to-matching argument is inherited from R22, not independently new. Its use here retains the full support domain Z minus F, rather than just the ambient endpoint graph.

## 4. Packet certificates for the opposite-color prefix and suffix fans

Let P_R be the ambient relation consisting of actual R5 endpoint pairs. All its members refer to the same X. It is deliberately not just H_R: red paths through T_R are relevant and cannot be deleted from the relation.

A useful exact certificate uses an actual red triple x<y<z. If a<x and z<u, and

    chi(a,x,y)=R,  chi(x,y,z)=R,  chi(y,z,u)=R,

then (a,x,y,z,u) is an actual R5. First, the packets (a,x,y,z) and (x,y,z,u), whose first and last entries are red, make both four-point sets fully red. For any two t<t' in {x,y,z}, the packet (a,t,t',u) again has red first and last entries and is fully red. These packets supply every triple containing both a and u as well as all remaining triples. Thus all ten triples are red.

In particular, for each actual red triple T=(x,y,z), define

    A_R(T) = {a<x : chi(a,x,y)=R},
    D_R(T) = {u>z : chi(y,z,u)=R}.

The whole rectangle A_R(T) by D_R(T) lies in P_R. Overlap between different certificates is allowed and incurs no resource charge. This packet gluing is an explicit source of fan relations, not a claim that every R5 must use one chosen triple.

For an actual B5 (a,s,t,u,d), its first four vertices give B4(a,u), and its last four give B4(s,d). Therefore no weak7 implies

    (a,u) not in P_R,  (s,d) not in P_R.                 (2)

The endpoint pairs in (2) are respectively the same actual (a,u) and (s,d) in both colors. Neither exclusion compares unrelated maxima. Red certificate paths may leave Z and may overlap the blue path; the ambient weak prohibition still applies.

## 5. The cross-core three-slot restriction

For every nested tight U contained in V and every F contained in Z, define J_F on (A minus F) by (B minus F). An edge (a,d) is present exactly when there exist three actual vertices

    a<s<t<u<d,  s,t,u in Z minus F,

such that neither (s,d) nor (a,u) belongs to P_R. No assertion about the colors of this five-set is imposed in J_F. This is a relaxation built from actual order, an explicitly restricted support domain, and actual red-five fans.

**Necessary compatibility theorem.** Under the ambient assumptions,

    matching_number(J_F) >= max(0,r-|F|)                 (3)

for every such pair of tight cores and every deletion F. Equivalently, every vertex cover C of J_F satisfies

    |F|+|C| >= r.                                       (4)

Proof. An edge of H_F has an actual five-vertex blue witness (a,s,t,u,d) wholly in Z minus F. Equation (2) shows that these same three internal vertices certify the corresponding edge of J_F. Hence H_F is a subgraph of J_F. Equation (1) proves (3), and the bipartite matching-cover identity proves (4).

The relation P_R in this theorem can be replaced by any certified subset, including any collection of the packet rectangles in Section 4. This enlarges J_F and leaves (3) necessary. Consequently, the forbidden interfaces can be specified entirely by actual monochromatic-triple packet certificates, order, two actual full cores, and a proposed small set F. No solver or exhaustive path calculation is needed for the proof.

This is the branch's support-sensitive composition of the older tools. It is stronger in the information it asks to retain than merely reporting two ambient edge-disjoint matchings: a reported ambient matching says nothing about whether its witnesses remain inside each Z minus F. We do **not** establish strict logical independence from every earlier full-path capacity consequence, nor claim that packet gluing, Hall, or private insertion existence is new.

## 6. A concrete excluded critical-interface subclass

Suppose two nested tight sets differ by two vertices, so A={a1,a2}, B={d1,d2}, and |Z|=27. Suppose there is one q in Z such that, for every a in A minus {q}, d in B minus {q}, and every ordered triple

    a<s<t<u<d in Z minus {q},

at least one of R5(s,d), R5(a,u) is present in the same ambient X. These red paths may be certified by the packet construction above and can differ between triples. Empty ordered-triple families satisfy the condition vacuously.

This critical interface is impossible. Indeed, J_{q} has no edges. Any B5 in Z minus {q} would have endpoints in the displayed A and B and would violate one of its two same-endpoint weak constraints. Thus the actual 26-point induced configuration Z minus {q} would have no B5; it inherits no R6 and no weak7, contradicting b=25. In general, the same argument excludes any F with |F|<r for which all three-slot routes are closed, and (4) allows a further endpoint cover C with |F|+|C|<r.

This is an actual forbidden interface with all quantifiers and the final capacity contradiction specified. It is not a claim that such a 50-point configuration was constructed, nor that every hypothetical 50-point configuration must exhibit this interface. It does not infer disjoint interiors from a matching. It does not require a shared internal triple to be forced between distinct blue paths. It also does not require a tight set on the red side: the mixed tight/strict case is covered by the necessary restriction, but is not excluded in full.

## 7. First genuine gap and unsuccessful stronger deductions

The first unresolved step is to show that some two tight cores and some F,C with |F|+|C|<r have enough actual red-five fans to close every remaining ordered three-slot route. Saturation and Hall alone do not supply this coverage, the requisite order of the fan endpoints, or a forced shared monochromatic triple. We have no proof that the forbidden subclass in Section 6 is unavoidable.

In particular:

- A proper tight set need not belong to a chain whose successive sizes differ by one or two. The r=2 illustration does not exclude all tight cases.
- Crossing tight sets give additional actual cores and the union domain above; they do not imply laminarity or a positive deficit.
- The internally recomputed matchings may use shared vertices. No conclusion of internally disjoint path packing follows from (1).
- Red fan relations may be too sparse, or positioned so that many ordered triples survive. The theorem does not give their density.
- For a single tight set one may use the intervals empty-to-U and U-to-L. These are valid applications, but do not by themselves supply an obstruction in either interval.
- The one-color-tight/other-color-strict branch remains unresolved. So does the case in which both endpoint graphs are strict Hall.

No weaker single-full-core example is offered as a counterexample to these ambient assumptions. No conditional exchange is presented as an existence theorem, and no new upper bound is inferred.

## 8. Attribution and outcome

[R3 Section 6.3](RESET_R3_BIDIRECTIONAL_IDEAL_INTERVALS.md) already proves actual same-endpoint support-rectangle exclusion and reliable shared-middle-edge gluing. [R22 Section 5.1](RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md) already converts full-path transversal lower bounds into endpoint matchings and explicitly allows shared interiors. [R23](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md) supplies the four-core saturation and complementary pure supplies. The [2026-10-28 interface manuscript](N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md) supplies the two actual induced endpoint matchings and the original opposite-color pair-shadow exclusions.

The present conclusion keeps support deletions inside unions of multiple actual Hall-tight cores and applies actual red-five prefix/suffix restrictions before extracting a matching. The resulting necessary inequality (3), and its explicit support-bottleneck forbidden subclass, are the complete mathematical output of this branch. Their usefulness for eliminating every critical interface has not been proved.

The inherited working bounds remain 40/50/80/81. New global numerical decrease: 0. All generation and proofs here remain unreviewed/unaccepted; no independent review or acceptance occurred.

## 9. Cross-challenge: allowed edges and the missing-corner gap

The parent correctly challenged (3) as a composition of the old transversal bound and an overapproximation. It remains a proved necessary condition, not a successful elimination of the tight branch. The following sharper target was then examined.

In a balanced bipartite graph H with a perfect matching, an edge (l,d) belongs to no perfect matching if and only if some tight U satisfies

    l not in U,  d in N(U).                             (5)

Proof. If such U exists, every perfect matching must match U onto all of N(U), leaving d unavailable for l. Conversely, if (l,d) extends to no perfect matching, remove l,d. Hall fails in the remaining balanced graph, giving U contained in L minus {l} with |N(U) minus {d}|<|U|. Original Hall gives |N(U)|>=|U|. Hence |N(U)|=|U| and d belongs to N(U). This is a standard matching fact; its exact barrier form matters here. In particular, strict Hall on every nonempty proper left subset makes every edge allowed.

Apply (5) to a hypothetical nonallowed actual H_B edge (l,d), with actual B5 witness P. The full W_U and its two separate insertions force actual B5 paths

    Q: l -> d',  d' in D minus N(U),  Q contained in W_U plus l,
    R: l' -> d,  l' in U,             R contained in W_U plus d.

All alternatives are retained. The missing corner (l',d') cannot be an H_B edge. If Q and R had three common vertices strictly between l' and d', the red-triple packet argument of Section 4, with colors exchanged, would construct B5(l',d') wholly in W_U. Consequently

    |Q intersection R intersection (l',d')| <= 2.       (6)

This is not yet a proof that every actual edge is allowed. A shared pair only gives B4(l',d'), which is compatible with W_U being B5-free. The original path P can have a different internal support; neither capacity nor (5) forces its extra vertex to extend the shared pair to a common triple. Packet constraints cannot be skipped at precisely that missing extension. No universal all-edges-allowed theorem is claimed.

## 10. Cross-challenge: a concentrated witness pair and a new full core

Here the setup is conditional on a witness concentration identified by the parent and Branch B. Suppose k is even, q=k/2 blue matching witnesses share an internal pair x<y, with their q distinct sources I and q distinct terminals J. Then all I<x<y<all J. Packet gluing gives B4(i,x,y,j) for every i in I, j in J. Thus there is no actual R5(i,j), by the same-endpoint weak7 prohibition. The red matching graph avoids I by J; Hall forces N_HR(I)=D minus J. The actual core

    W = I union T_B union J

has b vertices and no R5. The pair x,y lies outside W: the chosen blue witnesses avoid T_B, and their shared internal points cannot be in I or J by the displayed strict order.

For v=x or y, capacity forces an R5 in W plus v. It must have v as an endpoint: if v were internal, its endpoints would be in I and J, contradicting the blue-four rectangle. The atom cases are exact:

- v in L: every such R5 starts at v and ends in J; its old support lies in (T_B strictly after v) union J.
- v in D: every such R5 starts in I and ends at v; its old support lies in I union (T_B strictly before v).
- v in T_R: incoming and outgoing paths are both possible; either or both families may exist. There is no justification for choosing a convenient direction.

If x has an outgoing R5 and y an incoming R5, their old supports can meet only inside T_B intersection (x,y). Three common internal points would create R5(i,j) for their actual source i in I and terminal j in J, contradicting the blue-four rectangle. Two common points create only R4(i,j), whose length sum with B4 is 8; that is not weak7. For a pair (i,j) that is itself one of the chosen blue-five matching edges, two common points do suffice for a contradiction, since R4+B5 has total length 9. Neither threshold may be substituted for the other.

No argument here forces three common points across all endpoint choices, or forces the chosen endpoints to be one of those matched pairs. The other direction patterns and all three atom types remain open. This equality analysis therefore supplies localization and exact overlap exclusions, not a contradiction for the full concentration case.

## 11. Final cross-branch bridge: central pairs force actual tight cores

This section records the parent/Branch B full-fan theorem together with the exact allowed-edge and real-core consequences checked in this branch. It is mathematical generation collaboration, not independent review. Let x<y be any two actual vertices, with no atom restriction. Define

    A_c(x,y) = {l in L : l<x, chi(l,x,y)=c},
    D_c(x,y) = {d in D : y<d, chi(x,y,d)=c},
    s_c(x,y) = k-|A_c(x,y)|-|D_c(x,y)|,
    e(x,y)   = |{l in L:l>=x}|+|{d in D:d<=y}|.

Each color-c rectangle A_c by D_c consists of actual c4 endpoint pairs: the packet (l,x,y,d) has equal first and last color c and is fully color c. Hence H_opposite contains no edge in this rectangle, since c4 plus opposite5 would be weak7 with the same actual endpoints. Hall in H_opposite gives |A_c|+|D_c|<=k, including the empty-set cases. Thus s_c>=0.

The two source fans partition L strictly before x, and the two terminal fans partition D strictly after y. Consequently

    s_R+s_B=e.                                         (7)

For any perfect matching M in H_c, the number of its edges with both ends outside A_opposite and D_opposite is exactly s_opposite. To see this, no edge of M lies in A_opposite by D_opposite. Exactly |A_opposite| matching edges meet its left fan and exactly |D_opposite| meet its right fan, with no double count; all other edges lie in the two complements.

If an actual c5 path in Y_c carries x,y internally, its source is in A_c and terminal in D_c. If its endpoint edge is allowed, extend that edge to a perfect matching and choose this actual path as its witness. Its edge lies in both complements of the opposite fans, so

    s_opposite>=1.                                    (8)

There is no assumption that all matching witnesses share the pair. A single allowed carrying edge is sufficient for (8).

**Zero exterior vertices.** If e=0, then s_R=s_B=0, and (8) fails. Therefore every actual induced c5 carrying x,y has a nonallowed edge. Section 9 supplies an actual tight barrier U in its own endpoint graph, and the two insertion paths Q,R, with the exact missing-corner gap already stated.

There are also two additional full real cores. An actual carrying path makes A_c and D_c nonempty. Since all L lies before x and all D after y, and |A_c|+|D_c|=k, both are proper. Their opposite-color complementary fans are likewise nonempty proper. Hall plus rectangle exclusion therefore gives

    N_HR(A_B)=D minus D_B,
    N_HB(A_R)=D minus D_R.

The actual induced configurations

    W_Rfree = A_B union T_B union D_B,
    W_Bfree = A_R union T_R union D_R

each have exactly b vertices and respectively no R5 and no B5. The first is a full color-dual 756 core and the second a full 756 core. Their definitions use actual fan neighborhoods, not independent abstract assignments. In fact they are disjoint and partition X. The pair x,y cannot belong to L or D when e=0. If it is carried by a path in Y_c, it must therefore lie in T_opposite. It lies inside the corresponding core with no c5; its carrying path has endpoints outside that core, which is not a contradiction.

**One exterior vertex and an allowed carrying edge.** If e=1 and an actual induced c5 carrying x,y has an allowed edge, (7)-(8) force s_c=0 and s_opposite=1. Its own fans are nonempty; equality makes them proper. Rectangle exclusion and Hall force

    N_Hopposite(A_c)=D minus D_c.

Thus

    W=A_c union T_c union D_c                         (9)

is an actual full b-point core with no opposite5. The through atom in (9) is T_c, not T_opposite. The allowed-edge hypothesis cannot be dropped from this e=1 conclusion: a nonallowed carrying edge does not by itself imply (8).

**Both graphs strict.** If both H_R and H_B satisfy strict Hall on every nonempty proper left subset, every actual edge is allowed by Section 9. An actual carrying path makes A_c,D_c nonempty. Strict Hall in the opposite graph and rectangle exclusion force s_c>=1, while (8) gives s_opposite>=1. Therefore e>=2. Equivalently, no actual induced path in either color may carry an internal pair with e<=1 in this strict/strict case.

These are genuine restrictions on actual supported paths and give full-core consequences in the tight cases. They do not prove that some carrying path with e<=1 must exist. Nor do they exclude the two extra cores in the e=0 case: the insertion paths from Section 9 still need a packet-valid missing-corner extension, and their supports need not share three internal points. The mixed strict/tight case and all complete m branches remain unresolved. The three-slot test from Sections 5-6 is a supplementary necessary condition; it is not counted as a new all-class closure.

Final status: full-fan central-pair restrictions and their tight-core bridge are proved here at research-draft level; universal exclusion and any new global numerical gain are not. The working chain remains 40/50/80/81, unreviewed/unaccepted.
