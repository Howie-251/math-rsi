import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_22 : ∀ (b : Fin 60),
    (¬∃ p, controller 22 p = b) →
    routeController 22 (wordP0 (controllerWord 22 b)) (wordP1 (controllerWord 22 b)) (wordP2 (controllerWord 22 b)) = b := by decide +kernel

theorem nb_basis_row_22 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 22 p = b) →
    routeVec 22 (wordP0 (controllerWord 22 b)) (wordP1 (controllerWord 22 b)) (wordP2 (controllerWord 22 b))
      (nbNoise 22 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_22 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 22 (adjP0 22 p d) (adjP1 22 p d) (adjP2 22 p d) (adjNoise 22 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
