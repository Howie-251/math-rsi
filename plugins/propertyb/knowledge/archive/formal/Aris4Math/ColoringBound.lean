import Aris4Math.Greedy

/-!
The actual greedy failure event is connected to the generic finite-event bound
and to the project's literal Property B definition. The event bounds remain
explicit mathematical obligations: this module does not prove that they hold
for one of the numerical profiles.
-/

open scoped BigOperators

namespace Aris4Math.ColoringBound

variable {v : ℕ}

/-- Three upper bounds on the actual critical-pair events, whose positionwise
minimum sums to less than the sample size, produce a valid two-coloring. -/
theorem propertyB_of_critical_bounds
    (H : Simple5Hypergraph (Fin v))
    (sample : Finset (Equiv.Perm (Fin v)))
    (A B C D : Fin v → ℚ)
    (boundA : ∀ k, ((Greedy.criticalPermutations H.edges sample k).card : ℚ) ≤ A k)
    (boundB : ∀ k, ((Greedy.criticalPermutations H.edges sample k).card : ℚ) ≤ B k)
    (boundC : ∀ k, ((Greedy.criticalPermutations H.edges sample k).card : ℚ) ≤ C k - D k)
    (strict : (∑ k : Fin v, min (A k) (min (B k) (C k - D k))) <
      (sample.card : ℚ)) : PropertyB H := by
  classical
  obtain ⟨σ, hsample, hgood⟩ := exists_outside_bad_of_min_bounds
    sample (Greedy.badPermutations H.edges sample) Finset.univ
    (Greedy.criticalPermutations H.edges sample) A B C D
    (Greedy.failure_event_cover H.edges 5 (by decide) H.five_uniform sample)
    (fun k _ => boundA k) (fun k _ => boundB k) (fun k _ => boundC k) strict
  apply Greedy.propertyB_of_successful_permutation H σ
  intro hfail
  apply hgood
  exact Finset.mem_filter.mpr ⟨hsample, hfail⟩

/-- P6's explicitly identified, distinct ordered pairs can supply the third
bound. All set/weight premises are exposed; the conclusion is original PB. -/
theorem propertyB_of_weighted_critical_bounds
    {P : Type*} [DecidableEq P]
    (H : Simple5Hypergraph (Fin v))
    (sample : Finset (Equiv.Perm (Fin v)))
    (all contributing deleted : Fin v → Finset P) (weight : Fin v → P → ℚ)
    (A B D : Fin v → ℚ)
    (boundA : ∀ k, ((Greedy.criticalPermutations H.edges sample k).card : ℚ) ≤ A k)
    (boundB : ∀ k, ((Greedy.criticalPermutations H.edges sample k).card : ℚ) ≤ B k)
    (pair_cover : ∀ k, ((Greedy.criticalPermutations H.edges sample k).card : ℚ) ≤
      ∑ p ∈ contributing k, weight k p)
    (contributing_subset : ∀ k, contributing k ⊆ all k)
    (deleted_subset : ∀ k, deleted k ⊆ all k)
    (separate : ∀ k, Disjoint (contributing k) (deleted k))
    (nonnegative : ∀ k, ∀ p ∈ all k, 0 ≤ weight k p)
    (deletion_lower_bound : ∀ k, D k ≤ ∑ p ∈ deleted k, weight k p)
    (strict : (∑ k : Fin v,
      min (A k) (min (B k) ((∑ p ∈ all k, weight k p) - D k))) <
      (sample.card : ℚ)) : PropertyB H := by
  apply propertyB_of_critical_bounds H sample A B
    (fun k => ∑ p ∈ all k, weight k p) D boundA boundB
  · intro k
    exact (pair_cover k).trans
      (weighted_deletion_bound (all k) (contributing k) (deleted k) (weight k) (D k)
        (contributing_subset k) (deleted_subset k) (separate k) (nonnegative k)
        (deletion_lower_bound k))
  · exact strict

end Aris4Math.ColoringBound

#print axioms Aris4Math.ColoringBound.propertyB_of_critical_bounds
#print axioms Aris4Math.ColoringBound.propertyB_of_weighted_critical_bounds
