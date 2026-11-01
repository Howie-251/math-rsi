import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyThreeFourLowJoint19Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 3
abbrev Quota := Fin 1
def sourceGroup : ℕ := 19
def labels : List (Finset (Fin 4)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Finset (Fin 4) → ℕ := fun T => if T=∅ then 19 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 2 else if T={2} then 1 else if T={0,2} then 2 else if T={1,2} then 2 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else 0
def support : Finset (Finset (Fin 4)) := {∅,{0},{1},{0,1},{2},{0,2},{1,2},{3},{0,3},{1,3},{2,3}}
def positionFn : Layout → Fin 4 → Fin 23 := ![![10,11,22,12],![10,22,11,12],![22,10,11,12]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 4 ↪ Fin 23 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨23,[11,12,13,23],[⟨[],19⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],2⟩,⟨[23],1⟩,⟨[11,23],2⟩,⟨[12,23],2⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[13,23],1⟩],none,[11,12,23,13]⟩,⟨23,[11,12,13,23],[⟨[],19⟩,⟨[11],1⟩,⟨[23],1⟩,⟨[11,23],2⟩,⟨[12],1⟩,⟨[11,12],2⟩,⟨[12,23],2⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[13,23],1⟩,⟨[12,13],1⟩],none,[11,23,12,13]⟩,⟨23,[11,12,13,23],[⟨[],19⟩,⟨[23],1⟩,⟨[11],1⟩,⟨[11,23],2⟩,⟨[12],1⟩,⟨[12,23],2⟩,⟨[11,12],2⟩,⟨[13],3⟩,⟨[13,23],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩],none,[23,11,12,13]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(1/3),(1/3),(1/3)]
def beta : Layout → Fin 4 → ℚ := ![![(1/3),(1/3),(0/1),(1/3)],![(1/3),(0/1),(1/3),(1/3)],![(0/1),(1/3),(1/3),(1/3)]]
def R : Fin 4 → Quota → Finset (Fin 4) := ![![∅],![∅],![∅],![∅]]
def delta : Fin 4 → Quota → ℚ := ![![(0/1)],![(0/1)],![(0/1)],![(30166/3333333)]]
def quota : Fin 4 → Quota → ℕ := ![![0],![0],![0],![1]]
end Aris4Math.ThirtyFour.TwentyThreeFourLowJoint19Data
