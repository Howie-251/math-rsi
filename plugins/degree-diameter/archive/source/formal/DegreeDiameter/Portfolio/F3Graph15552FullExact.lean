import DegreeDiameter.Portfolio.F3Graph15552FullRows
import DegreeDiameter.Portfolio.F3Graph15552FullLower
namespace DegreeDiameter.Portfolio.F3Graph15552
abbrev FinalClaim := SourceFinalClaim
theorem d15_15552 : Fintype.card (Fin 15552)=15552 ∧ (∀v,graph.degree v≤15) ∧
    DiameterAtMost graph 4 ∧ ¬DiameterAtMost graph 3 :=
  ⟨Fintype.card_fin _,degree_le_fifteen,diameterAtMost_four,not_diameterAtMost_three⟩
theorem final_claim : FinalClaim := d15_15552
#print axioms final_claim
end DegreeDiameter.Portfolio.F3Graph15552
