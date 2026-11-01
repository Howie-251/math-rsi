import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage2Block0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage2Block1
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage2Block2
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage2Block3
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage2Block4
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage2Block5
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage2Block6
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows2 : List (List ℕ × (Degree → Witness)) := rows2_0 ++ rows2_1 ++ rows2_2 ++ rows2_3 ++ rows2_4 ++ rows2_5 ++ rows2_6
theorem catalogue_eq2 : catalogue (some 2)=rows2.map Prod.fst := by decide +kernel
theorem rows_checked2 : rows2.all (fun row => decide (∀ d : Degree, Matched d (some 2) row.1 (row.2 d)))=true := by
  simp only [rows2,List.all_append,rows2_0_checked,rows2_1_checked,rows2_2_checked,rows2_3_checked,rows2_4_checked,rows2_5_checked,rows2_6_checked,Bool.true_and]
theorem coverage2 (values : List ℕ) (mem : values∈catalogue (some 2)) (d : Degree) :
    ∃ w : Witness, Matched d (some 2) values w := by
  rw [catalogue_eq2] at mem
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  subst values
  exact ⟨r.2 d,(of_decide_eq_true (List.all_eq_true.mp rows_checked2 r member)) d⟩
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
