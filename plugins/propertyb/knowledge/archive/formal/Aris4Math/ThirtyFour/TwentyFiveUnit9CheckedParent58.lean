import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows58Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected58 : rows58.map Row.selected=choices (candidates 58) ∅ := by decide +kernel
theorem checked58 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 58))
  (choices (candidates 58) ∅) witnesses58 := by
  rw [← selected58]
  apply checked_rows
  simp only [rows58,List.all_append,TwentyFiveUnit9Rows58Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
