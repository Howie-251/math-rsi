import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows19Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows19Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected19 : rows19.map Row.selected=choices (candidates 19) ∅ := by decide +kernel
theorem checked19 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 19))
  (choices (candidates 19) ∅) witnesses19 := by
  rw [← selected19]
  apply checked_rows
  simp only [rows19,List.all_append,TwentyFiveUnit9Rows19Batch0.checked,TwentyFiveUnit9Rows19Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
