import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Data
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem slots_40 : ∀s,min (aValue 40 (slot s).center)
    (cValue 40 (slot s).center-
      (LocalProfiles.executableWeights positions p 40 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 40 (slot s).center (slot s).right (slot s).left))=valueValue 40 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_41 : ∀s,min (aValue 41 (slot s).center)
    (cValue 41 (slot s).center-
      (LocalProfiles.executableWeights positions p 41 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 41 (slot s).center (slot s).right (slot s).left))=valueValue 41 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_42 : ∀s,min (aValue 42 (slot s).center)
    (cValue 42 (slot s).center-
      (LocalProfiles.executableWeights positions p 42 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 42 (slot s).center (slot s).right (slot s).left))=valueValue 42 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_43 : ∀s,min (aValue 43 (slot s).center)
    (cValue 43 (slot s).center-
      (LocalProfiles.executableWeights positions p 43 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 43 (slot s).center (slot s).right (slot s).left))=valueValue 43 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel

theorem slots_44 : ∀s,min (aValue 44 (slot s).center)
    (cValue 44 (slot s).center-
      (LocalProfiles.executableWeights positions p 44 (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p 44 (slot s).center (slot s).right (slot s).left))=valueValue 44 s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
