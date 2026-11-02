# The K3,3 double-interface model reduces to six Petersen fibers

Date: 2026-10-11. This is an analytic reduction of the proposed construction
family, with explicit valid local interfaces. It is not a nonexistence proof
for the full six-Petersen-fiber family.

## Model and exact adjacent-fiber obligation

Partition sixty vertices into six fibers of size ten, indexed by the
vertices of $K_{3,3}$. Each fiber induces a simple two-regular graph $D_i$.
Every interface across the bipartition is a simple two-regular bipartite
graph, represented by a zero-one matrix $Y_{ij}$ with row and column sums
two. There are no interfaces within either side of the bipartition. The
whole graph is eight-regular.

For adjacent fibers there is no two-step route through a third fiber,
because $K_{3,3}$ has no triangles. The direct and two internal-route types
have ten slots per source. Thus diameter at most two forces the exact
identity

$$D_iY_{ij}+Y_{ij}D_j+Y_{ij}=J_{10}.\tag{1}$$

Two nonadjacent fibers on the same side have twelve route slots through
the three fibers on the opposite side. That count alone is not a proof of
coverage, and is not used to assume any unspecified matching is feasible.

The five possible internal types are $C_{10}$, $C_7+C_3$, $C_6+C_4$,
$2C_5$, and $C_4+2C_3$.

## Only C10 and 2C5 admit any exact interface

Let $D,E$ be two internal adjacency matrices and suppose $Y$ satisfies
(1). Take a cycle of length $\ell$ in $D$, and let $h$ be its indicator
column vector. Since $h^TD=2h^T$, the row vector $s=h^TY$ satisfies

$$s(E+3I)=\ell\mathbf1^T.$$

All eigenvalues of the symmetric two-regular adjacency matrix $E$ lie
between $-2$ and $2$, so $E+3I$ is invertible. As its row and column sums
are five, the unique solution is

$$s=\frac{\ell}{5}\mathbf1^T.$$

The entries of $s$ are integers. Every cycle in $D$ therefore has length
divisible by five. Transposing (1) gives the same conclusion for $E$.
Only $C_{10}$ and $2C_5$ remain. For these two types all four ordered pairs
really admit an interface, as the explicit construction below shows.

## Every C10 fiber fails same-fiber coverage

Suppose $D=C_{10}$ and number its vertices cyclically by $u\in\mathbb Z_{10}$.
Let $H$ be the antipodal permutation $u\mapsto u+5$. On the subspace where
$H$ acts by minus one, the eigenvalues of $D$ are

$$\varphi,\quad-\varphi^{-1},\quad-2,
\qquad \varphi=\frac{1+\sqrt5}{2}.$$

The complete sets of eigenvalues of the two allowed opposite types are

$$\operatorname{spec}(C_{10})=
\{2,\varphi,\varphi^{-1},-\varphi^{-1},-\varphi,-2\},$$

$$\operatorname{spec}(2C_5)=\{2,\varphi^{-1},-\varphi\}.$$

For an eigenvector $f$ of $D$ in the antipodal minus subspace, multiply
(1) on the left by $f^T$. Since $f^T\mathbf1=0$, this gives

$$f^TY\bigl(E+(\lambda+1)I\bigr)=0.$$

For each of the three listed minus-subspace eigenvalues $\lambda$, neither
allowed opposite spectrum contains $-1-\lambda$. Therefore the matrix in
parentheses is invertible and $f^TY=0$. The antipodal minus subspace is
annihilated, so

$$Y_{u,*}=Y_{u+5,*}\quad\text{for every }u.\tag{2}$$

Because each column of $Y$ has exactly two ones, (2) means every external
neighbor of $u$ has exactly $u$ and $u+5$ as neighbors back in this fiber.
Thus a two-step route out of the fiber and back can reach only the source
and its antipode, for every one of the three interfaces. Internal routes
of length at most two reach only $u,u\pm1,u\pm2$. Altogether at most six
of the ten vertices of this fiber are reached. This contradicts diameter
at most two.

Hence every internal graph of a target in this model must be $2C_5$.

## All-2C5 targets regroup into the existing six-Petersen model

Split each of the six original fibers into its two five-cycles. There are
six cycles on the left side and six on the right side. For any left cycle
and any right cycle, the corresponding $5\times5$ block $M$ of $Y$ has
row and column sums one: apply the preceding cycle-sum identity with
$\ell=5$ on both sides. Thus $M$ is a permutation matrix.

Writing $C,C'$ for the adjacency matrices of these cycles, the corresponding
block of (1) is

$$CM+MC'+M=J_5.$$

After identifying the two cycles along the matching, this becomes

$$C+MC'M^T+I=J_5.$$

The matching therefore identifies the second cycle with the complement
of the first cycle. Two five-cycles joined by such a matching form the
Petersen graph: label the first cycle with steps $\pm1$ on $\mathbb Z_5$,
transport those labels through the matching, and the second has steps
$\pm2$, with the matching as spokes.

Choose any bijection between the six left cycles and the six right cycles,
and group the paired cycles into six new ten-vertex fibers. Each new
fiber induces a Petersen graph. Between two new fibers $(L_a,R_a)$ and
$(L_b,R_b)$ the only edges are the matching $L_a$--$R_b$ and the matching
$R_a$--$L_b$. Their union is one perfect matching on all ten vertices.
All edges have been accounted for.

Consequently every possible diameter-two target in the proposed double-
interface model already belongs to the full six-Petersen-fiber family
with arbitrary perfect matchings. This conclusion does not impose an
automorphism or identify fibers with defect-matrix support components.

## A complete valid local interface

Label $C_{10}$ by $0,\ldots,9$ in cyclic order. Label $2C_5$ by two cycles
$0,\ldots,4$ and $5,\ldots,9$. For any ordered pair of these two types,
take

$$Y_{uv}=1\quad\Longleftrightarrow\quad v\equiv2u\pmod5.$$

The two target neighbors of each row are explicitly

```text
0: 0,5     1: 2,7     2: 4,9     3: 1,6     4: 3,8
5: 0,5     6: 2,7     7: 4,9     8: 1,6     9: 3,8
```

Each row and column has two ones. The three terms in (1) respectively
reach target residues $2u\pm2$, $2u\pm1$, and $2u$, with both target
vertices of each residue reached exactly once. Thus (1) holds for all
four allowed ordered internal-type pairs.

The [direct generator and matrix check](../../../computations/dd82/construction/k33_double_interface.py)
saves the full matrix and the four exact checks in
[the result JSON](../../../computations/dd82/construction/k33_double_interface.json).
This is a complete local interface, not a complete sixty-vertex candidate.
No graph search, interface enumeration, or SAT call was required.
