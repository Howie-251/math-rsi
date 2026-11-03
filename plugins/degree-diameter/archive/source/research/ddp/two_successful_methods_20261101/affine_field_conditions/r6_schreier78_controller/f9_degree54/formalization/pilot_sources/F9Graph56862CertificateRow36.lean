import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_36 : ∀ (b : Fin 78),
    (¬∃ p, controller 36 p = b) →
    routeController 36 (wordP0 (controllerWord 36 b)) (wordP1 (controllerWord 36 b)) (wordP2 (controllerWord 36 b)) = b := by decide +kernel
theorem nb_basis_row_36 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 36 p = b) →
    routeVec 36 (wordP0 (controllerWord 36 b)) (wordP1 (controllerWord 36 b)) (wordP2 (controllerWord 36 b))
      (nbNoise 36 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_36
end DegreeDiameter.Portfolio.F9Graph56862
