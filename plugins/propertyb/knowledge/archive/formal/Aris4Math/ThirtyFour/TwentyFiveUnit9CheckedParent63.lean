import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows63Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows63Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows63Batch2
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected63 : rows63.map Row.selected=choices (candidates 63) ∅ := by decide +kernel
theorem checked63 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 63))
  (choices (candidates 63) ∅) witnesses63 := by
  rw [← selected63]
  apply checked_rows
  simp only [rows63,List.all_append,TwentyFiveUnit9Rows63Batch0.checked,TwentyFiveUnit9Rows63Batch1.checked,TwentyFiveUnit9Rows63Batch2.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
