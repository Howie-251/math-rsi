import DegreeDiameter.Portfolio.F4Graph3840Diameter
import DegreeDiameter.Portfolio.F4Graph3840Lower

namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 10000
set_option maxHeartbeats 20000000

theorem concrete_order_degree_and_D3 :
    Fintype.card (Fin 3840) = 3840 ∧
      (∀ u, graph.degree u ≤ 20) ∧ DiameterAtMost graph 3 := by
  exact ⟨Fintype.card_fin _, degree_le_twenty, diameterAtMost_three⟩

theorem diameter_exact_three_in_project_definition :
    DiameterAtMost graph 3 ∧ ¬ DiameterAtMost graph 2 :=
  ⟨diameterAtMost_three, not_diameterAtMost_two⟩

#print axioms concrete_order_degree_and_D3
#print axioms diameter_exact_three_in_project_definition
end DegreeDiameter.Portfolio.F4Graph3840
