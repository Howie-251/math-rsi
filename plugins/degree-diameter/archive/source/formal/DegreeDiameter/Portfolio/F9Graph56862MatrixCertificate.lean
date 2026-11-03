import DegreeDiameter.Portfolio.F9Graph56862
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
/-- Actual reverse dart matrices checked on all three basis vectors. -/
theorem inverse_basis : ∀ (a : Fin 78) (p : Fin 6) (j : Fin 3),
  act (matrix (controller a p) (inversePort p)) (act (matrix a p) (basisVec j)) = basisVec j := by decide +kernel

/-- Actual transported noise directions, one check per dart. -/
theorem inverse_direction : ∀ (a : Fin 78) (p : Fin 6),
  act (matrix (controller a p) (inversePort p)) (direction (inversePort p)) = direction p := by decide +kernel


#print axioms inverse_basis
#print axioms inverse_direction
end DegreeDiameter.Portfolio.F9Graph56862
