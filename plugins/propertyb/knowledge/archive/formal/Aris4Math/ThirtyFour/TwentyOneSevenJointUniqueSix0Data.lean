import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyOneSevenJointUniqueSix0Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 3
abbrev Quota := Fin 3
def labels : List (Finset (Fin 6)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4},{5},{0,5},{1,5},{0,1,5},{2,5},{0,2,5},{1,2,5},{0,1,2,5},{3,5},{0,3,5},{1,3,5},{0,1,3,5},{2,3,5},{0,2,3,5},{1,2,3,5},{0,1,2,3,5},{4,5},{0,4,5},{1,4,5},{0,1,4,5},{2,4,5},{0,2,4,5},{1,2,4,5},{0,1,2,4,5},{3,4,5},{0,3,4,5},{1,3,4,5},{0,1,3,4,5},{2,3,4,5},{0,2,3,4,5},{1,2,3,4,5},{0,1,2,3,4,5}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀T,T∈labels := by decide +kernel
def μ (T : Finset (Fin 6)) : ℕ := if T=∅ then 8 else if T={0} then 4 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={1,3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 2 else if T={3,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={1,4,5} then 1 else 0
def support : Finset (Finset (Fin 6)) := {∅,{0},{1},{2},{1,2},{0,1,2},{3},{1,3},{2,3},{4},{1,4},{2,4},{3,4},{0,3,4},{5},{0,5},{1,5},{2,5},{3,5},{2,3,5},{4,5},{1,4,5}}
def positionFn : Layout → Fin 6 → Fin 21 := ![![10,7,9,8,19,20],![10,7,19,8,9,20],![10,19,20,7,8,9]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 6 ↪ Fin 21 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨21,[8,9,10,11,20,21],[⟨[],8⟩,⟨[11],4⟩,⟨[8],1⟩,⟨[10],1⟩,⟨[8,10],1⟩,⟨[8,10,11],1⟩,⟨[9],1⟩,⟨[8,9],2⟩,⟨[9,10],1⟩,⟨[20],1⟩,⟨[8,20],1⟩,⟨[10,20],2⟩,⟨[9,20],1⟩,⟨[9,11,20],1⟩,⟨[21],1⟩,⟨[11,21],1⟩,⟨[8,21],1⟩,⟨[10,21],1⟩,⟨[9,21],1⟩,⟨[9,10,21],1⟩,⟨[20,21],1⟩,⟨[8,20,21],1⟩],none,[11,8,10,9,20,21]⟩,⟨21,[8,9,10,11,20,21],[⟨[],8⟩,⟨[11],4⟩,⟨[8],1⟩,⟨[20],1⟩,⟨[8,20],1⟩,⟨[8,11,20],1⟩,⟨[9],1⟩,⟨[8,9],2⟩,⟨[9,20],1⟩,⟨[10],1⟩,⟨[8,10],1⟩,⟨[10,20],2⟩,⟨[9,10],1⟩,⟨[9,10,11],1⟩,⟨[21],1⟩,⟨[11,21],1⟩,⟨[8,21],1⟩,⟨[20,21],1⟩,⟨[9,21],1⟩,⟨[9,20,21],1⟩,⟨[10,21],1⟩,⟨[8,10,21],1⟩],none,[11,8,20,9,10,21]⟩,⟨21,[8,9,10,11,20,21],[⟨[],8⟩,⟨[11],4⟩,⟨[20],1⟩,⟨[21],1⟩,⟨[20,21],1⟩,⟨[11,20,21],1⟩,⟨[8],1⟩,⟨[8,20],2⟩,⟨[8,21],1⟩,⟨[9],1⟩,⟨[9,20],1⟩,⟨[9,21],2⟩,⟨[8,9],1⟩,⟨[8,9,11],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,20],1⟩,⟨[10,21],1⟩,⟨[8,10],1⟩,⟨[8,10,21],1⟩,⟨[9,10],1⟩,⟨[9,10,20],1⟩],none,[11,20,21,8,9,10]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(9/20),(2/5),(3/20)]
def beta : Layout → Fin 6 → ℚ := ![![(9/20),(0/1),(9/20),(0/1),(0/1),(0/1)],![(2/5),(0/1),(0/1),(0/1),(2/5),(0/1)],![(3/20),(0/1),(0/1),(0/1),(0/1),(3/20)]]
def R : Fin 6 → Quota → Finset (Fin 6) := ![![∅,{5},{1,2,3,4,5}],![∅,∅,∅],![∅,∅,∅],![∅,∅,∅],![∅,∅,∅],![∅,∅,∅]]
def delta : Fin 6 → Quota → ℚ := ![![(90287/10000000),(3481/2000000),(17/156250)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)]]
def quota : Fin 6 → Quota → ℕ := ![![3,2,1],![0,0,0],![0,0,0],![0,0,0],![0,0,0],![0,0,0]]
end Aris4Math.ThirtyFour.TwentyOneSevenJointUniqueSix0Data
