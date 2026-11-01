import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows11Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected11 : rows11.map Row.selected=choices (candidates 11) ∅ := by decide +kernel
theorem checked11 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 11))
  (choices (candidates 11) ∅) witnesses11 := by
  rw [← selected11]
  apply checked_rows
  simp only [rows11,List.all_append,TwentyFiveUnit9Rows11Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
