import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_58 : ∀ (b : Fin 60),
    (¬∃ p, controller 58 p = b) →
    routeController 58 (wordP0 (controllerWord 58 b)) (wordP1 (controllerWord 58 b)) (wordP2 (controllerWord 58 b)) = b := by decide +kernel

theorem nb_basis_row_58 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 58 p = b) →
    routeVec 58 (wordP0 (controllerWord 58 b)) (wordP1 (controllerWord 58 b)) (wordP2 (controllerWord 58 b))
      (nbNoise 58 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_58 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 58 (adjP0 58 p d) (adjP1 58 p d) (adjP2 58 p d) (adjNoise 58 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
