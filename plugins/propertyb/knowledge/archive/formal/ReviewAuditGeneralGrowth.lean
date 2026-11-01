import Aris4Math.General.Growth.Main

/-! Independent original-vocabulary restatement of both the maximum definition
and the full growing-budget theorem. No parameter witness or structural
certificate is an external assumption. -/
namespace GeneralGrowthAudit
open Aris4Math.General.RS
universe u

theorem original_complete_statement (k : ℕ) (hk : 17 ≤ k) :
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
      1 ≤ ⌊Real.sqrt (B : ℝ) / (8 * (1 + Real.log (k : ℝ)))⌋₊ ∧
      ∀ (V : Type u) [Finite V] (E : Finset (Finset V)),
        (∀ e ∈ E, e.card = k) →
        E.card ≤ B + ⌊Real.sqrt (B : ℝ) / (8 * (1 + Real.log (k : ℝ)))⌋₊ →
        ∃ coloring : V → Bool, ∀ e ∈ E,
          (∃ red ∈ e, coloring red = true) ∧
          (∃ blue ∈ e, coloring blue = false) := by
  refine ⟨rsBudget k, rsBudget_accepts hk, ?_, seed_le_rsBudget hk,
    rsBudget_lt hk, integerGain_pos hk (seed_le_rsBudget hk), ?_⟩
  · intro M hM hp
    exact le_rsBudget_of_accepts hk ⟨hM, hp⟩
  · intro V _ E hu hE
    exact propertyB_of_general_growth E hk hu hE

theorem original_noncolorable_lower_bound (V : Type u) [Finite V]
    (E : Finset (Finset V)) (k : ℕ) (hk : 17 ≤ k)
    (uniform : ∀ e ∈ E, e.card = k)
    (noncolorable : ¬ ∃ coloring : V → Bool, ∀ e ∈ E,
      (∃ red ∈ e, coloring red = true) ∧ (∃ blue ∈ e, coloring blue = false)) :
    rsBudget k + 1 +
      ⌊Real.sqrt (rsBudget k : ℝ) / (8 * (1 + Real.log (k : ℝ)))⌋₊ ≤ E.card := by
  have h := non_propertyB_edges_ge_general_growth E hk uniform noncolorable
  change rsBudget k + integerGain k (rsBudget k) + 1 ≤ E.card at h
  change rsBudget k + 1 + integerGain k (rsBudget k) ≤ E.card
  omega

end GeneralGrowthAudit

#print Aris4Math.General.RS.AcceptedAt
#print Aris4Math.General.RS.RSAccepts
#print Aris4Math.General.RS.rsBudget
#print Aris4Math.General.RS.integerGain
#print Aris4Math.General.RS.Uniform
#print Aris4Math.General.RS.PropertyB
#print Aris4Math.General.RS.Bichromatic
#check Aris4Math.General.RS.rsBudget_characterization
#check Aris4Math.General.RS.propertyB_of_general_growth
#check GeneralGrowthAudit.original_complete_statement
#print axioms Aris4Math.General.RS.rsBudget_characterization
#print axioms Aris4Math.General.RS.rsBudget_parameter
#print axioms Aris4Math.General.RS.propertyB_of_accepted_gain
#print axioms Aris4Math.General.RS.propertyB_of_general_growth
#print axioms Aris4Math.General.RS.non_propertyB_edges_ge_general_growth
#print axioms GeneralGrowthAudit.original_complete_statement
#print axioms GeneralGrowthAudit.original_noncolorable_lower_bound
