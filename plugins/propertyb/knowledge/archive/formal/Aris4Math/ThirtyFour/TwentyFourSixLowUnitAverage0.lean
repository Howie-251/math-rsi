import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Rows
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Profile
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Core
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots0
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots1
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots2
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots3
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots4
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots5
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots6
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots7
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots8
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots9
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots10
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots11
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots12
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots13
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots14
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots15
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots16
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots17
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots18
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots19
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots20
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots21
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots22
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0Slots23
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0
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
  · exact slots_48
  · exact slots_49
  · exact slots_50
  · exact slots_51
  · exact slots_52
  · exact slots_53
  · exact slots_54
  · exact slots_55
  · exact slots_56
  · exact slots_57
  · exact slots_58
  · exact slots_59
  · exact slots_60
  · exact slots_61
  · exact slots_62
  · exact slots_63
  · exact slots_64
  · exact slots_65
  · exact slots_66
  · exact slots_67
  · exact slots_68
  · exact slots_69
  · exact slots_70
  · exact slots_71
  · exact slots_72
  · exact slots_73
  · exact slots_74
  · exact slots_75
  · exact slots_76
  · exact slots_77
  · exact slots_78
  · exact slots_79
  · exact slots_80
  · exact slots_81
  · exact slots_82
  · exact slots_83
  · exact slots_84
  · exact slots_85
  · exact slots_86
  · exact slots_87
  · exact slots_88
  · exact slots_89
  · exact slots_90
  · exact slots_91
  · exact slots_92
  · exact slots_93
  · exact slots_94
  · exact slots_95
  · exact slots_96
  · exact slots_97
  · exact slots_98
  · exact slots_99
  · exact slots_100
  · exact slots_101
  · exact slots_102
  · exact slots_103
  · exact slots_104
  · exact slots_105
  · exact slots_106
  · exact slots_107
  · exact slots_108
  · exact slots_109
  · exact slots_110
  · exact slots_111
  · exact slots_112
  · exact slots_113
  · exact slots_114
  · exact slots_115
  · exact slots_116
  · exact slots_117
  · exact slots_118
  · exact slots_119
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
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0.propertyB_of_counts
