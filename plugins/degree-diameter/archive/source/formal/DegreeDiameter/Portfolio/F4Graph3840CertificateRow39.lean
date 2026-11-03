import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_39 : ∀ (b : Fin 60),
    (¬∃ p, controller 39 p = b) →
    routeController 39 (wordP0 (controllerWord 39 b)) (wordP1 (controllerWord 39 b)) (wordP2 (controllerWord 39 b)) = b := by decide +kernel

theorem nb_basis_row_39 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 39 p = b) →
    routeVec 39 (wordP0 (controllerWord 39 b)) (wordP1 (controllerWord 39 b)) (wordP2 (controllerWord 39 b))
      (nbNoise 39 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_39 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 39 (adjP0 39 p d) (adjP1 39 p d) (adjP2 39 p d) (adjNoise 39 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
