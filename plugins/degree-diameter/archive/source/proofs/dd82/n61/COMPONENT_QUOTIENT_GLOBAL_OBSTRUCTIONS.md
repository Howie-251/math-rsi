# Order61 component quotients: a global quadratic-norm obstruction

## Result and boundary

For every actual order61 weighted-defect component quotient with at
least five components, the product of the component sizes satisfies

`product_i n_i = a^2 or 5a^2` for some positive integer a.         (1)

Equivalently, in the already established size domain containing only
prime factors2,3,5,7, the total valuations at2,3 and7 must all be even.
This is a single global necessary condition on the entire size multiset;
it can be added before choosing any quotient entries.

The proof below uses the actual reversible quotient and elementary
rational linear algebra. It assumes neither a binary defect nor a graph
automorphism. It does not establish that every size multiset satisfying
(1) supports a quotient, or that any abstract quotient lifts to a graph.
No contradiction for all c>=5 has been obtained in this bounded analytic
task. The connected-defect case c=1 is not constrained further here.

Status: root/writer and fresh scoped proof-checker checked the full elementary derivation; actual
Gemini round3 accepted it in reviews/dd82/20261013_V3_n61_row_norm_review.json. No new enumeration, solver,
profile, MCP call or Lean calculation was performed. The already-read
formula-derivation/proof-writer instructions are applied with the V3 DD82
mathematical adaptation. This note belongs to
`dd82-v3-defect-components61-20261013`.

## 1. The actual quotient and its rational inner product

Use the unconditional quotient from
[GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md](GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md).
Write `c=2m+1`, `D=diag(n_1,...,n_c)`, and `n=(n_1,...,n_c)^T`.
The same actual matrix Q satisfies

`Q 1=8 1`,       `D Q=Q^T D`,       `sum_i n_i=61`,
`Q^2+Q-11I=1 n^T`.                                             (2)

All sizes are positive integers. On Q^c use the positive definite
rational inner product

`<x,y>_D=x^T D y`.

Let

`E={x in Q^c : n^T x=0} = 1^(perp_D)`.

Detailed balance and the row sum give `n^T Q=8n^T`, so E is Q-invariant.
On E, equation (2) reduces to `Q^2+Q=11I`. Thus the rational operator

`C=(2Q+I)/3` on E

is self-adjoint for this inner product and satisfies

`C^2=5I`.                                                      (3)

The polynomial `x^2-5` is irreducible over Q, so (3) makes E a vector
space over the field `K=Q(sqrt(5))`, with sqrt(5) acting by C. Its
dimension over K is m because its rational dimension is2m.

## 2. Exact determinant identity over Q(sqrt(5))

Choose any K-basis `v_1,...,v_m` of E. Then

`v_1,...,v_m,Cv_1,...,Cv_m`

is a rational basis of E. Define rational m-by-m matrices

`X_ij=<v_i,v_j>_D`,       `Y_ij=<v_i,Cv_j>_D`.

Both X and Y are symmetric, the latter by self-adjointness of C.
Equation (3) shows that the Gram matrix in this rational basis is

```
G_E = [[X,Y],
       [Y,5X]].
```

Over K, put `H=[[X,Y/sqrt(5)],[Y/sqrt(5),X]]`. Factoring sqrt(5)
from the second block of rows and columns gives

`det G_E = 5^m det H`.

The subspaces of vectors `(u,u)` and `(u,-u)` block-diagonalize H,
without any assumption that X and Y commute. Consequently

`det G_E
 = 5^m det(X+Y/sqrt(5)) det(X-Y/sqrt(5))
 = 5^m Norm_(K/Q)(alpha)`,                                     (4)

where `alpha=det(X+Y/sqrt(5))`. Positive definiteness of G_E makes
alpha nonzero. This identity is an explicit determinant calculation,
not an appeal to a classification of quadratic forms.

Let P be the rational c-by-c change-of-basis matrix with columns

`1,v_1,...,v_m,Cv_1,...,Cv_m`,

and write `delta=det P`, a nonzero rational number. Since E is
D-orthogonal to1 and `<1,1>_D=61`,

`P^T D P = diag(61,G_E)`.

Taking determinants and using (4) yields the exact identity

`(product_i n_i)/(61*5^m)
   = Norm_(K/Q)(alpha)/delta^2
   = Norm_(K/Q)(alpha/delta)`.                                 (5)

There is no ambiguity from a square class in (5): every rational square
is itself the norm of a rational element of K. Moreover,

`Norm(9+2sqrt(5))=61`,       `Norm(5+2sqrt(5))=5`.

Multiplying (5) by these norms proves that

`product_i n_i` is a nonzero norm from `Q(sqrt(5))`.              (6)

In fact (5)--(6) hold for any quotient satisfying (2), before imposing
the small-size prime restrictions.

## 3. Elementary parity of the norm valuations

Every nonzero element of K can be written
`(a+b sqrt(5))/d` with integers a,b,d and d nonzero. Its norm is

`(a^2-5b^2)/d^2`.

For p=3 or7, remove the common p-power from a and b. The resulting
a,b are not both divisible by p. The numerator cannot be divisible
by p: otherwise, when b is nonzero modulo p, 5 would be a nonzero
quadratic residue modulo p; when b is zero, a would also be zero.
But the nonzero squares are `{1}` modulo3 and `{1,2,4}` modulo7,
and5 is absent in each case. Thus the valuation of the original
numerator is twice the common p-valuation. Subtracting the denominator's
even valuation preserves its parity.

For p=2, again remove the common power of2 from a and b. If exactly
one is odd, the numerator is odd. If both are odd, their squares
are1 modulo8, so

`a^2-5b^2 = 4 (mod 8)`.

Its 2-adic valuation is exactly2. Adding back the removed common
power and subtracting the denominator's valuation changes this only
by an even integer. Therefore every nonzero K-norm has even valuation
at2,3 and7.

Apply this to (6):

`sum_i v_p(n_i) = 0 (mod 2)` for p=2,3,7.                       (7)

No general theorem about inert primes is needed for this argument.

## 4. Consequence for the existing complete size domain

The independent elementary size reduction in
[LARGE_DEFECT_COMPONENT_QUOTIENT_DOMAIN.md](LARGE_DEFECT_COMPONENT_QUOTIENT_DOMAIN.md)
shows that, for c>=5, every size has prime factors only from
`{2,3,5,7}`. Briefly, a prime p>8 dividing one size propagates across
each positive quotient interface by detailed balance, because all
positive q_ij are at most8. The quotient support is connected, so p
would divide all sizes and their sum61, impossible for a proper
component size. The other recorded size bounds do not need to be
recomputed to apply (7).

Thus the only potentially odd prime exponent in `product_i n_i`
is that of5, proving (1). This can be implemented by tracking the
three parity bits `(sum v2, sum v3, sum v7) mod 2` in the existing
size DP, or by an exact integer test on each completed size multiset.
Neither operation was run in this analytic task.

As consistency examples, the previously classified c=3 size vectors
have products

`12*21*28=84^2`,       `6*25*30=5*30^2`.

Both satisfy the new necessary condition; this observation does not
replace either realization-exclusion proof.

## 5. What remains unresolved

The norm obstruction applies uniformly to all c>=5 and couples all
component sizes at once. It is a necessary arithmetic restriction,
not a quotient construction or a proof of nonexistence for every
remaining c. Any surviving sizes must still admit a single integer Q
satisfying every equation in (2), the actual diagonal constraints,
and ultimately the same original adjacency/defect blocks. No claim
about the number of surviving size vectors is made without the actual
next filtering run. No new obligation for c=1 was established here.

Actual application after the analytic task: component_norm_screen.py filtered all142 row-moment survivors to65; its saved result is complete. Counts for c=5,7,9,11,13,15,17 are4,3,10,11,18,10,9. These remain necessary sizes, not graph realizations.
