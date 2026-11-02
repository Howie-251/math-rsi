# Proposed n63 exclusion using rational characteristic polynomials

Status: self-contained paper route and Lean implementation roadmap, not a compiled n63 exclusion. The already compiled original-graph bound remains 63. This route reorganizes the reviewed paper ../proofs/dd82/construction/N63_CYCLOTOMIC_SPECTRAL_OBSTRUCTION.md to avoid real spectral decompositions, real-subfield embeddings, and the K-linear half-dimension trace theorem. It still requires the stated graph and arithmetic lemmas to be proved.

## 1. From the original graph to a permutation defect

Assume an actual original graph G on 63 vertices, maximum degree at most 8, and the explicit edge-or-two-edge-path diameter condition. The existing Moore and Defect modules prove that G is eight-regular and its integer matrices satisfy

A²+A=7I+J+B, B=Bᵀ, B≥0, diag(B)=0, B1=2·1, AB=BA.

Every row of B has either one entry 2, or two distinct entries 1. In the first case symmetry and row sums force an isolated doubled edge. The remaining ordinary support graph is two-regular, and each finite connected component is a cycle of length at least three. Orient each ordinary cycle and take a transposition on each doubled edge. These choices yield a permutation matrix P with

B=P+P⁻¹.

Every orbit of P has length r between 2 and 63. No automorphism assumption on the original graph G is involved; P encodes only the independently constructed defect components.

The required finite-cycle coverage has a useful existing Mathlib interface: `SimpleGraph.IsCycles.exists_cycle_toSubgraph_verts_eq_connectedComponentSupp` in Combinatorics/SimpleGraph/Matching.lean:500. It returns a genuine simple closed walk whose vertices are the entire component. Weighted doubled edges must still be separated before applying that simple-graph theorem.

## 2. A polynomial annihilator without spectral vectors

Define R₀(X)=2, R₁(X)=X and Rᵣ₊₁(X)=X Rᵣ(X)−Rᵣ₋₁(X). Since P commutes with its inverse, induction gives

Rᵣ(P+P⁻¹)=Pʳ+P⁻ʳ.

On an orbit of length r, this is 2I. Consequently the polynomial

H(X)=∏_{r=1}^{63}(Rᵣ(X)−2)

annihilates B: on each permutation orbit one factor is zero, and all factors are polynomials in the same matrix and commute. The same conclusion follows by applying the product to each standard basis vector and commuting its orbit-length factor to the right.

It would be insufficient merely to state P^L=I for L=lcm(1,...,63) and then allow all divisors of L: those divisors include conductors greater than 63, which are outside the finite norm table. The orbit-length argument above preserves the exact conductor range.

Let C₁=X−2, C₂=X+2, and let C_ell, ell≥3, be the monic integer polynomials in the existing finite table. The following identities hold for every 1≤r≤63:

Rᵣ(X)−2 = (X−2) · (X+2)^[2 divides r] · ∏_{ell|r, ell≥3} C_ell(X)².

They are exact finite polynomial identities. The accompanying check_n63_chebyshev.py reads the actual coefficient table and verifies all 63 identities by integer coefficient multiplication; it additionally verifies all composition degree/next-coefficient formulas below. Its actual output is logs/n63-chebyshev-check.log. This check is not yet Lean reflection and is not a substitute for the graph-to-annihilator proof.

Thus every irreducible factor of H is among C_ell for 1≤ell≤63. Repeated factors are harmless; no squarefree extraction or diagonalizability theorem is needed.

## 3. The finite arithmetic lemma, with no real subfield

For ell≥3 choose a primitive ell-th root ζ in a cyclotomic field F over Q, and put μ=ζ+ζ⁻¹ and K=Q(μ)⊆F. The cyclotomic polynomial Φ_ell is irreducible over Q of degree φ(ell)=2d. The table's polynomial identity

T^d C_ell(T+T⁻¹)=Φ_ell(T)

proves C_ell(μ)=0. Since ζ satisfies Z²−μZ+1, [F:K]≤2. The tower formula and [F:Q]=2d give [K:Q]≥d; C_ell(μ)=0 and deg C_ell=d give the reverse inequality. Hence C_ell is exactly the monic minimal polynomial of μ. This proof needs neither complex conjugation nor a real-subfield degree theorem. Cases ell=1,2 are rational and immediate.

The exact field norm is

N_ell=Norm_{K/Q}(29+4μ)=(-4)^d C_ell(-29/4).

The existing table proves that N_ell is an integer nonsquare for every ell≠3, using a nonsquare residue modulo its listed modulus. If 29+4μ were a square in K, its norm would be a square in Q; an integer that is a rational square is an integer square, contradicting that residue. For ell=3, C₃=X+1 and the discriminant is 25.

Set q(X)=X²+X−7 and F_ell(X)=C_ell(q(X)). For ell≠3, the quadratic q(X)−μ is irreducible over K because its discriminant 29+4μ is not a square. Capelli's composition lemma now proves F_ell irreducible over Q. Mathlib already supplies this exact type of result as `Polynomial.irreducible_comp` in FieldTheory/IntermediateField/Adjoin/Basic.lean:600: it asks for the monic irreducible outer polynomial and irreducibility of the inner polynomial minus a root in the simple adjoining field.

For ell=3,

F₃(X)=X²+X−6=(X−2)(X+3).

Every C_ell is monic of degree d_ell. Therefore F_ell is monic of degree 2d_ell with coefficient d_ell at X^(2d_ell−1): the leading term q^d contributes d_ell there, while lower C terms have degree at most 2d_ell−2. These finite formulas have also been checked against every actual table row.

## 4. Work entirely over Q on the sum-zero subspace

Let W={x∈Q^63 : Σx_i=0}. It has dimension 62, and the constant vector spans a complementary one-dimensional subspace. A preserves both spaces because its row and column sums are 8. Its action on constants is 8, and tr(A)=0, so the restriction T=A|W has tr(T)=−8. B likewise preserves W; call its restriction U. Since J|W=0,

q(T)=U.

The already established H(B)=0 restricts to H(U)=0, hence H(q(T))=0. No extension of scalars or decomposition into real eigenspaces is used.

A finite-dimensional linear operator's characteristic and minimal polynomials have the same irreducible-factor support. One proof sufficient here takes a root α of an irreducible characteristic factor in an extension field: determinant zero gives an eigenvector, any annihilating polynomial vanishes at α on that eigenvector, and the irreducible factor consequently divides the annihilator. The needed local APIs include `LinearMap.hasEigenvalue_iff_isRoot_charpoly` and `LinearMap.aeval_apply_of_hasEigenvector`. Base-change and minimal-polynomial divisibility still need to be connected explicitly; a charpoly-factor-support lemma has not been claimed as already implemented.

By the factorizations of H(q(X)) and irreducibility of F_ell for ell≠3, unique factorization therefore gives nonnegative integers p,q and e_ell such that

charpoly(T)=(X−2)^p (X+3)^q ∏_{1≤ell≤63, ell≠3} F_ell(X)^e_ell.

Degree and the negative-trace coefficient give

62=p+q+Σ 2d_ell e_ell,
8=−2p+3q+Σ d_ell e_ell.

Subtracting twice the second equality from the first yields

46=5(p−q),

impossible over the integers. This proves the paper-level contradiction once the foregoing actual graph and arithmetic obligations are established. It does not supply an already compiled n63 theorem.

## Minimal Lean obligation order

1. Actual row-two B: separate doubled edges, prove the remaining support graph is IsCycles, and construct a permutation/cycle-block representation B=P+P⁻¹. Reuse the compiled nonnegativity, diagonal, row sum and symmetry; do not assume a component certificate.
2. Chebyshev recurrence evaluation and orbit-length annihilation; reflect the 63 integer factor identities against the real coefficient table.
3. For each C_ell, establish the minimal-polynomial property by the finite algebraic tower argument; derive its exact norm identity and reflect its nonsquare residue. This is the main number-field obligation that the redesign does not remove.
4. Apply the existing irreducible_comp theorem to obtain the 62 irreducible F_ell; use the explicit ell=3 factorization.
5. Construct W over Q (or an explicit 62-dimensional rational coordinate model), prove trace(T)=−8 and q(T)=U, and prove characteristic-factor support lies in the annihilator's support.
6. Use monic degree/nextCoeff product formulas to obtain the final integer contradiction, then call it from the unchanged original graph specification. `Polynomial.Monic.nextCoeff_mul`, `nextCoeff_pow`, and `nextCoeff_multiset_prod` already exist.

Recommended implementation decision: prefer this rational-annihilator route to the original real-eigenspace half-trace route. It removes the complete real spectral decomposition, the K-to-R eigenspace base-change theorem, and the half-dimension trace lemma. It does not justify skipping the finite norm/minimal-polynomial arithmetic or the row-two graph construction.


## Further simplification: irreducibility by a finite Laurent lift

The tower argument in Section 3 can itself be replaced by a purely polynomial argument. For a nonzero polynomial f of degree a, define L(f)(T)=T^a f(T+T⁻¹), interpreted by expansion as an ordinary polynomial. It has degree 2a, is multiplicative because degrees add over Q, and is nonconstant whenever f is nonconstant. For ell≥3 the checked table identity is L(C_ell)=Φ_ell. If C_ell factored as nonconstant rational polynomials f g, the ordinary polynomials L(f),L(g) would give a nontrivial factorization of the irreducible Φ_ell. Thus C_ell is irreducible without introducing any cyclotomic field or real subfield. Cases ell=1,2 are degree one.

Then use K=AdjoinRoot C_ell directly: its canonical root has minimal polynomial C_ell, and the exact norm of 29+4root can be established from the multiplication determinant or resultant using the finite table. The Laurent lift can be implemented as an explicit binomial-coefficient polynomial transform, avoiding a dependency on a general Laurent-field construction. Its multiplicativity and degree statement are genuine remaining lemmas, not certificates assumed by the original-graph theorem.


## Concrete norm interface

For the final version prefer K=AdjoinRoot C_ell and the polynomial-only lift proof. The existing `Polynomial.cyclotomic.irreducible_rat` (RingTheory/Polynomial/Cyclotomic/Roots.lean:186) proves the needed rational cyclotomic irreducibility. An explicit lift is `Σ_j c_j X^(d−j)(X²+1)^j`; its value at nonzero t is t^d C(t+t⁻¹), and its leading degree is 2d.

For the norm, let M be multiplication by the root in its power basis. `Algebra.norm_eq_matrix_det`, `Matrix.charpoly_leftMulMatrix`, `Matrix.eval_charpoly` (Matrix/Charpoly/Basic.lean:131), and `Matrix.det_smul` give

Norm(29+4α)=det(29I+4M)=(-4)^d det((-29/4)I−M)=(-4)^d C(-29/4).

Thus no explicit determinant expansion of up to 30×30 matrices is necessary. The arithmetic certificate can remain a short integer coefficient evaluation and residue check after this symbolic identity is proved.
