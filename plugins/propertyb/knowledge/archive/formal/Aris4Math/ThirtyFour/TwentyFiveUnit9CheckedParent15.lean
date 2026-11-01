import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows15Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows15Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected15 : rows15.map Row.selected=choices (candidates 15) ∅ := by decide +kernel
theorem checked15 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 15))
  (choices (candidates 15) ∅) witnesses15 := by
  rw [← selected15]
  apply checked_rows
  simp only [rows15,List.all_append,TwentyFiveUnit9Rows15Batch0.checked,TwentyFiveUnit9Rows15Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
