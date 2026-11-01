import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows42Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows42Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected42 : rows42.map Row.selected=choices (candidates 42) ∅ := by decide +kernel
theorem checked42 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 42))
  (choices (candidates 42) ∅) witnesses42 := by
  rw [← selected42]
  apply checked_rows
  simp only [rows42,List.all_append,TwentyFiveUnit9Rows42Batch0.checked,TwentyFiveUnit9Rows42Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
