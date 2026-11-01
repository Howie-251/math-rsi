import Aris4Math.ThirtyFour.TwentyLow

/-! Actual low-degree selection and complete degree-five/six branches at 20
vertices and 34 edges. The numeric profiles are built from the selected H. -/
namespace Aris4Math.ThirtyFour.TwentyLow
open scoped BigOperators
open Aris4Math.ThirtyFour.NineteenPairs

variable (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
  (edges34 : H.edges.card = 34)
include cover edges34

theorem propertyB_of_degree_five (x : Fin 20) (dx : H.degree x = 5) : PropertyB H := by
  have minimum (z : Fin 20) : 5 ≤ H.degree z := by
    have h := H.pairCovering_degree_bound cover z
    simp only [Fintype.card_fin] at h
    omega
  have good := H.goodPartners_budget cover x
  simp only [Fintype.card_fin,dx] at good
  have partner : ∃ y ∈ H.goodPartners x, H.degree y ≤ 8 := by
    by_contra hn
    have high (y : Fin 20) (hy : y ∈ H.goodPartners x) : 5+4 ≤ H.degree y := by
      have h : ¬ H.degree y ≤ 8 := fun he => hn ⟨y,hy,he⟩
      omega
    have hb := H.subset_degree_budget (H.goodPartners x) 5 4 minimum high
    simp only [Fintype.card_fin,edges34] at hb
    omega
  obtain ⟨y,hy,dy⟩ := partner
  obtain ⟨yx,codeg⟩ := (H.mem_goodPartners cover x y).mp hy
  have lower := minimum y
  have mem : (⟨5,H.degree y,1,10,11⟩ : PairCase) ∈ cases := by
    interval_cases h : H.degree y <;> decide
  exact propertyB_of_case H cover edges34 x y (Ne.symm yx) _ mem dx rfl codeg

theorem propertyB_of_six_pair (x y : Fin 20) (ne : x ≠ y)
    (dx : H.degree x = 6) (lower : 6 ≤ H.degree y) (upper : H.degree y ≤ 7) : PropertyB H := by
  have lambdaLower := H.one_le_codegree cover ne
  have lambdaUpper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H x y
  rw [dx] at lambdaUpper
  by_cases dy : H.degree y = 6
  · by_cases small : H.codegree x y ≤ 3
    · have mem : (⟨6,6,H.codegree x y,10,11⟩ : PairCase) ∈ cases := by
        interval_cases h : H.codegree x y <;> decide
      exact propertyB_of_case H cover edges34 x y ne _ mem dx dy rfl
    · have mem : (⟨6,6,H.codegree x y,1,11⟩ : PairCase) ∈ cases := by
        have : 4 ≤ H.codegree x y := by omega
        interval_cases h : H.codegree x y <;> decide
      exact propertyB_of_case H cover edges34 x y ne _ mem dx dy rfl
  · have dy7 : H.degree y = 7 := by omega
    by_cases small : H.codegree x y ≤ 2
    · have mem : (⟨6,7,H.codegree x y,10,11⟩ : PairCase) ∈ cases := by
        interval_cases h : H.codegree x y <;> decide
      exact propertyB_of_case H cover edges34 x y ne _ mem dx dy7 rfl
    · have mem : (⟨7,6,H.codegree x y,1,11⟩ : PairCase) ∈ cases := by
        have : 3 ≤ H.codegree x y := by omega
        interval_cases h : H.codegree x y <;> decide
      exact propertyB_of_case H cover edges34 y x (Ne.symm ne) _ mem dy7 dx
        (H.codegree_comm y x)

theorem propertyB_of_min_six (minimum : ∀ z, 6 ≤ H.degree z)
    (x : Fin 20) (dx : H.degree x = 6) : PropertyB H := by
  by_cases pair : ∃ y, y ≠ x ∧ H.degree y ≤ 7
  · obtain ⟨y,yx,dy⟩ := pair
    exact propertyB_of_six_pair H cover edges34 x y (Ne.symm yx) dx (minimum y) dy
  have others (z : Fin 20) (zx : z ≠ x) : 8 ≤ H.degree z := by
    have hn : ¬ H.degree z ≤ 7 := fun h => pair ⟨z,zx,h⟩
    omega
  have good := H.goodPartners_budget cover x
  simp only [Fintype.card_fin,dx] at good
  have partner : ∃ y ∈ H.goodPartners x, H.degree y ≤ 8 := by
    by_contra hn
    have high (y : Fin 20) (hy : y ∈ H.goodPartners x) : 9 ≤ H.degree y := by
      have h : ¬ H.degree y ≤ 8 := fun he => hn ⟨y,hy,he⟩
      omega
    have each (z : Fin 20) :
        8 + (if z ∈ H.goodPartners x then 1 else 0) ≤ H.degree z + (if z=x then 2 else 0) := by
      by_cases zx : z=x
      · subst z
        have absent : x ∉ H.goodPartners x := by
          intro hx
          exact ((H.mem_goodPartners cover x x).mp hx).1 rfl
        simp [absent,dx]
      · have lo := others z zx
        by_cases member : z ∈ H.goodPartners x
        · have hi := high z member
          simp only [member,if_true,zx,if_false,add_zero]
          exact hi
        · simp only [member,if_false,zx,add_zero]
          exact lo
    have sum := Finset.sum_le_sum (s := Finset.univ) (fun z _ => each z)
    have budget : 160 + (H.goodPartners x).card ≤ 172 := by
      simpa [Finset.sum_add_distrib,H.sum_degrees,edges34] using sum
    omega
  obtain ⟨y,hy,dy⟩ := partner
  obtain ⟨yx,codeg⟩ := (H.mem_goodPartners cover x y).mp hy
  have dy8 : H.degree y = 8 := by have := others y yx; omega
  exact propertyB_of_case H cover edges34 x y (Ne.symm yx) ⟨6,8,1,10,11⟩
    (by decide) dx dy8 codeg

/-- Complete original-coloring conclusion whenever a 20-vertex input has a
vertex of degree at most six. All selection and numeric premises are internal. -/
theorem propertyB_of_low_degree (small : ∃ x, H.degree x ≤ 6) : PropertyB H := by
  by_cases five : ∃ x, H.degree x = 5
  · obtain ⟨x,dx⟩ := five
    exact propertyB_of_degree_five H cover edges34 x dx
  have minimum (z : Fin 20) : 6 ≤ H.degree z := by
    have lo := H.pairCovering_degree_bound cover z
    simp only [Fintype.card_fin] at lo
    have ne : H.degree z ≠ 5 := fun h => five ⟨z,h⟩
    omega
  obtain ⟨x,dx⟩ := small
  exact propertyB_of_min_six H cover edges34 minimum x (by have := minimum x; omega)

end Aris4Math.ThirtyFour.TwentyLow
#print axioms Aris4Math.ThirtyFour.TwentyLow.propertyB_of_low_degree
