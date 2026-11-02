# Six matching fibers: one surviving quotient and an explicit failed seed

Date: 2026-10-12. The quotient classification below uses one complete small
integer-matrix enumeration. The fixed-interface obstruction is analytic.
Neither part excludes the general surviving interface family.

## Model and complete quotient domain

Consider a simple eight-regular graph on sixty vertices, with an equitable
partition into six fibers of size ten. Each fiber induces a perfect
matching. Let $Q=(q_{ij})$ be the symmetric cross-degree matrix, with zero
diagonal and row sum seven. No cyclic action or defect-component partition
is assumed.

Writing $s_i=\sum_kq_{ik}^2$, the necessary cross-fiber capacities are

$$h_{ij}=3q_{ij}+(Q^2)_{ij}\ge10\qquad(i\ne j),$$

and their sum in row $i$ is $70-s_i$. Hence $s_i\le20$. Inside a fiber,
the matching reaches only the source and its mate. The external returning
routes contribute at most $\sum_jq_{ij}(q_{ij}-1)=s_i-7$ other vertices,
so $s_i\ge15$. Since $s_i\equiv7\pmod2$, it belongs to $\{15,17,19\}$.

If an entry equals $t\ge4$, its cross capacity is at least $3t$, while
the other four capacities total at least forty. Also
$s_i\ge t^2+7-t$. These inequalities imply

$$70-(t^2+7-t)\ge40+3t,\qquad t^2+2t\le23,$$

which fails for $t\ge4$. Thus all entries are at most three. The complete
list of possible off-diagonal row multisets is consequently

$$ (3,3,1,0,0),\qquad(3,2,2,0,0),\qquad(3,2,1,1,0).$$

## One complete finite screen

The [source](../../../computations/dd82/construction/six_matching_fibers_quotients.py)
forms all distinct permutations of these row multisets. It then assigns
rows in order, accepting a row exactly when its already fixed prefix
agrees with earlier symmetric entries. Thus every symmetric matrix in the
proved domain appears once. No capacity pruning occurs before a complete
matrix is counted. Each complete matrix is checked against all fifteen
cross capacities. Surviving matrices are grouped by all $720$ permutations
of the six fiber labels.

The [actual result](../../../computations/dd82/construction/six_matching_fibers_quotients.json)
records:

* $120$ distinct row patterns;
* $6210$ symmetric labeled matrices;
* $120$ capacity survivors, forming exactly one $S_6$ orbit;
* $0.143514$ CPU seconds, on one pinned CPU, under a ten-second limit.

One representative is

$$Q=\begin{pmatrix}
0&0&1&1&2&3\\
0&0&2&3&1&1\\
1&2&0&1&3&0\\
1&3&1&0&0&2\\
2&1&3&0&0&1\\
3&1&0&2&1&0
\end{pmatrix}.$$

Its degree-one interfaces form two triangles on $\{0,2,3\}$ and
$\{1,4,5\}$. Between the triangles, the degree-three, degree-two, and
degree-zero pairs each form a perfect matching. Equivalently, index the
triangles by $L_a,R_a$, $a\in\mathbb Z_3$: the cross degrees are three
on $L_aR_a$, two on $L_aR_{a+1}$, and zero on $L_aR_{a-1}$.

Every row has squared norm fifteen. Capacities are exactly ten on degree
zero and degree one pairs, twelve on degree two pairs, and thirteen on
degree three pairs. A capacity survivor is not a complete graph witness.

## Exact remaining interface obligations

After independently labeling each fiber, all six internal perfect
matchings may be represented by the same permutation matrix $S$.
Write $F_{ij}$ for an oriented interface matrix, with
$F_{ji}=F_{ij}^T$. A degree-one interface is a permutation $M_{ij}$;
degree-two and degree-three interfaces are zero-one matrices of the
specified row and column sums.

Each fiber has one degree-two interface $Y_i$ and one degree-three
interface $Z_i$, both oriented outward. Same-fiber capacity is exact,
giving

$$S+Y_iY_i^T+Z_iZ_i^T=J_{10}+4I_{10}.\tag{1}$$

For a degree-zero pair, all routes go through one of the other four
fibers, and exact capacity requires

$$\sum_{k\ne i,j}F_{ik}F_{kj}=J_{10}.\tag{2}$$

For a degree-one pair $i,j$, let $k$ be the third vertex of their quotient
triangle, and let $\ell$ be their unique common neighboring fiber on the
other side. Its two incident cross degrees are two and three. The exact
condition is

$$M_{ij}+SM_{ij}+M_{ij}S+M_{ik}M_{kj}
       +F_{i\ell}F_{\ell j}=J_{10}.\tag{3}$$

For degree-two and degree-three pairs the remaining condition is the
entrywise inequality

$$F_{ij}+SF_{ij}+F_{ij}S+
  \sum_{k\ne i,j}F_{ik}F_{kj}\ge J_{10}.\tag{4}$$

Together (1)--(4), the zero-one interface conditions, and their prescribed
row/column sums are necessary and sufficient for diameter at most two in
this particular quotient model. They are coupled equations for the same
six degree-one matchings and six higher-degree interfaces.

One useful consequence is that the defect matrix $B=A^2+A-7I-J$ would be
zero within fibers and on every degree-zero or degree-one interface.
Its only nonzero blocks can be on the degree-two and degree-three pairs,
with block row sums two and three respectively. Therefore its support is
bipartite across the two thirty-vertex halves. This does not identify the
six original fibers with its support components.

## Explicit interfaces satisfying every same-fiber equation

Use Petersen coordinates $u=(e,x)$, $e\in\{0,1\}$ and
$x\in\mathbb Z_5$. Let $S(e,x)=(1-e,x)$ be the spoke matching. Let $R$
rotate layer zero by one and layer one by two, and put

$$C=R+R^T,\qquad P=C+S,\qquad Y=I+R,\qquad Z=P.$$

Here $P$ is the Petersen adjacency matrix, $Y$ is a zero-one interface of
degree two, and $Z$ is one of degree three. Since
$P^2=2I-P+J$ and $YY^T=Y^TY=2I+C$,

$$S+YY^T+ZZ^T=J+4I.$$

The column version holds too. Thus these are actual compatible local
interfaces for (1), including either orientation of $Y$.

For a complete sixty-vertex seed, take the displayed quotient, use $S$
inside every fiber, use $P$ on every degree-three interface, and use $Y$
from lower-index to higher-index fiber on every degree-two interface,
with $Y^T$ in reverse. Use the identity on all six degree-one interfaces.
The [generator](../../../computations/dd82/construction/six_matching_fibers_seed.py)
saves every edge in
[the complete seed](../../../computations/dd82/construction/six_matching_fibers_seed/seed.edges.json).

The existing independent all-source BFS checker read that edge list and
confirmed $60$ vertices, $240$ edges, degree eight everywhere, diameter
three, and **600 bad unordered pairs**. There are no bad same-fiber
pairs. The bad cross-fiber pairs are distributed as follows:

| Interface degree | Number of bad pairs |
| ---: | ---: |
| $0$ | $180$ |
| $1$ | $240$ |
| $2$ | $120$ |
| $3$ | $60$ |

Every bad pair and its neighbor/common-neighbor data is retained in
[the independent verification](../../../computations/dd82/construction/six_matching_fibers_seed/seed.edges.verification.json).
This seed is a failed construction, not a lower-bound improvement.

## The fixed local interfaces cannot be completed by changing the six matchings

Keep these common coordinates, $S$, $P$, and $Y$ or $Y^T$ on the higher-
degree interfaces. Allow all six degree-one matchings to vary arbitrarily.
For any degree-one pair, the fixed product
$F=F_{i\ell}F_{\ell j}$ in (3) is one of

$$YP,\quad Y^TP,\quad PY,\quad PY^T.$$

Partition the coordinates into the two layers of size five. Each row of
$F$ has exactly four distinct targets in its own layer: its same-layer
part is a product of $R+R^T$ with $I+R$ or $I+R^T$, giving four different
powers of a five-cycle. Thus $L=J-F$ has exactly one same-layer target
per row. Equation (3) becomes

$$M+SM+MS+N=L,\qquad N=M_{ik}M_{kj}.\tag{5}$$

For each source, $M$ and $MS$ together contribute exactly one same-layer
target, since $S$ switches layers. Nonnegativity and the unique same-layer
slot in $L$ force $SM$ to contribute no same-layer target. Equivalently,
$M$ preserves the two layers. This applies to all three degree-one
matchings in each quotient triangle, so their product $N$ preserves the
layers too. Now both $M$ and $N$ contribute a same-layer route in (5),
contradicting the single available slot.

Therefore the complete fixed-$S,Y,P$ interface family is impossible even
when its six degree-one matchings are released. No $10!$ catalog was
launched, because this proof resolves that proposed continuation.

## Scope still open

The quotient screen leaves one possible degree-one-fiber quotient. Its
general degree-two and degree-three interfaces need not be the common
$Y$ and $P$ used above, nor share their coordinate alignment. The fixed-
interface contradiction does not exclude those general choices, and no
repartition into six Petersen fibers has been proved for them. Equations
(1)--(4) describe that remaining construction obligation precisely.
