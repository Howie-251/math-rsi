import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Data
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem slots_10 : ∀s,min (aValue 10 (slot s).center)
    (cValue 10 (slot s).center-
      (LocalProfiles.executableWeights positions p 10 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 10 (slot s).center (slot s).right (slot s).left))=valueValue 10 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_11 : ∀s,min (aValue 11 (slot s).center)
    (cValue 11 (slot s).center-
      (LocalProfiles.executableWeights positions p 11 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 11 (slot s).center (slot s).right (slot s).left))=valueValue 11 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
