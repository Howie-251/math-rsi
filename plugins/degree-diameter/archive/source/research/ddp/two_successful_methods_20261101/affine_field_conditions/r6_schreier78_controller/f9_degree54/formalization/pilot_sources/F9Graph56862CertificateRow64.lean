import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_64 : ∀ (b : Fin 78),
    (¬∃ p, controller 64 p = b) →
    routeController 64 (wordP0 (controllerWord 64 b)) (wordP1 (controllerWord 64 b)) (wordP2 (controllerWord 64 b)) = b := by decide +kernel
theorem nb_basis_row_64 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 64 p = b) →
    routeVec 64 (wordP0 (controllerWord 64 b)) (wordP1 (controllerWord 64 b)) (wordP2 (controllerWord 64 b))
      (nbNoise 64 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_64
end DegreeDiameter.Portfolio.F9Graph56862
