import DegreeDiameter.Portfolio.F5Graph3750RouteData

namespace DegreeDiameter.Portfolio.F5Graph3750
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

theorem adjacent_decoder_port_0 : ∀ (d : Fin 125),
    routeFiber (adjP0 0 d) (adjP1 0 d) (adjP2 0 d) (adjNoise 0 d) 0 = d := by decide +kernel

theorem adjacent_decoder_port_1 : ∀ (d : Fin 125),
    routeFiber (adjP0 1 d) (adjP1 1 d) (adjP2 1 d) (adjNoise 1 d) 0 = d := by decide +kernel

theorem adjacent_decoder_port_2 : ∀ (d : Fin 125),
    routeFiber (adjP0 2 d) (adjP1 2 d) (adjP2 2 d) (adjNoise 2 d) 0 = d := by decide +kernel

theorem adjacent_decoder_port_3 : ∀ (d : Fin 125),
    routeFiber (adjP0 3 d) (adjP1 3 d) (adjP2 3 d) (adjNoise 3 d) 0 = d := by decide +kernel

theorem adjacent_decoder_valid : ∀ (p : Fin 4) (d : Fin 125),
    routeFiber (adjP0 p d) (adjP1 p d) (adjP2 p d) (adjNoise p d) 0 = d := by
  intro p
  fin_cases p
  · exact adjacent_decoder_port_0
  · exact adjacent_decoder_port_1
  · exact adjacent_decoder_port_2
  · exact adjacent_decoder_port_3

theorem adjacent_controller (a : Fin 30) (p : Fin 4) (d : Fin 125) :
    controller (controller (controller a (adjP0 p d)) (adjP1 p d)) (adjP2 p d) =
      controller a p := by
  by_cases h : adjBefore p d
  · simp only [adjP0, adjP1, adjP2, if_pos h, controller_reverse]
  · simp only [adjP0, adjP1, adjP2, if_neg h, controller_reverse]

theorem adjacent_center (p : Fin 4) (d x : Fin 125) :
    routeFiber (adjP0 p d) (adjP1 p d) (adjP2 p d) 0 x = fiberStep p 0 x := by
  by_cases h : adjBefore p d
  · simp only [adjP0, adjP1, adjP2, if_pos h, route_before_center]
  · simp only [adjP0, adjP1, adjP2, if_neg h, route_after_center]

#print axioms adjacent_decoder_valid
end DegreeDiameter.Portfolio.F5Graph3750
