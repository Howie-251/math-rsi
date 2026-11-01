import Aris4Math.SevenPoint

/-! The full finite-block deletion argument used to avoid the exceptional
six-point type. No classification or hypergraph realization is assumed here. -/

namespace Aris4Math.Avoidance

variable {α : Type*} [DecidableEq α]

/-- Delete u, discard traces of size less than two, and keep distinct traces. -/
def restrictBlocks (blocks : Finset (Finset α)) (u : α) : Finset (Finset α) :=
  ((blocks.image (fun B => B.erase u)).filter (fun B => 2 ≤ B.card))

/-- The exceptional two-disjoint-triangles type satisfies this weaker shape:
there is no block of size four or more, and there are exactly two triples. -/
def TwoTripleShape (blocks : Finset (Finset α)) : Prop :=
  (∀ B ∈ blocks, B.card ≤ 3) ∧ (blocks.filter (fun B => B.card = 3)).card = 2

/-- If every deletion has the small-block shape, no original block can have
size four or five: a point outside that block preserves it. -/
theorem all_blocks_small
    (W : Finset α) (blocks : Finset (Finset α))
    (seven : W.card = 7)
    (inside : ∀ B ∈ blocks, B ⊆ W)
    (at_most_five : ∀ B ∈ blocks, B.card ≤ 5)
    (small_deletions : ∀ u ∈ W, ∀ B ∈ restrictBlocks blocks u, B.card ≤ 3) :
    ∀ B ∈ blocks, B.card ≤ 3 := by
  intro B hB
  by_contra hlarge
  have hfour : 4 ≤ B.card := by omega
  have hdiff : (W \ B).Nonempty := by
    apply Finset.card_pos.mp
    rw [Finset.card_sdiff_of_subset (inside B hB), seven]
    have hf := at_most_five B hB
    omega
  obtain ⟨u, hu⟩ := hdiff
  obtain ⟨huW, huB⟩ := Finset.mem_sdiff.mp hu
  have hkeep : B ∈ restrictBlocks blocks u := by
    apply Finset.mem_filter.mpr
    refine ⟨?_, by omega⟩
    exact Finset.mem_image.mpr ⟨B, hB, Finset.erase_eq_of_notMem huB⟩
  exact hlarge (small_deletions u huW B hkeep)

/-- With all blocks of size at most three, the triples after deletion are
exactly the original triples that avoided the deleted point. -/
theorem triples_after_deletion
    (blocks : Finset (Finset α)) (u : α)
    (small : ∀ B ∈ blocks, B.card ≤ 3) :
    (restrictBlocks blocks u).filter (fun B => B.card = 3) =
      (blocks.filter (fun B => B.card = 3)).filter (fun B => u ∉ B) := by
  ext B
  simp only [Finset.mem_filter, restrictBlocks]
  constructor
  · rintro ⟨⟨himage, _⟩, hthree⟩
    obtain ⟨C, hC, hCB⟩ := Finset.mem_image.mp himage
    have huC : u ∉ C := by
      intro huC
      have hcard := Finset.card_erase_add_one huC
      rw [hCB, hthree] at hcard
      have hsmall := small C hC
      omega
    have hCeq : C = B := by simpa [Finset.erase_eq_of_notMem huC] using hCB
    subst C
    exact ⟨⟨hC, hthree⟩, huC⟩
  · rintro ⟨⟨hB, hthree⟩, huB⟩
    refine ⟨⟨?_, by omega⟩, hthree⟩
    exact Finset.mem_image.mpr ⟨B, hB, Finset.erase_eq_of_notMem huB⟩

/-- Among seven points, some deletion avoids the two-triple small-block
shape. In particular, it cannot have two disjoint triangles and only pairs.
The theorem is universal over finite block families, not an enumeration. -/
theorem exists_deletion_not_two_triple_shape
    (W : Finset α) (blocks : Finset (Finset α))
    (seven : W.card = 7)
    (inside : ∀ B ∈ blocks, B ⊆ W)
    (at_most_five : ∀ B ∈ blocks, B.card ≤ 5) :
    ∃ u ∈ W, ¬ TwoTripleShape (restrictBlocks blocks u) := by
  by_contra hnone
  have every : ∀ u ∈ W, TwoTripleShape (restrictBlocks blocks u) := by
    intro u hu
    by_contra hbad
    exact hnone ⟨u, hu, hbad⟩
  have small := all_blocks_small W blocks seven inside at_most_five
    (fun u hu => (every u hu).1)
  let triples := blocks.filter (fun B => B.card = 3)
  obtain ⟨u, hu, hne⟩ := SevenPoint.exists_deletion_not_two W triples seven
    (fun B hB => inside B (Finset.mem_filter.mp hB).1)
    (fun B hB => (Finset.mem_filter.mp hB).2)
  apply hne
  have heq := (every u hu).2
  rw [triples_after_deletion blocks u small] at heq
  exact heq

end Aris4Math.Avoidance

#print axioms Aris4Math.Avoidance.all_blocks_small
#print axioms Aris4Math.Avoidance.triples_after_deletion
#print axioms Aris4Math.Avoidance.exists_deletion_not_two_triple_shape
