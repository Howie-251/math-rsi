import Aris4Math.LowDegree

/-!
# Twenty-two vertices: complete lock-pair selection for thirty-three edges

This theorem concerns actual degrees and codegrees of the original hypergraph.
It proves the structural selection, not the probability bound or Property B.
The old thirty-two-edge statements and their proofs are unchanged.
-/

namespace Aris4Math.ThirtyThree

open scoped BigOperators

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- At 22 points the complete two-lock alternatives arise from actual degrees. -/
theorem exists_two_locks_of_twenty_two
    (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (vertices22 : Fintype.card V = 22) :
    ∃ x y, x ≠ y ∧ H.codegree x y = 1 ∧
      ((H.degree x = 6 ∧ H.degree y = 6) ∨
       (H.degree x = 6 ∧ H.degree y = 7) ∨
       (H.degree x = 7 ∧ H.degree y = 7)) := by
  have minimum (x : V) : 6 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices22] at h
    omega
  by_cases hsix : ∃ x, H.degree x = 6
  · obtain ⟨x, hx⟩ := hsix
    have size := H.goodPartners_budget cover x
    rw [vertices22, hx] at size
    have partner : ∃ y ∈ H.goodPartners x, H.degree y ≤ 7 := by
      by_contra hn
      have high : ∀ y ∈ H.goodPartners x, 6 + 2 ≤ H.degree y := by
        intro y hy
        have : ¬ H.degree y ≤ 7 := fun h => hn ⟨y, hy, h⟩
        omega
      have budget := H.subset_degree_budget (H.goodPartners x) 6 2 minimum high
      rw [vertices22, edges33] at budget
      omega
    obtain ⟨y, hy, dy⟩ := partner
    obtain ⟨hne, hcodeg⟩ := (H.mem_goodPartners cover x y).mp hy
    refine ⟨x, y, Ne.symm hne, hcodeg, ?_⟩
    have ly := minimum y
    rcases (show H.degree y = 6 ∨ H.degree y = 7 by omega) with h6 | h7
    · exact Or.inl ⟨hx, h6⟩
    · exact Or.inr (Or.inl ⟨hx, h7⟩)
  · have min7 (x : V) : 7 ≤ H.degree x := by
      have h := minimum x
      have : H.degree x ≠ 6 := fun h => hsix ⟨x, h⟩
      omega
    let S := Finset.univ.filter fun x => H.degree x = 7
    have size : 11 ≤ S.card := by
      have each (x : V) : 8 ≤ H.degree x + if H.degree x = 7 then 1 else 0 := by
        have h := min7 x
        split_ifs <;> omega
      have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
      have hs : 8 * Fintype.card V ≤ 165 + S.card := by
        simpa [Finset.sum_add_distrib, H.sum_degrees, edges33,
          S, Nat.mul_comm] using h
      rw [vertices22] at hs
      omega
    obtain ⟨x, hx⟩ := Finset.card_pos.mp (show 0 < S.card by omega)
    have dx : H.degree x = 7 := (Finset.mem_filter.mp hx).2
    let B := insert x (H.badPartners x)
    have bsize : B.card ≤ 8 := by
      have hb := H.badPartners_card_le_excess cover x
      rw [vertices22, dx] at hb
      have hi := Finset.card_insert_le x (H.badPartners x)
      dsimp [B]
      omega
    have large := Finset.card_le_card_sdiff_add_card (s := S) (t := B)
    obtain ⟨y, hy⟩ := Finset.card_pos.mp (show 0 < (S \ B).card by omega)
    obtain ⟨hyS, hyB⟩ := Finset.mem_sdiff.mp hy
    have good : y ∈ H.goodPartners x := by
      exact Finset.mem_sdiff.mpr ⟨Finset.mem_univ y, hyB⟩
    obtain ⟨hne, hcodeg⟩ := (H.mem_goodPartners cover x y).mp good
    exact ⟨x, y, Ne.symm hne, hcodeg,
      Or.inr (Or.inr ⟨dx, (Finset.mem_filter.mp hyS).2⟩)⟩

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.exists_two_locks_of_twenty_two
