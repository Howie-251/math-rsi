import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyOneEightJointTriple0Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 1
abbrev Quota := Fin 2
def labels : List (Finset (Fin 3)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀T,T∈labels := by decide +kernel
def μ (T : Finset (Fin 3)) : ℕ := if T=∅ then 16 else if T={0} then 5 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 2 else if T={0,1,2} then 1 else 0
def support : Finset (Finset (Fin 3)) := {∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2}}
def positionFn : Layout → Fin 3 → Fin 21 := ![![10,9,11]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 3 ↪ Fin 21 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨21,[10,11,12],[⟨[],16⟩,⟨[11],5⟩,⟨[10],4⟩,⟨[10,11],1⟩,⟨[12],4⟩,⟨[11,12],1⟩,⟨[10,12],2⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(1/1)]
def beta : Layout → Fin 3 → ℚ := ![![(1/1),(0/1),(0/1)]]
def R : Fin 3 → Quota → Finset (Fin 3) := ![![{1},{2}],![∅,∅],![∅,∅]]
def delta : Fin 3 → Quota → ℚ := ![![(95023/10000000),(4319/5000000)],![(0/1),(0/1)],![(0/1),(0/1)]]
def quota : Fin 3 → Quota → ℕ := ![![2,2],![0,0],![0,0]]
end Aris4Math.ThirtyFour.TwentyOneEightJointTriple0Data
