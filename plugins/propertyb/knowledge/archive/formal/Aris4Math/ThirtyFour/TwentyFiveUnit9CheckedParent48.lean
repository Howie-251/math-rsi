import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows48Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows48Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected48 : rows48.map Row.selected=choices (candidates 48) ∅ := by decide +kernel
theorem checked48 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 48))
  (choices (candidates 48) ∅) witnesses48 := by
  rw [← selected48]
  apply checked_rows
  simp only [rows48,List.all_append,TwentyFiveUnit9Rows48Batch0.checked,TwentyFiveUnit9Rows48Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
