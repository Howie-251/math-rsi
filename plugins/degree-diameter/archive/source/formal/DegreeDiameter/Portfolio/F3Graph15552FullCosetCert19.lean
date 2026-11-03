import DegreeDiameter.Portfolio.F3Graph15552FullCosetData19
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

namespace FullCoset87
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset87

namespace FullCoset88
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset88

namespace FullCoset89
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset89

namespace FullCoset90
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset90

end DegreeDiameter.Portfolio.F3Graph15552
