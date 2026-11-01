import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage6Block0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage6Block1
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage6Block2
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage6Block3
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage6Block4
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows6 : List (List ℕ × (Degree → Witness)) := rows6_0 ++ rows6_1 ++ rows6_2 ++ rows6_3 ++ rows6_4
theorem catalogue_eq6 : catalogue none=rows6.map Prod.fst := by decide +kernel
theorem rows_checked6 : rows6.all (fun row => decide (∀ d : Degree, Matched d none row.1 (row.2 d)))=true := by
  simp only [rows6,List.all_append,rows6_0_checked,rows6_1_checked,rows6_2_checked,rows6_3_checked,rows6_4_checked,Bool.true_and]
theorem coverage6 (values : List ℕ) (mem : values∈catalogue none) (d : Degree) :
    ∃ w : Witness, Matched d none values w := by
  rw [catalogue_eq6] at mem
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  subst values
  exact ⟨r.2 d,(of_decide_eq_true (List.all_eq_true.mp rows_checked6 r member)) d⟩
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
