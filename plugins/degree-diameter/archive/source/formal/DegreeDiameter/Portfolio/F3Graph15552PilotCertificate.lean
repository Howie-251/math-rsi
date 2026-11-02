import DegreeDiameter.Portfolio.F3Graph15552PilotData
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
namespace PilotLargestGroup
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem controller_certificate : ∀k,routeController a (word k)=b := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end PilotLargestGroup
namespace PilotFullrank
theorem basis_certificate : ∀j,routeVec word (inverseBasis j) 0=basisVec j := by decide +kernel
theorem controller_certificate : routeController a word=b := by decide +kernel
theorem length_certificate : word.length≤4 := by decide +kernel
#print axioms basis_certificate
end PilotFullrank
end DegreeDiameter.Portfolio.F3Graph15552
