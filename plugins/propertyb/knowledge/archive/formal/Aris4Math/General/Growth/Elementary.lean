import Aris4Math.General.Growth.Definitions
import Aris4Math.General.Structure.Definitions
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace Aris4Math.General.RS

/-- The elementary exponential lower bound needed only at natural arguments. -/
theorem pow_two_ge_fourth {k : ℕ} (hk : 16 ≤ k) : k ^ 4 ≤ 2 ^ k := by
  induction k, hk using Nat.le_induction with
  | base => norm_num
  | succ k hk ih =>
    have hstep : (k + 1) ^ 4 ≤ 2 * k ^ 4 := by
      obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hk
      nlinarith [Nat.zero_le (t ^ 4), Nat.zero_le (t ^ 3), Nat.zero_le (t ^ 2)]
    calc
      (k + 1) ^ 4 ≤ 2 * k ^ 4 := hstep
      _ ≤ 2 * 2 ^ k := Nat.mul_le_mul_left 2 ih
      _ = 2 ^ (k + 1) := by rw [pow_succ]; ac_rfl

/-- A large integer RS budget has square root at least `k²`. -/
theorem sqrt_ge_square {k M : ℕ} (hk : 17 ≤ k) (hM : 2 ^ k ≤ M) :
    (k : ℝ) ^ 2 ≤ Real.sqrt (M : ℝ) := by
  apply Real.le_sqrt_of_sq_le
  have h := (pow_two_ge_fourth (by omega : 16 ≤ k)).trans hM
  exact_mod_cast (show (k ^ 2) ^ 2 ≤ M by simpa [← pow_mul] using h)

theorem sqrt_gt_eight {k M : ℕ} (hk : 17 ≤ k) (hM : 2 ^ k ≤ M) :
    8 < Real.sqrt (M : ℝ) := by
  have hkreal : (17 : ℝ) ≤ k := by exact_mod_cast hk
  have hs := sqrt_ge_square hk hM
  nlinarith

theorem gain_denominator_pos {k : ℕ} (hk : 17 ≤ k) :
    0 < 8 * (1 + Real.log (k : ℝ)) := by
  have hkreal : (1 : ℝ) ≤ k := by exact_mod_cast (show 1 ≤ k by omega)
  have hl := Real.log_nonneg hkreal
  linarith

theorem gain_denominator_le_sqrt {k M : ℕ} (hk : 17 ≤ k) (hM : 2 ^ k ≤ M) :
    8 * (1 + Real.log (k : ℝ)) ≤ Real.sqrt (M : ℝ) := by
  have hkreal : (17 : ℝ) ≤ k := by exact_mod_cast hk
  have hl := Real.log_le_sub_one_of_pos (by linarith : (0 : ℝ) < k)
  have hs := sqrt_ge_square hk hM
  nlinarith

theorem integerGain_pos {k M : ℕ} (hk : 17 ≤ k) (hM : 2 ^ k ≤ M) :
    1 ≤ integerGain k M := by
  unfold integerGain
  apply (Nat.one_le_floor_iff _).2
  exact (le_div_iff₀ (gain_denominator_pos hk)).2 (by
    simpa using gain_denominator_le_sqrt hk hM)

theorem integerGain_le_quotient {k M : ℕ} (hk : 17 ≤ k) :
    (integerGain k M : ℝ) ≤ Real.sqrt (M : ℝ) / (8 * (1 + Real.log (k : ℝ))) := by
  apply Nat.floor_le
  exact div_nonneg (Real.sqrt_nonneg _) (gain_denominator_pos hk).le

theorem integerGain_le_budget {k M : ℕ} (hk : 17 ≤ k) (hM : 2 ^ k ≤ M) :
    integerGain k M ≤ M := by
  have hs := integerGain_le_quotient (M := M) hk
  have hd := gain_denominator_pos hk
  have hl : 1 ≤ 8 * (1 + Real.log (k : ℝ)) := by
    have hlog := Real.log_nonneg (show (1 : ℝ) ≤ k by exact_mod_cast (show 1 ≤ k by omega))
    linarith
  have hq : Real.sqrt (M : ℝ) / (8 * (1 + Real.log (k : ℝ))) ≤ Real.sqrt (M : ℝ) :=
    div_le_self (Real.sqrt_nonneg _) hl
  have hroot : Real.sqrt (M : ℝ) ≤ M := by
    apply Real.sqrt_le_iff.2
    have hMr : (1 : ℝ) ≤ M := by
      exact_mod_cast (show 1 ≤ M from (one_le_pow₀ (by omega : 1 ≤ (2 : ℕ))).trans hM)
    constructor
    · positivity
    · nlinarith
  exact_mod_cast hs.trans (hq.trans hroot)

theorem budget_add_integerGain_le_twice {k M : ℕ} (hk : 17 ≤ k) (hM : 2 ^ k ≤ M) :
    M + integerGain k M ≤ 2 * M := by
  have h := integerGain_le_budget hk hM
  omega

/-- Unified elementary inputs for the main growing-budget theorem. -/
theorem integerGain_bounds {k M : ℕ} (hk : 17 ≤ k) (hM : 2 ^ k ≤ M) :
    1 ≤ integerGain k M ∧
    (integerGain k M : ℝ) ≤ Real.sqrt (M : ℝ) / (8 * (1 + Real.log (k : ℝ))) ∧
    integerGain k M ≤ M ∧ M + integerGain k M ≤ 2 * M :=
  ⟨integerGain_pos hk hM, integerGain_le_quotient hk,
    integerGain_le_budget hk hM, budget_add_integerGain_le_twice hk hM⟩

/-- The pair-covering vertex budget controls the same clique budget used by
Turán; this estimate does not assume a particular hypergraph. -/
theorem cliqueBudget_le_twice_sqrt {k M N n : ℕ} (hk : 17 ≤ k)
    (hM : 2 ^ k ≤ M) (hN : N ≤ 2 * M)
    (hn : n * (n - 1) ≤ k * (k - 1) * N) :
    (cliqueBudget k n : ℝ) ≤ 2 * Real.sqrt (M : ℝ) := by
  have hs := sqrt_ge_square hk hM
  have hs0 := Real.sqrt_nonneg (M : ℝ)
  have hfirstNat : k * k - k + 1 ≤ k ^ 2 := by
    have hkk : k ≤ k * k := by nlinarith
    simp only [pow_two]
    omega
  have hfirst : ((k * k - k + 1 : ℕ) : ℝ) ≤ 2 * Real.sqrt (M : ℝ) := by
    have ht : ((k * k - k + 1 : ℕ) : ℝ) ≤ (k : ℝ) ^ 2 := by exact_mod_cast hfirstNat
    linarith
  have hsqNat : (n - 1) ^ 2 ≤ k * (k - 1) * (2 * M) := by
    calc
      (n - 1) ^ 2 = (n - 1) * (n - 1) := pow_two _
      _ ≤ n * (n - 1) := Nat.mul_le_mul_right _ (Nat.sub_le n 1)
      _ ≤ k * (k - 1) * N := hn
      _ ≤ k * (k - 1) * (2 * M) := Nat.mul_le_mul_left _ hN
  have hsq : ((n - 1 : ℕ) : ℝ) ^ 2 ≤
      (k : ℝ) * ((k - 1 : ℕ) : ℝ) * (2 * (M : ℝ)) := by exact_mod_cast hsqNat
  have hkd : (k : ℝ) ≤ 2 * ((k - 1 : ℕ) : ℝ) := by
    exact_mod_cast (show k ≤ 2 * (k - 1) by omega)
  have hmul := mul_le_mul_of_nonneg_right hkd
    (show 0 ≤ 2 * ((k - 1 : ℕ) : ℝ) * (M : ℝ) by positivity)
  have hsquare := Real.sq_sqrt (show 0 ≤ (M : ℝ) by positivity)
  have htsq : ((n - 1 : ℕ) : ℝ) ^ 2 ≤
      (2 * ((k - 1 : ℕ) : ℝ) * Real.sqrt (M : ℝ)) ^ 2 := by
    simp only [mul_pow, hsquare]
    nlinarith only [hsq, hmul]
  have ht : ((n - 1 : ℕ) : ℝ) ≤ 2 * ((k - 1 : ℕ) : ℝ) * Real.sqrt (M : ℝ) :=
    (sq_le_sq₀ (by positivity) (by positivity)).1 htsq
  have hd : (0 : ℝ) < ((k - 1 : ℕ) : ℝ) := by exact_mod_cast (show 0 < k - 1 by omega)
  have hsecond : (((n - 1) / (k - 1) : ℕ) : ℝ) ≤ 2 * Real.sqrt (M : ℝ) := by
    calc
      (((n - 1) / (k - 1) : ℕ) : ℝ) ≤ ((n - 1 : ℕ) : ℝ) / ((k - 1 : ℕ) : ℝ) :=
        Nat.cast_div_le
      _ ≤ 2 * Real.sqrt (M : ℝ) := (div_le_iff₀ hd).2 (by nlinarith only [ht])
  simpa only [cliqueBudget, Nat.cast_max] using max_le hfirst hsecond

end Aris4Math.General.RS
