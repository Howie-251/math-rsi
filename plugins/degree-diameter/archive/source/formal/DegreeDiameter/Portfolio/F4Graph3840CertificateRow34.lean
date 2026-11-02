import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_34 : ∀ (b : Fin 60),
    (¬∃ p, controller 34 p = b) →
    routeController 34 (wordP0 (controllerWord 34 b)) (wordP1 (controllerWord 34 b)) (wordP2 (controllerWord 34 b)) = b := by decide +kernel

theorem nb_basis_row_34 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 34 p = b) →
    routeVec 34 (wordP0 (controllerWord 34 b)) (wordP1 (controllerWord 34 b)) (wordP2 (controllerWord 34 b))
      (nbNoise 34 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_34 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 34 (adjP0 34 p d) (adjP1 34 p d) (adjP2 34 p d) (adjNoise 34 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
