import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_21 : ∀ (b : Fin 60),
    (¬∃ p, controller 21 p = b) →
    routeController 21 (wordP0 (controllerWord 21 b)) (wordP1 (controllerWord 21 b)) (wordP2 (controllerWord 21 b)) = b := by decide +kernel

theorem nb_basis_row_21 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 21 p = b) →
    routeVec 21 (wordP0 (controllerWord 21 b)) (wordP1 (controllerWord 21 b)) (wordP2 (controllerWord 21 b))
      (nbNoise 21 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_21 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 21 (adjP0 21 p d) (adjP1 21 p d) (adjP2 21 p d) (adjNoise 21 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
