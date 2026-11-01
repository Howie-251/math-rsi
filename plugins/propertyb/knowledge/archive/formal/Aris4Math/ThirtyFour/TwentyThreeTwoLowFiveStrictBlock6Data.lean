import Aris4Math.ThirtyFour.SingleLayoutApplication
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock6Data
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles
open scoped BigOperators
set_option maxRecDepth 100000
abbrev Case := Fin 5
abbrev Quota := Fin 2
def degree : Fin 5 → ℕ := ![6,6,7,7,7]
def sourceGroup : Case → ℕ := ![156,157,158,159]
def labels : List (Finset (Fin 5)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Case → Finset (Fin 5) → ℕ := ![fun T => if T=∅ then 11 else if T={0} then 4 else if T={1} then 4 else if T={2} then 2 else if T={0,1,2} then 1 else if T={3} then 3 else if T={2,3} then 2 else if T={4} then 3 else if T={2,4} then 2 else if T={3,4} then 1 else if T={0,1,3,4} then 1 else 0,fun T => if T=∅ then 14 else if T={0,1} then 3 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 3 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 2 else 0,fun T => if T=∅ then 15 else if T={0,1} then 3 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={2,3,4} then 1 else 0,fun T => if T=∅ then 16 else if T={0,1} then 3 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 2 else if T={3,4} then 2 else 0]
def positionFn : Case → Fin 5 → Fin 23 := ![![9,11,10,12,22],![10,12,9,11,22],![10,12,9,11,22],![10,12,9,11,22]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel
def positions (i : Case) : Fin 5 ↪ Fin 23 := ⟨positionFn i,positionFn_injective i⟩
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i=profile labels (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Case → Numeric.Profile := ![⟨23,[10,11,12,13,23],[⟨[],11⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[11],2⟩,⟨[10,11,12],1⟩,⟨[13],3⟩,⟨[11,13],2⟩,⟨[23],3⟩,⟨[11,23],2⟩,⟨[13,23],1⟩,⟨[10,12,13,23],1⟩],none,[10,12,11,13,23]⟩,⟨23,[10,11,12,13,23],[⟨[],14⟩,⟨[11,13],3⟩,⟨[10],3⟩,⟨[10,11],1⟩,⟨[10,13],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[23],3⟩,⟨[11,23],1⟩,⟨[13,23],1⟩,⟨[10,12,23],2⟩],none,[11,13,10,12,23]⟩,⟨23,[10,11,12,13,23],[⟨[],15⟩,⟨[11,13],3⟩,⟨[10],2⟩,⟨[10,11],1⟩,⟨[10,13],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[10,12],1⟩,⟨[23],2⟩,⟨[11,23],1⟩,⟨[13,23],1⟩,⟨[10,23],1⟩,⟨[12,23],1⟩,⟨[10,12,23],1⟩],none,[11,13,10,12,23]⟩,⟨23,[10,11,12,13,23],[⟨[],16⟩,⟨[11,13],3⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,13],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[10,12],2⟩,⟨[23],1⟩,⟨[11,23],1⟩,⟨[13,23],1⟩,⟨[10,23],2⟩,⟨[12,23],2⟩],none,[11,13,10,12,23]⟩]
set_option maxHeartbeats 0 in
theorem p_eq_computed (i : Case) : p i=computed i := by fin_cases i <;> rfl
def loss : Case → Fin 5 → ℚ := ![![(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1),(0/1)]]
def R : Case → Fin 5 → Quota → Finset (Fin 5) := ![![![∅,{1,2,3,4}],![∅,{0,2,3,4}],![∅,{0,1,3,4}],![∅,{0,1,2,4}],![∅,{0,1,2,3}]],![![∅,{1,2,3,4}],![∅,{0,2,3,4}],![∅,{0,1,3,4}],![∅,{0,1,2,4}],![∅,{0,1,2,3}]],![![∅,{1,2,3,4}],![∅,{0,2,3,4}],![∅,{0,1,3,4}],![∅,{0,1,2,4}],![∅,{0,1,2,3}]],![![∅,{1,2,3,4}],![∅,{0,2,3,4}],![∅,{0,1,3,4}],![∅,{0,1,2,4}],![∅,{0,1,2,3}]]]
def α : Case → Fin 5 → Quota → ℚ := ![![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(0/1)]],![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(0/1)]],![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(0/1)]],![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(0/1)]]]
def quota : Case → Fin 5 → Quota → ℕ := ![![![1,0],![1,0],![2,0],![2,0],![2,0]],![![1,0],![1,0],![2,0],![2,0],![2,0]],![![1,0],![1,0],![2,0],![2,0],![2,0]],![![1,0],![1,0],![2,0],![2,0],![2,0]]]
end Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictBlock6Data
