import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_40 : ∀ (b : Fin 60),
    (¬∃ p, controller 40 p = b) →
    routeController 40 (wordP0 (controllerWord 40 b)) (wordP1 (controllerWord 40 b)) (wordP2 (controllerWord 40 b)) = b := by decide +kernel

theorem nb_basis_row_40 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 40 p = b) →
    routeVec 40 (wordP0 (controllerWord 40 b)) (wordP1 (controllerWord 40 b)) (wordP2 (controllerWord 40 b))
      (nbNoise 40 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_40 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 40 (adjP0 40 p d) (adjP1 40 p d) (adjP2 40 p d) (adjNoise 40 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
