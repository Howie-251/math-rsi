import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows41Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows41Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected41 : rows41.map Row.selected=choices (candidates 41) ∅ := by decide +kernel
theorem checked41 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 41))
  (choices (candidates 41) ∅) witnesses41 := by
  rw [← selected41]
  apply checked_rows
  simp only [rows41,List.all_append,TwentyFiveUnit9Rows41Batch0.checked,TwentyFiveUnit9Rows41Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
