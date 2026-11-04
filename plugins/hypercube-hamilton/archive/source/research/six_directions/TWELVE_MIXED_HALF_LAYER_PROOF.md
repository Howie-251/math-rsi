# Exact ordinary mixed-omission classification from a deficient-rank certificate

2026-11-02. ARIS proof-writer candidate, independent verification pending.

## Exact claim

Let H={0,1,3,31}, U={0,31}, K=V(Q5) minus H, and

R={4-6,8-10,13-15,16-18,21-23,25-27,28-30}.

For every perfect matching F of the COMPLETE graph on K, there exists
a simple cycle on V(Q5) minus U containing F and adding only cube edges
if and only if R is not a subset of F. Required F edges may be long or
same-parity. The theorem transports under common cube automorphisms of
all marked data. It is an ORDINARY cycle theorem, with no prescribed
additional edge3-7 or other opening edge.

## Necessity: the exact half-layer deficit

Split Q5 by mask2 into A={x:x&2=0} and its other face. The odd half-layer
in this direction consists of all short edges x-(x xor2) for odd x in A.
Its eight edges are R together with1-3. The omitted vertices0 and31
belong to the other, even half-layer and do not remove these eight edges.

Suppose a desired cycle C exists and R is contained in F. Delete its
required F edges; the remaining S consists solely of short edges,
degree one at every K vertex and degree two at1,3. Omitted0,31 have
degree zero. In A, the seven retained even vertices have total S-degree7,
while the eight odd vertices have total S-degree9 (vertex1 contributes2).
Internal short edges contribute equally to these two degree sums.
Consequently the number of S crossing edges from odd A to even B minus
the number from even A to odd B equals2. But all odd-half-layer edges
except1-3 are already in F and cannot also occur in S. Thus the first
number is at most1, an impossibility. This argument uses positive degree
counts and does not depend on a failed search or on F being bipartite.

## The fixed-R bad-column space has dimension64

Let H_K denote the full binary matching-connectivity matrix on all
perfect matchings of K, where one means that the labelled union is a
single alternating cycle. Its GF(2) rank is8192, by the general
Cygan--Kratsch--Nederlof Corollary3.5 at28 endpoints. Put B equal to the
set of matching columns G containing all seven edges of R. The matrix
H_K restricted to columns B has rank64.

To prove this last assertion, set L=K minus V(R), so |L|=14, and write
G=R union G', where G' is an arbitrary perfect matching of L. For any
row P, the labelled graph P+R is a disjoint union of alternating cycles
and paths. If it has a cycle then that component persists for every G',
so the restricted row is zero (L is nonempty). Otherwise all components
are paths with endpoints exactly L. Compress their R vertices to obtain
a perfect matching P' of L. For every G', connectivity of P+G is
equivalent to connectivity of P'+G'. Thus every nonzero restricted row
is a row of H_L.

Conversely, every perfect matching P' of L is realizable this way:
choose any one of its edges a-b, replace it by a path traversing the
seven R edges in any order and orientation, and let its eight intervening
edges belong to P; keep all other P' edges in P. This is a perfect
matching of K and P+R has exactly the desired compressed pairing P'.
The restricted matrix therefore has exactly the row space of H_L, whose
GF(2) rank is2^(14/2-1)=64 by the same general theorem.

## Sufficiency: span the kernel instead of the entire row space

Let V be the8192-dimensional row space of H_K, and let A be the kernel
of restricting a row vector in V to the columns B. The preceding
paragraph shows dim(A)=8192-64=8128.

The certificate supplies8128 short forests S_i on V(Q5) minus U, degree
one at K and degree two at1,3, with no cycle. Their endpoint pairings
P_i are perfect matchings of K. By the necessity argument each complete
row H_K[P_i,:] vanishes on every column in B. All these rows lie in A.
Their supplied8128-by8192 connectivity submatrix has exact GF(2) rank8128.
Consequently these complete rows form a basis of A.

Now let F not contain R. Choose an edge e in R minus F. Its endpoints
belong to different F edges. There is a perfect matching P of K that
contains e and whose union with F is a single alternating cycle:
order and orient the fourteen F edges cyclically so that the two F edges
incident to e are consecutive with e joining their exposed ends; join
the remaining consecutive ends to complete P. Every G containing R
shares e with P, giving an isolated labelled two-edge component, so
H_K[P,G]=0 for all G in B. Thus H_K[P,:] belongs to A, yet its entry at
F equals1. Since the selected forest rows span A, some one of those
rows has entry1 at F.

Expand that forest's endpoint paths to obtain the desired thirty-vertex
cycle. Interiors are the two included holes. A physical F edge cannot
be duplicated by the forest: a common endpoint pair would already form
an isolated labelled two-edge component, contradicting connectedness on
28 endpoints. All newly added physical edges are short. This proves
sufficiency and the exact classification.

## Frozen finite certificate obligations

Prefix `TWELVE_ROOT_STAR_MIXED_probe` has:

- `_forests.bin`: 8128 records of32 bytes (sixteen short edge pairs).
- `_pairs.bin`: 8128 records of28 bytes (fourteen endpoint pairs).
- `_columns.bin`: 8192 records of28 bytes (arbitrary perfect matchings).
- `_matrix.bin`: 8128 records of1024 bytes, little-bit-first.
- `_pivots.bin`, `_combos.bin`: 8192 records of1024 bytes. There are8128
  nonzero pivots; combo bits refer only to the8128 original rows.
- `_config.txt`, `.json`, source and preparation script.

The independent checker must reconstruct all forests/pairings and all
66,584,576 connectivity bits, then verify exact rank8128. The search's
exhaustiveness is NOT used. Any8128 legal independent rows suffice,
because necessity and the analytic rank64 computation give the matching
upper bound. The producer's count85452 examined forests is diagnostic.

The only external mathematical import is the general matching-connectivity
rank formula recorded in `A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`,
arXiv1211.1506 / DOI10.1145/3148227. A related half-layer classification
for bipartite perfect matchings with two faulty vertices appears in
[Gregor--Novotny--Skrekovski2018](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i2p56/pdf/),
Theorem3; it motivated the obstruction search but is not a premise of
the proof above.

## Boundary

This theorem does NOT guarantee a usable opening edge q-t. The separate
force-edge3-7 search produced rank8031 and establishes no classification
by itself. The actual root-star Q6 transfer still needs a suitable opening
edge or another construction. Full twelve-hole and full P6 remain OPEN.
