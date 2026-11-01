import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualData
namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualNumeric
open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualData
open Aris4Math.ThirtyThree.RefinedDeletion
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem abc_exact : ∀ c : Case, ∀ k : Fin 23,
    Numeric.boundA (p c) (k.val+1) = (abc c k).1 ∧
    Numeric.boundB (p c) (k.val+1) = (abc c k).2.1 ∧
    Numeric.boundC (p c) (k.val+1) = (abc c k).2.2 := by
  intro c
  fin_cases c <;> decide +kernel

#print axioms abc_exact

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem dual_exact : ∀ c : Case, ∀ j : Fin 6,
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
  if k = (positions r 4).val+1 then lossAt r 4 else
  if k = (positions r 5).val+1 then lossAt r 5 else 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem loss_at : ∀ r : Case, ∀ j : Fin 6,
    loss r ((positions r j).val+1) = lossAt r j := by
  intro r
  fin_cases r <;> decide +kernel

theorem centers_exact : ∀ c : Case,
    (p c).correctionCenters = List.ofFn (fun j => (positions c j).val+1) := by decide +kernel

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
  have hne : ∀ j : Fin 6, k ≠ (positions r j).val+1 := by
    intro j he
    apply hk
    rw [centers_exact,he]
    exact List.mem_ofFn.mpr ⟨j,rfl⟩
  simp only [loss,if_neg (hne 0),if_neg (hne 1),if_neg (hne 2),if_neg (hne 3),if_neg (hne 4),if_neg (hne 5)]

end Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualNumeric

#print axioms Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualNumeric.strict
