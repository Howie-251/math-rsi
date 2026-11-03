import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_16 : ∀ (b : Fin 60),
    (¬∃ p, controller 16 p = b) →
    routeController 16 (wordP0 (controllerWord 16 b)) (wordP1 (controllerWord 16 b)) (wordP2 (controllerWord 16 b)) = b := by decide +kernel

theorem nb_basis_row_16 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 16 p = b) →
    routeVec 16 (wordP0 (controllerWord 16 b)) (wordP1 (controllerWord 16 b)) (wordP2 (controllerWord 16 b))
      (nbNoise 16 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_16 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 16 (adjP0 16 p d) (adjP1 16 p d) (adjP2 16 p d) (adjNoise 16 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
