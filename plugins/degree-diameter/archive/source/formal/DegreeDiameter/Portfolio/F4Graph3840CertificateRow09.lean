import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_9 : ∀ (b : Fin 60),
    (¬∃ p, controller 9 p = b) →
    routeController 9 (wordP0 (controllerWord 9 b)) (wordP1 (controllerWord 9 b)) (wordP2 (controllerWord 9 b)) = b := by decide +kernel

theorem nb_basis_row_9 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 9 p = b) →
    routeVec 9 (wordP0 (controllerWord 9 b)) (wordP1 (controllerWord 9 b)) (wordP2 (controllerWord 9 b))
      (nbNoise 9 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_9 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 9 (adjP0 9 p d) (adjP1 9 p d) (adjP2 9 p d) (adjNoise 9 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
