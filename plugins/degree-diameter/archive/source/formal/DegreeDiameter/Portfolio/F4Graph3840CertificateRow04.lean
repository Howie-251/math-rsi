import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_4 : ∀ (b : Fin 60),
    (¬∃ p, controller 4 p = b) →
    routeController 4 (wordP0 (controllerWord 4 b)) (wordP1 (controllerWord 4 b)) (wordP2 (controllerWord 4 b)) = b := by decide +kernel

theorem nb_basis_row_4 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 4 p = b) →
    routeVec 4 (wordP0 (controllerWord 4 b)) (wordP1 (controllerWord 4 b)) (wordP2 (controllerWord 4 b))
      (nbNoise 4 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_4 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 4 (adjP0 4 p d) (adjP1 4 p d) (adjP2 4 p d) (adjNoise 4 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
