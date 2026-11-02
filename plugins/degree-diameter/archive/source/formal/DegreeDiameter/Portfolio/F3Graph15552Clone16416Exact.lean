import DegreeDiameter.Portfolio.F3Graph15552Clone16416Inputs
import DegreeDiameter.Portfolio.F3Graph15552FullExact
namespace DegreeDiameter.Portfolio.F3Graph15552.Clone16416
theorem card_vertex : Fintype.card Vertex=16416 := by
  simpa only [Fintype.card_fin] using Fintype.card_congr label
theorem degree_le : ∀v,graph.degree v≤16 :=
  FullNeighborhoodClones.degree_le F3Graph15552.graph center 15 1
    F3Graph15552.final_claim.2.1 load_le_one
theorem diameterAtMost_four : DiameterAtMost graph 4 :=
  FullNeighborhoodClones.diameterAtMost F3Graph15552.graph center 4 (by decide)
    F3Graph15552.final_claim.2.2.1 F3Graph15552.source_no_isolated
theorem not_diameterAtMost_three : ¬DiameterAtMost graph 3 :=
  FullNeighborhoodClones.not_diameterAtMost F3Graph15552.graph center 3
    F3Graph15552.final_claim.2.2.2
theorem d16_16416 : Fintype.card Vertex=16416 ∧ (∀v,graph.degree v≤16) ∧
    DiameterAtMost graph 4 ∧ ¬DiameterAtMost graph 3 :=
  ⟨card_vertex,degree_le,diameterAtMost_four,not_diameterAtMost_three⟩
theorem original_concrete_goal : Fintype.card Vertex=16416 ∧ (∀v,graph.degree v≤16) ∧
    (∀u v,∃w : graph.Walk u v,w.length≤4) ∧ ¬DiameterAtMost graph 3 := d16_16416
theorem final_claim : FinalClaim := original_concrete_goal
theorem old_walk_bound_iff (u v : Fin 15552)(n : Nat) :
    (∃w : graph.Walk (.inl u) (.inl v),w.length≤n) ↔
      ∃w : F3Graph15552.graph.Walk u v,w.length≤n :=
  FullNeighborhoodClones.old_walk_bound_iff F3Graph15552.graph center u v n
#print axioms final_claim
end DegreeDiameter.Portfolio.F3Graph15552.Clone16416
