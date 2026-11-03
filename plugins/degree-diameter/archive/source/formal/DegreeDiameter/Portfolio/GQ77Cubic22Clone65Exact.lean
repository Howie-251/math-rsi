import DegreeDiameter.Portfolio.OppositeGQ77SpreadExact
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65Inputs
namespace DegreeDiameter.Portfolio.GQ77Cubic22Clone65
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

/-- The accepted source's actual WalkD3 and two distinct old vertices imply
it has no isolated vertex; no regularity premise is required. -/
theorem source_no_isolated (v : Source.Vertex) : ∃ w, OppositeGQ77Spread.graph.Adj v w := by
  have ht : ∃ t : Source.Vertex, v ≠ t := by
    by_cases h0 : v = .inl (0 : OppositeGQ77Spread.Old)
    · refine ⟨.inl (1 : OppositeGQ77Spread.Old),?_⟩
      rw [h0]
      decide
    · exact ⟨.inl (0 : OppositeGQ77Spread.Old),h0⟩
  obtain ⟨t,ht⟩ := ht
  obtain ⟨p,_⟩ := OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.1 v t
  obtain ⟨w,hw,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne ht p
  exact ⟨w,hw⟩

theorem old_walk_bound_iff (u v : Source.Vertex) (n : Nat) :
    (∃ p : graph.Walk (.inl u) (.inl v), p.length ≤ n) ↔
      ∃ p : OppositeGQ77Spread.graph.Walk u v, p.length ≤ n :=
  FullNeighborhoodClones.old_walk_bound_iff OppositeGQ77Spread.graph center u v n

theorem degree_le_sixty_five : ∀ v, graph.degree v ≤ 65 :=
  FullNeighborhoodClones.degree_le OppositeGQ77Spread.graph center 64 1
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.1 load_le_one

theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  FullNeighborhoodClones.diameterAtMost OppositeGQ77Spread.graph center 3 (by decide)
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.1 source_no_isolated

theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  FullNeighborhoodClones.not_diameterAtMost OppositeGQ77Spread.graph center 2
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.2

theorem concrete_order_degree_and_exact_D3 :
    Fintype.card Vertex = 161150 ∧ (∀ v, graph.degree v ≤ 65) ∧
      DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le_sixty_five,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := concrete_order_degree_and_exact_D3
#print axioms source_no_isolated
#print axioms old_walk_bound_iff
#print axioms concrete_order_degree_and_exact_D3
#print axioms final_claim
end DegreeDiameter.Portfolio.GQ77Cubic22Clone65
