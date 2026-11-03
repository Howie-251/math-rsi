import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_13 : ∀ (b : Fin 60),
    (¬∃ p, controller 13 p = b) →
    routeController 13 (wordP0 (controllerWord 13 b)) (wordP1 (controllerWord 13 b)) (wordP2 (controllerWord 13 b)) = b := by decide +kernel

theorem nb_basis_row_13 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 13 p = b) →
    routeVec 13 (wordP0 (controllerWord 13 b)) (wordP1 (controllerWord 13 b)) (wordP2 (controllerWord 13 b))
      (nbNoise 13 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_13 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 13 (adjP0 13 p d) (adjP1 13 p d) (adjP2 13 p d) (adjNoise 13 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
