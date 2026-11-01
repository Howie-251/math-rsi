import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows2Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows2Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected2 : rows2.map Row.selected=choices (candidates 2) ∅ := by decide +kernel
theorem checked2 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 2))
  (choices (candidates 2) ∅) witnesses2 := by
  rw [← selected2]
  apply checked_rows
  simp only [rows2,List.all_append,TwentyFiveUnit9Rows2Batch0.checked,TwentyFiveUnit9Rows2Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
