import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage4Data
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage4
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem slots_5 : ∀s,min (aValue 5 (slot s).center)
    (cValue 5 (slot s).center-
      (LocalProfiles.executableWeights positions p 5 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 5 (slot s).center (slot s).right (slot s).left))=valueValue 5 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_6 : ∀s,min (aValue 6 (slot s).center)
    (cValue 6 (slot s).center-
      (LocalProfiles.executableWeights positions p 6 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 6 (slot s).center (slot s).right (slot s).left))=valueValue 6 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_7 : ∀s,min (aValue 7 (slot s).center)
    (cValue 7 (slot s).center-
      (LocalProfiles.executableWeights positions p 7 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 7 (slot s).center (slot s).right (slot s).left))=valueValue 7 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_8 : ∀s,min (aValue 8 (slot s).center)
    (cValue 8 (slot s).center-
      (LocalProfiles.executableWeights positions p 8 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 8 (slot s).center (slot s).right (slot s).left))=valueValue 8 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_9 : ∀s,min (aValue 9 (slot s).center)
    (cValue 9 (slot s).center-
      (LocalProfiles.executableWeights positions p 9 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 9 (slot s).center (slot s).right (slot s).left))=valueValue 9 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage4
