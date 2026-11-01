import Aris4Math.ThirtyFour.LocalProfiles
namespace Aris4Math.ThirtyFour.TwentyOneSevenJointQuad0Data
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 7
abbrev Quota := Fin 4
def labels : List (Finset (Fin 4)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀T,T∈labels := by decide +kernel
def μ (T : Finset (Fin 4)) : ℕ := if T=∅ then 13 else if T={0} then 4 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 2 else 0
def support : Finset (Finset (Fin 4)) := {∅,{0},{1},{0,1},{2},{0,2},{1,2},{3},{0,3},{1,3},{2,3}}
def positionFn : Layout → Fin 4 → Fin 21 := ![![9,11,10,20],![9,11,20,10],![11,9,20,10],![11,10,20,9],![9,10,11,8],![9,11,10,8],![10,9,8,11]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 4 ↪ Fin 21 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨21,[10,11,12,21],[⟨[],13⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,12],1⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[21],3⟩,⟨[10,21],1⟩,⟨[12,21],1⟩,⟨[11,21],2⟩],none,[10,12,11,21]⟩,⟨21,[10,11,12,21],[⟨[],13⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,12],1⟩,⟨[21],3⟩,⟨[10,21],1⟩,⟨[12,21],1⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[11,21],2⟩],none,[10,12,21,11]⟩,⟨21,[10,11,12,21],[⟨[],13⟩,⟨[12],4⟩,⟨[10],4⟩,⟨[10,12],1⟩,⟨[21],3⟩,⟨[12,21],1⟩,⟨[10,21],1⟩,⟨[11],3⟩,⟨[11,12],1⟩,⟨[10,11],1⟩,⟨[11,21],2⟩],none,[12,10,21,11]⟩,⟨21,[10,11,12,21],[⟨[],13⟩,⟨[12],4⟩,⟨[11],4⟩,⟨[11,12],1⟩,⟨[21],3⟩,⟨[12,21],1⟩,⟨[11,21],1⟩,⟨[10],3⟩,⟨[10,12],1⟩,⟨[10,11],1⟩,⟨[10,21],2⟩],none,[12,11,21,10]⟩,⟨21,[9,10,11,12],[⟨[],13⟩,⟨[10],4⟩,⟨[11],4⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[9],3⟩,⟨[9,10],1⟩,⟨[9,11],1⟩,⟨[9,12],2⟩],none,[10,11,12,9]⟩,⟨21,[9,10,11,12],[⟨[],13⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,12],1⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[9],3⟩,⟨[9,10],1⟩,⟨[9,12],1⟩,⟨[9,11],2⟩],none,[10,12,11,9]⟩,⟨21,[9,10,11,12],[⟨[],13⟩,⟨[11],4⟩,⟨[10],4⟩,⟨[10,11],1⟩,⟨[9],3⟩,⟨[9,11],1⟩,⟨[9,10],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[10,12],1⟩,⟨[9,12],2⟩],none,[11,10,9,12]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(1/8),(28409/2500000),(1/8),(623967/2000000),(909091/2500000),(28409/2500000),(516529/10000000)]
def beta : Layout → Fin 4 → ℚ := ![![(1/8),(1/8),(1/8),(0/1)],![(28409/2500000),(28409/2500000),(0/1),(28409/2500000)],![(1/8),(1/8),(0/1),(1/8)],![(623967/2000000),(623967/2000000),(0/1),(623967/2000000)],![(909091/2500000),(909091/2500000),(909091/2500000),(0/1)],![(28409/2500000),(28409/2500000),(28409/2500000),(0/1)],![(516529/10000000),(516529/10000000),(0/1),(516529/10000000)]]
def R : Fin 4 → Quota → Finset (Fin 4) := ![![∅,{1},{2},{3}],![∅,{0},{2},{3}],![{0},{1},{3},∅],![{0},{1},{2},∅]]
def delta : Fin 4 → Quota → ℚ := ![![(14921/2000000),(1767/1250000),(6479/10000000),(4221/5000000)],![(14921/2000000),(1767/1250000),(4221/5000000),(6479/10000000)],![(27/125000),(5939/2500000),(5183/2000000),(0/1)],![(5939/2500000),(27/125000),(5183/2000000),(0/1)]]
def quota : Fin 4 → Quota → ℕ := ![![3,2,2,2],![3,2,2,2],![2,2,1,0],![2,2,1,0]]
end Aris4Math.ThirtyFour.TwentyOneSevenJointQuad0Data
