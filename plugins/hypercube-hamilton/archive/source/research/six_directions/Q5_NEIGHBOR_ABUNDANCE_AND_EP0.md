# Proof Package: Q5 free-neighbor abundance and EP0

Date: 2026-11-01. ARIS proof-writer. New proof package; previously audited files and global coverage state are unchanged. Independent semantic/finite audit is pending.

## Claims

**Q5 neighbor abundance.** Let $M$ be an arbitrary complete-graph matching on $V(Q_5)$ with exactly two distinct holes $q,v$ of equal parity. Let $U(M;q,v)$ consist of the short neighbors $a$ of $q$ for which there is a simple cycle on $V(Q_5)\setminus\{v\}$ containing $M$ and the edge $qa$, with every edge outside $M$ short. Then
$$|U(M;q,v)|\ge3.$$
Since $q$ is a hole, every incident cycle edge is new and short.

**EP0 consequence.** In an $(a,b)=(2,0)$ eight-hole cut as defined in `EIGHT_HOLE_COVERED_NEXT_DRAFT.md`, suppose there is an odd original crossing port $q\ne v$ with
$$|N_A(q)\cap S|\ge3,\qquad S=\{\bar w:w\in W\}.$$
Then EP0 holds at that cut. The original Q6 matching is short; the auxiliary complete-graph matching need not be short or bipartite.

## Status

**PROVABLE AS STATED**, subject to the explicit finite inputs and existing imported theorems below passing their independent audit. A complete mathematical reduction and positive finite certificates are supplied. The new sixty-million-pair finite check currently has a complete producer result; independent fresh-context verification is in progress. This document alone does not assert an unconditional final eight-hole or P6 theorem.

## Assumptions and notation

A short edge differs in one bit. All required matching edges in the Q5 abundance theorem may have arbitrary lengths or parity. A free vertex is not incident to a required matching edge. Coordinate cuts have mirror pairs with the same remaining local labels.

For a Q4 matching $F$ with free vertex0 and omitted equal-parity vertex $h$, let $\mathcal P(F)$ be the family of unordered neighbor pairs at0 occurring in its valid fifteen-cycles. For a complete perfect matching $P$ on Q4, let $G(P)$ consist of unit vertices $a\in\{1,2,4,8\}$ for which a Hamilton cycle containing $P$ uses $0a$ as a new edge. An edge of $P$ itself is excluded from this optional-edge set.

## Dependencies

1. Q4 free-neighbor classification below: $|\bigcup\mathcal P(F)|\ge3$ for either possible equal-parity hole distance.
2. The existing Q4 perfect-matching extension theorem, allowing arbitrary complete-graph matchings and only short new edges.
3. `Q4_PERFECT_ENDPOINT_ABUNDANCE.md` and its checked full minimal-endpoint-set classification: $|G(P)|\ge2$ for every Q4 perfect matching. A Hamilton $0$--$a$ path containing $P$ is equivalent to a Hamilton cycle containing $P$ with optional edge $0a$, by closing/deleting that short edge. The path cannot contain its own endpoint edge $0a$ on sixteen vertices.
4. The audited complete opposite-hole Q4 fourteen-cycle tables, used to describe exact unavailable optional edges of a perfect matching.
5. The finite star-input mask check described in Step4.

## Proof of Q5 abundance

### Step1. The complete Q4 neighbor-pair data

Normalize free vertex $q$ to0. Its distinct equal-parity omitted vertex can be normalized to3 or15 by coordinate permutation. For either geometry, every one of the $135135=13!!$ arbitrary matchings on the other fourteen vertices is included.

The exact neighbor-union histograms are:

| Omitted vertex | Matchings with union size3 | Matchings with union size4 |
|---:|---:|---:|
|3|208|134927|
|15|212|134923|

These are independently obtained in two ways. `eight_ep0_q4_neighbor_inverse.py` contracts a required optional edge $0s$ through the original edge $st$, obtaining a fourteen-cycle matching with holes $h,s$. Each audited negative matching has the unique inverse obtained by replacing its edge $0t$ with $st$. No matching is unavailable at two different unit neighbors. Outside the complete negative inverse sets, the positive fourteen-cycle expands through $0-s-t$ to give a fifteen-cycle.

`verify_eight_ep0_q4_neighbor_spectrum.cpp` independently enumerates all input matchings and every possible short degree completion: degree two at0, zero at the omitted vertex, one at all other vertices. It rejects repeated required edges, checks exact cycle support and connectivity, and accumulates every available neighbor. There are116 degree patterns for omitted3 and96 for omitted15. The exact histograms coincide and the checker reports PASS.

For omitted15, the fuller pair-family classification in `eight_ep0_q4_pair_spectrum.json` shows precisely444 matchings for which
$$\bigcap_{B\in\mathcal P(F)}B\ne\varnothing.$$
The intersection is a single center $a$; two mandatory neighbors would contradict the union lower bound. For each center $a\in\{1,2,4,8\}$ there are111 such matchings. These are the star matchings. The remaining134691 matchings have empty pair intersection.

`eight_ep0_q4_star_A_prepare.cpp` supplies every star matching, its center, all its positive fifteen-cycle witnesses, and the union $U_A(F)$ of optional short edges in those cycles that are not incident to0. The files are `eight_ep0_q4_star_A.jsonl` and `eight_ep0_q4_star_A.bin`. No required matching edge is included in this union.

### Step2. A positive-crossing cut of Q5

Choose a coordinate on which $q,v$ agree. Let A contain both holes and B be its opposite Q4 face. The crossing count $c$ is even. Suppose $c>0$.

Pair all A crossing ports arbitrarily into an artificial matching D. Together with $M_A$ this is a Q4 matching with holes $q,v$. Step1 supplies fifteen-cycles whose optional neighbors at $q$ have union size at least three.

For any one of these cycles, delete D, attach every original crossing, and compress the resulting A path forest to edges on the distinct B ports. There is no closed component: deletion of the nonempty D breaks the original A cycle into paths, and crossing attachments have distinct leaves. Join the compressed edges to $M_B$ to form a perfect matching on B. The Q4 perfect-matching extension theorem gives a Hamilton B cycle; expansion restores the entire A face except $v$ and produces a thirty-one-cycle containing the original M.

No edge at $q$ was deleted, since $q$ is a hole and is in no edge of D. Therefore each of the at-least-three A neighbor options survives in a Q5 cycle, possibly with a different B completion. This proves the abundance bound whenever such a positive-crossing common-coordinate cut exists.

### Step3. Zero crossings when $d(q,v)=2$

There are three coordinates on which $q,v$ agree. If any has positive crossings, Step2 applies. Otherwise each of the three common-coordinate cuts has zero crossings.

For any one of these cuts, choose an A fifteen-cycle and a B Hamilton cycle both having the same optional short edge $qa$ in their common local labels. Such an edge exists: Step1 gives at least three available A unit neighbors; Dependency3 gives at least two B unit neighbors among the same four units, so the two sets intersect.

Delete the two copies of $qa$ and add the two mirror bridges at $q,a$. The two opened disjoint cycles become one thirty-one-cycle on exactly $Q_5-v$, retain every original matching edge, and use only short new edges. Its neighbor at q across this cut is the vertical mirror of q. Repeating this existential construction at each of the three zero-crossing common-coordinate cuts yields three distinct vertical neighbors of q. The cycles need not be the same. This proves the abundance bound for distance2.

### Step4. Zero crossings when $d(q,v)=4$

There is exactly one common-coordinate cut. If it has positive crossings, use Step2. Otherwise A contains a Q4 matching F with holes $q,v$, and B a Q4 perfect matching P. Normalize common local labels to $q=0,v=15$.

Let $\mathcal F=\mathcal P(F)$ and $G=G(P)$. Splicing A and B at an optional edge $0a$ with $a\in G$ preserves the other A neighbor $b$ from the pair $\{a,b\}\in\mathcal F$ and adds the vertical neighbor of0. Thus every vertex in
$$T=\{b:\text{ some }a\in G\text{ satisfies }\{a,b\}\in\mathcal F\}$$
is a realizable nonvertical Q5 neighbor.

Here $|G|\ge2$ and $|\bigcup\mathcal F|\ge3$. If $T$ had size one, say $T=\{b\}$, then $b\notin G$: any edge of $\mathcal F$ entirely in G would put both its endpoints in T. Every family edge incident to G must contain b. At most two vertices lie outside G, so any family edge disjoint from G must also contain b. Hence every edge of $\mathcal F$ contains b. Therefore $\mathcal F$ has a mandatory center outside G.

It follows that $|T|\ge2$ unless F is one of the444 star matchings and its center $a$ is unavailable in P. In all nonexceptional cases the two nonvertical neighbors in T and the vertical neighbor give the desired bound.

For the exceptional pairs, use a non-q optional edge. If
$$U_A(F)\cap U_B(P)\ne\varnothing,$$
where $U_B(P)$ is the exact union of optional short edges over B Hamilton cycles, select one common edge, choose its witnessing A and B cycles, and splice at that edge. Since the edge is not incident to q, the resulting Q5 cycle retains both distinct A neighbors of q. Separately the q-edge splice already supplies a cycle containing the vertical q neighbor. This again yields at least three Q5 neighbor options.

The displayed intersection holds for every exceptional F,P pair, by the following complete finite certificate.

**Exact exceptional P universe.** For a fixed unit center a, P is unavailable at optional edge $0a$ in exactly two disjoint cases. First, P contains $0a$, giving $135135=13!!$ matchings. Second, $P(0)\ne a$ and its Hamilton $0$--$a$ path contraction is one of the51 audited negative fourteen-cycle matchings on holes0,a. For each negative T, choose an edge $bc$ and either endpoint assignment, then replace it by $0b,ac$. These give714 distinct nonmatching-edge obstructions. This follows from the exact endpoint-path contraction and its unique inverse; hence all135849 exceptional perfect matchings are included.

**Exact $U_B$ masks.** For each of the32 Q4 short edges, perform the same negative inverse construction. `eight_ep0_q4_PB_bad_optional.py` produces16816 distinct perfect matchings with22848 labeled unavailable nonmatching optional edges. For any P, an optional short edge is unavailable precisely when it is an edge of P or appears in this inverse dictionary. Thus its exact positive union mask is the complement, among the32 short edges, of those two bad masks.

**Complete pair comparison.** `eight_ep0_q4_star_joint.cpp` reads all444 star F inputs. For each center it enumerates all135135 P containing the center edge and all714 additional inverse obstructions. For each of the111 star F with that center, it tests the two short-edge union masks. All
$$4\cdot111\cdot135849=60316956$$
pairs have a nonempty common non-q optional edge; there are zero residual pairs. The producer's result is `eight_ep0_q4_star_joint.json`, with the positive A cycles stored separately for checking. This finite mask comparison completes the distance4 zero-crossing case.

Distinct equal-parity vertices in Q5 have distance2 or4. Steps2--4 exhaust all cuts and both distances, proving Q5 neighbor abundance.

## Deriving EP0

Fix the original eight-hole matching and a cut satisfying the second claim. Set $r=0$ if the root lies in A, otherwise choose either of the two nonroot even holes in A. Choose any perfect matching D on the EP0 completion domain
$$(X_A\setminus\{q\})\cup((Z\cap A)\setminus\{r\}).$$
This domain has even cardinality, and its vertices are disjoint from the internal matching $M_A$. The completed matching $L=M_A\cup D$ has exactly holes $r,q$. The covered target $v\ne q$ has the same parity as q; let $t=L(v)$.

Define
$$K=L-\{vt\}+\{rt\}.$$
The four vertices $r,q,v,t$ are distinct. K is a matching with holes v,q of the same parity, so Q5 abundance applies. At least three neighbors of q occur on its valid thirty-one-cycles omitting v. Since $|N_A(q)\cap S|\ge3$ and q has five neighbors, at least one of these cycles C has an edge $qs$ with $s\in S$.

C contains the required artificial edge rt. Replace rt by $r-v-t$ and delete rv. The result is a Hamilton r--v path on A containing every edge of L. The original edge vt is restored and the artificial edge rt is gone. The inserted edge rv is deleted, so its length is immaterial. All surviving new edges are short.

The edge qs is unchanged: q is a hole of K, and differs from r,v,t. This remains true if s equals r or t. Therefore this path, together with the chosen q,D,s, satisfies exactly the quantified EP0 obligation. No prescribed-edge strengthening of the imported N10 theorem is assumed. Instead that strengthening is derived from the proved abundance theorem.

## Additional local facts and limits

The separate endpoint-path lemma in `eight_ep0_endpoint_path_probe.py` is valid but closes no additional representative by itself: if the only non-S q neighbors are r,a and the chosen completion contains av, avoiding qS forces the entire Hamilton path to be the four-vertex path $r-q-a-v$, a contradiction. Adding these clauses still leaves realizing matchings for the five previously open orbits. Such matching witnesses refute only that sufficient rule, not EP0.

The maximal-short-matching reduction and its exploratory counts are recorded separately; they are not needed for this proof. The abundance proof uses only the finite Q4 inputs and Q5 constructions above.

## Open risks and audit boundary

- A fresh checker must verify the444 star-input list, positive optional unions, complete negative PB inverse dictionary, and all60316956 mask comparisons; semantic review must verify Steps2--4 and the EP0 conversion.
- Q6 geometry must separately establish that a suitable cut and q with three S neighbors always exist. `eight_ep0_three_neighbor_geometry.json` is the root agent's separate geometry input, not assumed silently here.
- The final Q6 path transfer still needs its corresponding T15 cores and the existing audited two-bridge proof.
- This file does not update any global coverage ledger or claim a final eight-hole theorem independently of those remaining imports and audits.
