import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_28 : ∀ (b : Fin 60),
    (¬∃ p, controller 28 p = b) →
    routeController 28 (wordP0 (controllerWord 28 b)) (wordP1 (controllerWord 28 b)) (wordP2 (controllerWord 28 b)) = b := by decide +kernel

theorem nb_basis_row_28 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 28 p = b) →
    routeVec 28 (wordP0 (controllerWord 28 b)) (wordP1 (controllerWord 28 b)) (wordP2 (controllerWord 28 b))
      (nbNoise 28 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_28 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 28 (adjP0 28 p d) (adjP1 28 p d) (adjP2 28 p d) (adjNoise 28 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
