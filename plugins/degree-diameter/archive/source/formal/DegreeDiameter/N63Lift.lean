import DegreeDiameter.N63Norm
import Mathlib.Algebra.Polynomial.Homogenize
import Mathlib.RingTheory.Polynomial.Cyclotomic.Roots

namespace DegreeDiameter

open Polynomial
open scoped BigOperators
noncomputable section

/-- The ordinary-polynomial interpretation of X^deg(p) p(X+X⁻¹). -/
def cyclotomicLift (p : ℚ[X]) : ℚ[X] :=
  MvPolynomial.aeval ![(X : ℚ[X]) ^ 2 + 1, X] (p.homogenize p.natDegree)

@[simp] theorem cyclotomicLift_zero : cyclotomicLift 0 = 0 := by
  simp [cyclotomicLift]

@[simp] theorem cyclotomicLift_one : cyclotomicLift 1 = 1 := by
  simp [cyclotomicLift]

@[simp] theorem cyclotomicLift_C (a : ℚ) : cyclotomicLift (C a) = C a := by
  simp [cyclotomicLift]

theorem cyclotomicLift_mul (p q : ℚ[X]) :
    cyclotomicLift (p * q) = cyclotomicLift p * cyclotomicLift q := by
  by_cases hp : p = 0
  · subst p; simp
  by_cases hq : q = 0
  · subst q; simp
  unfold cyclotomicLift
  rw [natDegree_mul hp hq, homogenize_mul p q le_rfl le_rfl, map_mul]

def cyclotomicLiftHom : ℚ[X] →* ℚ[X] where
  toFun := cyclotomicLift
  map_one' := cyclotomicLift_one
  map_mul' := cyclotomicLift_mul

theorem cyclotomicLift_eq_sum (p : ℚ[X]) :
    cyclotomicLift p = ∑ j ∈ Finset.range (p.natDegree + 1),
      C (p.coeff j) * (X ^ 2 + 1) ^ j * X ^ (p.natDegree - j) := by
  have hp := congrArg
    (fun q : ℚ[X] => MvPolynomial.aeval ![(X : ℚ[X]) ^ 2 + 1, X]
      (q.homogenize p.natDegree)) p.as_sum_range_C_mul_X_pow
  dsimp only at hp
  rw [homogenize_finsetSum, map_sum] at hp
  change cyclotomicLift p = _ at hp
  rw [hp]
  apply Finset.sum_congr rfl
  intro j hj
  have hj' : j ≤ p.natDegree := Nat.le_of_lt_succ (Finset.mem_range.mp hj)
  rw [homogenize_C_mul, homogenize_X_pow hj']
  simp [mul_assoc]

/-- Nonzero lifts have twice the degree; this makes the lift reflect units. -/
theorem cyclotomicLift_natDegree (p : ℚ[X]) (hp : p ≠ 0) :
    (cyclotomicLift p).natDegree = 2 * p.natDegree := by
  let d := p.natDegree
  let term (j : ℕ) : ℚ[X] := C (p.coeff j) * (X ^ 2 + 1) ^ j * X ^ (d - j)
  have hb : ((X : ℚ[X]) ^ 2 + 1).natDegree = 2 := by
    simpa using (natDegree_X_pow_add_C (R := ℚ) (n := 2) (r := 1))
  have hb0 : (X : ℚ[X]) ^ 2 + 1 ≠ 0 := by
    intro h
    rw [h] at hb
    norm_num at hb
  have ht (j : ℕ) (hj : j ≤ d) (hc : p.coeff j ≠ 0) :
      (term j).natDegree = d + j := by
    dsimp [term]
    rw [mul_assoc, natDegree_C_mul hc,
      natDegree_mul (pow_ne_zero j hb0) (pow_ne_zero (d - j) X_ne_zero),
      natDegree_pow, hb, natDegree_X_pow]
    omega
  have hc (j : ℕ) (h : term j ≠ 0) : p.coeff j ≠ 0 := by
    intro hh
    apply h
    simp [term, hh]
  have hpair : Set.Pairwise {j | j ∈ Finset.range (d + 1) ∧ term j ≠ 0}
      (fun i j => (term i).natDegree ≠ (term j).natDegree) := by
    intro i hi j hj hij heq
    rw [ht i (Nat.le_of_lt_succ (Finset.mem_range.mp hi.1)) (hc i hi.2),
      ht j (Nat.le_of_lt_succ (Finset.mem_range.mp hj.1)) (hc j hj.2)] at heq
    exact hij (by omega)
  rw [cyclotomicLift_eq_sum]
  change (∑ j ∈ Finset.range (d + 1), term j).natDegree = 2 * d
  rw [natDegree_sum_eq_of_disjoint term (Finset.range (d + 1)) hpair]
  apply le_antisymm
  · apply Finset.sup_le
    intro j hj
    have hj' : j ≤ d := Nat.le_of_lt_succ (Finset.mem_range.mp hj)
    by_cases hz : term j = 0
    · simp [hz]
    · rw [ht j hj' (hc j hz)]
      omega
  · have hle := Finset.le_sup (f := fun j => (term j).natDegree)
      (Finset.mem_range.mpr (Nat.lt_succ_self d))
    change (term d).natDegree ≤ _ at hle
    rw [ht d le_rfl (leadingCoeff_ne_zero.mpr hp)] at hle
    simpa only [Nat.succ_eq_add_one, two_mul] using hle

theorem isUnit_of_cyclotomicLift_isUnit {p : ℚ[X]} (h : IsUnit (cyclotomicLift p)) :
    IsUnit p := by
  have hp : p ≠ 0 := by
    intro hz
    rw [hz, cyclotomicLift_zero] at h
    exact not_isUnit_zero h
  have hd := Polynomial.natDegree_eq_zero_of_isUnit h
  rw [cyclotomicLift_natDegree p hp] at hd
  have hd0 : p.natDegree = 0 := by omega
  apply Polynomial.isUnit_iff_degree_eq_zero.mpr
  rw [degree_eq_natDegree hp, hd0]
  rfl

theorem irreducible_of_cyclotomicLift_irreducible {p : ℚ[X]}
    (h : Irreducible (cyclotomicLift p)) : Irreducible p := by
  constructor
  · intro hu
    exact h.not_isUnit (hu.map cyclotomicLiftHom)
  · intro a b hab
    have hh : cyclotomicLift p = cyclotomicLift a * cyclotomicLift b := by
      rw [hab, cyclotomicLift_mul]
    exact (h.isUnit_or_isUnit hh).imp isUnit_of_cyclotomicLift_isUnit
      isUnit_of_cyclotomicLift_isUnit

/-- An actual lift identity with a positive-order cyclotomic polynomial suffices
for the rational irreducibility of the table polynomial. -/
theorem irreducible_of_cyclotomic_lift {p : ℚ[X]} {ell : ℕ} (hell : 0 < ell)
    (hlift : cyclotomicLift p = cyclotomic ell ℚ) : Irreducible p := by
  apply irreducible_of_cyclotomicLift_irreducible
  rw [hlift]
  exact cyclotomic.irreducible_rat hell

end
end DegreeDiameter
