import Aris4Math.ThirtyFour.TwentyOneSevenUniqueActual
import Aris4Math.ThirtyFour.TwentyOneSevenOneSelection
namespace Aris4Math.ThirtyFour.TwentyOneSevenOne

theorem propertyB_of_one_seven (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,7≤H.degree v)
    (one : (TwentyOneSevenSelection.sevens H).card=1) : PropertyB H := by
  classical
  by_contra noB
  have nonempty : (TwentyOneSevenSelection.sevens H).Nonempty:=Finset.card_pos.mp (by omega)
  obtain ⟨x,hx⟩:=nonempty
  have dx : H.degree x=7:=(Finset.mem_filter.mp hx).2
  obtain ⟨f,ds,ps,promotions⟩:=TwentyOneSevenOneSelection.exists_last_locks H cover size minimum noB one x dx
  exact noB (TwentyOneSevenUniqueActual.propertyB_of_locks H size f ds ps promotions)
end Aris4Math.ThirtyFour.TwentyOneSevenOne
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenOne.propertyB_of_one_seven
