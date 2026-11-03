import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputChecks
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices00 : Line → Fin 4 × Fin 4 × Fin 4 := ![(0,0,0), (0,0,1), (0,0,2), (0,0,3), (0,0,1), (0,0,1), (0,0,1), (0,0,1), (0,0,2), (0,0,2), (0,0,2), (0,0,2), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,1), (0,0,1), (0,0,1), (0,0,1), (0,0,1), (0,0,2), (0,0,2), (0,0,2), (0,0,2), (0,0,2), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,1), (0,0,1), (0,0,1), (0,0,1), (1,0,1), (1,0,1), (1,0,1), (1,0,1), (2,0,2), (2,0,2), (2,0,2), (2,0,2), (3,0,3), (3,0,3), (3,0,3), (3,0,3), (0,0,2), (0,0,2), (0,0,2), (0,0,2), (3,0,3), (3,0,3), (3,0,3), (3,0,3), (1,0,1), (1,0,1), (1,0,1), (1,0,1), (2,0,2), (2,0,2), (2,0,2), (2,0,2), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (2,0,2), (2,0,2), (2,0,2), (2,0,2), (3,0,3), (3,0,3), (3,0,3), (3,0,3), (1,0,1), (1,0,1), (1,0,1), (1,0,1), (0,0,1), (1,0,1), (2,0,1), (3,0,1), (0,0,2), (3,0,2), (1,0,2), (2,0,2), (0,0,3), (2,0,3), (3,0,3), (1,0,3)]
theorem projection_check_00 : ProjectionIndexCheck 0 projectionIndices00 := by
  unfold ProjectionIndexCheck
  decide
theorem input_row_00 : InputRow 0 :=
  inputRow_of_checks 0 projectionIndices00 projection_check_00
end DegreeDiameter.Portfolio.OppositeGQ35Spread
