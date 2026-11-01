import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows50Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows50Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected50 : rows50.map Row.selected=choices (candidates 50) ∅ := by decide +kernel
theorem checked50 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 50))
  (choices (candidates 50) ∅) witnesses50 := by
  rw [← selected50]
  apply checked_rows
  simp only [rows50,List.all_append,TwentyFiveUnit9Rows50Batch0.checked,TwentyFiveUnit9Rows50Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
