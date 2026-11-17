# Branch B: actual internal-pair boundary restriction

Date: 2026-10-29. Mathematical generation note, **unreviewed/unaccepted**. No independent review, solver, enumeration, research-code execution, or new literature was used. This note changes no historical artifact or acceptance state. There is no new global bound and no proof that the strict-Hall branch is empty.

## 1. Actual frame and attribution

Fix the hypothetical complete ordered rank-3 signotope X of size 50 with no R6, B6, or weak7. All paths below are actual paths in this one coloring. Their length is their number of vertices. Packet order is abc, abd, acd, bcd, with at most one color change. Monochromatic paths are hereditary on subsequences. Weak7 uses the same actual first and last vertices, and forbids opposite-color path lengths summing to at least 9, by shortening if necessary.

Use the four saturated ambient atoms from [the saturated-interface note](N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md):

\[
X=L\sqcup D\sqcup T_R\sqcup T_B,\qquad |L|=|D|=k=25-m,\quad |T_R|=|T_B|=m.
\]

Here 9<=m<=13 and 12<=k<=16 use the previously stated Through14 and Joint17 semantic conclusions with their unchanged evidence limitations. H_B is the graph of all actual B5 endpoints in Y_B=X\T_B; H_R is defined using all actual R5 in Y_R=X\T_R. Both have vertex classes L,D, both have perfect matchings, and they have disjoint edge sets. Paths in these graphs can have internal L or D vertices. No claim restricts their internal supports to a through atom.

The baseline saturation and complete pure supplies come from [R23, section 5](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md). Same-pair Cartesian gluing and same-endpoint restrictions are old tools from [R3, section 6.3](RESET_R3_BIDIRECTIONAL_IDEAL_INTERVALS.md); endpoint matching with potentially shared interiors is also old [R22, section 5.1](RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md). They are not claimed as new here. The deduction studied here combines the **full actual triple fans**, their complementary colors on the same owners, and the two matching constraints. It does not merely use the old pure-supply shadows inside T_R or T_B.

Other primary context read: [the global frame](N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md), [common assignment](BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md), [near-capacity audit](N7_NEAR_CAPACITY_COMPATIBILITY_AND_BIDIRECTIONAL_REPARTITION_20261028.md), and [internal-insertion/path-exchange barrier](N7_FULL_CAPACITY_INTERNAL_INSERTIONS_AND_PATH_EXCHANGE_BARRIER_20261028.md). The last source's single-full-core example is not a counterexample to this full X50 frame.

## 2. Full fans and their exact boundary budget

Fix any two actual vertices x<y, with no assumed atom types. For c in {R,B}, define

\[
A_c(xy)=\{l\in L:l<x,\ \chi(l,x,y)=c\},\qquad
D_c(xy)=\{d\in D:y<d,\ \chi(x,y,d)=c\}.
\]

Write a_c=|A_c(xy)|, d_c=|D_c(xy)| and

\[
s_c=k-a_c-d_c,\qquad
e(xy)=|\{l\in L:l\ge x\}|+|\{d\in D:d\le y\}|.
\]

The weak inequalities in e are intentional if x or y itself belongs to L or D. Every relevant actual triple has exactly one color, so

\[
A_R\sqcup A_B=L_{<x},\qquad D_R\sqcup D_B=D_{>y},\qquad s_R+s_B=e(xy). \tag{1}
\]

For l in A_c and d in D_c, the packet on l<x<y<d starts and ends with c. It is therefore entirely c and gives a c4 from l to d. Consequently

\[
H_{\bar c}\cap(A_c\times D_c)=\varnothing. \tag{2}
\]

The opposite graph's perfect matching gives a_c+d_c<=k and hence s_c>=0. This remains valid when one fan is empty: then the other fan has size at most k.

More precisely, in **every** perfect matching M of H_bar_c, exactly s_c edges have their source outside A_c and their terminal outside D_c. Indeed the a_c edges whose sources lie in A_c and the d_c edges whose terminals lie in D_c are disjoint collections by (2); every remaining edge lies in the complementary rectangle. This is an exact edge count and says nothing about disjointness of path interiors.

Choose arbitrary perfect matchings of both graphs and independently choose any actual induced 5-path realizing every matched edge. Let r and b count the red and blue chosen witnesses containing x,y both internally. A red witness of this kind cannot start in A_B or end in D_B, because its corresponding actual triple has color R. The exact complementary-rectangle count therefore yields

\[
r\le s_B,\qquad b\le s_R,\qquad r+b\le e(xy). \tag{3}
\]

These statements quantify over all choices of perfect matchings and all their alternative actual witnesses. Pure supplies are included without selecting a preferred supply. The proof also includes non-pure paths and pairs from every atom type.

## 3. Main actual-path theorem and the mixed-case dichotomy

Call an edge extendable if it belongs to a perfect matching of its actual graph.

**Theorem.** Suppose an actual c5 in Y_c has internal vertices x<y and has an extendable endpoint edge in H_c.

1. e(xy)=0 is impossible.
2. If e(xy)=1, then A_c(xy) is a nonempty proper Hall-tight set in H_bar_c, with

\[
N_{H_{\bar c}}(A_c(xy))=D\setminus D_c(xy),\qquad
|A_c(xy)|+|D_c(xy)|=k. \tag{4}
\]

3. If H_bar_c strictly expands every nonempty proper subset of L, then e(xy)>=2.

**Proof.** Extend the specified endpoint edge to a perfect matching of H_c and use the specified actual path as its witness. Choose arbitrary witnesses for all other edges and choose any opposite perfect matching. Thus the count for color c in (3) is at least one, and s_bar_c>=1. Since s_c>=0 and e=s_c+s_bar_c, e>=1, proving item 1.

If e=1, necessarily s_c=0. Both A_c and D_c are nonempty, because the given path supplies its actual source and terminal. Hence a_c+d_c=k, with 0<a_c<k. Equation (2) gives N_Hbar_c(A_c) contained in D\D_c. Hall gives the reverse cardinality bound a_c, while |D\D_c|=a_c. Equality of sets and Hall tightness follow, proving item 2. Strict Hall excludes (4), proving item 3. Equivalently, strict Hall directly gives s_c>=1 whenever the own-color fan rectangle is nonempty. Together with s_bar_c>=1 this gives e>=2. QED.

**Both-strict corollary.** If both actual induced graphs strictly expand every nonempty proper U subset L, then **every actual 5-path in either Y_c**, and every pair of its internal vertices x<y, satisfies

\[
\boxed{|L_{\ge x}|+|D_{\le y}|\ge2.} \tag{5}
\]

To justify the universal quantifier, every edge (l,d) of a strictly expanding balanced graph extends to a perfect matching. Delete l,d. For any nonempty U subset L\{l}, strict Hall in the original graph gives |N(U)|>=|U|+1, so deletion of d leaves at least |U| neighbors. The empty U is trivial. Hall gives a matching in the deleted graph, and restoring (l,d) completes it. This proof does not require Ferrers structure or an uncrossing rule.

Thus the both-strict branch forbids any induced 5-path whose internal pair has zero or one boundary owner counted by (5). In particular, two strictly central vertices, after every L and before every D, cannot both be internal to such a path. This is a conditional exclusion of an actual path-support pattern throughout the full X50 frame; it is not a construction of X50 and does not prove that every X50 must contain the forbidden pattern.

The mixed case is explicitly retained: e=1 for an extendable actual edge produces the tight set (4), so it returns to a genuine tight branch. An actual edge in a merely Hall graph need not be extendable; this note makes no unsupported deduction for such an edge.

**Central-pair entry without extendability.** If e=0 and an actual c5 in Y_c uses xy internally, then both graphs have nonempty proper tight sets and that carrier edge belongs to no perfect matching. Indeed (1) and nonnegative slacks give s_R=s_B=0. The carrier makes A_c,D_c nonempty, so a_c+d_c=k makes both proper. Complementarity now makes A_bar_c,D_bar_c nonempty as well. Applying the rectangle avoidance and Hall argument in both colors gives

\[
N_{H_{\bar c}}(A_c)=D_{\bar c},\qquad
N_{H_c}(A_{\bar c})=D_c.
\]

Every perfect matching of H_c must match all of D_c from A_bar_c; it therefore cannot use the carrier edge from A_c into D_c. This proves the precise both-tight entry instead of silently discarding nonextendable edges. The two actual cores

\[
W_{R\text{-free}}=A_B\cup T_B\cup D_B,\qquad
W_{B\text{-free}}=A_R\cup T_R\cup D_R
\]

are disjoint, each has size25, and together cover X; they respectively contain no R5 and no B5 by the rectangle argument. This is a genuine actual full-core decomposition, not a contradiction. For example, a blue carrier has its endpoints in the first core while its two central internal vertices are in T_R in the second core, so its existence does not contradict either core's internal prohibition.

## 4. The e=1 tight core and the first unresolved insertion step

Under item 2, put A=A_c(xy), J=D_c(xy) and

\[
W=A\cup T_c\cup J.
\]

This is an actual 25-point core, since |A|+|J|=k and |T_c|=m. It contains no opposite-color 5-path: it lies in Y_bar_c, every such path would have source in A and terminal in J, and (2) forbids that endpoint pair. It inherits the other ambient forbidden shapes.

Both x,y are outside W. They lie outside T_c because they are on the original path in Y_c; all A precedes x and all J follows y. Capacity b25 therefore forces an opposite-color 5-path in W+v for each v in {x,y}. Every such new path uses v. Moreover **v must be an actual endpoint**: if it were internal, the source and terminal would belong to A,J, contradicting their c4 rectangle and weak7. This conclusion concerns these tight cores, not arbitrary full cores.

In the blue-carrier/red-insertion notation, write I=A_B(xy) and J=D_B(xy). An R5 ending at v has its other four vertices in I union T_B and its first point in I; an R5 starting at v has its other four vertices in T_B union J and its last point in J. This follows from I<x<y<J and the ambient source/terminal identities. All replacement supplies must still be retained.

Attempted next step: classify whether the forced R5 at x and at y point in or out. For the pattern “an R5 ends at x and an R5 starts at y”, let a be the former's penultimate point and b the latter's second point. No R6 forces chi(a,x,y)=B and chi(x,y,b)=B; packet gives B4(a,x,y,b). If the original carrier also has a third internal point z between x and y, the corresponding extension constraints and carrier triple give B5(a,x,z,y,b). This is a valid replacement path. It is **not** a B6 or a same-endpoint weak7 contradiction. The missing extra point cannot be supplied by joining unrelated extrema.

No complete exclusion of this pattern or of all four in/out possibilities was obtained. Consequently the insertion localization and the mixed-case tight set are proved consequences, while the proposed global contradiction stops here. A tight block is not thereby a region isolating all path interiors.

## 5. Secondary coupled incidence bounds, including arbitrary cycles

For any fixed xy and arbitrary matching witnesses as in section 2, one also has

\[
2r+b\le k,\qquad r+2b\le k,\qquad r+b\le\lfloor2k/3\rfloor. \tag{6}
\]

Proof: the r red witnesses give r distinct sources I and r distinct terminals J. Their common internal pair makes I times J a red4 rectangle. The blue matching avoids that rectangle. Its r edges starting in I and r edges ending in J are disjoint, so exactly k-2r blue matching edges lie in the complementary rectangle. Every blue witness using xy must lie there, since a common source or terminal would give a triple of both colors. Thus b<=k-2r. Exchange colors for the other inequality.

For any alternating cycle in the union of the two matchings, let its length be 2h. The identical proof, restricted to that cycle's h sources and h terminals, gives

\[
2r_C+b_C\le h,\qquad r_C+2b_C\le h,\qquad r_C+b_C\le\lfloor2h/3\rfloor. \tag{7}
\]

This covers every possible alternating-cycle length. It does not interpret an abstract alternating cycle as a directed actual-path cycle. In cycle-edge language, two occurrences of xy cannot be adjacent (opposite-color shared endpoint triple) or distance two apart (same-color rectangle forbidden to the intervening opposite edge). Neither argument assigns exclusive owners to different witnesses.

Under strict Hall in the opposite graph, r>0 also gives 2r<=a_R+d_R<=k-1, and similarly for b. Hence each color's multiplicity is at most floor((k-1)/2). The improvement over the non-strict floor(k/2) bound is only for even k. These are necessary support-incidence restrictions, not vertex-disjoint path packings or an additive resource charge.

For completeness, actual internal triples provide an exact support-labelled description of H_c. For a c-monochromatic triple T={u<v<w} in Y_c, take all l in L before u such that l union T is c4, and all d in D after w such that T union d is c4. Every crossed choice produces c5 on l union T union d: packet on l, any two T vertices,d supplies the missing mixed triples. Conversely every actual c5 has such an internal triple. This is an application of the old gluing tool, not a new gluing theorem; it keeps the full alternative supports visible.

## 6. Precise obstacle and stopping point

An attempted proof based only on edge-disjointness and strict Hall in the two endpoint graphs cannot conclude nonexistence. For every k from 12 through 16, take abstract L_i,D_i with indices modulo k, put blue edges at offsets 0,1 and red edges at offsets 2,3. Each graph is a connected 2-regular bipartite cycle. If a nonempty proper U had |N(U)|=|U|, degree counting would leave no edges from N(U) to the remaining left vertices, contradicting connectivity. Thus each graph strictly expands; their edge sets are disjoint. All L may be ordered before all D without violating edge direction.

This is **only a countermodel to that specified endpoint-graph axiom set**. It is not a coloring, does not specify complete pure supplies or full triple fans, does not satisfy a claimed actual capacity model, and is not a real critical X50 counterexample. In particular it does not refute the complete actual pair-shadow mechanism or theorem (5).

The lost information in that graph-only projection is concrete: an endpoint edge is an existential statement about one of many internal triples, while the same actual triple color must be shared by all witnesses using those owners. The complementary identities (1) preserve some of that information and produce the genuine new boundary restriction (5). Old pure-through shadows alone do not express (1) for all actual pairs. Conversely, proving (5) does not establish that every saturated frame has a carrier pair with e<=1.

The remaining burden is to force an actual forbidden boundary support, or to close the e=1 tight-core insertion patterns using all supplies and shared triples. Neither has been completed here. Mixed tight/strict graphs and the both-tight case are not declared solved. The 40/50/80/81 global baseline and all prior evidence/acceptance limitations remain unchanged.

## 7. Same-turn revision, 2026-10-29: e=1 entry without extendability

The root collaboration supplied the following strengthening after the initial note. The proof below was checked within mathematical generation, not independently reviewed. It removes the extendability assumption from the **existence of a proper tight-set entry** at e=1. The earlier theorem remains valid and identifies the particular tight set when the carrier is extendable.

**Strengthened dichotomy.** Let P be any actual c5 in Y_c with internal pair x<y and e(xy)=1. There are exactly two possible integer slack cases:

* If s_c=0 and s_bar_c=1, then A_c is a nonempty proper tight set in H_bar_c, with N_Hbar_c(A_c)=D\D_c. This conclusion does not require the carrier edge to be extendable.
* If s_c=1 and s_bar_c=0, then A_bar_c is a nonempty proper tight set in H_c, with N_Hc(A_bar_c)=D\D_bar_c. The endpoint edge of P belongs to no perfect matching of H_c.

**Proof.** Section 2 gives nonnegative integer slacks summing to e=1, so these cases are exhaustive. The actual carrier gives a_c>=1 and d_c>=1.

In the first case a_c+d_c=k. Both own-color fans are therefore nonempty and proper. Rectangle avoidance gives N_Hbar_c(A_c) contained in D\D_c, and Hall gives cardinality at least a_c=|D\D_c|. Equality of neighborhoods follows, proving the first claim independently of any matching containing the carrier.

In the second case a_c+d_c=k-1. Since each term is positive, each is at most k-2. Put ell=|L_<x| and t=|D_>y|. Because (k-ell)+(k-t)=e=1 and each deficit is nonnegative, ell>=k-1 and t>=k-1. Complementarity of the actual fans gives

\[
a_{\bar c}=\ell-a_c\ge1,\qquad
d_{\bar c}=t-d_c\ge1.
\]

Moreover s_bar_c=0 gives a_bar_c+d_bar_c=k, so both opposite-color fans are proper. Apply rectangle avoidance and Hall to H_c to obtain

\[
N_{H_c}(A_{\bar c})=D\setminus D_{\bar c}.
\]

Every perfect matching of H_c has exactly s_bar_c=0 edges in (L\A_bar_c) times (D\D_bar_c), by the exact count in section 2. But the carrier starts in A_c and ends in D_c, and opposite-color fans are disjoint in each coordinate. Its edge lies in this complementary rectangle and therefore belongs to no perfect matching. QED.

Consequently **any actual e=1 carrier**, including a nonextendable one, forces an explicit proper tight set in at least one graph, with the slack determining which graph and which set. An extendable carrier cannot fall in the second case, agreeing with section 3. The first case still does not assert that the carrier is extendable.

Together with the e=0 both-tight conclusion in section 3, this gives a direct proof that both strict graphs prohibit every actual induced carrier with e<=1. The proof of the universal boundary bound (5) can therefore avoid the edge-extension lemma entirely. The bound and its actual-path quantifiers are unchanged; this revision strengthens the mixed-case entry. It does not claim that either tight-set case has been eliminated, and it does not supply a new global numerical bound.
