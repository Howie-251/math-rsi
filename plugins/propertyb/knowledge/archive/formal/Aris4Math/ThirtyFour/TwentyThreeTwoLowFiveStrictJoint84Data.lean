import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint84Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 5
abbrev Quota := Fin 3
def sourceGroup : ℕ := 84
def labels : List (Finset (Fin 5)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Finset (Fin 5) → ℕ := fun T => if T=∅ then 10 else if T={0} then 3 else if T={1} then 3 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 4 else if T={0,1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else 0
def support : Finset (Finset (Fin 5)) := {∅,{0},{1},{2},{0,2},{1,2},{3},{0,1,3},{2,3},{4},{0,1,4},{2,4},{3,4}}
def positionFn : Layout → Fin 5 → Fin 23 := ![![9,22,10,11,12],![9,22,10,12,11],![9,22,11,10,12],![9,22,12,10,11]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 5 ↪ Fin 23 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨23,[10,11,12,13,23],[⟨[],10⟩,⟨[10],3⟩,⟨[23],3⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[11,23],1⟩,⟨[12],4⟩,⟨[10,12,23],1⟩,⟨[11,12],1⟩,⟨[13],4⟩,⟨[10,13,23],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩],none,[10,23,11,12,13]⟩,⟨23,[10,11,12,13,23],[⟨[],10⟩,⟨[10],3⟩,⟨[23],3⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[11,23],1⟩,⟨[13],4⟩,⟨[10,13,23],1⟩,⟨[11,13],1⟩,⟨[12],4⟩,⟨[10,12,23],1⟩,⟨[11,12],1⟩,⟨[12,13],1⟩],none,[10,23,11,13,12]⟩,⟨23,[10,11,12,13,23],[⟨[],10⟩,⟨[10],3⟩,⟨[23],3⟩,⟨[12],3⟩,⟨[10,12],1⟩,⟨[12,23],1⟩,⟨[11],4⟩,⟨[10,11,23],1⟩,⟨[11,12],1⟩,⟨[13],4⟩,⟨[10,13,23],1⟩,⟨[12,13],1⟩,⟨[11,13],1⟩],none,[10,23,12,11,13]⟩,⟨23,[10,11,12,13,23],[⟨[],10⟩,⟨[10],3⟩,⟨[23],3⟩,⟨[13],3⟩,⟨[10,13],1⟩,⟨[13,23],1⟩,⟨[11],4⟩,⟨[10,11,23],1⟩,⟨[11,13],1⟩,⟨[12],4⟩,⟨[10,12,23],1⟩,⟨[12,13],1⟩,⟨[11,12],1⟩],none,[10,23,13,11,12]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(5/11),(2045455/10000001),(1/11),(2500000/10000001)]
def beta : Layout → Fin 5 → ℚ := ![![(0/1),(0/1),(5/11),(5/11),(5/11)],![(0/1),(0/1),(2045455/10000001),(2045455/10000001),(2045455/10000001)],![(0/1),(0/1),(1/11),(1/11),(1/11)],![(0/1),(0/1),(2500000/10000001),(2500000/10000001),(2500000/10000001)]]
def R : Fin 5 → Quota → Finset (Fin 5) := ![![∅,∅,∅],![∅,∅,∅],![∅,{3},{4}],![{0,1},{0,1,2},{0,1,4}],![{0,1},{0,1,2},{0,1,3}]]
def delta : Fin 5 → Quota → ℚ := ![![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(17277/10000001),(30234/10000001),(47511/10000001)],![(86384/10000001),(8638/10000001),(8638/10000001)],![(86384/10000001),(8638/10000001),(8638/10000001)]]
def quota : Fin 5 → Quota → ℕ := ![![0,0,0],![0,0,0],![2,1,1],![2,1,1],![2,1,1]]
end Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint84Data
