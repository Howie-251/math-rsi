# False-twin order 58: the cube-translation matching mechanism is impossible

Date: 2026-10-13. This is an analytic check of the proposed mechanism, with
no permutation search, solver run or Lean formalization.

## Claim

In the eight-six-fibre false-twin construction, index the eight fibres by
$V=\mathbb F_2^3$ and label their six vertices by a common set $L$.
Suppose every matching from fibre $i$ to fibre $j$ depends only on $i+j$:

$$Q_{ij}=P_{i+j}\qquad(i\ne j),$$

where each $P_w$ is a permutation matrix on $L$. No such construction has
diameter at most two.

This excludes precisely the stated label-preserving translation mechanism.
It does not exclude all false-twin constructions, all order-58 graphs, or
every possible action of $C_2^3$ on a target graph.

## Status

**PROVABLE AS STATED.** The proposed collision/XOR argument is valid after
making the contribution from the two special indices explicit.

## Assumptions

- The graph has the exact false-twin construction described in
  [the eight-six-fibre representation](FALSE_TWINS58_EIGHT_SIX_FIBERS.md),
  Section 2: two twins, eight independent common neighbours, and eight
  independent fibres of size six with a perfect matching between every pair.
- In the chosen common fibre coordinates, $Q_{ij}=P_{i+j}$.
- The graph is undirected. Consequently $P_w=P_w^T=P_w^{-1}$, so the
  corresponding permutation $p_w$ is an involution; fixed points and the
  identity permutation are allowed.

## Notation

Matrices use the row-source convention: $(P_w)_{ab}=1$ exactly when
$p_w(a)=b$. Write $J$ for the $6$-by-$6$ all-ones matrix. Sums of elements
of $V$ are vector sums in characteristic two, also called XOR.

## Proof Strategy

For one fixed fibre coordinate, translate the necessary diagonal coverage
conditions into collision counts of an eight-point labelling of $V$.
They would force the seven nonzero differences to occur exactly once among
equal-label pairs. The possible label-class sizes contradict the XOR of
these differences.

## Dependency Map

1. The exact matching-cover representation gives the cross-fibre path-count
   matrix, with row and column sums seven.
2. Diameter-two coverage and involutivity give exactly one unordered
   equal-label pair of each nonzero difference.
3. Elementary integer partitions and characteristic-two addition exclude
   every resulting label-class profile.

## Proof

**Step 1: the necessary path-count matrices.** For each nonzero $w\in V$,
the matrix of paths of length one or two from fibre $0$ to fibre $w$ is

$$
K_w=P_w+\sum_{u\in V\setminus\{0,w\}}P_uP_{u+w}.
$$

The direct matching contributes one permutation matrix, and the six other
fibres contribute six products of permutation matrices. There are no
additional cross-fibre two-step routes through the common neighbours or
twins. Thus every row and column of $K_w$ sums to seven. Diameter at most
two would imply $K_w\ge J$, so $K_w-J$ is a permutation matrix. In
particular, every diagonal entry of $K_w$ belongs to $\{1,2\}$.

**Step 2: collision counts on all eight group elements.** Fix any $a\in L$
and define $f:V\to L$ by

$$f(0)=a,\qquad f(u)=p_u(a)\quad(u\ne0).$$

For nonzero $w$, put $e_w=\mathbf1_{f(w)=a}$. Since both $p_u$ and
$p_{u+w}$ are involutions,

$$
(P_uP_{u+w})_{aa}=1
\quad\Longleftrightarrow\quad
p_{u+w}(p_u(a))=a
\quad\Longleftrightarrow\quad
f(u)=f(u+w).
$$

It follows that

$$
(K_w)_{aa}=e_w+
\#\{u\in V\setminus\{0,w\}: f(u)=f(u+w)\}.
$$

The set counted on the right is paired without fixed points by
$u\mapsto u+w$, so its size is even. Because $(K_w)_{aa}\in\{1,2\}$,
this diagonal entry is $1$ when $e_w=1$ and $2$ when $e_w=0$.
Restoring the two omitted indices $0,w$, each of which contributes $e_w$,
gives the full ordered collision count

$$
D_w:=\#\{u\in V:f(u)=f(u+w)\}=(K_w)_{aa}+e_w=2.
$$

Therefore, for every nonzero $w$, exactly one unordered pair of distinct
points with the same $f$-label has difference $w$.

**Step 3: only two label-class profiles remain.** If the nonempty classes
of $f$ have sizes $s_1,\ldots,s_r$, then

$$\sum_i s_i=8,\qquad \sum_i\binom{s_i}{2}=7.$$

No class has size at least five, since that alone contributes at least ten
pairs. A class of size four contributes six pairs, so the remaining four
points must form classes of sizes $2,1,1$. If the largest class has size
three, exactly two size-three classes are needed: one size-three class
and five points in classes of size at most two contribute at most five
pairs; two size-three classes leave two points which must share a label.
If all classes have size at most two, there are at most four pairs.
The only possibilities are therefore

$$4+2+1+1\qquad\text{or}\qquad3+3+2.$$

**Step 4: both profiles contradict the difference XOR.** The seven
equal-label unordered pairs have all seven nonzero elements of $V$ as
their differences. Their sum is zero, since each of the three coordinates
is one in four of the eight elements of $V$.

For a class $C$, the sum of the differences of all its unordered pairs is

$$
\sum_{\{x,y\}\subset C}(x+y)
=(|C|-1)\sum_{x\in C}x,
$$

because each point occurs in exactly $|C|-1$ pairs.

In the profile $3+3+2$, the size-three classes each contribute zero.
The size-two class contributes the sum of its two distinct elements,
which is nonzero. This contradicts the total sum zero.

In the profile $4+2+1+1$, the total difference sum is the sum of the six
elements in the size-four and size-two classes, so those six elements
sum to zero. All eight elements of $V$ also sum to zero; therefore the
two singleton elements sum to zero. They would be equal, contradicting
that the classes partition eight distinct elements.

Both cases are impossible, proving the claim. $\square$

## Corrections or Missing Assumptions

The translation formula $Q_{ij}=P_{i+j}$ is essential to this proof and is
explicitly part of the claim. An unspecified $C_2^3$ automorphism action
does not by itself supply the stated representation. No assumption that
the seven involutions are fixed-point-free, distinct or commuting is used.

## Open Risks

There is no unfilled implication in the displayed finite argument. This
document is a local mathematical check; it does not assert Gemini approval,
an executed exhaustive permutation search or a Lean-checked theorem.
