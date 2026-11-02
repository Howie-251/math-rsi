import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputInterface
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices01 : Line → Fin 5 × Fin 5 × Fin 5 := ![(1,0,1), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,1,0), (0,2,0), (0,3,0), (0,4,0), (0,0,2), (0,0,2), (0,0,2), (0,0,2), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,4), (0,0,4), (0,0,4), (0,0,4), (1,1,1), (1,2,2), (1,3,3), (1,4,4), (1,2,1), (1,1,2), (1,4,3), (1,3,4), (1,3,1), (1,4,2), (1,1,3), (1,2,4), (1,4,1), (1,3,2), (1,2,3), (1,1,4), (1,1,1), (1,2,2), (1,3,3), (1,4,4), (1,2,1), (1,1,2), (1,4,3), (1,3,4), (1,3,1), (1,4,2), (1,1,3), (1,2,4), (1,4,1), (1,3,2), (1,2,3), (1,1,4), (1,1,1), (1,2,2), (1,3,3), (1,4,4), (1,2,1), (1,1,2), (1,4,3), (1,3,4), (1,3,1), (1,4,2), (1,1,3), (1,2,4), (1,4,1), (1,3,2), (1,2,3), (1,1,4), (1,1,1), (1,2,2), (1,3,3), (1,4,4), (1,2,1), (1,1,2), (1,4,3), (1,3,4), (1,3,1), (1,4,2), (1,1,3), (1,2,4), (1,4,1), (1,3,2), (1,2,3), (1,1,4)]
theorem projection_check_01 : ProjectionIndexCheck 1 projectionIndices01 := by
  unfold ProjectionIndexCheck
  decide
theorem projection_row_01 : ProjectionRow 1 :=
  projection_row_of_check 1 projectionIndices01 projection_check_01
end DegreeDiameter.Portfolio.OppositeGQ44Spread
