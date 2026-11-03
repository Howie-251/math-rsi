# Connected order61 triple defect: exact layer interfaces

## Scope and inherited object

This is a necessary refinement of
[CONNECTED_TRIPLE_REPEAT_LOCAL.md](CONNECTED_TRIPLE_REPEAT_LOCAL.md),
not an exclusion of its remaining triple-edge template. All matrices
refer to the same actual simple8-regular diameter-two graph on61
vertices, with connected positive support of

`B=A²+A−7I−J`.

No enumeration, solver, or external review was run for this note.
The prior manuscript is unchanged. Here Z denotes its24-point set R;
the lower-case r,s retain their prior meaning as the extra B ports of
c,d. Thus

```text
V(G)={u,v} ⊔ {a,b,c,d} ⊔ U ⊔ V
       ⊔ {w} ⊔ T_a ⊔ T_b ⊔ T_c ⊔ T_d ⊔ Z,
sizes: 2 + 4 + 4 + 4 + 1 + 5 + 5 + 6 + 6 + 24 =61.
```

Each of T_a,T_b,T_c,T_d is independent. A point in T_i has i as
its only neighbor in {a,b,c,d}, and no neighbor in U∪V. A point of
Z has no neighbor in {a,b,c,d} and exactly one neighbor in each of
U,V. The only S neighbors of w are a,b, and w has no U/V neighbor.
The exact inherited defect rows are

```text
B_a*=2e_bᵀ+e_cᵀ+e_dᵀ,
B_b*=2e_aᵀ+e_cᵀ+e_dᵀ,
B_c*=e_aᵀ+e_bᵀ+e_dᵀ+e_rᵀ,
B_d*=e_aᵀ+e_bᵀ+e_cᵀ+e_sᵀ.
```

Also r,s are distinct A neighbors of w, are not adjacent to c,d
respectively, and

`N_A(w)={a,b,r,s}⊔D`, where D has four distinct points and avoids r,s.

The notation d_X(t) means |N_A(t)∩X|, and all indicators below are
ordinary zero-one integers.

## 1. The w interface

The points a,b are triangle-free. Since aw,bw are A edges, w has no
neighbor in T_a or T_b. The pair c,w is an A nonedge with B_cw=0:
its unique common A neighbor must lie in T_c. Similarly w has exactly
one neighbor in T_d. Write those neighbors as γ∈T_c and δ∈T_d.
Degree8 now gives

`N_A(w)={a,b,γ,δ}⊔F`, where F⊂Z and |F|=4.                 (1)

Because r is not adjacent to c, it is not in T_c. It is a W neighbor
of w and therefore belongs to T_d or Z. Similarly

`r∈T_d∪Z`, `s∈T_c∪Z`, `D⊂T_c∪T_d∪Z`.                   (2)

In particular r=δ whenever r∈T_d, and s=γ whenever s∈T_c.

## 2. Exact degrees from the four S rows

For distinct i,t, the actual defect identity reads

`|N_A(i)∩N_A(t)|=1+B_it−A_it`.                            (3)

Apply it with i∈{a,b,c,d}; the complete neighborhoods of these four
points and their complete B rows are already fixed. This suffices to
derive all the following degrees, without independent choices of A
and B.

For t∈T_a, triangle-freeness at a excludes t-w and edges inside T_a.
The b row then gives d_(T_b)(t)=1. Neither r nor s lies in T_a by
(2), so the c and d rows each give one neighbor. Degree8 supplies
the remaining four Z neighbors. The T_b statement is symmetric:

| Point | Its S parent | w | T_a | T_b | T_c | T_d | Z |
|---|---:|---:|---:|---:|---:|---:|---:|
| t∈T_a | 1 | 0 | 0 | 1 | 1 | 1 | 4 |
| t∈T_b | 1 | 0 | 1 | 0 | 1 | 1 | 4 |

For t∈T_c, set h=A_wt. The a,b rows give
`d_(T_a)(t)=d_(T_b)(t)=1−h`. The d row gives
`d_(T_d)(t)=1+1_[t=s]`. Its own layer is independent. Subtracting
these degrees and the parent c from8 gives the last column below.
The same calculation applies to T_d:

| Point | Its S parent | w | T_a | T_b | T_c | T_d | Z |
|---|---:|---:|---:|---:|---:|---:|---:|
| t∈T_c | 1 | h | 1−h | 1−h | 0 | 1+1_[t=s] | 4+h−1_[t=s] |
| t∈T_d | 1 | h | 1−h | 1−h | 1+1_[t=r] | 0 | 4+h−1_[t=r] |

Here h=1 only at γ in T_c, and only at δ in T_d. In particular,
each of the four interfaces from T_a or T_b to T_c or T_d is a
bijection onto the five points other than γ or δ, respectively.
A[T_a,T_b] is the already forced perfect matching.

Finally, for z∈Z, put h=A_wz. Its U and V neighbors account for two
degrees. Equation (3) at a,b,c,d gives

`d_(T_a)(z)=d_(T_b)(z)=1−h`,
`d_(T_c)(z)=1+1_[z=r]`, `d_(T_d)(z)=1+1_[z=s]`.

Therefore

`d_Z(z)=2+h−1_[z=r]−1_[z=s]`.                            (4)

This degree formula uses every vertex class of the exact partition.

## 3. Exactly two port-position cases

Let k=|{r,s}∩Z|. All points of {r,s}∩Z belong to F, by (1), and
have Z degree2 by (4). The other4−k points of F have Z degree3;
all points of Z\F have Z degree2. Handshaking in the actual simple
graph A[Z] makes its number of odd-degree vertices even. Thus
4−k is even, and k is0 or2. In particular the mixed placement of
exactly one of r,s in Z is impossible.

The two surviving cases have the following exact properties.

| Property | Case I: r,s∈Z | Case II: r=δ∈T_d, s=γ∈T_c |
|---|---|---|
| D | {γ,δ} plus two points of Z | Four points of Z, namely F |
| F | r,s and the two Z points of D | D |
| Degrees in A[Z] | Two degree3, twenty-two degree2 | Four degree3, twenty degree2 |
| Number of A[Z] edges | 25 | 26 |
| A[T_c,T_d] | A perfect matching | Degree2 at row s and column r, degree1 elsewhere |
| Number of T_c–T_d edges | 6 | 7 |
| T_c–Z degrees | γ has5, the other five have4 | Every point has4 |
| T_d–Z degrees | δ has5, the other five have4 | Every point has4 |

The interface with seven edges in Case II is not prescribed entry
by entry: in particular whether rs is an A edge remains undecided.
These conclusions are a restriction on actual interfaces, not an
enumerated list of complete graphs.

## 4. An additional triangle restriction at w

The inherited exact row of w is

`B_w*=e_uᵀ+e_vᵀ+e_xᵀ+e_yᵀ`, with x∈T_c and y∈T_d.

For every z∈F⊂Z, wz is an A edge and B_wz=0. Consequently z has
no A neighbor anywhere else in N_A(w). Thus F is independent and
has no edges to γ or δ. The points a,b are triangle-free, so the
only possible edge inside N_A(w) is γδ.

If γδ is present, its triangle with w forces x=γ and y=δ. If γδ
is absent, N_A(w) is independent, and x≠γ and y≠δ. This gives two
explicit alternatives within each port-position case, without
claiming either is realizable.

## 5. What is still free

The layer degrees, four five-point bijections, A[T_c,T_d], and the
two possible Z degree sequences are now fixed as above. The actual
incidence maps into the24 Z points, the graph A[Z], and their joint
compatibility with the U/V cell relation `|Z_ij|=C_ij+1−δ_ij` still
have to be determined. All entries must satisfy the original single
A/B identity and all pairwise coverage conditions.

In particular, C_ii=0 only excludes A adjacency between u_i and its
unit B port z_i (and the corresponding V adjacency). It does not
exclude z_i∈Z: that point may lie in a different U/V cell. No count
or classification of possible C matrices is assumed in this note.
Neither port-position case has been eliminated here, and the triple
defect branch remains open after this refinement.
