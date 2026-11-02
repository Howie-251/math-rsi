import DegreeDiameter.Portfolio.F3Graph15552FullSymmetryData
namespace DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem controller_coverage : ∀a,
    wordController (representatives (representativeIndex a)) (transportWord a)=a := by decide +kernel
#print axioms controller_coverage
end DegreeDiameter.Portfolio.F3Graph15552.FullSymmetry
