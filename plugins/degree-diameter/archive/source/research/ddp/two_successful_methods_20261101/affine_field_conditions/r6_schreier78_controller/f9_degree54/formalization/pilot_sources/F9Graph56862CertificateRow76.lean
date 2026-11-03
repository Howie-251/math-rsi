import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_76 : ∀ (b : Fin 78),
    (¬∃ p, controller 76 p = b) →
    routeController 76 (wordP0 (controllerWord 76 b)) (wordP1 (controllerWord 76 b)) (wordP2 (controllerWord 76 b)) = b := by decide +kernel
theorem nb_basis_row_76 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 76 p = b) →
    routeVec 76 (wordP0 (controllerWord 76 b)) (wordP1 (controllerWord 76 b)) (wordP2 (controllerWord 76 b))
      (nbNoise 76 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_76
end DegreeDiameter.Portfolio.F9Graph56862
