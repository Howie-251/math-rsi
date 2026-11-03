import DegreeDiameter.Portfolio.F3Graph15552FullCosetData05
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

namespace FullCoset28
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset28

namespace FullCoset29
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset29

namespace FullCoset30
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset30

namespace FullCoset31
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset31

end DegreeDiameter.Portfolio.F3Graph15552
