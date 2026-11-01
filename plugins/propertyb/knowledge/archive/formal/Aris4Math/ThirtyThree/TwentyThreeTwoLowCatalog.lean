import Aris4Math.ThirtyThree.TwentyThreeTwoLowHighCatalog
import Aris4Math.ThirtyThree.TwentyThreeTwoLowData

namespace Aris4Math.ThirtyThree.TwentyThreeTwoLowCatalog
open TwentyThreeTwoLowHighCatalog
open TwentyFourMatchingHighCatalog (largeTypes highValue pairSum)
open TwentyThreeTwoLowData

def degreeData (i : Fin 5) : ℕ := if i.val < 2 then 6 else 7

theorem permutation_left : ∀ r i, inverseFn r (permFn r i) = i := by decide +kernel
theorem permutation_right : ∀ r i, permFn r (inverseFn r i) = i := by decide +kernel
def permutation (r : Fin 12) : Fin 5 ≃ Fin 5 where
  toFun := permFn r
  invFun := inverseFn r
  left_inv := permutation_left r
  right_inv := permutation_right r

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem choice_exact : ∀ a b : Fin 3, ∀ s : Fin 55,
    Admissible (a.val+1) (b.val+1) (catalog s) →
    let c := selectedGroup a b s
    let σ := permutation (selectedPerm a b s)
    params c = (a,b) ∧
    (∀ i, degreeData (σ i) = degreeData i) ∧
    (∀ i j, pairDegree (a.val+1) (b.val+1) (σ i) (σ j) =
      pairDegree (a.val+1) (b.val+1) i j) ∧
    (∀ T : Finset (Fin 5), 3 ≤ T.card →
      highValue (catalog s) (T.image σ) = counts c T) := by
  intro a b s
  fin_cases a <;> fin_cases b <;> fin_cases s <;> unfold Admissible <;> decide +kernel

theorem classify (a b : ℕ) (h : Fin 16 → Bool)
    (ha : 1 ≤ a ∧ a ≤ 3) (hb : 1 ≤ b ∧ b ≤ 3)
    (admissible : Admissible a b h) :
    ∃ c : Case, ∃ σ : Fin 5 ≃ Fin 5,
      (params c).1.val+1 = a ∧ (params c).2.val+1 = b ∧
      (∀ i, degreeData (σ i) = degreeData i) ∧
      (∀ i j, pairDegree a b (σ i) (σ j) = pairDegree a b i j) ∧
      (∀ T : Finset (Fin 5), 3 ≤ T.card → highValue h (T.image σ) = counts c T) := by
  obtain ⟨s,hs⟩ := covers a b h ha.2 hb.2 admissible
  have heq : h = catalog s := funext hs
  subst h
  let aa : Fin 3 := ⟨a-1,by omega⟩
  let bb : Fin 3 := ⟨b-1,by omega⟩
  have ae : aa.val+1 = a := by dsimp [aa]; omega
  have be : bb.val+1 = b := by dsimp [bb]; omega
  have result := choice_exact aa bb s
  rw [ae,be] at result
  obtain ⟨hp,hd,hpair,hh⟩ := result admissible
  refine ⟨selectedGroup aa bb s,permutation (selectedPerm aa bb s),?_,?_,hd,hpair,hh⟩
  · rw [hp]; exact ae
  · rw [hp]; exact be

end Aris4Math.ThirtyThree.TwentyThreeTwoLowCatalog
#print axioms Aris4Math.ThirtyThree.TwentyThreeTwoLowCatalog.classify
