import Aris4Math.ThirtyFour.TwentyFourMatchingSelection

namespace Aris4Math.ThirtyFour.TwentyFourCommonSevens
open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyFourSelection (sevenVertices)
variable (H : Simple5Hypergraph (Fin 24))

/-- Seven-degree vertices whose codegrees with all low vertices are one. -/
def common : Finset (Fin 24) :=
  sevenVertices H \ H.sixVertices.biUnion H.badPartners

theorem excluded_card (cover : H.PairCovering) :
    (H.sixVertices.biUnion H.badPartners).card≤H.sixVertices.card := by
  calc
    _ ≤ ∑x∈H.sixVertices,(H.badPartners x).card := Finset.card_biUnion_le
    _ ≤ ∑_x∈H.sixVertices,1 := Finset.sum_le_sum (fun x hx=>
      H.badPartners_card_le_one_of_twenty_four cover (by simp) (Finset.mem_filter.mp hx).2)
    _ = _ := by simp

theorem budget (cover : H.PairCovering) (size : H.edges.card=34) :
    22≤3*H.sixVertices.card+(common H).card := by
  have a := TwentyFourMatchingSelection.six_seven_budget H cover size
  have b := excluded_card H cover
  have c := Finset.card_le_card_sdiff_add_card (s:=sevenVertices H)
    (t:=H.sixVertices.biUnion H.badPartners)
  dsimp only [common]
  omega

theorem data (cover : H.PairCovering) {q : Fin 24} (hq : q∈common H) :
    H.degree q=7 ∧ ∀x∈H.sixVertices,q≠x ∧ H.codegree x q=1 := by
  obtain ⟨high,out⟩ := Finset.mem_sdiff.mp hq
  have degree : H.degree q=7 := (Finset.mem_filter.mp high).2
  refine ⟨degree,?_⟩
  intro x hx
  have low : H.degree x=6 := (Finset.mem_filter.mp hx).2
  have qx : q≠x := by intro eq; subst q; omega
  have good : q∈H.goodPartners x := by
    apply Finset.mem_sdiff.mpr
    refine ⟨Finset.mem_univ _,?_⟩
    simp only [Finset.mem_insert,not_or]
    exact ⟨qx,fun h=>out (Finset.mem_biUnion.mpr ⟨x,hx,h⟩)⟩
  exact ⟨qx,((H.mem_goodPartners cover x q).mp good).2⟩

theorem card_ge_seven_of_five (cover : H.PairCovering) (size : H.edges.card=34)
    (five : H.sixVertices.card=5) : 7≤(common H).card := by
  have h := budget H cover size
  omega

theorem card_ge_four_of_six (cover : H.PairCovering) (size : H.edges.card=34)
    (six : H.sixVertices.card=6) : 4≤(common H).card := by
  have h := budget H cover size
  omega

/-- With exactly five lows, any common seven-degree vertex has another
common seven-degree vertex with unit codegree. -/
theorem exists_other_unit_of_five (cover : H.PairCovering) (size : H.edges.card=34)
    (five : H.sixVertices.card=5) {x : Fin 24} (hx : x∈common H) :
    ∃y∈common H,y≠x ∧ H.codegree x y=1 := by
  have many := card_ge_seven_of_five H cover size five
  have dx := (data H cover hx).1
  have bad := H.badPartners_card_le_excess cover x
  rw [dx] at bad
  norm_num at bad
  have small := Finset.card_insert_le x (H.badPartners x)
  have diff := Finset.card_le_card_sdiff_add_card (s:=common H)
    (t:=insert x (H.badPartners x))
  obtain ⟨y,hy⟩ := Finset.card_pos.mp
    (show 0<(common H\insert x (H.badPartners x)).card by omega)
  obtain ⟨inside,out⟩ := Finset.mem_sdiff.mp hy
  have good : y∈H.goodPartners x := Finset.mem_sdiff.mpr ⟨Finset.mem_univ _,out⟩
  exact ⟨y,inside,(H.mem_goodPartners cover x y).mp good⟩

end Aris4Math.ThirtyFour.TwentyFourCommonSevens
#print axioms Aris4Math.ThirtyFour.TwentyFourCommonSevens.exists_other_unit_of_five
