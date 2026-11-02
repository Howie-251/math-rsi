import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_54 : ∀ (b : Fin 60),
    (¬∃ p, controller 54 p = b) →
    routeController 54 (wordP0 (controllerWord 54 b)) (wordP1 (controllerWord 54 b)) (wordP2 (controllerWord 54 b)) = b := by decide +kernel

theorem nb_basis_row_54 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 54 p = b) →
    routeVec 54 (wordP0 (controllerWord 54 b)) (wordP1 (controllerWord 54 b)) (wordP2 (controllerWord 54 b))
      (nbNoise 54 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_54 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 54 (adjP0 54 p d) (adjP1 54 p d) (adjP2 54 p d) (adjNoise 54 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
