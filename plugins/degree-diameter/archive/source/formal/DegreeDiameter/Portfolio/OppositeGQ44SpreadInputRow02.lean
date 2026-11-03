import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputInterface
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices02 : Line → Fin 5 × Fin 5 × Fin 5 := ![(2,0,2), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,1), (0,0,1), (0,0,1), (0,0,1), (0,1,0), (0,2,0), (0,3,0), (0,4,0), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (0,0,4), (0,0,4), (0,0,4), (0,0,4), (0,1,1), (0,1,1), (0,1,1), (0,1,1), (0,2,1), (0,2,1), (0,2,1), (0,2,1), (0,3,1), (0,3,1), (0,3,1), (0,3,1), (0,4,1), (0,4,1), (0,4,1), (0,4,1), (0,2,2), (0,2,2), (0,2,2), (0,2,2), (0,1,2), (0,1,2), (0,1,2), (0,1,2), (0,4,2), (0,4,2), (0,4,2), (0,4,2), (0,3,2), (0,3,2), (0,3,2), (0,3,2), (0,3,3), (0,3,3), (0,3,3), (0,3,3), (0,4,3), (0,4,3), (0,4,3), (0,4,3), (0,1,3), (0,1,3), (0,1,3), (0,1,3), (0,2,3), (0,2,3), (0,2,3), (0,2,3), (0,4,4), (0,4,4), (0,4,4), (0,4,4), (0,3,4), (0,3,4), (0,3,4), (0,3,4), (0,2,4), (0,2,4), (0,2,4), (0,2,4), (0,1,4), (0,1,4), (0,1,4), (0,1,4)]
theorem projection_check_02 : ProjectionIndexCheck 2 projectionIndices02 := by
  unfold ProjectionIndexCheck
  decide
theorem projection_row_02 : ProjectionRow 2 :=
  projection_row_of_check 2 projectionIndices02 projection_check_02
end DegreeDiameter.Portfolio.OppositeGQ44Spread
