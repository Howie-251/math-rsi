import Aris4Math.ThirtyFour.TwentyFourNoLow

namespace TwentyFourNoLowReviewAudit
/-- The complete r=0 branch, restated using only an edge Finset, ordinary
incidence hypotheses and the literal Bool coloring conclusion. -/
theorem original_branch (E : Finset (Finset (Fin 24)))
    (uniform : ∀e∈E,e.card=5) (size : E.card=34)
    (cover : ∀x y : Fin 24,x≠y→∃e∈E,x∈e ∧ y∈e)
    (no_six : ∀x : Fin 24,(E.filter (fun e=>x∈e)).card≠6) :
    ∃c : Fin 24→Bool,∀e∈E,
      1≤(e.filter (fun x=>c x=true)).card ∧
      (e.filter (fun x=>c x=true)).card≤4 := by
  let H : Aris4Math.Simple5Hypergraph (Fin 24) := ⟨E,uniform⟩
  have none : H.sixVertices.card=0 := by
    apply Finset.card_eq_zero.mpr
    apply Finset.eq_empty_iff_forall_not_mem.mpr
    intro x hx
    exact no_six x (Finset.mem_filter.mp hx).2
  exact Aris4Math.ThirtyFour.TwentyFourNoLow.propertyB_of_no_six H cover size none

#print axioms original_branch
#print axioms Aris4Math.ThirtyFour.TwentyFourNoLow.propertyB_of_no_six
#print axioms Aris4Math.ThirtyFour.TwentyFourNoLowCoverage.coverage
end TwentyFourNoLowReviewAudit
