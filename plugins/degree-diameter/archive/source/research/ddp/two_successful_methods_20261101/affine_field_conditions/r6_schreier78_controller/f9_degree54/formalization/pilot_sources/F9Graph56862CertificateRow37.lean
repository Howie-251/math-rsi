import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_37 : ∀ (b : Fin 78),
    (¬∃ p, controller 37 p = b) →
    routeController 37 (wordP0 (controllerWord 37 b)) (wordP1 (controllerWord 37 b)) (wordP2 (controllerWord 37 b)) = b := by decide +kernel
theorem nb_basis_row_37 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 37 p = b) →
    routeVec 37 (wordP0 (controllerWord 37 b)) (wordP1 (controllerWord 37 b)) (wordP2 (controllerWord 37 b))
      (nbNoise 37 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_37
end DegreeDiameter.Portfolio.F9Graph56862
