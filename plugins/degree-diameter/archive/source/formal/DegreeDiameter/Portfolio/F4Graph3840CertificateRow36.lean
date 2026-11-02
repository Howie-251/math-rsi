import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_36 : ∀ (b : Fin 60),
    (¬∃ p, controller 36 p = b) →
    routeController 36 (wordP0 (controllerWord 36 b)) (wordP1 (controllerWord 36 b)) (wordP2 (controllerWord 36 b)) = b := by decide +kernel

theorem nb_basis_row_36 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 36 p = b) →
    routeVec 36 (wordP0 (controllerWord 36 b)) (wordP1 (controllerWord 36 b)) (wordP2 (controllerWord 36 b))
      (nbNoise 36 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_36 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 36 (adjP0 36 p d) (adjP1 36 p d) (adjP2 36 p d) (adjNoise 36 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
