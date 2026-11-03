import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_41 : ∀ (b : Fin 60),
    (¬∃ p, controller 41 p = b) →
    routeController 41 (wordP0 (controllerWord 41 b)) (wordP1 (controllerWord 41 b)) (wordP2 (controllerWord 41 b)) = b := by decide +kernel

theorem nb_basis_row_41 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 41 p = b) →
    routeVec 41 (wordP0 (controllerWord 41 b)) (wordP1 (controllerWord 41 b)) (wordP2 (controllerWord 41 b))
      (nbNoise 41 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_41 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 41 (adjP0 41 p d) (adjP1 41 p d) (adjP2 41 p d) (adjNoise 41 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
