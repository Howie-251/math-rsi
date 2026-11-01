import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Data
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem data_valid :
    (∀l,Numeric.validProfile (p l) 34) ∧ (∀l,(p l).emptyPairCap=none) ∧
    (∀l j,(positions l j).val+1∈(p l).correctionCenters) ∧
    (∀l,0≤gamma l) ∧ (∑l,gamma l)=1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

theorem positive_complete : ∀T,0<μ T→∃t,positive t=T := by decide +kernel

theorem complete_positive : ∀j t u,Admissible μ j (positive t) (positive u)→∃s,
    (slot s).center=j ∧
    (((slot s).left=positive t ∧ (slot s).right=positive u) ∨
     ((slot s).left=positive u ∧ (slot s).right=positive t)) := by
  intro j;fin_cases j <;> decide +kernel

theorem complete : ∀j T U,Admissible μ j T U→∃s,
    (slot s).center=j ∧
    (((slot s).left=T ∧ (slot s).right=U) ∨
     ((slot s).left=U ∧ (slot s).right=T)) := by
  intro j T U h
  obtain ⟨t,rfl⟩ := positive_complete T h.2.1
  obtain ⟨u,rfl⟩ := positive_complete U h.2.2.1
  exact complete_positive j t u h

theorem averages : (∀s,(∑l,gamma l*valueValue l s)≤centerBound (slot s).center) ∧
    (∑l,gamma l*freeValue l)+(∑j,centerBound j)<1 := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
