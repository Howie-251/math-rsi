import Aris4Math.ThirtyFour.Assembly
namespace TwentyThreeManyLowReviewAudit
theorem original_branch (E : Finset (Finset (Fin 23)))
    (uniform : ∀e∈E,e.card=5) (size : E.card=34)
    (cover : ∀x y : Fin 23,x≠y→∃e∈E,x∈e ∧ y∈e)
    (many : 7≤(Finset.univ.filter (fun x : Fin 23 =>
      (E.filter (fun e=>x∈e)).card=6)).card) :
    ∃c : Fin 23→Bool,∀e∈E,
      1≤(e.filter (fun x=>c x=true)).card ∧
      (e.filter (fun x=>c x=true)).card≤4 := by
  let H : Aris4Math.Simple5Hypergraph (Fin 23) := ⟨E,uniform⟩
  exact Aris4Math.ThirtyFour.TwentyThreeManyLowComplete.propertyB H cover size many
#print axioms original_branch
#print axioms Aris4Math.ThirtyFour.TwentyThreeManyLowComplete.propertyB
#print axioms Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal
end TwentyThreeManyLowReviewAudit
