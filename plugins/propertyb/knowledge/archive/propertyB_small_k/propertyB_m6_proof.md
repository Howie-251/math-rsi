# A computer-assisted proof that m(6) >= 65

**Theorem.** Every finite simple 6-uniform hypergraph with at most 64 edges admits a 2-coloring with no monochromatic edge.

**Certificate:** `propertyB_m6_certificate.py`, a pure Python 3 standard-library program. All arithmetic used for the final comparisons is exact `fractions.Fraction`, not floating point.

## 1. Reduction

Suppose the theorem is false and choose a counterexample with the minimum number of vertices. If two vertices are not in a common edge, identify them; the image is still 6-uniform, still non-2-colorable and has no more edges. Thus all pairs occur in some edge. Write `v=|V|`, `m=|E|<=64`, `d(x)=#edges containing x`, and `lambda_xy=#edges containing {x,y}`. Then

`5 d(x) = sum_{y != x} lambda_xy >= v-1`, `sum_x d(x) = 6m <= 384`.

Consequently `v ceil((v-1)/5) <=384`, giving `v<=42`. A uniform balanced 2-coloring makes any one edge monochromatic with probability

`p(v)=[C(floor(v/2),6)+C(ceil(v/2),6)]/C(v,6)`.

For `11<=v<=26`, `64 p(v)<1` (its maximum is `768/805` at `v=25,26`); `v<=10` is trivially 2-colorable. Thus `27<=v<=42`. Since `C(v,6)>=64`, adding distinct edges up to 64 preserves pair coverage and non-colorability. Hence we may take `m=64`.

## 2. Greedy algorithm and its critical-pair bound

Fix distinct locked vertices and distinct positions, then uniformly permute the remaining vertices. Initially all vertices are red. When a vertex is processed, change it to blue iff it is the last vertex in a still-all-red edge. No edge is finally red. If a blue edge B exists, let x be its first vertex; when x turned blue an all-red edge A ended at x, so A and B meet exactly at x, and A ends where B begins.

Let locked vertices have indices 0,...,s-1 and positions t_i. Let `ell_T` be the number of edges meeting the locked set in exactly the mask T; `r_T=6-|T|`, `N=v-s`. At position h, let a,b be the number of free slots before/after h, and I^-,I^+ the lock indices before/after h.

For a free h, the probability that a T-edge ends there is

`(r_T/N) C(a,r_T-1)/C(N-1,r_T-1)` if all its locks are before h, and zero otherwise. The analogous start probability replaces a by b and before by after. For h=t_j locked, a T-edge can end only if it contains j and all other locks are before h; its probability is `C(a,r_T)/C(N,r_T)`, and analogously for start.

For a *fixed single-intersection ordered pair* of types T,U, the probability its common vertex is the end of A/start of B at free position h is

`w_h(T,U)=C(a,r_T-1) C(b,r_U-1)/[N C(N-1,r_T-1) C(N-r_T,r_U-1)]`

when locked positions and capacities permit, and zero otherwise. At locked position h=t_j it is

`w_h(T,U)=C(a,r_T) C(b,r_U)/[C(N,r_T) C(N-r_T,r_U)]`

when `T intersect U={j}`, all other locks of T are before h, all others of U are after h, and capacities permit; otherwise zero.

Let A_h and B_h be sums of the edge-end and edge-start probabilities, and

`C_h=sum_{T,U} ell_T (ell_U - indicator[T=U]) w_h(T,U)`.

This is an upper bound on the union of all critical-pair events at h, since it counts all distinct ordered pairs of the given types, including some non-single-intersecting pairs, which may be overcounted with a nonnegative bookkeeping weight. Therefore the failure probability is at most `sum_h min(A_h,B_h,C_h)`.

## 3. Valid deletion of necessarily bad overlapping link pairs

Fix a locked vertex x_j. Let q(x_j) be the number of *unordered* pairs of distinct edges both containing x_j and meeting in another vertex. The link edges are distinct 5-sets covering the other v-1 vertices. Therefore

`sum_{y != x_j} C(lambda_{x_j y},2) >= 5d(x_j)-(v-1)`.

Each distinct link-edge pair meets in at most four vertices. Hence

`q(x_j) >= q_j:=ceil([5d(x_j)-(v-1)]/4)`.

An unordered pair of types {T,U}, both containing j, has weight

`delta_h(T,U)=w_h(T,U)+w_h(U,T)`

in C_h. Its multiplicity among all unordered pairs is `C(ell_T,2)` if T=U and `ell_T ell_U` otherwise. Arrange this multiset of weights in nondecreasing order. Let D_h be the sum of its q_j smallest elements. Any selection of at least q_j genuinely overlapping link pairs has total weight at least D_h. These pairs cannot be single-intersection critical pairs, and their two directions are separately present as bookkeeping terms in C_h. Consequently

`P(failure) <= U:=sum_h min(A_h,B_h,C_h-D_h)`

where D_h=0 for free h. This definition automatically allows zero-weight bad pairs; it never assumes all bad pairs have positive weight.

## 4. Four exhaustive types of locking certificates

**(a) No locks, v=27,...,33.** Let Q be the number of distinct unordered edge pairs with intersection size at least two. By pair coverage,

`sum_{A<B} C(|A cap B|,2) = sum_{x<y} C(lambda_xy,2) >= 64 C(6,2)-C(v,2)`.

Two distinct six-edges meet in at most five vertices, so

`Q >= ceil([960-C(v,2)]/10)`.

The total number of ordered single-intersection pairs is therefore at most `gamma=64*63-2Q`. Because unconditioned ordered single-intersection pairs have equal weights at any position, use `gamma*w_h` in place of C_h. This gives U<1 for every v=27,...,33.

**(b) One lock, v=34, and v=35,36 when the minimum degree <=9.** Pick a minimum-degree vertex x and lock it at position floor(v/2). Its degree obeys `ceil((v-1)/5)<=d(x)<=floor(384/v)`. For v=34, check d=7,...,11. For v=35,36, check d=7,8,9.

**(c) Two locks, remaining v=35,36, and all v=37.** For v=35,36 where single-lock was not used, a minimum degree vertex x must have degree 10. Set `e=5d(x)-(v-1)`; at most e other vertices have codegree >=2 with x. If every y with lambda_xy=1 had degree >=14, then total degree would be at least `d+(v-1-e)*14+e*d>384`; contradiction. So there exists y with lambda_xy=1 and `10<=d(y)<=13`. For v=37, the minimum degree d lies in {8,9,10}. If every y with lambda_xy=1 had degree >=13, then the total degree would be at least `d+(36-e)*13+e*d>384`; contradiction. Hence choose y with lambda_xy=1 and `d<=d(y)<=12`. Lock x,y at positions floor(v/2),floor(v/2)+1. With lambda_xy=1 the types have multiplicities

`ell_empty=65-d(x)-d(y), ell_x=d(x)-1, ell_y=d(y)-1, ell_xy=1`.

All 4+4+12 profiles are checked with the weighted link deletions.

**(d) Three locks, v=38,...,42.** For v=38,...,41, every vertex has degree >=8. Let L be all vertices with degree <=11, let r=|L|. Because vertices outside L have degree >=12,

`384>=8r+12(v-r)`, hence `r>=3v-96`, giving r>=18,21,24,27.

On L, join x,y when lambda_xy>=2. This graph G has

`2|E(G)| <= sum_{x in L}(5d(x)-(v-1)) <= (61-v)r+1920-60v`.

For any graph on r vertices with e edges, a random vertex ordering gives an independent set of expected size `sum_x 1/(deg_G(x)+1)>=r^2/(r+2e)`. Thus

`alpha(G) >= r^2/[(62-v)r+1920-60v]>2`

for each v=38,...,41. The final inequality follows from

`r^2-2((62-v)r+1920-60v)=(r-(62-v))^2+c_v>0`,

where `c_38=144`, `c_39=311`, `c_40=476`, `c_41=639`. Therefore choose three degree <=11 vertices of pairwise codegree one. Arrange their degrees increasingly `d1<=d2<=d3` and lock them at positions floor(v/2)-1, floor(v/2),floor(v/2)+1.

For v=42, every vertex has degree >=9 and total degree 384=9*42+6. Thus at least 36 vertices have degree exactly nine. Each such vertex has excess `5*9-41=4`, so in the same auxiliary graph its degree is at most four. An independent set has size at least ceil(36/5)>=3. Pick three degree-9 vertices of pairwise codegree one and lock at positions 20,21,22.

For *any* chosen triple of pairwise codegree-one vertices, there are precisely two possible patterns on their 3-set: either a single edge contains all three (tri=1), or there are three different edges each containing one of the three pairs (tri=0). If tri=1 the nonzero exact types are:

`ell_xyz=1; ell_x=d1-1; ell_y=d2-1; ell_z=d3-1; ell_empty=64-(d1+d2+d3)+2`.

If tri=0, they are:

`ell_xy=ell_xz=ell_yz=1; ell_x=d1-2; ell_y=d2-2; ell_z=d3-2; ell_empty=64-(d1+d2+d3)+3`.

Check all nondecreasing degree triples in [8,11] for v=38,...,41 and both tri patterns (40 exact profiles per v), plus (9,9,9) with both patterns at v=42.

## 5. Output of the exact rational certificate

Every entry in this table is the MAXIMUM of U over all profiles for the indicated class (not an approximation). The entire code enumerates precisely 200 profiles.

| Class | Profiles | Maximum U |
|---|---:|---:|
| v=27,...,33, unlocked | 7 | 30456829/30705345 |
| v=34, one lock | 5 | 20526/20677 |
| v=35, one lock d=7,...,9 | 3 | 228571/229245 |
| v=35, two locks (10,10,...,13) | 4 | 6081796/6141069 |
| v=36, one lock d=7,...,9 | 3 | 1600867/1604715 |
| v=36, two locks (10,10,...,13) | 4 | 7522879/7565085 |
| v=37, two locks | 12 | 264643139/264777975 |
| v=38, three locks | 40 | 15221219/15575175 |
| v=39, three locks | 40 | 73619797/74760840 |
| v=40, three locks | 40 | 51026249/51225020 |
| v=41, three locks | 40 | 389058273/389310152 |
| v=42, three locks | 2 | 1258094393/1265257994 |

The biggest of all certified profile bounds is 264643139/264777975 < 1 (v=37, degrees 10 and 12). Each possible counterexample therefore admits at least one successful greedy ordering. Contradiction. Consequently `m(6)>=65`.

## 6. Reproduction

Run from a directory containing the attached script:

```sh
python3 propertyB_m6_certificate.py
```

The script uses only exact integer binomial coefficients and rational arithmetic. It fails an assertion if any of the 200 checked upper bounds is >=1; it also checks the numerical prerequisites used by the structural reduction. The executable arithmetic is not a Lean formalization; the mathematical arguments in Sections 1-4 justify its finite, exhaustive domain and every subtraction in the bound.
