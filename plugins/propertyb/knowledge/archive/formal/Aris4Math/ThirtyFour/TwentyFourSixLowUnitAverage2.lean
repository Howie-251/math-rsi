import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Core
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows0
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows1
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows2
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows3
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows4
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows5
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows6
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows7
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows8
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Rows9
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots0
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots1
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots2
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots3
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots4
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots5
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots6
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots7
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots8
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2Slots9
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
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
  · exact rows_12
  · exact rows_13
  · exact rows_14
  · exact rows_15
  · exact rows_16
  · exact rows_17
  · exact rows_18
  · exact rows_19
  · exact rows_20
  · exact rows_21
  · exact rows_22
  · exact rows_23
  · exact rows_24
  · exact rows_25
  · exact rows_26
  · exact rows_27
  · exact rows_28
  · exact rows_29
  · exact rows_30
  · exact rows_31
  · exact rows_32
  · exact rows_33
  · exact rows_34
  · exact rows_35
  · exact rows_36
  · exact rows_37
  · exact rows_38
  · exact rows_39
  · exact rows_40
  · exact rows_41
  · exact rows_42
  · exact rows_43
  · exact rows_44
  · exact rows_45
  · exact rows_46
  · exact rows_47
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
  · exact slots_12
  · exact slots_13
  · exact slots_14
  · exact slots_15
  · exact slots_16
  · exact slots_17
  · exact slots_18
  · exact slots_19
  · exact slots_20
  · exact slots_21
  · exact slots_22
  · exact slots_23
  · exact slots_24
  · exact slots_25
  · exact slots_26
  · exact slots_27
  · exact slots_28
  · exact slots_29
  · exact slots_30
  · exact slots_31
  · exact slots_32
  · exact slots_33
  · exact slots_34
  · exact slots_35
  · exact slots_36
  · exact slots_37
  · exact slots_38
  · exact slots_39
  · exact slots_40
  · exact slots_41
  · exact slots_42
  · exact slots_43
  · exact slots_44
  · exact slots_45
  · exact slots_46
  · exact slots_47
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
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2.propertyB_of_counts
