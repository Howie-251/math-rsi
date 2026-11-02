# The actual new C5 quotient has no diameter-two lift

**Theorem.** The matrix saved in
[`cyclic5_full60_quotient_run/best_quotient.json`](../../../computations/dd82/construction/cyclic5_full60_quotient_run/best_quotient.json)
is not the quotient of a simple degree-eight, diameter-two graph under
the specified free C5 action. The obstruction is purely mathematical;
no voltage enumeration or solver result is used.

The proof also excludes the following more general architecture:
two halves each consisting of six disjoint pentagons, with a perfect
matching between every pair of opposite pentagons, each matching
mapping cycle adjacency to cycle nonadjacency. The matching orientations
are arbitrary. This architecture need not preserve the original free
C5 action, and its exclusion is not asserted to close all free-C5
order60 graphs or arbitrary order60 graphs.

The original proof has been read by root and a fresh same-family
proof-checker, whose completed
[audit record](../../../reviews/dd82/proof-checker-c5-twelve-pentagons-20261013/PROOF_AUDIT.md)
reports no gap. Same-thread Gemini round3 also accepted that argument
([original response](../../../reviews/dd82/20261013_V3_c5_quotient_obstruction_review.json)).
These are mathematical reviews, not Lean or a machine-checked proof
certificate. The broader corollary and second instance added below
were subsequently checked by root and the author and accepted in
[same-thread round4](../../../reviews/dd82/20261013_V3_c5_generalized_obstruction_review.json).
They are not represented as covered by the earlier local audit or round3.

**Structural corollary used by the next quotient search.** The same
conclusion holds for every quotient M for which D is exactly two K6
components and the restriction of M to each six-label component is one
diagonal-two isolated label plus a unit-edge C5 on the other five labels.
Indeed Section 1 uses only these properties to obtain the two half-graphs
and equation (1); the remainder does not depend on particular cross-half
entries of the saved M. This does not exclude other quotients with D=2K6.

**More general structural corollary.** It suffices that the twelve
labels admit a partition into two six-element sets U,V such that

1. `D_ab=0` for every `a in U, b in V`;
2. each induced principal block `M[U]`, `M[V]` consists of a unit-edge
   C5 and one isolated label with diagonal entry two (all other entries
   in that block are zero).

No condition that `D[U]` or `D[V]` is a clique is needed. In a
hypothetical target, condition 1 and actual B nonnegativity give the
zero 30-by-30 cross block. Condition 2 gives the same two 2-factors
`6 C5` or `C5+C25`, each with cross-degree six, and hence equation (1).
Sections 2--8 use only that equation, the indicated cycle lengths,
degree eight, full distance-two coverage, and the actual B row budget
five. They never use either within-half block of D. Thus the previous
`D=2K6` sufficient condition is retained as a special case of this
broader one. The two sets need not be individual components of D;
the stated zero cross block is the precise hypothesis.

This clarification and the new instance below were checked locally
after the original proof reviews cited above; those earlier receipts
are not represented as reviews of the added instance.

## 1. What the actual quotient forces

Write A for the adjacency matrix of a hypothetical target, and

`B = A^2 + A - 7I60 - J60`.

Then B is nonnegative with zero diagonal and row sum five. For the
twelve size-five vertex orbits, its quotient is
`D = M^2 + M - 7I12 - 5J12`.

The saved matrix has

`U = {0,1,4,7,8,10}`, `V = {2,3,5,6,9,11}`,

and D is the adjacency matrix of the two disjoint cliques on U and V.
In particular every entry of D from U to V is zero. Because actual B
entries are nonnegative, this means the entire actual 30-by-30 cross
block of B is zero, not merely that its aggregate is zero.

Inside U, the nontrivial quotient cycle is

`0 -- 4 -- 1 -- 8 -- 10 -- 0`,

with unit interfaces, and the remaining orbit 7 has internal degree
two and no other U-neighbor. Inside V the corresponding cycle is

`3 -- 6 -- 5 -- 9 -- 11 -- 3`,

and orbit 2 has internal degree two and no other V-neighbor. These
statements follow directly from the saved entries of M. Every row has
internal-half degree two and cross-half degree six.

A lift of a unit-interface quotient pentagon is either five pentagons
or one 25-cycle: going once around its five interfaces translates the
fiber coordinate by a total voltage delta in Z5; delta zero gives
five cycles of length five, while nonzero delta has order five and
gives one cycle of length 25. Each isolated internal orbit is itself
a pentagon. Therefore the two actual half-graphs are 2-factors R and
T, each of shape `6 C5` or `C5 + C25`.

Let X be the actual binary cross-adjacency matrix, with every row and
column sum six. In this order the full adjacency matrix is

`A = [[R, X], [X^T, T]]`.

The zero cross block of B gives the exact equation

`R X + X T + X = J30`.                                           (1)

### 1a. The subsequent escape quotient also satisfies the broader condition

The second saved matrix is
[`cyclic5_full60_quotient_escape_run/best_quotient.json`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_run/best_quotient.json).
For it, take

`U = {0,4,6,7,10,11}`, `V = {1,2,3,5,8,9}`.

Its U block has unit cycle `0--4--7--10--6--0` and isolated diagonal-two
label 11. Its V block has unit cycle `1--3--2--8--5--1` and isolated
diagonal-two label 9. The 36 entries of `D[U,V]` are all zero.
All twelve rows of M sum to eight, and each has within-half degree two
and cross-half degree six. Direct recomputation of `M^2+M-7I-5J`
equals the saved D, whose entries are nonnegative and rows sum to five.

Here the D diagonal is two at all labels except 9 and 11, where it is
zero. Thus D is not two K6 components, but the broader corollary
applies and excludes every diameter-two free-C5 lift of this matrix.
Its passage through a search filter checking only the former
`D=2K6` condition does not escape the proved Sylvester obstruction.

This is one direct 12-by-12 arithmetic and structural check, recorded in
[`best_quotient.pentagon_obstruction.json`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_run/best_quotient.pentagon_obstruction.json),
with reproducible source
[`cyclic5_full60_quotient_escape_structure_check.py`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_structure_check.py).
It used 0.000742685 CPU seconds. No quotient enumeration, voltage
assignment, solver or graph-distance computation was performed.

## 2. The five-term root-of-unity lemma

Let eta be a primitive 25th root of unity. If

`1 + eta^r + eta^(-r) + eta^s + eta^(-s) = 0`,                     (2)

then the multiset `{r,-r,s,-s}` modulo 25 is exactly
`{5,10,15,20}`.

First r and s cannot be zero modulo 25: if one is zero, the left-hand
side is at least `3-2=1` as a real number. Choose exponents in
`{0,...,24}` and let f(x) be the five-term polynomial in (2), allowing
coincident terms to add. It has nonnegative integer coefficients,
constant coefficient one, and f(1)=5.

The minimal polynomial is

`Phi25(x) = 1 + x^5 + x^10 + x^15 + x^20`.

For completeness, irreducibility follows from Eisenstein at five after
substitution x+1: modulo five this substituted polynomial is x^20,
and its constant coefficient is five, not divisible by 25. Thus
`f = Phi25 * g` with degree(g) at most four. The five translates of g
occupy disjoint degree intervals, so each coefficient of g appears
unchanged at the five exponents of its residue class modulo five.
Consequently every coefficient of g is nonnegative. Its constant
coefficient is one and `g(1)=f(1)/Phi25(1)=1`, so g=1. Hence f=Phi25,
which proves the lemma.

In spectral terms, for adjacency eigenvalues lambda and mu of cycles
whose lengths are five or 25,

`lambda + mu + 1 = 0`

can occur only when both modes are nontrivial fifth-root modes, with
the two complementary frequency classes. In particular a primitive
25th-root mode has no partner.

## 3. Neither half can contain a 25-cycle

Restrict (1) to a cycle of length p in R and a cycle of length q in T,
where p,q belong to `{5,25}`. The relevant block Y satisfies

`C_p Y + Y C_q + Y = J_(p,q)`.                                   (3)

Diagonalize the two cycle matrices by their finite Fourier bases.
For mode indices r,s the coefficient of the transformed Y is multiplied
by `lambda_r + mu_s + 1`. The transformed right-hand side is zero
unless both modes are constant.

If p=25, every row-frequency r not divisible by five has nonzero
multiplier against every column mode, by Section 2. All these
coefficients of Y vanish. The remaining row frequencies are multiples
of five, so each column of Y is periodic with period five along the
25-cycle. This holds against every cycle of T; hence the complete
cross-neighborhoods of positions

`t, t+5, t+10, t+15, t+20`

are identical. Each has six cross-neighbors. The five positions are
pairwise nonadjacent in their 25-cycle, so for a fixed one of them,
each of the other four has at least six common neighbors with it.
The corresponding four B entries are at least five each, contrary
to B's row sum five. The transposed argument excludes q=25 as well.

Thus R and T are each exactly six disjoint pentagons.

## 4. Every opposite pair of pentagons is joined by an anti-cycle matching

Take a 5-by-5 block P of X between one pentagon in each half. Its
equation is

`C P + P C + P = J5`,                                            (4)

after choosing standard cycle coordinates on both pentagons. If
`y=P 1`, multiplication by 1 gives `(C+3I)y=5 1`. The matrix C+3I is
invertible, since C has all eigenvalues in [-2,2], and y=1 is a
solution. Therefore every row of P sums to one. Applying the same
argument to the transpose gives column sums one. Since P is binary,
it is a permutation matrix.

Multiplying (4) on the right by P^T yields

`P C P^T = J5 - I5 - C`.                                        (5)

The matched image of an adjacent cycle pair is therefore nonadjacent
in the opposite pentagon. In coordinates t in F5, every such matching
has the form

`f_ij(t) = 2 epsilon_ij t + a_ij`,

where `epsilon_ij in {+1,-1}`, `a_ij in F5`, and `0 <= i,j < 6` index
the two sets of pentagons. This follows by identifying the complement
of the standard pentagon with its step-two cycle. No uniformity of
the 36 signs has been assumed.

## 5. Six covering dihedral permutations have only four sign counts

For two different pentagons in the same half, the six possible
two-step routes go through the six opposite pentagons. Each route is
a composition of two maps in Section 4 and hence a dihedral
automorphism of C5. Coverage implies

`sum_(j=0)^5 Q_j = J5 + W`,                                      (6)

where W is a permutation matrix: the difference is nonnegative
integral with every row and column sum one. Every Q_j commutes with
C, and J5 does as well, so W commutes with C. A permutation commuting
with C preserves its adjacency and is a dihedral automorphism.

Let A_x count rotations `t -> t+x` among the six Q_j and B_y count
reflections `t -> -t+y`. At source t and target u the coverage count
is `A_(u-t)+B_(u+t)`. The map `(t,u) -> (u-t,u+t)` is a bijection of
F5 squared. Subtract the one rotation or reflection representing W
from its corresponding count. Equation (6) becomes

`A'_x + B'_y = 1` for every x,y in F5.

Thus A' is constant, B' is constant, and the two constants are
nonnegative integers summing to one. Nonnegativity of the adjusted
constant holds even for the family from which W was subtracted:
the other four unadjusted entries are nonnegative and equal to it.
It follows that five of the permutations consist of all five
rotations, or of all five reflections, plus the residual W.

In particular, the number of rotations among the six is one of
`0,1,5,6`. Hence any two rows of the sign matrix epsilon have Hamming
distance in `{0,1,5,6}`. The same argument to two pentagons in the
other half gives the identical condition for every pair of columns.

## 6. The sign matrix reduces to all positive or a single negative

Reversing a pentagon's coordinate multiplies the corresponding row
or column of epsilon by -1; constants a change but remain arbitrary
elements of F5. These are legitimate vertex relabelings.

First switch columns so the first row is positive. Each other row
then has 0,1,5 or 6 negative entries. Switch individual rows to make
each have at most one negative. Two such rows cannot have their
negative entries in different columns, since their distance would
be two. Therefore all negatives are in a single column, if any.

That column's distance from an all-positive column is in
`{0,1,5,6}`. Its first entry is positive, so there are at most five
negatives. Zero gives the all-positive case; one gives a single
negative; five becomes a single negative after switching the column.
Relabeling the pentagons puts the single negative at `(0,0)`.

This proves the reduction, rather than assuming that the original
signs factor as row and column signs.

## 7. The all-positive case

If every epsilon is positive, all cross maps are `t -> 2t+a_ij`.
Simultaneously translate every left pentagon by +1 and every right
pentagon by +2. This is a free order-five automorphism of the full
graph, since it preserves both internal cycles and all cross maps.
Its twelve vertex orbits are the twelve pentagons, so its quotient
is `2I + A(K6,6)`.

This contradicts
[CYCLIC5_K66_QUOTIENT_EXCLUSION.md](CYCLIC5_K66_QUOTIENT_EXCLUSION.md).
The automorphism just constructed need not be the original one that
defined M. The old exclusion is invoked only after constructing the
required action, so no identification of the two partitions is assumed.

## 8. The single-negative case

Assume epsilon_00=-1 and every other epsilon is +1. For a regular
row i>0 and row 0, the five routes through columns j>0 are rotations
with translation `3(a_0j-a_ij)`; the route through column 0 is a
reflection. Section 5 forces those five rotations to be the five
distinct translations. Since multiplication by -3 is invertible
in F5, this says

`{a_ij-a_0j : 1 <= j <= 5} = F5` as a multiset.                   (7)

In particular, every regular row has the same tail sum:

`sum_(j=1)^5 a_ij = sum_(j=1)^5 a_0j` in F5.                     (8)

Let zeta be a primitive fifth root, let Z be the 5-by-5 matrix
`Z_ij=zeta^(a_ij)` for i,j>0, and let w be the nonzero row vector
`w_j=zeta^(a_0j)`, j>0. Equation (7) gives

`Z w* = 0`.                                                     (9)

Now take two distinct regular rows i,k>0. All six composed routes
are rotations. Their six translation values contain F5 once plus
one repeated value. Removing the common invertible factor 3, the
same statement holds for the six differences `a_ij-a_kj`.
The repeated difference equals their sum, since the sum of F5 is
zero. By (8) this sum is exactly `a_i0-a_k0`. Consequently

`sum_(j=0)^5 zeta^(a_ij-a_kj) = zeta^(a_i0-a_k0)`.

Canceling the j=0 term shows that distinct rows of Z are orthogonal.
Each row has squared norm five. Therefore

`Z Z* = 5I5`.

Z is invertible, contradicting (9) and the fact that w is nonzero.
The sign-reduced cases are both impossible, completing the theorem.

## Scope and remaining problem

The chain is complete for each of the two saved actual quotients, and
for every quotient satisfying the broader structural corollary:
`M -> two actual 30-point 2-factors -> exact Sylvester equation ->
no C25 -> twelve pentagons with anti-cycle matchings -> sign
classification -> contradiction`.
Every use of defect nonnegativity concerns the same hypothetical
original graph A. The result does not close the remaining free-C5
quotients. In particular, the successful necessary-quotient search
did not itself construct a target graph; this proof explains why both
saved complete quotients cannot be lifted. The second application
does not require the defect to equal two cliques and does not exclude
the remaining free-C5 quotients.

This task used the previously read project-local `formula-derivation`
and `proof-writer` instructions with the V3 DD82 adaptation. It did
not enumerate a new family, run a solver or graph-distance check,
perform Lean work, or alter shared navigation files.
