import Aris4Math.ThirtyFour.SingleLayoutApplication
namespace Aris4Math.ThirtyFour.TwentyOneSixQuad6777Data
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles
open scoped BigOperators
set_option maxRecDepth 100000
abbrev Case := Fin 4
abbrev Quota := Fin 2
def degree : Fin 4 → ℕ := ![6,7,7,7]
def labels : List (Finset (Fin 4)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Case → Finset (Fin 4) → ℕ := ![fun T => if T=∅ then 13 else if T={0} then 5 else if T={1} then 4 else if T={2} then 4 else if T={1,2} then 1 else if T={3} then 4 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,1,2,3} then 1 else 0,fun T => if T=∅ then 12 else if T={0} then 5 else if T={1} then 5 else if T={2} then 5 else if T={3} then 5 else if T={1,2,3} then 1 else if T={0,1,2,3} then 1 else 0,fun T => if T=∅ then 16 else if T={1} then 3 else if T={0,1} then 2 else if T={2} then 3 else if T={0,2} then 2 else if T={1,2} then 1 else if T={3} then 3 else if T={0,3} then 2 else if T={1,3} then 1 else if T={2,3} then 1 else 0,fun T => if T=∅ then 15 else if T={1} then 4 else if T={0,1} then 2 else if T={2} then 4 else if T={0,2} then 2 else if T={3} then 4 else if T={0,3} then 2 else if T={1,2,3} then 1 else 0]
def co : Case → Fin 6 → ℕ := ![![1,1,1,2,2,2],![1,1,1,2,2,2],![2,2,2,1,1,1],![2,2,2,1,1,1]]
def high : Case → Fin 5 → ℕ := ![![0,0,0,0,1],![0,0,0,1,1],![0,0,0,0,0],![0,0,0,1,0]]
def positionFn : Case → Fin 4 → Fin 21 := ![![10,9,11,20],![10,9,11,20],![9,18,19,20],![9,18,19,20]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel
def positions (i : Case) : Fin 4 ↪ Fin 21 := ⟨positionFn i,positionFn_injective i⟩
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i=profile labels (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Case → Numeric.Profile := ![⟨21,[10,11,12,21],[⟨[],13⟩,⟨[11],5⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,12],1⟩,⟨[21],4⟩,⟨[10,21],1⟩,⟨[12,21],1⟩,⟨[10,11,12,21],1⟩],none,[11,10,12,21]⟩,⟨21,[10,11,12,21],[⟨[],12⟩,⟨[11],5⟩,⟨[10],5⟩,⟨[12],5⟩,⟨[21],5⟩,⟨[10,12,21],1⟩,⟨[10,11,12,21],1⟩],none,[11,10,12,21]⟩,⟨21,[10,19,20,21],[⟨[],16⟩,⟨[19],3⟩,⟨[10,19],2⟩,⟨[20],3⟩,⟨[10,20],2⟩,⟨[19,20],1⟩,⟨[21],3⟩,⟨[10,21],2⟩,⟨[19,21],1⟩,⟨[20,21],1⟩],none,[10,19,20,21]⟩,⟨21,[10,19,20,21],[⟨[],15⟩,⟨[19],4⟩,⟨[10,19],2⟩,⟨[20],4⟩,⟨[10,20],2⟩,⟨[21],4⟩,⟨[10,21],2⟩,⟨[19,20,21],1⟩],none,[10,19,20,21]⟩]
set_option maxHeartbeats 0 in
theorem p_eq_computed (i : Case) : p i=computed i := by fin_cases i <;> rfl
def loss : Case → Fin 4 → ℚ := ![![(126/12155),(0/1),(0/1),(0/1)],![(126/12155),(252/12155),(126/12155),(0/1)],![(0/1),(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1),(0/1)]]
def R : Case → Fin 4 → Quota → Finset (Fin 4) := ![![![∅,{1,2,3}],![∅,{0,2,3}],![∅,{0,1,3}],![∅,{0,1,2}]],![![∅,{1,2,3}],![∅,{0,2,3}],![∅,{0,1,3}],![∅,{0,1,2}]],![![∅,{1,2,3}],![∅,{0,2,3}],![∅,{0,1,3}],![∅,{0,1,2}]],![![∅,{1,2,3}],![∅,{0,2,3}],![∅,{0,1,3}],![∅,{0,1,2}]]]
def α : Case → Fin 4 → Quota → ℚ := ![![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(0/1)]],![![(0/1),(126/12155)],![(126/12155),(0/1)],![(0/1),(126/12155)],![(0/1),(0/1)]],![![(0/1),(126/12155)],![(0/1),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)]],![![(0/1),(126/12155)],![(0/1),(0/1)],![(0/1),(0/1)],![(0/1),(0/1)]]]
def quota : Case → Fin 4 → Quota → ℕ := ![![![2,1],![3,0],![3,0],![3,0]],![![2,1],![3,1],![3,1],![3,1]],![![2,0],![3,0],![3,0],![3,0]],![![2,0],![3,0],![3,0],![3,0]]]
set_option maxHeartbeats 0 in
theorem μ_eq_recovered : ∀ i T, μ i T=Aris4Math.ThirtyThree.QuadProfiles.recovered 34
    degree (co i) (high i) T := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSixQuad6777Data
