import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_35 : ∀ (b : Fin 60),
    (¬∃ p, controller 35 p = b) →
    routeController 35 (wordP0 (controllerWord 35 b)) (wordP1 (controllerWord 35 b)) (wordP2 (controllerWord 35 b)) = b := by decide +kernel

theorem nb_basis_row_35 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 35 p = b) →
    routeVec 35 (wordP0 (controllerWord 35 b)) (wordP1 (controllerWord 35 b)) (wordP2 (controllerWord 35 b))
      (nbNoise 35 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_35 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 35 (adjP0 35 p d) (adjP1 35 p d) (adjP2 35 p d) (adjNoise 35 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
