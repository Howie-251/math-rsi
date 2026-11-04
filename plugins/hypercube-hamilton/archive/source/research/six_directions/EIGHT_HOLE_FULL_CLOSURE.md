# Complete eight-hole P6: proof assembly

2026-11-01. ARIS proof-writer. This is the full eight-hole proof assembly.
It requires the final independent reviews of all listed imports and of this
assembly before the main ledger may mark the eight-hole layer closed.
It makes no assertion about the ten-through-eighteen-hole layers or full P6.

## Exact theorem

Let Q6 be the graph on binary labels0,...,63, with short edges joining labels
of Hamming distance1. For every matching M consisting of28 short edges,
every uncovered vertex u, and every vertex v of parity opposite to u,
there is a Hamilton u-v path containing all28 edges of M. There is no
restriction that v be uncovered.

The proof is computer-assisted. Finite cases below have explicit positive
certificates or complete, separately implemented finite classifications.
Semantic review has the project's stated same-family/provisional assurance,
relative to explicitly imported published and previously audited theorems.

## Explicit dependency ledger

1. The complete two-, four- and six-hole P6 cases, including covered targets.
   In particular use `SIX_HOLE_CLOSED.md` and its cited A4 audit.
2. Full Q5 A6 and the complete eight-hole free-target branch, together with
   the nine good covered-target cut types. Their closed scope is recorded
   in `A6_AND_EIGHT_FREE_CLOSED.md`; the proofs and reviews are
   `A6_CLOSURE_DRAFT.md`, `A6_CLOSURE_REVIEW.md/.json`, and
   `EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW.md/.json`.
3. The complete covered-target geometry reduction, the T15 transfer for
   a (2,1) cut, and the EP0-dependent transfer for a (2,0) cut. Use
   `EIGHT_HOLE_COVERED_NEXT_DRAFT.md` and its retained independent review.
4. The accepted T44, singleton-avoided-face and balanced-bridge core
   reductions. In particular the fixed independently reconstructed base
   `eight_after_balanced_bridge_candidates.json`, with its audit
   `T15_BALANCED_BRIDGE_CONSEQUENCES_REVIEW.md/.json`, leaves exactly21350
   normalized geometries:21300 with a (2,1) projection and50 without one.
5. The full arbitrary-K(Q5)-matching marked T15 cores listed in the final
   finite manifest. Each has an independent whole-core review. Only the
   explicitly used marked geometries are imported; full T15 is unnecessary.
6. `Q5_NEIGHBOR_ABUNDANCE_AND_EP0.md`: the new Q5 included-free-hole
   neighbor-abundance theorem, relative to its complete Q4 neighbor,
   perfect-matching endpoint and star-family finite checks. Its independent
   review must be accepted before this assembly is accepted.
7. The independent all-EP0 geometry/projection review, including the exact
   fifty normalized images and all234 possible selected-edge projections.

All original Q6 matching edges are short. The intermediate Q5 matchings
may contain long and same-parity auxiliary edges. Imports5--6 apply to
arbitrary complete-graph matchings, so this change of scope is explicit.

## Step1. Standard normalization and root-preserving augmentation

Translate labels to put u=0. Translation preserves graph adjacency and
matching containment; global parity may reverse, which does not affect
the argument. The root is now even and v is odd. Because M is short and
has28 edges, its holes consist of four even and four odd vertices. Write
the even holes as {0} union Z, |Z|=3, and the odd holes as W, |W|=4.

If v is free, the already proved full eight-hole free-target branch applies.
Assume henceforth that v is covered. If there is a short edge between a
vertex of Z and a vertex of W, add it to M. This keeps0 free and gives a
six-hole matching; its already proved full endpoint theorem produces a
path containing the augmented matching, hence M. Thus assume Z union W
is independent. This does not require0 to be nonadjacent to W.

A coordinate permutation normalizes v to1,7 or31 according to its odd
Hamming weight1,3 or5. Every choice of the original matching remains
quantified after this normalization.

## Step2. Previously audited geometry coverage

The nine good cut types and subsequent T44/core reductions close the
previously recorded classes. The audited fixed base has21350 remaining
marked hole geometries. Its core_choices entry for a row is obtained by
an actual coordinate cut, translation and five-coordinate projection,
preserving the roles of the two specified omitted holes.

For each of its21300 rows with a nonempty core_choices list, the final
coverage checker finds a choice whose complete arbitrary-matching T15
theorem has an accepted independent review. The (2,1) transfer therefore
solves every realizing original short matching of that geometry, not just
one sample. The arbitrary auxiliary matching and crossing bijection are
within the imported core theorem's scope.

This accounts for all rows with a (2,1) projection. The other50 rows form
seven target-preserving coordinate orbits. Steps3--5 handle all of them.

## Step3. A sufficient EP0 rule from three available neighbors

Fix a (2,0) cut for one of the seven representatives. Let A contain v,
let B be the other face, and write Z intersection A={z1,z2}. Put
S={w xor 2^i : w in W}, the four even mirrors of B's odd holes. Choose
r=0 when0 lies in A; otherwise choose either z1 or z2 as r.

Suppose an odd original crossing port q in A satisfies q!=v and
|N_A(q) intersection S|>=3. Choose any perfect auxiliary pairing D on

    (X_A minus {q}) union ({z1,z2} minus {r}).

When r=0 and0 is not a member of {z1,z2}, both z1,z2 remain in this set.
The set is even: A has three original even holes when0 is in A and two
when it is not, so c is respectively odd or even. Its union with the
internal matching M_A is a matching L with exactly the holes r,q.

Since q!=v, the target v is covered by L. Let t=L(v) and replace vt by rt:

    L1 = L minus {vt} plus {rt}.

This is a matching with the two odd holes v,q. The new Q5 neighbor theorem
provides at least three distinct short neighbors of q that occur, across
the family of31-cycles omitting v and containing L1. The neighborhood of
q in Q5 has size5. Since at least three of these neighbors belong to S,
some such cycle C contains qs with s in S. The assertion is about a union
over cycles; it does not claim one cycle has three incident edges at q.

Replace the required edge rt of C by r-v-t and delete the artificial rv
edge. This produces a Hamilton r-v path P on A containing L. The old
required edge vt has been restored. All surviving edges outside L are
short. The edge qs survives: q is a hole of L1 and differs from r,v,t,
so qs is not rt or rv. Consequently P satisfies EP0 exactly as quantified
in the previously audited (2,0) transfer.

This works for any fixed D; the cycle and the selected neighbor s may
depend on D and the original matching. No particular optional neighbor
is prescribed in advance.

## Step4. Every realizing matching has a sufficient cut and port

`eight_ep0_three_neighbor_geometry.py` constructs every sufficient
crossing edge in each of the seven representatives directly from cube
bit flips, using q!=v and the three-neighbor condition of Step3. Remove
all of these crossing edges from the short-edge graph on covered vertices.
The following covered even vertices become isolated (one per row suffices):

| v | Z | W | One isolated covered even vertex |
|---|---|---|---:|
|1|3,5,9|14,31,47,62|15|
|7|3,5,6|8,16,32,56|24|
|7|3,5,15|8,25,41,56|9|
|7|3,15,23|25,26,56,59|24|
|7|15,23,39|56,59,61,62|57|
|31|15,23,27|1,2,32,35|3|
|31|15,23,63|32,35,37,38|33|

An original matching covers every vertex outside its stated holes. It
must therefore use one of the removed sufficient edges to cover the
listed vertex. This selects a cut and q satisfying Step3. The chosen
cut is allowed to depend on the actual original matching. The argument
does not assert EP0 for every arbitrarily fixed cut.

The seven orbit sizes are10,1,9,9,1,10,10, summing to50. Coordinate
permutations preserving each normalized target transport every matching,
selected cut, neighbor condition and constructed path. The independent
consequence check reconstructs the images and compares their union with
the exact50 no-(2,1) base rows.

## Step5. Every resulting T15 instance is already covered

For each sufficient q and every possible s in S intersection N_A(q),
the existing EP0 transfer consumes the odd B hole t=s xor 2^i. Its two
marked avoided B vertices are the mirrors of z1,z2. The minority hole
is the remaining member of Z in B; the retained majority holes are
W minus {t}.

`eight_ep0_three_neighbor_projection.py` performs the original-coordinate
translation and projection for every such choice, then checks the marked
core under all five-coordinate permutations. There are234 choices:
174 project to core4 and60 to core1. Thus **every** possible edge qs
obtained by Step3 leads to an accepted core, not just a favorable choice
that the path theorem might fail to provide.

The audited (2,0) transfer now supplies the Hamilton0-v path through M.
That transfer attaches all original short crossings, records the tagged
endpoint closure, suppresses its two conflicting bridge mirrors, applies
the appropriate30-cycle T15 theorem and expands every recorded path.
Deleting the tag restores the desired endpoints. Its proof explicitly
covers root and target positions, retains every original edge and removes
all auxiliary edges. Hence all50 exceptional geometries are solved.

## Conclusion and scope

Steps1--5 cover every short28-edge matching, every free root, and every
opposite-parity target, proving the stated complete eight-hole theorem
relative to the listed accepted imports and finite checks.

No inference from "exactly18 holes" to "eight holes" is used. No full
T15 assertion is needed. Ten-, twelve-, fourteen-, sixteen- and eighteen-
hole layers remain outside this theorem; full P6 remains an active goal.
