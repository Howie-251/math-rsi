import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_10 : ∀ (b : Fin 60),
    (¬∃ p, controller 10 p = b) →
    routeController 10 (wordP0 (controllerWord 10 b)) (wordP1 (controllerWord 10 b)) (wordP2 (controllerWord 10 b)) = b := by decide +kernel

theorem nb_basis_row_10 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 10 p = b) →
    routeVec 10 (wordP0 (controllerWord 10 b)) (wordP1 (controllerWord 10 b)) (wordP2 (controllerWord 10 b))
      (nbNoise 10 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_10 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 10 (adjP0 10 p d) (adjP1 10 p d) (adjP2 10 p d) (adjNoise 10 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
