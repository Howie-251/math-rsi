import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_11 : ∀ (b : Fin 60),
    (¬∃ p, controller 11 p = b) →
    routeController 11 (wordP0 (controllerWord 11 b)) (wordP1 (controllerWord 11 b)) (wordP2 (controllerWord 11 b)) = b := by decide +kernel

theorem nb_basis_row_11 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 11 p = b) →
    routeVec 11 (wordP0 (controllerWord 11 b)) (wordP1 (controllerWord 11 b)) (wordP2 (controllerWord 11 b))
      (nbNoise 11 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_11 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 11 (adjP0 11 p d) (adjP1 11 p d) (adjP2 11 p d) (adjNoise 11 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
