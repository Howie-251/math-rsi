import DegreeDiameter.N63Compose
import Mathlib.Tactic.ComputeDegree
import Mathlib.Data.Rat.Lemmas

namespace DegreeDiameter.N63Table
open Polynomial
open scoped BigOperators
noncomputable section
set_option maxRecDepth 10000
set_option maxHeartbeats 4000000

theorem not_isSquare_rat_of_mod (z : ℤ) (p : ℕ) [NeZero p]
    (h : ¬ IsSquare (z : ZMod p)) : ¬ IsSquare (z : ℚ) := by
  intro hz
  exact h ((Rat.isSquare_intCast_iff.mp hz).map (Int.castRingHom (ZMod p)))

theorem phi_1 : cyclotomic 1 ℚ = C (1 : ℚ) * X ^ 1 + C (-1 : ℚ) * X ^ 0 := by
  symm
  apply (eq_cyclotomic_iff (by decide : 0 < 1) _).2
  have hd : Nat.properDivisors 1 = ∅ := by decide
  rw [hd]
  norm_num [] <;> ring

def c1 : ℚ[X] := C (1 : ℚ) * X ^ 1 + C (-2 : ℚ) * X ^ 0

theorem degree_c1 : (c1).natDegree = 1 := by
  unfold c1
  compute_degree!

theorem monic_c1 : (c1).Monic := by
  unfold c1
  monicity!

theorem irreducible_c1 : Irreducible c1 := by
  apply Polynomial.irreducible_of_degree_eq_one
  unfold c1
  compute_degree!

theorem norm_c1 : (-4 : ℚ) ^ (c1).natDegree * (c1).eval (-29 / 4) = 37 := by
  rw [degree_c1]
  norm_num [c1]

theorem nonsquare_c1 : ¬ IsSquare ((-4 : ℚ) ^ (c1).natDegree * (c1).eval (-29 / 4)) := by
  rw [norm_c1]
  exact not_isSquare_rat_of_mod 37 5 (by unfold IsSquare; decide)

theorem irreducible_comp_c1 : Irreducible ((c1).comp n63Quadratic) :=
  n63_composition_irreducible monic_c1 irreducible_c1 nonsquare_c1

theorem phi_2 : cyclotomic 2 ℚ = C (1 : ℚ) * X ^ 1 + C (1 : ℚ) * X ^ 0 := by
  symm
  apply (eq_cyclotomic_iff (by decide : 0 < 2) _).2
  have hd : Nat.properDivisors 2 = {1} := by decide
  rw [hd]
  norm_num [phi_1] <;> ring

def c2 : ℚ[X] := C (1 : ℚ) * X ^ 1 + C (2 : ℚ) * X ^ 0

theorem degree_c2 : (c2).natDegree = 1 := by
  unfold c2
  compute_degree!

theorem monic_c2 : (c2).Monic := by
  unfold c2
  monicity!

theorem irreducible_c2 : Irreducible c2 := by
  apply Polynomial.irreducible_of_degree_eq_one
  unfold c2
  compute_degree!

theorem norm_c2 : (-4 : ℚ) ^ (c2).natDegree * (c2).eval (-29 / 4) = 21 := by
  rw [degree_c2]
  norm_num [c2]

theorem nonsquare_c2 : ¬ IsSquare ((-4 : ℚ) ^ (c2).natDegree * (c2).eval (-29 / 4)) := by
  rw [norm_c2]
  exact not_isSquare_rat_of_mod 21 11 (by unfold IsSquare; decide)

theorem irreducible_comp_c2 : Irreducible ((c2).comp n63Quadratic) :=
  n63_composition_irreducible monic_c2 irreducible_c2 nonsquare_c2

theorem phi_3 : cyclotomic 3 ℚ = C (1 : ℚ) * X ^ 2 + C (1 : ℚ) * X ^ 1 + C (1 : ℚ) * X ^ 0 := by
  symm
  apply (eq_cyclotomic_iff (by decide : 0 < 3) _).2
  have hd : Nat.properDivisors 3 = {1} := by decide
  rw [hd]
  norm_num [phi_1] <;> ring

def c3 : ℚ[X] := C (1 : ℚ) * X ^ 1 + C (1 : ℚ) * X ^ 0

theorem degree_c3 : (c3).natDegree = 1 := by
  unfold c3
  compute_degree!

theorem monic_c3 : (c3).Monic := by
  unfold c3
  monicity!

theorem lift_c3 : cyclotomicLift c3 = cyclotomic 3 ℚ := by
  rw [phi_3]
  unfold cyclotomicLift
  rw [degree_c3]
  norm_num [c3, homogenize_add, homogenize_C_mul, homogenize_X_pow, MvPolynomial.aeval_def] <;> ring

theorem irreducible_c3 : Irreducible c3 :=
  irreducible_of_cyclotomic_lift (by decide : 0 < 3) lift_c3

theorem norm_c3 : (-4 : ℚ) ^ (c3).natDegree * (c3).eval (-29 / 4) = 25 := by
  rw [degree_c3]
  norm_num [c3]

theorem phi_4 : cyclotomic 4 ℚ = C (1 : ℚ) * X ^ 2 + C (1 : ℚ) * X ^ 0 := by
  symm
  apply (eq_cyclotomic_iff (by decide : 0 < 4) _).2
  have hd : Nat.properDivisors 4 = {1, 2} := by decide
  rw [hd]
  norm_num [phi_1, phi_2] <;> ring

def c4 : ℚ[X] := C (1 : ℚ) * X ^ 1

theorem degree_c4 : (c4).natDegree = 1 := by
  unfold c4
  compute_degree!

theorem monic_c4 : (c4).Monic := by
  unfold c4
  monicity!

theorem lift_c4 : cyclotomicLift c4 = cyclotomic 4 ℚ := by
  rw [phi_4]
  unfold cyclotomicLift
  rw [degree_c4]
  norm_num [c4, homogenize_add, homogenize_C_mul, homogenize_X_pow, MvPolynomial.aeval_def] <;> ring

theorem irreducible_c4 : Irreducible c4 :=
  irreducible_of_cyclotomic_lift (by decide : 0 < 4) lift_c4

theorem norm_c4 : (-4 : ℚ) ^ (c4).natDegree * (c4).eval (-29 / 4) = 29 := by
  rw [degree_c4]
  norm_num [c4]

theorem nonsquare_c4 : ¬ IsSquare ((-4 : ℚ) ^ (c4).natDegree * (c4).eval (-29 / 4)) := by
  rw [norm_c4]
  exact not_isSquare_rat_of_mod 29 3 (by unfold IsSquare; decide)

theorem irreducible_comp_c4 : Irreducible ((c4).comp n63Quadratic) :=
  n63_composition_irreducible monic_c4 irreducible_c4 nonsquare_c4

theorem phi_5 : cyclotomic 5 ℚ = C (1 : ℚ) * X ^ 4 + C (1 : ℚ) * X ^ 3 + C (1 : ℚ) * X ^ 2 + C (1 : ℚ) * X ^ 1 + C (1 : ℚ) * X ^ 0 := by
  symm
  apply (eq_cyclotomic_iff (by decide : 0 < 5) _).2
  have hd : Nat.properDivisors 5 = {1} := by decide
  rw [hd]
  norm_num [phi_1] <;> ring

def c5 : ℚ[X] := C (1 : ℚ) * X ^ 2 + C (1 : ℚ) * X ^ 1 + C (-1 : ℚ) * X ^ 0

theorem degree_c5 : (c5).natDegree = 2 := by
  unfold c5
  compute_degree!

theorem monic_c5 : (c5).Monic := by
  unfold c5
  monicity!

theorem lift_c5 : cyclotomicLift c5 = cyclotomic 5 ℚ := by
  rw [phi_5]
  unfold cyclotomicLift
  rw [degree_c5]
  norm_num [c5, homogenize_add, homogenize_C_mul, homogenize_X_pow, MvPolynomial.aeval_def] <;> ring

theorem irreducible_c5 : Irreducible c5 :=
  irreducible_of_cyclotomic_lift (by decide : 0 < 5) lift_c5

theorem norm_c5 : (-4 : ℚ) ^ (c5).natDegree * (c5).eval (-29 / 4) = 709 := by
  rw [degree_c5]
  norm_num [c5]

theorem nonsquare_c5 : ¬ IsSquare ((-4 : ℚ) ^ (c5).natDegree * (c5).eval (-29 / 4)) := by
  rw [norm_c5]
  exact not_isSquare_rat_of_mod 709 13 (by unfold IsSquare; decide)

theorem irreducible_comp_c5 : Irreducible ((c5).comp n63Quadratic) :=
  n63_composition_irreducible monic_c5 irreducible_c5 nonsquare_c5

theorem phi_6 : cyclotomic 6 ℚ = C (1 : ℚ) * X ^ 2 + C (-1 : ℚ) * X ^ 1 + C (1 : ℚ) * X ^ 0 := by
  symm
  apply (eq_cyclotomic_iff (by decide : 0 < 6) _).2
  have hd : Nat.properDivisors 6 = {1, 2, 3} := by decide
  rw [hd]
  norm_num [phi_1, phi_2, phi_3] <;> ring

def c6 : ℚ[X] := C (1 : ℚ) * X ^ 1 + C (-1 : ℚ) * X ^ 0

theorem degree_c6 : (c6).natDegree = 1 := by
  unfold c6
  compute_degree!

theorem monic_c6 : (c6).Monic := by
  unfold c6
  monicity!

theorem lift_c6 : cyclotomicLift c6 = cyclotomic 6 ℚ := by
  rw [phi_6]
  unfold cyclotomicLift
  rw [degree_c6]
  norm_num [c6, homogenize_add, homogenize_C_mul, homogenize_X_pow, MvPolynomial.aeval_def] <;> ring

theorem irreducible_c6 : Irreducible c6 :=
  irreducible_of_cyclotomic_lift (by decide : 0 < 6) lift_c6

theorem norm_c6 : (-4 : ℚ) ^ (c6).natDegree * (c6).eval (-29 / 4) = 33 := by
  rw [degree_c6]
  norm_num [c6]

theorem nonsquare_c6 : ¬ IsSquare ((-4 : ℚ) ^ (c6).natDegree * (c6).eval (-29 / 4)) := by
  rw [norm_c6]
  exact not_isSquare_rat_of_mod 33 5 (by unfold IsSquare; decide)

theorem irreducible_comp_c6 : Irreducible ((c6).comp n63Quadratic) :=
  n63_composition_irreducible monic_c6 irreducible_c6 nonsquare_c6

theorem phi_61 : cyclotomic 61 ℚ = C (1 : ℚ) * X ^ 60 + C (1 : ℚ) * X ^ 59 + C (1 : ℚ) * X ^ 58 + C (1 : ℚ) * X ^ 57 + C (1 : ℚ) * X ^ 56 + C (1 : ℚ) * X ^ 55 + C (1 : ℚ) * X ^ 54 + C (1 : ℚ) * X ^ 53 + C (1 : ℚ) * X ^ 52 + C (1 : ℚ) * X ^ 51 + C (1 : ℚ) * X ^ 50 + C (1 : ℚ) * X ^ 49 + C (1 : ℚ) * X ^ 48 + C (1 : ℚ) * X ^ 47 + C (1 : ℚ) * X ^ 46 + C (1 : ℚ) * X ^ 45 + C (1 : ℚ) * X ^ 44 + C (1 : ℚ) * X ^ 43 + C (1 : ℚ) * X ^ 42 + C (1 : ℚ) * X ^ 41 + C (1 : ℚ) * X ^ 40 + C (1 : ℚ) * X ^ 39 + C (1 : ℚ) * X ^ 38 + C (1 : ℚ) * X ^ 37 + C (1 : ℚ) * X ^ 36 + C (1 : ℚ) * X ^ 35 + C (1 : ℚ) * X ^ 34 + C (1 : ℚ) * X ^ 33 + C (1 : ℚ) * X ^ 32 + C (1 : ℚ) * X ^ 31 + C (1 : ℚ) * X ^ 30 + C (1 : ℚ) * X ^ 29 + C (1 : ℚ) * X ^ 28 + C (1 : ℚ) * X ^ 27 + C (1 : ℚ) * X ^ 26 + C (1 : ℚ) * X ^ 25 + C (1 : ℚ) * X ^ 24 + C (1 : ℚ) * X ^ 23 + C (1 : ℚ) * X ^ 22 + C (1 : ℚ) * X ^ 21 + C (1 : ℚ) * X ^ 20 + C (1 : ℚ) * X ^ 19 + C (1 : ℚ) * X ^ 18 + C (1 : ℚ) * X ^ 17 + C (1 : ℚ) * X ^ 16 + C (1 : ℚ) * X ^ 15 + C (1 : ℚ) * X ^ 14 + C (1 : ℚ) * X ^ 13 + C (1 : ℚ) * X ^ 12 + C (1 : ℚ) * X ^ 11 + C (1 : ℚ) * X ^ 10 + C (1 : ℚ) * X ^ 9 + C (1 : ℚ) * X ^ 8 + C (1 : ℚ) * X ^ 7 + C (1 : ℚ) * X ^ 6 + C (1 : ℚ) * X ^ 5 + C (1 : ℚ) * X ^ 4 + C (1 : ℚ) * X ^ 3 + C (1 : ℚ) * X ^ 2 + C (1 : ℚ) * X ^ 1 + C (1 : ℚ) * X ^ 0 := by
  symm
  apply (eq_cyclotomic_iff (by decide : 0 < 61) _).2
  have hd : Nat.properDivisors 61 = {1} := by decide
  rw [hd]
  norm_num [phi_1] <;> ring

def c61 : ℚ[X] := C (1 : ℚ) * X ^ 30 + C (1 : ℚ) * X ^ 29 + C (-29 : ℚ) * X ^ 28 + C (-28 : ℚ) * X ^ 27 + C (378 : ℚ) * X ^ 26 + C (351 : ℚ) * X ^ 25 + C (-2925 : ℚ) * X ^ 24 + C (-2600 : ℚ) * X ^ 23 + C (14950 : ℚ) * X ^ 22 + C (12650 : ℚ) * X ^ 21 + C (-53130 : ℚ) * X ^ 20 + C (-42504 : ℚ) * X ^ 19 + C (134596 : ℚ) * X ^ 18 + C (100947 : ℚ) * X ^ 17 + C (-245157 : ℚ) * X ^ 16 + C (-170544 : ℚ) * X ^ 15 + C (319770 : ℚ) * X ^ 14 + C (203490 : ℚ) * X ^ 13 + C (-293930 : ℚ) * X ^ 12 + C (-167960 : ℚ) * X ^ 11 + C (184756 : ℚ) * X ^ 10 + C (92378 : ℚ) * X ^ 9 + C (-75582 : ℚ) * X ^ 8 + C (-31824 : ℚ) * X ^ 7 + C (18564 : ℚ) * X ^ 6 + C (6188 : ℚ) * X ^ 5 + C (-2380 : ℚ) * X ^ 4 + C (-560 : ℚ) * X ^ 3 + C (120 : ℚ) * X ^ 2 + C (15 : ℚ) * X ^ 1 + C (-1 : ℚ) * X ^ 0

theorem degree_c61 : (c61).natDegree = 30 := by
  unfold c61
  compute_degree!

theorem monic_c61 : (c61).Monic := by
  unfold c61
  monicity!

theorem lift_c61 : cyclotomicLift c61 = cyclotomic 61 ℚ := by
  rw [phi_61]
  unfold cyclotomicLift
  rw [degree_c61]
  norm_num [c61, homogenize_add, homogenize_C_mul, homogenize_X_pow, MvPolynomial.aeval_def] <;> ring

theorem irreducible_c61 : Irreducible c61 :=
  irreducible_of_cyclotomic_lift (by decide : 0 < 61) lift_c61

theorem norm_c61 : (-4 : ℚ) ^ (c61).natDegree * (c61).eval (-29 / 4) = 36267865031665081837166120096939452874186101 := by
  rw [degree_c61]
  norm_num [c61]

theorem nonsquare_c61 : ¬ IsSquare ((-4 : ℚ) ^ (c61).natDegree * (c61).eval (-29 / 4)) := by
  rw [norm_c61]
  exact not_isSquare_rat_of_mod 36267865031665081837166120096939452874186101 37 (by unfold IsSquare; decide)

theorem irreducible_comp_c61 : Irreducible ((c61).comp n63Quadratic) :=
  n63_composition_irreducible monic_c61 irreducible_c61 nonsquare_c61

end
end DegreeDiameter.N63Table
