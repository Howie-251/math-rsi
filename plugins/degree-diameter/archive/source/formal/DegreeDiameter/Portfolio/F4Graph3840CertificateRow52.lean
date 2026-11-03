import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_52 : ∀ (b : Fin 60),
    (¬∃ p, controller 52 p = b) →
    routeController 52 (wordP0 (controllerWord 52 b)) (wordP1 (controllerWord 52 b)) (wordP2 (controllerWord 52 b)) = b := by decide +kernel

theorem nb_basis_row_52 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 52 p = b) →
    routeVec 52 (wordP0 (controllerWord 52 b)) (wordP1 (controllerWord 52 b)) (wordP2 (controllerWord 52 b))
      (nbNoise 52 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_52 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 52 (adjP0 52 p d) (adjP1 52 p d) (adjP2 52 p d) (adjNoise 52 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
