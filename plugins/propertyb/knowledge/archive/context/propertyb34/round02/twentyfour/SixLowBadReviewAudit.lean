import Aris4Math.ThirtyFour.TwentyFourSixLowBadComplete

namespace TwentyFourSixLowBadReviewAudit
/-- Original finite edge data and a literal Bool coloring conclusion for the
complete at-least-six-low/nonunit-pair branch. -/
theorem original_branch (E : Finset (Finset (Fin 24)))
    (uniform : ∀e∈E,e.card=5) (size : E.card=34)
    (cover : ∀x y : Fin 24,x≠y→∃e∈E,x∈e ∧ y∈e)
    (many : 6≤(Finset.univ.filter (fun x : Fin 24=>(E.filter (fun e=>x∈e)).card=6)).card)
    (bad : ∃x y : Fin 24,x≠y ∧
      (E.filter (fun e=>x∈e)).card=6 ∧ (E.filter (fun e=>y∈e)).card=6 ∧
      (E.filter (fun e=>x∈e ∧ y∈e)).card≠1) :
    ∃c : Fin 24→Bool,∀e∈E,
      1≤(e.filter (fun x=>c x=true)).card ∧
      (e.filter (fun x=>c x=true)).card≤4 := by
  let H : Aris4Math.Simple5Hypergraph (Fin 24) := ⟨E,uniform⟩
  have actual_bad : ∃x∈H.sixVertices,∃y∈H.sixVertices,x≠y ∧ H.codegree x y≠1 := by
    obtain ⟨x,y,xy,hx,hy,hxy⟩ := bad
    exact ⟨x,Finset.mem_filter.mpr ⟨Finset.mem_univ _,hx⟩,
      y,Finset.mem_filter.mpr ⟨Finset.mem_univ _,hy⟩,xy,hxy⟩
  exact Aris4Math.ThirtyFour.TwentyFourSixLowBadComplete.propertyB_of_nonunit_low_pair
    H cover size many actual_bad
#print axioms original_branch
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowBadComplete.propertyB_of_nonunit_low_pair
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage.coverage
end TwentyFourSixLowBadReviewAudit
