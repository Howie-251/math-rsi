import DegreeDiameter.Portfolio.F4Graph1920Row14Data
namespace DegreeDiameter.Portfolio.F4Graph1920.Row14
open F4Graph3840
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem controller_row : ∀(b : Fin 30),(¬∃p,controller 14 p=b) →
    routeController 14 (wordP0 (controllerWord b)) (wordP1 (controllerWord b)) (wordP2 (controllerWord b))=b := by decide +kernel
theorem nb_basis_row : ∀(b : Fin 30)(j : Fin 3),(¬∃p,controller 14 p=b) →
    routeVec 14 (wordP0 (controllerWord b)) (wordP1 (controllerWord b)) (wordP2 (controllerWord b))
      (nbNoise b (basisVec j)) 0=basisVec j := by
  simp only [routeVec,stepVec]
  decide +kernel
theorem adjacent_row : ∀(p : Fin 4)(d : Fin 64),
    routeVec 14 (adjP0 p d) (adjP1 p d) (adjP2 p d) (adjNoise p d) 0=decodeVec d := by
  simp only [routeVec,stepVec]
  decide +kernel
#print axioms nb_basis_row
#print axioms adjacent_row
end DegreeDiameter.Portfolio.F4Graph1920.Row14
