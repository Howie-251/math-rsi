import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_53 : ∀ (b : Fin 60),
    (¬∃ p, controller 53 p = b) →
    routeController 53 (wordP0 (controllerWord 53 b)) (wordP1 (controllerWord 53 b)) (wordP2 (controllerWord 53 b)) = b := by decide +kernel

theorem nb_basis_row_53 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 53 p = b) →
    routeVec 53 (wordP0 (controllerWord 53 b)) (wordP1 (controllerWord 53 b)) (wordP2 (controllerWord 53 b))
      (nbNoise 53 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_53 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 53 (adjP0 53 p d) (adjP1 53 p d) (adjP2 53 p d) (adjNoise 53 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
