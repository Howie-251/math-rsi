import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_41 : ∀ (b : Fin 78),
    (¬∃ p, controller 41 p = b) →
    routeController 41 (wordP0 (controllerWord 41 b)) (wordP1 (controllerWord 41 b)) (wordP2 (controllerWord 41 b)) = b := by decide +kernel
theorem nb_basis_row_41 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 41 p = b) →
    routeVec 41 (wordP0 (controllerWord 41 b)) (wordP1 (controllerWord 41 b)) (wordP2 (controllerWord 41 b))
      (nbNoise 41 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_41
end DegreeDiameter.Portfolio.F9Graph56862
