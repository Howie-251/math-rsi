import Aris4Math.ThirtyThree.GlobalPairs

/-! Actual no-lock probability bounds for all simple five-uniform hypergraphs
on nineteen vertices with at most thirty-three edges. No profile-realization,
pair-covering, or supplied probability assumptions are required. -/

namespace Aris4Math.ThirtyThree.Nineteen

open Aris4Math.EndpointCounting Aris4Math.CriticalCounting Aris4Math.NoLocks
open scoped BigOperators

/-- Sum the real endpoint probabilities, retaining the new edge bound. -/
theorem endpoint_sum_le {v : ℕ} (H : Simple5Hypergraph (Fin v))
    (hE : H.edges.card ≤ 33) (k : Fin v) (last : Bool) :
    (∑ e ∈ H.edges, lockedRatio (noLocks v) (noLocks v)
      (fun σ => EndpointAt e σ k last)) ≤ 33 * endpointWeight v k last := by
  calc
    _ = ∑ _e ∈ H.edges, endpointWeight v k last := by
      apply Finset.sum_congr rfl
      intro e he
      exact endpoint_ratio e (H.five_uniform e he) k last
    _ = (H.edges.card : ℚ) * endpointWeight v k last := by simp
    _ ≤ _ := mul_le_mul_of_nonneg_right (by exact_mod_cast hE)
      (endpointWeight_nonneg k last)

/-- Non-singleton intersections contribute zero to the true critical event.
The remaining count is bounded by a theorem of the actual edge set. -/
theorem critical_sum_le (H : Simple5Hypergraph (Fin 19))
    (hE : H.edges.card ≤ 33) (k : Fin 19) :
    (∑ p ∈ H.edges.offDiag, lockedRatio (noLocks 19) (noLocks 19)
      (fun σ => Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k)) ≤
      1003 * pairWeight 19 k := by
  classical
  calc
    _ ≤ ∑ p ∈ H.edges.offDiag,
        if (p.1 ∩ p.2).card = 1 then pairWeight 19 k else 0 := by
      apply Finset.sum_le_sum
      intro p hp
      rcases Finset.mem_offDiag.mp hp with ⟨he, hf, hne⟩
      split_ifs with hi
      · exact NoLocks.critical_ratio_le p.1 p.2 (H.five_uniform p.1 he)
          (H.five_uniform p.2 hf) hne k
      · rw [critical_ratio_zero_of_intersection _ _ p.1 p.2 k hi]
    _ = ((Aris4Math.GlobalPairs.singletonPairs H).card : ℚ) * pairWeight 19 k := by
      rw [← Finset.sum_filter]
      simp [Aris4Math.GlobalPairs.singletonPairs]
    _ ≤ _ := mul_le_mul_of_nonneg_right
      (by exact_mod_cast ThirtyThree.GlobalPairs.singletonPairs_le_1003 H (by simp) hE)
      (pairWeight_nonneg k)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- Only nineteen explicit rational formulas are evaluated by the kernel.
This is not enumeration of hypergraphs, colorings or permutations. -/
theorem nineteen_sum_value :
    (∑ k : Fin 19, min (33 * endpointWeight 19 k true)
      (min (33 * endpointWeight 19 k false) (1003 * pairWeight 19 k))) =
        (228354 / 230945 : ℚ) := by
  decide +kernel

theorem nineteen_sum_lt_one :
    (∑ k : Fin 19, min (33 * endpointWeight 19 k true)
      (min (33 * endpointWeight 19 k false) (1003 * pairWeight 19 k))) < 1 := by
  rw [nineteen_sum_value]
  norm_num

/-- Complete nineteen-vertex branch of T33, for the actual original object. -/
theorem nineteen_propertyB (H : Simple5Hypergraph (Fin 19))
    (hE : H.edges.card ≤ 33) : PropertyB H := by
  apply ConditionalUnion.propertyB_of_position_bounds H (noLocks 19) (noLocks 19)
    (fun k => 33 * endpointWeight 19 k true)
    (fun k => 33 * endpointWeight 19 k false)
    (fun k => 1003 * pairWeight 19 k)
  · exact fun k => endpoint_sum_le H hE k true
  · exact fun k => endpoint_sum_le H hE k false
  · exact fun k => critical_sum_le H hE k
  · exact nineteen_sum_lt_one

end Aris4Math.ThirtyThree.Nineteen

#print axioms Aris4Math.ThirtyThree.GlobalPairs.singletonPairs_le_1003
#print axioms Aris4Math.ThirtyThree.Nineteen.nineteen_propertyB
