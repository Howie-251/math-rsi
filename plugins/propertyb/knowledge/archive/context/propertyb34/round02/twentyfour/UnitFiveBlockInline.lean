import Aris4Math.ThirtyFour.SingleLayoutApplication
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitFiveBlockData
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles
open scoped BigOperators
set_option maxRecDepth 100000
abbrev Case := Fin 1
abbrev Quota := Fin 2
def degree : Fin 6 → ℕ := ![6,6,6,6,6,6]
def labels : List (Finset (Fin 6)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4},{5},{0,5},{1,5},{0,1,5},{2,5},{0,2,5},{1,2,5},{0,1,2,5},{3,5},{0,3,5},{1,3,5},{0,1,3,5},{2,3,5},{0,2,3,5},{1,2,3,5},{0,1,2,3,5},{4,5},{0,4,5},{1,4,5},{0,1,4,5},{2,4,5},{0,2,4,5},{1,2,4,5},{0,1,2,4,5},{3,4,5},{0,3,4,5},{1,3,4,5},{0,1,3,4,5},{2,3,4,5},{0,2,3,4,5},{1,2,3,4,5},{0,1,2,3,4,5}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Case → Finset (Fin 6) → ℕ := ![fun T => if T=∅ then 7 else if T={0} then 1 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={4} then 4 else if T={0,4} then 1 else if T={5} then 4 else if T={0,5} then 1 else if T={1,2,3,4,5} then 1 else 0]
def co : Case → Fin 15 → ℕ := ![![1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
def positionFn : Case → Fin 6 → Fin 24 := ![![9,10,11,12,13,14]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel
def positions (i : Case) : Fin 6 ↪ Fin 24 := ⟨positionFn i,positionFn_injective i⟩
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨24,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i=profile labels (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Case → Numeric.Profile := ![⟨24,[10,11,12,13,14,15],[⟨[],7⟩,⟨[10],1⟩,⟨[11],4⟩,⟨[10,11],1⟩,⟨[12],4⟩,⟨[10,12],1⟩,⟨[13],4⟩,⟨[10,13],1⟩,⟨[14],4⟩,⟨[10,14],1⟩,⟨[15],4⟩,⟨[10,15],1⟩,⟨[11,12,13,14,15],1⟩],none,[10,11,12,13,14,15]⟩]
set_option maxHeartbeats 0 in
theorem p_eq_computed (i : Case) : p i=computed i := by fin_cases i <;> rfl
def loss : Case → Fin 6 → ℚ := ![![(0/1),(21/2210),(0/1),(0/1),(0/1),(0/1)]]
def R : Case → Fin 6 → Quota → Finset (Fin 6) := ![![![∅,{1,2,3,4,5}],![∅,{0,2,3,4,5}],![∅,{0,1,3,4,5}],![∅,{0,1,2,4,5}],![∅,{0,1,2,3,5}],![∅,{0,1,2,3,4}]]]
def α : Case → Fin 6 → Quota → ℚ := ![![![(0/1),(126/12155)],![(21/2210),(21/24310)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)]]]
def quota : Case → Fin 6 → Quota → ℕ := ![![![1,0],![1,0],![1,0],![1,0],![1,0],![1,0]]]
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitFiveBlockData
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitFiveBlockNumeric
open scoped BigOperators
open TwentyFourSixLowUnitFiveBlockData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cachedCertificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧ (p i).emptyPairCap=none ∧
    (∀ j, (positions i j).val+1∈(p i).correctionCenters) ∧
    (∀ j z, 0≤α i j z) ∧ (∀ j z, j∉R i j z) ∧
    (∀ j z, quota i j z ≤
      (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (R i j z))+2-
        (24-1-(R i j z).card))/3) ∧
    (∀ j, loss i j ≤ (∑ z, (quota i j z : ℚ)*α i j z)-
      penaltySum (p i) ((positions i j).val+1) (fun z => avoidedPositions (positions i) (R i j z)) (α i j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p i) (k.val+1) true)
      (min (CachedRows.cachedA (p i) (k.val+1) false) (CachedRows.cachedC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))))<1 := by
  intro i
  fin_cases i <;> simp only [p_eq_computed] <;> unfold Numeric.validProfile <;> decide +kernel

theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧ (p i).emptyPairCap=none ∧
    (∀ j, (positions i j).val+1∈(p i).correctionCenters) ∧
    (∀ j z, 0≤α i j z) ∧ (∀ j z, j∉R i j z) ∧
    (∀ j z, quota i j z ≤
      (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (R i j z))+2-
        (24-1-(R i j z).card))/3) ∧
    (∀ j, loss i j ≤ (∑ z, (quota i j z : ℚ)*α i j z)-
      penaltySum (p i) ((positions i j).val+1) (fun z => avoidedPositions (positions i) (R i j z)) (α i j)) ∧
    (∑ k : Fin 24, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))))<1 := by
  intro i
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := cachedCertificates i
  refine ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,?_⟩
  have eq : (∑k : Fin 24, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1)))) =
      ∑k : Fin 24, min (CachedRows.cachedA (p i) (k.val+1) true)
      (min (CachedRows.cachedA (p i) (k.val+1) false) (CachedRows.cachedC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))) := by
    apply Finset.sum_congr rfl
    intro k _
    obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq (p i) 34 (k.val+1) valid nocap
    rw [ha,hb,hc]
  rw [eq]
  exact strict
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitFiveBlockNumeric
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowUnitFiveBlockNumeric.certificates
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitFiveBlock
open TwentyFourSixLowUnitFiveBlockData TwentyFourSixLowUnitFiveBlockNumeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 24)) (vertices : Fin 6 ↪ Fin 24)
    (i : Case) (counts : ∀ T, count H vertices T=μ i T) : PropertyB H := by
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := certificates i
  have real : Aris4Math.TypeCounting.RealizesProfile H vertices (positions i) (p i) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions i) labels labels_nodup mem_labels (μ i) counts
    rw [← p_eq]; exact valid
  exact SingleLayoutApplication.propertyB_of_single_layout H vertices (positions i) (p i) real
    nocap centers (R i) (α i) (quota i) (loss i) nonneg avoids quotas deduction strict
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitFiveBlock
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowUnitFiveBlock.propertyB_of_counts