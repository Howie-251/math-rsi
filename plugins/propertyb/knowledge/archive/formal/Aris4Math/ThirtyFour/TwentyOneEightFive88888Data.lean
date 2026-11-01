import Aris4Math.ThirtyFour.SingleLayoutApplication
namespace Aris4Math.ThirtyFour.TwentyOneEightFive88888Data
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles
open scoped BigOperators
set_option maxRecDepth 100000
abbrev Case := Fin 1
abbrev Quota := Fin 2
def degree : Fin 5 → ℕ := ![8,8,8,8,8]
def labels : List (Finset (Fin 5)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Case → Finset (Fin 5) → ℕ := ![fun T => if T=∅ then 4 else if T={0} then 6 else if T={1} then 5 else if T={2} then 5 else if T={3} then 5 else if T={0,1,2,3} then 1 else if T={4} then 3 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={1,2,3,4} then 1 else 0]
def co : Case → Fin 10 → ℕ := ![![1,1,1,1,2,2,2,2,2,2]]
def positionFn : Case → Fin 5 → Fin 21 := ![![17,9,18,19,20]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel
def positions (i : Case) : Fin 5 ↪ Fin 21 := ⟨positionFn i,positionFn_injective i⟩
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i=profile labels (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Case → Numeric.Profile := ![⟨21,[10,18,19,20,21],[⟨[],4⟩,⟨[18],6⟩,⟨[10],5⟩,⟨[19],5⟩,⟨[20],5⟩,⟨[10,18,19,20],1⟩,⟨[21],3⟩,⟨[18,21],1⟩,⟨[10,21],1⟩,⟨[19,21],1⟩,⟨[20,21],1⟩,⟨[10,19,20,21],1⟩],none,[18,10,19,20,21]⟩]
set_option maxHeartbeats 0 in
theorem p_eq_computed (i : Case) : p i=computed i := by fin_cases i <;> rfl
def loss : Case → Fin 5 → ℚ := ![![(0/1),(14/715),(0/1),(0/1),(0/1)]]
def R : Case → Fin 5 → Quota → Finset (Fin 5) := ![![![∅,{1,2,3,4}],![∅,{0,2,3,4}],![∅,{0,1,3,4}],![∅,{0,1,2,4}],![∅,{0,1,2,3}]]]
def α : Case → Fin 5 → Quota → ℚ := ![![![(0/1),(0/1)],![(0/1),(7/715)],![(0/1),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)]]]
def quota : Case → Fin 5 → Quota → ℕ := ![![![4,3],![4,2],![4,2],![4,2],![4,0]]]
def upper (i : Case) (T : Finset (Fin 5)) : ℕ :=
  ∑ U : Finset (Fin 5), if T⊆U then μ i U else 0
set_option maxHeartbeats 0 in
theorem μ_eq_recovered : ∀ i T, μ i T=Aris4Math.ThirtyThree.MultiLockRecovery.recovered (upper i) (μ i) T := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneEightFive88888Data
