import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_55 : ∀ (b : Fin 60),
    (¬∃ p, controller 55 p = b) →
    routeController 55 (wordP0 (controllerWord 55 b)) (wordP1 (controllerWord 55 b)) (wordP2 (controllerWord 55 b)) = b := by decide +kernel

theorem nb_basis_row_55 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 55 p = b) →
    routeVec 55 (wordP0 (controllerWord 55 b)) (wordP1 (controllerWord 55 b)) (wordP2 (controllerWord 55 b))
      (nbNoise 55 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_55 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 55 (adjP0 55 p d) (adjP1 55 p d) (adjP2 55 p d) (adjNoise 55 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
