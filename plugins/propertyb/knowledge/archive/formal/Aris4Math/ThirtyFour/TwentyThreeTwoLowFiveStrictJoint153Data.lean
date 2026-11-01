import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint153Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 5
abbrev Quota := Fin 3
def sourceGroup : ℕ := 153
def labels : List (Finset (Fin 5)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Finset (Fin 5) → ℕ := fun T => if T=∅ then 9 else if T={0} then 4 else if T={1} then 4 else if T={2} then 4 else if T={0,1,2} then 1 else if T={3} then 4 else if T={2,3} then 1 else if T={4} then 4 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,1,3,4} then 1 else 0
def support : Finset (Finset (Fin 5)) := {∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{2,4},{3,4},{0,1,3,4}}
def positionFn : Layout → Fin 5 → Fin 23 := ![![9,22,10,12,11],![10,12,11,9,22],![22,9,10,11,12],![22,9,11,10,12]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 5 ↪ Fin 23 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨23,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨23,[10,11,12,13,23],[⟨[],9⟩,⟨[10],4⟩,⟨[23],4⟩,⟨[11],4⟩,⟨[10,11,23],1⟩,⟨[13],4⟩,⟨[11,13],1⟩,⟨[12],4⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[10,12,13,23],1⟩],none,[10,23,11,13,12]⟩,⟨23,[10,11,12,13,23],[⟨[],9⟩,⟨[11],4⟩,⟨[13],4⟩,⟨[12],4⟩,⟨[11,12,13],1⟩,⟨[10],4⟩,⟨[10,12],1⟩,⟨[23],4⟩,⟨[12,23],1⟩,⟨[10,23],1⟩,⟨[10,11,13,23],1⟩],none,[11,13,12,10,23]⟩,⟨23,[10,11,12,13,23],[⟨[],9⟩,⟨[23],4⟩,⟨[10],4⟩,⟨[11],4⟩,⟨[10,11,23],1⟩,⟨[12],4⟩,⟨[11,12],1⟩,⟨[13],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,12,13,23],1⟩],none,[23,10,11,12,13]⟩,⟨23,[10,11,12,13,23],[⟨[],9⟩,⟨[23],4⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,12,23],1⟩,⟨[11],4⟩,⟨[11,12],1⟩,⟨[13],4⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[10,11,13,23],1⟩],none,[23,10,12,11,13]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(3/11),(4000000/10000001),(3/11),(545455/10000001)]
def beta : Layout → Fin 5 → ℚ := ![![(0/1),(0/1),(3/11),(3/11),(3/11)],![(4000000/10000001),(4000000/10000001),(4000000/10000001),(0/1),(0/1)],![(0/1),(0/1),(3/11),(3/11),(3/11)],![(0/1),(0/1),(545455/10000001),(545455/10000001),(545455/10000001)]]
def R : Fin 5 → Quota → Finset (Fin 5) := ![![∅,∅,∅],![∅,∅,∅],![{0,1},{0,1,3},{0,1,4}],![{0,1},{0,1,2},{0,1,4}],![{0,1},{0,1,2},{0,1,3}]]
def delta : Fin 5 → Quota → ℚ := ![![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(86384/10000001),(8638/10000001),(8638/10000001)],![(51831/10000001),(5183/10000001),(5183/10000001)],![(51831/10000001),(5183/10000001),(5183/10000001)]]
def quota : Fin 5 → Quota → ℕ := ![![0,0,0],![0,0,0],![2,1,1],![2,1,1],![2,1,1]]
end Aris4Math.ThirtyFour.TwentyThreeTwoLowFiveStrictJoint153Data
