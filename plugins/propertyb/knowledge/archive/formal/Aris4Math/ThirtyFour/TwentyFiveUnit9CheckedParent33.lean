import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows33Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows33Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected33 : rows33.map Row.selected=choices (candidates 33) ∅ := by decide +kernel
theorem checked33 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 33))
  (choices (candidates 33) ∅) witnesses33 := by
  rw [← selected33]
  apply checked_rows
  simp only [rows33,List.all_append,TwentyFiveUnit9Rows33Batch0.checked,TwentyFiveUnit9Rows33Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
