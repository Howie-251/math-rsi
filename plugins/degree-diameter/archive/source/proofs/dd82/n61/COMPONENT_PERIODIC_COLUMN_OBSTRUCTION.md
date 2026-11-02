# Order61 component lifting: periodic columns forced by two-regular blocks

## Result and scope

The abstract quotient

```
n=(3,3,15,15,25),

Q=[[0,3,5,0,0],
   [3,0,0,5,0],
   [1,0,2,0,5],
   [0,1,0,2,5],
   [0,0,3,3,2]]
```

cannot lift to an order61 simple graph of maximum degree8 and diameter2.
The matrix really satisfies the row sums, detailed balance and
`Q^2+Q-11I=1n^T`; the obstruction is to a common binary adjacency
realization, not to this abstract integer quotient.

The reusable ingredient is a periodic-column obstruction: two coprime
Fourier periods in a binary incidence matrix force a single period,
and the resulting identical rows exceed the actual defect budget.
The five required cycle-polynomial gcds were computed exactly once.
This does not exclude every quotient edge between two-regular blocks.

Status: fresh scoped local proof-checker PASS with independent exact resonance check; same-thread Gemini round4 accepted the actual lifting proof in
`dd82-v3-defect-components61-20261013`. Existing norm and matching-edge
manuscripts are unchanged. The already-read formula-derivation,
proof-writer and experiment-bridge skills are applied with the V3 DD82
adaptation. No graph search or solver was run.

## 1. A general periodic-column obstruction

Let an actual graph have a defect matrix with zero diagonal,
nonnegative off-diagonal entries

`B_uv=(A^2)_uv+A_uv-1`

and constant defect row sum delta. Let Y be one of its binary adjacency
blocks, with rows labeled by `Z/(ab)Z`, where a,b>1 are coprime.
Suppose every column has a representation

`y(z)=f(z mod a)+g(z mod b)`                                    (1)

and has the same weight w, which is not divisible by a. Then every
column has period a. If each Y row has weight r, necessarily

`(b-1)(r-1)<=delta`.                                           (2)

To prove the first assertion, the Chinese remainder theorem makes
the values in (1) exactly `f_i+g_j` over all pairs of residues. If f
is nonconstant, choose two different values. Their nonzero difference
is, for every j, the difference of two binary entries, hence is1 or -1.
The two entries are then fixed as (1,0) or (0,1), forcing g to be
constant. Otherwise f is constant and the column has period b. But
a period-b binary column of length ab has weight divisible by a,
which is excluded. Thus each column has period a. This argument also
allows complex Fourier coefficients, since differences of the binary
entries are real.

Therefore the b rows at positions `z,z+a,...,z+(b-1)a` are identical.
Their corresponding distinct graph vertices share all r neighbors
recorded by the block. For every other vertex in this row class,
the defect entry is at least r-1. Nonnegativity of the remaining
defect entries gives (2). No assumptions about adjacency inside the
row set, or about the simplicity of B, were used.

## 2. Actual blocks for the displayed quotient

Use the same original adjacency A throughout. At order61, the degree
bound and diameter force eight-regularity, and

`B=A^2+A-7I61-J61`

is nonnegative symmetric with diagonal zero and row sum4. Its actual
components have the displayed sizes and quotient. The positive
off-diagonal quotient support is the five-cycle

`0-1-3-4-2-0`.

Let U be the size3 component indexed0, V the size15 component indexed2,
and W the size25 component indexed4. U is independent; the induced
adjacency matrices S on V and T on W are two-regular. Write

`X=A_(U,V)` of size `3 x 15`, row sum5, column sum1;
`Y=A_(V,W)` of size `15 x 25`, row sum5, column sum3.

The two corresponding quotient edges have no common third support
neighbor, so the zero cross blocks of the actual B give exactly

`X+XS=J_(3,15)`,
`SY+YT+Y=J_(15,25)`.                                          (3)

In particular, no unspecified route through another component is
being dropped. The same argument could start with the other size3
and size15 pair, but one pair suffices.

## 3. Integer block sums force S=C15

Take any p-cycle of S and the corresponding three-by-p column block
X_p. The first identity in (3) gives `X_p(I+C_p)=J_(3,p)`.
Its row sums are p/3, so p is divisible by3.

Next take any p-cycle of S and any q-cycle of T. Let Z be the
corresponding p-by-q block of Y. The second identity in (3) restricts to

`C_p Z+Z C_q+Z=J_(p,q)`.

Its row-sum and column-sum vectors r,c obey

`(C_p+3I)r=q1`,       `(C_q+3I)c=p1`.

Cycle eigenvalues lie in [-2,2], so these matrices are invertible;
their row sums are5. Consequently

`r=(q/5)1`,       `c=(p/5)1`.

These are integer counts. Every S cycle therefore has length divisible
by both3 and5. As S has15 vertices, it is a single C15. Every T cycle
has length divisible by5, and so its length belongs to

`{5,10,15,20,25}`.                                              (4)

No classification of T's possible cycle partitions is required.

## 4. Exact resonance table and column periods

Define integer polynomials

`L_0(x)=2`, `L_1(x)=x`, `L_p(x)=xL_(p-1)(x)-L_(p-2)(x)`.

The characteristic polynomial of the cycle C_p is
`chi_p(x)=L_p(x)-2`. This follows from
`L_p(z+z^(-1))=z^p+z^(-p)`, with the cycle eigenvalues
`2cos(2pi k/p)` and their usual multiplicities.

Put `f(x)=x^2+x-1`. The complete five-entry exact table needed here is

| q | monic `gcd(chi_15(x),chi_q(-1-x))` |
|---|---|
| 5 | `f(x)^2` |
| 10 | `f(x)^2` |
| 15 | `f(x)^2` |
| 20 | `(x+1)^2 f(x)^2` |
| 25 | `f(x)^2` |

The multiplicity-two factor at q=20 is included explicitly.
The source is
[`component_3_3_15_15_25_resonance.py`](../../../computations/dd82/n61/component_3_3_15_15_25_resonance.py),
and the complete coefficient/cofactor record is
[`component_3_3_15_15_25_resonance.result.json`](../../../computations/dd82/n61/component_3_3_15_15_25_resonance.result.json).
The program reuses only exact rational polynomial arithmetic from the
previous calculation; importing it does not execute that earlier table.
This new five-entry run completed under a one-CPU-second hard limit,
using 0.004077951 internal CPU seconds and 0.008001383 wall seconds.
No floating-point eigenvalues, graph enumeration or solver are involved.

Here is the precise implication of the table. For a q-cycle of T,
its block Z satisfies

`C15 Z+Z C_q+Z=J_(15,q)`.

If u is a nonconstant C15 Fourier vector with eigenvalue lambda, then

`u^* Z (C_q+(lambda+1)I)=0`.

Thus `u^*Z` must vanish unless lambda is an eigenvalue of C15 and
`-1-lambda` is an eigenvalue of C_q. The gcd table lists all such
lambda: the two roots of f, whose C15 Fourier modes have exact
order5, and possibly -1, whose modes have exact order3. The constant
mode is unrestricted by this argument. It follows that every column
of the entire Y has the form

`y(z)=f_0(z mod5)+g_0(z mod3)`,       z in Z/15Z.                 (5)

This conclusion uses the same S=C15 and all actual T-cycle blocks
of Y, not independently chosen incidence certificates.

## 5. The defect contradiction

Every Y column has weight3. Apply Section1 to (5), with

`a=5`,       `b=3`,       `w=3`,       `r=5`,       `delta=4`.

A period3 column would have weight divisible by5, so all columns
have period5. Hence rows z,z+5,z+10 of Y are identical. Each of
the corresponding three vertices shares five W-neighbors with
each of the other two. Its actual defect row therefore has sum
at least

`2*(5-1)=8>4`,

a contradiction. This excludes every graph lift of the displayed
quotient and its relabelings. No other one of the65 screened size
patterns is declared excluded by this particular application.
