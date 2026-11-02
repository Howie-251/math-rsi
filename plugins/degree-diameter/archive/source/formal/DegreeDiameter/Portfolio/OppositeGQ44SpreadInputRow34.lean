import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputInterface
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices34 : Line → Fin 5 × Fin 5 × Fin 5 := ![(1,0,0), (4,4,2), (4,3,2), (4,2,2), (4,1,2), (0,0,0), (4,0,4), (0,0,0), (0,0,0), (3,3,0), (4,4,0), (1,1,0), (2,2,0), (1,2,4), (4,1,4), (2,4,4), (3,3,4), (4,1,3), (2,2,3), (1,3,3), (3,4,3), (4,2,4), (1,0,2), (3,4,3), (2,1,2), (1,0,1), (3,2,3), (4,3,4), (2,1,2), (0,1,0), (0,1,0), (0,1,0), (1,1,1), (3,3,3), (4,4,4), (1,0,3), (2,1,2), (4,1,4), (1,0,2), (3,3,3), (2,2,2), (1,0,1), (3,1,3), (4,4,4), (2,2,2), (0,2,0), (0,2,0), (0,2,0), (1,2,1), (3,4,3), (4,3,4), (1,0,3), (2,2,2), (4,4,4), (1,0,2), (3,2,3), (2,3,2), (1,0,1), (3,4,3), (4,1,4), (2,3,2), (0,3,0), (0,3,0), (0,3,0), (1,3,1), (3,1,3), (4,2,4), (1,0,3), (2,3,2), (4,3,4), (1,0,2), (3,1,3), (2,4,2), (1,0,1), (3,3,3), (4,2,4), (2,4,2), (0,4,0), (0,4,0), (0,4,0), (1,4,1), (3,2,3), (4,1,4), (1,0,3), (2,4,2)]
theorem projection_check_34 : ProjectionIndexCheck 34 projectionIndices34 := by
  unfold ProjectionIndexCheck
  decide
theorem projection_row_34 : ProjectionRow 34 :=
  projection_row_of_check 34 projectionIndices34 projection_check_34
end DegreeDiameter.Portfolio.OppositeGQ44Spread
