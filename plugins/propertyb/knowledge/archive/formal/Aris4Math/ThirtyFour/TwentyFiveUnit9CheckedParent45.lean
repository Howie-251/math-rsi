import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows45Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows45Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected45 : rows45.map Row.selected=choices (candidates 45) ∅ := by decide +kernel
theorem checked45 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 45))
  (choices (candidates 45) ∅) witnesses45 := by
  rw [← selected45]
  apply checked_rows
  simp only [rows45,List.all_append,TwentyFiveUnit9Rows45Batch0.checked,TwentyFiveUnit9Rows45Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
