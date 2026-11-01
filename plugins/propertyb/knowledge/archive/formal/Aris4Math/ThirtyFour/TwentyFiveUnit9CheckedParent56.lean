import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows56Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows56Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected56 : rows56.map Row.selected=choices (candidates 56) ∅ := by decide +kernel
theorem checked56 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 56))
  (choices (candidates 56) ∅) witnesses56 := by
  rw [← selected56]
  apply checked_rows
  simp only [rows56,List.all_append,TwentyFiveUnit9Rows56Batch0.checked,TwentyFiveUnit9Rows56Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
