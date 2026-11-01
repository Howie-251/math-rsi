import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage3Block0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage3Block1
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage3Block2
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage3Block3
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage3Block4
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage3Block5
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage3Block6
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows3 : List (List ℕ × (Degree → Witness)) := rows3_0 ++ rows3_1 ++ rows3_2 ++ rows3_3 ++ rows3_4 ++ rows3_5 ++ rows3_6
theorem catalogue_eq3 : catalogue (some 3)=rows3.map Prod.fst := by decide +kernel
theorem rows_checked3 : rows3.all (fun row => decide (∀ d : Degree, Matched d (some 3) row.1 (row.2 d)))=true := by
  simp only [rows3,List.all_append,rows3_0_checked,rows3_1_checked,rows3_2_checked,rows3_3_checked,rows3_4_checked,rows3_5_checked,rows3_6_checked,Bool.true_and]
theorem coverage3 (values : List ℕ) (mem : values∈catalogue (some 3)) (d : Degree) :
    ∃ w : Witness, Matched d (some 3) values w := by
  rw [catalogue_eq3] at mem
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  subst values
  exact ⟨r.2 d,(of_decide_eq_true (List.all_eq_true.mp rows_checked3 r member)) d⟩
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
