import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_6 : ∀ (b : Fin 60),
    (¬∃ p, controller 6 p = b) →
    routeController 6 (wordP0 (controllerWord 6 b)) (wordP1 (controllerWord 6 b)) (wordP2 (controllerWord 6 b)) = b := by decide +kernel

theorem nb_basis_row_6 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 6 p = b) →
    routeVec 6 (wordP0 (controllerWord 6 b)) (wordP1 (controllerWord 6 b)) (wordP2 (controllerWord 6 b))
      (nbNoise 6 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_6 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 6 (adjP0 6 p d) (adjP1 6 p d) (adjP2 6 p d) (adjNoise 6 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
