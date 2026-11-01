import Aris4Math.ThirtyThree.TwentyThreeHighComplete
import Aris4Math.ThirtyThree.TwentyThreeLowBadHighComplete
import Aris4Math.ThirtyThree.TwentyThreeLowUnitComplete
import Aris4Math.ThirtyThree.TwentyThreeTwoLowComplete
import Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete
import Aris4Math.ThirtyThree.TwentyThreeFourLowComplete

/-! Complete actual 23-point branch, partitioned by the number of degree-six vertices. -/
namespace Aris4Math.ThirtyThree
namespace TwentyThreeComplete

/-- The unique degree-six vertex either has a nonunit degree-seven partner,
or has unit codegree with all degree-seven vertices. -/
theorem propertyB_of_one_six (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (count1 : H.sixVertices.card = 1) : PropertyB H := by
  obtain ⟨x,hx⟩ := Finset.card_pos.mp (show 0 < H.sixVertices.card by omega)
  have dx : H.degree x = 6 := by simpa [Simple5Hypergraph.sixVertices] using hx
  by_cases bad : ∃ y, H.degree y = 7 ∧ 2 ≤ H.codegree x y
  · obtain ⟨y,dy,hxy⟩ := bad
    exact TwentyThreeLowBadHighComplete.propertyB_of_low_bad_high H cover edges33
      count1 x y dx dy hxy
  · have unit (y : Fin 23) (dy : H.degree y = 7) : H.codegree x y = 1 := by
      have xy : x ≠ y := by
        intro h
        rw [h] at dx
        omega
      have lower := H.one_le_codegree cover xy
      have upper : H.codegree x y < 2 := by
        by_contra hn
        exact bad ⟨y,dy,by omega⟩
      omega
    exact TwentyThreeLowUnitComplete.propertyB_of_low_unit H cover edges33 count1 x dx unit

end TwentyThreeComplete

/-- Every pair-covering simple five-uniform hypergraph on 23 vertices with
exactly 33 edges has an actual Property B coloring. -/
theorem twenty_three_propertyB (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) : PropertyB H := by
  rcases TwentyThreeSelection.degree_count_cases H cover edges33 (Fintype.card_fin 23) with
    four | ⟨three,_⟩ | ⟨two,_⟩ | ⟨one,_⟩ | ⟨zero,_⟩
  · exact TwentyThreeFourLowComplete.propertyB_of_four_sixes H cover edges33 four
  · exact TwentyThreeThreeLowComplete.propertyB_of_three_sixes H cover edges33 three
  · exact TwentyThreeTwoLowComplete.propertyB_of_two_sixes H cover edges33 two
  · exact TwentyThreeComplete.propertyB_of_one_six H cover edges33 one
  · exact TwentyThreeHighComplete.propertyB_of_no_sixes H cover edges33 zero

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.TwentyThreeComplete.propertyB_of_one_six
#print axioms Aris4Math.ThirtyThree.twenty_three_propertyB
