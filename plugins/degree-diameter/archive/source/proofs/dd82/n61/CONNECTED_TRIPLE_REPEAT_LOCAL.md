# Connected order61 defect: the forced local form of a triple edge

## Target and status

**COHERENT AS STATED: necessary local reduction, not an exclusion.**
For the actual adjacency A of an order61 target, assume the positive
support of its actual weighted defect B is connected. A defect entry
B_uv=3 forces the specific linked configuration below. In particular,
the two remaining unit defect edges at u and v have the same endpoint.
This manuscript does not exclude that last configuration, assume B is
simple, or import a guarded order62/CP02 conclusion. No enumeration,
solver, new external review, or formal proof was run for this derivation.

## Invariant object, assumptions, and notation

G is a finite simple undirected graph on61 vertices, of maximum degree8
and diameter at most2. It is8-regular: degree at most7 at a vertex would
allow at most1+7+7·7=57 vertices within distance two. Its adjacency is A,
and throughout this note

`B=A²+A−7I−J`.

Thus B is symmetric, integral, nonnegative, has zero diagonal and row
sum4, and AB=BA. Write μ(x,y)=|N_A(x)∩N_A(y)|. For distinct vertices,

`B_xy=μ(x,y)` if xy is an A edge, and
`B_xy=μ(x,y)−1` otherwise.

The positive support of B is assumed connected. A positive B entry is
always a weight of this actual matrix, not a separately chosen edge.
All neighborhoods and incidences below refer to the same A.

## Derivation strategy and map

First spend the exact row-four defect budget at a triple pair. Then
use AB=BA to identify its two unit ports and the ports of its four
common A neighbors. Eliminate unequal unit-port endpoints. Finally
record the remaining configuration and its forced eight-vertex blocks.

The steps are exact identities or necessary propositions. No
approximation or model restriction enters the argument.

## 1. Initial local budgets

A weight4 entry would saturate both of its endpoint rows and give a
two-vertex B component, so connectedness excludes it. If xy is an A
edge with B_xy=λ, each of its λ common A neighbors z satisfies B_xz≥1.
Consequently the B row at x has weight at least2λ, and λ≤2. Hence a
weight3 entry can occur only at a nonedge of A.

Fix B_uv=3. There are unique vertices p,q with

`B_u*=3e_vᵀ+e_pᵀ`,  `B_v*=3e_uᵀ+e_qᵀ`.                    (1)

Here p is different from u,v, and q is different from u,v. The sum of
B_xz over A neighbors z of x is twice the number of triangles through
x. At u and v the nonneighbor of weight3 leaves only one unit of
defect, so neither u nor v lies in a triangle. In particular their
A neighborhoods are independent, and p is not A-adjacent to u, nor
q to v.

Put

`S=N_A(u)∩N_A(v)`, `U=N_A(u)\S`, `V=N_A(v)\S`.

Then |S|=|U|=|V|=4. The sets S,U,V are disjoint, and

`W=V(G)\({u,v}∪S∪U∪V)` has size47.

There are no A edges inside S, U, or V, or between S and U∪V. Every
s∈S has A neighborhood `{u,v}∪T_s` for some six-set T_s⊂W.

Every pair of distinct points of S has u,v as common A neighbors and
therefore B weight at least1. These three nonneighbor entries spend
at least three units of each S row. The triangle-count argument again
shows that every s∈S is triangle-free. Its row consequently has the
exact form

`B_s*=Σ_(t∈S\{s}) e_tᵀ+e_ρ(s)ᵀ`.                         (2)

The unique extra endpoint ρ(s) is neither s,u,v. If it belongs to S,
symmetry forces ρ(ρ(s))=s, producing a weight2 S edge. In every case
ρ(s) is not A-adjacent to s, because s is triangle-free.

A useful sparsity fact is

`z∈W and |N_A(z)∩S|≥2  ⇒  z=p=q,
                                  and |N_A(z)∩S|=2`.       (3)

Indeed two S neighbors give B_uz,B_vz≥1; (1) forces z=p=q, and its
two-step multiplicity from u is exactly2. Thus if p≠q, every point
other than u,v has at most one S neighbor. Points of S∪U∪V have none.

## 2. Exact commutation identities for the ports

The (u,v) entry of AB=BA gives

`A_uq=A_vp=:ε`.                                             (4)

If ε=1, then p∈V and q∈U. If ε=0, then p,q∈W; this uses their
nonadjacency to u and v already proved above.

For each s∈S, the (u,s) and (v,s) entries give

`A_ps=1_[ρ(s)∈S∪U]`, `A_qs=1_[ρ(s)∈S∪V]`.                (5)

For example, the two sides of the first identity before cancellation
are3+A_ps and3+1_[ρ(s)∈S∪U]. For each z∈W the same commutation gives

`Σ_(x∈S∪U) B_xz=A_pz`,
`Σ_(x∈S∪V) B_xz=A_qz`.                                    (6)

Consequently every port ρ(s) that lies in W is an A common neighbor
of p and q. Such W ports for different s are distinct: two of them
at the same z would make the first sum in (6) at least2, whereas its
right side is a binary entry. This distinctness does not assume that
arbitrary B neighbors are distinct in any other part of the graph.

The A graph between U and V has degrees

`deg_V(x)=1+1_[x=q]` for x∈U,
`deg_U(y)=1+1_[y=p]` for y∈V.                               (7)

For instance, v is nonadjacent to x∈U, and its common A neighbors
with x lie in V, since x has no S neighbor.

## 3. Unequal unit-port endpoints are impossible

Suppose p≠q. We repeatedly use the following observation: B_pq=3
would, together with (1), saturate the four rows u,v,p,q and give a
closed four-vertex B component. Thus it is impossible here.

### 3a. The case ε=1

Now p∈V and q∈U, so both have no S neighbor. Equation (5) puts all
four ports ρ(s) in W. They are four distinct common A neighbors of
p,q. If pq were an A edge, its defect weight would be at least4,
contrary to the adjacent-edge bound. Otherwise B_pq≥3; weight4 is
already excluded, and weight3 gives the closed component just noted.
Hence ε=1 is impossible.

### 3b. The case ε=0

Here p,q∈W. Let α=|N_A(p)∩S| and β=|N_A(q)∩S|. By (3), both belong
to {0,1}. Their S neighbors, if both present, are different. To see
this, a common S neighbor s would, by (5), have ρ(s)∈S. Symmetry and
(5) would then make both p and q adjacent to the distinct point
ρ(s), contradicting α,β≤1.

When α=1, the unique S neighbor of p has its port in U; when β=1,
the unique S neighbor of q has its port in V. Every other S port
lies in W. The latter are4−α−β distinct common A neighbors of p,q.
Also, since B_up=1 but B_vp=0,

`deg_U(p)=2−α`, `deg_V(p)=1−α`;                              (8)

interchanging p,q and u,v gives deg_U(q)=1−β, deg_V(q)=2−β.

If α=β=0, four W ports force B_pq=3 exactly as in3a, giving the
same closed component.

If (α,β)=(1,0), let s₀ be p's unique S neighbor. The other three
S ports give μ(p,q)≥3. The adjacent-edge bound excludes pq∈E(A),
and connectedness excludes B_pq=3, so B_pq=2. The remaining B row
of p is therefore

`B_p*=e_uᵀ+2e_qᵀ+e_hᵀ`, with h∉{u,v,p,q}.                 (9)

For s∈S\{s₀}, the (p,s) entry of AB equals2: s₀ supplies one unit
from (2), and ρ(s)∈W supplies the other. The corresponding BA entry
is1+A_hs, because q has no S neighbor. Thus h is adjacent to all
three points of S\{s₀}. This contradicts (3). The (0,1) case follows
by interchanging u,v and p,q.

If α=β=1, let s₀ and s₁ be the distinct S neighbors of p and q.
There are two W ports, so B_pq≥1, irrespective of whether p,q are
adjacent. Equation (8) gives deg_V(p)=0, while ρ(s₁)∈V. Consequently

`(AB)_(p,s₁)=1`,

the only contribution being s₀ from the base S clique in (2).
But `(BA)_(p,s₁)≥B_pu A_us₁+B_pq A_qs₁=1+B_pq≥2`, a contradiction.

All unequal-endpoint cases are exhausted. Therefore

`p=q=w∈W`.                                                 (10)

## 4. The remaining seven-vertex configuration

Let k=|N_A(w)∩S|. It is at most2 by (3). Equation (5) says that
w-adjacent S points are precisely the endpoints of internal S port
edges. They occur in pairs, so k is0 or2.

If k=0, all four ports ρ(s) lie in W and are adjacent to w. Therefore
`(AB)_(w,s)=1` for every s∈S. But B_wu=B_wv=1 gives
`(BA)_(w,s)≥2`, a contradiction. Hence k=2.

Label S={a,b,c,d} so that N_A(w)∩S={a,b}. Then

```text
B_u* = 3e_vᵀ + e_wᵀ,
B_v* = 3e_uᵀ + e_wᵀ,
B_a* = 2e_bᵀ + e_cᵀ + e_dᵀ,
B_b* = 2e_aᵀ + e_cᵀ + e_dᵀ,
B_c* = e_aᵀ + e_bᵀ + e_dᵀ + e_rᵀ,
B_d* = e_aᵀ + e_bᵀ + e_cᵀ + e_sᵀ.
```

Here r,s are distinct points of W, each A-adjacent to w; r is not
A-adjacent to c, and s is not A-adjacent to d. Also w has no A neighbor
in U∪V: its two common A neighbors with each of u,v are already a,b.

The B row of w has two further units beyond u,v. Apply AB=BA at
(w,a),(w,b),(w,c),(w,d). Its residual row has A-neighbor sums0,0,1,1
at these four columns: the AB sides are respectively2,2,3,3, and
the two terms from u,v on the BA side contribute2 each time.
Every point other than u,v,w has at most one S neighbor by (3).
Therefore those two remaining units must be at two distinct points
x,y∈W with

`B_w*=e_uᵀ+e_vᵀ+e_xᵀ+e_yᵀ`,
`N_A(x)∩S={c}`, `N_A(y)∩S={d}`.                             (11)

In particular x≠r and y≠s. Other coincidences or A adjacencies among
these W points are not settled by this argument.

## 5. The forced eight-vertex blocks and their four unit ports

Equation (7), now with w outside U∪V, says A[U,V] is a perfect
matching. Put f=e_u−e_v and g=Af=1_U−1_V. From (10),

`Bf=−3f`, `Bg=−3g`, `Ag=4f−g`.                             (12)

The second identity uses AB=BA; the third follows from the actual
defect identity and Jf=0. Thus span(f,g) is an A-invariant plane with
matrix `[[0,4],[1,−1]]` and characteristic factor `t²+t−4`. This is
an actual subspace, not a hypothetical eigenvalue assignment, and is
not by itself a contradiction. It also shows that every point outside
{u,v}∪U∪V has equal numbers of A neighbors in U and V.

For distinct z,z'∈N_A(u), their B weight counts common A neighbors
other than u: N_A(u) is independent. From the exact B row of u, the
only outside points with at least two neighbors in N_A(u) are v,
with neighbor set S, and w, with neighbor set {a,b}. Hence

`B[N_A(u)] = K4(S) + K2({a,b})` entrywise as weighted matrices. (13)

The identical statement holds for N_A(v). In particular B[U]=B[V]=0
and B[S,U∪V]=0. The equation Bg=−3g now makes B[U,V] a nonnegative
integer4×4 matrix C with every row and column sum3. Each point of
U∪V has exactly one remaining unit B edge, necessarily into W.

For z∈W, Bg=−3g implies its total B weight to U equals that to V.
Equation (6), with p=q=w, bounds each of those totals by1. Thus these
eight unit ports meet exactly four distinct points D={z₁,…,z₄}⊂W:
each point of D has one unit B edge to U and one to V, and is
A-adjacent to w. None equals r or s, because the corresponding
S contribution already exhausts the right side of (6). Since w has
six W neighbors in total, this proves the exact neighborhood

`N_A(w)={a,b,r,s}∪D`.                                       (14)

Normalize A[U,V] as the matching u_i v_i. Label z_i∈D by its unit
B neighbor u_i; its V endpoint is v_(σ(i)) for a permutation σ∈S4.
The unresolved local weighted block thus includes C and σ with

`C≥0 integral`, `C1=Cᵀ1=3·1`, `C_ii∈{0,1}`.                (15)

For the diagonal bound, C_ii=2 would give two triangles through the
A edge u_i v_i and spend at least4 defect units on A neighbors of
u_i. Another3−2=1 cross-block unit lies at an A nonneighbor, exceeding
the row-four budget. Larger diagonal entries were already excluded.

If C_ii=0, the three cross-block units are all at A nonneighbors,
so u_i is triangle-free and is not A-adjacent to its B port z_i.
If C_ii=1, the unique triangle through u_i v_i must use both unit
ports; consequently σ(i)=i and z_i is A-adjacent to u_i and v_i.
The corresponding conclusions for V hold with its own unit port.
If an off-diagonal entry C_ij=3, the already proved common-port result
applies to that new triple pair and forces σ(i)=j. None of these
conditions is a sufficiency claim.

### The actual 24-point A interface and the full W partition

Any two points of U have exactly one common A neighbor, namely u:
they are nonadjacent and their B entry is zero by (13). The analogous
statement holds for V. Thus each z∈W has at most one A neighbor in
U and at most one in V. Equation (12) makes those numbers equal.
Each point of U already has neighbors u and its matched V point,
and has six further neighbors in W. Consequently exactly24 distinct
points R⊂W have one neighbor in each of U,V; the other23 have none.

For z∈W\{w}, the exact defect row at u gives

`|N_A(z)∩S|+|N_A(z)∩U|=1`.

Indeed u,z are nonadjacent, B_uz=0, and N_A(u)=S∪U. Thus points of
R have no S neighbor, and every point of W\(R∪{w}) has exactly one.
Define the pairwise disjoint sets

`T_a=N_A(a)\{u,v,w}`, `T_b=N_A(b)\{u,v,w}`,
`T_c=N_A(c)\{u,v}`,   `T_d=N_A(d)\{u,v}`.

Their sizes are5,5,6,6. Together with (3), the counts give the exact
partition

`W={w} ⊔ T_a ⊔ T_b ⊔ T_c ⊔ T_d ⊔ R`,  `|R|=24`.

There are no unassigned vertices outside these layers. Split R into
cells R_ij according to its unique U neighbor u_i and V neighbor v_j.
Write H_ij=|R_ij|. The common A neighbors of u_i,v_j can only lie
in W, so their actual defect entry gives

`H=C+J4−I4`,  `H1=Hᵀ1=6·1`.                              (16)

In particular H_ii=C_ii∈{0,1}. Every point of R has its two specified
U/V neighbors and six further neighbors outside U∪V, whose full incidence pattern is not determined by this count. This incidence count is necessary, not a construction of those
remaining edges.

### The second signed pair and its five-point blocks

Put f_ab=e_a−e_b and h=Af_ab=1_(T_a)−1_(T_b). The exact rows in
Section4 imply

`Bf_ab=−2f_ab`, `Bh=−2h`, `Ah=5f_ab−h`.                    (17)

Since N_A(a) and N_A(b) are independent, the last identity forces
A[T_a,T_b] to be a perfect matching. Its invariant plane has
characteristic factor t²+t−5; again this is not a contradiction.

The same actual-neighborhood count used in (13) gives a useful exact
B block. In N_A(a), the only additional common A neighbors of pairs
are b, whose common-neighbor set with a is {u,v,w}, and c,d, each
with common-neighbor set {u,v}. Consequently B[N_A(a)] has weights
3,1,1 on uv,uw,vw respectively and is zero elsewhere. The statement
for N_A(b) is identical. In particular

`B[T_a]=B[T_b]=0`.

Equation (17) now forces B[T_a,T_b] to have every row and column
sum2. Each point of T_a∪T_b has two further defect units outside
T_a∪T_b. These units need not have distinct endpoints: no simplicity
assumption on B is introduced.

## 6. Exact remaining scope

The derivation excludes every triple-edge branch except (10)–(17).
It fixes21 distinct vertices `{u,v,a,b,c,d}∪U∪V∪{w,r,s}∪D` and many
of their actual A/B incidences, and partitions the remaining vertices
into the explicit layers above. The remaining variables include C,
σ, the positions of x,y from (11), the cells R_ij, and the unspecified
A edges within and between these layers. All must still satisfy
binary symmetric A, degree8, the actual identity defining B, row4,
nonnegativity, and connected positive B support.

These are a complete necessary local template for a triple edge, not
an executed local catalogue or an actual lift. No final contradiction
for this template has been obtained. The case B_uv=3 is therefore
still open after this note. This new local mechanism is separate from
the now-completed defect-component quotient review loop.
