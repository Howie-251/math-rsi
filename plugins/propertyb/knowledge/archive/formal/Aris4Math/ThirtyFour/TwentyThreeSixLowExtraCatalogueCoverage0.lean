import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage0Block0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage0Block1
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage0Block2
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage0Block3
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage0Block4
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage0Block5
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage0Block6
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows0 : List (List ℕ × (Degree → Witness)) := rows0_0 ++ rows0_1 ++ rows0_2 ++ rows0_3 ++ rows0_4 ++ rows0_5 ++ rows0_6
theorem catalogue_eq0 : catalogue (some 0)=rows0.map Prod.fst := by decide +kernel
theorem rows_checked0 : rows0.all (fun row => decide (∀ d : Degree, Matched d (some 0) row.1 (row.2 d)))=true := by
  simp only [rows0,List.all_append,rows0_0_checked,rows0_1_checked,rows0_2_checked,rows0_3_checked,rows0_4_checked,rows0_5_checked,rows0_6_checked,Bool.true_and]
theorem coverage0 (values : List ℕ) (mem : values∈catalogue (some 0)) (d : Degree) :
    ∃ w : Witness, Matched d (some 0) values w := by
  rw [catalogue_eq0] at mem
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  subst values
  exact ⟨r.2 d,(of_decide_eq_true (List.all_eq_true.mp rows_checked0 r member)) d⟩
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
