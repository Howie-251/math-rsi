import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_44 : ∀ (b : Fin 60),
    (¬∃ p, controller 44 p = b) →
    routeController 44 (wordP0 (controllerWord 44 b)) (wordP1 (controllerWord 44 b)) (wordP2 (controllerWord 44 b)) = b := by decide +kernel

theorem nb_basis_row_44 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 44 p = b) →
    routeVec 44 (wordP0 (controllerWord 44 b)) (wordP1 (controllerWord 44 b)) (wordP2 (controllerWord 44 b))
      (nbNoise 44 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_44 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 44 (adjP0 44 p d) (adjP1 44 p d) (adjP2 44 p d) (adjNoise 44 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
