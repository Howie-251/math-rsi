import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart0Block0
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart0Block1
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart0Block2
namespace DegreeDiameter.Portfolio.F9Graph56862
theorem adjacent_chart_0 : ∀ d : Fin 729, planeNoise 0 d = decodeVec d := by
  intro d
  obtain ⟨⟨b,j⟩,rfl⟩ := (finProdFinEquiv (m:=3) (n:=243)).surjective d
  fin_cases b
  · exact adjacent_chart_0_block_0 j
  · exact adjacent_chart_0_block_1 j
  · exact adjacent_chart_0_block_2 j
end DegreeDiameter.Portfolio.F9Graph56862
