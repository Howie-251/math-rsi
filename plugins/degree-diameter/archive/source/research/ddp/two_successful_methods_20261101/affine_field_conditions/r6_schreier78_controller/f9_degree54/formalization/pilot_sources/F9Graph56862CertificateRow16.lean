import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_16 : ∀ (b : Fin 78),
    (¬∃ p, controller 16 p = b) →
    routeController 16 (wordP0 (controllerWord 16 b)) (wordP1 (controllerWord 16 b)) (wordP2 (controllerWord 16 b)) = b := by decide +kernel
theorem nb_basis_row_16 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 16 p = b) →
    routeVec 16 (wordP0 (controllerWord 16 b)) (wordP1 (controllerWord 16 b)) (wordP2 (controllerWord 16 b))
      (nbNoise 16 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_16
end DegreeDiameter.Portfolio.F9Graph56862
