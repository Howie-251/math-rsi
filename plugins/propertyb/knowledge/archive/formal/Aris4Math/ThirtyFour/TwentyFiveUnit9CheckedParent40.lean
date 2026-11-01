import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows40Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows40Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows40Batch2
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected40 : rows40.map Row.selected=choices (candidates 40) ∅ := by decide +kernel
theorem checked40 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 40))
  (choices (candidates 40) ∅) witnesses40 := by
  rw [← selected40]
  apply checked_rows
  simp only [rows40,List.all_append,TwentyFiveUnit9Rows40Batch0.checked,TwentyFiveUnit9Rows40Batch1.checked,TwentyFiveUnit9Rows40Batch2.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
