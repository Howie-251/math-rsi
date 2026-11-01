import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyOneSevenJointUnitFive0Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 3
abbrev Quota := Fin 2
def labels : List (Finset (Fin 5)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀T,T∈labels := by decide +kernel
def μ (T : Finset (Fin 5)) : ℕ := if T=∅ then 7 else if T={0} then 4 else if T={1} then 4 else if T={2} then 4 else if T={0,1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 4 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={1,3,4} then 1 else if T={2,3,4} then 1 else 0
def support : Finset (Finset (Fin 5)) := {∅,{0},{1},{2},{0,1,2},{3},{0,3},{1,3},{2,3},{4},{0,4},{1,2,4},{1,3,4},{2,3,4}}
def positionFn : Layout → Fin 5 → Fin 21 := ![![9,19,8,20,10],![10,8,11,20,9],![10,8,20,9,11]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 5 ↪ Fin 21 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨21,[9,10,11,20,21],[⟨[],7⟩,⟨[10],4⟩,⟨[20],4⟩,⟨[9],4⟩,⟨[9,10,20],1⟩,⟨[21],3⟩,⟨[10,21],1⟩,⟨[20,21],1⟩,⟨[9,21],1⟩,⟨[11],4⟩,⟨[10,11],1⟩,⟨[9,11,20],1⟩,⟨[11,20,21],1⟩,⟨[9,11,21],1⟩],none,[10,20,9,21,11]⟩,⟨21,[9,10,11,12,21],[⟨[],7⟩,⟨[11],4⟩,⟨[9],4⟩,⟨[12],4⟩,⟨[9,11,12],1⟩,⟨[21],3⟩,⟨[11,21],1⟩,⟨[9,21],1⟩,⟨[12,21],1⟩,⟨[10],4⟩,⟨[10,11],1⟩,⟨[9,10,12],1⟩,⟨[9,10,21],1⟩,⟨[10,12,21],1⟩],none,[11,9,12,21,10]⟩,⟨21,[9,10,11,12,21],[⟨[],7⟩,⟨[11],4⟩,⟨[9],4⟩,⟨[21],4⟩,⟨[9,11,21],1⟩,⟨[10],3⟩,⟨[10,11],1⟩,⟨[9,10],1⟩,⟨[10,21],1⟩,⟨[12],4⟩,⟨[11,12],1⟩,⟨[9,12,21],1⟩,⟨[9,10,12],1⟩,⟨[10,12,21],1⟩],none,[11,9,21,10,12]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(2727273/10000000),(2/5),(3272727/10000000)]
def beta : Layout → Fin 5 → ℚ := ![![(2727273/10000000),(0/1),(0/1),(0/1),(2727273/10000000)],![(2/5),(0/1),(0/1),(0/1),(2/5)],![(3272727/10000000),(0/1),(0/1),(0/1),(3272727/10000000)]]
def R : Fin 5 → Quota → Finset (Fin 5) := ![![{1},∅],![∅,∅],![∅,∅],![∅,∅],![{0,1},{2}]]
def delta : Fin 5 → Quota → ℚ := ![![(48951/5000000),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)],![(5439/5000000),(48951/5000000)]]
def quota : Fin 5 → Quota → ℕ := ![![2,0],![0,0],![0,0],![0,0],![1,2]]
end Aris4Math.ThirtyFour.TwentyOneSevenJointUnitFive0Data
