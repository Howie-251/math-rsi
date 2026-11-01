import Aris4Math.ThirtyFour.SingleLayoutApplication
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
