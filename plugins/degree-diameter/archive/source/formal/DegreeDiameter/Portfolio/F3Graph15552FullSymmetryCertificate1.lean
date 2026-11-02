import DegreeDiameter.Portfolio.F3Graph15552FullSymmetryData
namespace DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem gen1_left_inverse : ∀a,inv1 (gen1 a)=a := by decide +kernel
theorem gen1_right_inverse : ∀a,gen1 (inv1 a)=a := by decide +kernel
theorem gen1_commutes : ∀a p,gen1 (controller a p)=controller (gen1 a) p := by decide +kernel
#print axioms gen1_left_inverse
#print axioms gen1_commutes
end DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
