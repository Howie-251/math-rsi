import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows28Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows28Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected28 : rows28.map Row.selected=choices (candidates 28) ∅ := by decide +kernel
theorem checked28 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 28))
  (choices (candidates 28) ∅) witnesses28 := by
  rw [← selected28]
  apply checked_rows
  simp only [rows28,List.all_append,TwentyFiveUnit9Rows28Batch0.checked,TwentyFiveUnit9Rows28Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
