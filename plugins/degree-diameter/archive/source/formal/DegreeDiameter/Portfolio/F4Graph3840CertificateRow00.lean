import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_0 : ∀ (b : Fin 60),
    (¬∃ p, controller 0 p = b) →
    routeController 0 (wordP0 (controllerWord 0 b)) (wordP1 (controllerWord 0 b)) (wordP2 (controllerWord 0 b)) = b := by decide +kernel

theorem nb_basis_row_0 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 0 p = b) →
    routeVec 0 (wordP0 (controllerWord 0 b)) (wordP1 (controllerWord 0 b)) (wordP2 (controllerWord 0 b))
      (nbNoise 0 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_0 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 0 (adjP0 0 p d) (adjP1 0 p d) (adjP2 0 p d) (adjNoise 0 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
