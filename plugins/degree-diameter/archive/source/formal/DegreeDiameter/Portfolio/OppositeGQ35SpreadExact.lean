import DegreeDiameter.Portfolio.OppositeGQ35SpreadLower
import DegreeDiameter.Portfolio.OppositeGQ35SpreadDiameter
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- The concrete6160 graph: no projection, incidence or capacity assumption. -/
theorem concrete_order_degree_and_exact_D3 :
    Fintype.card Vertex = 6160 ∧ (∀ v, graph.degree v ≤ 24) ∧
      DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le_twentyfour,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := concrete_order_degree_and_exact_D3
#print axioms concrete_order_degree_and_exact_D3
#print axioms final_claim
end DegreeDiameter.Portfolio.OppositeGQ35Spread
