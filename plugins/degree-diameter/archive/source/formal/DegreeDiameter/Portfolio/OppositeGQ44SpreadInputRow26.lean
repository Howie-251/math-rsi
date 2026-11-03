import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputInterface
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices26 : Line → Fin 5 × Fin 5 × Fin 5 := ![(1,0,0), (2,2,2), (2,1,2), (2,4,2), (2,3,2), (0,0,0), (2,0,2), (0,0,0), (0,0,0), (1,1,0), (2,2,0), (3,3,0), (4,4,0), (4,4,4), (1,3,4), (3,2,4), (2,1,4), (3,3,3), (1,4,3), (2,1,3), (4,2,3), (0,1,0), (1,1,1), (0,1,0), (0,1,0), (1,0,1), (2,1,2), (3,3,3), (4,4,4), (3,4,3), (2,1,2), (4,2,4), (1,0,4), (4,3,4), (2,1,2), (1,0,3), (3,2,3), (0,2,0), (1,2,1), (0,2,0), (0,2,0), (1,0,1), (2,2,2), (3,4,3), (4,3,4), (3,3,3), (2,2,2), (4,1,4), (1,0,4), (4,4,4), (2,2,2), (1,0,3), (3,1,3), (0,3,0), (1,3,1), (0,3,0), (0,3,0), (1,0,1), (2,3,2), (3,1,3), (4,2,4), (3,2,3), (2,3,2), (4,4,4), (1,0,4), (4,1,4), (2,3,2), (1,0,3), (3,4,3), (0,4,0), (1,4,1), (0,4,0), (0,4,0), (1,0,1), (2,4,2), (3,2,3), (4,1,4), (3,1,3), (2,4,2), (4,3,4), (1,0,4), (4,2,4), (2,4,2), (1,0,3), (3,3,3)]
theorem projection_check_26 : ProjectionIndexCheck 26 projectionIndices26 := by
  unfold ProjectionIndexCheck
  decide
theorem projection_row_26 : ProjectionRow 26 :=
  projection_row_of_check 26 projectionIndices26 projection_check_26
end DegreeDiameter.Portfolio.OppositeGQ44Spread
