import Aris4Math.General.Growth.Elementary

open Aris4Math.General.RS

/-- Boundary value k=17 and the original power-of-two RS budget. -/
theorem actualGainCaller :
    1 ≤ integerGain 17 131072 ∧
    (integerGain 17 131072 : ℝ) ≤
      Real.sqrt (131072 : ℝ) / (8 * (1 + Real.log (17 : ℝ))) ∧
    integerGain 17 131072 ≤ 131072 ∧
    131072 + integerGain 17 131072 ≤ 2 * 131072 := by
  exact integerGain_bounds (by norm_num) (by norm_num)

/-- A genuine large vertex-budget input for the optional structural estimate. -/
theorem actualCliqueBudgetCaller :
    (cliqueBudget 17 1000 : ℝ) ≤ 2 * Real.sqrt (131072 : ℝ) := by
  exact cliqueBudget_le_twice_sqrt (N := 131073)
    (by norm_num) (by norm_num) (by norm_num) (by norm_num)

#print axioms pow_two_ge_fourth
#print axioms sqrt_ge_square
#print axioms sqrt_gt_eight
#print axioms gain_denominator_pos
#print axioms gain_denominator_le_sqrt
#print axioms integerGain_pos
#print axioms integerGain_le_quotient
#print axioms integerGain_le_budget
#print axioms budget_add_integerGain_le_twice
#print axioms integerGain_bounds
#print axioms cliqueBudget_le_twice_sqrt
#print axioms actualGainCaller
#print axioms actualCliqueBudgetCaller
#check @integerGain_bounds
#check @cliqueBudget_le_twice_sqrt
