# Adjacent double defect at order 61: complete layer and port constraints

## Target and status

**PROVABLE AS STATED for the necessary template below.** The stronger
claim that no adjacent double defect exists is **NOT CURRENTLY
JUSTIFIED** by this derivation. Both the adjacency and defect matrices
below come from the same original graph. No enumeration, solver, or
external review was run for this note.

## Assumptions, invariant object, and notation

Let $A$ be the adjacency matrix of a simple $8$-regular graph on $61$
vertices with diameter at most two, and put
$$B=A^2+A-7I-J.$$
We use the accepted imports in
[CONNECTED_TRIPLE_EXCLUSION.md](CONNECTED_TRIPLE_EXCLUSION.md): the
positive support of $B$ is connected, its diagonal is zero, every row
sum is $4$, and its entries belong to $\{0,1,2\}$. Also $AB=BA$.
For distinct vertices let $\mu(x,y)=|N_A(x)\cap N_A(y)|$; then
$$\mu(x,y)=1+B_{xy}-A_{xy}. \tag{1}$$

Assume $A_{uv}=1$ and $B_{uv}=2$. The notation $d_X(z)$ means the
number of actual $A$ neighbors of $z$ in $X$. All sets subsequently
introduced are disjoint unless an intersection is explicitly stated.

## Strategy and dependency map

1. Spend the exact defect budget at the two triangles on $uv$.
2. Use the actual neighborhood defect blocks and $AB=BA$ to locate
   every extra core port and obtain a partition of all $61$ vertices.
3. Derive every layer degree from (1), then record the remaining
   weighted interfaces and cell cardinalities.

All steps are exact identities or necessary propositions. No
triangle-free assumption, simple-defect assumption, or equal row-type
assumption is imposed.

## 1. The four-point core and its two external defect ports

There are exactly two common $A$ neighbors $s,t$ of $u,v$. The
triangles $uvs$ and $uvt$ give $B_{us},B_{ut},B_{vs},B_{vt}\geq1$.
The row-four budget forces
$$B_{u*}=2e_v^T+e_s^T+e_t^T,
\qquad B_{v*}=2e_u^T+e_s^T+e_t^T. \tag{2}$$
In particular $s,t$ are not adjacent: otherwise $u,s$ would have both
$v$ and $t$ as common neighbors, contradicting $B_{us}=1$.

The common neighbors $u,v$ give $B_{st}\geq1$. If $B_{st}=2$, the
four defect rows on $\{u,v,s,t\}$ are saturated internally, contrary
to connected positive support. Therefore $B_{st}=1$, and
$$B_{s*}=e_u^T+e_v^T+e_t^T+e_p^T,
\qquad B_{t*}=e_u^T+e_v^T+e_s^T+e_q^T, \tag{3}$$
where $p,q$ lie outside the core. They are not yet assumed distinct.

The sum of $B_{xz}$ over $A$ neighbors $z$ of $x$ equals twice the
number of triangles through $x$. At $s$, the neighbors $u,v$ already
contribute two units; the entry at the nonneighbor $t$ contributes
none to this sum. Consequently $p$ is not adjacent to $s$, and $s$
lies in exactly the triangle $suv$. The corresponding facts at $t$
are $A_{tq}=0$ and exactly one triangle $tuv$. Likewise (2) shows
that the only triangles at $u$ or $v$ are the two already identified.

## 2. The full partition and exact location of the ports

Define
$$\begin{aligned}
U&=N_A(u)\setminus\{v,s,t\},& |U|&=5,\\
V&=N_A(v)\setminus\{u,s,t\},& |V|&=5,\\
S&=N_A(s)\setminus\{u,v\},& |S|&=6,\\
T&=N_A(t)\setminus\{u,v\},& |T|&=6.
\end{aligned}$$
The four sets are independent. They are disjoint: the $u,v$
intersection is exactly $\{s,t\}$; the $s,t$ intersection is exactly
$\{u,v\}$; and a point belonging to one of $U,V$ and one of $S,T$
would create an additional triangle at $u$ or $v$.

Let $f=e_u-e_v$ and $g=1_U-1_V$. Equations (2) and the actual
defect identity give
$$Bf=-2f,\quad Af=-f+g,\quad Ag=5f,\quad Bg=-2g. \tag{4}$$
For example $A^2f+Af=5f$, which together with $Af=-f+g$ yields
$Ag=5f$; the last identity follows by commuting $A$ and $B$.
Since $U,V$ are independent, the $U,V$ coordinates of $Ag=5f$
force $A[U,V]=0$. At every other vertex except $u,v$, they force
equal numbers of $A$ neighbors in $U,V$.

We need the exact neighborhood defect block, not merely its support:
$$B[N_A(u)]=K_3(\{v,s,t\}),
\qquad B[N_A(v)]=K_3(\{u,s,t\}). \tag{5}$$
To prove the first identity, any distinct pair in $N_A(u)$ already
has common neighbor $u$, so its defect equals its $A$ adjacency plus
its number of other common neighbors. The only vertex other than
$u$ with two neighbors in $N_A(u)$ is $v$, with neighbors $s,t$;
this follows from the complete row (2) and (1). The induced $A$
edges in $N_A(u)$ are exactly $vs,vt$. These give the claimed three
unit defect entries. Interchanging $u,v$ proves the second identity.
In particular $B[U]=B[V]=0$ and there are no defect edges between
$U\cup V$ and the core.

Two distinct points of $U$ have exactly one common $A$ neighbor,
namely $u$. Thus any vertex other than $u$ has at most one neighbor
in $U$; the same statement holds for $V$. Each point of $U$ has
seven neighbors outside the core and $U\cup V$. By (4), these are
exactly $35$ distinct points having one neighbor in each of $U,V$.
Call this set $Z$. The $12$ points in $S\cup T$ have no such neighbor,
since their existing neighbor $s$ or $t$ already gives their unique
common neighbor with $u$ and with $v$. Counting now proves
$$V(G)=\{u,v,s,t\}\sqcup U\sqcup V\sqcup S\sqcup T\sqcup Z,
\qquad |Z|=35. \tag{6}$$

Equations (3),(5) put both $p,q$ outside $U\cup V$. For any
$z\in S\cup T\cup Z$, the $(u,z)$ entry of $AB=BA$ is
$$1_{z=p}+1_{z=q}+\sum_{i\in U}B_{iz}=A_{sz}+A_{tz}. \tag{7}$$
The corresponding $(v,z)$ equation replaces $U$ by $V$. If $p$ or
$q$ belonged to $Z$, the right side would be zero while the left
side were positive. Also $p\notin S$ and $q\notin T$ by their
nonadjacencies to $s,t$. Hence the ports are completely located:
$$p\in T,\qquad q\in S. \tag{8}$$
In particular they are distinct. Equation (7) gives exactly one unit
of defect from each point of $S\setminus\{q\}$ or
$T\setminus\{p\}$ to each of $U,V$. The points $p,q$ have none,
and there are no defect edges between $Z$ and $U\cup V$.

## 3. All layer degrees and the two cell matrices

Every $U$ point has its parent $u$ and seven $Z$ neighbors; every
$V$ point has its parent $v$ and seven $Z$ neighbors. A point
$x\in S$ has parent $s$, no same-layer neighbor, and by (1)
$$d_T(x)=1+1_{x=q},\qquad d_Z(x)=6-1_{x=q}.$$
For $y\in T$ the degrees are
$$d_S(y)=1+1_{y=p},\qquad d_Z(y)=6-1_{y=p}.$$
Thus the binary interface $K=A[S,T]$ has seven edges: only row $q$
and column $p$ have degree two; its other rows and columns have
degree one. For a point $z\in Z$, (1) at $s,t$ gives one neighbor
in each of $S,T$, because the only external core defect ports are
(8). Including its one neighbor in each of $U,V$ leaves
$$A[Z]\text{ a simple }4\text{-regular graph on }35\text{ points}.
\tag{9}$$

Equation (4) and $B[U]=B[V]=0$ make
$$C=B[U,V]\quad\text{a nonnegative integral }5\times5
\text{ matrix with every row and column sum }2.$$
If $Z_{ij}$ is the cell of points whose $U,V$ neighbors are $u_i,v_j$,
all common neighbors of this nonadjacent pair lie in $Z$, and
$$|Z_{ij}|=1+C_{ij}. \tag{10}$$
All $25$ cells are nonempty. The matrix $C$ need not be binary.

For $y\in T$, commutation at $(s,y)$ gives
$$\sum_{x\in S}B_{xy}=A_{ty}+A_{py}=1,$$
because $T$ is independent. Commutation at $(t,x)$ for $x\in S$
gives the row sums. Hence
$$P=B[S,T]\text{ is a }6\times6\text{ permutation matrix}. \tag{11}$$
If $L_{xy}$ counts the $Z$ points with respective $S,T$ neighbors
$x,y$, their only common $A$ neighbors lie in $Z$, and (1) yields
$$L=J_6-K+P. \tag{12}$$
This equality preserves possible overlap of the $A$ and $B$
interfaces. In particular it does not prescribe one fixed matching.

## 4. Internal defect edges and the remaining Z ports

Let $E=N_A(p)\cap S$ and $F=N_A(q)\cap T$; both have size two.
The same neighborhood count proving (5) now gives
$$B[N_A(s)]=2K_2(\{u,v\})+K_2(E),
\qquad B[N_A(t)]=2K_2(\{u,v\})+K_2(F). \tag{13}$$
For the first equality, the induced $A$ graph on $N_A(s)$ contains
only $uv$. The vertex $t$ contributes one further common neighbor
to that pair, and $p$ contributes one to the pair $E$. The other
vertices have at most one neighbor in $N_A(s)$, by (1),(3).
Thus $B[S]$ is exactly the one unit edge on $E$, and $B[T]$ is
exactly the one unit edge on $F$.

Commutation at $(s,z),(t,z)$ for $z\in Z$ gives
$$\sum_{x\in S}B_{xz}=A_{pz},\qquad
\sum_{y\in T}B_{yz}=A_{qz}. \tag{14}$$
Consequently every positive entry in these two interfaces is a unit;
their supports meet exactly the five $Z$ neighbors of $p$ and the
five $Z$ neighbors of $q$, respectively. The remaining defect row
inside $Z$ is
$$\sum_{z'\in Z}B_{zz'}=4-A_{pz}-A_{qz}. \tag{15}$$
Thus the total weight of unordered edges in $B[Z]$ is $65$, whereas
$A[Z]$ has $70$ edges. No contradiction is asserted between these
different matrices.

More explicitly the $S$-to-$Z$ row sums are
$$\sum_{z\in Z}B_{xz}=1+1_{x=q}-1_{x\in E}\quad(x\in S); \tag{16}$$
the corresponding $T$ formula replaces $q,E$ by $p,F$. Indeed the
other contributions in an $S$ row are its internal edge indicator,
one $S$-to-$T$ unit, two $U/V$ units except at $q$, and the one core
unit at $q$. This accounts for the entire row-four budget.

Each of the sets $N_Z(p)$ and $N_Z(q)$ is a transversal of
the five $U$ classes and also of the five $V$ classes. For example,
$q$ has no defect to any $u_i$, so $\mu(q,u_i)=1$; all such common
neighbors lie in $Z$, giving exactly one in each class. The same
argument applies to $p$ and to the $V$ classes.

Finally let $\epsilon=A_{pq}$ and $\eta=B_{pq}$. Equation (11)
gives $\eta\in\{0,1\}$, and (12) gives the exact overlap
$$|N_A(p)\cap N_A(q)|=|N_Z(p)\cap N_Z(q)|
=1+\eta-\epsilon. \tag{17}$$
All four pairs $(\epsilon,\eta)\in\{0,1\}^2$ remain in this note;
their overlap sizes are respectively $1,2,0,1$ in the order
$(0,0),(0,1),(1,0),(1,1)$. This is not a claim that each is realizable.

## 5. Compatible finite normalizations for a full graph model

There are exactly seven independent row/column permutation types of
$C$. Indeed view its entries as multiplicities of edges of a bipartite
multigraph on $U,V$. Every degree is two. Each component is an even
cycle, including a pair of parallel edges as a cycle of length two.
Alternating colors around each component decomposes $C$ into two
perfect matchings. Independent labels on $U,V$ make one matching the
identity, leaving
$$C=I_5+P_\sigma.$$
The remaining simultaneous relabeling conjugates $\sigma$. Its cycle
type is one of the seven partitions
$$5;\quad4+1;\quad3+2;\quad3+1+1;\quad2+2+1;
\quad2+1+1+1;\quad1+1+1+1+1.$$
Conversely the cycle lengths of the bipartite components distinguish
these seven types. This is a mathematical classification of this
small weighted interface, not of the whole graph. It is legitimate
here because $A[U,V]=0$: there is no independently fixed $A$ matching
requiring the two labelings to agree.

For each type, assign the $35$ point labels of $Z$ to cells of the
fixed sizes $1+C_{ij}$. Every actual graph admits this assignment,
because (10) was derived from its actual common neighborhoods.
Permutation of the labels within each cell remains free.

There is a further compatible labeling. For $u_i\in U$, commutation
at $(s,u_i)$ yields
$$\sum_{x\in S}B_{x,u_i}
=(AB)_{s,u_i}=(BA)_{s,u_i}=1.$$
On the right only the term $A_{u,u_i}$ is nonzero; the vertices
$v,t,p$ have no $U$ neighbor. The equation at $(t,u_i)$ gives one
unit from $T$. Interchanging $u,v$ gives the same statement for each
$V$ point. In conjunction with (7), the four defect interfaces
$$S\setminus\{q\}\longleftrightarrow U,\quad
S\setminus\{q\}\longleftrightarrow V,\quad
T\setminus\{p\}\longleftrightarrow U,\quad
T\setminus\{p\}\longleftrightarrow V$$
are all perfect matchings. Therefore, after fixing $U,V,C$, one can
independently label $S\setminus\{q\}$ and $T\setminus\{p\}$ by
their unique defect endpoints in $U$. Their defect matchings to $V$
must remain variable. No pattern of $K=A[S,T]$ is fixed by this step.

Likewise the $Z$ transversal belonging to $q$ must remain variable:
the $V$ labeling was already used to normalize $C$, so this argument
does not also make that transversal the identity permutation.

## Remaining obligation and non-claims

The original adjacent-double question has been reduced to a full
partition, fixed layer degrees, two coupled cell matrices (10),(12),
the seven-edge interface $K$, and the port identities (13)–(17).
The incidence assignments and the actual four-regular graph on $Z$
are still free subject to the original same-$A$ coverage conditions.
These conditions are necessary, not a sufficiency theorem or an
executed finite classification. They do not yet exclude adjacent
double defects, binary defect, or order $61$ itself.
