import DegreeDiameter.Portfolio.F5Graph3750ControllerCertificate
import DegreeDiameter.Portfolio.F5Graph3750NBDecoderCertificate
import DegreeDiameter.Portfolio.F5Graph3750AdjacentCertificate

namespace DegreeDiameter.Portfolio.F5Graph3750

/-- Concrete all-pairs three-step walks, from local finite decoders and controller words. -/
theorem diameterAtMost_three : DiameterAtMost graph 3 := by
  intro u v
  by_cases h : ∃ p, controller (controllerOf u) p = controllerOf v
  · obtain ⟨p, hp⟩ := h
    let d := subFiber (fiberOf v) (fiberStep p 0 (fiberOf u))
    refine bounded_walk_of_route u v (adjP0 p d) (adjP1 p d) (adjP2 p d) (adjNoise p d) ?_ ?_
    · exact (adjacent_controller (controllerOf u) p d).trans hp
    · rw [route_affine, adjacent_decoder_valid, adjacent_center]
      exact add_sub_cancel (fiberStep p 0 (fiberOf u)) (fiberOf v)
  · let w := controllerWord (controllerOf u) (controllerOf v)
    have hw := controllerWord_valid (controllerOf u) (controllerOf v) h
    let d := subFiber (fiberOf v)
      (routeFiber (wordP0 w) (wordP1 w) (wordP2 w) 0 (fiberOf u))
    refine bounded_walk_of_route u v (wordP0 w) (wordP1 w) (wordP2 w)
      (nbNoiseDecoder w d) hw.2 ?_
    rw [route_affine, nb_decoder_valid w d hw.1]
    exact add_sub_cancel _ _

#print axioms diameterAtMost_three
end DegreeDiameter.Portfolio.F5Graph3750
