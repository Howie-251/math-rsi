import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows17Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected17 : rows17.map Row.selected=choices (candidates 17) ∅ := by decide +kernel
theorem checked17 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 17))
  (choices (candidates 17) ∅) witnesses17 := by
  rw [← selected17]
  apply checked_rows
  simp only [rows17,List.all_append,TwentyFiveUnit9Rows17Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
