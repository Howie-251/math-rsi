import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Data
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem slots_45 : ∀s,min (aValue 45 (slot s).center)
    (cValue 45 (slot s).center-
      (LocalProfiles.executableWeights positions p 45 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 45 (slot s).center (slot s).right (slot s).left))=valueValue 45 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_46 : ∀s,min (aValue 46 (slot s).center)
    (cValue 46 (slot s).center-
      (LocalProfiles.executableWeights positions p 46 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 46 (slot s).center (slot s).right (slot s).left))=valueValue 46 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_47 : ∀s,min (aValue 47 (slot s).center)
    (cValue 47 (slot s).center-
      (LocalProfiles.executableWeights positions p 47 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 47 (slot s).center (slot s).right (slot s).left))=valueValue 47 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
