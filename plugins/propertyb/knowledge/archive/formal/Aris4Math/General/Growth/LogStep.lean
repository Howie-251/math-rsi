import Aris4Math.General.Growth.Definitions

/-! The real-variable logarithmic comparison used to spend the clique saving
on an increment of the accepted edge budget. -/
noncomputable section
namespace Aris4Math.General.RS

/-- The ratio estimate counts only the loss in the edge-pair coefficient. -/
theorem log_increment_ratio_le (M s r : ℝ) (hM : 2 ≤ M) (hs : 0 < s)
    (hr : 1 < r) :
    Real.log ((M + s) ^ 2 * (1 - 1 / r) / (M * (M - 1))) ≤
      (2 * s + 2) / M - 1 / r := by
  have hM0 : 0 < M := by linarith
  have hMm : 0 < M - 1 := by linarith
  have hr0 : 0 < r := by linarith
  have hB : 0 < 1 - 1 / r := by
    have := (div_lt_one hr0).mpr hr
    linarith
  have hA : 0 < 1 + s / M := by positivity
  have hC : 0 < 1 + 1 / (M - 1) := by positivity
  have hfactor : (M + s) ^ 2 * (1 - 1 / r) / (M * (M - 1)) =
      (1 + s / M) ^ 2 * (1 - 1 / r) * (1 + 1 / (M - 1)) := by
    field_simp
    ring
  have hrecip : 1 / (M - 1) ≤ 2 / M := by
    apply (div_le_div_iff₀ hMm hM0).mpr
    nlinarith
  have hlogA := Real.log_le_sub_one_of_pos hA
  have hlogB := Real.log_le_sub_one_of_pos hB
  have hlogC := Real.log_le_sub_one_of_pos hC
  rw [hfactor, Real.log_mul (mul_ne_zero (pow_ne_zero 2 hA.ne') hB.ne') hC.ne',
    Real.log_mul (pow_ne_zero 2 hA.ne') hB.ne', Real.log_pow]
  push_cast
  calc
    2 * Real.log (1 + s / M) + Real.log (1 - 1 / r) +
        Real.log (1 + 1 / (M - 1)) ≤ 2 * (s / M) - 1 / r + 2 / M := by
      linarith
    _ = (2 * s + 2) / M - 1 / r := by ring

/-- Uniform real-variable step from strict RS acceptance to the clique-refined
criterion at the incremented budget, retaining the same a and J. -/
theorem rs_increment_of_log_slack (M s r d a J L : ℝ)
    (hM : 2 ≤ M) (hs0 : 0 < s) (hr : 1 < r) (hd : 0 < d)
    (ha : 0 < a) (_hJ : 0 ≤ J)
    (hlog : -2 * L < (M / d) * Real.log a)
    (hs : (2 + 2 * L) * s + 2 < M / r)
    (hacc : M * (M - 1) / d ^ 2 * J < a ^ (M / d)) :
    ((M + s) ^ 2 * (1 - 1 / r)) / d ^ 2 * J < a ^ ((M + s) / d) := by
  have hM0 : 0 < M := by linarith
  have hMm : 0 < M - 1 := by linarith
  have hr0 : 0 < r := by linarith
  have hB : 0 < 1 - 1 / r := by
    have := (div_lt_one hr0).mpr hr
    linarith
  let R := (M + s) ^ 2 * (1 - 1 / r) / (M * (M - 1))
  have hR : 0 < R := by dsimp [R]; positivity
  have hsdiv : ((2 + 2 * L) * s + 2) / M < 1 / r := by
    apply (div_lt_iff₀ hM0).mpr
    simpa [div_eq_mul_inv, mul_comm] using hs
  have hlogR : Real.log R < -2 * s * L / M := by
    calc
      Real.log R ≤ (2 * s + 2) / M - 1 / r :=
        log_increment_ratio_le M s r hM hs0 hr
      _ = (((2 + 2 * L) * s + 2) / M - 1 / r) + (-2 * s * L / M) := by ring
      _ < 0 + (-2 * s * L / M) :=
        add_lt_add_right (sub_neg.mpr hsdiv) _
      _ = -2 * s * L / M := zero_add _
  have hscaled : -2 * s * L / M < (s / d) * Real.log a := by
    have ht := mul_lt_mul_of_pos_left hlog (div_pos hs0 hM0)
    convert ht using 1 <;> field_simp
  have hratio : R < a ^ (s / d) := by
    apply (Real.log_lt_log_iff hR (Real.rpow_pos_of_pos ha _)).mp
    rw [Real.log_rpow ha]
    exact hlogR.trans hscaled
  have hfirst := mul_lt_mul_of_pos_left hacc hR
  have hsecond := mul_lt_mul_of_pos_right hratio (Real.rpow_pos_of_pos ha (M / d))
  calc
    ((M + s) ^ 2 * (1 - 1 / r)) / d ^ 2 * J =
        R * (M * (M - 1) / d ^ 2 * J) := by
      dsimp [R]
      field_simp
    _ < R * a ^ (M / d) := hfirst
    _ < a ^ (s / d) * a ^ (M / d) := hsecond
    _ = a ^ ((M + s) / d) := by
      rw [← Real.rpow_add ha]
      congr 1
      ring

end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.log_increment_ratio_le
#print axioms Aris4Math.General.RS.rs_increment_of_log_slack
