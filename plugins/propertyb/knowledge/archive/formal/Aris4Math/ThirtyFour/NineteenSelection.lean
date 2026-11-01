import Aris4Math.ThirtyThree.TwentyOneStructure

/-! Selection on actual 19-vertex, 34-edge pair-covering hypergraphs. -/
namespace Aris4Math.ThirtyFour.NineteenSelection
open scoped BigOperators

variable (H : Simple5Hypergraph (Fin 19))

def PairCase (x y : Fin 19) : Prop :=
  H.degree x = 8 ∧
    ((9 ≤ H.degree y ∧ H.degree y ≤ 10 ∧ H.codegree x y = 1) ∨
      (H.degree y = 8 ∧ 3 ≤ H.codegree x y))

def TripleCase (x y z : Fin 19) : Prop :=
  H.degree x = 8 ∧ H.degree y = 8 ∧ H.degree z = 8 ∧
    H.codegree x y ≤ 2 ∧ H.codegree x z ≤ 2 ∧ H.codegree y z ≤ 2

def Selected : Prop :=
  (∃ x, 5 ≤ H.degree x ∧ H.degree x ≤ 7) ∨
  (∃ x y, x ≠ y ∧ PairCase H x y) ∨
  (∃ x y z, x ≠ y ∧ x ≠ z ∧ y ≠ z ∧ TripleCase H x y z)

theorem exists_selected (cover : H.PairCovering) (edges34 : H.edges.card = 34) : Selected H := by
  classical
  by_cases small : ∃ x, 5 ≤ H.degree x ∧ H.degree x ≤ 7
  · exact Or.inl small
  have minimum (x : Fin 19) : 8 ≤ H.degree x := by
    have lower := H.pairCovering_degree_bound cover x
    simp only [Fintype.card_fin] at lower
    have hn : ¬ (5 ≤ H.degree x ∧ H.degree x ≤ 7) := fun h => small ⟨x,h⟩
    omega
  let S := Finset.univ.filter fun x => H.degree x = 8
  have existsEight : S.Nonempty := by
    by_contra hn
    have lower (x : Fin 19) : 9 ≤ H.degree x := by
      have hm := minimum x
      have hx : H.degree x ≠ 8 := by
        intro he
        exact hn ⟨x,Finset.mem_filter.mpr ⟨Finset.mem_univ x,he⟩⟩
      omega
    have budget := H.subset_degree_budget Finset.univ 9 0 lower
      (fun x _ => by simpa using lower x)
    simp [edges34] at budget
  by_cases few : S.card ≤ 2
  · obtain ⟨x,hx⟩ := existsEight
    have dx : H.degree x = 8 := (Finset.mem_filter.mp hx).2
    have good := H.goodPartners_budget cover x
    simp only [Fintype.card_fin,dx] at good
    have hdifference := Finset.card_le_card_sdiff_add_card (s := H.goodPartners x) (t := S)
    obtain ⟨y,hy⟩ := Finset.card_pos.mp
      (show 0 < (H.goodPartners x \ S).card by omega)
    obtain ⟨hgood,houtside⟩ := Finset.mem_sdiff.mp hy
    obtain ⟨yx,codeg⟩ := (H.mem_goodPartners cover x y).mp hgood
    have dyLower : 9 ≤ H.degree y := by
      have hm := minimum y
      have hy8 : H.degree y ≠ 8 := by
        intro h; exact houtside (Finset.mem_filter.mpr ⟨Finset.mem_univ y,h⟩)
      omega
    have each (z : Fin 19) : 9 ≤ H.degree z + if z ∈ S then 1 else 0 := by
      have hm := minimum z
      by_cases hz : z ∈ S
      · simp only [hz,if_true]; omega
      · have hn : H.degree z ≠ 8 := by
          intro h; exact hz (Finset.mem_filter.mpr ⟨Finset.mem_univ z,h⟩)
        simp only [hz,if_false]; omega
    have hl := Finset.sum_le_sum (s := Finset.univ.erase y) (fun z _ => each z)
    have hs := Finset.sum_erase_add (s := Finset.univ)
      (fun z => H.degree z + if z ∈ S then 1 else 0) (Finset.mem_univ y)
    have sum : (∑ z : Fin 19, (H.degree z + if z ∈ S then 1 else 0)) = 170 + S.card := by
      simp [Finset.sum_add_distrib,H.sum_degrees,edges34]
    rw [sum] at hs
    simp only [houtside,if_false,add_zero] at hs
    norm_num at hl
    have dyUpper : H.degree y ≤ 10 := by omega
    exact Or.inr (Or.inl ⟨x,y,Ne.symm yx,dx,Or.inl ⟨dyLower,dyUpper,codeg⟩⟩)
  have many : 3 ≤ S.card := by omega
  by_cases pair : ∃ x ∈ S, ∃ y ∈ S, x ≠ y ∧ 3 ≤ H.codegree x y
  · obtain ⟨x,hx,y,hy,ne,hc⟩ := pair
    exact Or.inr (Or.inl ⟨x,y,ne,(Finset.mem_filter.mp hx).2,
      Or.inr ⟨(Finset.mem_filter.mp hy).2,hc⟩⟩)
  have low (x : Fin 19) (hx : x ∈ S) (y : Fin 19) (hy : y ∈ S) (ne : x ≠ y) :
      H.codegree x y ≤ 2 := by
    have hn : ¬ 3 ≤ H.codegree x y := fun h => pair ⟨x,hx,y,hy,ne,h⟩
    omega
  obtain ⟨x,hx⟩ := existsEight
  have size1 : 2 ≤ (S.erase x).card := by rw [Finset.card_erase_of_mem hx]; omega
  obtain ⟨y,hy⟩ := Finset.card_pos.mp (show 0 < (S.erase x).card by omega)
  obtain ⟨yx,hyS⟩ := Finset.mem_erase.mp hy
  have size2 : 1 ≤ ((S.erase x).erase y).card := by
    rw [Finset.card_erase_of_mem hy]; omega
  obtain ⟨z,hz⟩ := Finset.card_pos.mp (by omega : 0 < ((S.erase x).erase y).card)
  obtain ⟨zy,hz1⟩ := Finset.mem_erase.mp hz
  obtain ⟨zx,hzS⟩ := Finset.mem_erase.mp hz1
  exact Or.inr (Or.inr ⟨x,y,z,Ne.symm yx,Ne.symm zx,Ne.symm zy,
    (Finset.mem_filter.mp hx).2,(Finset.mem_filter.mp hyS).2,(Finset.mem_filter.mp hzS).2,
    low x hx y hyS (Ne.symm yx),low x hx z hzS (Ne.symm zx),low y hyS z hzS (Ne.symm zy)⟩)

end Aris4Math.ThirtyFour.NineteenSelection
#print axioms Aris4Math.ThirtyFour.NineteenSelection.exists_selected
