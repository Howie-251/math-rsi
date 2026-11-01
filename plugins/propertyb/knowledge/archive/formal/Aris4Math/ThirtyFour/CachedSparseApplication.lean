import Aris4Math.ThirtyFour.CachedRows

/-! Sparse profiles cover all actual edges through positive actual multiplicities.
A complete powerset listing is unnecessary. -/
namespace Aris4Math.ThirtyFour.CachedSparseApplication
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery

/-- Every actual edge has positive multiplicity at its own trace. -/
theorem self_count_pos (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (e : Finset (Fin v)) (he : e ∈ H.edges) :
    0 < count H vertices (lockSignature vertices e) := by
  unfold count multiplicity fiber
  apply Finset.card_pos.mpr
  exact ⟨e, by simp [he]⟩

/-- The support condition replaces complete powerset enumeration. It is not an
extra condition on H: finite certificate data discharge it at every caller. -/
theorem realizes_sparse (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v)
    (labels : List (Finset (Fin n))) (nodup : labels.Nodup)
    (μ : Finset (Fin n) → ℕ) (support : ∀ T, μ T ≠ 0 → T ∈ labels)
    (counts : ∀ T,count H vertices T=μ T)
    (centers : List ℕ) (valid : Numeric.validProfile (rawProfile labels positions μ centers) m) :
    RealizesProfile H vertices positions (rawProfile labels positions μ centers) m := by
  refine ⟨rfl, valid, ?_, ?_⟩
  · simp [rawProfile,canonicalType]
  · constructor
    · simpa only [rawProfile,List.map_map,Function.comp_def] using
        nodup.map (canonicalType_injective positions)
    · intro e he
      have hc : μ (lockSignature vertices e) ≠ 0 := by
        rw [← counts]; exact ne_of_gt (self_count_pos H vertices e he)
      have hs := support _ hc
      change canonicalType positions (lockSignature vertices e) ∈
        (labels.map fun T => (⟨canonicalType positions T,μ T⟩ : Numeric.EdgeType)).map Numeric.EdgeType.locks
      simp only [List.map_map,List.mem_map]
      exact ⟨_,hs,rfl⟩
    · intro t ht
      obtain ⟨T,_,rfl⟩ := List.mem_map.mp ht
      exact (position_fiber_count H vertices positions T).trans (counts T)

theorem propertyB_of_sparse_counts (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v)
    (labels : List (Finset (Fin n))) (nodup : labels.Nodup)
    (μ : Finset (Fin n) → ℕ) (support : ∀ T, μ T ≠ 0 → T ∈ labels)
    (counts : ∀ T,count H vertices T=μ T)
    (valid : Numeric.validProfile (rawProfile labels positions μ []) m)
    (strict : (∑ k : Fin v,
      min (CachedRows.cachedA (rawProfile labels positions μ []) (k.val+1) true)
      (min (CachedRows.cachedA (rawProfile labels positions μ []) (k.val+1) false)
        (CachedRows.cachedC (rawProfile labels positions μ []) (k.val+1))))<1) : PropertyB H := by
  exact CachedRows.propertyB_of_cached H vertices positions _ m
    (realizes_sparse H vertices positions labels nodup μ support counts [] valid) rfl strict
end Aris4Math.ThirtyFour.CachedSparseApplication
#print axioms Aris4Math.ThirtyFour.CachedSparseApplication.propertyB_of_sparse_counts
