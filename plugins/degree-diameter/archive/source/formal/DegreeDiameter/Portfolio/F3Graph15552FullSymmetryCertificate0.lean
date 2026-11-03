import DegreeDiameter.Portfolio.F3Graph15552FullSymmetryData
namespace DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem gen0_left_inverse : ∀a,inv0 (gen0 a)=a := by decide +kernel
theorem gen0_right_inverse : ∀a,gen0 (inv0 a)=a := by decide +kernel
theorem gen0_commutes : ∀a p,gen0 (controller a p)=controller (gen0 a) p := by decide +kernel
#print axioms gen0_left_inverse
#print axioms gen0_commutes
end DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
