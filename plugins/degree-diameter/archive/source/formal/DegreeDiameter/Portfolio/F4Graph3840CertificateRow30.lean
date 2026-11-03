import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_30 : ∀ (b : Fin 60),
    (¬∃ p, controller 30 p = b) →
    routeController 30 (wordP0 (controllerWord 30 b)) (wordP1 (controllerWord 30 b)) (wordP2 (controllerWord 30 b)) = b := by decide +kernel

theorem nb_basis_row_30 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 30 p = b) →
    routeVec 30 (wordP0 (controllerWord 30 b)) (wordP1 (controllerWord 30 b)) (wordP2 (controllerWord 30 b))
      (nbNoise 30 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_30 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 30 (adjP0 30 p d) (adjP1 30 p d) (adjP2 30 p d) (adjNoise 30 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
