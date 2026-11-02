import DegreeDiameter.Portfolio.GQ77Cubic22Clone70Inputs
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65Exact
namespace DegreeDiameter.Portfolio.GQ77Cubic22Clone70
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
theorem source_no_isolated (v : Source.Vertex) : ∃ w, OppositeGQ77Spread.graph.Adj v w :=
  GQ77Cubic22Clone65.source_no_isolated v
theorem old_walk_bound_iff (u v : Source.Vertex) (n : Nat) :
    (∃ p : graph.Walk (.inl u) (.inl v), p.length ≤ n) ↔
      ∃ p : OppositeGQ77Spread.graph.Walk u v, p.length ≤ n :=
  FullNeighborhoodClones.old_walk_bound_iff OppositeGQ77Spread.graph center u v n
theorem degree_le_seventy : ∀ v, graph.degree v ≤ 70 :=
  FullNeighborhoodClones.degree_le OppositeGQ77Spread.graph center 64 6
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.1 load_le_six
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  FullNeighborhoodClones.diameterAtMost OppositeGQ77Spread.graph center 3 (by decide)
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.1 source_no_isolated
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  FullNeighborhoodClones.not_diameterAtMost OppositeGQ77Spread.graph center 2
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.2
theorem concrete_order_degree_and_exact_D3 :
    Fintype.card Vertex = 166650 ∧ (∀ v, graph.degree v ≤ 70) ∧
      DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le_seventy,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := concrete_order_degree_and_exact_D3
#print axioms source_no_isolated
#print axioms old_walk_bound_iff
#print axioms concrete_order_degree_and_exact_D3
#print axioms final_claim
end DegreeDiameter.Portfolio.GQ77Cubic22Clone70
