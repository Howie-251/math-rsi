import Aris4Math.ThirtyThree.TwentyStructure
import Aris4Math.ThirtyThree.TwentyStandard
import Aris4Math.ThirtyThree.TwentyEight

/-! Complete twenty-vertex branch of T33. The lock-pair selection covers
all actual inputs; eleven standard cases and the enhanced (8,8) case prove
colorability without retaining profile or probability premises. -/

namespace Aris4Math.ThirtyThree

theorem twenty_propertyB (H : Simple5Hypergraph (Fin 20))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) : PropertyB H := by
  obtain ⟨x, y, hne, one, degrees⟩ :=
    exists_two_locks_of_twenty H cover edges33 (by simp)
  rcases degrees with ⟨dx, lo, hi⟩ | ⟨dx, lo, hi⟩ | ⟨dx, lo, hi⟩ | ⟨dx, dy⟩
  · apply TwentyStandard.propertyB_of_standard_pair H cover edges33 x y hne one
    rw [dx]
    interval_cases dy : H.degree y <;> decide
  · apply TwentyStandard.propertyB_of_standard_pair H cover edges33 x y hne one
    rw [dx]
    interval_cases dy : H.degree y <;> decide
  · apply TwentyStandard.propertyB_of_standard_pair H cover edges33 x y hne one
    rw [dx]
    interval_cases dy : H.degree y <;> decide
  · exact TwentyEight.propertyB_of_eight_eight H cover edges33 x y hne one dx dy

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.twenty_propertyB
