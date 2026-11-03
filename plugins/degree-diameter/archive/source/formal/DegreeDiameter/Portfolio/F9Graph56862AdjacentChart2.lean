import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart2Block0
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart2Block1
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart2Block2
namespace DegreeDiameter.Portfolio.F9Graph56862
theorem adjacent_chart_2 : ∀ d : Fin 729, planeNoise 2 d = decodeVec d := by
  intro d
  obtain ⟨⟨b,j⟩,rfl⟩ := (finProdFinEquiv (m:=3) (n:=243)).surjective d
  fin_cases b
  · exact adjacent_chart_2_block_0 j
  · exact adjacent_chart_2_block_1 j
  · exact adjacent_chart_2_block_2 j
end DegreeDiameter.Portfolio.F9Graph56862
