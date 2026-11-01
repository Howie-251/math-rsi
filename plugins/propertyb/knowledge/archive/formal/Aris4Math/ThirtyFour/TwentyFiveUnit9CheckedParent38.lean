import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows38Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected38 : rows38.map Row.selected=choices (candidates 38) ∅ := by decide +kernel
theorem checked38 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 38))
  (choices (candidates 38) ∅) witnesses38 := by
  rw [← selected38]
  apply checked_rows
  simp only [rows38,List.all_append,TwentyFiveUnit9Rows38Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
