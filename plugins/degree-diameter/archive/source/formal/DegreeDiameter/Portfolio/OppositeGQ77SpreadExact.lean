import DegreeDiameter.Portfolio.OppositeGQ77SpreadInputs
namespace DegreeDiameter.Portfolio.OppositeGQ77Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

/-- All finite hypotheses of the generic family are supplied by the fixed literal inputs. -/
theorem concrete_order_degree_and_exact_D3 :
    Fintype.card Vertex = 160050 ∧ (∀ v, graph.degree v ≤ 64) ∧
      DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 := by
  have h := OppositeIncidenceSpread.order_degree_and_exact_D3 oldEquiv linePoint pointLine spread spreadOwner
    (by decide) pointLine_covers spread_unique projection (by decide)
  simpa only [Fintype.card_fin] using h
theorem final_claim : FinalClaim := concrete_order_degree_and_exact_D3
#print axioms concrete_order_degree_and_exact_D3
#print axioms final_claim
end DegreeDiameter.Portfolio.OppositeGQ77Spread
