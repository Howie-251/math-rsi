import Aris4Math.ThirtyThree.TwentyFourMixedData
open Aris4Math.ThirtyThree.TwentyFourMixedData
def loss (r : Row) (k : ℕ) : ℚ :=
  if k = (positions (configOf r) 0).val+1 then rowLoss r 0 else
  if k = (positions (configOf r) 1).val+1 then rowLoss r 1 else
  if k = (positions (configOf r) 2).val+1 then rowLoss r 2 else
  if k = (positions (configOf r) 3).val+1 then rowLoss r 3 else
  if k = (positions (configOf r) 4).val+1 then rowLoss r 4 else 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem loss_at : ∀ r : Row, ∀ j : Fin 5,
    loss r ((positions (configOf r) j).val+1) = rowLoss r j := by
  decide +kernel

