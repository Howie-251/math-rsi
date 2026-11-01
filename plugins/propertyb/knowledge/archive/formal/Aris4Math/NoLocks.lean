import Aris4Math.CriticalCounting
import Aris4Math.ConditionalUnion
import Aris4Math.Numeric
import Mathlib.Order.Interval.Finset.Fin

/-! The actual unlocked permutation argument, specialized below to 19 vertices.
No hypergraphs or permutations are enumerated. Closed arithmetic is imported
from `Numeric`; this file proves the connection to arbitrary edge sets. -/

namespace Aris4Math.NoLocks

open Aris4Math.EndpointCounting Aris4Math.CriticalCounting

def noLocks (v : ℕ) : Empty ↪ Fin v :=
  ⟨Empty.elim, fun i => i.elim⟩

theorem not_locked {v : ℕ} (x : Fin v) : x ∉ Set.range (noLocks v) := by
  rintro ⟨i, _⟩
  exact i.elim

theorem freePart_card {v : ℕ} (A : Finset (Fin v)) :
    (freePart (noLocks v) A).card = A.card := by
  simp [freePart, Finset.card_subtype]

theorem beforeSlots_card {v : ℕ} (k : Fin v) :
    (beforeSlots (noLocks v) k).card = k.val := by
  rw [beforeSlots_eq_freePart, freePart_card]
  have heq : Finset.univ.filter (fun y : Fin v => y < k) = Finset.Iio k := by
    ext y
    simp
  rw [heq, Fin.card_Iio]

theorem afterSlots_card {v : ℕ} (k : Fin v) :
    (afterSlots (noLocks v) k).card = v - 1 - k.val := by
  rw [afterSlots_eq_freePart, freePart_card]
  have heq : Finset.univ.filter (fun y : Fin v => k < y) = Finset.Ioi k := by
    ext y
    simp
  rw [heq, Fin.card_Ioi]

def endpointWeight (v : ℕ) (k : Fin v) (last : Bool) : ℚ :=
  5 * ((if last then k.val else v - 1 - k.val).choose 4 : ℚ) /
    ((v : ℚ) * ((v - 1).choose 4 : ℚ))

def pairWeight (v : ℕ) (k : Fin v) : ℚ :=
  (k.val.choose 4 : ℚ) * ((v - 1 - k.val).choose 4 : ℚ) /
    ((v : ℚ) * ((v - 1).choose 4 : ℚ) * ((v - 5).choose 4 : ℚ))

theorem endpoint_ratio {v : ℕ} (A : Finset (Fin v)) (hA : A.card = 5)
    (k : Fin v) (last : Bool) :
    lockedRatio (noLocks v) (noLocks v) (fun σ => EndpointAt A σ k last) =
      endpointWeight v k last := by
  rw [free_endpoint_ratio _ _ _ _ (not_locked k)]
  have hcompatible : EndpointCompatible (noLocks v) (noLocks v) A k last := by
    cases last <;> simp [EndpointCompatible, LocksBefore, LocksAfter]
  rw [if_pos hcompatible, freePart_card, hA]
  cases last <;> simp [endpointSlots, beforeSlots_card, afterSlots_card, endpointWeight]

theorem pairWeight_nonneg {v : ℕ} (k : Fin v) : 0 ≤ pairWeight v k := by
  unfold pairWeight
  exact div_nonneg (mul_nonneg (Nat.cast_nonneg _) (Nat.cast_nonneg _))
    (mul_nonneg (mul_nonneg (Nat.cast_nonneg _) (Nat.cast_nonneg _)) (Nat.cast_nonneg _))

theorem endpointWeight_nonneg {v : ℕ} (k : Fin v) (last : Bool) :
    0 ≤ endpointWeight v k last := by
  unfold endpointWeight
  exact div_nonneg (mul_nonneg (by norm_num) (Nat.cast_nonneg _))
    (mul_nonneg (Nat.cast_nonneg _) (Nat.cast_nonneg _))

theorem critical_ratio_le {v : ℕ} (A B : Finset (Fin v))
    (hA : A.card = 5) (hB : B.card = 5) (hneq : A ≠ B) (k : Fin v) :
    lockedRatio (noLocks v) (noLocks v)
      (fun σ => Greedy.CriticalPair (A.map σ.toEmbedding) (B.map σ.toEmbedding) k) ≤
      pairWeight v k := by
  classical
  by_cases hi : (A ∩ B).card = 1
  · obtain ⟨x, hx⟩ := Finset.card_eq_one.mp hi
    have hxA : x ∈ A := (Finset.mem_inter.mp (hx.symm ▸ Finset.mem_singleton_self x)).1
    have hxB : x ∈ B := (Finset.mem_inter.mp (hx.symm ▸ Finset.mem_singleton_self x)).2
    rw [free_critical_ratio _ _ A B x k hneq hx (not_locked x) (not_locked k)]
    have hcompatible : Compatible (noLocks v) (noLocks v) A B x k := by
      simp [Compatible, LocksBefore, LocksAfter]
    rw [if_pos hcompatible]
    simp only [freeLocationWeight, freePart_card, Finset.card_erase_of_mem hxA,
      Finset.card_erase_of_mem hxB, hA, hB, beforeSlots_card, afterSlots_card,
      Fintype.card_empty, Nat.sub_zero]
    simp [pairWeight, Nat.sub_sub]
  · rw [critical_ratio_zero_of_intersection _ _ A B k hi]
    exact pairWeight_nonneg k

theorem endpoint_sum_le {v : ℕ} (H : Simple5Hypergraph (Fin v))
    (hE : H.edges.card ≤ 32) (k : Fin v) (last : Bool) :
    (∑ e ∈ H.edges, lockedRatio (noLocks v) (noLocks v)
      (fun σ => EndpointAt e σ k last)) ≤ 32 * endpointWeight v k last := by
  calc
    _ = ∑ _e ∈ H.edges, endpointWeight v k last := by
      apply Finset.sum_congr rfl
      intro e he
      exact endpoint_ratio e (H.five_uniform e he) k last
    _ = (H.edges.card : ℚ) * endpointWeight v k last := by simp
    _ ≤ _ := mul_le_mul_of_nonneg_right (by exact_mod_cast hE)
      (endpointWeight_nonneg k last)

theorem offDiag_card_le {v : ℕ} (H : Simple5Hypergraph (Fin v))
    (hE : H.edges.card ≤ 32) : H.edges.offDiag.card ≤ 992 := by
  rw [Finset.offDiag_card]
  calc
    H.edges.card * H.edges.card - H.edges.card = H.edges.card * (H.edges.card - 1) := by
      rw [Nat.mul_sub_left_distrib, mul_one]
    _ ≤ 32 * 31 := Nat.mul_le_mul hE (Nat.sub_le_sub_right hE 1)
    _ = 992 := rfl

theorem critical_sum_le {v : ℕ} (H : Simple5Hypergraph (Fin v))
    (hE : H.edges.card ≤ 32) (k : Fin v) :
    (∑ p ∈ H.edges.offDiag, lockedRatio (noLocks v) (noLocks v)
      (fun σ => Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k)) ≤
      992 * pairWeight v k := by
  calc
    _ ≤ ∑ _p ∈ H.edges.offDiag, pairWeight v k := by
      apply Finset.sum_le_sum
      intro p hp
      rcases Finset.mem_offDiag.mp hp with ⟨hpA, hpB, hpne⟩
      exact critical_ratio_le p.1 p.2 (H.five_uniform p.1 hpA)
        (H.five_uniform p.2 hpB) hpne k
    _ = (H.edges.offDiag.card : ℚ) * pairWeight v k := by simp
    _ ≤ _ := mul_le_mul_of_nonneg_right (by exact_mod_cast offDiag_card_le H hE)
      (pairWeight_nonneg k)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- This finite computation concerns the nineteen explicit rational formulas,
not a search through graphs, colorings, or permutations. It identifies the
actual no-lock event bounds with the existing Numeric certificate. -/
theorem nineteen_sum_eq_numeric :
    (∑ k : Fin 19, min (32 * endpointWeight 19 k true)
      (min (32 * endpointWeight 19 k false) (992 * pairWeight 19 k))) =
      Numeric.totalBound Numeric.v19 := by
  decide +kernel

theorem nineteen_sum_lt_one :
    (∑ k : Fin 19, min (32 * endpointWeight 19 k true)
      (min (32 * endpointWeight 19 k false) (992 * pairWeight 19 k))) < 1 := by
  rw [nineteen_sum_eq_numeric]
  exact Numeric.v19_lt_one

/-- Every simple 5-uniform hypergraph on nineteen vertices with at most
32 edges is 2-colorable. All event bounds are derived above for the actual
hypergraph, and the final witness is obtained from its greedy coloring. -/
theorem nineteen_propertyB (H : Simple5Hypergraph (Fin 19))
    (hE : H.edges.card ≤ 32) : PropertyB H := by
  apply ConditionalUnion.propertyB_of_position_bounds H (noLocks 19) (noLocks 19)
    (fun k => 32 * endpointWeight 19 k true)
    (fun k => 32 * endpointWeight 19 k false)
    (fun k => 992 * pairWeight 19 k)
  · exact fun k => endpoint_sum_le H hE k true
  · exact fun k => endpoint_sum_le H hE k false
  · exact fun k => critical_sum_le H hE k
  · exact nineteen_sum_lt_one

end Aris4Math.NoLocks

#print axioms Aris4Math.NoLocks.endpoint_ratio
#print axioms Aris4Math.NoLocks.critical_ratio_le
#print axioms Aris4Math.NoLocks.endpoint_sum_le
#print axioms Aris4Math.NoLocks.critical_sum_le
#print axioms Aris4Math.NoLocks.nineteen_sum_eq_numeric
#print axioms Aris4Math.NoLocks.nineteen_propertyB
