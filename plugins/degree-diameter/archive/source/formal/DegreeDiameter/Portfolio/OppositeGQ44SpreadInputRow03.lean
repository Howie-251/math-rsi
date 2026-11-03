import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputInterface
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices03 : Line → Fin 5 × Fin 5 × Fin 5 := ![(3,0,3), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,1), (0,0,1), (0,0,1), (0,0,1), (0,0,2), (0,0,2), (0,0,2), (0,0,2), (0,1,0), (0,2,0), (0,3,0), (0,4,0), (0,0,4), (0,0,4), (0,0,4), (0,0,4), (4,1,1), (4,4,2), (4,2,3), (4,3,4), (4,3,1), (4,2,2), (4,4,3), (4,1,4), (4,4,1), (4,1,2), (4,3,3), (4,2,4), (4,2,1), (4,3,2), (4,1,3), (4,4,4), (4,2,4), (4,3,3), (4,1,2), (4,4,1), (4,4,4), (4,1,3), (4,3,2), (4,2,1), (4,3,4), (4,2,3), (4,4,2), (4,1,1), (4,1,4), (4,4,3), (4,2,2), (4,3,1), (4,3,2), (4,2,1), (4,4,4), (4,1,3), (4,1,2), (4,4,1), (4,2,4), (4,3,3), (4,2,2), (4,3,1), (4,1,4), (4,4,3), (4,4,2), (4,1,1), (4,3,4), (4,2,3), (4,4,3), (4,1,4), (4,3,1), (4,2,2), (4,2,3), (4,3,4), (4,1,1), (4,4,2), (4,1,3), (4,4,4), (4,2,1), (4,3,2), (4,3,3), (4,2,4), (4,4,1), (4,1,2)]
theorem projection_check_03 : ProjectionIndexCheck 3 projectionIndices03 := by
  unfold ProjectionIndexCheck
  decide
theorem projection_row_03 : ProjectionRow 3 :=
  projection_row_of_check 3 projectionIndices03 projection_check_03
end DegreeDiameter.Portfolio.OppositeGQ44Spread
