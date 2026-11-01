import Aris4Math.ThirtyThree.TwentyThreeThreeLowData
namespace Aris4Math.ThirtyThree.TwentyThreeThreeLowNumeric
open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyThreeThreeLowData
open Aris4Math.ThirtyThree.RefinedDeletion


set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem dual_exact : ∀ c : Case, ∀ j : Fin 5,
    (∀ i, 0 ≤ alpha c j i) ∧ (∀ i, j ∉ avoid c j i) ∧
    (∀ i, quota c j i ≤
      (4 * avoidedCount (p c) ((positions c j).val+1)
        (avoidedPositions (positions c) (avoid c j i)) + 2 -
          (23 - 1 - (avoid c j i).card)) / 3) ∧
    lossAt c j ≤ (∑ i, (quota c j i : ℚ) * alpha c j i) -
      penaltySum (p c) ((positions c j).val+1)
        (fun i => avoidedPositions (positions c) (avoid c j i)) (alpha c j) := by
  intro c
  fin_cases c <;> decide +kernel

#print axioms dual_exact

def loss (r : Case) (k : ℕ) : ℚ :=
  if k = (positions r 0).val+1 then lossAt r 0 else
  if k = (positions r 1).val+1 then lossAt r 1 else
  if k = (positions r 2).val+1 then lossAt r 2 else
  if k = (positions r 3).val+1 then lossAt r 3 else
  if k = (positions r 4).val+1 then lossAt r 4 else 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem loss_at : ∀ r : Case, ∀ j : Fin 5,
    loss r ((positions r j).val+1) = lossAt r j := by
  intro r
  fin_cases r <;> decide +kernel

theorem centers_exact : ∀ c : Case,
    (p c).correctionCenters = List.ofFn (fun j => (positions c j).val+1) := by decide +kernel


end Aris4Math.ThirtyThree.TwentyThreeThreeLowNumeric

#print axioms Aris4Math.ThirtyThree.TwentyThreeThreeLowNumeric.dual_exact
