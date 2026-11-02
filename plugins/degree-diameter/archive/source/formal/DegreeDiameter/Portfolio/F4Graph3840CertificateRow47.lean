import DegreeDiameter.Portfolio.F4Graph3840RouteData
import DegreeDiameter.Portfolio.F4Graph3840Linear
import DegreeDiameter.Portfolio.F4Graph3840FastTables
namespace DegreeDiameter.Portfolio.F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row_47 : ∀ (b : Fin 60),
    (¬∃ p, controller 47 p = b) →
    routeController 47 (wordP0 (controllerWord 47 b)) (wordP1 (controllerWord 47 b)) (wordP2 (controllerWord 47 b)) = b := by decide +kernel

theorem nb_basis_row_47 : ∀ (b : Fin 60) (j : Fin 3),
    (¬∃ p, controller 47 p = b) →
    routeVec 47 (wordP0 (controllerWord 47 b)) (wordP1 (controllerWord 47 b)) (wordP2 (controllerWord 47 b))
      (nbNoise 47 b (basisVec j)) 0 = basisVec j := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel

theorem adjacent_row_47 : ∀ (p : Fin 5) (d : Fin 64),
    routeVec 47 (adjP0 47 p d) (adjP1 47 p d) (adjP2 47 p d) (adjNoise 47 p d) 0 = decodeVec d := by
  simp only [routeVec,stepVec,matrix_eq_fast]
  decide +kernel


end DegreeDiameter.Portfolio.F4Graph3840
