import Aris4Math.ThirtyThree.TwentyThreeThreeLowHighCatalog
import Aris4Math.ThirtyThree.TwentyThreeThreeLowData

namespace Aris4Math.ThirtyThree.TwentyThreeThreeLowCatalog
open TwentyThreeThreeLowHighCatalog TwentyThreeThreeLowData

def degreeData (i : Fin 5) : ℕ := if i.val < 3 then 6 else 7

theorem permutation_left : ∀ r i, inverseFn r (permFn r i) = i := by decide +kernel
theorem permutation_right : ∀ r i, permFn r (inverseFn r i) = i := by decide +kernel
def permutation (r : Fin 12) : Fin 5 ≃ Fin 5 where
  toFun := permFn r
  invFun := inverseFn r
  left_inv := permutation_left r
  right_inv := permutation_right r

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem excess_complete : ∀ a b c : Fin 3,
    a.val+b.val ≤ 2 → a.val+c.val ≤ 2 → b.val+c.val ≤ 2 →
    ∃ s : Fin 11, excessCatalog s = ![a.val,b.val,c.val] := by decide +kernel

theorem excess_classify (e : Fin 3 → ℕ) (he : ∀ i, e i ≤ 2)
    (h01 : e 0+e 1 ≤ 2) (h02 : e 0+e 2 ≤ 2) (h12 : e 1+e 2 ≤ 2) :
    ∃ s : Fin 11, excessCatalog s = e := by
  have hv : ![e 0,e 1,e 2] = e := by funext i; fin_cases i <;> rfl
  obtain ⟨s,hs⟩ := excess_complete ⟨e 0,by have := he 0; omega⟩
    ⟨e 1,by have := he 1; omega⟩ ⟨e 2,by have := he 2; omega⟩ h01 h02 h12
  exact ⟨s,hs.trans hv⟩

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem choice_exact : ∀ e : Fin 11, ∀ b : Fin 3, ∀ s : Fin 131,
    Admissible (excessCatalog e) (b.val+1) (catalog s) →
    let c := selectedGroup e b s
    let σ := permutation (selectedPerm e b s)
    (∀ i, degreeData (σ i) = degreeData i) ∧
    (∀ i j, pairDegree (excessCatalog e) (b.val+1) (σ i) (σ j) =
      pairDegree (lowExcess c) (highCodegree c) i j) ∧
    (∀ T : Finset (Fin 5), 3 ≤ T.card →
      highValue (catalog s) (T.image σ) = counts c T) := by
  intro e b
  fin_cases e <;> fin_cases b <;> unfold Admissible <;> decide +kernel

theorem classify (e : Fin 3 → ℕ) (b : ℕ) (h : Fin 16 → ℕ)
    (he : ∀ i, e i ≤ 2)
    (h01 : e 0+e 1 ≤ 2) (h02 : e 0+e 2 ≤ 2) (h12 : e 1+e 2 ≤ 2)
    (hb : 1 ≤ b ∧ b ≤ 3) (first : h 0 ≤ 2)
    (rest : ∀ i : Fin 16, i ≠ 0 → h i ≤ 1) (admissible : Admissible e b h) :
    ∃ c : Case, ∃ σ : Fin 5 ≃ Fin 5,
      (∀ i, degreeData (σ i) = degreeData i) ∧
      (∀ i j, pairDegree e b (σ i) (σ j) = pairDegree (lowExcess c) (highCodegree c) i j) ∧
      (∀ T : Finset (Fin 5), 3 ≤ T.card → highValue h (T.image σ) = counts c T) := by
  obtain ⟨s,hs⟩ := covers e b h he hb.2 first rest admissible
  have heq : h = catalog s := funext hs
  subst h
  obtain ⟨q,hq⟩ := excess_classify e he h01 h02 h12
  let bb : Fin 3 := ⟨b-1,by omega⟩
  have be : bb.val+1 = b := by dsimp [bb]; omega
  have result := choice_exact q bb s
  rw [be,hq] at result
  exact ⟨selectedGroup q bb s,permutation (selectedPerm q bb s),result admissible⟩

end Aris4Math.ThirtyThree.TwentyThreeThreeLowCatalog
#print axioms Aris4Math.ThirtyThree.TwentyThreeThreeLowCatalog.classify
