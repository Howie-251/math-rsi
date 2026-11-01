import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows52Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows52Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected52 : rows52.map Row.selected=choices (candidates 52) ∅ := by decide +kernel
theorem checked52 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 52))
  (choices (candidates 52) ∅) witnesses52 := by
  rw [← selected52]
  apply checked_rows
  simp only [rows52,List.all_append,TwentyFiveUnit9Rows52Batch0.checked,TwentyFiveUnit9Rows52Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
