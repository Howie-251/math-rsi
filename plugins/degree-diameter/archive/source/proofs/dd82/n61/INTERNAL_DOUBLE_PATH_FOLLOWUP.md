# Double paths: offset restriction and a bounded length consequence

Date: 2026-10-13. **Writer-checked exploratory draft only.** No independent
review, solver, enumeration, external call, or formalization is claimed.

## Assumptions and claim

Let $A$ be the actual adjacency of an order61, degree8, diameter-two
graph and $B=A^2+A-7I-J$. Import the actual defect conclusions and path
forest premise stated in
[INTERNAL_DOUBLE_PATH_LOCAL.md](INTERNAL_DOUBLE_PATH_LOCAL.md): $B$ is
symmetric, nonnegative integral, has row sum4 and entries at most2,
and $D=\{xy:B_{xy}=2\}$ is a path forest. Use that note's proved
Toeplitz restriction on the adjacency inside a $D$ path.

The following are additional necessary conclusions:

1. Its three internal-vertex types with $\beta=1$ occur only when the
   entire $D$ component has exactly three vertices.
2. If a path has vertices $v_0,\ldots,v_m$ and Toeplitz adjacency
   coefficients $a_d=A_{v_i,v_{i+d}}$, distinct positive offsets with
   $a_p=a_q=1$ satisfy
   $$p+q>m\quad\text{or}\quad p+q=m\text{ and }|p-q|=1. \tag{1}$$
3. Every component of $D$ has at most52 vertices.

These statements neither exclude internal double vertices nor assert
that a path near the bound is realizable. The only identities used
after the imported local lemma are actual common-neighbor counts and
degree eight. All deductions are exact; there is no approximation.

## 1. The three beta-one types belong only to a three-vertex component

Consider consecutive $u,v,w$ on a $D$ path. In the local notation,
$\beta=B_{uw}$. If $\beta=1$, the row at $u$ already contains the
double edge $uv$ and this unit edge. It cannot have a second double
edge: that would give row weight at least5. Hence $u$ is a $D$
endpoint. The same argument makes $w$ an endpoint. Since $v$ already
has its two double neighbors, this component is exactly $u,v,w$.

Consequently any three consecutive vertices in a component with at
least four vertices have $\beta=0$. Only the local types
$$(\epsilon,\beta,r,h)=(1,0,0,0),\ (0,0,0,1),\ (0,0,1,0)$$
remain there. This does not eliminate the three beta-one types from
the whole graph; it confines them to components of size three.

## 2. Distinct Toeplitz offsets cannot make an interior rectangle

It suffices to consider $m\ge2$. The imported local result gives
$a_1=0$ and the stated Toeplitz form. An internal path vertex has its
entire defect row equal to twice the two neighboring path vertices.
In particular, between nonconsecutive path vertices with at least one
internal endpoint, $B$ is zero. Their actual coverage count is thus
$$\mu(x,y)+A_{xy}=1. \tag{2}$$

Suppose $p\ne q$, $a_p=a_q=1$, and $p+q\le m$. The four distinct
path vertices
$$v_0,\ v_p,\ v_q,\ v_{p+q}$$
form an $A$ rectangle: both $v_p$ and $v_q$ are common neighbors of
$v_0,v_{p+q}$. If $p+q<m$, the last vertex is internal and their
path distance exceeds one. This contradicts (2).

It remains that $p+q=m$. Now $v_0,v_m$ are two common neighbors of
$v_p,v_q$. Both latter vertices are internal. If $|p-q|\ge2$, (2)
again gives a contradiction. The only unexcluded boundary case is
$|p-q|=1$, proving (1). No original adjacency between these opposite
vertices was assumed: two common neighbors alone already violate (2).

## 3. At least nine vertices must lie outside a sufficiently long path

Suppose for contradiction that the path has $k=m+1\ge53$ vertices.
Consecutive internal vertices $x,y$ are original nonneighbors and
have exactly three common $A$ neighbors, because $B_{xy}=2$.
Write $d_P(x)$ for the number of $A$ neighbors of $x$ lying on this
whole $D$ path. The union of their outside neighbor sets has size
$$16-d_P(x)-d_P(y)
 -|N_A(x)\cap N_A(y)\setminus V(P)|. \tag{3}$$

First let $m=2r$. Since $m$ is even, the boundary alternative in
(1) cannot occur: distinct offsets summing to an even number cannot
differ by one. Thus any two selected distinct offsets have sum
greater than $2r$. For $x=v_r$, at most one selected offset is at
most $r$, and it contributes two path neighbors; hence $d_P(x)\le2$.
For $y=v_{r-1}$, offsets at most $r-1$ each contribute twice, and
offsets $r,r+1$ each contribute once. At most one of the small offsets
can occur. If one occurs, it cannot coexist with either large offset
by (1). With no small offset, the two large offsets contribute at
most two neighbors. Hence $d_P(y)\le2$ as well. Their outside common
neighbors number at most three, so (3) is at least $16-2-2-3=9$.

Now let $m=2r+1$ and take $x=v_r,y=v_{r+1}$. For either central
vertex, selected offsets at most $r$ contribute twice and offset
$r+1$ contributes once; their path degrees are equal. At most one
of the smaller offsets occurs. If both the smaller offset $p$ and
$r+1$ occur, (1) forces $p=r$. Thus either both central path degrees
are at most two, giving the same lower bound nine, or
$$a_r=a_{r+1}=1,\qquad d_P(x)=d_P(y)=3.$$
In the latter case both endpoints $v_0,v_m$ are common $A$ neighbors
of $x,y$. At most one of their three common neighbors can lie outside
the path. Equation (3) is then at least $16-3-3-1=9$.

In both parity cases the graph needs at least nine vertices outside
the path. But $61-k\le8$, a contradiction. Therefore $k\le52$.
The argument intentionally addresses only paths large enough for this
contradiction; isolated vertices and short paths require no extra case.

## Boundary and remaining obligation

The new restrictions use the same original $A,B$ as the inherited
template. They do not extend Toeplitz symmetry beyond the path, impose
any automorphism, make $B$ simple, or show that all internal-vertex
types are impossible. Paths on at most52 vertices, the three beta-zero
types on longer-than-three components, and all six types on eligible
three-vertex components remain unexcluded by this draft. No claim of a
sharp path bound or progress to a complete order61 exclusion is made.
