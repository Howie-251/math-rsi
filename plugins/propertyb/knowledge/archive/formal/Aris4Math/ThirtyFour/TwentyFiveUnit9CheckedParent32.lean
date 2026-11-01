import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows32Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected32 : rows32.map Row.selected=choices (candidates 32) ∅ := by decide +kernel
theorem checked32 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 32))
  (choices (candidates 32) ∅) witnesses32 := by
  rw [← selected32]
  apply checked_rows
  simp only [rows32,List.all_append,TwentyFiveUnit9Rows32Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
