import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block0
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block1
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block2
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block3
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block4
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block5
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block6
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block7
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block8
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block9
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block10
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block11
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block12
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block13
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block14
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block15
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block16
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block17
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block18
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block19
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block20
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block21
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block22
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block23
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block24
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block25
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block26
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block27
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0Block28
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows0 : List (List ℕ × Reason) := rows0_0 ++ rows0_1 ++ rows0_2 ++ rows0_3 ++ rows0_4 ++ rows0_5 ++ rows0_6 ++ rows0_7 ++ rows0_8 ++ rows0_9 ++ rows0_10 ++ rows0_11 ++ rows0_12 ++ rows0_13 ++ rows0_14 ++ rows0_15 ++ rows0_16 ++ rows0_17 ++ rows0_18 ++ rows0_19 ++ rows0_20 ++ rows0_21 ++ rows0_22 ++ rows0_23 ++ rows0_24 ++ rows0_25 ++ rows0_26 ++ rows0_27 ++ rows0_28
theorem catalogue_eq0 : catalogue 0=rows0.map Prod.fst := by decide +kernel
theorem row_coverage0 : rows0.all (fun row => decide (rowValid 0 row.1 row.2))=true := by
  simp only [rows0,List.all_append,rows0_0_checked,rows0_1_checked,rows0_2_checked,rows0_3_checked,rows0_4_checked,rows0_5_checked,rows0_6_checked,rows0_7_checked,rows0_8_checked,rows0_9_checked,rows0_10_checked,rows0_11_checked,rows0_12_checked,rows0_13_checked,rows0_14_checked,rows0_15_checked,rows0_16_checked,rows0_17_checked,rows0_18_checked,rows0_19_checked,rows0_20_checked,rows0_21_checked,rows0_22_checked,rows0_23_checked,rows0_24_checked,rows0_25_checked,rows0_26_checked,rows0_27_checked,rows0_28_checked,Bool.true_and]
theorem coverage0 (values : List ℕ) (mem : values∈catalogue 0) : covered 0 values := by
  rw [catalogue_eq0] at mem
  obtain ⟨row,member,same⟩ := List.mem_map.mp mem
  subst values
  exact rowValid_covered 0 row.1 row.2 (of_decide_eq_true (List.all_eq_true.mp row_coverage0 row member))
end Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
