import DegreeDiameter.Portfolio.F3Graph15552FullRowData
namespace DegreeDiameter.Portfolio.F3Graph15552.FullKernel
set_option maxRecDepth 20000
set_option maxHeartbeats 40000000
theorem endpoint_row2 : ∀b,pairCondition (2 : Fin 8) b := by decide +kernel
#print axioms endpoint_row2
end DegreeDiameter.Portfolio.F3Graph15552.FullKernel
