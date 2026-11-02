# Independent mathematical acceptance argument

This acceptance is a fresh finite arithmetic check and a mathematical instantiation of the existing general short-walk argument. It does not compile a new concrete Lean instance. The producer's implementation, geometry records, and route caches are not inputs. The only producer artifact to be accepted is the completed literal edge file. The final literal run has now passed, as recorded in `SUMMARY.json` and `NEW_ROOT_BFS.csv`. All 5121600 literal edges were checked; all 160050 vertices have degree 64; all 50 new roots reached all 160050 vertices within radius three. Their common distance histogram is (1,64,3528,156457).

## Finite incidence structure and labels

Work over GF(7) with vectors `(u0,u1,v0,v1)`. The alternating form is

`B(x,y) = u0*v0' + 3*u1*v1' - v0*u0' - 3*v1*u1' (mod 7)`.

In GF(49)=GF(7)[beta]/(beta^2-3), this is half the trace of `u*v'-v*u'`. Multiplication by the nonzero scalar 2 does not change the zero relation. Three is a nonsquare modulo seven, so the stated quadratic quotient is a field. Nondegeneracy of B also follows directly from its displayed matrix, with the two nonzero coefficients 1 and 3.

The validator independently enumerates all 400 projective points, using first nonzero coordinate 1 and lexicographic order. It enumerates every 2-by-4 rank-two RREF matrix. These 2850 distinct matrices represent every two-dimensional subspace exactly once. Retaining B(row0,row1)=0 yields exactly 400 isotropic projective lines. Each is stored as its eight sorted point IDs; sorting those tuples fixes the line labels independently. Pairwise B=0 is additionally checked on all points of every retained line. Each point lies on exactly eight of those lines. Distinct lines have at most one common point, and two different points have at most one common line.

For each of all 400*400=160000 point-line pairs `(p,l)`, the validator searches every point `q` of `l` and requires an actual line `m` containing both p and q. This is precisely the premise

`exists q,m: q in l and p in m and q in m`.

For each of the 156800 nonincident pairs exactly one q works. For each incident pair all eight q work. Uniqueness is checked but the diameter upper bound needs only existence.

For each finite slope `j=0,...,48`, put `a=j%7,b=j/7`. The corresponding spread line is

`v0=a*u0+3*b*u1, v1=b*u0+a*u1 (mod 7)`.

The final spread line is `u0=u1=0`. Each of these 50 independently derived eight-point sets must equal one of the independently enumerated isotropic lines, and every point must belong to exactly one of them. The run checks all 400 ownership obligations. The through-point lists provide all eight line slots; this supplies the general theorem's `hline` premise. The unique spread owner supplies its `howner` premise. All spread lines are nonempty.

An old label `x=400*p+l` is identified with `(p,l)` by integer quotient and remainder. This is a bijection from the 160000 old labels to all 400*400 point-line pairs; incidence of p and l is not required for a vertex to exist. The new label `160000+j` is denoted `z_j`.

## Complete adjacency formula and binding to the literal file

For distinct old vertices `(p,l),(q,m)`, adjacency means `p in m` and `q in l`. The new vertex `z_j` is adjacent exactly to the old flags `(p,l)` with `p in l` and `p in spread(j)`. There are no edges between new vertices.

For any old `(p,l)`, all possible old neighbors are the 8*8 distinct pairs `(q,m)` with `q in l` and `m` through p. This includes the old vertex itself precisely when `p in l`; that one candidate is discarded. Thus the old formula degree is 63 on 3200 flags and 64 on the other 156800 vertices, and the old edge count is `(160000*64-3200)/2=5118400`. Each flag obtains exactly one new neighbor by the unique spread owner of p. Each `z_j` has exactly 8*8=64 flag neighbors. Consequently the full formula graph is 64-regular, of order 160050, with 5121600 edges. The finite program independently enumerates these 64 candidates for every old vertex and the 64 flags for every new vertex; it does not assume the degree formula from the producer.

The literal validation must check its declared header, exactly two endpoints on every edge line, endpoint range, u<v, strict lexicographic sorting (therefore no repeated edges), all 5121600 edges against the independent formula, and degree exactly 64 at every one of the 160050 vertices. This proves equality with the entire formula graph: the literal graph is an allowed subgraph, while both graphs have degree 64 at each vertex. No formula edge can be missing without lowering a literal degree. This also proves that all old formula edges are retained, without regenerating a second giant source edge file.

## Why the finite premises cover every pair within three steps

The actual existing statements and proof bodies were read in:

- `formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadGeneric.lean` (exact graph definition),
- `formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadWalks.lean` (`diameter_three`),
- `formal/DegreeDiameter/Portfolio/OppositeIncidenceSpreadSlots.lean` (incidence lists, owner and degree coverage),
- `formal/DegreeDiameter/Portfolio/OppositeIncidenceSpreadFamily.lean` (conditional family interface).

The reusable theorem is generic in the point, line, old-label and spread types. Its proof does not depend on numerical 6160 or 7242 geometry. It still requires the actual finite projection premises, and this acceptance checks all of them independently for the present 400-point geometry. The following direct reconstruction explains its three cases. A step between identical old tuples can be omitted; otherwise each displayed step is an actual edge by opposite incidence. This handles coincidences without requiring loops.

For two old vertices `(p,l)` and `(q,m)`, project q onto l, giving `a in l` and a line k containing q and a. Project p onto m, giving `b in m` and a line n containing p and b. Then the weak three-step walk is

`(p,l) -> (a,n) -> (b,k) -> (q,m)`.

The three pairs of required incidences are respectively `(p in n,a in l)`, `(a in k,b in n)`, and `(b in m,q in k)`. Thus every old-old pair is covered, including the 160000 old roots that are not subjected to literal BFS.

For `z_i` and an old vertex `(p,l)`, project p onto spread(i), giving `a in spread(i)` and a line n through p and a. Project a onto l, giving `q in l` and a line b through a and q. Then

`z_i -> (a,b) -> (q,n) -> (p,l)`.

The first old tuple is a flag whose point is on spread(i); the two opposite-incidence steps use `(a in n,q in b)` and `(q in l,p in n)`. Reversing the walk covers the other orientation.

For `z_i,z_j`, choose any a on the nonempty spread(i). Project a onto spread(j), giving `c in spread(j)` and a line b through a and c. Then

`z_i -> (a,b) -> (c,b) -> z_j`.

Again any identical intermediate tuple is omitted. This covers every new-new pair. These three constructions establish the all-pairs diameter bound from the complete finite geometry premises and the exact formula binding. The 50 new-root literal queue BFS runs are additional direct checks with a clearly separate scope; alone they would not prove the old-old case.

Finally, a graph of maximum degree 64 and diameter at most two has at most `1+64+64^2=4161` vertices, even using this deliberately loose walk-count bound. Here 160050>4161, so the diameter is exactly three.

No public priority, adoption, or world-record certification follows from this acceptance. It is distinct from a future concrete Lean instance.
