# Nongenerated triangle witnesses avoid heavy endpoints

## Claim and status

**PROVABLE AS STATED:** under connected repeat support, every original
common-neighbor witness of a pair in a nongenerated unit repeat triangle
lies outside the heavy endpoint set. The consequences below sharpen
the type-one center, mixed-trace, port, and diamond constraints.

This is a new paper proof awaiting independent review. It excludes one
specific configuration when $d=9$, not that value of $d$ itself, and
does not exclude either nongenerated triangle type in general.

## Assumptions, notation, and dependencies

Use the actual order-62 graph, connected repeat support, triangle-free
original graph, and all-D1 double-repeat reduction as in
`CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md`. Write $A$ for the original
adjacency matrix and $B=A^2+A-7I-J$ for its actual repeat matrix. The
rows of $A$ sum to eight, those of $B$ to three, and $AB=BA$.

Let $d$ count double repeats, $D$ be their $2d$ endpoints, and
$S_{\rm gen}$ the $3d$ generated-triangle vertices. Let $U$ contain
all unit-triangle vertices and put

$$v_{\rm extra}=|U\setminus S_{\rm gen}|,\qquad
W=V(G)\setminus(D\cup S_{\rm gen}).$$

A unit triangle is type $i$ if its three vertices have exactly $i$
common original neighbors, for $i=0,1,2$. Type two is precisely the
generated case. Generated triangles are disjoint from every other unit
triangle. Every type-one triangle $T$ has a unique center $c(T)$,
and distinct type-one triangles have distinct centers, by the cited
triangle-pattern paper. Write

$$t_1=|\{T:T\text{ has type one}\}|,\quad
C_1=\{c(T):T\text{ has type one}\},\quad
U_1=\bigcup_{T\text{ of type one}}T,\quad
c_{\rm out}=|C_1\setminus U|.$$

Thus $|C_1|=t_1$. A center is outside its own triangle.

For $w\in W$, let $m(w)$ count original edges among its three unit
repeat neighbors, let $\ell(w)$ count its heavy repeat neighbors,
and let $L_3=|\{w\in W:\ell(w)=3\}|$. The identities proved in
`CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md` give

$$\tau:=\operatorname{tr}(AB^2)=2\sum_{w\in W}m(w),\quad
\sum_{w\in W}\ell(w)=2d,\quad
m(w)\le2-\ell(w)+\mathbf1_{\ell(w)=3}. \tag{1}$$

The D1 root parent description is from
`D1_MATCH_HARD_BRANCH_REDUCTION.md`; its light-mate facts are from
`D1_MATCH_C4_TRANSPORT_REFINEMENT.md`. No finite search is used.

## Proof strategy

First determine the entire repeat restriction to an actual heavy
endpoint's original neighborhood. Then apply the established separation
of generated triangles. At type-one centers, commutation makes the
center isolated in each witness's repeat neighborhood, improving both
packing and mixed-trace counts. Finally track the symmetric relation
between a type-one triangle and triangles containing its center.

## 1. The exact heavy-root neighborhood restriction

Let $u\in D$. In its normalized D1 representation, $X=N_G(u)$ is
independent; the exceptional vertex $w$ has parent triple $\{1,2,3\}$
and the exceptional vertex $a$ has parent pair $\{1,4\}$. All other
vertices outside $X\cup\{u\}$ have exactly one parent in $X$.

For distinct $x,y\in X$, their common original neighbors consist of
$u$ and precisely those exceptional vertices whose parent sets contain
both. No vertex in $X$ is an additional common neighbor, since $X$
is independent. Thus the common-neighbor identity gives the complete
restriction

$$\boxed{B[X]\text{ is the unit triangle }123
\text{ together with the unit edge }14
\text{ and four isolated vertices}.} \tag{2}$$

In particular every positive repeat pair inside $X$ meets the generated
triangle $\{1,2,3\}$ of this heavy pair.

Let $T$ be any nongenerated unit triangle. It is disjoint from every
generated triangle. If two of its vertices were both in $N_G(u)$,
their positive repeat would contradict (2). Therefore

$$\boxed{|N_G(u)\cap T|\le1\quad(u\in D).} \tag{3}$$

Equivalently, every common original neighbor of any pair in $T$ lies
outside $D$. This applies to all six witnesses of a type-zero triangle
and all four witnesses of a type-one triangle. It does not assert that
these witnesses all avoid generated-triangle vertices.

For a unit diamond, the same argument says that a heavy endpoint's
neighbors inside its four vertices form an independent set of the
diamond: it can meet at most two vertices, and a two-vertex intersection
must consist of the two nonadjacent tips.

## 2. A type-one center has no heavy repeat neighbor

Write a type-one triangle as $T=\{x,y,z\}$ with center $u$, and write
its other pair witnesses as

$$N(x)\cap N(y)=\{u,a\},\quad
N(y)\cap N(z)=\{u,b\},\quad
N(z)\cap N(x)=\{u,c\}.$$

The established complete row is

$$B_u=e_a+e_b+e_c. \tag{4}$$

By (3), $a,b,c\notin D$. They are pairwise nonadjacent in the
original graph, since each pair shares a neighbor in $T$. Hence

$$\boxed{\ell(u)=0,\qquad m(u)=0.} \tag{5}$$

In particular $u$ cannot be a light mate of any heavy endpoint.

There is a further consequence of commutation. For a witness $a$,
the independent set $\{a,b,c\}$ gives

$$0=(AB)_{au}=(BA)_{au}=\sum_v B_{av}A_{vu}.$$

Nonnegativity shows that every repeat neighbor of $a$ is an original
nonneighbor of $u$. The same holds for $b$ and $c$. Since
$T\subseteq N_G(u)$, no positive repeat joins any of $a,b,c$ to any
vertex of $T$. Also $B_{u,T}=0$ because those are original edges.
Thus

$$\boxed{B[\{u,a,b,c\},T]=0.} \tag{6}$$

Equivalently, $u$ is isolated in the original graph induced on each
witness's repeat neighborhood. Each of $a,b,c$ has three unit repeat
neighbors by (3), so each has at most one original edge among them.

At $x\in T$, its repeat row consists of $y,z$ and one external port
$p_x$. The only possible original edges among these three neighbors
join $p_x$ to $y$ or $z$. If both occurred, $p_x$ would be one of the
two pair witnesses $u,b$, contradicting (6) and $B_{xp_x}=1$.
Consequently

$$\boxed{m(v)\le1\quad(v\in U_1).} \tag{7}$$

Moreover $\ell(v)=0$ for every $v\in U$: a heavy repeat neighbor would
make $v$ a D1 light mate, and such a mate lies on no unit triangle.

## 3. Strengthened packing and mixed trace

Heavy endpoints' $2d$ unit incidences end outside $D$, outside $U$,
and outside $C_1$ by (5). The union $U\cup C_1$ has size
$3d+v_{\rm extra}+c_{\rm out}$. Row capacity three therefore gives

$$2d\le3\bigl(62-5d-v_{\rm extra}-c_{\rm out}\bigr),$$

or

$$\boxed{17d+3v_{\rm extra}+3c_{\rm out}\le186.} \tag{8}$$

For the mixed trace, every center in $C_1$ has $\ell=0$ and $m=0$,
improving the local upper bound in (1) by two. Every vertex in
$U_1\setminus C_1$ has $\ell=0$ and $m\le1$, improving it by one.
These two sets are disjoint. Summing (1) with these improvements yields

$$\boxed{\tau+4t_1+2|U_1\setminus C_1|
\le248-24d+2L_3.} \tag{9}$$

No assumption about intersections between witnesses of different
triangles enters this count.

## 4. The graph of type-one centers

Define a simple graph $\Gamma$ whose vertices are the type-one unit
triangles, with $T$ adjacent to $T'$ if $c(T)\in T'$. This relation
is symmetric. Indeed in the notation (4), any unit triangle containing
$u=c(T)$ uses two vertices among $a,b,c$. A triangle $\{u,a,b\}$
has exactly the common original neighbor $y\in T$; the other two
choices have center $x$ or $z$. Thus

$$c(T)\in T'\quad\Longleftrightarrow\quad c(T')\in T. \tag{10}$$

Every adjacent pair $T,T'$ in $\Gamma$ consists of disjoint unit
triangles: $T'$ is formed from witnesses lying outside $T$.
This does not say that two different neighbors of $T$ are disjoint.
In fact, if $T$ has two neighbors, both contain $c(T)$, so they are
the two overlapping triangles of a single diamond. Since no vertex
lies on more than two unit triangles, every degree in $\Gamma$ is
at most two. Its isolated vertices correspond exactly to centers
outside $U$, so their number is $c_{\rm out}$.

Every component of $\Gamma$ is one of

$$\boxed{K_1,\ K_2,\ P_3,\ P_4,\ C_4,} \tag{11}$$

where the subscript is the number of vertices. Here is the complete
length argument. In any path with consecutive vertices
$T_0,T_1,T_2,T_3,T_4$, the pairs $T_0,T_2$ and $T_2,T_4$ each
overlap because they are the two neighbors of an interior vertex.
This would place three distinct triangles in one overlap cluster,
whereas a cluster contains at most the two triangles of a diamond.
Thus a path has at most four vertices. A three-cycle is impossible:
two neighbors of one vertex would overlap, but they would also be
adjacent in $\Gamma$ and hence disjoint. A cycle of length at least
five has the same forbidden five consecutive vertices. Only a
four-cycle remains.

There are two useful refinements. In a $P_3$ component, the middle
triangle is an isolated unit-triangle cluster. To prove this, let its
two neighbors be $T',T''$. Their distinct centers lie in the middle
triangle by (10). If the middle triangle overlapped another triangle
$Q$, only one of its three vertices would lie outside $Q$. Thus at
least one of those two centers would belong to $Q$. The triangle $Q$
would be type one by the same center argument, giving an additional
edge from $T'$ or $T''$, contrary to that component being $P_3$.

In a $P_4$ or $C_4$ component, the four triangle vertices belong to
exactly two diamond clusters: the triangles in positions zero and
two form one diamond, and those in positions one and three the other.
They cannot all lie in one cluster, which contains at most two
triangles.

## 5. A specific restriction when there are nine double repeats

When $d=9$, (8) gives

$$v_{\rm extra}+c_{\rm out}\le11. \tag{12}$$

Suppose $v_{\rm extra}=11$. Writing the nongenerated overlap clusters
as $s$ isolated triangles and $k$ diamonds gives $3s+4k=11$, whose
unique nonnegative integer solution is $s=1,k=2$. Equation (12)
also forces $c_{\rm out}=0$.

These five triangles cannot all be type one. Otherwise $\Gamma$ would
have five vertices and no isolated vertex. By (11), its only possible
component-size decomposition would be $3+2$, namely $P_3$ and $K_2$.
The middle of the $P_3$ must be the sole isolated unit triangle;
its two neighbors constitute a whole diamond. The remaining two
triangles are the two overlapping triangles of the other diamond.
They cannot form a $K_2$ in $\Gamma$, whose adjacent triangles are
disjoint. This contradiction proves

$$\boxed{d=9,\ v_{\rm extra}=11
\ \Longrightarrow\ \text{at least one nongenerated triangle is type zero}.}
\tag{13}$$

For another direct consequence, the existing mixed-trace identity is
$\tau=10c_5-24976$ at $d=9$. Its nonnegative permitted values start
at four and differ by ten. Since $L_3\le6$, (9) shows that if a
type-one triangle exists, then $\tau<44$ and therefore
$c_5\le2501$, improving the earlier upper bound $2502$ in this case.
Neither consequence excludes $d=9$.

## 6. Exact diamond matching and tip restriction

Let a unit diamond have shared-edge endpoints $x,y$ and tips $z,w$.
Its rows at the shared endpoints are

$$B_x=e_y+e_z+e_w,\qquad B_y=e_x+e_z+e_w.$$

For $f=e_x-e_y$, this gives $Bf=-f$ and hence, because $Jf=0$,

$$A^2f+Af=6f. \tag{14}$$

Put $X=N_G(x)\setminus N_G(y)$ and
$Y=N_G(y)\setminus N_G(x)$. The two common neighbors of $x,y$
give $|X|=|Y|=6$. Both sets are independent in $G$, and
$Af=\mathbf1_X-\mathbf1_Y=:r$. Equation (14) says $Ar=6f-r$.
At a vertex of $X$, its left side is minus its number of neighbors
in $Y$, while its right side is minus one. At a vertex of $Y$ the
corresponding equation gives exactly one neighbor in $X$. Thus

$$\boxed{G[X,Y]\text{ is a perfect matching}.} \tag{15}$$

Every vertex outside $X\cup Y\cup\{x,y\}$ has equally many original
neighbors in $X$ and $Y$.

Write the remaining diamond rows as

$$B_z=e_x+e_y+e_p,\qquad B_w=e_x+e_y+e_q.$$

The ports $p,q$ lie outside the diamond but may coincide. Commutation
at $(x,z),(y,z),(x,w),(y,w)$ gives

$$A_{xp}=A_{yp}=A_{zw},\qquad
  A_{xq}=A_{yq}=A_{zw}. \tag{16}$$

If the tips are originally adjacent, then the repeat neighborhood
$\{x,y,p\}$ of $z$ has the two original edges $xp,yp$, so $m(z)=2$.
The bound (7) rules out type one for the triangle $\{x,y,z\}$.
The same argument at $w$ rules out type one for $\{x,y,w\}$.
Neither triangle is generated, since it overlaps the other. Hence

$$\boxed{z\sim_G w\quad\Longrightarrow\quad
\text{both diamond triangles have type zero}.} \tag{17}$$

This proof treats coincident ports $p=q$ without assuming that two
displayed ports exhaust the common-neighbor set of $x,y$.

## Remaining scope

The witness exclusion does not separate all witnesses from the
generated-triangle vertex set, and witnesses from different triangles
may coincide. The counts retain these possibilities. Type-zero and
type-one triangles, the remaining center-graph components, and the
allowed diamond configurations have not been excluded in general.
No local pattern is claimed to extend to an actual order-62 graph.
