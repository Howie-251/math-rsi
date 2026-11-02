import DegreeDiameter.Portfolio.Q4DiagonalFillInputs
import DegreeDiameter.Portfolio.DiagonalFillReallocationDegree
import DegreeDiameter.Portfolio.DiagonalFillReallocationLower
namespace DegreeDiameter.Portfolio.Q4DiagonalFill
theorem degree_le : ∀v,graph.degree v≤26 :=
  DiagonalFillReallocation.degree_le raw Source.graph center 25 compat
    OppositeGQ44Spread.concrete_order_degree_and_exact_D3.2.1 load_le_one (by decide)
theorem diameterAtMost_three : DiameterAtMost graph 3 :=
  DiagonalFillReallocation.diameter_three raw Source.graph center compat
    OppositeGQ44Spread.concrete_order_degree_and_exact_D3.2.2.1 raw_D3 raw_no_isolated filler_route flag_route
theorem not_diameterAtMost_two : ¬DiameterAtMost graph 2 :=
  DiagonalFillReallocation.not_diameterAtMost_two raw Source.graph center (0,0)
theorem d26_7532 : Fintype.card Vertex=7532 ∧
    (∀v,graph.degree v≤26) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  ⟨card_vertex,degree_le,diameterAtMost_three,not_diameterAtMost_two⟩
theorem final_claim : FinalClaim := d26_7532
#print axioms final_claim
end DegreeDiameter.Portfolio.Q4DiagonalFill
