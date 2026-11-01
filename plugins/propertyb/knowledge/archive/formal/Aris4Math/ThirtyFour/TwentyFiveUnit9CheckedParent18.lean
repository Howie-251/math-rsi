import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows18Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows18Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected18 : rows18.map Row.selected=choices (candidates 18) ∅ := by decide +kernel
theorem checked18 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 18))
  (choices (candidates 18) ∅) witnesses18 := by
  rw [← selected18]
  apply checked_rows
  simp only [rows18,List.all_append,TwentyFiveUnit9Rows18Batch0.checked,TwentyFiveUnit9Rows18Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
