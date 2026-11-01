import Aris4Math.Structure

namespace Aris4Math.ThirtyFour.Incidence
open scoped BigOperators
variable {V : Type*} [Fintype V] [DecidableEq V]

theorem sum_codegrees_subset (H : Simple5Hypergraph V) (x : V) (S : Finset V) :
    (∑ z ∈ S, H.codegree x z) =
      ∑ e ∈ H.edges.filter (fun e => x ∈ e), (S ∩ e).card := by
  simp only [Simple5Hypergraph.codegree,Finset.card_eq_sum_ones,Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro e he
  by_cases hx : x ∈ e
  · simp [hx,Finset.sum_boole,Finset.filter_mem_eq_inter]
  · simp [hx]

/-- Bound the actual total x-to-S incidence by a per-edge capacity. -/
theorem codegree_capacity (H : Simple5Hypergraph V) (x : V) (S : Finset V) (k : ℕ)
    (capacity : ∀ e ∈ H.edges, x ∈ e → (S ∩ e).card ≤ k) :
    (∑ z ∈ S, H.codegree x z) ≤ k*H.degree x := by
  rw [sum_codegrees_subset]
  calc
    _ ≤ ∑ _e ∈ H.edges.filter (fun e => x ∈ e), k := by
      apply Finset.sum_le_sum
      intro e he
      obtain ⟨he,hx⟩ := Finset.mem_filter.mp he
      exact capacity e he hx
    _ = _ := by simp [Simple5Hypergraph.degree,Nat.mul_comm]

/-- A distinguished neighbor uses one unit of the same actual edge capacity. -/
theorem extra_capacity (H : Simple5Hypergraph V) (x y : V) (S : Finset V) (k : ℕ)
    (capacity : ∀ e ∈ H.edges, x ∈ e → (S ∩ e).card ≤ k)
    (extra : ∀ e ∈ H.edges, x ∈ e → y ∈ e → (S ∩ e).card+1 ≤ k) :
    (∑ z ∈ S, H.codegree x z)+H.codegree x y ≤ k*H.degree x := by
  rw [sum_codegrees_subset]
  have hy : H.codegree x y =
      ∑ e ∈ H.edges.filter (fun e => x ∈ e), if y ∈ e then 1 else 0 := by
    simp only [Simple5Hypergraph.codegree,Finset.card_eq_sum_ones,Finset.sum_filter]
    apply Finset.sum_congr rfl
    intro e he
    by_cases hx : x ∈ e <;> simp [hx]
  rw [hy,← Finset.sum_add_distrib]
  calc
    _ ≤ ∑ _e ∈ H.edges.filter (fun e => x ∈ e), k := by
      apply Finset.sum_le_sum
      intro e he
      obtain ⟨he,hx⟩ := Finset.mem_filter.mp he
      by_cases hym : y ∈ e
      · simpa [hym] using extra e he hx hym
      · simpa [hym] using capacity e he hx
    _ = _ := by simp [Simple5Hypergraph.degree,Nat.mul_comm]

/-- Each edge through x has capacity one, spent either on its y incidence or
on one member of S. This is actual edge counting, without a local profile. -/
theorem neighbor_capacity (H : Simple5Hypergraph V) (x y : V) (S : Finset V)
    (atMost : ∀ e ∈ H.edges, x ∈ e → (S ∩ e).card ≤ 1)
    (separate : ∀ e ∈ H.edges, x ∈ e → y ∈ e → ∀ z ∈ S, z ∉ e) :
    (∑ z ∈ S, H.codegree x z) + H.codegree x y ≤ H.degree x := by
  rw [sum_codegrees_subset]
  have hy : H.codegree x y =
      ∑ e ∈ H.edges.filter (fun e => x ∈ e), if y ∈ e then 1 else 0 := by
    simp only [Simple5Hypergraph.codegree,Finset.card_eq_sum_ones,Finset.sum_filter]
    apply Finset.sum_congr rfl
    intro e he
    by_cases hx : x ∈ e <;> simp [hx]
  rw [hy,← Finset.sum_add_distrib]
  calc
    _ ≤ ∑ _e ∈ H.edges.filter (fun e => x ∈ e), 1 := by
      apply Finset.sum_le_sum
      intro e he
      obtain ⟨he,hx⟩ := Finset.mem_filter.mp he
      by_cases hym : y ∈ e
      · have empty : S ∩ e = ∅ := by
          apply Finset.eq_empty_iff_forall_notMem.mpr
          intro z hz
          obtain ⟨hz,hze⟩ := Finset.mem_inter.mp hz
          exact separate e he hx hym z hz hze
        simp [hym,empty]
      · simpa [hym] using atMost e he hx
    _ = H.degree x := by simp [Simple5Hypergraph.degree]
end Aris4Math.ThirtyFour.Incidence
