import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows37Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows37Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected37 : rows37.map Row.selected=choices (candidates 37) ∅ := by decide +kernel
theorem checked37 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 37))
  (choices (candidates 37) ∅) witnesses37 := by
  rw [← selected37]
  apply checked_rows
  simp only [rows37,List.all_append,TwentyFiveUnit9Rows37Batch0.checked,TwentyFiveUnit9Rows37Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
