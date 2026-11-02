import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_49 : ∀ (b : Fin 60),
    (¬∃ p, controller 49 p = b) →
    routeController 49 (wordP0 (controllerWord 49 b)) (wordP1 (controllerWord 49 b)) (wordP2 (controllerWord 49 b)) = b := by decide +kernel

theorem nb_basis_row_49 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 49 p = b) →
    routeVec 49 (wordP0 (controllerWord 49 b)) (wordP1 (controllerWord 49 b)) (wordP2 (controllerWord 49 b))
      (nbNoise 49 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_49 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 49 (adjP0 49 p d) (adjP1 49 p d) (adjP2 49 p d) (adjNoise 49 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
