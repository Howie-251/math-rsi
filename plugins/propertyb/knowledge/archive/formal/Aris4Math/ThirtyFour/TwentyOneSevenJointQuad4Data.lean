import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyOneSevenJointQuad4Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 4
abbrev Quota := Fin 3
def labels : List (Finset (Fin 4)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀T,T∈labels := by decide +kernel
def μ (T : Finset (Fin 4)) : ℕ := if T=∅ then 12 else if T={0} then 5 else if T={1} then 5 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 4 else if T={0,1,3} then 1 else if T={2,3} then 2 else 0
def support : Finset (Finset (Fin 4)) := {∅,{0},{1},{2},{0,2},{1,2},{3},{0,1,3},{2,3}}
def positionFn : Layout → Fin 4 → Fin 21 := ![![9,10,11,8],![9,11,10,8],![10,9,11,8],![11,9,10,8]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 4 ↪ Fin 21 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨21,[9,10,11,12],[⟨[],12⟩,⟨[10],5⟩,⟨[11],5⟩,⟨[12],3⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[9],4⟩,⟨[9,10,11],1⟩,⟨[9,12],2⟩],none,[10,11,12,9]⟩,⟨21,[9,10,11,12],[⟨[],12⟩,⟨[10],5⟩,⟨[12],5⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[9],4⟩,⟨[9,10,12],1⟩,⟨[9,11],2⟩],none,[10,12,11,9]⟩,⟨21,[9,10,11,12],[⟨[],12⟩,⟨[11],5⟩,⟨[10],5⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[10,12],1⟩,⟨[9],4⟩,⟨[9,10,11],1⟩,⟨[9,12],2⟩],none,[11,10,12,9]⟩,⟨21,[9,10,11,12],[⟨[],12⟩,⟨[12],5⟩,⟨[10],5⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[10,11],1⟩,⟨[9],4⟩,⟨[9,10,12],1⟩,⟨[9,11],2⟩],none,[12,10,11,9]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(733471/2500000),(1/4),(4338843/10000000),(227273/10000000)]
def beta : Layout → Fin 4 → ℚ := ![![(733471/2500000),(733471/2500000),(733471/2500000),(0/1)],![(1/4),(1/4),(1/4),(0/1)],![(4338843/10000000),(4338843/10000000),(4338843/10000000),(0/1)],![(227273/10000000),(227273/10000000),(227273/10000000),(0/1)]]
def R : Fin 4 → Quota → Finset (Fin 4) := ![![∅,{1,2},∅],![∅,{2},{0,2}],![{0},{1},{3}],![∅,∅,∅]]
def delta : Fin 4 → Quota → ℚ := ![![(86777/10000000),(4221/2500000),(0/1)],![(90703/10000000),(2513/2000000),(393/10000000)],![(47511/10000000),(4319/10000000),(51831/10000000)],![(0/1),(0/1),(0/1)]]
def quota : Fin 4 → Quota → ℕ := ![![3,1,0],![3,2,1],![2,2,1],![0,0,0]]
end Aris4Math.ThirtyFour.TwentyOneSevenJointQuad4Data
