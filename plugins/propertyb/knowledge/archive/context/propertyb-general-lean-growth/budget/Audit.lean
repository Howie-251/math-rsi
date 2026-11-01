import Aris4Math.General.Growth.Budget

open Aris4Math.General.RS

#print rsBudget
#check rsaAccepts_lt
#check rsBudget_characterization
#print axioms rsaAccepts_lt
#print axioms le_rsBudget_of_accepts
#print axioms seed_le_rsBudget
#print axioms rsBudget_accepts
#print axioms rsBudget_lt
#print axioms rsBudget_characterization
#print axioms rsBudget_parameter

/-- Independent caller from the original formulas, with no supplied cutoff. -/
example {k : ℕ} (hk : 17 ≤ k) :
    2^k ≤ rsBudget k ∧ rsBudget k < k*2^k ∧
    (∃ p : ℝ, 0 < p ∧ p ≤ 1 ∧
      (rsBudget k : ℝ)*((rsBudget k : ℝ)-1)/((2:ℝ)^(k-1))^2*jk k p <
        (1-(1-p)^k)^((rsBudget k : ℝ)/(2:ℝ)^(k-1))) ∧
    (∀ M : ℕ, 1 ≤ M → (∃ p : ℝ, 0 ≤ p ∧ p ≤ 1 ∧
      (M:ℝ)*((M:ℝ)-1)/((2:ℝ)^(k-1))^2*jk k p <
        (1-(1-p)^k)^((M:ℝ)/(2:ℝ)^(k-1))) → M ≤ rsBudget k) := by
  refine ⟨seed_le_rsBudget hk, rsBudget_lt hk, ?_, ?_⟩
  · obtain ⟨p, hp, hp1, hA⟩ := rsBudget_parameter hk
    exact ⟨p, hp, hp1, hA.2.2⟩
  · intro M hM hA
    exact le_rsBudget_of_accepts hk ⟨hM, hA⟩
