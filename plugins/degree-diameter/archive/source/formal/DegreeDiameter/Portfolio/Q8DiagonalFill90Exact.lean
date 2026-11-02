import DegreeDiameter.Portfolio.Q8DiagonalFill90Inputs
import DegreeDiameter.Portfolio.Q8DiagonalFill83Exact
namespace DegreeDiameter.Portfolio.Q8DiagonalFill90
theorem degree_le : ∀v,graph.degree v≤90 :=
  FullNeighborhoodClones.degree_le Source.graph center 82 8
    Q8DiagonalFill.final_claim.2.1 load_le
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  FullNeighborhoodClones.diameterAtMost Source.graph center 3 (by decide)
    Q8DiagonalFill.final_claim.2.2.1 Q8DiagonalFill83.source_no_isolated
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  FullNeighborhoodClones.not_diameterAtMost Source.graph center 2 Q8DiagonalFill.final_claim.2.2.2
theorem d90_380324 : Fintype.card Vertex=380324 ∧ (∀v,graph.degree v≤90) ∧
    DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d90_380324
theorem old_walk_bound_iff (u v : Source.Vertex) (n : Nat) :
    (∃p:graph.Walk (.inl u) (.inl v),p.length≤n) ↔
      ∃p:Source.graph.Walk u v,p.length≤n :=
  FullNeighborhoodClones.old_walk_bound_iff Source.graph center u v n
#print axioms final_claim
end DegreeDiameter.Portfolio.Q8DiagonalFill90
