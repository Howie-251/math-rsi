import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_8 : ∀ (b : Fin 78),
    (¬∃ p, controller 8 p = b) →
    routeController 8 (wordP0 (controllerWord 8 b)) (wordP1 (controllerWord 8 b)) (wordP2 (controllerWord 8 b)) = b := by decide +kernel
theorem nb_basis_row_8 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 8 p = b) →
    routeVec 8 (wordP0 (controllerWord 8 b)) (wordP1 (controllerWord 8 b)) (wordP2 (controllerWord 8 b))
      (nbNoise 8 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_8
end DegreeDiameter.Portfolio.F9Graph56862
