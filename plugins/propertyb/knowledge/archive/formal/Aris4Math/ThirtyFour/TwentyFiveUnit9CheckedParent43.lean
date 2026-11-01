import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows43Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected43 : rows43.map Row.selected=choices (candidates 43) ∅ := by decide +kernel
theorem checked43 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 43))
  (choices (candidates 43) ∅) witnesses43 := by
  rw [← selected43]
  apply checked_rows
  simp only [rows43,List.all_append,TwentyFiveUnit9Rows43Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
