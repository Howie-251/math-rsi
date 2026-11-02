import DegreeDiameter.Portfolio.F3Graph15552FullRowData
namespace DegreeDiameter.Portfolio.F3Graph15552.FullKernel
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem endpoint_row5 : ∀b,pairCondition (5 : Fin 8) b := by decide +kernel
#print axioms endpoint_row5
end DegreeDiameter.Portfolio.F3Graph15552.FullKernel
