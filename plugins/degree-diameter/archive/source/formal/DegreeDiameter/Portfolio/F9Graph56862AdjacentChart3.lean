import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart3Block0
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart3Block1
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart3Block2
namespace DegreeDiameter.Portfolio.F9Graph56862
theorem adjacent_chart_3 : ∀ d : Fin 729, planeNoise 3 d = decodeVec d := by
  intro d
  obtain ⟨⟨b,j⟩,rfl⟩ := (finProdFinEquiv (m:=3) (n:=243)).surjective d
  fin_cases b
  · exact adjacent_chart_3_block_0 j
  · exact adjacent_chart_3_block_1 j
  · exact adjacent_chart_3_block_2 j
end DegreeDiameter.Portfolio.F9Graph56862
