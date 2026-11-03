import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_3 : ∀ (b : Fin 60),
    (¬∃ p, controller 3 p = b) →
    routeController 3 (wordP0 (controllerWord 3 b)) (wordP1 (controllerWord 3 b)) (wordP2 (controllerWord 3 b)) = b := by decide +kernel

theorem nb_basis_row_3 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 3 p = b) →
    routeVec 3 (wordP0 (controllerWord 3 b)) (wordP1 (controllerWord 3 b)) (wordP2 (controllerWord 3 b))
      (nbNoise 3 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_3 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 3 (adjP0 3 p d) (adjP1 3 p d) (adjP2 3 p d) (adjNoise 3 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
