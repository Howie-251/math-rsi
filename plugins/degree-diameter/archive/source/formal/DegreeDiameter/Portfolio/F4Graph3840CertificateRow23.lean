import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_23 : ∀ (b : Fin 60),
    (¬∃ p, controller 23 p = b) →
    routeController 23 (wordP0 (controllerWord 23 b)) (wordP1 (controllerWord 23 b)) (wordP2 (controllerWord 23 b)) = b := by decide +kernel

theorem nb_basis_row_23 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 23 p = b) →
    routeVec 23 (wordP0 (controllerWord 23 b)) (wordP1 (controllerWord 23 b)) (wordP2 (controllerWord 23 b))
      (nbNoise 23 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_23 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 23 (adjP0 23 p d) (adjP1 23 p d) (adjP2 23 p d) (adjNoise 23 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
