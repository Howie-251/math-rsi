import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_5 : ∀ (b : Fin 60),
    (¬∃ p, controller 5 p = b) →
    routeController 5 (wordP0 (controllerWord 5 b)) (wordP1 (controllerWord 5 b)) (wordP2 (controllerWord 5 b)) = b := by decide +kernel

theorem nb_basis_row_5 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 5 p = b) →
    routeVec 5 (wordP0 (controllerWord 5 b)) (wordP1 (controllerWord 5 b)) (wordP2 (controllerWord 5 b))
      (nbNoise 5 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_5 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 5 (adjP0 5 p d) (adjP1 5 p d) (adjP2 5 p d) (adjNoise 5 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
