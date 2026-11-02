# D1 heavy and generated-triangle components have at least twelve vertices

## Claim and status

**PROVABLE AS STATED, new paper derivation awaiting independent review.**
For any D1 double edge, let $H$ be its component in the positive support
of $B$, and let $K$ contain its generated unit triangle. Then

$$|H|\ge12,\qquad |K|\ge12.$$

If $|K|=12$, then $|H|=12$, the original graph has four neighbors per
vertex in each direction between these components, and their original
internal degrees are zero and one in some order.

The five possible size/incidence triples when $|H|=12$ are listed below.
None of these remaining cases is excluded here, so this does not finish
the order-62 problem.

## Assumptions, notation, and dependencies

Use the actual order-62 graph and matrix identities in
`RECOVERED_REDUCTION.md`, the D1 rows in
`D1_MATCH_HARD_BRANCH_REDUCTION.md`, and $B_{pq}=0$ from
`D1_MATCH_C4_TRANSPORT_REFINEMENT.md`.

Use the component equitability and D1 incidence bounds established in
`GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`: if $C_i$ has size $n_i$, every
vertex in $C_i$ has $r_{ij}$ original neighbors in $C_j$, and

$$\sum_j r_{ij}=8,\qquad n_i r_{ij}=n_j r_{ji},\qquad
 R^2+R=10I+\mathbf1 n^T. \tag{1}$$

All component sizes are even. For the D1 components $H,K$, if they
differ, write

$$h=|H|,\quad k=|K|,\quad a=r_{HK}\ge4,\quad b=r_{KH}\ge3.$$

Then $ha=kb$. If $H=K$, its original internal degree is at least four.
All original degrees are eight. Across two different components of $B$,
the actual identity is $c(x,y)+A_{xy}=1$.

## Proof strategy

The local D1 rows first give $h\ge8$. An exact common-neighbor budget
then reduces $h=8$ and $h=10$ to very few integer possibilities. Counting
actual neighbors outside the two components excludes those possibilities.
The same budget gives $k\ge12$ and a precise restriction when $k=12$.

## 1. A nonnegative common-neighbor budget

For a component $C_i$ of size $n_i$, count common neighbors of its
unordered vertex pairs. Since its total unordered repeat weight is
$3n_i/2$ and its original internal edge count is $n_i r_{ii}/2$,

$$\sum_j n_j\binom{r_{ji}}2
 =\binom{n_i}2+\frac{3n_i}2-\frac{n_i r_{ii}}2
 =\frac{n_i(n_i+2-r_{ii})}2. \tag{2}$$

Using balance in (1), this becomes

$$\boxed{\sum_j r_{ij}(r_{ji}-1)=n_i+2-r_{ii}}. \tag{3}$$

Every summand is nonnegative. For an off-diagonal entry, positive
$r_{ij}$ implies positive integer $r_{ji}$ by balance. The diagonal
term is $r_{ii}(r_{ii}-1)$.

Consequently, if a component has internal original degree $t$,

$$n_i\ge t^2-2. \tag{4}$$

If $H=K$, this gives $h\ge14$. If $H\ne K$, it gives the two inequalities

$$a(b-1)\le h+2-r_{HH},\qquad
 b(a-1)\le k+2-r_{KK}. \tag{5}$$

This use of nonnegative summands is stronger than merely retaining one
term of the diagonal equation for $R^2$.

## 2. The heavy component has at least eight vertices

The normalized D1 rows are

$$B_0=2e_w+e_a,\quad B_w=2e_0+e_r,\quad
 B_a=e_0+e_p+e_q,\quad B_r=e_w+e_s+e_t.$$

The vertices $0,w,a,r,p,q$ are distinct, and $B_{ar}=B_{pq}=0$.
All six belong to $H$. If they were the whole component, the two
remaining unit entries of row $r$ would have to go to $p,q$: the
rows at $0,w$ are exhausted and $B_{ar}=0$. The rows at $a,r$ would
then both be exhausted. Row $p$ already contains its two units to
$a,r$, and its last unit would have to go to $q$, contradicting
$B_{pq}=0$. Thus $|H|>6$, and evenness gives $h\ge8$.

## 3. Size eight is impossible

If $h=8$, (4) rules out $H=K$. The first inequality in (5) implies

$$a(b-1)\le10.$$

Together with $a\ge4,b\ge3$, this leaves $b=3$ and $a\in\{4,5\}$.
But balance would give $k=8a/3$, which is not an integer for either
value. Thus $h\ne8$.

## 4. Size ten is impossible

Suppose $h=10$. Again $H\ne K$ by (4). The inequality
$a(b-1)\le12$ gives either $b=3$, $4\le a\le6$, or $(a,b)=(4,4)$.
Balance $k=10a/b$ leaves exactly

$$ (k,a,b)=(10,4,4)\quad\text{or}\quad(20,6,3). \tag{6}$$

In both cases $a(b-1)=12$, so (5) forces $r_{HH}=0$. Moreover the
vertices of $K$ exhaust the entire common-neighbor budget (2) for
pairs in $H$. Therefore every vertex outside $K$ has at most one
original neighbor in $H$.

### 4.1. The ten-by-ten case

If $(k,a,b)=(10,4,4)$, the reverse budget also forces $r_{KK}=0$
and every vertex outside $H$ has at most one neighbor in $K$.

There are 100 pairs with one vertex in each component, exactly 40
of which are original edges. Since their repeat entries vanish,
the total number of common neighbors over these pairs is 60.
The two components are internally independent, so these common
neighbors must lie among the other 42 vertices. Each such vertex
has at most one neighbor in each component, and hence contributes
at most one. This gives $60\le42$, a contradiction.

### 4.2. The ten-by-twenty case

Suppose $(k,a,b)=(20,6,3)$, and put $t=r_{KK}$. Each vertex outside
$K$ has at most one neighbor in $H$. Since $H$ is internally
independent and has 60 edges to $K$, its remaining 20 incidences
give exactly 20 distinct vertices $X$ outside $H\cup K$, each with
one neighbor in $H$. Let $Y$ be the other 12 vertices. The values
of $d_H(v)=|N(v)\cap H|$ on the four sets are therefore

$$d_H|_H=0,\qquad d_H|_K=3,\qquad
 d_H|_X=1,\qquad d_H|_Y=0. \tag{7}$$

There are 200 pairs in $H\times K$ and 60 original edges between
the components. Thus their total common-neighbor count is 140.
The contribution from $K$ is $20\cdot3t=60t$, and that from $X$
is the number of edges between $X$ and $K$. The other two sets
contribute zero. Hence

$$e(X,K)=140-60t.$$

The degree sum on $K$ now gives

$$e(Y,K)=160-60-20t-e(X,K)=40(t-1). \tag{8}$$

For each $y\in Y$ and every $u\in H$, the pair is nonadjacent and
has repeat entry zero, so $c(u,y)=1$. Summing over $u\in H$ and
using (7) gives

$$3d_K(y)+d_X(y)=10.$$

As $y$ has only eight neighbors, this implies $1\le d_K(y)\le3$.
Summing over the 12 vertices of $Y$ gives

$$12\le e(Y,K)\le36,$$

which contradicts (8), since $40(t-1)$ is a multiple of 40.

Both cases in (6) are impossible. Component sizes are even, so

$$\boxed{h\ge12}. \tag{9}$$

## 5. The generated-triangle component also has at least twelve vertices

If $H=K$, (4) already gives $k\ge14$. Otherwise suppose $k\le10$.
Substitute $b=ha/k$ into the first inequality of (5), and drop the
nonnegative $r_{HH}$:

$$h(a^2-k)\le k(a+2).$$

For $a\ge4$ and $k\le10$,

$$a^2-k\ge a^2-10\ge a+2,$$

where the second inequality is $(a-4)(a+3)\ge0$. Thus $h\le k\le10$,
contrary to (9). Evenness now gives

$$\boxed{k\ge12}. \tag{10}$$

## 6. A twelve-vertex generated component has a twelve-vertex heavy partner

Suppose $k=12$. The components differ by (4). The second inequality
of (5) gives $b(a-1)\le14$. With $a\ge4,b\ge3$, the only pairs are

$$ (a,b)=(4,3),(4,4),(5,3).$$

Balance $h=12b/a$, integrality, and $h\ge12$ leave only

$$h=k=12,\qquad a=b=4. \tag{11}$$

Write $\alpha=r_{HH}$ and $\beta=r_{KK}$. Keeping the diagonal term
in (3) gives $\alpha^2\le2$ and $\beta^2\le2$, so each lies in
$\{0,1\}$.

For every one of the other 38 vertices $v$, put
$x_v=d_H(v)$ and $y_v=d_K(v)$. The degree and common-neighbor
identities give

$$\begin{aligned}
\sum x_v&=48-12\alpha,& \sum y_v&=48-12\beta,\\
\sum x_v^2&=72-24\alpha,& \sum y_v^2&=72-24\beta,\\
\sum x_vy_v&=96-48(\alpha+\beta).
\end{aligned} \tag{12}$$

For example, the last equality counts common neighbors of pairs in
$H\times K$. There are $144-48=96$ in total, of which the internal
vertices contribute $48\alpha+48\beta$. The square identities follow
by doubling (2), adding the total neighbor incidence, and removing
the contributions inside $H\cup K$.

If $\alpha=\beta=0$, the pointwise inequality
$2x_vy_v\le x_v^2+y_v^2$ gives $\sum x_vy_v\le72$, contradicting
the value 96 in (12).

If $\alpha=\beta=1$, then $\sum x_vy_v=0$. However,
$\sum x_v=36$ and $\sum\binom{x_v}{2}=6$. For a positive integer
$x$, $x-1\le\binom{x}{2}$, so at least 30 of the 38 vertices have
$x_v>0$. At least 30 also have $y_v>0$. The two supports intersect,
contradicting the zero cross sum. Therefore

$$\boxed{\{\alpha,\beta\}=\{0,1\}}. \tag{13}$$

## 7. The remaining size-twelve heavy-component list

If $h=12$, then $H\ne K$ by (4), and $a(b-1)\le14$. The possibilities
are $b=3$, $a\in\{4,5,6,7\}$, or $(a,b)=(4,4)$. Balance gives exactly

$$\boxed{(k,a,b)\in
\{(12,4,4),(16,4,3),(20,5,3),(24,6,3),(28,7,3)\}}. \tag{14}$$

The first alternative additionally satisfies (13). Equation (14) is
an exact list of necessary size/incidence triples, not a list of
realizable component pairs.

## 8. General exterior moment constraints for subsequent use

For any two distinct components $C,D$, write
$h=|C|$, $k=|D|$, $a=r_{CD}$, $b=r_{DC}$,
$\alpha=r_{CC}$, $\beta=r_{DD}$, with $ha=kb$. On the other
$N=62-h-k$ vertices define $x_v=d_C(v)$ and $y_v=d_D(v)$. Exact
degree and common-neighbor counting gives

$$\begin{aligned}
S_x:=\sum x_v&=h(8-\alpha-a),\\
S_y:=\sum y_v&=k(8-\beta-b),\\
Q_x:=\sum x_v^2&=h(h+10-\alpha-\alpha^2)-kb^2,\\
Q_y:=\sum y_v^2&=k(k+10-\beta-\beta^2)-ha^2,\\
Q_{xy}:=\sum x_vy_v&=h\bigl(k-a(1+\alpha+\beta)\bigr).
\end{aligned} \tag{15}$$

In particular the actual Gram matrix

$$\begin{pmatrix}
N&S_x&S_y\\ S_x&Q_x&Q_{xy}\\ S_y&Q_{xy}&Q_y
\end{pmatrix}$$

is positive semidefinite. Also $x_v,y_v$ are nonnegative integers
with $x_v+y_v\le8$. Summing common-neighbor counts from an exterior
vertex $v$ into $C$ gives

$$\sum_{u\in N(v)}d_C(u)=h-x_v.$$

The neighbors in $C$ and $D$ contribute $\alpha x_v+b y_v$ and
all other contributions are nonnegative. Applying the same argument
to $D$ gives the pointwise restrictions

$$ (\alpha+1)x_v+b y_v\le h,\qquad
 a x_v+(\beta+1)y_v\le k. \tag{16}$$

Each exterior component has a constant pair $(x_v,y_v)$ and even
size. Consequently the total number of exterior vertices of each
such type is even. These are necessary conditions on actual
component pairs; no independent matrix model or enumeration is used.

## Remaining gap

The minimum-size and exterior-moment bounds do not yet exclude the
five cases (14), larger component pairs, or the case $H=K$. They do
not establish evenness of the number of double edges in a component.
The input component quotient paper and this new derivation require
their separate independent reviews before being treated as reviewed
research conclusions.
