import Aris4Math.LowDegree
import Mathlib.Data.Finset.Max
import Mathlib.Tactic.IntervalCases

/-!
# Twenty vertices: minimum-degree two-lock selection for 33 edges

Every pair-covering input has one of twelve degree pairs with codegree one.
The proof chooses an actual minimum-degree vertex and bounds its actual good
partners using the total incidence budget. It supplies structure only; no
probability or colorability conclusion is asserted in this module.
-/

namespace Aris4Math.ThirtyThree

open scoped BigOperators

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Complete degree-pair range for an actual pair-covering 20-vertex,
33-edge hypergraph: (5,5..8), (6,6..9), (7,7..9), or (8,8). -/
theorem exists_two_locks_of_twenty
    (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (vertices20 : Fintype.card V = 20) :
    ∃ x y, x ≠ y ∧ H.codegree x y = 1 ∧
      ((H.degree x = 5 ∧ 5 ≤ H.degree y ∧ H.degree y ≤ 8) ∨
       (H.degree x = 6 ∧ 6 ≤ H.degree y ∧ H.degree y ≤ 9) ∨
       (H.degree x = 7 ∧ 7 ≤ H.degree y ∧ H.degree y ≤ 9) ∨
       (H.degree x = 8 ∧ H.degree y = 8)) := by
  have vertices_nonempty : (Finset.univ : Finset V).Nonempty := by
    apply Finset.card_pos.mp
    rw [Finset.card_univ, vertices20]
    decide
  obtain ⟨x, _, hx⟩ := Finset.exists_min_image Finset.univ H.degree vertices_nonempty
  have minimum (z : V) : H.degree x ≤ H.degree z := hx z (Finset.mem_univ z)
  have lower : 5 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices20] at h
    omega
  have upper : H.degree x ≤ 8 := by
    have h := H.subset_degree_budget Finset.univ (H.degree x) 0 minimum
      (fun z _ => by simpa using minimum z)
    rw [vertices20, edges33] at h
    omega
  let W := H.goodPartners x
  have sizeW : 38 - 4 * H.degree x ≤ W.card := by
    have h := H.goodPartners_budget cover x
    rw [vertices20] at h
    change 20 ≤ W.card + 1 + (4 * H.degree x - (20 - 1)) at h
    omega
  have partner (b extra : ℕ)
      (hthreshold : H.degree x + extra = b + 1)
      (hstrict : 165 < H.degree x * 20 + extra * (38 - 4 * H.degree x)) :
      ∃ y ∈ W, H.degree y ≤ b := by
    by_contra hn
    have high (y : V) (hy : y ∈ W) : H.degree x + extra ≤ H.degree y := by
      have : ¬ H.degree y ≤ b := fun h => hn ⟨y, hy, h⟩
      omega
    have budget := H.subset_degree_budget W (H.degree x) extra minimum high
    rw [vertices20, edges33] at budget
    have scaled := Nat.mul_le_mul_left extra sizeW
    omega
  have pair (b extra : ℕ)
      (hthreshold : H.degree x + extra = b + 1)
      (hstrict : 165 < H.degree x * 20 + extra * (38 - 4 * H.degree x)) :
      ∃ y, x ≠ y ∧ H.codegree x y = 1 ∧ H.degree x ≤ H.degree y ∧ H.degree y ≤ b := by
    obtain ⟨y, hy, dy⟩ := partner b extra hthreshold hstrict
    obtain ⟨hne, hone⟩ := (H.mem_goodPartners cover x y).mp hy
    exact ⟨y, Ne.symm hne, hone, minimum y, dy⟩
  interval_cases hd : H.degree x
  · obtain ⟨y, hne, hone, hlow, hupp⟩ := pair 8 4 (by omega) (by norm_num [hd])
    exact ⟨x, y, hne, hone, Or.inl ⟨hd, by omega, hupp⟩⟩
  · obtain ⟨y, hne, hone, hlow, hupp⟩ := pair 9 4 (by omega) (by norm_num [hd])
    exact ⟨x, y, hne, hone, Or.inr (Or.inl ⟨hd, by omega, hupp⟩)⟩
  · obtain ⟨y, hne, hone, hlow, hupp⟩ := pair 9 3 (by omega) (by norm_num [hd])
    exact ⟨x, y, hne, hone, Or.inr (Or.inr (Or.inl ⟨hd, by omega, hupp⟩))⟩
  · obtain ⟨y, hne, hone, hlow, hupp⟩ := pair 8 1 (by omega) (by norm_num [hd])
    exact ⟨x, y, hne, hone, Or.inr (Or.inr (Or.inr ⟨hd, by omega⟩))⟩

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.exists_two_locks_of_twenty
