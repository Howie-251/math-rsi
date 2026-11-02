import DegreeDiameter.Portfolio.EvenQ8SourceFullExact
import DegreeDiameter.Portfolio.Q8DiagonalFillInputs
import DegreeDiameter.Portfolio.DiagonalFillReallocationDegree
import DegreeDiameter.Portfolio.DiagonalFillReallocationLower
namespace DegreeDiameter.Portfolio.Q8DiagonalFill
theorem degree_le : ∀v,graph.degree v≤82 :=
  DiagonalFillReallocation.degree_le raw Source.graph center 81 compat
    EvenQ8SourceFull.D81_342290.final_claim.2.1 load_le_one (by decide)
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  DiagonalFillReallocation.diameter_three raw Source.graph center compat
    EvenQ8SourceFull.D81_342290.final_claim.2.2.1 raw_D3 raw_no_isolated filler_route flag_route
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  DiagonalFillReallocation.not_diameterAtMost_two raw Source.graph center (0,0)
theorem d82_346516 : Fintype.card Vertex=346516 ∧
    (∀v,graph.degree v≤82) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d82_346516
#print axioms final_claim
end DegreeDiameter.Portfolio.Q8DiagonalFill
