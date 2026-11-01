import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyOneEightJointStar0Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 3
abbrev Quota := Fin 1
def labels : List (Finset (Fin 5)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀T,T∈labels := by decide +kernel
def μ (T : Finset (Fin 5)) : ℕ := if T=∅ then 6 else if T={0} then 6 else if T={1} then 4 else if T={2} then 4 else if T={3} then 4 else if T={1,2,3} then 1 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 2 else if T={2,4} then 2 else if T={3,4} then 2 else 0
def support : Finset (Finset (Fin 5)) := {∅,{0},{1},{2},{3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{2,4},{3,4}}
def positionFn : Layout → Fin 5 → Fin 21 := ![![18,9,19,20,10],![18,19,9,20,10],![18,19,20,9,10]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 5 ↪ Fin 21 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨21,[10,11,19,20,21],[⟨[],6⟩,⟨[19],6⟩,⟨[10],4⟩,⟨[20],4⟩,⟨[21],4⟩,⟨[10,20,21],1⟩,⟨[10,19,20,21],1⟩,⟨[11],1⟩,⟨[11,19],1⟩,⟨[10,11],2⟩,⟨[11,20],2⟩,⟨[11,21],2⟩],none,[19,10,20,21,11]⟩,⟨21,[10,11,19,20,21],[⟨[],6⟩,⟨[19],6⟩,⟨[20],4⟩,⟨[10],4⟩,⟨[21],4⟩,⟨[10,20,21],1⟩,⟨[10,19,20,21],1⟩,⟨[11],1⟩,⟨[11,19],1⟩,⟨[11,20],2⟩,⟨[10,11],2⟩,⟨[11,21],2⟩],none,[19,20,10,21,11]⟩,⟨21,[10,11,19,20,21],[⟨[],6⟩,⟨[19],6⟩,⟨[20],4⟩,⟨[21],4⟩,⟨[10],4⟩,⟨[10,20,21],1⟩,⟨[10,19,20,21],1⟩,⟨[11],1⟩,⟨[11,19],1⟩,⟨[11,20],2⟩,⟨[11,21],2⟩,⟨[10,11],2⟩],none,[19,20,21,10,11]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(1/3),(1/3),(1/3)]
def beta : Layout → Fin 5 → ℚ := ![![(0/1),(0/1),(0/1),(0/1),(1/3)],![(0/1),(0/1),(0/1),(0/1),(1/3)],![(0/1),(0/1),(0/1),(0/1),(1/3)]]
def R : Fin 5 → Quota → Finset (Fin 5) := ![![∅],![∅],![∅],![∅],![∅]]
def delta : Fin 5 → Quota → ℚ := ![![(0/1)],![(0/1)],![(0/1)],![(0/1)],![(61189/9999999)]]
def quota : Fin 5 → Quota → ℕ := ![![0],![0],![0],![0],![4]]
end Aris4Math.ThirtyFour.TwentyOneEightJointStar0Data
