import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_48 : ∀ (b : Fin 60),
    (¬∃ p, controller 48 p = b) →
    routeController 48 (wordP0 (controllerWord 48 b)) (wordP1 (controllerWord 48 b)) (wordP2 (controllerWord 48 b)) = b := by decide +kernel

theorem nb_basis_row_48 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 48 p = b) →
    routeVec 48 (wordP0 (controllerWord 48 b)) (wordP1 (controllerWord 48 b)) (wordP2 (controllerWord 48 b))
      (nbNoise 48 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_48 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 48 (adjP0 48 p d) (adjP1 48 p d) (adjP2 48 p d) (adjNoise 48 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
