import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_50 : ∀ (b : Fin 60),
    (¬∃ p, controller 50 p = b) →
    routeController 50 (wordP0 (controllerWord 50 b)) (wordP1 (controllerWord 50 b)) (wordP2 (controllerWord 50 b)) = b := by decide +kernel

theorem nb_basis_row_50 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 50 p = b) →
    routeVec 50 (wordP0 (controllerWord 50 b)) (wordP1 (controllerWord 50 b)) (wordP2 (controllerWord 50 b))
      (nbNoise 50 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_50 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 50 (adjP0 50 p d) (adjP1 50 p d) (adjP2 50 p d) (adjNoise 50 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
