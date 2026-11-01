import Aris4Math

/-!
The integer-counting core of the seven-point avoidance argument.
This does not assume that every six-point set is a good profile: it proves
that seven deletions cannot all leave exactly two triples.
The hypergraph-to-block-family correspondence remains a separate obligation.
-/

open scoped BigOperators

namespace Aris4Math.SevenPoint

variable {α : Type*} [DecidableEq α]

/-- Count the pairs `(u, B)` with `u ∈ W`, `B ∈ blocks`, and `u ∉ B`
in the two possible orders. No enumeration of block families is used. -/
theorem absent_incidence_count (W : Finset α) (blocks : Finset (Finset α)) :
    (∑ u ∈ W, (blocks.filter (fun B => u ∉ B)).card) =
      ∑ B ∈ blocks, (W \ B).card := by
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro B _
  rw [Finset.sdiff_eq_filter, Finset.sum_filter]

/-- A family of three-element subsets of a seven-element set has a deletion
that leaves a number of intact triples different from two. -/
theorem exists_deletion_not_two
    (W : Finset α) (blocks : Finset (Finset α))
    (seven : W.card = 7)
    (inside : ∀ B ∈ blocks, B ⊆ W)
    (triples : ∀ B ∈ blocks, B.card = 3) :
    ∃ u ∈ W, (blocks.filter (fun B => u ∉ B)).card ≠ 2 := by
  by_contra h
  have each : ∀ u ∈ W, (blocks.filter (fun B => u ∉ B)).card = 2 := by
    intro u hu
    by_contra hn
    exact h ⟨u, hu, hn⟩
  have left : (∑ u ∈ W, (blocks.filter (fun B => u ∉ B)).card) = 14 := by
    calc
      _ = ∑ _u ∈ W, 2 := Finset.sum_congr rfl each
      _ = 14 := by simp [seven]
  have right : (∑ B ∈ blocks, (W \ B).card) = blocks.card * 4 := by
    calc
      _ = ∑ _B ∈ blocks, 4 := by
        apply Finset.sum_congr rfl
        intro B hB
        rw [Finset.card_sdiff_of_subset (inside B hB), seven, triples B hB]
      _ = _ := by simp
  have impossible := absent_incidence_count W blocks
  rw [left, right] at impossible
  omega

end Aris4Math.SevenPoint

#print axioms Aris4Math.SevenPoint.absent_incidence_count
#print axioms Aris4Math.SevenPoint.exists_deletion_not_two
