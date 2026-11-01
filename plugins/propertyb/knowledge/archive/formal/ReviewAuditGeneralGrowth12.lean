import Aris4Math.General.Growth.Twelve

/-! Independent original-vocabulary restatement of both the maximum definition
and the full growing-budget theorem. No parameter witness or structural
certificate is an external assumption. -/
namespace GeneralGrowthTwelveAudit
open Aris4Math.General.RS
universe u

theorem original_complete_statement (k : ℕ) (hk : 12 ≤ k) :
    ∃ B : ℕ,
      (1 ≤ B ∧ ∃ p : ℝ, 0 ≤ p ∧ p ≤ 1 ∧
        (B : ℝ) * ((B : ℝ) - 1) / ((2 : ℝ) ^ (k - 1)) ^ 2 *
          (∫ y in (0 : ℝ)..p, (1 - y ^ 2) ^ (k - 1)) <
          (1 - (1 - p) ^ k) ^ ((B : ℝ) / (2 : ℝ) ^ (k - 1))) ∧
      (∀ M : ℕ, 1 ≤ M →
        (∃ p : ℝ, 0 ≤ p ∧ p ≤ 1 ∧
          (M : ℝ) * ((M : ℝ) - 1) / ((2 : ℝ) ^ (k - 1)) ^ 2 *
            (∫ y in (0 : ℝ)..p, (1 - y ^ 2) ^ (k - 1)) <
            (1 - (1 - p) ^ k) ^ ((M : ℝ) / (2 : ℝ) ^ (k - 1))) → M ≤ B) ∧
      2 ^ k ≤ B ∧ B < k * 2 ^ k ∧
      2 ≤ ⌊Real.sqrt (B : ℝ) / (8 * (1 + Real.log (k : ℝ)))⌋₊ ∧
      ∀ (V : Type u) [Finite V] (E : Finset (Finset V)),
        (∀ e ∈ E, e.card = k) →
        E.card ≤ B + ⌊Real.sqrt (B : ℝ) / (8 * (1 + Real.log (k : ℝ)))⌋₊ →
        ∃ coloring : V → Bool, ∀ e ∈ E,
          (∃ red ∈ e, coloring red = true) ∧
          (∃ blue ∈ e, coloring blue = false) := by
  refine ⟨rsBudget k, rsBudget_accepts_twelve hk, ?_, seed_le_rsBudget_twelve hk,
    rsBudget_lt_twelve hk, integerGain_two_twelve hk (seed_le_rsBudget_twelve hk), ?_⟩
  · intro M hM hp
    exact le_rsBudget_of_accepts_twelve hk ⟨hM, hp⟩
  · intro V _ E hu hE
    exact propertyB_of_general_growth_twelve E hk hu hE

theorem original_noncolorable_lower_bound (V : Type u) [Finite V]
    (E : Finset (Finset V)) (k : ℕ) (hk : 12 ≤ k)
    (uniform : ∀ e ∈ E, e.card = k)
    (noncolorable : ¬ ∃ coloring : V → Bool, ∀ e ∈ E,
      (∃ red ∈ e, coloring red = true) ∧ (∃ blue ∈ e, coloring blue = false)) :
    rsBudget k + 1 +
      ⌊Real.sqrt (rsBudget k : ℝ) / (8 * (1 + Real.log (k : ℝ)))⌋₊ ≤ E.card := by
  have h := non_propertyB_edges_ge_general_growth_twelve E hk uniform noncolorable
  change rsBudget k + integerGain k (rsBudget k) + 1 ≤ E.card at h
  change rsBudget k + 1 + integerGain k (rsBudget k) ≤ E.card
  omega

end GeneralGrowthTwelveAudit

#print Aris4Math.General.RS.AcceptedAt
#print Aris4Math.General.RS.RSAccepts
#print Aris4Math.General.RS.rsBudget
#print Aris4Math.General.RS.integerGain
#print Aris4Math.General.RS.Uniform
#print Aris4Math.General.RS.PropertyB
#print Aris4Math.General.RS.Bichromatic
#check Aris4Math.General.RS.rsBudget_characterization_twelve
#check Aris4Math.General.RS.propertyB_of_general_growth_twelve
#check GeneralGrowthTwelveAudit.original_complete_statement
#print axioms Aris4Math.General.RS.rsBudget_characterization_twelve
#print axioms Aris4Math.General.RS.rsBudget_parameter_twelve
#print axioms Aris4Math.General.RS.propertyB_of_accepted_gain_twelve
#print axioms Aris4Math.General.RS.propertyB_of_general_growth_twelve
#print axioms Aris4Math.General.RS.non_propertyB_edges_ge_general_growth_twelve
#print axioms GeneralGrowthTwelveAudit.original_complete_statement
#print axioms GeneralGrowthTwelveAudit.original_noncolorable_lower_bound
