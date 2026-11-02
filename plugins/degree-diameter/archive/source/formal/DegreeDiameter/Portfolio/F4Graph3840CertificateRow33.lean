import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_33 : ∀ (b : Fin 60),
    (¬∃ p, controller 33 p = b) →
    routeController 33 (wordP0 (controllerWord 33 b)) (wordP1 (controllerWord 33 b)) (wordP2 (controllerWord 33 b)) = b := by decide +kernel

theorem nb_basis_row_33 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 33 p = b) →
    routeVec 33 (wordP0 (controllerWord 33 b)) (wordP1 (controllerWord 33 b)) (wordP2 (controllerWord 33 b))
      (nbNoise 33 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_33 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 33 (adjP0 33 p d) (adjP1 33 p d) (adjP2 33 p d) (adjNoise 33 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
