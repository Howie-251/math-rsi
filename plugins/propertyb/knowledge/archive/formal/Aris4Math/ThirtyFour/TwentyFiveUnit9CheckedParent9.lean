import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows9Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows9Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected9 : rows9.map Row.selected=choices (candidates 9) ∅ := by decide +kernel
theorem checked9 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 9))
  (choices (candidates 9) ∅) witnesses9 := by
  rw [← selected9]
  apply checked_rows
  simp only [rows9,List.all_append,TwentyFiveUnit9Rows9Batch0.checked,TwentyFiveUnit9Rows9Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
