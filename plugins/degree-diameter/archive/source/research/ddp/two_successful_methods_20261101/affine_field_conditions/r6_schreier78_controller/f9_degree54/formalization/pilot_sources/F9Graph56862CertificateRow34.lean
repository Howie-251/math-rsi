import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_34 : ∀ (b : Fin 78),
    (¬∃ p, controller 34 p = b) →
    routeController 34 (wordP0 (controllerWord 34 b)) (wordP1 (controllerWord 34 b)) (wordP2 (controllerWord 34 b)) = b := by decide +kernel
theorem nb_basis_row_34 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 34 p = b) →
    routeVec 34 (wordP0 (controllerWord 34 b)) (wordP1 (controllerWord 34 b)) (wordP2 (controllerWord 34 b))
      (nbNoise 34 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_34
end DegreeDiameter.Portfolio.F9Graph56862
