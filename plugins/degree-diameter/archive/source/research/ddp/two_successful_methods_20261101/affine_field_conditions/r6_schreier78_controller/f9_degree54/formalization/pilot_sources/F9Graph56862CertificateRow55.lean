import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_55 : ∀ (b : Fin 78),
    (¬∃ p, controller 55 p = b) →
    routeController 55 (wordP0 (controllerWord 55 b)) (wordP1 (controllerWord 55 b)) (wordP2 (controllerWord 55 b)) = b := by decide +kernel
theorem nb_basis_row_55 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 55 p = b) →
    routeVec 55 (wordP0 (controllerWord 55 b)) (wordP1 (controllerWord 55 b)) (wordP2 (controllerWord 55 b))
      (nbNoise 55 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_55
end DegreeDiameter.Portfolio.F9Graph56862
