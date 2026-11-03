import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_62 : ∀ (b : Fin 78),
    (¬∃ p, controller 62 p = b) →
    routeController 62 (wordP0 (controllerWord 62 b)) (wordP1 (controllerWord 62 b)) (wordP2 (controllerWord 62 b)) = b := by decide +kernel
theorem nb_basis_row_62 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 62 p = b) →
    routeVec 62 (wordP0 (controllerWord 62 b)) (wordP1 (controllerWord 62 b)) (wordP2 (controllerWord 62 b))
      (nbNoise 62 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_62
end DegreeDiameter.Portfolio.F9Graph56862
