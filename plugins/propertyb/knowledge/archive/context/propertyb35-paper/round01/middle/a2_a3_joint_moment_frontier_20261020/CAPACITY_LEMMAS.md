# Two degree-sensitive common-middle capacities

Let H be a simple five-uniform hypergraph with M distinct original edges. For an unordered outer pair {G,J}, a valid middle F is an original edge with F∩G={g}, F∩J={h}, g≠h. Write c(G,J) for their number, nj for the number of unordered original outer pairs with intersection size j, and Cj=Σ_{|G∩J|=j}c(G,J). All counts below refer to this same H and retain original edge indices.

## Two-intersection capacity

If |G∩J|=2, set A=G\J and B=J\G, each of size three. A valid middle contains its two different attachments respectively in A and B. Charging that original middle once at each attachment gives exactly2c(G,J) charges. For v∈A∪B, there are at most d_H(v)−1 available original edges through v: the outer edge containing v is unavailable as a middle. This is an upper bound even if other actual incidence constraints would make fewer usable. Therefore

\[
2c(G,J)\le\sum_{v\in A\cup B}(d_H(v)-1)
\le S_6-6,
\]

where S6 is the sum of the six largest original point degrees. Consequently

\[
C_2\le\left\lfloor\frac{S_6-6}{2}\right\rfloor n_2.
\tag{1}
\]

For every A2/A3 degree spectrum in the supplied complete spectrum list, there are at least eight degree-at-least-nine points and at most four points above nine. If e=Σ_v max(d_H(v)−9,0), all that excess occurs among the six largest degrees, so S6=54+e. Thus

\[
C_2\le(24+\lfloor e/2\rfloor)n_2.
\tag{2}
\]

This charges each middle exactly twice, not once, before dividing; no independence between the choices at its two attachments is assumed.

## Singleton-intersection capacity

For each point v let tv be the number of unordered original outer pairs with intersection exactly{v}. These actual integers satisfy

\[
\sum_v t_v=n_1,\qquad0\le t_v\le\binom{d_H(v)}2.
\]

For any such outer pair a valid middle cannot contain v, because its two singleton attachments differ. There are M−d_H(v) original edges avoiding v. Hence

\[
C_1\le\sum_v(M-d_H(v))t_v
=Mn_1-\sum_vd_H(v)t_v.
\tag{3}
\]

Order the actual point degrees d1≤…≤dn, with capacities pi=C(di,2). Let

\[
K_d(N)=\min\left\{\sum_i d_i z_i:
\sum_i z_i=N,\ 0\le z_i\le p_i,\ z_i\in\mathbb Z\right\}.
\]

This minimum is obtained by filling the capacities in nondecreasing degree order. Indeed, if a higher-cost capacity is used while a lower-cost capacity is not full, moving one unit reduces or preserves the objective. All capacities and N are integral, so this procedure gives an integral minimizer and is exactly optimal for the displayed relaxation. The actual tv give one feasible allocation, yielding

\[
\boxed{C_1\le Mn_1-K_d(n_1).}
\tag{4}
\]

Higher-degree capacities need not be filled at all. This is why replacing each dv by a maximum degree is unnecessary and generally weaker. The minimum is a relaxation of actual singleton-pair allocations; it does not assert that its optimizer is realizable by an H.

Neither lemma uses a coloring, Δ≤9, or a vertex-degree-role assignment beyond the actual degree list. Formula(2), unlike(1), specifically uses the supplied A2/A3 spectrum form. These are necessary common-middle capacities, not sufficient coloring criteria by themselves.
