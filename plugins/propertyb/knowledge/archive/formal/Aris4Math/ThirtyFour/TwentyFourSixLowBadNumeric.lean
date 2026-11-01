import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases0
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases1
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases2
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases3
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases4
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases5
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases6
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases7
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases8
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases9
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases10
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases11
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases12
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases13
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases14
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases15
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases16
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases17
import Aris4Math.ThirtyFour.TwentyFourSixLowBadNumericCases18
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cachedCertificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧ (p i).emptyPairCap=none ∧
    (∀ j, (positions i j).val+1∈(p i).correctionCenters) ∧
    (∀ j z, 0≤α i j z) ∧ (∀ j z, j∉R i j z) ∧
    (∀ j z, quota i j z ≤
      (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (R i j z))+2-
        (24-1-(R i j z).card))/3) ∧
    (∀ j, loss i j ≤ (∑ z, (quota i j z : ℚ)*α i j z)-
      penaltySum (p i) ((positions i j).val+1) (fun z => avoidedPositions (positions i) (R i j z)) (α i j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p i) (k.val+1) true)
      (min (CachedRows.cachedA (p i) (k.val+1) false) (CachedRows.cachedC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))))<1 := by
  intro i
  fin_cases i
  · exact cached_case_0
  · exact cached_case_1
  · exact cached_case_2
  · exact cached_case_3
  · exact cached_case_4
  · exact cached_case_5
  · exact cached_case_6
  · exact cached_case_7
  · exact cached_case_8
  · exact cached_case_9
  · exact cached_case_10
  · exact cached_case_11
  · exact cached_case_12
  · exact cached_case_13
  · exact cached_case_14
  · exact cached_case_15
  · exact cached_case_16
  · exact cached_case_17
  · exact cached_case_18
  · exact cached_case_19
  · exact cached_case_20
  · exact cached_case_21
  · exact cached_case_22
  · exact cached_case_23
  · exact cached_case_24
  · exact cached_case_25
  · exact cached_case_26
  · exact cached_case_27
  · exact cached_case_28
  · exact cached_case_29
  · exact cached_case_30
  · exact cached_case_31
  · exact cached_case_32
  · exact cached_case_33
  · exact cached_case_34
  · exact cached_case_35
  · exact cached_case_36
  · exact cached_case_37
  · exact cached_case_38
  · exact cached_case_39
  · exact cached_case_40
  · exact cached_case_41
  · exact cached_case_42
  · exact cached_case_43
  · exact cached_case_44
  · exact cached_case_45
  · exact cached_case_46
  · exact cached_case_47
  · exact cached_case_48
  · exact cached_case_49
  · exact cached_case_50
  · exact cached_case_51
  · exact cached_case_52
  · exact cached_case_53
  · exact cached_case_54
  · exact cached_case_55
  · exact cached_case_56
  · exact cached_case_57
  · exact cached_case_58
  · exact cached_case_59
  · exact cached_case_60
  · exact cached_case_61
  · exact cached_case_62
  · exact cached_case_63
  · exact cached_case_64
  · exact cached_case_65
  · exact cached_case_66
  · exact cached_case_67
  · exact cached_case_68
  · exact cached_case_69
  · exact cached_case_70
  · exact cached_case_71
  · exact cached_case_72
  · exact cached_case_73
  · exact cached_case_74
  · exact cached_case_75
  · exact cached_case_76
  · exact cached_case_77
  · exact cached_case_78
  · exact cached_case_79
  · exact cached_case_80
  · exact cached_case_81
  · exact cached_case_82
  · exact cached_case_83
  · exact cached_case_84
  · exact cached_case_85
  · exact cached_case_86
  · exact cached_case_87
  · exact cached_case_88
  · exact cached_case_89
  · exact cached_case_90
  · exact cached_case_91
  · exact cached_case_92
  · exact cached_case_93
  · exact cached_case_94
  · exact cached_case_95
  · exact cached_case_96
  · exact cached_case_97
  · exact cached_case_98
  · exact cached_case_99
  · exact cached_case_100
  · exact cached_case_101
  · exact cached_case_102
  · exact cached_case_103
  · exact cached_case_104
  · exact cached_case_105
  · exact cached_case_106
  · exact cached_case_107
  · exact cached_case_108
  · exact cached_case_109
  · exact cached_case_110
  · exact cached_case_111
  · exact cached_case_112
  · exact cached_case_113
  · exact cached_case_114
  · exact cached_case_115
  · exact cached_case_116
  · exact cached_case_117
  · exact cached_case_118
  · exact cached_case_119
  · exact cached_case_120
  · exact cached_case_121
  · exact cached_case_122
  · exact cached_case_123
  · exact cached_case_124
  · exact cached_case_125
  · exact cached_case_126
  · exact cached_case_127
  · exact cached_case_128
  · exact cached_case_129
  · exact cached_case_130
  · exact cached_case_131
  · exact cached_case_132
  · exact cached_case_133
  · exact cached_case_134
  · exact cached_case_135
  · exact cached_case_136
  · exact cached_case_137
  · exact cached_case_138
  · exact cached_case_139
  · exact cached_case_140
  · exact cached_case_141
  · exact cached_case_142
  · exact cached_case_143
  · exact cached_case_144
  · exact cached_case_145
  · exact cached_case_146
  · exact cached_case_147
  · exact cached_case_148
  · exact cached_case_149
  · exact cached_case_150
  · exact cached_case_151
  · exact cached_case_152
  · exact cached_case_153
  · exact cached_case_154
  · exact cached_case_155
  · exact cached_case_156
  · exact cached_case_157
  · exact cached_case_158
  · exact cached_case_159
  · exact cached_case_160
  · exact cached_case_161
  · exact cached_case_162
  · exact cached_case_163
  · exact cached_case_164
  · exact cached_case_165
  · exact cached_case_166
  · exact cached_case_167
  · exact cached_case_168
  · exact cached_case_169
  · exact cached_case_170
  · exact cached_case_171
  · exact cached_case_172
  · exact cached_case_173
  · exact cached_case_174
  · exact cached_case_175
  · exact cached_case_176
  · exact cached_case_177
  · exact cached_case_178
  · exact cached_case_179
  · exact cached_case_180

theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧ (p i).emptyPairCap=none ∧
    (∀ j, (positions i j).val+1∈(p i).correctionCenters) ∧
    (∀ j z, 0≤α i j z) ∧ (∀ j z, j∉R i j z) ∧
    (∀ j z, quota i j z ≤
      (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (R i j z))+2-
        (24-1-(R i j z).card))/3) ∧
    (∀ j, loss i j ≤ (∑ z, (quota i j z : ℚ)*α i j z)-
      penaltySum (p i) ((positions i j).val+1) (fun z => avoidedPositions (positions i) (R i j z)) (α i j)) ∧
    (∑ k : Fin 24, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))))<1 := by
  intro i
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := cachedCertificates i
  refine ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,?_⟩
  have eq : (∑k : Fin 24, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1)))) =
      ∑k : Fin 24, min (CachedRows.cachedA (p i) (k.val+1) true)
      (min (CachedRows.cachedA (p i) (k.val+1) false) (CachedRows.cachedC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))) := by
    apply Finset.sum_congr rfl
    intro k _
    obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq (p i) 34 (k.val+1) valid nocap
    rw [ha,hb,hc]
  rw [eq]
  exact strict
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric.certificates
