import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_7 : ∀ (b : Fin 60),
    (¬∃ p, controller 7 p = b) →
    routeController 7 (wordP0 (controllerWord 7 b)) (wordP1 (controllerWord 7 b)) (wordP2 (controllerWord 7 b)) = b := by decide +kernel

theorem nb_basis_row_7 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 7 p = b) →
    routeVec 7 (wordP0 (controllerWord 7 b)) (wordP1 (controllerWord 7 b)) (wordP2 (controllerWord 7 b))
      (nbNoise 7 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_7 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 7 (adjP0 7 p d) (adjP1 7 p d) (adjP2 7 p d) (adjNoise 7 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
