# Order61: exclusion of the actual defect-component quotient (12,21,28)

## Statement and scope

Let G be a simple graph of order61, maximum degree at most8 and diameter
at most2. Its actual weighted defect

`B = A^2 + A - 7I61 - J61`

cannot have three positive-support components with sizes and adjacency
quotient

```
n = (12,21,28),     Q = [[1,0,7],
                        [0,4,4],
                        [3,3,2]].
```

All relabelings are included. The proof is from the same original
adjacency matrix throughout; it does not assume a simple defect matrix,
an automorphism, or CP02's conditional hypotheses.

Combined with the
[unconditional three-component quotient classification](GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md)
and the separate
[(6,25,30) exclusion](THREE_COMPONENT_6_25_30_EXCLUSION.md), this closes
the entire **exactly three defect components** branch for arbitrary
order61 targets. It does not exclude a connected defect or the other
allowed odd component counts at least5, and is not an order61 exclusion.

Status: complete local proof, fresh scoped proof-checker PASS and Gemini
round2 acceptance under `dd82-v3-defect-components61-20261013`.
Receipts: `reviews/dd82/proof-checker-n61-c3-lift-20261013/PROOF_AUDIT.md`
and `reviews/dd82/20261013_V3_n61_complete_c3_review.json`.
This new proof uses no computation, solver or graph enumeration. The
companion manuscripts and their exact finite checks remain explicit
inherited dependencies of the final c3 corollary. Local review is
same-family/provisional; Gemini metadata is CLI-reported. No Lean or
whole-order61 acceptance is claimed. The already-read formula-derivation
and proof-writer skills use the V3 DD82 mathematical adaptation.

## 1. Actual blocks and their identities

A vertex of degree at most7 could reach at most `1+7+7*7=57` vertices
within two steps. Therefore G is eight-regular. B is symmetric,
entrywise nonnegative, has diagonal zero and row sum

`64+8-7-61=4`.

Regularity gives `AJ=JA`, hence `AB=BA`. With the actual three defect
components in the displayed order,

```
A = [[S,   0,   X],
     [0,   T,   Y],
     [X^T, Y^T, R]],       B = diag(B_1,B_2,B_3).
```

S is the adjacency matrix of six disjoint matching edges on12 vertices;
T is four-regular on21 vertices; R is two-regular on28 vertices. X is
binary of size `12 x 28`, with row sum7 and column sum3. Y is binary of
size `21 x 28`, with row sum4 and column sum3. The zero off-diagonal
blocks of B give

`X Y^T = J_(12,21)`,
`S X + X R + X = J_(12,28)`,
`T Y + Y R + Y = J_(21,28)`.                                    (1)

The diagonal blocks of the same defect are

```
B_1 = X X^T + S - 6I12 - J12,
B_2 = T^2 + T + Y Y^T - 7I21 - J21,
B_3 = R^2 + R + X^T X + Y^T Y - 7I28 - J28.
```

Each B_i is nonnegative symmetric with row sum4, so all its eigenvalues
are in [-4,4]. The diagonal blocks of `AB=BA` give

`S B_1=B_1 S`,       `T B_2=B_2 T`,       `R B_3=B_3 R`.          (2)

For completeness, T is necessarily connected. Otherwise some nonzero
vector v constant on its components satisfies `Tv=4v` and `1^T v=0`.
Then

`v^T B_2 v = 13 ||v||^2 + ||Y^T v||^2 >= 13 ||v||^2`,

contradicting the upper eigenvalue bound4 for B_2. The final exclusions
below do not need this extra connectivity fact.

## 2. The complete list of possible R cycle lengths

For an arbitrary q-cycle of R, let Z be its `12 x q` column block in X.
The middle identity in (1) restricts to

`S Z + Z C_q + Z = J_(12,q)`,

where C_q is the cycle adjacency matrix. Its row-sum vector r satisfies

`(S+3I12)r=q 1_12`.

Since `S^2=I12`, the shifted matrix is invertible; it has row sum4.
Consequently `r=(q/4)1_12`. These are integer row sums, so

`4 divides q`.                                                  (3)

Let `E={v:Sv=v, 1^T v=0}`. The positive eigenspace of the six-edge
matching S has dimension6, so E has dimension5. For v in E, the B_1
identity gives

`||X^T v||^2 = v^T(B_1+5I12)v >= ||v||^2`.

Thus `X^T` is injective on E. Transposing the middle identity in (1)
and applying it to v gives

`R X^T v = -2 X^T v`.

The eigenvalue -2 of each even cycle is simple, with alternating
eigenvector. Equations (3) and the injection therefore force at least
five R cycles. Dividing their lengths by4 gives a partition of7 into
at least five positive integers. The complete list is

```
12+4+4+4+4,
8+8+4+4+4,
8+4+4+4+4+4,
4+4+4+4+4+4+4.
```

## 3. X is four-periodic on every R cycle

Fix a `4k`-cycle of R, labeled by z modulo4k, and a matched pair of
rows of X. Write their binary entries as a_z and b_z. Equation (1)
gives

`a_z+b_z+a_(z-1)+a_(z+1)=1`,
`b_z+a_z+b_(z-1)+b_(z+1)=1`.                                   (4)

Set `h_z=a_z+b_z` and `d_z=a_z-b_z`. Adding (4) yields

`2h_z+h_(z-1)+h_(z+1)=2`.

For `g_z=h_z-1/2`, multiply the homogeneous recurrence by g_z and
sum around the cycle. The result is

`sum_z (g_z+g_(z+1))^2=0`.

Hence `h_(z+1)=1-h_z`. Because h is a nonnegative integer vector, it
alternates between0 and1. Subtracting (4) gives

`d_(z-1)+d_(z+1)=0`,       hence `d_(z+2)=-d_z`.

On the active parity, d is1 or -1 and alternates every two steps;
on the other parity it is zero. Therefore a selects exactly one
residue class modulo4, and b selects the opposite residue class.

It follows that on this cycle X has four column types, each repeated
k times. Their supports partition all12 rows into four sets of size3,
because every row selects one phase and every column has sum3. In
particular, columns at distinct residues modulo4 have disjoint supports,
and columns at the same residue are identical.

## 4. A Rayleigh bound excludes the C12 case

For each R cycle l of length `4k_l`, define a six-coordinate sign vector
epsilon_l: its i-th entry is +1 if matched pair i is active at even
positions, and -1 otherwise. Each column contains3 ones from3 different
matched pairs. Thus three pairs are active at either parity, and

`epsilon_l in {+1,-1}^6`,       `1^T epsilon_l=0`,
`sum_l k_l=7`.

Use the orthonormal basis
`u_i=(e_(a_i)+e_(b_i))/sqrt(2)` of the positive eigenspace of S.
The contribution of cycle l to the compression of `X X^T` in this
basis is

`(k_l/2) (J6 + epsilon_l epsilon_l^T)`.

Indeed its two parity types occur `2k_l` times each, and the projected
column vectors are `p/sqrt(2)` and `(1-p)/sqrt(2)`, where
`p=(1+epsilon_l)/2`. On the five-dimensional contrast space `1^perp`,
the compression is consequently

`M = (1/2) sum_l k_l epsilon_l epsilon_l^T`.                     (5)

By the B_1 identity, on E the quadratic form of `X X^T` is that of
`B_1+5I`. Hence every Rayleigh quotient of (5) is at most9.

Two balanced sign vectors of length6 have inner product in
`{-6,-2,2,6}`: their sets of three positive coordinates have symmetric
difference of size0,2,4 or6. Fix a cycle of weight k and use its own
epsilon, of squared norm6, as the test vector in (5). We obtain

`epsilon^T M epsilon / 6
    >= (1/12) (36k+4(7-k))
     = (8k+7)/3`.                                              (6)

For any k>=3 this is at least `31/3>9`, a contradiction. Thus every
cycle of length at least12 is excluded, including the C12 case.
The same calculation shows that the total weight of any
single sign type up to sign is at most2, but no enumeration of those
types is needed here.

## 5. No C8 component is possible

This argument applies to any C8 component of R, regardless of all
its other components. Label its vertices modulo8 and let Z denote
the corresponding `21 x 8` block of Y. Equation (1) gives

`T Z + Z C8 + Z = J_(21,8)`.                                    (7)

Its nonnegative integer row-sum vector r satisfies

`(T+3I21)r=8 1_21`.

Therefore every r_i is at most2. Also, no row of Z can select two
positions at cycle distance1 or2: in that case the two closed cycle
neighborhoods overlap, making an entry of `Z C8+Z` at least2,
contrary to (7).

Positions z and z+4 cannot both be selected either. Their X columns
are identical and have three ones by Section3; selecting both would
make three entries of the corresponding column of `X Y^T` at least2,
contrary to the first identity in (1). Thus every row with r_i=2
selects a pair at cycle distance3.

Write

`h_z = sum_i Z_(i,z) Z_(i,z+3)`.

Consider the principal `8 x 8` block B_88 of B_3 on this C8.
The actual formula for B_3, and the restrictions just proved, give

| Cyclic distance between distinct vertices | Entry of B_88 |
|---|---|
| 1 | 0 |
| 2 | 0 |
| 4 | 2 |
| pair `{z,z+3}` | `h_z-1` |

For distance2 there is exactly one R common neighbor; for distance1
there is a direct R edge. Both X-column and Y-column intersections
vanish in these cases. At distance4, the X-column intersection is3
and the Y-column intersection is zero. At distance3, only the
Y-column intersection contributes. The diagonal remains zero, as
it is the diagonal of the actual B.

Let P4 be the permutation matrix for the opposite-point map `z -> z+4`.
Then

`B_88 = 2P4+W`,

where W is supported on the step3 cycle edges `{z,z+3}`, with
nonnegative integer weights `w_z=h_z-1`.

Since R is block diagonal by its cycles, the principal C8 block of
`R B_3=B_3 R` is `C8 B_88=B_88 C8`. The opposite-point map commutes
with C8, so `C8 W=W C8`. Its entry `(z,z+2)` says exactly

`w_(z-1)=w_z`:

the left product has the single possible term `W_(z-1,z+2)`, and
the right product has the single possible term `W_(z,z+3)`. Hence
all h_z are the same positive integer h.

Let n_j be the number of Z rows with row sum j, for j=0,1,2. Every
row of size2 corresponds to exactly one of the eight distinct
unordered pairs `{z,z+3}`. Consequently

`n_2=sum_z h_z=8h`.

Every Z column has sum3, so `n_1+2n_2=24`, implying `n_2<=12`.
As h is a positive integer, it follows that

`h=1`,       `n_2=8`,       `n_1=8`,       `n_0=5`.              (8)

For a vertex i with r_i=0, the row-sum equation gives
`sum_(j adjacent_T i) r_j=8`. There are four neighbors and each
r_j is at most2, so all four have r_j=2. The number of T edges
between the r=0 and r=2 classes is therefore `5*4=20`.

On the other hand, consider an r=2 row supported at `{z,z+3}`.
Its own closed C8 neighborhoods cover the six positions

`{z-1,z,z+1,z+2,z+3,z+4}`,

each once. Equation (7) forces the sum of its four T-neighbor rows
of Z to be the indicator of the remaining adjacent pair
`{z+5,z+6}`. Thus each neighbor row is supported within that pair,
and the nonempty rows have disjoint supports. No such neighbor
can have r=2, since every r=2 support has cycle distance3. There
must be exactly two r=1 neighbors and two r=0 neighbors. Counting
the same edges from the eight r=2 vertices gives `8*2=16`,
contradicting20.

This excludes every C8, so both remaining circle types containing
C8 are impossible.

## 6. Seven C4 components would cover too many labels

Only `R=7C4` remains. Index its cycles by l=1,...,7 and let Z_l
be the corresponding Y blocks. Each integer row-sum vector r_l
satisfies

`(T+3I21)r_l=4 1_21`.

Nonnegativity forces its entries to be0 or1. Its total is12 because
the four columns each have sum3. Put

`D_l={i:(r_l)_i=1}`,       `E_l={i:(r_l)_i=0}`.

Then `|D_l|=12` and `|E_l|=9`. For a vertex in D_l, exactly one
T neighbor lies in D_l and three in E_l. For a vertex in E_l,
all four neighbors lie in D_l. In particular, E_l is independent
and D_l induces six matching edges.

Every row of Y has total4, so every vertex lies in exactly four
of the D_l and exactly three of the E_l. Assign each T vertex its
three-element label

`L(i)={l:i belongs to E_l} subset {1,...,7}`.

Adjacent vertices have disjoint labels, because each E_l is
independent. Fix a vertex i. The labels of its four neighbors are
three-subsets of the four-element complement of L(i). For every
l outside L(i), the vertex i belongs to D_l, and exactly three
of those neighbors belong to E_l. Thus each of the four available
labels occurs in exactly three neighbor sets. Equivalently each
is omitted once, so the four neighbor sets are precisely all four
three-subsets of that complement, each occurring once.

The map L therefore has nonempty image closed under all neighbors
in the Kneser graph KG(7,3), whose vertices are the35 three-subsets
of a seven-set, adjacent when disjoint. This graph is connected:
two triples differing in one element have union of size4, and the
complement of their union is a triple disjoint from both, giving
a path of length2. Any two triples can be joined by successive
single-element replacements. A nonempty neighbor-closed image
must consequently contain all35 vertices of KG(7,3). It cannot
be the image of a21-element set. This is the final contradiction.

## Conclusion

Sections2--6 exhaust every possible R circle type forced by the
same actual graph. Thus the quotient `(12,21,28)` cannot occur.
Together with the two cited earlier results, this excludes exactly
three positive-support components of the weighted defect for an
arbitrary order61 target. The connected case and component counts
at least5 are not addressed by this conclusion.
