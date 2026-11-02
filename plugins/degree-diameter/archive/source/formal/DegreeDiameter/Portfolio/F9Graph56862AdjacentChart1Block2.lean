import Mathlib.Logic.Equiv.Fin.Basic
import DegreeDiameter.Portfolio.F9Graph56862RouteData
namespace DegreeDiameter.Portfolio.F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem adjacent_chart_1_block_2 : ∀ j : Fin 243,
    let d := (finProdFinEquiv (m:=3) (n:=243)) ((2 : Fin 3),j)
    planeNoise 1 d = decodeVec d := by decide +kernel
#print axioms adjacent_chart_1_block_2
end DegreeDiameter.Portfolio.F9Graph56862
