import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_7 : ∀ (b : Fin 78),
    (¬∃ p, controller 7 p = b) →
    routeController 7 (wordP0 (controllerWord 7 b)) (wordP1 (controllerWord 7 b)) (wordP2 (controllerWord 7 b)) = b := by decide +kernel
theorem nb_basis_row_7 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 7 p = b) →
    routeVec 7 (wordP0 (controllerWord 7 b)) (wordP1 (controllerWord 7 b)) (wordP2 (controllerWord 7 b))
      (nbNoise 7 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_7
end DegreeDiameter.Portfolio.F9Graph56862
