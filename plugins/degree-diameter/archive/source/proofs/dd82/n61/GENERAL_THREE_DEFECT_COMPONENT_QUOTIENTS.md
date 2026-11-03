# Arbitrary order61 targets: the exact three-defect-component obligation

## Result and current scope

For any simple order61, maximum-degree-eight, diameter-two graph whose
actual weighted defect has exactly three support components, the
component sizes and adjacency quotient must, after reordering, be one
of the following two pairs:

```
n = (12,21,28),       Q = [[1,0,7],
                          [0,4,4],
                          [3,3,2]];

n = (6,25,30),        Q = [[3,0,5],
                          [0,2,6],
                          [1,5,2]].
```

The reduction is unconditional: it assumes neither simplicity of the
defect matrix nor CP02's H/no-O hypotheses. One complete short integer
check yielded these two possibilities. Immediately after that enumeration,
both remained unlifted and unexcluded. The companion (6,25,30) exclusion
has since received a fresh local mathematical check and Gemini review;
the (12,21,28) realization remains outside the initial classification.
This is not a proof that the defect is connected or an
order61 exclusion. Other possible component counts remain
`c=1,5,7,9,11,13,15,17` and were not enumerated here.

Status: exact local reduction plus finite necessary-quotient classification.
Fresh proof-checker and Gemini direction review found no mathematical gap
in this reduction and the initial section5 necessary conditions. The sole
minor stale-status wording was corrected. See reviews/dd82/proof-checker-n61-components-20261013/
and reviews/dd82/20261013_V3_n61_components_direction.json. No solver result
or Lean proof is claimed.

## 1. The actual historical boundary

The recovered
[n61 CP02 theory](../../../context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/theory/n61/i12_cp02_theory.md)
proves defect connectivity in its stated scope `H and G and not O`,
using the inherited P/T/W types, simplicity of the defect in that
scope, and five-neighbor propagation. H includes historical root
closures/RAW evidence; O quantifies fifteen complete marked outlet
obligations over all legal roots of the same graph. Neither guard can
be discarded. In particular, that conditional connectivity theorem
does not close the general weighted-defect cases considered here.

The actual CP02 INSIDE run was one logical input with 55 seeds, all
timing out after the declared twelve hours; its added mathematical
constraint was the global W bound, while the new connectivity and
several later structural interfaces were not implemented. See the
[recovery record](../../../context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/evidence/n61/cp02_recovery.json)
and [results](../../../context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/materials/n61/20260929_cp02_results.md).
Those are terminal historical records, not current jobs or whole-order
exclusions. This task does not rerun or recertify them.

## 2. Unconditional component quotient from the original graph

Let A be the adjacency matrix of an arbitrary target G. A vertex of
degree at most seven could reach at most `1+7+7*7=57` vertices in two
steps. Hence G is eight-regular, with 244 edges. Define the actual
matrix

`B = A^2 + A - 7I61 - J61`.

Its diagonal is zero; every off-diagonal entry is the number of
length-one/two routes minus one, hence is a nonnegative integer.
B is symmetric with row sum `64+8-7-61=4`. Since A is regular,
it commutes with J and therefore with B. B is not assumed binary.

Let `C_1,...,C_c` be the connected components of B's positive support,
with sizes n_i. Each size is at least two because B has zero diagonal
and positive row sum. The eigenvalue-four space of B is exactly the
space of component-constant vectors: on a component, a coordinate
attaining the maximum of a real four-eigenvector equals a positively
weighted average of its neighbors, forcing equality along every
support edge, and hence on the entire component. Conversely each
component indicator is a four-eigenvector.

Because AB=BA, A preserves that space. In particular, `A 1_(C_j)`
is constant on every C_i. Its value q_ij is the number of graph
neighbors in C_j of any vertex in C_i. Thus Q is a nonnegative
integer matrix satisfying

`Q 1 = 8 1`,       `n_i q_ij = n_j q_ji`.                        (1)

This is the actual adjacency quotient, not a separately chosen
surrogate. On component-constant vectors B acts as 4I and J as
`1 n^T`, so the original identity gives

`Q^2 + Q - 11I_c = 1 n^T`,       `sum_i n_i = 61`.               (2)

Detailed balance makes Q similar to a real symmetric matrix.
The eigenvalue eight is simple, since G is connected and any quotient
eight-eigenvector lifts to an eight-eigenvector of A. On `n^T x=0`,
(2) gives `Q^2+Q-11I=0`, whose roots are
`(-1+3 sqrt(5))/2` and `(-1-3 sqrt(5))/2`.
The characteristic polynomial of Q has integer coefficients, so the
two irrational conjugate roots have equal multiplicity m. Therefore

`c=2m+1`,       `trace(Q)=8-m`.                                  (3)

Nonnegative diagonal entries imply `m<=8`, giving odd `c<=17`.
These statements use none of the CP02 P/T/W properties.

## 3. Complete finite check for c=3

When c=3, equation (3) gives trace seven. Every row of Q is one of
the 45 triples `(a,b,8-a-b)` with `a,b>=0` and `a+b<=8`. The program
therefore visits every one of the `45^3=91,125` labeled matrices.
It applies only necessary tests, in this order:

| Test | Remaining labeled matrices |
|---|---:|
| All nonnegative rows of sum eight | 91,125 |
| Trace seven | 9,108 |
| `Q^2+Q-11I` has identical rows n, `n_i>=2`, `sum n_i=61` | 72 |
| All detailed-balance identities in (1) | 12 |
| `q_ii<n_i` and `n_i q_ii` even (simple induced graph and handshake) | 12 |

All twelve matrices and their sizes are retained in
[`component_quotient_three.result.json`](../../../computations/dd82/n61/component_quotient_three.result.json).
They are the six simultaneous row/column permutations of each pair
displayed at the start; the distinct component sizes make the six
labelings in each class distinct. Each displayed pair also directly
satisfies (1)--(3). No actual component graph or B matrix is asserted
to exist for either pair.

Source:
[`component_quotient_three.py`](../../../computations/dd82/n61/component_quotient_three.py).
The single complete run used 0.102128582 CPU seconds and 0.102157239
wall seconds. Solver calls and graph searches were zero. No c>=5
enumeration or additional candidate search was started.

## 4. The concrete remaining lifting obligation

Both surviving quotients have `q_12=q_21=0`. With components in the
displayed order, the same actual adjacency matrix must be

```
A = [[S,   0,   X],
     [0,   T,   Y],
     [X^T, Y^T, R]].
```

S,T,R must be symmetric binary matrices with zero diagonal; X,Y
must be binary. Their exact degrees and sizes are:

| Sizes | S | T | R | X row/column degrees | Y row/column degrees |
|---|---|---|---|---|---|
| `(12,21,28)` | degree-one matching on12 | four-regular on21 | two-regular on28 | `12x28`, 7 / 3 | `21x28`, 4 / 3 |
| `(6,25,30)` | cubic on6 | two-regular on25 | two-regular on30 | `6x30`, 5 / 1 | `25x30`, 6 / 5 |

Because different B components have zero cross defect, the three
exact, load-bearing equations are

`X Y^T = J_(n1,n2)`,
`S X + X R + X = J_(n1,n3)`,
`T Y + Y R + Y = J_(n2,n3)`.                                    (4)

The diagonal defects must come from those very same matrices:

```
B_1 = S^2 + S + X X^T       - 7I_(n1) - J_(n1),
B_2 = T^2 + T + Y Y^T       - 7I_(n2) - J_(n2),
B_3 = R^2 + R + X^T X+Y^T Y - 7I_(n3) - J_(n3).
```

Each must be entrywise nonnegative. Zero diagonals and row sums four
then follow from the prescribed degrees and the respective quotient
identity. To represent exactly the proposed three support components,
each B_i must additionally have connected positive support.

These conditions give a precise candidate-preserving obligation. If
the binary matrices satisfy (4) and the nonnegative diagonal-defect
conditions, their assembled A is a complete simple eight-regular
order61 graph with `A^2+A-7I-J >= 0`, hence diameter at most two.
With the three support-connectivity conditions it has exactly the
specified B components. Conversely, every target in the c=3 branch
produces such matrices. S,T,R and the two incidence matrices cannot
be chosen as independent certificates with incompatible shared blocks.

No cubic-six classification, cycle decomposition, or realization
search was performed here. A proof that both systems have no binary
solution would close the **entire c=3 branch for arbitrary order61
targets**, rather than one imposed construction family. It would
still leave c=1 and the unexamined odd counts c>=5. This is the
specific new executable mathematical obligation furnished by the
short check; there is no current all-order61 conclusion.

## 5. Subsequent local reduction of the (12,21,28) type

This necessary-condition lemma was checked by root and the local derivation agent after the initial quotient enumeration. It is not yet a fresh proof-checker or external acceptance. The separate complete local draft for the other type is [THREE_COMPONENT_6_25_30_EXCLUSION.md](THREE_COMPONENT_6_25_30_EXCLUSION.md), also pending those reviews.

For the (12,21,28) type, every cycle of R has length divisible by4, and R has at least five cycles. Consequently its cycle lengths are exactly one of

`(12,4,4,4,4), (8,8,4,4,4), (8,4,4,4,4,4), (4,4,4,4,4,4,4)`.

To prove this, take a q-cycle of R and let Z be the corresponding twelve-by-q column block of X. The same actual block equation (4) gives `SZ+ZC_q+Z=J`. Its row sums r satisfy `(S+3I)r=q*1`. Since S is a matching, its eigenvalues are +/-1, so this matrix is invertible and `r=(q/4)*1`. The entries of r are integers; hence4 divides q.

Here `B_1=XX^T+S-6I-J` is the actual nonnegative symmetric row-four defect block. Let `E={v:Sv=v,1^T v=0}`. The six matching edges give dim E=5. Every eigenvalue of B_1 is at least-4 (its absolute eigenvalues are bounded by its nonnegative row sum). Therefore for v in E, `||X^T v||^2=v^T(B_1+5I)v >= ||v||^2`. Thus X^T is injective on E. Transposing (4) and applying v yields `R X^T v=-2 X^T v`; hence R's -2 eigenspace has dimension at least5. Each even cycle has exactly one -2 eigenvector, so R has at least five cycles. Partitioning28 into at least five positive multiples of4 gives precisely the four listed types.

No binary-defect assumption, extra symmetry, imposed group action or hypothesis from CP02 is used. This does not solve the shared X,Y,T realization or exclude this quotient.
