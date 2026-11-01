import Aris4Math.ThirtyFour.TwentyFourSixLowBadSparseBridge
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
open TwentyFourSixLowBadData
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_cover_0 : (rows 0).map rowValues=catalogue 0 := by decide +kernel
theorem rows_cover_1 : (rows 1).map rowValues=catalogue 1 := by decide +kernel
theorem rows_cover_2 : (rows 2).map rowValues=catalogue 2 := by decide +kernel
theorem rows_cover (b : Pattern) : (rows b).map rowValues=catalogue b := by
  fin_cases b
  · exact rows_cover_0
  · exact rows_cover_1
  · exact rows_cover_2
theorem rows_correct_0 : ∀r∈rows 0,CheapMatch 0 (rowValues r) r.2 := by decide +kernel
theorem rows_correct_1 : ∀r∈rows 1,CheapMatch 1 (rowValues r) r.2 := by decide +kernel
theorem rows_correct_2 : ∀r∈rows 2,CheapMatch 2 (rowValues r) r.2 := by decide +kernel
theorem rows_correct (b : Pattern) : ∀r∈rows b,CheapMatch b (rowValues r) r.2 := by
  fin_cases b
  · exact rows_correct_0
  · exact rows_correct_1
  · exact rows_correct_2
theorem coverage (b : Pattern) (values : List ℕ) (member : values∈catalogue b) :
    ∃selected : Case×Perm,
      (∀T,T.card≤2→low b (T.map (perm selected.2).toEmbedding)=upper selected.1 T) ∧
      (∀T,3≤T.card→vector values (T.map (perm selected.2).toEmbedding)=μ selected.1 T) := by
  have inrows : values∈(rows b).map rowValues := by rw [rows_cover];exact member
  obtain ⟨r,hr,eq⟩ := List.mem_map.mp inrows
  rw [← eq]
  exact ⟨r.2,cheap_correct b (rowValues r) r.2 (rows_correct b _ hr)⟩
end Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage.coverage
