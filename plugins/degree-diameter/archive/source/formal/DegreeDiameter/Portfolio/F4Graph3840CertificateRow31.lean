import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_31 : ∀ (b : Fin 60),
    (¬∃ p, controller 31 p = b) →
    routeController 31 (wordP0 (controllerWord 31 b)) (wordP1 (controllerWord 31 b)) (wordP2 (controllerWord 31 b)) = b := by decide +kernel

theorem nb_basis_row_31 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 31 p = b) →
    routeVec 31 (wordP0 (controllerWord 31 b)) (wordP1 (controllerWord 31 b)) (wordP2 (controllerWord 31 b))
      (nbNoise 31 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_31 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 31 (adjP0 31 p d) (adjP1 31 p d) (adjP2 31 p d) (adjNoise 31 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
