import DegreeDiameter.Portfolio.F3Graph15552Row0Data
namespace DegreeDiameter.Portfolio.F3Graph15552.Row0Coset
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec (reference (slotGroup k)) 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem controller_certificate : ∀k,routeController 0 (word k)=target (slotGroup k) := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms controller_certificate
end DegreeDiameter.Portfolio.F3Graph15552.Row0Coset
