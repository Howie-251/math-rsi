import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_57 : ∀ (b : Fin 60),
    (¬∃ p, controller 57 p = b) →
    routeController 57 (wordP0 (controllerWord 57 b)) (wordP1 (controllerWord 57 b)) (wordP2 (controllerWord 57 b)) = b := by decide +kernel

theorem nb_basis_row_57 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 57 p = b) →
    routeVec 57 (wordP0 (controllerWord 57 b)) (wordP1 (controllerWord 57 b)) (wordP2 (controllerWord 57 b))
      (nbNoise 57 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_57 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 57 (adjP0 57 p d) (adjP1 57 p d) (adjP2 57 p d) (adjNoise 57 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
