import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint23Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 6
abbrev Quota := Fin 2
def sourceGroup : ℕ := 23
def labels : List (Finset (Fin 5)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Finset (Fin 5) → ℕ := fun T => if T=∅ then 11 else if T={0} then 3 else if T={1} then 3 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 3 else if T={0,1,4} then 1 else if T={2,4} then 2 else if T={3,4} then 1 else 0
def support : Finset (Finset (Fin 5)) := {∅,{0},{1},{2},{0,2},{1,2},{3},{0,3},{1,3},{2,3},{4},{0,1,4},{2,4},{3,4}}
def positionFn : Layout → Fin 5 → Fin 23 := ![![10,11,13,12,9],![10,12,9,11,13],![10,12,13,11,9],![11,10,13,12,9],![11,10,9,12,22],![12,11,22,10,9]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 5 ↪ Fin 23 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨23,[10,11,12,13,14],[⟨[],11⟩,⟨[11],3⟩,⟨[12],3⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[13,14],1⟩,⟨[10],3⟩,⟨[10,11,12],1⟩,⟨[10,14],2⟩,⟨[10,13],1⟩],none,[11,12,14,13,10]⟩,⟨23,[10,11,12,13,14],[⟨[],11⟩,⟨[11],3⟩,⟨[13],3⟩,⟨[10],2⟩,⟨[10,11],1⟩,⟨[10,13],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[10,12],1⟩,⟨[14],3⟩,⟨[11,13,14],1⟩,⟨[10,14],2⟩,⟨[12,14],1⟩],none,[11,13,10,12,14]⟩,⟨23,[10,11,12,13,14],[⟨[],11⟩,⟨[11],3⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[12,14],1⟩,⟨[10],3⟩,⟨[10,11,13],1⟩,⟨[10,14],2⟩,⟨[10,12],1⟩],none,[11,13,14,12,10]⟩,⟨23,[10,11,12,13,14],[⟨[],11⟩,⟨[12],3⟩,⟨[11],3⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[13,14],1⟩,⟨[10],3⟩,⟨[10,11,12],1⟩,⟨[10,14],2⟩,⟨[10,13],1⟩],none,[12,11,14,13,10]⟩,⟨23,[10,11,12,13,23],[⟨[],11⟩,⟨[12],3⟩,⟨[11],3⟩,⟨[10],2⟩,⟨[10,12],1⟩,⟨[10,11],1⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[10,13],1⟩,⟨[23],3⟩,⟨[11,12,23],1⟩,⟨[10,23],2⟩,⟨[13,23],1⟩],none,[12,11,10,13,23]⟩,⟨23,[10,11,12,13,23],[⟨[],11⟩,⟨[13],3⟩,⟨[12],3⟩,⟨[23],2⟩,⟨[13,23],1⟩,⟨[12,23],1⟩,⟨[11],3⟩,⟨[11,13],1⟩,⟨[11,12],1⟩,⟨[11,23],1⟩,⟨[10],3⟩,⟨[10,12,13],1⟩,⟨[10,23],2⟩,⟨[10,11],1⟩],none,[13,12,23,11,10]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(673077/2500000),(1/16),(1/4),(420673/2500000),(1161859/10000000),(1338141/10000000)]
def beta : Layout → Fin 5 → ℚ := ![![(673077/2500000),(673077/2500000),(0/1),(673077/2500000),(0/1)],![(1/16),(1/16),(0/1),(1/16),(0/1)],![(1/4),(1/4),(0/1),(1/4),(0/1)],![(420673/2500000),(420673/2500000),(0/1),(420673/2500000),(0/1)],![(1161859/10000000),(1161859/10000000),(0/1),(1161859/10000000),(0/1)],![(1338141/10000000),(1338141/10000000),(0/1),(1338141/10000000),(0/1)]]
def R : Fin 5 → Quota → Finset (Fin 5) := ![![∅,∅],![∅,∅],![∅,∅],![∅,{0}],![∅,∅]]
def delta : Fin 5 → Quota → ℚ := ![![(59389/10000000),(0/1)],![(95023/10000000),(0/1)],![(0/1),(0/1)],![(59389/10000000),(35633/10000000)],![(0/1),(0/1)]]
def quota : Fin 5 → Quota → ℕ := ![![1,0],![1,0],![0,0],![2,1],![0,0]]
end Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint23Data
