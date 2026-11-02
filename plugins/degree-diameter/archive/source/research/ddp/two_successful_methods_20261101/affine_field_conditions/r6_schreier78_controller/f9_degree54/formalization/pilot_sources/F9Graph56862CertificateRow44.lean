import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_44 : ∀ (b : Fin 78),
    (¬∃ p, controller 44 p = b) →
    routeController 44 (wordP0 (controllerWord 44 b)) (wordP1 (controllerWord 44 b)) (wordP2 (controllerWord 44 b)) = b := by decide +kernel
theorem nb_basis_row_44 : ∀ (b : Fin 78) (j : Fin 3),
    (¬∃ p, controller 44 p = b) →
    routeVec 44 (wordP0 (controllerWord 44 b)) (wordP1 (controllerWord 44 b)) (wordP2 (controllerWord 44 b))
      (nbNoise 44 b (basisVec j)) 0 = basisVec j := by decide +kernel
#print axioms nb_basis_row_44
end DegreeDiameter.Portfolio.F9Graph56862
