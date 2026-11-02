import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_27 : ∀ (b : Fin 60),
    (¬∃ p, controller 27 p = b) →
    routeController 27 (wordP0 (controllerWord 27 b)) (wordP1 (controllerWord 27 b)) (wordP2 (controllerWord 27 b)) = b := by decide +kernel

theorem nb_basis_row_27 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 27 p = b) →
    routeVec 27 (wordP0 (controllerWord 27 b)) (wordP1 (controllerWord 27 b)) (wordP2 (controllerWord 27 b))
      (nbNoise 27 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_27 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 27 (adjP0 27 p d) (adjP1 27 p d) (adjP2 27 p d) (adjNoise 27 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
