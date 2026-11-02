# Order 63 exclusion by a finite cyclotomic norm table

Status: complete paper argument with exact integer arithmetic certificate;
fresh Codex proof-checker and fresh Gemini review found no mathematical gap.
The Codex reviewer independently verified all63 norms by multiplication determinants.
Lean implementation remains pending. See reviews/dd82/proof-checker-n63-trace-20261011/
and reviews/dd82/20261011_N63_cyclotomic.json for actual reviewed scope. This is an independent route,
not a certification of the older defect-two classification papers.

## Statement and original scope

There is no finite simple undirected graph on 63 vertices with maximum degree at
most 8 and diameter at most 2. No symmetry, vertex-transitivity, prescribed local
template, SAT result, or inherited triangle classification is assumed.

Together with the separate exclusions of orders 64 and 65 and the Moore bound
in `../FOUNDATIONS.md`, this would give an arbitrary-graph upper bound of 62.
It does not identify the exact value of N(8,2).

## 1. Actual graph and the defect multigraph

Suppose such a graph G exists. The root bound |V| <= 1+8 deg(v) implies that
G is 8-regular. Let A be its ordinary 0/1 adjacency matrix and put

    B = A² + A - 7I - J.

The standard original-graph identities give: B is a symmetric integer matrix,
has zero diagonal, is entrywise nonnegative, has every row sum 2, and commutes
with A. Here diagonal zero follows from deg(v)=8; off-diagonal nonnegativity
is exactly the length-at-most-two condition; the row sum is 64+8-7-63=2.
Commutation uses AJ=JA=8J. These identities have separately been connected to
the original graph predicates in `formal/DegreeDiameter/Defect.lean`.

A row containing an entry 2 forces the corresponding two vertices to form a
whole component consisting of one doubled edge. In every other component all
positive entries are 1, and each vertex has exactly two distinct neighbors.
Thus each such component is an ordinary cycle of length between 3 and 63.
This classification concerns B, not the original adjacency graph G.

The spectrum of a doubled edge is {2,-2}. The eigenvalues of the adjacency
matrix of a cycle of length l are 2 cos(2 pi j/l), 0 <= j < l: the vectors
(1,zeta^j,...,zeta^((l-1)j)) give this directly. Every such eigenvalue has the
form mu=zeta+zeta^-1 for a primitive root of unity of order ell <= 63.
Orders ell=1,2 give mu=2,-2 respectively.

## 2. The precise finite arithmetic lemma

For every such conductor ell other than 3, the element 29+4mu is not a square
in K=Q(mu). For ell=3, mu=-1 and 29+4mu=25.

Here is a finite exact certificate of this assertion. Let C_ell be the monic
minimal polynomial of mu. For ell=1,2 it is x-2,x+2. For ell>=3 let
d=phi(ell)/2. The cyclotomic polynomial satisfies

    Phi_ell(t) = t^d C_ell(t+t^-1).

Indeed Q(zeta) has degree phi(ell), whereas its real subfield Q(mu) has half
that degree: zeta solves z²-mu z+1=0 and is nonreal. The displayed polynomial
is monic of degree d, annihilates mu, and therefore is its minimal polynomial.

The field norm in question is the positive integer

    N_ell = Norm_K/Q(29+4mu) = (-4)^d C_ell(-29/4).

If 29+4mu were a square in K, N_ell would be a square in Q, hence an integer
square. The accompanying table gives, for each ell != 3, a modulus m and a
residue N_ell mod m outside the set {a² mod m: 0 <= a < m}. The largest modulus
needed is 47. The one exception is C_3=x+1 and N_3=25.

Full table: `computations/dd82/construction/n63_cyclotomic_norms.table.md`.
All coefficients, exact norms, integer-square brackets, and residue sets:
`computations/dd82/construction/n63_cyclotomic_norms.json`.
Generator/checker: `computations/dd82/construction/n63_cyclotomic_norms.py`.

The arithmetic procedure is specified without an algebra system:

1. Generate Phi_ell by dividing t^ell-1 by the previously generated Phi_d for
   all proper divisors d of ell. Each monic integer division has zero remainder.
2. Set F_0=2, F_1=x and F_(j+1)=x F_j-F_(j-1). Then F_j(t+t^-1)=t^j+t^-j.
   Writing Phi_ell(t)=sum a_k t^k gives
   C_ell(x)=a_d + sum_(j=1)^d a_(d+j) F_j(x).
3. Check the full polynomial identity t^d C_ell(t+t^-1)=Phi_ell(t) by binomial
   expansion with integer coefficients.
4. If C_ell=sum c_j x^j, compute N_ell=sum c_j 29^j (-4)^(d-j).
   Check its stated residue against every square residue modulo m. An additional
   direct bracket k²<N_ell<(k+1)² is included in the data.

The actual standard-library execution checked all 63 conductors, with 62
nonsquare norms and the sole exception ell=3, and all polynomial identities.
This is a small finite arithmetic check, not a graph enumeration. The data do
not by themselves certify the graph-to-field argument; that is given here.

## 3. Rational eigenspace trace lemma

Let K be a subfield of R, mu in K, and let T be a K-linear endomorphism of a
finite-dimensional K-vector space U with

    T² + T - (7+mu) Id = 0.

If 29+4mu is not a square in K, the polynomial q_mu(x)=x²+x-7-mu is
irreducible over K. The action makes U a vector space over the quadratic
field L=K[x]/(q_mu), where x acts as T. A basis of U over L, expanded by
the basis (1,x) of L over K, splits T into 2-by-2 blocks, each with trace -1.
Consequently dim_K U is even and tr_K T=-(dim_K U)/2. The assertion includes
the zero-dimensional space. Scalar extension to R preserves dimension and trace.

Merely pairing real roots would not justify equal multiplicities. It is this
K-linear structure and irreducibility that justify the trace formula.

## 4. Apply the lemma on the complement of the constants

Let W={v in R^63: sum v_i=0}. It has dimension 62, is defined over Q, and is
invariant under both symmetric regular matrices A and B. On W, J acts as zero,
so

    A² + A = 7I + B.

The symmetric matrix B decomposes W into its real eigenspaces U_mu. Since
AB=BA, A preserves each U_mu. For any eigenvalue mu, set K=Q(mu); the same
eigenspace is obtained by extending to R the K-space

    {v in K^63 : Bv=mu v and sum v_i=0}.

This space is defined by a matrix of equations over K, so extension to R
preserves its dimension and recovers the full real eigenspace. The restricted
A is K-linear and satisfies q_mu(A)=0.

For mu != -1, Section 2 and Section 3 therefore give

    tr(A restricted to U_mu) = -dim(U_mu)/2.

In particular this applies to the mu=2 part INSIDE W, with discriminant 37.
The single all-ones direction is outside W and is kept separate; on it A=8.

For mu=-1 the polynomial is (x-2)(x+3). Let p and q be the dimensions of the
2- and -3-eigenspaces of A on U_(-1). These are nonnegative integers; their
sum is dim U_(-1), and their trace contribution is 2p-3q.

All remaining eigenspaces have total dimension 62-p-q. As A has zero diagonal,

    0 = tr A
      = 8 - (62-p-q)/2 + 2p - 3q
      = -23 + 5(p-q)/2.

Thus 46=5(p-q), impossible for integers p,q. This proves the claimed exclusion.

## Remaining formal obligations

The graph-to-defect identities already have compiled original-graph callers.
The remaining Lean work is the row-two component/spectral coverage, cyclotomic
norm lemma and finite certificate reflection, eigenspace field argument, and
final arbitrary-graph caller. None is inserted as an axiom. No complete Lean
upper bound 62 is claimed by this paper or by the finite table alone.
