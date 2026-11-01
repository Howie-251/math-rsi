import Aris4Math.SevenPoint

/-! A common block family is seen in every deletion. Constant local counts
therefore obey an integer divisibility condition. -/
namespace Aris4Math.ThirtyFour.UniformDeletionCounting
open scoped BigOperators
variable {V : Type*} [DecidableEq V]

theorem constant_deletion_identity (W : Finset V)
    (blocks : Finset (Finset V)) (r c : ℕ)
    (inside : ∀ B ∈ blocks, B ⊆ W)
    (uniform : ∀ B ∈ blocks, B.card=r)
    (constant : ∀ x ∈ W, (blocks.filter (fun B => x ∉ B)).card=c) :
    W.card*c=blocks.card*(W.card-r) := by
  have left : (∑ x ∈ W, (blocks.filter (fun B => x ∉ B)).card)=W.card*c := by
    calc
      _ = ∑ _x ∈ W, c := Finset.sum_congr rfl constant
      _ = _ := by simp
  have right : (∑ B ∈ blocks, (W \ B).card)=blocks.card*(W.card-r) := by
    calc
      _ = ∑ _B ∈ blocks, (W.card-r) := by
        apply Finset.sum_congr rfl
        intro B hB
        rw [Finset.card_sdiff_of_subset (inside B hB),uniform B hB]
      _ = _ := by simp
  simpa only [left,right] using SevenPoint.absent_incidence_count W blocks

theorem exists_nonconstant_deletion (W : Finset V)
    (blocks : Finset (Finset V)) (r c : ℕ)
    (inside : ∀ B ∈ blocks, B ⊆ W)
    (uniform : ∀ B ∈ blocks, B.card=r)
    (obstruction : ¬ (W.card-r) ∣ W.card*c) :
    ∃ x ∈ W, (blocks.filter (fun B => x ∉ B)).card≠c := by
  by_contra none
  have constant : ∀ x ∈ W, (blocks.filter (fun B => x ∉ B)).card=c := by
    intro x hx
    by_contra different
    exact none ⟨x,hx,different⟩
  have eq := constant_deletion_identity W blocks r c inside uniform constant
  apply obstruction
  exact ⟨blocks.card,by simpa only [Nat.mul_comm] using eq⟩

/-- In particular, a graph on five points cannot have exactly one edge in
each of its four-point induced subgraphs. No matching assumption is needed. -/
theorem five_pairs (W : Finset V) (edges : Finset (Finset V))
    (five : W.card=5) (inside : ∀ e ∈ edges, e ⊆ W)
    (pairs : ∀ e ∈ edges, e.card=2) :
    ∃ x ∈ W, (edges.filter (fun e => x ∉ e)).card≠1 := by
  apply exists_nonconstant_deletion W edges 2 1 inside pairs
  rw [five]
  decide

end Aris4Math.ThirtyFour.UniformDeletionCounting
#print axioms Aris4Math.ThirtyFour.UniformDeletionCounting.constant_deletion_identity
#print axioms Aris4Math.ThirtyFour.UniformDeletionCounting.five_pairs
