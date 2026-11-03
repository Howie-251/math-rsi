import DegreeDiameter.Portfolio.F4Graph1920SourceDiameter
import DegreeDiameter.Portfolio.F4Graph1920SourceLower
namespace DegreeDiameter.Portfolio.F4Graph1920
def source_label : Fin 1920 ≃ Fin 1920 := Equiv.refl _
abbrev FinalClaim := SourceFinalClaim
theorem d16_1920 : Fintype.card (Fin 1920)=1920 ∧ (∀v,graph.degree v≤16) ∧
    DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨Fintype.card_fin _,degree_le_sixteen,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d16_1920
#print axioms final_claim
end DegreeDiameter.Portfolio.F4Graph1920
