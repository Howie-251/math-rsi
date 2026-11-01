import Aris4Math.General.Growth.Slack

open Aris4Math.General.RS

/-- The original formula with its actual gain and actual clique budget. -/
theorem originalFormulaCaller {k M n : ℕ} (hk : 17 ≤ k) (hM : 2 ^ k ≤ M)
    (hn : n * (n - 1) ≤ k * (k - 1) * (M + integerGain k M)) :
    let s := integerGain k M
    let r := cliqueBudget k n
    (1 : ℝ) < (r : ℝ) ∧
      (2 + 2 * Real.log (k : ℝ)) * (s : ℝ) + 2 < (M : ℝ) / (r : ℝ) := by
  exact ⟨cliqueBudget_gt_one hk n, integerGain_log_slack hk hM hn⟩

/-- A boundary-k concrete caller; its structural budget premise is proved
without computing or assuming the value of the gain. -/
theorem actualSlackCaller :
    (2 + 2 * Real.log (17 : ℝ)) * (integerGain 17 131072 : ℝ) + 2 <
      (131072 : ℝ) / (cliqueBudget 17 17 : ℝ) := by
  apply integerGain_log_slack (by norm_num) (by norm_num)
  norm_num
  omega

#print axioms cliqueBudget_gt_one
#print axioms integerGain_log_slack
#print axioms originalFormulaCaller
#print axioms actualSlackCaller
#check @integerGain_log_slack
