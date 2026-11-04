# Independent audit: six-hole closure and general Q4 augmentation

Date: 2026-11-01. Requested reviewer: GPT-6.1-sol, high reasoning.
Verdict: **PASS modulo the explicitly imported prior results**.
Review independence: same-family; semantic acceptance: provisional.

Reviewed in full: `SIX_HOLE_CLOSED.md` and
`Q4_GENERAL_AUGMENTATION.md`. No changes to the earlier proofs or audits
were needed. No new eight-hole or full P6 claim is accepted here.

## Six-hole theorem and augmentation corollary

The six-hole theorem has exactly the hypotheses of the previously proved
C6-free and C6-covered results: a short Q6 matching with six holes, any
free root, and any opposite-parity target. A target is either free or
covered, so the two cases exhaust the domain. Their previously remaining
A4 hypothesis is discharged by `CANONICAL_A4_CLOSURE.md` and its independent
finite and semantic audit. Neither six-hole theorem is an input to the
A4 proof, so there is no dependency cycle. Original long auxiliary edges
in the proofs are not being mistaken for short matching inputs.

The augmentation corollary is valid. An augmented short matching that
leaves the root free has at most 31 edges, since 32 edges would cover
every vertex. At least 29 edges therefore means exactly 29,30,31 edges,
or exactly 6,4,2 holes. The established endpoint theorem at that hole
level applies to the same root and target. The target may have become
covered during augmentation; all three endpoint theorems allow that.
The resulting path contains the augmented matching and hence the
original matching. Every edge on it is short. This does not assert that
such an augmentation always reaches 29 edges.

The 18-hole root-preserving maximal bound is an explicit imported range
result from `ROOTED_MAXIMAL_18_HOLES.md`. Closing the 2-,4-,6-hole levels
leaves the 8,10,12,14,16,18-hole levels as listed. No inference closes them.

## General Q4 results

For two distinct same-parity Q4 vertices their distance is 2 or 4. At
distance 2 their neighbor sets intersect in exactly two vertices; at
distance 4 they have no common neighbor. Thus their neighbor union has
size 6 or 8. The opposite class has size 8, so at most two vertices of
that class are outside the union. Any three vertices of that class
therefore include a neighbor of the chosen pair. This uses no matching
extension theorem or assumption about required long edges.

GQ4-avoid is a finite induction on m. For m=0 the holes are the two
same-parity vertices required by N14_4. For m=1 the hole counts are 1,3,
as required by A4_4, and the forbidden vertex is in the larger class.
For m>=2, select two free smaller-class vertices and three free
larger-class vertices excluding the forbidden vertex v. There are enough
of the latter because m+2-1=m+1>=3. The geometric fact gives a short
edge between these sets. Both endpoints are free and neither is v, so
adding the edge is a legal matching augmentation, preserves the required
forbidden hole, and reduces both class counts by one. The induction
parameter decreases strictly to a base. Edges added in the induction
are short, so the final circle meets the original extension requirements.
No bipartite restriction was imposed on the original matching.

GQ4-path is likewise correct. A free root implies at least one hole in
its parity class; the balanced zero-hole case has no such root and
creates no omitted path case. At m=1, the other free hole has opposite
parity from the root, so any prescribed opposite target has precisely
the target parity required by N10_4. At m=2, K4_4 applies to a balanced
four-hole arbitrary matching and allows covered targets. At m>=3,
there are at least two root-parity free vertices other than the root,
and at least three opposite-parity free vertices. Adding the supplied
short edge preserves the root and reduces m by one. The target can
become covered; the induction statement and both bases allow this.
Thus the quantifiers remain unchanged during induction.

GQ4-cycle at zero holes imports Fink's arbitrary perfect-matching circle
theorem. With holes, choose a free root and any short neighbor as target
in GQ4-path. Their edge is short and cannot already occur in a simple
16-vertex path with those endpoints, so adding it creates one simple
Hamilton circle. All original matching edges are retained and all edges
outside the original matching are short. The three Q4 proofs use their
earlier Q4 inputs only, without depending on Q5 A4 or Q6 P6.

## Independent finite checks and counterexample pass

A fresh read-only standard-library check verified all 56 unordered
same-parity vertex pairs: 48 have neighbor-union size 6 and eight have
size 8. All 3136 choices of such a pair and an opposite-class triple
contain a short edge. This confirms the small geometric calculation;
the preceding argument supplies its proof.

The 52 optional canonical construction certificates were also checked
directly, without importing the constructor. All specified matchings
have holes {0,1,14,22}; every supplied global circle contains all 28
required matching endpoints, has exactly the 31 vertices other than 1,
and uses only short edges outside the required matching. The modes are
28 fixed-free-target, eight safe-flexible-target, and 16 occupied-target
prescribed-root cases. The latter satisfy the actual crossing-partner
root condition, y in X_B, y outside X_A, and nonempty D. All auxiliary
D edges occur in the supplied A path. The four reported isolated A
endpoint cases are independently confirmed by y being covered by D.
These are individual witnesses and are not used for universal closure.

Adversarial boundary checks covered: an augmentation that covers the
target; the impossible 32-edge augmentation with a free root; m=2 in
the avoid induction with exactly three permissible majority holes;
m=3 in the path induction with exactly two non-root same-parity holes;
the vacuous zero-hole path case; and a possible duplicate closing edge.
All are handled by the stated hypotheses and proofs. There are no open
issues in these consequences. Full P6 remains unproved.
