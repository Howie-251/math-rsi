import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_17 : ∀ (b : Fin 60),
    (¬∃ p, controller 17 p = b) →
    routeController 17 (wordP0 (controllerWord 17 b)) (wordP1 (controllerWord 17 b)) (wordP2 (controllerWord 17 b)) = b := by decide +kernel

theorem nb_basis_row_17 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 17 p = b) →
    routeVec 17 (wordP0 (controllerWord 17 b)) (wordP1 (controllerWord 17 b)) (wordP2 (controllerWord 17 b))
      (nbNoise 17 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_17 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 17 (adjP0 17 p d) (adjP1 17 p d) (adjP2 17 p d) (adjNoise 17 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
