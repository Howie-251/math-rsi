import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows57Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows57Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected57 : rows57.map Row.selected=choices (candidates 57) ∅ := by decide +kernel
theorem checked57 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 57))
  (choices (candidates 57) ∅) witnesses57 := by
  rw [← selected57]
  apply checked_rows
  simp only [rows57,List.all_append,TwentyFiveUnit9Rows57Batch0.checked,TwentyFiveUnit9Rows57Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
