import DegreeDiameter.Portfolio.F3Graph15552Row0Data
namespace DegreeDiameter.Portfolio.F3Graph15552.Row0Coset
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem choice_group_certificate : ∀g z,slotGroup (choice g z)=g := by decide +kernel
theorem cover_certificate : ∀g z,routeVec (word (choice g z)) (alpha g z) 0=decodeVec z := by decide +kernel
#print axioms choice_group_certificate
#print axioms cover_certificate
end DegreeDiameter.Portfolio.F3Graph15552.Row0Coset
