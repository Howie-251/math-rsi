import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_18 : ∀ (b : Fin 78),
    (¬∃ p, controller 18 p = b) →
    routeController 18 (wordP0 (controllerWord 18 b)) (wordP1 (controllerWord 18 b)) (wordP2 (controllerWord 18 b)) = b := by decide +kernel
theorem nb_basis_row_18 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 18 p = b) →
    routeVec 18 (wordP0 (controllerWord 18 b)) (wordP1 (controllerWord 18 b)) (wordP2 (controllerWord 18 b))
      (nbNoise 18 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_18
end DegreeDiameter.Portfolio.F9Graph56862
