import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows21Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows21Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected21 : rows21.map Row.selected=choices (candidates 21) ∅ := by decide +kernel
theorem checked21 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 21))
  (choices (candidates 21) ∅) witnesses21 := by
  rw [← selected21]
  apply checked_rows
  simp only [rows21,List.all_append,TwentyFiveUnit9Rows21Batch0.checked,TwentyFiveUnit9Rows21Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
