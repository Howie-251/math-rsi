import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage4Block0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage4Block1
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage4Block2
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage4Block3
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage4Block4
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage4Block5
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage4Block6
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows4 : List (List ℕ × (Degree → Witness)) := rows4_0 ++ rows4_1 ++ rows4_2 ++ rows4_3 ++ rows4_4 ++ rows4_5 ++ rows4_6
theorem catalogue_eq4 : catalogue (some 4)=rows4.map Prod.fst := by decide +kernel
theorem rows_checked4 : rows4.all (fun row => decide (∀ d : Degree, Matched d (some 4) row.1 (row.2 d)))=true := by
  simp only [rows4,List.all_append,rows4_0_checked,rows4_1_checked,rows4_2_checked,rows4_3_checked,rows4_4_checked,rows4_5_checked,rows4_6_checked,Bool.true_and]
theorem coverage4 (values : List ℕ) (mem : values∈catalogue (some 4)) (d : Degree) :
    ∃ w : Witness, Matched d (some 4) values w := by
  rw [catalogue_eq4] at mem
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  subst values
  exact ⟨r.2 d,(of_decide_eq_true (List.all_eq_true.mp rows_checked4 r member)) d⟩
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
