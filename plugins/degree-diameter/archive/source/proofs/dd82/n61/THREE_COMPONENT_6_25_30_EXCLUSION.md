# Order61: exclusion of the actual defect-component quotient (6,25,30)

## Statement and scope

Let G be a simple graph of order61, maximum degree at most8 and diameter
at most2. Its actual weighted defect

`B = A^2 + A - 7I61 - J61`

cannot have three positive-support components with sizes and adjacency
quotient

```
n = (6,25,30),      Q = [[3,0,5],
                        [0,2,6],
                        [1,5,2]].
```

This excludes all relabelings of the second quotient in
[the unconditional three-component classification](GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md).
It does not exclude the other quotient `(12,21,28)`, a connected defect,
or any component count at least5. No symmetry, binary-defect assumption,
CP02 hypothesis, or imposed construction family is used.

Status: a complete local proof with one five-entry exact polynomial
calculation, now checked by the fresh local proof-checker and the first
Gemini review of dd82-v3-defect-components61-20261013. Neither found a
mathematical gap; the local review remains same-family/provisional.
Receipts: reviews/dd82/proof-checker-n61-components-20261013/ and
reviews/dd82/20261013_V3_n61_components_direction.json. No solver, new quotient
enumeration, graph search, or Lean proof is claimed. The previously read
formula-derivation, proof-writer and experiment-bridge skills are applied
in the V3 DD82 mathematical adaptation; this is a separate mechanism from the completed
order60 construction review.

## 1. The same actual adjacency and defect blocks

A vertex of degree at most7 could reach at most `1+7+7*7=57` vertices
within two steps. Thus G is eight-regular. B is symmetric, has diagonal
zero, is entrywise nonnegative, and has row sum

`8^2+8-7-61 = 4`.

Use the actual three defect components in the stated order. Their
adjacency blocks are

```
A = [[S,   0,   X],
     [0,   T,   Y],
     [X^T, Y^T, R]],
```

where S is cubic on6 vertices, T is two-regular on25, and R is
two-regular on30. The binary matrix X has size `6 x 30`, row sum5
and column sum1. The binary matrix Y has size `25 x 30`, row sum6
and column sum5. Different B components have zero cross defect, so

`X Y^T = J_(6,25)`,
`S X + X R + X = J_(6,30)`,
`T Y + Y R + Y = J_(25,30)`.                                    (1)

These identities concern the same X,Y,S,T,R throughout the proof.
In fact the contradiction below needs only the last two identities,
the degrees, and the actual defect conditions.

Since every column of X has exactly one1, `X X^T = 5I6`. Therefore
the first diagonal defect block is

`B_1 = S^2 + S - 2I6 - J6`.                                    (2)

Its positive support must be connected: the six vertices are one
actual B component, not a union of components.

## 2. The cubic-six graph and the cycle cover

The complement of any simple cubic graph on6 vertices is a simple
two-regular graph on6 vertices. Its components are cycles of length
at least3, so it is either C6 or two disjoint C3's. Hence S is either
the complement of C6 (the triangular prism) or K3,3. This is a
self-contained exhaustive classification; connectedness of S was not
assumed.

If S is K3,3, two different vertices in one part have three common
neighbors, while vertices in different parts are adjacent and have
no common neighbors. Equation (2) then gives weight2 on each of the
two part-triangles and zero between them: `B_1 = 2 A(2K3)`. This
contradicts the connected positive support of B_1. Consequently

`S = J6 - I6 - C6`,                                             (3)

after labeling the six vertices cyclically; here and below C_p also
denotes the adjacency matrix of the p-cycle.

Let `pi(z)` be the unique row whose entry in column z of X is1.
Each value of pi has five preimages. At entry `(a,z)`, the middle
identity in (1), together with (3), says

`#{w adjacent_R z : pi(w)=a}
       = 1 - S_(a,pi(z)) - 1_(a=pi(z))
       = (C6)_(a,pi(z))`.                                      (4)

Every R vertex therefore has exactly one neighbor over each of the
two C6 neighbors of its image. Thus R is a five-sheet graph cover
of C6. To see the possible cycle lengths directly, walk around any
R component. At each step its next edge must project to the base
edge other than the edge just traversed, since there is exactly one
edge to either adjacent base fiber. The projected walk consistently
goes around C6, so that component has length divisible by6. Since
R has30 vertices, each of its component lengths is in

`{6,12,18,24,30}`.                                              (5)

## 3. Integral block sums force R=C30

Take any T component C_p and any R component C_q, and let Z be the
corresponding binary `p x q` submatrix of Y. Since T and R have no
edges between their own cycle components, their block of (1) is

`C_p Z + Z C_q + Z = J_(p,q)`.                                 (6)

Put `r=Z 1_q` and `c=Z^T 1_p`. Multiplying (6) by all-ones vectors
on the two sides gives, respectively,

`(C_p+3I_p)r = q 1_p`,       `(C_q+3I_q)c = p 1_q`.              (7)

All adjacency eigenvalues of a cycle lie in [-2,2], so both shifted
matrices are invertible. Their row sums are5. The unique solutions
of (7) are therefore

`r=(q/5)1_p`,       `c=(p/5)1_q`.                              (8)

The entries are actual integer row and column counts. Hence every
T cycle length p and every R cycle length q is divisible by5.
Combining this with (5), every R cycle would have length30. There
are only30 vertices, so

`R=C30`,       and every T cycle has length in `{5,10,15,20,25}`.  (9)

This removes the need to analyze a separate case in which R has
no C30 component. No enumeration of cycle partitions is needed.

## 4. The exact cycle-resonance calculation

For a p-cycle, define polynomials

`L_0(x)=2`, `L_1(x)=x`, `L_p(x)=x L_(p-1)(x)-L_(p-2)(x)`.

Then its characteristic polynomial is

`chi_p(x)=L_p(x)-2`.                                           (10)

Indeed `L_p(z+z^(-1))=z^p+z^(-p)`, so the roots are precisely
`2 cos(2 pi k/p)`. The non-endpoint roots occur twice, whereas2
and, for even p, -2 occur once; their multiplicities sum to p,
proving (10) as a monic polynomial identity.

The required exact gcds over Q[x] are as follows, with
`f(x)=x^2+x-1`:

| T cycle length p | monic `gcd(chi_p(x),chi_30(-1-x))` |
|---|---|
| 5 | `f(x)^2` |
| 10 | `(x+2) f(x)^2` |
| 15 | `f(x)^2` |
| 20 | `x^2 (x+2) f(x)^2` |
| 25 | `f(x)^2` |

This table was computed once by the integer recurrence (10) and
ordinary Euclidean division with exact rational coefficients. The
short standalone source is
[`component_6_25_30_resonance.py`](../../../computations/dd82/n61/component_6_25_30_resonance.py).
The [complete result](../../../computations/dd82/n61/component_6_25_30_resonance.result.json)
retains all polynomial coefficients, gcds, both division cofactors
and Euclidean degree sequences. The complete five-entry calculation
used 0.028182800 CPU seconds and 0.028213181 wall seconds internally.
It uses only Python's standard library and no approximate eigenvalues.

Here is the exact consequence of the table. Label R=C30 cyclically
by z in Z/30Z. For a nonconstant Fourier eigenvector v of C30 with
eigenvalue mu, (6) gives

`(C_p+(1+mu)I_p) Z v = 0`,                                    (11)

since `J_(p,30)v=0`. Thus Z v can be nonzero only if some C_p
eigenvalue lambda satisfies `lambda+mu+1=0`. The gcd table lists
all such lambda. The possible mu and their C30 Fourier orders are

| lambda | mu=-1-lambda | exact Fourier order in C30 |
|---|---|---|
| root of `x^2+x-1` | the other root of `x^2+x-1` | 5 |
| -2 | 1 | 6 |
| 0 | -1 | 3 |

For example mu=1 means `2 cos(2 pi k/30)=1`, hence k=5 or25,
and similarly the other entries follow from the elementary cycle
Fourier eigenvalues. Consequently every row y of Y is a sum of
functions of periods5 and6:

`y(z) = a(z mod5) + b(z mod6)`.                                (12)

Constants can be included in either summand; the order3 modes
belong to the period6 summand. Formula (11) proves this for each
actual T cycle and therefore for every row of the same Y.

## 5. Binary additivity and the contradiction

The Chinese remainder map identifies Z/30Z with
`(Z/5Z) x (Z/6Z)`. Since y is binary, (12) means

`a_i+b_j` belongs to `{0,1}` for every i,j.                       (13)

If a is nonconstant, choose i,i' with `a_i-a_i' != 0`. For every j
this nonzero difference is the difference of two binary entries,
so it equals1 or -1. Those two entries must then be respectively
(1,0) or (0,1), independently of j, forcing b to be constant.
If a is constant instead, y has period6. Thus every binary row
satisfying (12) has period5 or period6. The argument also works
directly for complex Fourier coefficients, since the displayed
differences of binary entries are real.

A period6 binary word of length30 has weight divisible by5. Every
row of Y has weight6, so no row can have period6. A period5 row
repeats its five entries six times, and weight6 forces exactly one
of those five entries to be1. There are only five such rows.

However, all25 rows of the actual Y must be distinct. If two
distinct vertices u,v in the 25-vertex component had equal rows,
they would share six neighbors in the 30-vertex component. Then

`B_uv = (A^2)_uv + A_uv - 1 >= 6-1 = 5`,

contradicting nonnegativity and row sum4 of the same B. Twenty-five
distinct rows cannot be chosen from the five possibilities above.
This contradiction proves the stated exclusion.

Only the `(6,25,30)` branch has been closed here. The other actual
three-component quotient and the other allowed component counts
remain outside this proof.
