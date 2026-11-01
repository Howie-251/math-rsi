import Aris4Math.ThirtyFour.SingleLayoutApplication
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowSevenStrictBlock0Data
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles
open scoped BigOperators
set_option maxRecDepth 100000
abbrev Case := Fin 1
abbrev Quota := Fin 2
def degree : Fin 7 → ℕ := ![6,6,7,7,7,7,7]
def sourceGroup : Case → ℕ := ![0]
def labels : List (Finset (Fin 7)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4},{5},{0,5},{1,5},{0,1,5},{2,5},{0,2,5},{1,2,5},{0,1,2,5},{3,5},{0,3,5},{1,3,5},{0,1,3,5},{2,3,5},{0,2,3,5},{1,2,3,5},{0,1,2,3,5},{4,5},{0,4,5},{1,4,5},{0,1,4,5},{2,4,5},{0,2,4,5},{1,2,4,5},{0,1,2,4,5},{3,4,5},{0,3,4,5},{1,3,4,5},{0,1,3,4,5},{2,3,4,5},{0,2,3,4,5},{1,2,3,4,5},{0,1,2,3,4,5},{6},{0,6},{1,6},{0,1,6},{2,6},{0,2,6},{1,2,6},{0,1,2,6},{3,6},{0,3,6},{1,3,6},{0,1,3,6},{2,3,6},{0,2,3,6},{1,2,3,6},{0,1,2,3,6},{4,6},{0,4,6},{1,4,6},{0,1,4,6},{2,4,6},{0,2,4,6},{1,2,4,6},{0,1,2,4,6},{3,4,6},{0,3,4,6},{1,3,4,6},{0,1,3,4,6},{2,3,4,6},{0,2,3,4,6},{1,2,3,4,6},{0,1,2,3,4,6},{5,6},{0,5,6},{1,5,6},{0,1,5,6},{2,5,6},{0,2,5,6},{1,2,5,6},{0,1,2,5,6},{3,5,6},{0,3,5,6},{1,3,5,6},{0,1,3,5,6},{2,3,5,6},{0,2,3,5,6},{1,2,3,5,6},{0,1,2,3,5,6},{4,5,6},{0,4,5,6},{1,4,5,6},{0,1,4,5,6},{2,4,5,6},{0,2,4,5,6},{1,2,4,5,6},{0,1,2,4,5,6},{3,4,5,6},{0,3,4,5,6},{1,3,4,5,6},{0,1,3,4,5,6},{2,3,4,5,6},{0,2,3,4,5,6},{1,2,3,4,5,6},{0,1,2,3,4,5,6}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Case → Finset (Fin 7) → ℕ := ![fun T => if T=∅ then 2 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 4 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 4 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 4 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,4,5,6} then 1 else 0]
def positionFn : Case → Fin 7 → Fin 23 := ![![10,12,9,19,20,21,22]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel
def positions (i : Case) : Fin 7 ↪ Fin 23 := ⟨positionFn i,positionFn_injective i⟩
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i=profile labels (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Case → Numeric.Profile := ![⟨23,[10,11,13,20,21,22,23],[⟨[],2⟩,⟨[11,13],1⟩,⟨[10],4⟩,⟨[10,11],1⟩,⟨[10,13],1⟩,⟨[20],4⟩,⟨[11,20],1⟩,⟨[13,20],1⟩,⟨[21],4⟩,⟨[11,21],1⟩,⟨[13,21],1⟩,⟨[22],4⟩,⟨[11,22],1⟩,⟨[13,22],1⟩,⟨[23],4⟩,⟨[11,23],1⟩,⟨[13,23],1⟩,⟨[10,20,21,22,23],1⟩],none,[11,13,10,20,21,22,23]⟩]
set_option maxHeartbeats 0 in
theorem p_eq_computed (i : Case) : p i=computed i := by fin_cases i <;> rfl
def loss : Case → Fin 7 → ℚ := ![![(0/1),(0/1),(0/1),(0/1),(0/1),(0/1),(0/1)]]
def R : Case → Fin 7 → Quota → Finset (Fin 7) := ![![![∅,{1,2,3,4,5,6}],![∅,{0,2,3,4,5,6}],![∅,{0,1,3,4,5,6}],![∅,{0,1,2,4,5,6}],![∅,{0,1,2,3,5,6}],![∅,{0,1,2,3,4,6}],![∅,{0,1,2,3,4,5}]]]
def α : Case → Fin 7 → Quota → ℚ := ![![![(0/1),(7/715)],![(0/1),(1/143)],![(0/1),(7/715)],![(0/1),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)]]]
def quota : Case → Fin 7 → Quota → ℕ := ![![![1,0],![1,0],![2,0],![2,0],![2,0],![2,0],![2,0]]]
end Aris4Math.ThirtyFour.TwentyThreeTwoLowSevenStrictBlock0Data
