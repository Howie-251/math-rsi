import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage5Block0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage5Block1
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage5Block2
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage5Block3
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage5Block4
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage5Block5
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage5Block6
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows5 : List (List ℕ × (Degree → Witness)) := rows5_0 ++ rows5_1 ++ rows5_2 ++ rows5_3 ++ rows5_4 ++ rows5_5 ++ rows5_6
theorem catalogue_eq5 : catalogue (some 5)=rows5.map Prod.fst := by decide +kernel
theorem rows_checked5 : rows5.all (fun row => decide (∀ d : Degree, Matched d (some 5) row.1 (row.2 d)))=true := by
  simp only [rows5,List.all_append,rows5_0_checked,rows5_1_checked,rows5_2_checked,rows5_3_checked,rows5_4_checked,rows5_5_checked,rows5_6_checked,Bool.true_and]
theorem coverage5 (values : List ℕ) (mem : values∈catalogue (some 5)) (d : Degree) :
    ∃ w : Witness, Matched d (some 5) values w := by
  rw [catalogue_eq5] at mem
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  subst values
  exact ⟨r.2 d,(of_decide_eq_true (List.all_eq_true.mp rows_checked5 r member)) d⟩
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
