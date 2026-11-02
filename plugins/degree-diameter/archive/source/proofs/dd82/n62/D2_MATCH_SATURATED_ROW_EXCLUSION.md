# Proof Package: saturated rows exclude D2_MATCH at order 62

## Claim

No original degree-at-most-eight, diameter-at-most-two graph on $62$ vertices can realize the D2_MATCH template of `RECOVERED_REDUCTION.md`.

This excludes the entire D2_MATCH branch by a direct argument on the actual adjacency and defect matrices. It does not exclude every order-$62$ graph.

## Status

PROVABLE AS STATED. Complete paper proof, fresh independent PASS26 and Gemini B15 accepted. No SAT result, matrix lifting assumption, finite enumeration, or spectral classification is used inside this branch. The separate recovered coverage theorem retains its own stated dependencies.

## Assumptions and notation

The graph is simple and undirected. The ordinary root count makes it $8$-regular. With adjacency matrix $A$, define

$$B=A^2+A-7I-J.$$

Then $B$ is symmetric and nonnegative integral, has zero diagonal and row sum three, commutes with $A$, and satisfies

$$c(u,v)+A_{uv}=1+B_{uv}\qquad(u\ne v),$$

where $c(u,v)$ counts common neighbors. Also

$$\sum_{v\sim u}B_{uv}=2t(u)\le3,$$

where $t(u)$ counts triangles at $u$.

The D2_MATCH root $0$ has the independent neighborhood $X=\{1,\ldots,8\}$. Outside its closed neighborhood, the exceptional points $w,a$ have parent sets

$$P(w)=\{1,2,3\},\qquad P(a)=\{1,2\},\qquad w\not\sim a.$$

Every other point has one parent in $X$. Denote its singleton-parent class by $C_i$. Thus

$$N_G(1)=\{0,w,a\}\cup C_1,
\quad N_G(2)=\{0,w,a\}\cup C_2,
\quad N_G(3)=\{0,w\}\cup C_3,$$

with

$$|C_1|=|C_2|=5,\qquad |C_3|=6.$$

The other five singleton classes will not need to be analyzed.

## Proof strategy and dependency map

1. The exceptional parent sets saturate four defect rows and force one further repeat into $C_3$.
2. Commutation shows that every repeat row on $C_1$ or $C_2$ is supported entirely in the opposite five-point class and $C_3$.
3. Ordinary common-neighbor counts force a point of $C_3$ with no original neighbor in either five-point class.
4. That point still has a positive defect entry toward $C_1$. Its original matching mate in $C_2$ makes one side of $AB=BA$ positive and the other zero.

## Proof

**Step 1. Four complete defect rows.** The parent sets give

$$B_{0w}=2,\qquad B_{0a}=1,$$

so row $0$ is exactly $2e_w+e_a$.

The common neighbors of $1,2$ are exactly $0,w,a$. The common neighbors of $1,3$ and of $2,3$ are exactly $0,w$. There are no additional common neighbors in $X$, which is independent, or among ordinary singleton-parent vertices. Consequently

$$B_{12}=2,\qquad B_{13}=B_{23}=1.$$

The row sum three therefore gives the complete rows

$$B_1=2e_2+e_3,\qquad B_2=2e_1+e_3.\tag{1}$$

All positive entries in these two rows lie at nonneighbors, so vertices $1,2$ lie in no triangle.

The nonedge pair $w,a$ has the two common neighbors $1,2$, so $B_{wa}\ge1$. Row $w$ already contains $B_{w0}=2$. Thus $B_{wa}=1$ and

$$B_w=2e_0+e_a.\tag{2}$$

Both of these positive entries are at nonneighbors, so $w$ also lies in no triangle.

**Step 2. The third repeat of $a$ lies in $C_3$.** Row $a$ contains the unit entries at $0,w$, and therefore has exactly one further unit endpoint $c$.

At entry $(0,a)$, the complete row of $0$ gives

$$(BA)_{0a}=2A_{wa}+A_{aa}=0.$$

Commutation and nonnegativity imply

$$0=(AB)_{0a}=\sum_{i\in X}B_{ia},$$

so $B_{ia}=0$ for every $i\in X$. Hence $c$ is an ordinary singleton-parent vertex.

At entry $(1,a)$, equations (1)--(2) give

$$2=(BA)_{1a}=(AB)_{1a}
=B_{0a}+B_{wa}+\sum_{x\in C_1}B_{xa}
=2+\sum_{x\in C_1}B_{xa}.$$

Thus $c\notin C_1$. The same calculation with row $2$ gives $c\notin C_2$.

Now $(AB)_{1c}\ge B_{ac}=1$, since $a\sim1$. On the other hand,

$$(BA)_{1c}=2A_{2c}+A_{3c}=A_{3c},$$

because $c\notin C_2$. It follows that $A_{3c}=1$, so

$$c\in C_3,\qquad B_a=e_0+e_w+e_c.\tag{3}$$

The first two endpoints $0,w$ are nonneighbors of $a$. The only remaining possible incident positive entry is a single unit at $c$; the identity $\sum_{v\sim a}B_{av}=2t(a)$ forces $t(a)=0$. In particular

$$a\not\sim c.\tag{4}$$

**Step 3. Vertex $3$ is triangle-free, and has no repeats in $C_1\cup C_2$.** Its row already contains the two unit entries at $1,2$, both at nonneighbors. Its remaining row budget is one, so the same even triangle-budget argument gives $t(3)=0$. Thus $C_3$ is independent in the original graph.

At entry $(1,3)$, equation (1) gives

$$(BA)_{13}=2A_{23}+A_{33}=0.$$

All terms of $(AB)_{13}$ are nonnegative, and this sum includes $\sum_{x\in C_1}B_{x3}$. Therefore $B_{x3}=0$ for every $x\in C_1$. The calculation at $(2,3)$ gives the same statement for $C_2$:

$$B_{3x}=0\qquad(x\in C_1\cup C_2).\tag{5}$$

**Step 4. The complete support location of rows on $C_1,C_2$.** Fix $x\in C_1$. At $(2,x)$, the complete row of $2$ gives $(BA)_{2x}=2$. Rows $0,w,a$ have no positive entry at $x$, by (2)--(3) and the complete row of $0$. Consequently

$$2=(AB)_{2x}=\sum_{y\in C_2}B_{yx}.\tag{6}$$

For $q\in C_3$, commutation at $(1,q)$ gives

$$1=(BA)_{1q}=(AB)_{1q}
=\mathbf1_{\{q=c\}}+\sum_{x\in C_1}B_{xq},$$

and hence

$$\sum_{x\in C_1}B_{xq}=1-\mathbf1_{\{q=c\}}.\tag{7}$$

Here rows $0,w$ vanish at $q$, and row $a$ contributes exactly at $c$.

Summing (7) over the six points of $C_3$ gives five units of defect weight from $C_1$ into $C_3$. By (6), each of the five rows in $C_1$ already spends two of its three units in $C_2$. The remaining total capacity is exactly five. Thus each such row spends its entire remaining unit in $C_3$, with no positive entry anywhere else.

Interchanging $1$ and $2$ proves the symmetric statement. Therefore

$$\operatorname{supp}(B_x)\subseteq C_2\cup C_3\quad(x\in C_1),$$

$$\operatorname{supp}(B_y)\subseteq C_1\cup C_3\quad(y\in C_2),\tag{8}$$

and every row in either five-point class has total defect weight two toward the opposite class and one toward $C_3$. Moreover every $q\in C_3\setminus\{c\}$ has exactly one unit defect endpoint in each of $C_1,C_2$, by (7) and its symmetric counterpart.

**Step 5. Original edges between $C_1,C_2$ form a perfect matching.** For $x\in C_1$, the nonedge pair $2,x$ has $B_{2x}=0$ by (1), and hence exactly one common neighbor. In

$$N_G(2)=\{0,w,a\}\cup C_2,$$

vertex $x$ is adjacent to none of $0,w,a$. Adjacency to $0$ is excluded by its singleton-parent status. Adjacency to either $w$ or $a$ would create a triangle through the triangle-free vertex $1$, since each of $w,a,x$ is adjacent to $1$. Hence $x$ has exactly one neighbor in $C_2$. The symmetric argument gives exactly one neighbor in $C_1$ for every point of $C_2$. These original edges are a perfect matching.

**Step 6. A point of $C_3$ misses both five-point classes.** By (5), a point $x\in C_1$ has exactly one common neighbor with $3$. Its only possible common neighbors in

$$N_G(3)=\{0,w\}\cup C_3$$

lie in $C_3$: $x\not\sim0$, and $x\not\sim w$ because $1$ is triangle-free. Thus every point of $C_1$ has exactly one original neighbor in $C_3$, giving

$$e(C_1,C_3)=5.\tag{9}$$

For any $q\in C_3$, the nonedge pair $1,q$ has $B_{1q}=0$, so it has exactly one common neighbor. Its common neighbors in $N_G(1)$ can only be $a$ and points of $C_1$. Indeed $q\not\sim0$, and $q\not\sim w$ because $3,w,q$ would be a triangle at the triangle-free vertex $w$. Therefore

$$A_{aq}+|N_G(q)\cap C_1|=1.\tag{10}$$

Summing (10) over $C_3$ and using (9) gives exactly one point $d\in C_3$ adjacent to $a$. Equation (4) shows $d\ne c$. Equation (10) then gives $N_G(d)\cap C_1=\varnothing$. The identical equation using label $2$ gives

$$N_G(d)\cap C_1=N_G(d)\cap C_2=\varnothing.\tag{11}$$

Also $d$ has no neighbor in $C_3$, since that set is independent.

**Step 7. The final commutation contradiction.** Because $d\ne c$, equation (7) provides a point $x\in C_1$ with $B_{xd}=1$. Let $y\in C_2$ be its original matching mate from Step 5. Nonnegativity gives

$$(AB)_{yd}\ge A_{yx}B_{xd}=1.$$

But (8) says that the entire positive defect support of row $y$ lies in $C_1\cup C_3$. The vertex $d$ has no original neighbor in either set, by (11) and the independence of $C_3$. Therefore

$$(BA)_{yd}=\sum_v B_{yv}A_{vd}=0.$$

This contradicts $AB=BA$ and excludes D2_MATCH. $\square$

## Scope and remaining obligations

The proof uses only the original graph identities and the displayed D2_MATCH parent structure. In particular it does not use the global triple-repeat elimination or its finite checker inside this branch, does not assume an independently specified repeat matrix can be realized, and does not import the order-$59$ N15 condition.

Together with the separate S_TOUCH exclusion and the recovered seven-template coverage, the other order-$62$ templates remain D0_MATCH, D0_EDGE_BIN, D0_EDGE_BOUT, D1_MATCH, and S_DISJOINT. They are not excluded here. Fresh independent review and any formalization of the present branch remain separate work.
