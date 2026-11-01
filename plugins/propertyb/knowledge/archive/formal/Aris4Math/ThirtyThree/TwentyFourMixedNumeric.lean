import Aris4Math.ThirtyThree.TwentyFourMixedFacts
namespace Aris4Math.ThirtyThree.TwentyFourMixedNumeric
open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyFourMixedData
open Aris4Math.ThirtyThree.TwentyFourMixedFacts
open Aris4Math.ThirtyThree.RefinedDeletion
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem abc_exact : ∀ c : Config, ∀ k : Fin 24,
    Numeric.boundA (p c) (k.val+1) = (abc c k).1 ∧
    Numeric.boundB (p c) (k.val+1) = (abc c k).2.1 ∧
    Numeric.boundC (p c) (k.val+1) = (abc c k).2.2 := by
  intro c
  fin_cases c <;> decide +kernel

#print axioms abc_exact

def avoided (j : Fin 5) : Fin 2 → Finset (Fin 5) := ![∅,Finset.univ.erase j]
def multipliers (c : Config) (j : Fin 5) : Fin 2 → ℚ := ![alpha c j,beta c j]
def quotas (c : Config) (j : Fin 5) : Fin 2 → ℕ := ![totalQuota c j,pureQuota c j]

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem dual_exact : ∀ c : Config, ∀ j : Fin 5,
    (∀ i, 0 ≤ multipliers c j i) ∧ (∀ i, j ∉ avoided j i) ∧
    (∀ i, quotas c j i ≤
      (4 * avoidedCount (p c) ((positions c j).val+1)
        (avoidedPositions (positions c) (avoided j i)) + 2 -
          (24 - 1 - (avoided j i).card)) / 3) ∧
    dualLoss c j ≤ (∑ i, (quotas c j i : ℚ) * multipliers c j i) -
      penaltySum (p c) ((positions c j).val+1)
        (fun i => avoidedPositions (positions c) (avoided j i)) (multipliers c j) := by
  intro c
  fin_cases c <;> decide +kernel

#print axioms dual_exact

def loss (r : Row) (k : ℕ) : ℚ :=
  if k = (positions (configOf r) 0).val+1 then rowLoss r 0 else
  if k = (positions (configOf r) 1).val+1 then rowLoss r 1 else
  if k = (positions (configOf r) 2).val+1 then rowLoss r 2 else
  if k = (positions (configOf r) 3).val+1 then rowLoss r 3 else
  if k = (positions (configOf r) 4).val+1 then rowLoss r 4 else 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem loss_at : ∀ r : Row, ∀ j : Fin 5,
    loss r ((positions (configOf r) j).val+1) = rowLoss r j := by
  intro r
  fin_cases r <;> decide +kernel

theorem centers_exact : ∀ c : Config,
    (p c).correctionCenters = List.ofFn (fun j => (positions c j).val+1) := by decide +kernel

def slotWeight (c : Config) (j : Fin 2) (z : Finset (Fin 5) × Finset (Fin 5)) : ℚ :=
  Numeric.pairWeight (p c) ⟨executableType (positions c) z.1,0⟩
    ⟨executableType (positions c) z.2,0⟩ ((positions c (j.castLE (by omega))).val+1) +
  Numeric.pairWeight (p c) ⟨executableType (positions c) z.2,0⟩
    ⟨executableType (positions c) z.1,0⟩ ((positions c (j.castLE (by omega))).val+1)

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem choice_exact : ∀ t : Fin 32, ∀ a b : Fin 8,
    family (configOf (choice t a b)) = t ∧
    (∀ j : Fin 2, if usesSlot (choice t a b) then
      rowLoss (choice t a b) (j.castLE (by omega)) ≤
        slotWeight (configOf (choice t a b)) j (slot t j (![a,b] j))
      else rowLoss (choice t a b) (j.castLE (by omega)) ≤
        dualLoss (configOf (choice t a b)) (j.castLE (by omega))) ∧
    (∀ j : Fin 5, 2 ≤ j.val → rowLoss (choice t a b) j ≤
      dualLoss (configOf (choice t a b)) j) := by
  intro t
  fin_cases t <;> decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem strict_cached : ∀ r : Row,
    (∑ k : Fin 24, min (abc (configOf r) k).1
      (min (abc (configOf r) k).2.1 ((abc (configOf r) k).2.2 - loss r (k.val+1)))) < 1 := by
  intro r
  fin_cases r <;> decide +kernel

theorem strict (r : Row) :
    (∑ k : Fin 24, min (Numeric.boundA (p (configOf r)) (k.val+1))
      (min (Numeric.boundB (p (configOf r)) (k.val+1))
        (Numeric.boundC (p (configOf r)) (k.val+1) - loss r (k.val+1)))) < 1 := by
  have heq : (∑ k : Fin 24, min (Numeric.boundA (p (configOf r)) (k.val+1))
      (min (Numeric.boundB (p (configOf r)) (k.val+1))
        (Numeric.boundC (p (configOf r)) (k.val+1) - loss r (k.val+1)))) =
      ∑ k : Fin 24, min (abc (configOf r) k).1
        (min (abc (configOf r) k).2.1 ((abc (configOf r) k).2.2 - loss r (k.val+1))) := by
    apply Finset.sum_congr rfl
    intro k _
    rw [(abc_exact (configOf r) k).1, (abc_exact (configOf r) k).2.1,
      (abc_exact (configOf r) k).2.2]
  rw [heq]
  exact strict_cached r

theorem loss_zeroOutside (r : Row) (k : ℕ)
    (hk : k ∉ (p (configOf r)).correctionCenters) : loss r k = 0 := by
  have hne : ∀ j : Fin 5, k ≠ (positions (configOf r) j).val+1 := by
    intro j he
    apply hk
    rw [centers_exact,he]
    exact List.mem_ofFn.mpr ⟨j,rfl⟩
  simp only [loss,if_neg (hne 0),if_neg (hne 1),if_neg (hne 2),if_neg (hne 3),if_neg (hne 4)]

end Aris4Math.ThirtyThree.TwentyFourMixedNumeric

#print axioms Aris4Math.ThirtyThree.TwentyFourMixedNumeric.choice_exact
#print axioms Aris4Math.ThirtyThree.TwentyFourMixedNumeric.strict
