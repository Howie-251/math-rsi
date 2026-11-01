import Aris4Math.ThirtyThree.TwentyThreeThreeLowABC
import Aris4Math.ThirtyThree.TwentyThreeThreeLowDual
namespace Aris4Math.ThirtyThree.TwentyThreeThreeLowNumeric
open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyThreeThreeLowData
open Aris4Math.ThirtyThree.RefinedDeletion
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem strict_cached : ∀ r : Case,
    (∑ k : Fin 23, min (abc r k).1
      (min (abc r k).2.1 ((abc r k).2.2 - loss r (k.val+1)))) < 1 := by
  intro r
  fin_cases r <;> decide +kernel

theorem strict (r : Case) :
    (∑ k : Fin 23, min (Numeric.boundA (p r) (k.val+1))
      (min (Numeric.boundB (p r) (k.val+1))
        (Numeric.boundC (p r) (k.val+1) - loss r (k.val+1)))) < 1 := by
  have heq : (∑ k : Fin 23, min (Numeric.boundA (p r) (k.val+1))
      (min (Numeric.boundB (p r) (k.val+1))
        (Numeric.boundC (p r) (k.val+1) - loss r (k.val+1)))) =
      ∑ k : Fin 23, min (abc r k).1
        (min (abc r k).2.1 ((abc r k).2.2 - loss r (k.val+1))) := by
    apply Finset.sum_congr rfl
    intro k _
    rw [(abc_exact r k).1, (abc_exact r k).2.1,
      (abc_exact r k).2.2]
  rw [heq]
  exact strict_cached r

theorem loss_zeroOutside (r : Case) (k : ℕ)
    (hk : k ∉ (p r).correctionCenters) : loss r k = 0 := by
  have hne : ∀ j : Fin 5, k ≠ (positions r j).val+1 := by
    intro j he
    apply hk
    rw [centers_exact,he]
    exact List.mem_ofFn.mpr ⟨j,rfl⟩
  simp only [loss,if_neg (hne 0),if_neg (hne 1),if_neg (hne 2),if_neg (hne 3),if_neg (hne 4)]

end Aris4Math.ThirtyThree.TwentyThreeThreeLowNumeric

#print axioms Aris4Math.ThirtyThree.TwentyThreeThreeLowNumeric.strict
