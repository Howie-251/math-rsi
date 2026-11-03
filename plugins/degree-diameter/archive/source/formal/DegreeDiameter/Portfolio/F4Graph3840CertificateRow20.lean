import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_20 : ∀ (b : Fin 60),
    (¬∃ p, controller 20 p = b) →
    routeController 20 (wordP0 (controllerWord 20 b)) (wordP1 (controllerWord 20 b)) (wordP2 (controllerWord 20 b)) = b := by decide +kernel

theorem nb_basis_row_20 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 20 p = b) →
    routeVec 20 (wordP0 (controllerWord 20 b)) (wordP1 (controllerWord 20 b)) (wordP2 (controllerWord 20 b))
      (nbNoise 20 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_20 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 20 (adjP0 20 p d) (adjP1 20 p d) (adjP2 20 p d) (adjNoise 20 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
