import Aris4Math.ThirtyFour.SingleLayoutApplication
namespace Aris4Math.ThirtyFour.TwentyOneSixPair77Data
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles
open scoped BigOperators
set_option maxRecDepth 100000
abbrev Case := Fin 3
abbrev Quota := Fin 2
def degree : Fin 2 → ℕ := ![7,7]
def labels : List (Finset (Fin 2)) := [∅,{0},{1},{0,1}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Case → Finset (Fin 2) → ℕ := ![fun T => if T=∅ then 25 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 5 else 0,fun T => if T=∅ then 26 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 6 else 0,fun T => if T=∅ then 27 else if T={0,1} then 7 else 0]
def co : Case → Fin 1 → ℕ := ![![5],![6],![7]]
def positionFn : Case → Fin 2 → Fin 21 := ![![9,10],![9,10],![9,10]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel
def positions (i : Case) : Fin 2 ↪ Fin 21 := ⟨positionFn i,positionFn_injective i⟩
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i=profile labels (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Case → Numeric.Profile := ![⟨21,[10,11],[⟨[],25⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[10,11],5⟩],none,[10,11]⟩,⟨21,[10,11],[⟨[],26⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],6⟩],none,[10,11]⟩,⟨21,[10,11],[⟨[],27⟩,⟨[10,11],7⟩],none,[10,11]⟩]
set_option maxHeartbeats 0 in
theorem p_eq_computed (i : Case) : p i=computed i := by fin_cases i <;> rfl
def loss : Case → Fin 2 → ℚ := ![![(0/1),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)]]
def R : Case → Fin 2 → Quota → Finset (Fin 2) := ![![![∅,{1}],![∅,{0}]],![![∅,{1}],![∅,{0}]],![![∅,{1}],![∅,{0}]]]
def α : Case → Fin 2 → Quota → ℚ := ![![![(0/1),(42/4199)],![(0/1),(42/4199)]],![![(0/1),(42/4199)],![(0/1),(42/4199)]],![![(0/1),(42/4199)],![(0/1),(42/4199)]]]
def quota : Case → Fin 2 → Quota → ℕ := ![![![3,0],![3,0]],![![3,0],![3,0]],![![3,0],![3,0]]]
end Aris4Math.ThirtyFour.TwentyOneSixPair77Data
