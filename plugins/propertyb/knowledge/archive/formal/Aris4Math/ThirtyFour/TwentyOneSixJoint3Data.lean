import Aris4Math.ThirtyFour.MixedLayoutFive
namespace Aris4Math.ThirtyFour.TwentyOneSixJoint3Data
open scoped BigOperators
open Aris4Math.ThirtyThree.FiveProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin 6
abbrev Quota := Fin 4
def μ (T : Finset (Fin 5)) : ℕ := if T=∅ then 8 else if T={0} then 3 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={3} then 3 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,2,3} then 1 else if T={4} then 3 else if T={0,4} then 1 else if T={2,4} then 1 else if T={1,2,4} then 1 else if T={3,4} then 2 else 0
def support : Finset (Finset (Fin 5)) := {∅,{0},{1},{0,1},{2},{3},{1,3},{2,3},{0,2,3},{4},{0,4},{2,4},{1,2,4},{3,4}}
def positionFn : Layout → Fin 5 → Fin 21 := ![![9,11,8,12,10],![9,11,10,12,8],![9,10,20,8,11],![10,9,20,8,11],![10,9,20,11,8],![11,9,8,10,20]]
theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 5 ↪ Fin 21 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout → Numeric.Profile := ![⟨21,[9,10,11,12,13],[⟨[],8⟩,⟨[10],3⟩,⟨[12],4⟩,⟨[10,12],1⟩,⟨[9],4⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[9,13],1⟩,⟨[9,10,13],1⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[9,11],1⟩,⟨[9,11,12],1⟩,⟨[11,13],2⟩],none,[10,12,9,13,11]⟩,⟨21,[9,10,11,12,13],[⟨[],8⟩,⟨[10],3⟩,⟨[12],4⟩,⟨[10,12],1⟩,⟨[11],4⟩,⟨[13],3⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[10,11,13],1⟩,⟨[9],3⟩,⟨[9,10],1⟩,⟨[9,11],1⟩,⟨[9,11,12],1⟩,⟨[9,13],2⟩],none,[10,12,11,13,9]⟩,⟨21,[9,10,11,12,21],[⟨[],8⟩,⟨[10],3⟩,⟨[11],4⟩,⟨[10,11],1⟩,⟨[21],4⟩,⟨[9],3⟩,⟨[9,11],1⟩,⟨[9,21],1⟩,⟨[9,10,21],1⟩,⟨[12],3⟩,⟨[10,12],1⟩,⟨[12,21],1⟩,⟨[11,12,21],1⟩,⟨[9,12],2⟩],none,[10,11,21,9,12]⟩,⟨21,[9,10,11,12,21],[⟨[],8⟩,⟨[11],3⟩,⟨[10],4⟩,⟨[10,11],1⟩,⟨[21],4⟩,⟨[9],3⟩,⟨[9,10],1⟩,⟨[9,21],1⟩,⟨[9,11,21],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[12,21],1⟩,⟨[10,12,21],1⟩,⟨[9,12],2⟩],none,[11,10,21,9,12]⟩,⟨21,[9,10,11,12,21],[⟨[],8⟩,⟨[11],3⟩,⟨[10],4⟩,⟨[10,11],1⟩,⟨[21],4⟩,⟨[12],3⟩,⟨[10,12],1⟩,⟨[12,21],1⟩,⟨[11,12,21],1⟩,⟨[9],3⟩,⟨[9,11],1⟩,⟨[9,21],1⟩,⟨[9,10,21],1⟩,⟨[9,12],2⟩],none,[11,10,21,12,9]⟩,⟨21,[9,10,11,12,21],[⟨[],8⟩,⟨[12],3⟩,⟨[10],4⟩,⟨[10,12],1⟩,⟨[9],4⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[9,11],1⟩,⟨[9,11,12],1⟩,⟨[21],3⟩,⟨[12,21],1⟩,⟨[9,21],1⟩,⟨[9,10,21],1⟩,⟨[11,21],2⟩],none,[12,10,9,11,21]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout → ℚ := ![(1651812/10000001),(1241830/10000001),(1176471/10000001),(475342/10000001),(3/11),(3/11)]
def beta : Layout → Fin 5 → ℚ := ![![(1651812/10000001),(1651812/10000001),(0/1),(0/1),(1651812/10000001)],![(1241830/10000001),(1241830/10000001),(1241830/10000001),(0/1),(0/1)],![(1176471/10000001),(1176471/10000001),(0/1),(0/1),(1176471/10000001)],![(475342/10000001),(475342/10000001),(0/1),(0/1),(475342/10000001)],![(3/11),(3/11),(0/1),(3/11),(0/1)],![(3/11),(3/11),(0/1),(3/11),(0/1)]]
def R : Fin 5 → Quota → Finset (Fin 5) := ![![∅,{1},{4},∅],![∅,{0},{2},{3}],![{0,1},∅,∅,∅],![{0},∅,∅,∅],![{1},∅,∅,∅]]
def delta : Fin 5 → Quota → ℚ := ![![(87024/10000001),(10878/10000001),(10878/10000001),(0/1)],![(31354/10000001),(31936/10000001),(34612/10000001),(10878/10000001)],![(12158/10000001),(0/1),(0/1),(0/1)],![(53401/10000001),(0/1),(0/1),(0/1)],![(32343/10000001),(0/1),(0/1),(0/1)]]
def quota : Fin 5 → Quota → ℕ := ![![2,1,1,0],![3,2,2,2],![2,0,0,0],![3,0,0,0],![3,0,0,0]]
end Aris4Math.ThirtyFour.TwentyOneSixJoint3Data
