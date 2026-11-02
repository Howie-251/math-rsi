# Complete original-graph model for an adjacent double defect

Run `dd82-v3-adjacent-doubles61-20261013`. This specification is prepared
before execution; it is not a solver result or an adjacent-double exclusion.
The source theorem is `ADJACENT_DOUBLE_REPEAT_LOCAL.md`, especially (2)–(12)
and section 5. The inherited actual B entry bound is in
`CONNECTED_TRIPLE_EXCLUSION.md`; neither inherited computation is rerun.

## Actual vertices and remaining variables

Use u=0, v=1, s=2, t=3, U=4..8, V=9..13, S=14..19,
T=20..25 and Z=26..60. Put q=14 and p=20. All 1,830 unordered
pairs are original adjacency variables; all 61 vertices have exact degree 8.
For every original pair x,y, retain the direct adjacency and the 59 genuine
conjunctions A_xw AND A_wy, requiring at least one of these 60 literals.
No abstract incidence matrix can replace these actual paths.

Fix the complete neighborhoods of u,v,s,t to the proved core and layers.
The sets U,V,S,T are independent, A[U,V]=0, and A[U/V,S/T]=0.
Every Z vertex has exactly one neighbor in each of U,V,S,T and four in Z.
Every U/V vertex has seven Z neighbors. Every ordinary S/T vertex has six
Z neighbors, while q,p have five. The S/T adjacency matrix K has row/column
degrees (2,1,1,1,1,1); all patterns with those degrees remain variable.

## Compatible labels and complete seven-type coverage

First choose U and V labels independently so the actual weighted matrix
C=B[U,V] equals I+P_sigma for one canonical permutation of each cycle
partition of 5. These seven types cover all nonnegative integral matrices
with every row and column sum two, by the even-cycle decomposition proved
in the source. They impose no automorphism on the original graph.

Use exactly one of seven selector variables. Split Z into five consecutive
groups of seven, one for each U parent. Within group i, allocate consecutive
Z labels to V columns j with cardinalities H_ij=1+C_ij. Thus the U–Z
incidences are unconditional, and all V–Z incidences are conditional on the
selected type. Every actual graph can be so labeled by its actual cells;
the total is 35 and no actual vertex is omitted or duplicated.

Next label the five ordinary S vertices and five ordinary T vertices by
their unique B-unit endpoint in U. These two permutations use only the
still-free S and T labels. They impose B(U_i,S_j)=B(U_i,T_j)=delta_ij,
with B(U_i,q)=B(U_i,p)=0. The corresponding V matchings stay variable.
Do not fix K to a preferred path/matching pattern, or fix q's Z transversal
to an identity permutation. The U/V freedom has already normalized C.

## Necessary count constraints are tied to the same A

For distinct x,y let c_xy=A_xy+sum_w(A_xw AND A_wy)=1+B_xy.
The inherited bound gives 1<=c_xy<=3 on every pair. Additional exact counts
may enforce the four complete B core rows (2),(3), B[U]=B[V]=0,
B[Z,U/V]=0, and the labeled U–S/T units above. They count the same path
variables, not separately guessed B entries. C is already determined by
the actual U/V cell sizes. Other proved port identities may be left to
propagation; omitting a necessary constraint enlarges the encoding and
does not invalidate an UNSAT exclusion. Any additional encoded constraint
must be identified with its actual original-graph proof.

An explicit propagation consequence is useful: write Z_i for the seven
points with U parent U_i. Since N(U_i)={u} union Z_i, A_uz=0 for z in Z,
and B_(U_i,z)=0, the actual codegree equation gives
d_(Z_i)(z)=1-A_(U_i,z). Thus each Z vertex has no neighbor in its own
U group and exactly one in each of the other four groups. The same proof
with V gives the analogous counts in the V groups selected by C. Each
two distinct U groups therefore induce a perfect matching, as do two
distinct V groups. These are redundant necessary counts on existing A
edges; they fix no particular matching and impose no automorphism.

## Complete implication and outcome boundary

Given any order61 target with an edge uv having B_uv=2, its actual core,
partition, C type and three consecutive label choices above produce one
satisfying assignment of this model, including all auxiliary path/count
variables. Therefore a checked UNSAT for the entire seven-selector model,
with the reduction and source checked, excludes every adjacent double.
It does not exclude nonadjacent doubles or order61 itself.

A SAT result must be decoded to all original edges and independently checked
for point count, simplicity, all degrees and all pair distances. A bounded
UNKNOWN proves nothing. The initial existing-solver profile is one attempt
with 50 CPU seconds / 70 wall seconds, 4 GiB address space and 256 MiB per
output file. Only actual RAW_UNSAT triggers a separate exact-input LRAT
check. No unchanged retry or unsupported speedup claim is authorized by
this specification.

## Revised ports and seven selected cases

After the first actual UNKNOWN profile, the revision explicitly enforces
the already proved P=B[S,T] permutation and S/T-to-Z unit-port marginals.
The new `ADJACENT_DOUBLE_PORT_PROPAGATION.md` additionally proves K and P
can overlap only at (q,p) and every S/T parent class is independent in A[Z].
The latter excludes a possible edge by a closed eight-vertex actual B
component; it does not remove the parameter case epsilon=0, eta=1.
All new B bits must be actual thresholds for c_xy=mu+A: with 1<=c_xy<=2,
the threshold c_xy>=2 is exactly B_xy. No independent B assignment is used.

Prepare the revised seven-selector model once, and test its seven selected
cases, rather than also solving the revised monolithic input. One positive
selector unit chooses each case; their exactly-one classification retains
the full domain. Each selected case has one bounded50CPU/70wall profile.
All cases must be covered to transfer a computational exclusion to the
entire adjacent-double branch; any UNKNOWN remains open.

There is a further compatible normalization within each already fixed
(U,V) cell. Order its Z labels lexicographically by their actual pair of
S-parent and T-parent indices, using the fixed orders S=(q,S1,...,S5) and
T=(p,T1,...,T5). Every finite cell admits such an order, with arbitrary ties.
Permuting Z labels independently inside cells preserves both U/V parents,
all core labels, K, and the previously labeled U-to-S/T defect matchings.
Relabel every incident A edge together. All actual degree, path, port and
group constraints are unchanged. Thus every original graph still has a
representative satisfying this order; neither an S/T permutation nor a
q/p transversal identity is being additionally imposed.

For consecutive labels z,z' of one cell, binary parent variables express
this order by forbidding S_i(z) and S_j(z') for i>j, and forbidding
S_i(z), S_i(z'), T_k(z), T_l(z') for k>l. Each vertex already has exactly
one S and one T parent, so these 15+6*15=105 clauses express precisely
nondecreasing lexicographic order. Every H has25 nonempty cells totaling35
vertices, hence10 consecutive cell pairs. Per selected case the added
clauses are its one selector unit and1050 such ordering clauses. This is
a coverage-preserving symmetry reduction, not a claimed measured speedup.
