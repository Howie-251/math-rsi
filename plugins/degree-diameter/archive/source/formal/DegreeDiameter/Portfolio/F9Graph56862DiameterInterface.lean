import DegreeDiameter.Portfolio.F9Graph56862DecoderInterface
namespace DegreeDiameter.Portfolio.F9Graph56862
theorem diameter_of_local_decoders
  (hc : ∀ (a b : Fin 78), (¬∃ p, controller a p = b) → routeController a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) = b)
  (hn : ∀ (a b : Fin 78), (¬∃ p, controller a p = b) → ∀ d, routeVec a (wordP0 (controllerWord a b)) (wordP1 (controllerWord a b)) (wordP2 (controllerWord a b)) (nbNoise a b d) 0 = d)
  (ha : ∀ (a : Fin 78) (p : Fin 6) (d : Fin 729), routeVec a (adjP0 a p d) (adjP1 a p d) (adjP2 a p d) (adjNoise a p d) 0 = decodeVec d) : DiameterAtMost graph 3 := by
  intro u v
  by_cases h : ∃ p, controller (controllerOf u) p = controllerOf v
  · obtain ⟨p,hp⟩ := h
    let d := encodeVec (decodeVec (fiberOf v) - stepVec (controllerOf u) p 0 (decodeVec (fiberOf u)))
    refine bounded_walk_of_route u v (adjP0 (controllerOf u) p d) (adjP1 (controllerOf u) p d)
      (adjP2 (controllerOf u) p d) (adjNoise (controllerOf u) p d) ?_ ?_
    · exact (adjacent_controller (controllerOf u) p d).trans hp
    · rw [route_affine, ha, adjacent_center]
      simp only [d,decodeVec_encodeVec]
      abel
  · let w := controllerWord (controllerOf u) (controllerOf v)
    let center := routeVec (controllerOf u) (wordP0 w) (wordP1 w) (wordP2 w) 0 (decodeVec (fiberOf u))
    let d := decodeVec (fiberOf v) - center
    refine bounded_walk_of_route u v (wordP0 w) (wordP1 w) (wordP2 w)
      (nbNoise (controllerOf u) (controllerOf v) d) (hc _ _ h) ?_
    rw [route_affine, hn _ _ h]
    change center + (decodeVec (fiberOf v)-center) = decodeVec (fiberOf v)
    abel


#print axioms diameter_of_local_decoders
end DegreeDiameter.Portfolio.F9Graph56862
