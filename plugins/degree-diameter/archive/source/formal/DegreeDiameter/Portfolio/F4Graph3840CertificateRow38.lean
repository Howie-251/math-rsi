import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_38 : ∀ (b : Fin 60),
    (¬∃ p, controller 38 p = b) →
    routeController 38 (wordP0 (controllerWord 38 b)) (wordP1 (controllerWord 38 b)) (wordP2 (controllerWord 38 b)) = b := by decide +kernel

theorem nb_basis_row_38 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 38 p = b) →
    routeVec 38 (wordP0 (controllerWord 38 b)) (wordP1 (controllerWord 38 b)) (wordP2 (controllerWord 38 b))
      (nbNoise 38 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_38 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 38 (adjP0 38 p d) (adjP1 38 p d) (adjP2 38 p d) (adjNoise 38 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
