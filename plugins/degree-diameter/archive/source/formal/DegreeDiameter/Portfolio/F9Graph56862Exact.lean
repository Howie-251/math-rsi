import DegreeDiameter.Portfolio.F9Graph56862Diameter
import DegreeDiameter.Portfolio.F9Graph56862Lower
import DegreeDiameter.Portfolio.F9Graph56862Degree
namespace DegreeDiameter.Portfolio.F9Graph56862
def FinalClaim : Prop := Fintype.card (Fin 56862) = 56862 ∧
  (∀ v, graph.degree v ≤ 54) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
theorem concrete_order_degree_and_exact_D3 :
    Fintype.card (Fin 56862) = 56862 ∧ (∀ v, graph.degree v ≤ 54) ∧
      DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨Fintype.card_fin _,degree_le_fifty_four,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := concrete_order_degree_and_exact_D3
theorem concrete_regular_and_exact_D3 :
    Fintype.card (Fin 56862) = 56862 ∧ (∀ v, graph.degree v = 54) ∧
      DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨Fintype.card_fin _,degree_fifty_four,diameterAtMost_three,not_diameterAtMost_two⟩
#print axioms concrete_order_degree_and_exact_D3
#print axioms final_claim
#print axioms concrete_regular_and_exact_D3
end DegreeDiameter.Portfolio.F9Graph56862
