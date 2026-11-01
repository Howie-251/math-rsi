import Aris4Math.CriticalCounting

/-! The actual locked greedy experiment, from event covers to Property B. -/

namespace Aris4Math.ConditionalUnion

open Equiv
open scoped BigOperators
open Aris4Math.Counting Aris4Math.EndpointCounting Aris4Math.CriticalCounting

variable {v : ℕ} {ι : Type*} [Fintype ι]

theorem lockedRatio_nonnegative (vertices positions : ι ↪ Fin v) (P : Perm (Fin v) → Prop) :
    0 ≤ lockedRatio vertices positions P := by
  classical
  unfold lockedRatio
  exact div_nonneg (Nat.cast_nonneg _) (Nat.cast_nonneg _)

/-- Union bound on the real locked-permutation sample space. -/
theorem lockedRatio_union_bound {K : Type*}
    (vertices positions : ι ↪ Fin v) (keys : Finset K)
    (P : Perm (Fin v) → Prop) (Q : K → Perm (Fin v) → Prop)
    (cover : ∀ σ : Locked vertices positions, P σ.1 → ∃ k ∈ keys, Q k σ.1) :
    lockedRatio vertices positions P ≤ ∑ k ∈ keys, lockedRatio vertices positions (Q k) := by
  classical
  have hcard : Fintype.card {σ : Locked vertices positions // P σ.1} ≤
      ∑ k ∈ keys, Fintype.card {σ : Locked vertices positions // Q k σ.1} := by
    simp_rw [Fintype.card_subtype]
    apply Aris4Math.card_event_cover_le
    intro σ hσ
    obtain ⟨k, hk, hQ⟩ := cover σ (Finset.mem_filter.mp hσ).2
    exact Finset.mem_biUnion.mpr ⟨k, hk, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hQ⟩⟩
  unfold lockedRatio
  rw [← Finset.sum_div]
  apply div_le_div_of_nonneg_right _ (Nat.cast_nonneg _)
  rw [← Nat.cast_sum]
  exact_mod_cast hcard

/-- A real critical event is covered by actual single-edge endpoint events. -/
theorem critical_ratio_le_endpoint_sum (vertices positions : ι ↪ Fin v)
    (E : Finset (Finset (Fin v))) (k : Fin v) (last : Bool) :
    lockedRatio vertices positions (fun σ => Aris4Math.Greedy.CriticalAt E σ k) ≤
      ∑ e ∈ E, lockedRatio vertices positions (fun σ => EndpointAt e σ k last) := by
  apply lockedRatio_union_bound
  intro σ h
  obtain ⟨A, hA, B, hB, _, hp⟩ := h
  have he := critical_implies_endpoints A B σ.1 k hp
  cases last with
  | false => exact ⟨B, hB, he.2⟩
  | true => exact ⟨A, hA, he.1⟩

/-- The pair cover retains ordered, distinct original edge identities. -/
theorem critical_ratio_le_pair_sum (vertices positions : ι ↪ Fin v)
    (E : Finset (Finset (Fin v))) (k : Fin v) :
    lockedRatio vertices positions (fun σ => Aris4Math.Greedy.CriticalAt E σ k) ≤
      ∑ p ∈ E.offDiag, lockedRatio vertices positions (fun σ =>
        Aris4Math.Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k) := by
  apply lockedRatio_union_bound
  intro σ h
  obtain ⟨A, hA, B, hB, hneq, hp⟩ := h
  exact ⟨(A, B), Finset.mem_offDiag.mpr ⟨hA, hB, hneq⟩, hp⟩

/-- The greedy failure implication has been proved by the actual scan. This
theorem now transports it into the true uniform locked sample probability. -/
theorem failure_ratio_le_critical_sum (H : Aris4Math.Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) :
    lockedRatio vertices positions (Aris4Math.Greedy.FailureAt H.edges) ≤
      ∑ k : Fin v, lockedRatio vertices positions (fun σ => Aris4Math.Greedy.CriticalAt H.edges σ k) := by
  apply lockedRatio_union_bound
  intro σ h
  obtain ⟨k, hk⟩ := Aris4Math.Greedy.failureAt_covered H.edges 5 (by decide) H.five_uniform σ.1 h
  exact ⟨k, Finset.mem_univ _, hk⟩

/-- Three independently justified per-position bounds apply to the same
critical event, hence their minimum bounds it. No probability formula or
greedy event-cover assumption is hidden in the hypotheses. -/
theorem failure_ratio_le_position_bounds (H : Aris4Math.Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (A B C : Fin v → ℚ)
    (boundA : ∀ k, (∑ e ∈ H.edges,
      lockedRatio vertices positions (fun σ => EndpointAt e σ k true)) ≤ A k)
    (boundB : ∀ k, (∑ e ∈ H.edges,
      lockedRatio vertices positions (fun σ => EndpointAt e σ k false)) ≤ B k)
    (boundC : ∀ k, (∑ p ∈ H.edges.offDiag, lockedRatio vertices positions (fun σ =>
      Aris4Math.Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k)) ≤ C k) :
    lockedRatio vertices positions (Aris4Math.Greedy.FailureAt H.edges) ≤
      ∑ k : Fin v, min (A k) (min (B k) (C k)) := by
  apply (failure_ratio_le_critical_sum H vertices positions).trans
  apply Finset.sum_le_sum
  intro k _
  exact le_min ((critical_ratio_le_endpoint_sum vertices positions H.edges k true).trans (boundA k))
    (le_min ((critical_ratio_le_endpoint_sum vertices positions H.edges k false).trans (boundB k))
      ((critical_ratio_le_pair_sum vertices positions H.edges k).trans (boundC k)))

/-- A probability strictly below one yields an actual successful permutation,
whose coloring was already proved to satisfy the original PropertyB definition. -/
theorem propertyB_of_failure_ratio_lt_one (H : Aris4Math.Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v)
    (hsmall : lockedRatio vertices positions (Aris4Math.Greedy.FailureAt H.edges) < 1) :
    Aris4Math.PropertyB H := by
  classical
  by_contra hnot
  have hall (σ : Locked vertices positions) : Aris4Math.Greedy.FailureAt H.edges σ.1 := by
    by_contra hgood
    exact hnot (Aris4Math.Greedy.propertyB_of_successful_permutation H σ.1 hgood)
  have hnz : (Fintype.card (Locked vertices positions) : ℚ) ≠ 0 := by
    rw [card_prescribed_images]
    exact Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _)
  have hone : lockedRatio vertices positions (Aris4Math.Greedy.FailureAt H.edges) = 1 := by
    unfold lockedRatio
    rw [Fintype.card_congr (Equiv.subtypeUnivEquiv hall), div_self hnz]
  exact (ne_of_lt hsmall) hone

/-- Main application interface: actual endpoint and ordered-pair sums, bounded
at each position, imply Property B when the sum of their minima is below one. -/
theorem propertyB_of_position_bounds (H : Aris4Math.Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (A B C : Fin v → ℚ)
    (boundA : ∀ k, (∑ e ∈ H.edges,
      lockedRatio vertices positions (fun σ => EndpointAt e σ k true)) ≤ A k)
    (boundB : ∀ k, (∑ e ∈ H.edges,
      lockedRatio vertices positions (fun σ => EndpointAt e σ k false)) ≤ B k)
    (boundC : ∀ k, (∑ p ∈ H.edges.offDiag, lockedRatio vertices positions (fun σ =>
      Aris4Math.Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k)) ≤ C k)
    (strict : (∑ k : Fin v, min (A k) (min (B k) (C k))) < 1) : Aris4Math.PropertyB H := by
  exact propertyB_of_failure_ratio_lt_one H vertices positions
    (lt_of_le_of_lt (failure_ratio_le_position_bounds H vertices positions A B C boundA boundB boundC)
      strict)

/-- P6 with actual original ordered edge pairs. Identified non-singleton
intersection pairs have zero actual probability; their bookkeeping weights
can therefore be deleted once each. Directional weights may differ or vanish. -/
theorem pair_sum_le_weighted_deletion (vertices positions : ι ↪ Fin v)
    (E : Finset (Finset (Fin v))) (k : Fin v)
    (weight : Finset (Fin v) × Finset (Fin v) → ℚ)
    (deleted : Finset (Finset (Fin v) × Finset (Fin v))) (d : ℚ)
    (upper : ∀ p ∈ E.offDiag, lockedRatio vertices positions (fun σ =>
      Aris4Math.Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k) ≤ weight p)
    (subset : deleted ⊆ E.offDiag)
    (bad : ∀ p ∈ deleted, (p.1 ∩ p.2).card ≠ 1)
    (deletion_lower : d ≤ ∑ p ∈ deleted, weight p) :
    (∑ p ∈ E.offDiag, lockedRatio vertices positions (fun σ =>
      Aris4Math.Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k)) ≤
      (∑ p ∈ E.offDiag, weight p) - d := by
  classical
  let probability := fun p : Finset (Fin v) × Finset (Fin v) =>
    lockedRatio vertices positions (fun σ => Aris4Math.Greedy.CriticalPair
      (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k)
  have hzero : ∑ p ∈ deleted, probability p = 0 := by
    apply Finset.sum_eq_zero
    intro p hp
    exact critical_ratio_zero_of_intersection vertices positions p.1 p.2 k (bad p hp)
  change (∑ p ∈ E.offDiag, probability p) ≤ _
  rw [← Finset.sum_sdiff subset, hzero, add_zero]
  apply (Finset.sum_le_sum (fun p hp => upper p (Finset.mem_sdiff.mp hp).1)).trans
  exact Aris4Math.weighted_deletion_bound E.offDiag (E.offDiag \ deleted) deleted weight d
    Finset.sdiff_subset subset Finset.sdiff_disjoint
    (fun p hp => (lockedRatio_nonnegative vertices positions _).trans (upper p hp)) deletion_lower

/-- Full application interface including actual bad-pair deletion. Structural
work supplies the distinct deleted pairs and their weighted lower bound; all
event coverage, probability normalization, minimum handling and final coloring
existence are proved here. -/
theorem propertyB_of_weighted_position_bounds (H : Aris4Math.Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (A B C D : Fin v → ℚ)
    (weight : Fin v → Finset (Fin v) × Finset (Fin v) → ℚ)
    (deleted : Fin v → Finset (Finset (Fin v) × Finset (Fin v)))
    (boundA : ∀ k, (∑ e ∈ H.edges,
      lockedRatio vertices positions (fun σ => EndpointAt e σ k true)) ≤ A k)
    (boundB : ∀ k, (∑ e ∈ H.edges,
      lockedRatio vertices positions (fun σ => EndpointAt e σ k false)) ≤ B k)
    (upper : ∀ k, ∀ p ∈ H.edges.offDiag, lockedRatio vertices positions (fun σ =>
      Aris4Math.Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k) ≤ weight k p)
    (boundC : ∀ k, (∑ p ∈ H.edges.offDiag, weight k p) ≤ C k)
    (subset : ∀ k, deleted k ⊆ H.edges.offDiag)
    (bad : ∀ k, ∀ p ∈ deleted k, (p.1 ∩ p.2).card ≠ 1)
    (deletion_lower : ∀ k, D k ≤ ∑ p ∈ deleted k, weight k p)
    (strict : (∑ k : Fin v, min (A k) (min (B k) (C k - D k))) < 1) :
    Aris4Math.PropertyB H := by
  apply propertyB_of_position_bounds H vertices positions A B (fun k => C k - D k)
    boundA boundB _ strict
  intro k
  exact (pair_sum_le_weighted_deletion vertices positions H.edges k (weight k) (deleted k) (D k)
    (upper k) (subset k) (bad k) (deletion_lower k)).trans (sub_le_sub_right (boundC k) (D k))

end Aris4Math.ConditionalUnion

#print axioms Aris4Math.ConditionalUnion.lockedRatio_union_bound
#print axioms Aris4Math.ConditionalUnion.failure_ratio_le_position_bounds
#print axioms Aris4Math.ConditionalUnion.propertyB_of_failure_ratio_lt_one
#print axioms Aris4Math.ConditionalUnion.propertyB_of_position_bounds
#print axioms Aris4Math.ConditionalUnion.pair_sum_le_weighted_deletion
#print axioms Aris4Math.ConditionalUnion.propertyB_of_weighted_position_bounds
