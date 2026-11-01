import Aris4Math.ThirtyThree.TwentyOneStructure
import Aris4Math.ThirtyThree.TwentyOnePairs

/-! Actual 21-point structural pair cases feed the complete checked two-lock
probability callers. Triple helpers express literal edge-filter relations. -/

namespace Aris4Math.ThirtyThree.TwentyOnePairAssembly

open TwentyOnePairs TripleProfiles

theorem codegree_le_degree {v : ℕ} (H : Simple5Hypergraph (Fin v)) (x y : Fin v) :
    H.codegree x y ≤ H.degree x := by
  apply Finset.card_le_card
  intro e he
  obtain ⟨he,hx,_⟩ := Finset.mem_filter.mp he
  exact Finset.mem_filter.mpr ⟨he,hx⟩

theorem propertyB_of_pairCase (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (x y : Fin 21) (hne : x ≠ y) (hcase : TwentyOneStructure.PairCase H x y) :
    PropertyB H := by
  have lo := H.one_le_codegree cover hne
  have hi := codegree_le_degree H x y
  rcases hcase with ⟨dx,dyl,dyu,lc⟩ | ⟨dx,dy⟩ | ⟨dx,dy,ln⟩ | ⟨dx,dy,ll⟩
  · apply propertyB_of_low_pair H cover edges33 x y hne ⟨5,H.degree y,1,10,11⟩
      ?_ dx rfl lc
    interval_cases hd : H.degree y <;> simp [lowCases,hd]
  · rw [dx] at hi
    by_cases low : H.codegree x y ≤ 2
    · interval_cases hc : H.codegree x y
      · exact propertyB_of_low_pair H cover edges33 x y hne ⟨6,6,1,10,11⟩
          (by decide) dx dy hc
      · exact propertyB_of_low_pair H cover edges33 x y hne ⟨6,6,2,10,12⟩
          (by decide) dx dy hc
    · apply propertyB_of_high_pair H edges33 x y hne ⟨6,6,H.codegree x y,8,12⟩
        ?_ dx dy rfl
      have h3 : 3 ≤ H.codegree x y := by omega
      interval_cases hc : H.codegree x y <;> simp [highCases,hc]
  · rw [dx] at hi
    by_cases one : H.codegree x y = 1
    · exact propertyB_of_low_pair H cover edges33 x y hne ⟨6,7,1,10,11⟩
        (by decide) dx dy one
    · apply propertyB_of_high_pair H edges33 x y hne ⟨6,7,H.codegree x y,10,12⟩
        ?_ dx dy rfl
      have h3 : 3 ≤ H.codegree x y := by omega
      interval_cases hc : H.codegree x y <;> simp [highCases,hc]
  · rw [dx] at hi
    apply propertyB_of_high_pair H edges33 x y hne ⟨7,7,H.codegree x y,10,12⟩
      ?_ dx dy rfl
    interval_cases hc : H.codegree x y <;> simp [highCases,hc]

theorem tripleCodegree_zero {v : ℕ} (H : Simple5Hypergraph (Fin v)) (x y z : Fin v)
    (none : TwentyOneStructure.NoTriple H x y z) : tripleCodegree H x y z = 0 := by
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_notMem.mpr
  intro e he
  obtain ⟨he,hxyz⟩ := Finset.mem_filter.mp he
  exact none e he hxyz

theorem tripleCodegree_le_pairs {v : ℕ} (H : Simple5Hypergraph (Fin v)) (x y z : Fin v) :
    tripleCodegree H x y z ≤ H.codegree x y ∧
    tripleCodegree H x y z ≤ H.codegree x z ∧
    tripleCodegree H x y z ≤ H.codegree y z := by
  constructor
  · apply Finset.card_le_card
    intro e he
    obtain ⟨he,hx,hy,_⟩ := Finset.mem_filter.mp he
    exact Finset.mem_filter.mpr ⟨he,hx,hy⟩
  constructor
  · apply Finset.card_le_card
    intro e he
    obtain ⟨he,hx,_,hz⟩ := Finset.mem_filter.mp he
    exact Finset.mem_filter.mpr ⟨he,hx,hz⟩
  · apply Finset.card_le_card
    intro e he
    obtain ⟨he,_,hy,hz⟩ := Finset.mem_filter.mp he
    exact Finset.mem_filter.mpr ⟨he,hy,hz⟩

end Aris4Math.ThirtyThree.TwentyOnePairAssembly

#print axioms Aris4Math.ThirtyThree.TwentyOnePairAssembly.propertyB_of_pairCase
#print axioms Aris4Math.ThirtyThree.TwentyOnePairAssembly.tripleCodegree_zero
#print axioms Aris4Math.ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs
