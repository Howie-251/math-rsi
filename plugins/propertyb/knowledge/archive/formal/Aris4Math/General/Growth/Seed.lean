import Aris4Math.General.Growth.Definitions
import Mathlib.Algebra.Order.Ring.Pow

/-! A uniform, explicit accepted RS witness at the exponential seed budget. -/
noncomputable section
namespace Aris4Math.General.RS

/-- Bernoulli's inequality bounds the probability of missing a k-edge at p=1/k. -/
theorem seed_ak_half {k : ℕ} (hk : 2 ≤ k) :
    (1 / 2 : ℝ) ≤ ak k (1 / (k : ℝ)) := by
  have hkR : (2 : ℝ) ≤ k := by exact_mod_cast hk
  have hk0 : (0 : ℝ) < k := by linarith
  have hkm : (0 : ℝ) < (k : ℝ) - 1 := by linarith
  have hb0 : 0 ≤ (1 - 1 / (k : ℝ)) := by
    have := (div_le_one hk0).mpr (show (1 : ℝ) ≤ k by linarith)
    linarith
  have hber := one_add_mul_le_pow
    (a := 1 / ((k : ℝ) - 1)) (by linarith [div_nonneg (by norm_num : (0 : ℝ) ≤ 1) hkm.le] : (-2 : ℝ) ≤ 1 / ((k : ℝ) - 1)) k
  have hdiv : (1 : ℝ) ≤ (k : ℝ) / ((k : ℝ) - 1) := by
    apply (le_div_iff₀ hkm).mpr
    linarith
  have htwo : (2 : ℝ) ≤ 1 + (k : ℝ) * (1 / ((k : ℝ) - 1)) := by
    have h := hdiv
    rw [div_eq_mul_inv] at h
    simpa [div_eq_mul_inv] using (show (2 : ℝ) ≤ 1 + (k : ℝ) * ((k : ℝ) - 1)⁻¹ by linarith)
  have hlower : (2 : ℝ) ≤ (1 + 1 / ((k : ℝ) - 1)) ^ k := htwo.trans hber
  have hproduct : (1 - 1 / (k : ℝ)) * (1 + 1 / ((k : ℝ) - 1)) = 1 := by
    field_simp
    ring
  have hpowproduct : (1 - 1 / (k : ℝ)) ^ k * (1 + 1 / ((k : ℝ) - 1)) ^ k = 1 := by
    rw [← mul_pow, hproduct, one_pow]
  have hm := mul_le_mul_of_nonneg_left hlower (pow_nonneg hb0 k)
  unfold ak
  nlinarith

/-- The exact accepted criterion has uniform strict slack at M=2^k, p=1/k. -/
theorem seed_acceptedAt {k : ℕ} (hk : 17 ≤ k) :
    AcceptedAt k (2 ^ k) (1 / (k : ℝ)) := by
  have hkR : (17 : ℝ) ≤ k := by exact_mod_cast hk
  have hk0 : (0 : ℝ) < k := by linarith
  have hp0 : (0 : ℝ) ≤ 1 / (k : ℝ) := by positivity
  have hp1 : (1 : ℝ) / (k : ℝ) ≤ 1 :=
    (div_le_one hk0).mpr (by linarith)
  have hd : (0 : ℝ) < (2 : ℝ) ^ (k - 1) := by positivity
  have hM : ((2 ^ k : ℕ) : ℝ) = 2 * (2 : ℝ) ^ (k - 1) := by
    rw [Nat.cast_pow, Nat.cast_ofNat]
    conv_lhs => rw [show k = (k - 1) + 1 by omega]
    rw [pow_succ]
    ring
  have hexp : ((2 ^ k : ℕ) : ℝ) / (2 : ℝ) ^ (k - 1) = 2 := by
    rw [hM]
    field_simp
  have hMr : (1 : ℝ) ≤ ((2 ^ k : ℕ) : ℝ) := by
    norm_cast
    exact Nat.one_le_pow k 2 (by decide)
  have hcoef0 : 0 ≤ ((2 ^ k : ℕ) : ℝ) * (((2 ^ k : ℕ) : ℝ) - 1) /
      ((2 : ℝ) ^ (k - 1)) ^ 2 := by
    exact div_nonneg (mul_nonneg (by positivity) (sub_nonneg.mpr hMr)) (sq_nonneg _)
  have hcoef : ((2 ^ k : ℕ) : ℝ) * (((2 ^ k : ℕ) : ℝ) - 1) /
      ((2 : ℝ) ^ (k - 1)) ^ 2 ≤ 4 := by
    apply (div_le_iff₀ (sq_pos_of_pos hd)).mpr
    rw [hM]
    nlinarith
  have hj := mul_le_mul_of_nonneg_left (jk_le k hp0 hp1) hcoef0
  have hc := mul_le_mul_of_nonneg_right hcoef hp0
  have hstrict : (4 : ℝ) * (1 / (k : ℝ)) < 1 / 4 := by
    rw [mul_one_div, div_lt_iff₀ hk0]
    linarith
  have ha := seed_ak_half (show 2 ≤ k by omega)
  have ha0 := ak_nonneg k hp0 hp1
  have hsq : (1 / 4 : ℝ) ≤ (ak k (1 / (k : ℝ))) ^ 2 := by nlinarith
  refine ⟨hp0, hp1, ?_⟩
  rw [hexp, Real.rpow_two]
  exact (hj.trans hc).trans_lt (hstrict.trans_le hsq)

theorem seed_rsAccepts {k : ℕ} (hk : 17 ≤ k) : RSAccepts k (2 ^ k) := by
  refine ⟨?_, 1 / (k : ℝ), seed_acceptedAt hk⟩
  exact Nat.one_le_pow k 2 (by decide)

/-- An accepted positive edge budget cannot use the degenerate parameter zero. -/
theorem acceptedAt_p_pos {k M : ℕ} (hM : 1 ≤ M) {p : ℝ}
    (hA : AcceptedAt k M p) : 0 < p := by
  by_contra hp
  have hpzero : p = 0 := le_antisymm (le_of_not_gt hp) hA.1
  have hMR : (1 : ℝ) ≤ M := by exact_mod_cast hM
  have hexp : (M : ℝ) / (2 : ℝ) ^ (k - 1) ≠ 0 := by
    apply ne_of_gt
    apply div_pos (by linarith)
    positivity
  have hbad := hA.2.2
  rw [hpzero] at hbad
  simp [ak, jk, Real.zero_rpow hexp] at hbad

end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.seed_ak_half
#print axioms Aris4Math.General.RS.seed_acceptedAt
#print axioms Aris4Math.General.RS.seed_rsAccepts

#print axioms Aris4Math.General.RS.acceptedAt_p_pos
