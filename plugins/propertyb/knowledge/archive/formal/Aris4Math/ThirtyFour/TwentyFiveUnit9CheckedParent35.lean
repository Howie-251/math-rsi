import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows35Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected35 : rows35.map Row.selected=choices (candidates 35) ∅ := by decide +kernel
theorem checked35 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 35))
  (choices (candidates 35) ∅) witnesses35 := by
  rw [← selected35]
  apply checked_rows
  simp only [rows35,List.all_append,TwentyFiveUnit9Rows35Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
