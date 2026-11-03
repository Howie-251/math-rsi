import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_59 : ∀ (b : Fin 60),
    (¬∃ p, controller 59 p = b) →
    routeController 59 (wordP0 (controllerWord 59 b)) (wordP1 (controllerWord 59 b)) (wordP2 (controllerWord 59 b)) = b := by decide +kernel

theorem nb_basis_row_59 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 59 p = b) →
    routeVec 59 (wordP0 (controllerWord 59 b)) (wordP1 (controllerWord 59 b)) (wordP2 (controllerWord 59 b))
      (nbNoise 59 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_59 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 59 (adjP0 59 p d) (adjP1 59 p d) (adjP2 59 p d) (adjNoise 59 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
