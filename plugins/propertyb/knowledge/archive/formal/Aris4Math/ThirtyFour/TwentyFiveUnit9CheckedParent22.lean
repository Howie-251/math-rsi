import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows22Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows22Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows22Batch2
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows22Batch3
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected22 : rows22.map Row.selected=choices (candidates 22) ∅ := by decide +kernel
theorem checked22 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 22))
  (choices (candidates 22) ∅) witnesses22 := by
  rw [← selected22]
  apply checked_rows
  simp only [rows22,List.all_append,TwentyFiveUnit9Rows22Batch0.checked,TwentyFiveUnit9Rows22Batch1.checked,TwentyFiveUnit9Rows22Batch2.checked,TwentyFiveUnit9Rows22Batch3.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
