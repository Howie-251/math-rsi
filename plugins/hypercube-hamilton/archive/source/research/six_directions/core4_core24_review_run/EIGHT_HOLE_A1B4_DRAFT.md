# Eight-hole covered targets: the a=1,b=4 row

Date: 2026-11-01. ARIS proof-writer draft; independent review pending.
The new input T44_5 is proved in T44_Q5_CLOSURE_DRAFT.md and audited PASS
in T44_Q5_CLOSURE_REVIEW.md/.json. Full eight-hole P6 remains open.

## Claim

Let M be a short matching of Q6 with eight holes, u a free even root,
and v a covered odd target. Let Z be the other three even holes and W
the four odd holes. Assume Z union W is independent. Suppose some
coordinate cut has, in the face A containing v, exactly one vertex
z of Z and all four vertices of W. Then M extends to a Hamilton u--v
path. This is precisely the previously bad row (a,b)=(1,4).

Use global parity on both faces. Let B be the other face, let delta be
1 when u belongs to A and 0 otherwise. Let M_A,M_B be internal required
edges, C the original crossing matching, and X_A,X_B its endpoint sets.
Every crossing edge is short, and therefore joins mirror coordinates.

## Inputs

- Q5 K4: arbitrary complete-graph matching with two holes of each parity
  has a Hamilton path from every free root to any opposite-parity target,
  including covered targets. It follows from the already audited A4/N10
  results; see SIX_HOLE_MIXED_AND_GEOMETRY.md and their closure reviews.
- Q5 T44_5: four same-parity holes, avoid any prescribed two, obtain a
  30-cycle containing the matching, with only short new edges.
- Elementary tagged endpoint closure and simultaneous two-conflict path
  compression, detailed below. The corresponding method was audited in
  EIGHT_DOUBLE_BRIDGE_REVIEW.md for the (2,1) row, but the present hole
  counts and parity-reversed conflicts are checked explicitly here.

## 1. Choose the bridges and complete the first face

Choose two distinct holes w1,w2 in W whose B mirrors y1,y2 are not u.
If delta=1 no mirror equals u; if delta=0 at most one of the four mirrors
equals u, so at least three candidates remain. The mirrors are even.
They cannot be other original holes: a nonroot even hole adjacent to a
member of W would contradict independence. They cannot be crossing
ports either: their unique short A neighbor is the original hole wj.
Thus both yj are internally covered by M_B, with distinct odd partners kj.

Since M_A is bipartite, the even-minus-odd port count in A equals the
odd-minus-even ORIGINAL hole count. Hence

    |X_A intersect E| - |X_A intersect O| = 4-(1+delta)=3-delta.

If delta=1, c=|C| is even and at least two. Pair X_A union {w1,w2}
arbitrarily into an artificial matching D and put r=u. The matching
L_A=M_A union D has precisely four holes: u,z even, and the two members
of W other than w1,w2 odd. D is nonempty and avoids r.

If delta=0, c is odd and at least three. Choose any even port r in X_A;
one exists by the displayed surplus. Pair
(X_A minus {r}) union {w1,w2} into D. Now L_A has four holes r,z even
and the other two members of W odd. D is again nonempty and avoids r.

K4 supplies a Hamilton r--v path P_A in A containing L_A. Its other new
edges are short. This invocation permits v to be internally covered or
to be a port covered by D; r is even, so r != v.

## 2. Transfer all original crossings and both bridges

Delete D from P_A, attach every original crossing edge, and add the
two short bridges wj-yj. Every added B attachment is at a distinct vertex:
the ports X_B, y1,y2 are disjoint. Therefore the result is a path forest.

All A vertices now have degree two except the global endpoints lying in A.
For delta=1, r=u keeps degree one. For delta=0, r is a crossing port and
its original crossing restores its degree to two. The holes wj were
covered by D; removing their D edge reduces degree by one and their new
bridges restore it. Other ports lose a D edge and gain a crossing edge.
If v is a port, its sole path edge belongs to D: deletion temporarily
isolates v, and its original crossing restores degree one. If v is
internally matched, its endpoint degree was unchanged.

For delta=1 the nonempty D separates u and v into different path
components, giving two distinct terminal segments to B. For delta=0
there is one terminal segment from v to B and u is an original free B
vertex. Temporarily add a tagged artificial edge uv. In the former
case it joins the two terminal segments into a B-to-B path; in the latter
it extends the terminal segment to the distinct B endpoint u. It creates
no cycle at this stage. Compress all resulting B-to-B paths into a
matching T, recording each expansion and the unique edge carrying the tag.

For delta=1 the endpoint set of T is X_B union Y; for delta=0 it is
X_B union Y union {u}, where Y={y1,y2}. Every A vertex occurs once in
the interiors of these transferred paths. The only overlap between
vertices covered by T and M_B is Y.

## 3. Suppress the two conflicts and invoke T44_5

Each yj has the original M_B edge yj-kj, with kj odd. The kj are distinct,
internally covered, and outside the endpoint set of T. In particular no
original matching edge joins y1 and y2, since both are even.

In M_B union T, the only degree-two vertices are y1,y2. Every component
meeting Y is a path: its original matching edge reaches a degree-one
vertex kj. If T joins y1,y2, the component is k1-y1-y2-k2; otherwise
there are two distinct paths. Suppress Y along these paths to produce
a matching L of K(B), retaining all expansion data and the tag.

If delta=1, the original B holes are the two even members of Z outside A.
After the port transfer and suppression, L has precisely those two holes
together with y1,y2, hence four even holes.

If delta=0, the original B holes are u and the two even members of Z
outside A. The tagged closure consumes u, while suppression exposes
y1,y2. The final four holes are again
(Z minus {z}) union {y1,y2}, all even.

Apply T44_5 to L, avoiding exactly y1,y2. It gives a single 30-vertex
circle in B minus Y containing all required compressed edges. Undo every
suppression and path compression. This restores both avoided bridge
vertices and all 32 A vertices, each once, to give a single 64-vertex
circle containing every original edge of M and the tagged uv edge.
Delete the tagged edge to get the desired Hamilton u--v path.

Every surviving edge outside M is either a local short edge supplied
by K4/T44_5 or one of the two short bridges. All artificial D edges were
deleted; all compressed edges were expanded; the possibly long tag uv
was removed. This proves the claimed row for every original matching.

## Scope and geometric accounting

For the earlier R8-covered domain, all its 66127 normalized hole
geometries are listed in covered_eight_residual_1/7/31.bin. Of these,
24669 have at least one (1,4) cut: 7535,8319,8815 for the three targets.
The new row therefore closes every realizing matching for those geometries.
The remaining geometry counts are 11995,14153,15310, totaling 41458.
Of these 41408 have an a2b1 cut, while 50 have none (the previously
identified seven exceptional orbits). These are hole-geometry counts,
not counts of matchings or a claim that every geometry is realizable.

The remaining (2,1) route still needs nonadjacent Q5 T15, and the last
50 geometries still need another argument such as a proved EP0 cut
selection. Full eight-hole P6, the higher layers, and full P6 remain open.
