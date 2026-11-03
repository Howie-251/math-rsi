import DegreeDiameter.Portfolio.F3Graph15552Row0Data
namespace DegreeDiameter.Portfolio.F3Graph15552.Row0Fullrank
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem basis_certificate : ∀k j,routeVec (word k) (inverseBasis k j) 0=basisVec j := by decide +kernel
theorem controller_certificate : ∀k,routeController 0 (word k)=target k := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms basis_certificate
#print axioms controller_certificate
end DegreeDiameter.Portfolio.F3Graph15552.Row0Fullrank
