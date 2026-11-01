import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint118Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 2
abbrev Quota := Fin 2
def sourceGroup : ℕ := 118
def labels : List (Finset (Fin 5)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Finset (Fin 5) → ℕ := fun T => if T=∅ then 10 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 2 else if T={2} then 4 else if T={0,2} then 1 else if T={3} then 4 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 5 else if T={1,2,4} then 1 else if T={0,3,4} then 1 else 0
def support : Finset (Finset (Fin 5)) := {∅,{0},{1},{0,1},{2},{0,2},{3},{1,3},{2,3},{4},{1,2,4},{0,3,4}}
def positionFn : Layout → Fin 5 → Fin 23 := ![![8,12,9,10,11],![12,9,10,8,11]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 5 ↪ Fin 23 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨23,[9,10,11,12,13],[⟨[],10⟩,⟨[9],2⟩,⟨[13],2⟩,⟨[9,13],2⟩,⟨[10],4⟩,⟨[9,10],1⟩,⟨[11],4⟩,⟨[11,13],1⟩,⟨[10,11],1⟩,⟨[12],5⟩,⟨[10,12,13],1⟩,⟨[9,11,12],1⟩],none,[9,13,10,11,12]⟩,⟨23,[9,10,11,12,13],[⟨[],10⟩,⟨[13],2⟩,⟨[10],2⟩,⟨[10,13],2⟩,⟨[11],4⟩,⟨[11,13],1⟩,⟨[9],4⟩,⟨[9,10],1⟩,⟨[9,11],1⟩,⟨[12],5⟩,⟨[10,11,12],1⟩,⟨[9,12,13],1⟩],none,[13,10,11,9,12]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(909091/2000000),(1090909/2000000)]
def beta : Layout → Fin 5 → ℚ := ![![(0/1),(909091/2000000),(0/1),(909091/2000000),(909091/2000000)],![(1090909/2000000),(0/1),(1090909/2000000),(0/1),(1090909/2000000)]]
def R : Fin 5 → Quota → Finset (Fin 5) := ![![∅,∅],![∅,∅],![{1,4},{0,1,4}],![{0,4},{0,1,4}],![{1,2},∅]]
def delta : Fin 5 → Quota → ℚ := ![![(0/1),(0/1)],![(0/1),(0/1)],![(8227/2000000),(11219/10000000)],![(34279/10000000),(9349/10000000)],![(47991/5000000),(0/1)]]
def quota : Fin 5 → Quota → ℕ := ![![0,0],![0,0],![2,1],![2,1],![2,0]]
end Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint118Data
