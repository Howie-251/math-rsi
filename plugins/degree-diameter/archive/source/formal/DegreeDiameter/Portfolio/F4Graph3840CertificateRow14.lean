import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_14 : ∀ (b : Fin 60),
    (¬∃ p, controller 14 p = b) →
    routeController 14 (wordP0 (controllerWord 14 b)) (wordP1 (controllerWord 14 b)) (wordP2 (controllerWord 14 b)) = b := by decide +kernel

theorem nb_basis_row_14 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 14 p = b) →
    routeVec 14 (wordP0 (controllerWord 14 b)) (wordP1 (controllerWord 14 b)) (wordP2 (controllerWord 14 b))
      (nbNoise 14 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_14 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 14 (adjP0 14 p d) (adjP1 14 p d) (adjP2 14 p d) (adjNoise 14 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
