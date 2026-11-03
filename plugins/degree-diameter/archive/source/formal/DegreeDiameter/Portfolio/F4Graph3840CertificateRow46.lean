import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_46 : ∀ (b : Fin 60),
    (¬∃ p, controller 46 p = b) →
    routeController 46 (wordP0 (controllerWord 46 b)) (wordP1 (controllerWord 46 b)) (wordP2 (controllerWord 46 b)) = b := by decide +kernel

theorem nb_basis_row_46 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 46 p = b) →
    routeVec 46 (wordP0 (controllerWord 46 b)) (wordP1 (controllerWord 46 b)) (wordP2 (controllerWord 46 b))
      (nbNoise 46 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_46 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 46 (adjP0 46 p d) (adjP1 46 p d) (adjP2 46 p d) (adjNoise 46 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
