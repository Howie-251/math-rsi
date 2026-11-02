import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputChecks
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices63 : Line → Fin 4 × Fin 4 × Fin 4 := ![(3,3,0), (0,3,0), (2,3,0), (1,3,0), (0,3,1), (3,3,1), (1,3,1), (2,3,1), (2,3,2), (1,3,2), (3,3,2), (0,3,2), (1,3,0), (2,3,1), (0,3,2), (0,3,0), (1,3,0), (1,3,1), (3,3,0), (2,3,2), (3,3,2), (3,3,0), (3,3,0), (3,3,1), (1,3,1), (2,3,2), (2,3,0), (2,3,2), (3,3,2), (3,3,1), (1,3,1), (0,3,0), (0,3,0), (0,3,0), (0,3,0), (0,3,0), (0,3,0), (0,3,0), (0,3,0), (0,3,0), (1,3,1), (3,3,1), (3,3,2), (2,3,2), (2,3,2), (1,3,1), (3,3,1), (3,3,0), (3,3,2), (2,3,2), (3,3,0), (1,3,1), (3,3,1), (3,3,0), (2,3,2), (1,3,1), (3,3,0), (1,3,1), (3,3,2), (2,3,2), (0,3,0), (0,3,0), (0,3,0), (0,3,0), (3,3,2), (2,3,2), (1,3,1), (3,3,1), (3,3,1), (1,3,1), (2,3,2), (3,3,2), (0,3,0), (0,3,0), (0,3,0), (0,3,0), (2,3,2), (3,3,2), (1,3,1), (3,3,0), (1,3,1), (2,3,2), (3,3,0), (3,3,1), (0,3,1), (3,3,1), (1,3,1), (2,3,1), (2,3,2), (3,3,2), (0,3,2), (1,3,2), (3,3,2), (0,3,0), (3,3,0), (3,3,1)]
theorem projection_check_63 : ProjectionIndexCheck 63 projectionIndices63 := by
  unfold ProjectionIndexCheck
  decide
theorem input_row_63 : InputRow 63 :=
  inputRow_of_checks 63 projectionIndices63 projection_check_63
end DegreeDiameter.Portfolio.OppositeGQ35Spread
