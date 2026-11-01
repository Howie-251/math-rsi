import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage1Block0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage1Block1
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage1Block2
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage1Block3
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage1Block4
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage1Block5
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage1Block6
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows1 : List (List ℕ × (Degree → Witness)) := rows1_0 ++ rows1_1 ++ rows1_2 ++ rows1_3 ++ rows1_4 ++ rows1_5 ++ rows1_6
theorem catalogue_eq1 : catalogue (some 1)=rows1.map Prod.fst := by decide +kernel
theorem rows_checked1 : rows1.all (fun row => decide (∀ d : Degree, Matched d (some 1) row.1 (row.2 d)))=true := by
  simp only [rows1,List.all_append,rows1_0_checked,rows1_1_checked,rows1_2_checked,rows1_3_checked,rows1_4_checked,rows1_5_checked,rows1_6_checked,Bool.true_and]
theorem coverage1 (values : List ℕ) (mem : values∈catalogue (some 1)) (d : Degree) :
    ∃ w : Witness, Matched d (some 1) values w := by
  rw [catalogue_eq1] at mem
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  subst values
  exact ⟨r.2 d,(of_decide_eq_true (List.all_eq_true.mp rows_checked1 r member)) d⟩
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
