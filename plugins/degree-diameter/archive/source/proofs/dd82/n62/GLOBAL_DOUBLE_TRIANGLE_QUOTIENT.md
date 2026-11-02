# Double repeats, generated unit triangles, and the component quotient

## Claim and status

**PROVABLE AS STATED:** the disjointness, D0 prism, equitable quotient,
and D1 quotient bounds below follow from the actual graph identities and
the cited local reductions. They do not prove that the number of D1 double
edges is even, or exclude the remaining order-62 candidate.

This is a new paper derivation, not an independently reviewed result or a
Lean theorem. The last port bound additionally uses the no-unit-triangle
consequence of `D1_MATCH_C4_TRANSPORT_REFINEMENT.md`.

## Assumptions and notation

Let $G$ be an actual 62-vertex graph of maximum degree eight and diameter
at most two. Write $A$ for its adjacency matrix and
$B=A^2+A-7I-J$. Use the established identities

$$A\mathbf1=8\mathbf1,\qquad B\mathbf1=3\mathbf1,
\qquad AB=BA,\qquad c(x,y)+A_{xy}=1+B_{xy}.$$

Use triple-repeat exclusion, triangle pairing, and the D0/D1 reductions
in the neighboring papers. Thus all entries of $B$ are at most two,
the double edges form a matching, and every double edge is either in a
closed D0 alternating four-cycle or has the D1 structure. Let $d$ be the
number of double edges and $T$ the number of original triangles.

For a double edge $e=\{u,v\}$ define its **generated triangle**

$$S_e=N_G(u)\cap N_G(v).$$

This is a unit triangle in $B$, not a triangle in $G$. Let $D$ be the set
of all double-edge endpoints and let $S$ be the union of all generated
triangles. A component always means a component of the positive support
of $B$ unless another graph is specified.

## Proof strategy and dependencies

1. Row budgets and common-neighbor counts separate the generated motifs.
2. The D0 theorem identifies their companion prism; commutation identifies
   its original-graph induced subgraph.
3. The eigenspace at $B$-eigenvalue three gives the component quotient of
   $A$. Its exact quadratic identity gives an odd component count and a
   diagonal sum.
4. The proved D1 rows give lower bounds on the corresponding quotient
   entries. The additional D1 light-mate theorem gives a global port count.

## 1. Generated triangles are disjoint motifs

The endpoints $u,v$ are nonadjacent and have exactly three common
neighbors. Both endpoints are triangle-free: their nonadjacent repeat
weight two leaves only one unit in their repeat row, whereas a triangle
would require two units on original edges. Consequently $S_e$ is an
independent three-set in $G$.

Each pair $x,y\in S_e$ already has common neighbors $u,v$, hence
$B_{xy}\ge1$. The recovered root template supplies the exact value:
at root $u$, its only exceptional parent sets
have sizes three and two; the parent pair can meet the triple in at
most one point after the D2 exclusion. Thus every pair in $S_e$ has
exactly the two common neighbors $u,v$, and

$$B[S_e]=J_3-I_3.$$

Each vertex of $S_e$ now has two nonadjacent unit repeats, so it cannot
be a double-edge endpoint or lie in an original triangle.

Two generated triangles cannot share exactly one vertex: that vertex
would have four distinct required unit repeat neighbors. If they share
at least two vertices $x,y$, then $x,y$ have the four distinct endpoints
of the two double edges as common neighbors. This contradicts their
already established common-neighbor count two. The double-edge endpoints
are distinct because a row of sum three cannot contain two double
entries. Thus the generated triangles are pairwise disjoint.

Original triangles are vertex-disjoint, so these observations give

$$|D|=2d,\qquad |S|=3d,\qquad 5d+3T\le62. \tag{1}$$

There is also a useful incidence restriction. For $e\ne f$, the
two-by-three matrix $A[e,S_f]$ is a partial matching: every row and
every column contains at most one one. A vertex outside the endpoints
of $f$ cannot neighbor two vertices of $S_f$, because each pair in
$S_f$ already has its exact two common neighbors. A vertex of $S_f$
cannot neighbor both endpoints of $e$, because then it would belong to
$S_e$, contrary to disjointness.

No assertion that *every* unit triangle of $B$ is generated is needed
or proved here.

## 2. A D0 component has a companion independent prism

Use the D0 notation with closed component

$$0\mathrel{-_2}w\mathrel{-_1}b
 \mathrel{-_2}a\mathrel{-_1}0.$$

Let $S_{0w}=\{1,2,3\}$. The D0 proof constructs distinct points
$c_1,c_2,c_3$, with $B_{i,c_i}=1$, that are all common neighbors of
$a,b$. Since $B_{ab}=2$, these three points are exactly $S_{ab}$.
Section 1 gives a unit triangle on each triple. Their three matching
unit edges exhaust all six repeat rows. Thus

$$K=S_{0w}\cup S_{ab}$$

is a separate closed six-vertex component of $B$, with block matrix

$$B[K]=\begin{pmatrix}J_3-I_3&I_3\\I_3&J_3-I_3\end{pmatrix}. \tag{2}$$

Both triples are independent in $G$. In D0_EDGE_BOUT each $c_i$ has
its unique root parent $b\notin S_{0w}$, so there are no original
edges between the triples either.

For D0_MATCH, every $c_i$ is an ordinary single-parent point. Thus each
has at most one original neighbor in $S_{0w}$. Section 3 below shows
that every component induces a regular original subgraph. Consequently
$G[K]$ has common degree zero or one. In the degree-one case its
cross-block $P=A[S_{0w},S_{ab}]$ is a permutation matrix. Its diagonal
is zero because each matched repeat pair $i,c_i$ is triangle-free and
therefore nonadjacent in $G$. Since $K$ is closed under $B$, the $K,K$
block of $AB=BA$ gives commutation of $A[K]$ and (2). Their upper-left
blocks give $P=P^T$. This would be a fixed-point-free involution of a
three-element set, which is impossible. Hence $G[K]$ has degree zero
also in D0_MATCH.

The four-vertex D0 component and its companion prism therefore have
sizes four and six and original internal degrees, respectively,

$$\begin{cases}(0,0)&\text{in D0_MATCH},\\
(1,0)&\text{in D0_EDGE_BOUT}.
\end{cases} \tag{3}$$

Different D0 components have different companion prisms, because the
generated triples are disjoint and each displayed prism exhausts its
six rows.

## 3. The component quotient has an exact spectral count

Let $C_1,\ldots,C_k$ be all components of $B$, and let $n_i=|C_i|$.
The eigenspace $Bf=3f$ consists exactly of vectors constant on these
components: the identity

$$f^T(3I-B)f=\frac12\sum_{x,y}B_{xy}(f_x-f_y)^2$$

proves the nontrivial direction. Since $A$ commutes with $B$, the
vector $A\mathbf1_{C_j}$ is constant on every $C_i$. Thus $r_{ij}$,
the number of original neighbors in $C_j$ of a vertex in $C_i$, is
well-defined. In particular each $G[C_i]$ is regular of degree $r_{ii}$.

For the quotient matrix $R=(r_{ij})$ and column vector
$n=(n_1,\ldots,n_k)^T$, the actual graph identity restricts to

$$R\mathbf1=8\mathbf1,\qquad
 R^2+R=10I+\mathbf1 n^T,\qquad
 n_i r_{ij}=n_j r_{ji}. \tag{4}$$

The quotient is similar to a symmetric matrix. On the subspace
$n^Tx=0$, every eigenvalue is one of

$$\lambda_\pm=\frac{-1\pm\sqrt{41}}2.$$

The principal direction has eigenvalue eight. Since $R$ is an integer
matrix and $x^2+x-10$ is irreducible over the rationals, the two
irrational eigenvalues have the same multiplicity, say $m$. Therefore

$$k=2m+1,\qquad
 \sum_{i=1}^k r_{ii}=8-m=\frac{17-k}{2},\qquad
 \boxed{k+2\sum_i r_{ii}=17}. \tag{5}$$

In particular $k$ is odd. Each component has even size, independently:
its total repeat weight is $3n_i$, twice its unordered edge weight.

Let $z$ be the number of D0 components, and $b$ the number among them
of D0_EDGE_BOUT type. The triangle-pairing theorem supplies $T/2$
additional closed components, each of size six and internal degree two.
Remove these and the $z$ D0 components with their $z$ companion prisms.
For the remaining components, (3) and (5) give the exact bookkeeping
identity

$$2z+2b+\frac{5T}{2}
 +\sum_{C\ \mathrm{remaining}}(1+2r_{CC})=17. \tag{6}$$

## 4. D1 forces large quotient incidences

Use the normalized D1 notation in
`D1_MATCH_HARD_BRANCH_REDUCTION.md`. Let $H$ contain its heavy
endpoints $0,w$, and let $K$ contain $S_{0w}=\{1,2,3\}$.
The unit rows at $1,2,3$ put $4,b,c$ in $K$. These are three distinct
vertices outside the triple. The original neighbors $1,2,3,4$ of $0$
all lie in $K$; the original neighbors $1,2,3,b$ of $w$ all lie there.
The unit mates $a,r$ of $0,w$ lie in $H$, and vertex $1$ has the three
distinct original neighbors $0,w,a$ in $H$. Hence

$$H\ne K\quad\Longrightarrow\quad
 r_{HK}\ge4,\qquad r_{KH}\ge3, \tag{7}$$

whereas

$$H=K\quad\Longrightarrow\quad r_{HH}\ge4. \tag{8}$$

For example, a fixed component can contain heavy pairs whose generated
triangles lie in at most two distinct other components: each such
component consumes at least four of the eight original neighbors of
every vertex. A component can receive generated triangles from heavy
pairs in at most two distinct other components, by the lower bound
three in the other direction. These are degree bounds on the relation
between components, not a pairing theorem for double edges.

## 5. Conditional on the additional D1 light-mate lemma: a port bound

The cited C4 refinement proves that each light mate of a D1 heavy
endpoint belongs to no unit triangle of $B$. In D0 its light mate is
another double-edge endpoint. Therefore no repeat edge joins $D$ to
$S$. Triangle pairing also separates $D$ from all original triangle
vertices.

Let $d_0=2z$ count the double edges in D0 components and put
$d_1=d-d_0$. Let $W$ be the complement of $D$, $S$, and all original
triangle vertices. Every one of the $2d_1$ D1 endpoints has its unique
unit mate in $W$. The total repeat capacity of a vertex of $W$ is three,
so

$$2d_1\le3|W|=3(62-5d-3T),$$

or equivalently

$$\boxed{15d+9T+2d_1\le186}. \tag{9}$$

This does not assume distinct light mates for different heavy pairs.

## 6. Bipartite components require a negative signed contribution

There is a second component parity, at the other extremal eigenvalue
of $B$. Let $\ell$ be the number of bipartite support components of
$B$. The identity

$$f^T(3I+B)f=\frac12\sum_{x,y}B_{xy}(f_x+f_y)^2$$

shows that the eigenspace $Bf=-3f$ has one dimension for each such
component and none for a nonbipartite component. A basis consists of
the vectors equal to $+1$ and $-1$ on the two parts of one component,
and zero elsewhere. The two parts have equal size, by weighted
degree counting, so all these vectors are orthogonal to $\mathbf1$.

Commutation makes this space invariant under $A$, and the actual
graph identity restricts to

$$A^2+A=4I.$$

Its two possible eigenvalues are $(-1\pm\sqrt{17})/2$. The restriction
has an integer matrix in the displayed signed-indicator basis: the
coefficient at another component is the difference of two integer
neighbor counts. Irreducibility of $x^2+x-4$ therefore gives

$$\ell\ \text{even},\qquad
 \operatorname{tr}(A|_{B=-3})=-\ell/2. \tag{10}$$

Inside a bipartite component $C$, write $s_C$ and $t_C$ for the
numbers of original neighbors within the same and the opposite
$B$-bipartition side. These are constant across the component: the
ordinary component indicator gives their sum, while the signed
indicator gives their difference. The diagonal entry of the
restricted matrix is $s_C-t_C$. Thus

$$\sum_{C\ \mathrm{bipartite}}(s_C-t_C)=-\ell/2. \tag{11}$$

A D0_MATCH component contributes zero. A D0_EDGE_BOUT component
contributes one, since its two original matching edges join vertices
within the same side of the alternating four-cycle. Consequently,
if any D0 component exists, some other bipartite component must
satisfy $t_C>s_C$. In particular, the D0 components cannot be all
the bipartite components. The additional component contains no unit
triangle of $B$, and hence no generated triangle or original triangle.

## Remaining gap

The component quotient is strongly constrained, but (4)--(9) do not
force an even number of D1 double edges. The bipartite-component
parity (10) counts components, not their double edges. In particular, components
containing a generated unit triangle have not been classified, and
the same component may contain both heavy edges and generated
triangles. No parity conclusion may be inferred solely from the
at-most-two incidence bounds in Section 4.
