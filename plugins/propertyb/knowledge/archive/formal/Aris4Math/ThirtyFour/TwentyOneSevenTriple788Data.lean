import Aris4Math.ThirtyFour.SingleLayoutApplication
namespace Aris4Math.ThirtyFour.TwentyOneSevenTriple788Data
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles
open scoped BigOperators
set_option maxRecDepth 100000
abbrev Case := Fin 11
abbrev Quota := Fin 2
def degree : Fin 3 → ℕ := ![7,8,8]
def labels : List (Finset (Fin 3)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
def μ : Case → Finset (Fin 3) → ℕ := ![fun T => if T=∅ then 16 else if T={0} then 5 else if T={1} then 4 else if T={0,1} then 1 else if T={2} then 4 else if T={0,2} then 1 else if T={1,2} then 3 else 0,fun T => if T=∅ then 15 else if T={0} then 6 else if T={1} then 5 else if T={2} then 5 else if T={1,2} then 2 else if T={0,1,2} then 1 else 0,fun T => if T=∅ then 17 else if T={0} then 5 else if T={1} then 3 else if T={0,1} then 1 else if T={2} then 3 else if T={0,2} then 1 else if T={1,2} then 4 else 0,fun T => if T=∅ then 16 else if T={0} then 6 else if T={1} then 4 else if T={2} then 4 else if T={1,2} then 3 else if T={0,1,2} then 1 else 0,fun T => if T=∅ then 18 else if T={0} then 5 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 5 else 0,fun T => if T=∅ then 17 else if T={0} then 6 else if T={1} then 3 else if T={2} then 3 else if T={1,2} then 4 else if T={0,1,2} then 1 else 0,fun T => if T=∅ then 19 else if T={0} then 5 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 6 else 0,fun T => if T=∅ then 18 else if T={0} then 6 else if T={1} then 2 else if T={2} then 2 else if T={1,2} then 5 else if T={0,1,2} then 1 else 0,fun T => if T=∅ then 20 else if T={0} then 5 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 7 else 0,fun T => if T=∅ then 19 else if T={0} then 6 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 6 else if T={0,1,2} then 1 else 0,fun T => if T=∅ then 20 else if T={0} then 6 else if T={1,2} then 7 else if T={0,1,2} then 1 else 0]
def co : Case → Fin 3 → ℕ := ![![1,1,3],![1,1,3],![1,1,4],![1,1,4],![1,1,5],![1,1,5],![1,1,6],![1,1,6],![1,1,7],![1,1,7],![1,1,8]]
def triple : Case → ℕ := ![0,1,0,1,0,1,0,1,0,1,1]
def positionFn : Case → Fin 3 → Fin 21 := ![![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel
def positions (i : Case) : Fin 3 ↪ Fin 21 := ⟨positionFn i,positionFn_injective i⟩
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i=profile labels (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Case → Numeric.Profile := ![⟨21,[10,11,12],[⟨[],16⟩,⟨[11],5⟩,⟨[10],4⟩,⟨[10,11],1⟩,⟨[12],4⟩,⟨[11,12],1⟩,⟨[10,12],3⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],15⟩,⟨[11],6⟩,⟨[10],5⟩,⟨[12],5⟩,⟨[10,12],2⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],17⟩,⟨[11],5⟩,⟨[10],3⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[10,12],4⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],16⟩,⟨[11],6⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,12],3⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],18⟩,⟨[11],5⟩,⟨[10],2⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[10,12],5⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],17⟩,⟨[11],6⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[10,12],4⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],5⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[10,12],6⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],18⟩,⟨[11],6⟩,⟨[10],2⟩,⟨[12],2⟩,⟨[10,12],5⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],5⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],7⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],6⟩,⟨[10],1⟩,⟨[12],1⟩,⟨[10,12],6⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],6⟩,⟨[10,12],7⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩]
set_option maxHeartbeats 0 in
theorem p_eq_computed (i : Case) : p i=computed i := by fin_cases i <;> rfl
def loss : Case → Fin 3 → ℚ := ![![(21/715),(0/1),(0/1)],![(252/12155),(126/12155),(126/12155)],![(21/715),(0/1),(0/1)],![(252/12155),(0/1),(0/1)],![(21/715),(0/1),(0/1)],![(252/12155),(0/1),(0/1)],![(21/715),(0/1),(0/1)],![(252/12155),(0/1),(0/1)],![(21/715),(0/1),(0/1)],![(252/12155),(0/1),(0/1)],![(252/12155),(0/1),(0/1)]]
def R : Case → Fin 3 → Quota → Finset (Fin 3) := ![![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]],![![∅,{1,2}],![∅,{0,2}],![∅,{0,1}]]]
def α : Case → Fin 3 → Quota → ℚ := ![![![(21/2210),(21/24310)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(21/2210),(21/24310)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(21/2210),(21/24310)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(21/2210),(21/24310)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(21/2210),(21/24310)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)]],![![(0/1),(126/12155)],![(0/1),(126/12155)],![(0/1),(126/12155)]]]
def quota : Case → Fin 3 → Quota → ℕ := ![![![3,1],![4,0],![4,0]],![![3,2],![4,1],![4,1]],![![3,1],![4,0],![4,0]],![![3,2],![4,0],![4,0]],![![3,1],![4,0],![4,0]],![![3,2],![4,0],![4,0]],![![3,1],![4,0],![4,0]],![![3,2],![4,0],![4,0]],![![3,1],![4,0],![4,0]],![![3,2],![4,0],![4,0]],![![3,2],![4,0],![4,0]]]
set_option maxHeartbeats 0 in
theorem μ_eq_recovered : ∀ i T, μ i T=Aris4Math.ThirtyThree.TripleProfiles.recovered 34
    (degree 0) (degree 1) (degree 2) (co i 0) (co i 1) (co i 2) (triple i) T := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenTriple788Data
