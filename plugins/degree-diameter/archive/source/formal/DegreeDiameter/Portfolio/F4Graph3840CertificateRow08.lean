import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_8 : ∀ (b : Fin 60),
    (¬∃ p, controller 8 p = b) →
    routeController 8 (wordP0 (controllerWord 8 b)) (wordP1 (controllerWord 8 b)) (wordP2 (controllerWord 8 b)) = b := by decide +kernel

theorem nb_basis_row_8 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 8 p = b) →
    routeVec 8 (wordP0 (controllerWord 8 b)) (wordP1 (controllerWord 8 b)) (wordP2 (controllerWord 8 b))
      (nbNoise 8 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_8 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 8 (adjP0 8 p d) (adjP1 8 p d) (adjP2 8 p d) (adjNoise 8 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
