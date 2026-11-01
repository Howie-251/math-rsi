import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyOneSevenJointQuad21Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 2
abbrev Quota := Fin 2
def labels : List (Finset (Fin 4)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀T,T∈labels := by decide +kernel
def μ (T : Finset (Fin 4)) : ℕ := if T=∅ then 13 else if T={0} then 5 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 4 else if T={1,2} then 1 else if T={3} then 4 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={1,2,3} then 1 else 0
def support : Finset (Finset (Fin 4)) := {∅,{0},{1},{0,1},{2},{1,2},{3},{1,3},{0,2,3},{1,2,3}}
def positionFn : Layout → Fin 4 → Fin 21 := ![![11,10,9,20],![9,10,8,11]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 4 ↪ Fin 21 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨21,[10,11,12,21],[⟨[],13⟩,⟨[12],5⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[10],4⟩,⟨[10,11],1⟩,⟨[21],4⟩,⟨[11,21],1⟩,⟨[10,12,21],1⟩,⟨[10,11,21],1⟩],none,[12,11,10,21]⟩,⟨21,[9,10,11,12],[⟨[],13⟩,⟨[10],5⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[9],4⟩,⟨[9,11],1⟩,⟨[12],4⟩,⟨[11,12],1⟩,⟨[9,10,12],1⟩,⟨[9,11,12],1⟩],none,[10,11,9,12]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(833333/10000000),(9166667/10000000)]
def beta : Layout → Fin 4 → ℚ := ![![(833333/10000000),(833333/10000000),(0/1),(0/1)],![(9166667/10000000),(9166667/10000000),(0/1),(0/1)]]
def R : Fin 4 → Quota → Finset (Fin 4) := ![![{2},{1,2}],![{2},{3}],![∅,∅],![∅,∅]]
def delta : Fin 4 → Quota → ℚ := ![![(5399/625000),(17277/10000000)],![(5489/625000),(15837/10000000)],![(0/1),(0/1)],![(0/1),(0/1)]]
def quota : Fin 4 → Quota → ℕ := ![![2,1],![1,1],![0,0],![0,0]]
end Aris4Math.ThirtyFour.TwentyOneSevenJointQuad21Data
