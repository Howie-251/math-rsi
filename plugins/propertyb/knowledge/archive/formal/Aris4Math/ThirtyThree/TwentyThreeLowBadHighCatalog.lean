import Aris4Math.ThirtyThree.TwentyThreeTwoLowHighCatalog
import Aris4Math.ThirtyThree.TwentyThreeLowBadHighData

namespace Aris4Math.ThirtyThree.TwentyThreeLowBadHighCatalog
open TwentyThreeTwoLowHighCatalog
open TwentyFourMatchingHighCatalog (largeTypes highValue pairSum)
open TwentyThreeLowBadHighData
def permutationFn : Fin 24 → Fin 5 → Fin 5 := ![![0,1,2,3,4],![0,1,2,4,3],![0,1,3,2,4],![0,1,3,4,2],![0,1,4,2,3],![0,1,4,3,2],![0,2,1,3,4],![0,2,1,4,3],![0,2,3,1,4],![0,2,3,4,1],![0,2,4,1,3],![0,2,4,3,1],![0,3,1,2,4],![0,3,1,4,2],![0,3,2,1,4],![0,3,2,4,1],![0,3,4,1,2],![0,3,4,2,1],![0,4,1,2,3],![0,4,1,3,2],![0,4,2,1,3],![0,4,2,3,1],![0,4,3,1,2],![0,4,3,2,1]]
def inverseFn : Fin 24 → Fin 5 → Fin 5 := ![![0,1,2,3,4],![0,1,2,4,3],![0,1,3,2,4],![0,1,4,2,3],![0,1,3,4,2],![0,1,4,3,2],![0,2,1,3,4],![0,2,1,4,3],![0,3,1,2,4],![0,4,1,2,3],![0,3,1,4,2],![0,4,1,3,2],![0,2,3,1,4],![0,2,4,1,3],![0,3,2,1,4],![0,4,2,1,3],![0,3,4,1,2],![0,4,3,1,2],![0,2,3,4,1],![0,2,4,3,1],![0,3,2,4,1],![0,4,2,3,1],![0,3,4,2,1],![0,4,3,2,1]]
theorem permutation_left : ∀ r i, inverseFn r (permutationFn r i) = i := by decide +kernel
theorem permutation_right : ∀ r i, permutationFn r (inverseFn r i) = i := by decide +kernel
def permutation (r : Fin 24) : Fin 5 ≃ Fin 5 where
  toFun := permutationFn r
  invFun := inverseFn r
  left_inv := permutation_left r
  right_inv := permutation_right r
def choice : Fin 2 → Fin 3 → Fin 55 → Config := ![![![0,9,9,14,7,6,0,5,9,14,14,0,13,12,0,11,7,13,8,6,12,8,5,11,7,13,8,8,6,12,8,8,5,11,4,10,10,15,0,0,0,0,10,15,15,0,0,0,0,0,3,0,2,0,1],![16,30,30,37,25,0,0,0,23,35,35,0,28,0,0,0,21,34,0,20,33,27,19,32,21,34,0,22,20,33,27,22,19,32,18,31,31,38,26,0,0,0,24,36,36,0,29,0,0,0,17,0,0,0,0],![39,53,53,60,48,0,0,0,46,58,58,0,51,0,0,0,44,57,0,43,56,50,42,55,44,57,0,45,43,56,50,45,42,55,41,54,54,61,49,0,0,0,47,59,59,0,52,0,0,0,40,0,0,0,0]],![![62,71,71,76,69,68,0,67,71,76,76,78,75,74,0,73,69,75,70,68,74,70,67,73,69,75,70,70,68,74,70,70,67,73,66,72,72,77,0,0,0,0,72,77,77,79,0,0,0,0,65,0,64,0,63],![80,94,94,101,89,0,0,0,87,99,99,103,92,0,0,0,85,98,0,84,97,91,83,96,85,98,0,86,84,97,91,86,83,96,82,95,95,102,90,0,0,0,88,100,100,104,93,0,0,0,81,0,0,0,0],![105,119,119,126,114,0,0,0,112,124,124,128,117,0,0,0,110,123,0,109,122,116,108,121,110,123,0,111,109,122,116,111,108,121,107,120,120,127,115,0,0,0,113,125,125,129,118,0,0,0,106,0,0,0,0]]]
def permutationChoice : Fin 2 → Fin 3 → Fin 55 → Fin 24 := ![![![0,3,1,4,4,4,0,4,0,2,0,0,0,0,0,0,2,1,3,2,1,5,2,1,0,3,1,0,0,3,4,2,0,3,0,3,1,4,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],![0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,2,0,2,2,0,0,2,0,0,0,2,0,2,0,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],![0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,2,0,2,2,0,0,2,0,0,0,2,0,2,0,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]],![![0,3,1,4,4,4,0,4,0,2,0,0,0,0,0,0,2,1,3,2,1,5,2,1,0,3,1,0,0,3,4,2,0,3,0,3,1,4,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],![0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,2,0,2,2,0,0,2,0,0,0,2,0,2,0,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],![0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,2,0,2,2,0,0,2,0,0,0,2,0,2,0,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]]]

def Forbidden (b : ℕ) (h : Fin 16 → Bool) : Prop :=
  b = 1 ∨ ∀ T : Finset (Fin 5), {1,2,3} ⊆ T → highValue h T = 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem choice_exact : ∀ a : Fin 2, ∀ b : Fin 3, ∀ s : Fin 55,
    Admissible (a.val+2) (b.val+1) (catalog s) → Forbidden (b.val+1) (catalog s) →
    let c := choice a b s
    let σ := permutation (permutationChoice a b s)
    lowCodegree c = a.val+2 ∧ highCodegree c = b.val+1 ∧ σ 0 = 0 ∧
    (∀ i j, pairDegree (a.val+2) (b.val+1) (σ i) (σ j) =
      pairDegree (a.val+2) (b.val+1) i j) ∧
    (∀ T : Finset (Fin 5), 3 ≤ T.card →
      highValue (catalog s) (T.image σ) = counts c T) := by
  intro a b s
  fin_cases a <;> fin_cases b <;> fin_cases s <;> unfold Admissible Forbidden <;> decide +kernel

 theorem classify (a b : ℕ) (h : Fin 16 → Bool)
    (ha : 2 ≤ a ∧ a ≤ 3) (hb : 1 ≤ b ∧ b ≤ 3)
    (admissible : Admissible a b h) (forbidden : Forbidden b h) :
    ∃ c : Config, ∃ σ : Fin 5 ≃ Fin 5,
      lowCodegree c = a ∧ highCodegree c = b ∧ σ 0 = 0 ∧
      (∀ i j, pairDegree a b (σ i) (σ j) = pairDegree a b i j) ∧
      (∀ T : Finset (Fin 5), 3 ≤ T.card → highValue h (T.image σ) = counts c T) := by
  obtain ⟨s,hs⟩ := covers a b h ha.2 hb.2 admissible
  have heq : h = catalog s := funext hs
  subst h
  let aa : Fin 2 := ⟨a-2,by omega⟩
  let bb : Fin 3 := ⟨b-1,by omega⟩
  have ae : aa.val+2 = a := by dsimp [aa]; omega
  have be : bb.val+1 = b := by dsimp [bb]; omega
  have result := choice_exact aa bb s
  rw [ae,be] at result
  exact ⟨choice aa bb s,permutation (permutationChoice aa bb s),
    result admissible forbidden⟩
end Aris4Math.ThirtyThree.TwentyThreeLowBadHighCatalog
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowBadHighCatalog.classify
