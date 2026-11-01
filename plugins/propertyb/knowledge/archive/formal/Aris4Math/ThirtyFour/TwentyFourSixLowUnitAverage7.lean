import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Core
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Rows0
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Rows1
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Rows2
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Slots0
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Slots1
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7Slots2
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem rows_exact (l : Layout) : TwentyFourSlotAverageCache.cachedFree (positions l) (p l)=freeValue l ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions l) (p l) j=aValue l j ∧
      TwentyFourSlotAverageCache.cachedC (positions l) (p l) j=cValue l j) := by
  fin_cases l
  · exact rows_0
  · exact rows_1
  · exact rows_2
  · exact rows_3
  · exact rows_4
  · exact rows_5
  · exact rows_6
  · exact rows_7
  · exact rows_8
  · exact rows_9
  · exact rows_10
  · exact rows_11
theorem slots_exact (l : Layout) : ∀s,min (aValue l (slot s).center)
    (cValue l (slot s).center-
      (LocalProfiles.executableWeights positions p l (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p l (slot s).center (slot s).right (slot s).left))=valueValue l s := by
  fin_cases l
  · exact slots_0
  · exact slots_1
  · exact slots_2
  · exact slots_3
  · exact slots_4
  · exact slots_5
  · exact slots_6
  · exact slots_7
  · exact slots_8
  · exact slots_9
  · exact slots_10
  · exact slots_11
theorem free_exact (l : Layout) : free (positions l) (p l)=freeValue l := by
  rw [TwentyFourSlotAverageCache.free_eq _ _ (data_valid.1 l) (data_valid.2.1 l)]
  exact (rows_exact l).1

theorem entry_exact (l : Layout) (s : SlotIndex) : contribution positions p l (slot s)=valueValue l s := by
  rw [TwentyFourSlotAverageCache.contribution_eq _ _ l _ (data_valid.1 l) (data_valid.2.1 l),
    ((rows_exact l).2 _).1,((rows_exact l).2 _).2]
  exact slots_exact l s

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (vertices : Fin 6↪Fin 24)
    (counts : ∀T,Aris4Math.ThirtyThree.MultiLockRecovery.count H vertices T=μ T)
    (degrees : ∀j,H.degree (vertices j)=6)
    (unit : ∀i j,i≠j→H.codegree (vertices i) (vertices j)=1) : PropertyB H := by
  have real (l : Layout) : Aris4Math.TypeCounting.RealizesProfile H vertices (positions l) (p l) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions l) labels labels_nodup mem_labels μ counts
    rw [←p_eq];exact data_valid.1 l
  apply propertyB_of_table H cover vertices μ counts degrees unit positions p real
    data_valid.2.1 data_valid.2.2.1 gamma data_valid.2.2.2.1 data_valid.2.2.2.2
    slot complete valueValue entry_exact centerBound averages.1
  simpa only [free_exact] using averages.2
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7.propertyB_of_counts
