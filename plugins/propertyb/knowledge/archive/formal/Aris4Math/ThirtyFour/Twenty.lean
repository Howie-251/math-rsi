import Aris4Math.ThirtyFour.TwentyLowComplete
import Aris4Math.ThirtyFour.TwentySevenMany
import Aris4Math.ThirtyFour.TwentySevenTwo
import Aris4Math.ThirtyFour.TwentySevenOne
import Aris4Math.ThirtyFour.TwentyEight

namespace Aris4Math.ThirtyFour

theorem twenty_propertyB (H : Simple5Hypergraph (Fin 20))
    (cover : H.PairCovering) (size : H.edges.card=34) : PropertyB H := by
  classical
  by_cases low : ∃ x, H.degree x ≤ 6
  · exact TwentyLow.propertyB_of_low_degree H cover size low
  have minSeven (x : Fin 20) : 7 ≤ H.degree x := by
    have hn : ¬ H.degree x ≤ 6 := fun h => low ⟨x,h⟩
    omega
  by_cases many : 3 ≤ (TwentySevenMany.sevens H).card
  · exact TwentySevenMany.propertyB_of_many_sevens H cover size minSeven many
  by_cases two : (TwentySevenMany.sevens H).card=2
  · exact TwentySevenTwo.propertyB_of_two_sevens H cover size minSeven two
  by_cases positive : 1 ≤ (TwentySevenMany.sevens H).card
  · exact TwentySevenOne.propertyB_of_one_seven H cover size minSeven (by omega)
  have minEight (x : Fin 20) : 8 ≤ H.degree x := by
    have absent : x ∉ TwentySevenMany.sevens H := by
      intro hx
      have := Finset.one_le_card.mpr ⟨x,hx⟩
      omega
    have ne : H.degree x ≠ 7 := fun h => absent ((TwentySevenMany.mem_sevens H x).mpr h)
    have := minSeven x
    omega
  exact TwentyEight.propertyB_of_minimum_eight H cover size minEight
end Aris4Math.ThirtyFour
#print axioms Aris4Math.ThirtyFour.twenty_propertyB
