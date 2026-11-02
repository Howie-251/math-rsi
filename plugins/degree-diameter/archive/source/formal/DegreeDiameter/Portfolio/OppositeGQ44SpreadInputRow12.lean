import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputInterface
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices12 : Line → Fin 5 × Fin 5 × Fin 5 := ![(2,0,0), (2,2,2), (1,1,2), (4,4,2), (3,3,2), (4,4,1), (3,3,1), (2,2,1), (1,1,1), (0,0,0), (0,0,0), (2,0,2), (0,0,0), (4,1,4), (2,3,4), (1,4,4), (3,2,4), (1,3,3), (4,2,3), (2,4,3), (3,1,3), (3,3,3), (3,4,3), (3,1,3), (3,2,3), (4,4,4), (4,3,4), (4,2,4), (4,1,4), (0,0,1), (0,0,1), (0,0,1), (0,0,1), (1,1,1), (1,2,1), (1,3,1), (1,4,1), (2,1,2), (2,2,2), (2,3,2), (2,4,2), (2,1,2), (2,2,2), (2,3,2), (2,4,2), (2,1,2), (2,2,2), (2,3,2), (2,4,2), (0,1,0), (0,2,0), (0,3,0), (0,4,0), (0,0,3), (0,0,3), (0,0,3), (0,0,3), (3,2,3), (3,1,3), (3,4,3), (3,3,3), (4,3,4), (4,4,4), (4,1,4), (4,2,4), (1,1,1), (1,2,1), (1,3,1), (1,4,1), (4,2,4), (4,1,4), (4,4,4), (4,3,4), (0,0,4), (0,0,4), (0,0,4), (0,0,4), (3,4,3), (3,3,3), (3,2,3), (3,1,3), (1,1,1), (1,2,1), (1,3,1), (1,4,1)]
theorem projection_check_12 : ProjectionIndexCheck 12 projectionIndices12 := by
  unfold ProjectionIndexCheck
  decide
theorem projection_row_12 : ProjectionRow 12 :=
  projection_row_of_check 12 projectionIndices12 projection_check_12
end DegreeDiameter.Portfolio.OppositeGQ44Spread
