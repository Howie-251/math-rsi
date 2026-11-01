import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows55Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows55Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows55Batch2
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected55 : rows55.map Row.selected=choices (candidates 55) ∅ := by decide +kernel
theorem checked55 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 55))
  (choices (candidates 55) ∅) witnesses55 := by
  rw [← selected55]
  apply checked_rows
  simp only [rows55,List.all_append,TwentyFiveUnit9Rows55Batch0.checked,TwentyFiveUnit9Rows55Batch1.checked,TwentyFiveUnit9Rows55Batch2.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
