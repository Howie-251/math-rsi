import Aris4Math.ThirtyThree.TwentyThreeFourLowUnitFacts
namespace Aris4Math.ThirtyThree.TwentyThreeFourLowUnitChoice
open scoped BigOperators
open TwentyThreeFourLowUnitData

def loss (r : Row) (k : ℕ) : ℚ :=
  if k = (positions (configOf r) 0).val+1 then rowLoss r 0 else
  if k = (positions (configOf r) 1).val+1 then rowLoss r 1 else
  if k = (positions (configOf r) 2).val+1 then rowLoss r 2 else
  if k = (positions (configOf r) 3).val+1 then rowLoss r 3 else 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem loss_at : ∀ r : Row, ∀ j : Fin 4,
    loss r ((positions (configOf r) j).val+1) = rowLoss r j := by
  intro r
  fin_cases r <;> decide +kernel

set_option maxHeartbeats 0 in
theorem centers_exact : ∀ c : Config,
    (p c).correctionCenters = List.ofFn (fun j => (positions c j).val+1) := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem choice_exact : ∀ k : Fin 3, ∀ a b c d : Fin 7,
    let r := choice k a b c d
    family (configOf r) = k ∧ ∀ j : Fin 4,
      rowLoss r j = weights (configOf r) j (![a,b,c,d] j) := by
  intro k a
  fin_cases k <;> fin_cases a <;> decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem strict_cached : ∀ r : Row,
    (∑ k : Fin 23, min (abc (configOf r) k).1
      (min (abc (configOf r) k).2.1 ((abc (configOf r) k).2.2 - loss r (k.val+1)))) < 1 := by
  intro r
  fin_cases r <;> decide +kernel

theorem loss_zeroOutside (r : Row) (k : ℕ)
    (hk : k ∉ (p (configOf r)).correctionCenters) : loss r k = 0 := by
  have hne : ∀ j : Fin 4, k ≠ (positions (configOf r) j).val+1 := by
    intro j he
    apply hk
    rw [centers_exact,he]
    exact List.mem_ofFn.mpr ⟨j,rfl⟩
  simp only [loss,if_neg (hne 0),if_neg (hne 1),if_neg (hne 2),if_neg (hne 3)]
end Aris4Math.ThirtyThree.TwentyThreeFourLowUnitChoice
#print axioms Aris4Math.ThirtyThree.TwentyThreeFourLowUnitChoice.choice_exact
#print axioms Aris4Math.ThirtyThree.TwentyThreeFourLowUnitChoice.strict_cached
