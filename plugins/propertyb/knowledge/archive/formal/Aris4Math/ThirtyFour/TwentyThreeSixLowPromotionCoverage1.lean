import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block0
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block1
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block2
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block3
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block4
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block5
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block6
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block7
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block8
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block9
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block10
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block11
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block12
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block13
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block14
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block15
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block16
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block17
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block18
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block19
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block20
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block21
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block22
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block23
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block24
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block25
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block26
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block27
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block28
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block29
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block30
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block31
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block32
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block33
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block34
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block35
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block36
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block37
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block38
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block39
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block40
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block41
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block42
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block43
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block44
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block45
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block46
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1Block47
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows1 : List (List ℕ × Reason) := rows1_0 ++ rows1_1 ++ rows1_2 ++ rows1_3 ++ rows1_4 ++ rows1_5 ++ rows1_6 ++ rows1_7 ++ rows1_8 ++ rows1_9 ++ rows1_10 ++ rows1_11 ++ rows1_12 ++ rows1_13 ++ rows1_14 ++ rows1_15 ++ rows1_16 ++ rows1_17 ++ rows1_18 ++ rows1_19 ++ rows1_20 ++ rows1_21 ++ rows1_22 ++ rows1_23 ++ rows1_24 ++ rows1_25 ++ rows1_26 ++ rows1_27 ++ rows1_28 ++ rows1_29 ++ rows1_30 ++ rows1_31 ++ rows1_32 ++ rows1_33 ++ rows1_34 ++ rows1_35 ++ rows1_36 ++ rows1_37 ++ rows1_38 ++ rows1_39 ++ rows1_40 ++ rows1_41 ++ rows1_42 ++ rows1_43 ++ rows1_44 ++ rows1_45 ++ rows1_46 ++ rows1_47
theorem catalogue_eq1 : catalogue 1=rows1.map Prod.fst := by decide +kernel
theorem row_coverage1 : rows1.all (fun row => decide (rowValid 1 row.1 row.2))=true := by
  simp only [rows1,List.all_append,rows1_0_checked,rows1_1_checked,rows1_2_checked,rows1_3_checked,rows1_4_checked,rows1_5_checked,rows1_6_checked,rows1_7_checked,rows1_8_checked,rows1_9_checked,rows1_10_checked,rows1_11_checked,rows1_12_checked,rows1_13_checked,rows1_14_checked,rows1_15_checked,rows1_16_checked,rows1_17_checked,rows1_18_checked,rows1_19_checked,rows1_20_checked,rows1_21_checked,rows1_22_checked,rows1_23_checked,rows1_24_checked,rows1_25_checked,rows1_26_checked,rows1_27_checked,rows1_28_checked,rows1_29_checked,rows1_30_checked,rows1_31_checked,rows1_32_checked,rows1_33_checked,rows1_34_checked,rows1_35_checked,rows1_36_checked,rows1_37_checked,rows1_38_checked,rows1_39_checked,rows1_40_checked,rows1_41_checked,rows1_42_checked,rows1_43_checked,rows1_44_checked,rows1_45_checked,rows1_46_checked,rows1_47_checked,Bool.true_and]
theorem coverage1 (values : List ℕ) (mem : values∈catalogue 1) : covered 1 values := by
  rw [catalogue_eq1] at mem
  obtain ⟨row,member,same⟩ := List.mem_map.mp mem
  subst values
  exact rowValid_covered 1 row.1 row.2 (of_decide_eq_true (List.all_eq_true.mp row_coverage1 row member))
end Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
