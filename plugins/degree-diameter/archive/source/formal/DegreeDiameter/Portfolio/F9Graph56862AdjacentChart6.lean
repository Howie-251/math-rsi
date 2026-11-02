import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart6Block0
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart6Block1
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart6Block2
namespace DegreeDiameter.Portfolio.F9Graph56862
theorem adjacent_chart_6 : ∀ d : Fin 729, planeNoise 6 d = decodeVec d := by
  intro d
  obtain ⟨⟨b,j⟩,rfl⟩ := (finProdFinEquiv (m:=3) (n:=243)).surjective d
  fin_cases b
  · exact adjacent_chart_6_block_0 j
  · exact adjacent_chart_6_block_1 j
  · exact adjacent_chart_6_block_2 j
end DegreeDiameter.Portfolio.F9Graph56862
