import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowSixStrictJoint39Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 1
abbrev Quota := Fin 2
def sourceGroup : ℕ := 39
def labels : List (Finset (Fin 6)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4},{5},{0,5},{1,5},{0,1,5},{2,5},{0,2,5},{1,2,5},{0,1,2,5},{3,5},{0,3,5},{1,3,5},{0,1,3,5},{2,3,5},{0,2,3,5},{1,2,3,5},{0,1,2,3,5},{4,5},{0,4,5},{1,4,5},{0,1,4,5},{2,4,5},{0,2,4,5},{1,2,4,5},{0,1,2,4,5},{3,4,5},{0,3,4,5},{1,3,4,5},{0,1,3,4,5},{2,3,4,5},{0,2,3,4,5},{1,2,3,4,5},{0,1,2,3,4,5}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Finset (Fin 6) → ℕ := fun T => if T=∅ then 7 else if T={0,1} then 2 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 4 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 4 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,4,5} then 1 else 0
def support : Finset (Finset (Fin 6)) := {∅,{0,1},{2},{0,2},{1,2},{3},{0,3},{1,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{2,3,4,5}}
def positionFn : Layout → Fin 6 → Fin 23 := ![![12,9,13,8,10,11]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 6 ↪ Fin 23 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨23,[9,10,11,12,13,14],[⟨[],7⟩,⟨[10,13],2⟩,⟨[14],4⟩,⟨[13,14],1⟩,⟨[10,14],1⟩,⟨[9],4⟩,⟨[9,13],1⟩,⟨[9,10],1⟩,⟨[11],4⟩,⟨[11,13],1⟩,⟨[10,11],1⟩,⟨[12],4⟩,⟨[12,13],1⟩,⟨[10,12],1⟩,⟨[9,11,12,14],1⟩],none,[13,10,14,9,11,12]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(1/1)]
def beta : Layout → Fin 6 → ℚ := ![![(1/1),(0/1),(0/1),(0/1),(1/1),(1/1)]]
def R : Fin 6 → Quota → Finset (Fin 6) := ![![∅,∅],![∅,∅],![∅,∅],![∅,∅],![{2,3},{0,2,3}],![{2,3},{0,2,3}]]
def delta : Fin 6 → Quota → ℚ := ![![(0/1),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)],![(5399/625000),(17277/10000000)],![(5399/625000),(17277/10000000)]]
def quota : Fin 6 → Quota → ℕ := ![![0,0],![0,0],![0,0],![0,0],![2,1],![2,1]]
end Aris4Math.ThirtyFour.TwentyThreeTwoLowSixStrictJoint39Data
