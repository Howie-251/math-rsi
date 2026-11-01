import Aris4Math.ThirtyFour.TwentyFiveUnit7Data
namespace Aris4Math.ThirtyFour.TwentyFiveUnit7Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnit7Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked0 : List.Forall₂ (Checks catalogue (Aris4Math.K6Classification.representative 0))
  (choices (candidates 0) ∅) witnesses0 := by decide +kernel
theorem checked1 : List.Forall₂ (Checks catalogue (Aris4Math.K6Classification.representative 1))
  (choices (candidates 1) ∅) witnesses1 := by decide +kernel
theorem checked2 : List.Forall₂ (Checks catalogue (Aris4Math.K6Classification.representative 2))
  (choices (candidates 2) ∅) witnesses2 := by decide +kernel
theorem checked3 : List.Forall₂ (Checks catalogue (Aris4Math.K6Classification.representative 3))
  (choices (candidates 3) ∅) witnesses3 := by decide +kernel
theorem checked4 : List.Forall₂ (Checks catalogue (Aris4Math.K6Classification.representative 4))
  (choices (candidates 4) ∅) witnesses4 := by decide +kernel
theorem checked5 : List.Forall₂ (Checks catalogue (Aris4Math.K6Classification.representative 5))
  (choices (candidates 5) ∅) witnesses5 := by decide +kernel
theorem checked6 : List.Forall₂ (Checks catalogue (Aris4Math.K6Classification.representative 6))
  (choices (candidates 6) ∅) witnesses6 := by decide +kernel
theorem checked7 : List.Forall₂ (Checks catalogue (Aris4Math.K6Classification.representative 7))
  (choices (candidates 7) ∅) witnesses7 := by decide +kernel
theorem checked8 : List.Forall₂ (Checks catalogue (Aris4Math.K6Classification.representative 8))
  (choices (candidates 8) ∅) witnesses8 := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveUnit7Checked
