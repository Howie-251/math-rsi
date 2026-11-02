import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_29 : ∀ (b : Fin 60),
    (¬∃ p, controller 29 p = b) →
    routeController 29 (wordP0 (controllerWord 29 b)) (wordP1 (controllerWord 29 b)) (wordP2 (controllerWord 29 b)) = b := by decide +kernel

theorem nb_basis_row_29 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 29 p = b) →
    routeVec 29 (wordP0 (controllerWord 29 b)) (wordP1 (controllerWord 29 b)) (wordP2 (controllerWord 29 b))
      (nbNoise 29 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_29 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 29 (adjP0 29 p d) (adjP1 29 p d) (adjP2 29 p d) (adjNoise 29 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
