import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_24 : ∀ (b : Fin 78),
    (¬∃ p, controller 24 p = b) →
    routeController 24 (wordP0 (controllerWord 24 b)) (wordP1 (controllerWord 24 b)) (wordP2 (controllerWord 24 b)) = b := by decide +kernel
theorem nb_basis_row_24 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 24 p = b) →
    routeVec 24 (wordP0 (controllerWord 24 b)) (wordP1 (controllerWord 24 b)) (wordP2 (controllerWord 24 b))
      (nbNoise 24 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_24
end DegreeDiameter.Portfolio.F9Graph56862
