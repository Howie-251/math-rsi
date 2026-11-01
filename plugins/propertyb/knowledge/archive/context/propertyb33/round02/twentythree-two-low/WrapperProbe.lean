import Aris4Math.ThirtyThree.TwentyThreeTwoLowFacts

namespace Aris4Math.ThirtyThree.TwoLowWrapperProbe
open scoped BigOperators
open RefinedDeletion
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeTwoLowData TwentyThreeTwoLowFacts

theorem actual_profile (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 5 ↪ Fin 23) (c : Case)
    (actual : ∀ T, count H vertices T = counts c T) :
    RealizesProfile H vertices (positions c) (p c) 33 := by
  have valid := profile_valid c
  rw [profiles_calculated, calculated_eq_profile] at valid ⊢
  exact FiveProfiles.realizes_profile H vertices (positions c) (counts c) actual _ valid

/-- The only intermediate premise is the actual type multiplicity equality;
all finite dual inequalities and the final strict bound are supplied here. -/
theorem propertyB_of_counts
    (loss : Case → ℕ → ℚ)
    (dual_exact : ∀ c : Case, ∀ j : Fin 5,
    (∀ i, 0 ≤ alpha c j i) ∧ (∀ i, j ∉ avoid c j i) ∧
    (∀ i, quota c j i ≤
      (4 * avoidedCount (p c) ((positions c j).val+1)
        (avoidedPositions (positions c) (avoid c j i)) + 2 -
          (23 - 1 - (avoid c j i).card)) / 3) ∧
    lossAt c j ≤ (∑ i, (quota c j i : ℚ) * alpha c j i) -
      penaltySum (p c) ((positions c j).val+1)
        (fun i => avoidedPositions (positions c) (avoid c j i)) (alpha c j))
    (loss_at : ∀ r : Case, ∀ j : Fin 5,
       loss r ((positions r j).val+1) = lossAt r j)
    (loss_zeroOutside : ∀ r : Case, ∀ k : ℕ,
       k ∉ (p r).correctionCenters → loss r k = 0)
    (strict : ∀ r : Case,
      (∑ k : Fin 23, min (Numeric.boundA (p r) (k.val+1))
      (min (Numeric.boundB (p r) (k.val+1))
        (Numeric.boundC (p r) (k.val+1) - loss r (k.val+1)))) < 1)
    (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 5 ↪ Fin 23) (c : Case)
    (actual : ∀ T, count H vertices T = counts c T) : PropertyB H := by
  have real := actual_profile H vertices c actual
  apply RefinedDeletion.propertyB_of_refined_deletion H vertices (positions c) (p c) real
    (by rw [profiles_calculated, calculated_eq_profile]; rfl) (loss c)
    (avoid c) (alpha c) (quota c)
  · intro j _
    exact (dual_exact c j).1
  · intro j _
    exact (dual_exact c j).2.1
  · intro j _
    exact (dual_exact c j).2.2.1
  · intro j _
    rw [loss_at]
    exact (dual_exact c j).2.2.2
  · exact loss_zeroOutside c
  · exact strict c

end Aris4Math.ThirtyThree.TwoLowWrapperProbe
