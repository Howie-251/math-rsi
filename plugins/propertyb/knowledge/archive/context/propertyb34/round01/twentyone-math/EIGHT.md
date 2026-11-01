# Twenty-one vertices of minimum degree eight

2026-10-13. Complete paper candidate, not yet Lean. H is simple, pair-covering and five-uniform on 21 vertices, has exactly 34 edges, and has minimum degree eight. We prove Property B by local exact probability bounds and an actual unit-codegree graph contradiction.

Let L be the degree-eight set. The degree sum is 170, only two above $21\cdot8=168$, so |L|≥19 and there are at most two vertices outside L. Write λ for pair codegree and τ for common-three multiplicity.

## 1. Codegrees inside L are one or two

Exact two-lock bounds, with all positions available, are strict whenever an L-pair has codegree at least four. For example the codegree-four profile has bound 4060/4199 with lock positions (10,21). These witnesses cover all possible codegrees four through eight. Hence we may assume every L-pair has codegree at most three.

The full (8,8,8) domain with pair codegrees in {1,2,3} has 63 profiles. Thirty-eight have strict single-layout witnesses and three more have strict mixed-layout certificates. In every retained profile containing a codegree-three pair, the common-three multiplicity is zero: its sorted pair-codegree vector is (1,1,3), (2,2,3) or (3,3,3), always with τ=0.

If x,y∈L had codegree three, no edge containing them could contain a third L point. But such an edge has three other distinct vertices and only two vertices lie outside L. This is impossible. Thus all L-pair codegrees are in {1,2}.

Both (1,1,1) triple profiles are strict, so the graph G on L, with x-y an edge precisely when λ(x,y)=1, is triangle-free.

## 2. Minimum degree and the four-point residues

For x∈L,

$$\sum_{v\ne x}(\lambda(x,v)-1)=4\cdot8-20=12.$$

At most twelve of the other vertices are nonunit neighbors. Therefore x has at least $|L|-1-12\geq6$ neighbors in G. Thus G has minimum degree at least six.

The four-eight-point domain with pair codegrees in {1,2} and triangle-free unit graph has 490 profiles. Of these, 356 are strict single-layout cases and 24 more have strict mixed-layout certificates. The 110 labelled residues have only the following graph shapes:

$$K_{1,3},\quad C_4,\quad P_4,\quad K_2\sqcup2K_1,\quad\overline{K_4}.$$

In particular an induced three-vertex path plus an isolated vertex is forbidden. Every C4 residue has common-four multiplicity one. A claw residue with positive common-four multiplicity has that multiplicity one and exactly one additional exact triple consisting of its three leaves. The claw with common-four one and no extra leaf triple is already a strict four-lock case.

## 3. Eliminate the last claw with a common edge

Suppose x,a,b,c induce a claw in G and lie in an edge e. Their common-four multiplicity is one, because each center-leaf codegree is one. By Section 2, unless an earlier strict witness already applies, there is also exactly one edge f containing a,b,c and not x. Since the leaf-pair codegrees are two, these two edges exhaust the common occurrences of each leaf pair.

The center x has at least six G-neighbors. Its edge e contains at most four other vertices, so choose a G-neighbor w outside e. Triangle-freeness implies all pairs among a,b,c,w have codegree two. Unit codegrees to x imply the unique x-edge through any of a,b,c is e, while the unique x-edge through w is different.

For locks (x,a,b,c,w), the exact trace of e is {x,a,b,c}. The trace of f is either {a,b,c} or {a,b,c,w}. No other trace of size at least three is possible: every leaf pair in {a,b,c} is already saturated by e,f, and x cannot share an edge with w and any of a,b,c. There are exactly two complete profiles. One has a strict single-layout bound 99/104; the other has a strict mixed-layout certificate

$$28464999941/28599997140<1.$$

Hence any common edge on a claw's four vertices yields a coloring. From now on every induced claw of G has common-four multiplicity zero.

## 4. No pair has three common neighbors

Suppose p,q have three distinct common G-neighbors a,b,c. Triangle-freeness implies p,q are nonadjacent and a,b,c are pairwise nonadjacent. The four-sets {p,q,a,b} and {p,q,a,c} are induced C4s. By Section 2 each is contained in a hyperedge, say e1 and e2.

Both hyperedges contain the unit pair p,a, so e1=e2. This common five-element edge contains p,q,a,b,c. In particular it contains the four vertices p,a,b,c, which induce a claw. This contradicts Section 3. Therefore any two vertices of G have at most two common neighbors.

## 5. The graph contradiction

Choose any vertex x of G and let d=deg_G(x)≥6. If z lies outside its closed neighborhood, take any two distinct neighbors a,b of x. They are nonadjacent because G is triangle-free. If z were adjacent to neither, the induced four-set {x,a,b,z} would be a path of length two plus an isolated point, forbidden by Section 2. Thus z misses at most one neighbor of x, giving at least d−1≥5 common neighbors of x,z, contrary to Section 4.

Consequently x is adjacent to every other vertex. Triangle-freeness then makes all those other vertices pairwise nonadjacent, so each has degree one. This contradicts the minimum degree six. The contradiction proves that an earlier strict probability witness must apply, and H has Property B.

## 6. Exact evidence and formalization boundary

`EIGHT_DOUBLES.json`, `EIGHT_TRIPLES.json`, `FOUR_EIGHTS.json` and `EIGHT_STAR_LARGE_EDGE.json` contain the stated local domains and witnesses. `FOUR_EIGHTS_RESIDUES.json` records all 110 remaining labels in eighteen permutation orbits, including the last claw family removed in Section 3.

`EIGHT_WITNESSES_VERIFIED.json` records 400 strict single-layout rows independently checked by labelled-injection A/B/C, exact quota/capacity arithmetic, actual selected degrees and 34-edge totals. The three `_STRICT_JOINT_VERIFIED.json` files for `EIGHT_TRIPLES`, `FOUR_EIGHTS` and `EIGHT_STAR_LARGE_EDGE` record 3+24+1 independently checked mixed-layout certificates. The actual run log is `verify_eight.log`.

The classifications are finite local trace domains; the structural argument applies them to every actual selected set. They are not a complete-hypergraph enumeration. Lean still needs to prove their coverage, transport exact actual trace multiplicities, connect bad-pair quotas and probability bounds, and assemble the branch. Cross-model review should particularly attack the codegree-three exclusion, the two-profile claw extension and the unit-pair uniqueness argument joining the two C4 edges.
