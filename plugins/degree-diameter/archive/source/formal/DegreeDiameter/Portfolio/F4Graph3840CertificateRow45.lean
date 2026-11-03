import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_45 : ∀ (b : Fin 60),
    (¬∃ p, controller 45 p = b) →
    routeController 45 (wordP0 (controllerWord 45 b)) (wordP1 (controllerWord 45 b)) (wordP2 (controllerWord 45 b)) = b := by decide +kernel

theorem nb_basis_row_45 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 45 p = b) →
    routeVec 45 (wordP0 (controllerWord 45 b)) (wordP1 (controllerWord 45 b)) (wordP2 (controllerWord 45 b))
      (nbNoise 45 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_45 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 45 (adjP0 45 p d) (adjP1 45 p d) (adjP2 45 p d) (adjNoise 45 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
