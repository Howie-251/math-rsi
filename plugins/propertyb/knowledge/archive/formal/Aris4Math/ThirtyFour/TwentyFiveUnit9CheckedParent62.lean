import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows62Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows62Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows62Batch2
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows62Batch3
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows62Batch4
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected62 : rows62.map Row.selected=choices (candidates 62) ∅ := by decide +kernel
theorem checked62 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 62))
  (choices (candidates 62) ∅) witnesses62 := by
  rw [← selected62]
  apply checked_rows
  simp only [rows62,List.all_append,TwentyFiveUnit9Rows62Batch0.checked,TwentyFiveUnit9Rows62Batch1.checked,TwentyFiveUnit9Rows62Batch2.checked,TwentyFiveUnit9Rows62Batch3.checked,TwentyFiveUnit9Rows62Batch4.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
