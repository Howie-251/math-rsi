# Adjacent double defect: port propagation inside the 35-point layer

## Claim, status, and dependencies

**PROVABLE AS STATED: necessary propagation constraints.** In the actual
adjacent-double template of
[ADJACENT_DOUBLE_REPEAT_LOCAL.md](ADJACENT_DOUBLE_REPEAT_LOCAL.md),
the overlap of the $S$–$T$ adjacency interface $K$ and defect matching
$P$ is confined to $(q,p)$. Moreover every $S$ color class and every $T$ color class
in $Z$ is independent in $A[Z]$, with no exceptional edge retained.
These conclusions do not exclude any of the four values of
$(\epsilon,\eta)=(A_{pq},B_{pq})$ by themselves.

We use only the proved local identities and connected positive support
of the actual $B=A^2+A-7I-J$. The source
[ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md](ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md)
fixes no additional hypothesis here. No solver, enumeration, or MCP
call was made for this derivation.

## Notation and inherited exact identities

Retain all vertex names from the local proof. For $z\in Z$, write
$x(z)\in S$ and $y(z)\in T$ for its unique parents. Put
$$Z^S_x=\{z\in Z:x(z)=x\},\qquad
Z^T_y=\{z\in Z:y(z)=y\}.$$
Let $K=A[S,T]$, let $P=B[S,T]$ be its independently variable defect
permutation matrix, and let
$$\beta_{xz}=B_{xz}\ (x\in S),\qquad
\gamma_{yz}=B_{yz}\ (y\in T).$$
These entries are binary, with exact column sums
$$\sum_{x\in S}\beta_{xz}=1_{y(z)=p},\qquad
\sum_{y\in T}\gamma_{yz}=1_{x(z)=q}. \tag{1}$$
Set $E=N_A(p)\cap S$, $F=N_A(q)\cap T$, each of size two. The
exact row sums, inherited from local equation (16), are
$$\sum_z\beta_{xz}=1+1_{x=q}-1_{x\in E},\qquad
\sum_z\gamma_{yz}=1+1_{y=p}-1_{y\in F}. \tag{2}$$
In particular $q\in E$ and $p\in F$ hold precisely when
$\epsilon=1$. The number of points in each parent cell is
$$|Z^S_x\cap Z^T_y|=1-K_{xy}+P_{xy}. \tag{3}$$

## 1. Exact colored neighbor counts

The full neighborhood of $x\in S$ is its core parent $s$, its
$K$ neighbors in $T$, and $Z^S_x$. Since $z\in Z$ is not adjacent
to $s$ and has exactly one $T$ parent, its common neighbors with
$x$ number
$$\mu(x,z)=K_{x,y(z)}+d_{Z^S_x}(z).$$
Combining this with the actual defect identity gives
$$d_{Z^S_x}(z)=1+\beta_{xz}-1_{x=x(z)}-K_{x,y(z)}. \tag{4}$$
The same direct calculation with $T$ gives
$$d_{Z^T_y}(z)=1+\gamma_{yz}-1_{y=y(z)}-K_{x(z),y}. \tag{5}$$
These are exact integer counts on the same $A$; the port variables
in (1) cannot be assigned independently of these equalities.

## 2. The only possible triangle using an S–T edge

Suppose a point $z$ lies in a cell with $K_{x(z),y(z)}=1$.
The triangle $x(z),y(z),z$ implies $\beta_{x(z),z}\geq1$.
Equation (1) then forces $y(z)=p$. Its $T$ version forces
$x(z)=q$. Thus every such triangle is $q,p,z$.

For an edge $K_{xy}=1$, equation (3) gives precisely $P_{xy}$
common $Z$ neighbors. Therefore
$$K_{xy}P_{xy}=0\quad\text{unless }(x,y)=(q,p). \tag{6}$$
If $\epsilon=\eta=1$, the $(q,p)$ cell has one point and its
triangle with $q,p$ is forced. If either bit is zero, there is no
triangle using an $S$–$T$ edge.

## 3. No Z edge can share an S or T parent

First suppose $zz'\in E(A[Z])$ and $x(z)=x(z')=x$. The triangle
$xzz'$ gives $\beta_{xz},\beta_{xz'}\geq1$. Equation (1) forces
$y(z)=y(z')=p$. At least two units are needed in row $x$ of
$\beta$. By (2) the only possibility is
$$x=q,\qquad q\notin E,\qquad \epsilon=0.$$
There are at least two points in the $(q,p)$ cell. By (3), its size
is $1+\eta$, so $\eta=1$ and $z,z'$ are exactly its two points.
Applying the same argument from a shared $T$ parent exchanges
$S,q$ with $T,p$ and reaches this identical exceptional case.

That potential exception is also impossible by connectedness.
When $\epsilon=0,\eta=1$, equation (2) says that the entire
$q$-to-$Z$ row and the entire $p$-to-$Z$ row each have weight two.
The two triangles already give all four entries
$B_{qz}=B_{qz'}=B_{pz}=B_{pz'}=1$. The adjacent pair $z,z'$
has common neighbors $q,p$, so its double entry and row budget give
$B_{zz'}=2$ and no further defect entries. The complete eight rows
are therefore
$$\begin{aligned}
B_{u*}&=2e_v^T+e_s^T+e_t^T,&
B_{v*}&=2e_u^T+e_s^T+e_t^T,\\
B_{s*}&=e_u^T+e_v^T+e_t^T+e_p^T,&
B_{t*}&=e_u^T+e_v^T+e_s^T+e_q^T,\\
B_{q*}&=e_t^T+e_p^T+e_z^T+e_{z'}^T,&
B_{p*}&=e_s^T+e_q^T+e_z^T+e_{z'}^T,\\
B_{z*}&=2e_{z'}^T+e_q^T+e_p^T,&
B_{z'*}&=2e_z^T+e_q^T+e_p^T.
\end{aligned} \tag{7}$$
All eight vertices are distinct, and every row is saturated inside
this proper eight-vertex set. This contradicts connected positive
support of $B$. Hence
$$A[Z^S_x]=0\quad(x\in S),\qquad
A[Z^T_y]=0\quad(y\in T). \tag{8}$$
This excludes the exceptional **edge**, not the parameter case
$\epsilon=0,\eta=1$. That case still has two nonadjacent points
in its $(q,p)$ cell.

## 4. Consequences for colors, triangles, and finite interfaces

Taking the own-parent entries in (4),(5) and using (8) gives
$$\beta_{x(z),z}=\gamma_{y(z),z}=K_{x(z),y(z)}. \tag{9}$$
Thus a port can meet its own $A$ parent only at the unique triangle
of the $\epsilon=\eta=1$ case. Every ordinary point of $S$ or $T$
is triangle-free. The points $q,p$ are also triangle-free unless
$\epsilon=\eta=1$, in which case each lies in exactly the one
triangle with the unique point in their common cell. To check that
this exhausts their triangles, their neighborhoods consist only of
the core parent, $K$ neighbors, and one color class in $Z$: the core
parent has no edges to the other two parts, the $K$ neighbors lie in
an independent set, (8) excludes edges inside the color class, and
Section 2 handles every remaining cross edge.

The equalities (4),(5) also specify the possible neighbor color
multisets of the four-regular graph $A[Z]$. If $y(z)\ne p$, its
$K$ column has one neighbor $\kappa\in S$ and its port column
$\beta_{*z}$ is zero. Necessarily $\kappa\ne x(z)$ by (6).
Its four neighbors have one of each of the four $S$ colors outside
$\{x(z),\kappa\}$.

If $y(z)=p$, its port column has one unit at some $\phi(z)\in S$.
In this case (4) becomes
$$d_{Z^S_x}(z)=1+1_{x=\phi(z)}-1_{x=x(z)}-1_{x\in E}. \tag{10}$$
No ordinary member of $E$ can be $\phi(z)$ by (2). If
$\epsilon=0$, neither member of $E$ is $q$, so all five points
of $N_Z(p)$ have one repeated neighbor $S$ color and two other
neighbor $S$ colors, with multiplicities $2,1,1$. If $\epsilon=1$,
exactly one of these five port columns has its unit at $q$; its four
neighbor colors are distinct, while the other four columns have
multiplicities $2,1,1$. This follows directly from (9),(10): a port
outside $E$ differs from the own parent and raises one existing
neighbor-color count from one to two. The unique port at $q\in E$
instead supplies the fourth distinct color, including when the
own parent is $q$ in the forced triangle.

Consequently exactly $5-\epsilon$ vertices of $Z$ have a repeated
$S$ color among their four neighbors; all others have four distinct
neighbor $S$ colors. Exchanging $S,p$ with $T,q$ proves the identical
count for $T$ colors. These are counts of actual neighbor incidences,
not of isomorphism types or candidate graphs.

## Remaining scope

A complete implementation may retain all four $(\epsilon,\eta)$
cases while imposing (1)–(6), (8)–(10), the original row sums (2),
and the existing $U/V$ color constraints. Every deduction above is
necessary for the original full graph and introduces no new symmetry
assumption. The $Z$ graph and compatible incidence maps remain to be
found or excluded. In particular triangles wholly inside $Z$ have
not been prohibited, and this note is not an adjacent-double or
order-61 exclusion.
