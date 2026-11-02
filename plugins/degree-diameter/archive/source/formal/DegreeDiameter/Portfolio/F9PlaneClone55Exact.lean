import DegreeDiameter.Portfolio.F9PlaneClone55Inputs
import DegreeDiameter.Portfolio.F9Graph56862Exact

namespace DegreeDiameter.Portfolio.F9PlaneClone55
open F9Graph56862
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

theorem source_no_isolated (v : Fin 56862) : ∃ w, F9Graph56862.graph.Adj v w :=
  ⟨forward v 0 F.c0,forward_adj v 0 F.c0⟩

theorem old_walk_bound_iff (u v : Fin 56862) (n : Nat) :
    (∃ p : graph.Walk (.inl u) (.inl v), p.length ≤ n) ↔
      ∃ p : F9Graph56862.graph.Walk u v, p.length ≤ n :=
  FullNeighborhoodClones.old_walk_bound_iff F9Graph56862.graph center u v n

theorem degree_le_fifty_five : ∀ v, graph.degree v ≤ 55 :=
  FullNeighborhoodClones.degree_le F9Graph56862.graph center 54 1
    degree_le_fifty_four load_le_one

theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  FullNeighborhoodClones.diameterAtMost F9Graph56862.graph center 3 (by decide)
    F9Graph56862.concrete_order_degree_and_exact_D3.2.2.1 source_no_isolated

theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  FullNeighborhoodClones.not_diameterAtMost F9Graph56862.graph center 2
    F9Graph56862.concrete_order_degree_and_exact_D3.2.2.2

theorem concrete_order_degree_and_exact_D3 :
    Fintype.card Vertex = 56943 ∧ (∀ v, graph.degree v ≤ 55) ∧
      DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le_fifty_five,diameterAtMost_three,not_diameterAtMost_two⟩

theorem final_claim : FinalClaim := concrete_order_degree_and_exact_D3

#print axioms load_le_one
#print axioms concrete_order_degree_and_exact_D3
#print axioms final_claim
end DegreeDiameter.Portfolio.F9PlaneClone55
