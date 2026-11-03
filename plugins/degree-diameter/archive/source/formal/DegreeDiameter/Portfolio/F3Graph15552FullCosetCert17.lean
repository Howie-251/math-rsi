import DegreeDiameter.Portfolio.F3Graph15552FullCosetData17
namespace DegreeDiameter.Portfolio.F3Graph15552
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000

namespace FullCoset78
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset78

namespace FullCoset79
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset79

namespace FullCoset80
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset80

namespace FullCoset81
theorem column_certificate : ∀k j,routeVec (word k) 0 (basisVec j)=
    routeVec reference 0 (basisVec j)+routeVec (word k) (column k j) 0 := by decide +kernel
theorem cover_certificate : ∀z,routeVec (word (choice z)) (alpha z) 0=decodeVec z := by decide +kernel
theorem length_certificate : ∀k,(word k).length≤4 := by decide +kernel
#print axioms column_certificate
#print axioms cover_certificate
end FullCoset81

end DegreeDiameter.Portfolio.F3Graph15552
