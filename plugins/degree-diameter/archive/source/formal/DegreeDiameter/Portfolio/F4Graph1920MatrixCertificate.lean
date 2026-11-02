import DegreeDiameter.Portfolio.F4Graph1920Definitions
namespace DegreeDiameter.Portfolio.F4Graph1920
open F4Graph3840
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
/-- Actual reverse dart matrices checked on all three basis vectors. -/
theorem inverse_basis : ∀ (a : Fin 30) (p : Fin 4) (j : Fin 3),
  act (matrix (controller a p) (inversePort p)) (act (matrix a p) (basisVec j)) = basisVec j := by decide

/-- Actual transported noise directions, one check per dart. -/
theorem inverse_direction : ∀ (a : Fin 30) (p : Fin 4),
  act (matrix (controller a p) (inversePort p)) (direction (inversePort p)) = direction p := by decide


#print axioms inverse_basis
#print axioms inverse_direction
end DegreeDiameter.Portfolio.F4Graph1920
