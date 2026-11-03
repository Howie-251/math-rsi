import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_43 : ∀ (b : Fin 60),
    (¬∃ p, controller 43 p = b) →
    routeController 43 (wordP0 (controllerWord 43 b)) (wordP1 (controllerWord 43 b)) (wordP2 (controllerWord 43 b)) = b := by decide +kernel

theorem nb_basis_row_43 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 43 p = b) →
    routeVec 43 (wordP0 (controllerWord 43 b)) (wordP1 (controllerWord 43 b)) (wordP2 (controllerWord 43 b))
      (nbNoise 43 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_43 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 43 (adjP0 43 p d) (adjP1 43 p d) (adjP2 43 p d) (adjNoise 43 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
