import Aris4Math.General.Growth.Elementary

namespace Aris4Math.General.RS

/-- The public-point clique budget is greater than one throughout the theorem's
parameter range, independently of the number of vertices. -/
theorem cliqueBudget_gt_one {k : ℕ} (hk : 17 ≤ k) (n : ℕ) :
    (1 : ℝ) < (cliqueBudget k n : ℝ) := by
  have hkk : k + k ≤ k * k := by nlinarith
  have htwo : 1 < k * k - k + 1 := by omega
  have hmax : k * k - k + 1 ≤ cliqueBudget k n := le_max_left _ _
  exact_mod_cast htwo.trans_le hmax

/-- The actual integer gain has the strict logarithmic slack needed for the
RS perturbation, with all structural budget premises discharged internally. -/
theorem integerGain_log_slack {k M n : ℕ} (hk : 17 ≤ k) (hM : 2 ^ k ≤ M)
    (hn : n * (n - 1) ≤ k * (k - 1) * (M + integerGain k M)) :
    (2 + 2 * Real.log (k : ℝ)) * (integerGain k M : ℝ) + 2 <
      (M : ℝ) / (cliqueBudget k n : ℝ) := by
  have hd := gain_denominator_pos hk
  have hgain := integerGain_le_quotient (M := M) hk
  have hmul : 8 * (1 + Real.log (k : ℝ)) * (integerGain k M : ℝ) ≤
      Real.sqrt (M : ℝ) := by
    have h := (le_div_iff₀ hd).1 hgain
    nlinarith only [h]
  have hleft : (2 + 2 * Real.log (k : ℝ)) * (integerGain k M : ℝ) ≤
      Real.sqrt (M : ℝ) / 4 := by nlinarith only [hmul]
  have hs8 := sqrt_gt_eight hk hM
  have hstrict : (2 + 2 * Real.log (k : ℝ)) * (integerGain k M : ℝ) + 2 <
      Real.sqrt (M : ℝ) / 2 := by linarith
  have hrbound := cliqueBudget_le_twice_sqrt hk hM
    (budget_add_integerGain_le_twice hk hM) hn
  have hrpos : (0 : ℝ) < (cliqueBudget k n : ℝ) :=
    lt_trans zero_lt_one (cliqueBudget_gt_one hk n)
  have hs0 := Real.sqrt_nonneg (M : ℝ)
  have hsq := Real.sq_sqrt (show 0 ≤ (M : ℝ) by positivity)
  have hprod := mul_le_mul_of_nonneg_left hrbound hs0
  have hright : Real.sqrt (M : ℝ) / 2 ≤ (M : ℝ) / (cliqueBudget k n : ℝ) := by
    apply (le_div_iff₀ hrpos).2
    nlinarith only [hprod, hsq]
  exact hstrict.trans_le hright

end Aris4Math.General.RS
