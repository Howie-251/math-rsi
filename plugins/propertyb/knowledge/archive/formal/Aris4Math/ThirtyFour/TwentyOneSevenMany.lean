import Aris4Math.ThirtyFour.TwentyOneSevenManyActual
import Aris4Math.ThirtyFour.TwentyOneSevenSelection

/-! Select five actual degree-seven vertices and apply the complete local
five-lock caller. No profile or selected-set premise is exposed. -/

namespace Aris4Math.ThirtyFour.TwentyOneSevenMany

theorem propertyB_of_many_sevens (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34)
    (many : 5≤(TwentyOneSevenSelection.sevens H).card) : PropertyB H := by
  classical
  obtain ⟨S,sub,card⟩ := Finset.exists_subset_card_eq many
  let e : ↥S ≃ Fin 5 := Fintype.equivFinOfCardEq (by simpa using card)
  let f : Fin 5 ↪ Fin 21 :=
    ⟨fun i => (e.symm i).val,Subtype.val_injective.comp e.symm.injective⟩
  have degrees (i : Fin 5) : H.degree (f i)=7 :=
    (Finset.mem_filter.mp (sub (e.symm i).property)).2
  exact TwentyOneSevenManyActual.propertyB_of_five_sevens H cover size f degrees

end Aris4Math.ThirtyFour.TwentyOneSevenMany

#print axioms Aris4Math.ThirtyFour.TwentyOneSevenMany.propertyB_of_many_sevens
