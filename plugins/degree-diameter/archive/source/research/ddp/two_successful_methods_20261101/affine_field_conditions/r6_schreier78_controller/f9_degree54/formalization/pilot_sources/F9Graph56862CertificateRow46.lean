import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_46 : ∀ (b : Fin 78),
    (¬∃ p, controller 46 p = b) →
    routeController 46 (wordP0 (controllerWord 46 b)) (wordP1 (controllerWord 46 b)) (wordP2 (controllerWord 46 b)) = b := by decide +kernel
theorem nb_basis_row_46 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 46 p = b) →
    routeVec 46 (wordP0 (controllerWord 46 b)) (wordP1 (controllerWord 46 b)) (wordP2 (controllerWord 46 b))
      (nbNoise 46 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_46
end DegreeDiameter.Portfolio.F9Graph56862
