import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows64Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows64Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected64 : rows64.map Row.selected=choices (candidates 64) ∅ := by decide +kernel
theorem checked64 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 64))
  (choices (candidates 64) ∅) witnesses64 := by
  rw [← selected64]
  apply checked_rows
  simp only [rows64,List.all_append,TwentyFiveUnit9Rows64Batch0.checked,TwentyFiveUnit9Rows64Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
