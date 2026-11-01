import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows53Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected53 : rows53.map Row.selected=choices (candidates 53) ∅ := by decide +kernel
theorem checked53 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 53))
  (choices (candidates 53) ∅) witnesses53 := by
  rw [← selected53]
  apply checked_rows
  simp only [rows53,List.all_append,TwentyFiveUnit9Rows53Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
