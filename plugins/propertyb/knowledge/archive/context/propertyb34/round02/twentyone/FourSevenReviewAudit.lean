import Aris4Math.ThirtyFour.Assembly

namespace TwentyOneFourSevenReviewAudit
theorem original_branch (E : Finset (Finset (Fin 21)))
    (uniform : ∀e∈E,e.card=5) (size : E.card=34)
    (cover : ∀x y : Fin 21,x≠y→∃e∈E,x∈e ∧ y∈e)
    (minimum : ∀x : Fin 21,7≤(E.filter (fun e=>x∈e)).card)
    (four : (Finset.univ.filter (fun x : Fin 21 =>
      (E.filter (fun e=>x∈e)).card=7)).card=4) :
    ∃c : Fin 21→Bool,∀e∈E,
      1≤(e.filter (fun x=>c x=true)).card ∧
      (e.filter (fun x=>c x=true)).card≤4 := by
  let H : Aris4Math.Simple5Hypergraph (Fin 21) := ⟨E,uniform⟩
  exact Aris4Math.ThirtyFour.TwentyOneSevenFour.propertyB_of_four_sevens
    H cover size minimum four

#print axioms original_branch
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenFour.propertyB_of_four_sevens
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue.coverage
#print axioms Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal
end TwentyOneFourSevenReviewAudit
