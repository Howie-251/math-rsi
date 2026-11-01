import Aris4Math.ThirtyFour.TwentyFourNoLowSparseBridge
namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
open TwentyFourNoLowSixData
set_option maxHeartbeats 0
set_option maxRecDepth 100000

/-- Exact equality with the complete bounded domain, checked once. -/
theorem rows_cover_false : (rows false).map rowValues=catalogue false := by decide +kernel
theorem rows_cover_true : (rows true).map rowValues=catalogue true := by decide +kernel
theorem rows_cover (b : Bool) : (rows b).map rowValues=catalogue b := by
  cases b
  · exact rows_cover_false
  · exact rows_cover_true

theorem rows_correct_false : ∀r∈rows false,CheapMatch false (rowValues r) r.2 := by decide +kernel
theorem rows_correct_true : ∀r∈rows true,CheapMatch true (rowValues r) r.2 := by decide +kernel
theorem rows_correct (b : Bool) : ∀r∈rows b,CheapMatch b (rowValues r) r.2 := by
  cases b
  · exact rows_correct_false
  · exact rows_correct_true

/-- Every complete-domain input has a genuine matching witness. Sparse
support equality is lifted to all high traces by the generic decoder proof. -/
theorem coverage (b : Bool) (values : List ℕ) (member : values∈catalogue b) :
    ∃selected : Case×Perm,
      (∀T,T.card≤2→low b (T.map (perm selected.2).toEmbedding)=upper selected.1 T) ∧
      (∀T,3≤T.card→vector values (T.map (perm selected.2).toEmbedding)=μ selected.1 T) := by
  have inrows : values∈(rows b).map rowValues := by rw [rows_cover];exact member
  obtain ⟨r,hr,eq⟩ := List.mem_map.mp inrows
  rw [← eq]
  exact ⟨r.2,cheap_correct b (rowValues r) r.2 (rows_correct b _ hr)⟩
end Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
#print axioms Aris4Math.ThirtyFour.TwentyFourNoLowCoverage.coverage
