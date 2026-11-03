import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart0
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart1
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart2
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart3
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart4
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart5
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart6
import DegreeDiameter.Portfolio.F9Graph56862AdjacentChart7
import DegreeDiameter.Portfolio.F9Graph56862DecoderInterface
namespace DegreeDiameter.Portfolio.F9Graph56862
theorem adjacent_planes : ∀ (c : Fin 8) (d : Fin 729), planeNoise c d = decodeVec d := by
  intro c
  fin_cases c
  · exact adjacent_chart_0
  · exact adjacent_chart_1
  · exact adjacent_chart_2
  · exact adjacent_chart_3
  · exact adjacent_chart_4
  · exact adjacent_chart_5
  · exact adjacent_chart_6
  · exact adjacent_chart_7
theorem adjacent_valid (a : Fin 78) (p : Fin 6) (d : Fin 729) :
    routeVec a (adjP0 a p d) (adjP1 a p d) (adjP2 a p d) (adjNoise a p d) 0 = decodeVec d := by
  have hc := adjacent_planes (chart a p) d
  by_cases h : adjBefore a p d
  · have hchart : chartBefore (chart a p) d := h
    simp only [adjP0,adjP1,adjP2,adjNoise,if_pos h,before_noise]
    simpa only [planeNoise,if_pos hchart,matrix,adjQ,chart_target_valid] using hc
  · have hchart : ¬chartBefore (chart a p) d := h
    simp only [adjP0,adjP1,adjP2,adjNoise,if_neg h,after_noise]
    simpa only [planeNoise,if_neg hchart,adjQ,chart_target_valid] using hc
#print axioms adjacent_valid
end DegreeDiameter.Portfolio.F9Graph56862
