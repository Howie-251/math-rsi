import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_14 : ∀ (b : Fin 78),
    (¬∃ p, controller 14 p = b) →
    routeController 14 (wordP0 (controllerWord 14 b)) (wordP1 (controllerWord 14 b)) (wordP2 (controllerWord 14 b)) = b := by decide +kernel
theorem nb_basis_row_14 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 14 p = b) →
    routeVec 14 (wordP0 (controllerWord 14 b)) (wordP1 (controllerWord 14 b)) (wordP2 (controllerWord 14 b))
      (nbNoise 14 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_14
end DegreeDiameter.Portfolio.F9Graph56862
