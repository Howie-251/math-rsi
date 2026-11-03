import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_25 : ∀ (b : Fin 60),
    (¬∃ p, controller 25 p = b) →
    routeController 25 (wordP0 (controllerWord 25 b)) (wordP1 (controllerWord 25 b)) (wordP2 (controllerWord 25 b)) = b := by decide +kernel

theorem nb_basis_row_25 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 25 p = b) →
    routeVec 25 (wordP0 (controllerWord 25 b)) (wordP1 (controllerWord 25 b)) (wordP2 (controllerWord 25 b))
      (nbNoise 25 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_25 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 25 (adjP0 25 p d) (adjP1 25 p d) (adjP2 25 p d) (adjNoise 25 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
