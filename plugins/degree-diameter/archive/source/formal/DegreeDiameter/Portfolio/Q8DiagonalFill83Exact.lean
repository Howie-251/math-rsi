import DegreeDiameter.Portfolio.Q8DiagonalFill83Inputs
import DegreeDiameter.Portfolio.Q8DiagonalFillExact
namespace DegreeDiameter.Portfolio.Q8DiagonalFill83
theorem source_no_isolated (v : Source.Vertex) : ∃w,Source.graph.Adj v w := by
  have ht : ∃t:Source.Vertex,v≠t := by
    by_cases h0 : v=.inl (.inl (.inl (0:Source.Old)))
    · refine ⟨.inl (.inl (.inl (1:Source.Old))),?_⟩
      rw [h0]
      decide
    · exact ⟨.inl (.inl (.inl (0:Source.Old))),h0⟩
  obtain ⟨t,ht⟩ := ht
  obtain ⟨p,_⟩ := Q8DiagonalFill.final_claim.2.2.1 v t
  obtain ⟨w,hw,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne ht p
  exact ⟨w,hw⟩
theorem degree_le : ∀v,graph.degree v≤83 :=
  FullNeighborhoodClones.degree_le Source.graph center 82 1 Q8DiagonalFill.final_claim.2.1 load_le_one
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  FullNeighborhoodClones.diameterAtMost Source.graph center 3 (by decide)
    Q8DiagonalFill.final_claim.2.2.1 source_no_isolated
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  FullNeighborhoodClones.not_diameterAtMost Source.graph center 2 Q8DiagonalFill.final_claim.2.2.2
theorem d83_350742 : Fintype.card Vertex=350742 ∧ (∀v,graph.degree v≤83) ∧
    DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d83_350742
theorem old_walk_bound_iff (u v : Source.Vertex) (n : Nat) :
    (∃p:graph.Walk (.inl u) (.inl v),p.length≤n) ↔
      ∃p:Source.graph.Walk u v,p.length≤n :=
  FullNeighborhoodClones.old_walk_bound_iff Source.graph center u v n
#print axioms final_claim
end DegreeDiameter.Portfolio.Q8DiagonalFill83
