import Aris4Math.LinkCounting
import Aris4Math.NoLocks

/-! Double counting actual vertex-pair/edge-pair incidences. The twenty-vertex
conclusion uses no pair-covering assumption and no enumeration of hypergraphs. -/

open scoped BigOperators

namespace Aris4Math.GlobalPairs

variable {V : Type*} [Fintype V] [DecidableEq V]

def singletonPairs (H : Simple5Hypergraph V) : Finset (Finset V × Finset V) :=
  H.edges.offDiag.filter (fun p => (p.1 ∩ p.2).card = 1)

def otherPairs (H : Simple5Hypergraph V) : Finset (Finset V × Finset V) :=
  H.edges.offDiag.filter (fun p => (p.1 ∩ p.2).card ≠ 1)

omit [Fintype V] in
theorem pair_partition (H : Simple5Hypergraph V) :
    (singletonPairs H).card + (otherPairs H).card = H.edges.offDiag.card := by
  exact Finset.filter_card_add_filter_neg_card_eq_card _

theorem offDiag_filter {α : Type*} [DecidableEq α] (F : Finset α)
    (p : α → Prop) [DecidablePred p] :
    (F.filter p).offDiag = F.offDiag.filter (fun q => p q.1 ∧ p q.2) := by
  ext q
  simp only [Finset.mem_offDiag, Finset.mem_filter]
  tauto

theorem contained_vertex_pairs (A B : Finset V) :
    ((Finset.univ.powersetCard 2).filter (fun P => P ⊆ A ∧ P ⊆ B)) =
      (A ∩ B).powersetCard 2 := by
  ext P
  simp only [Finset.mem_filter, Finset.mem_powersetCard, Finset.subset_univ, true_and,
    Finset.subset_inter_iff]
  tauto

/-- Every actual five-element edge contains exactly ten unordered vertex pairs. -/
theorem sum_pair_degrees (H : Simple5Hypergraph V) :
    (∑ P ∈ Finset.univ.powersetCard 2, (H.edges.filter (fun e => P ⊆ e)).card) =
      10 * H.edges.card := by
  conv_lhs => simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  calc
    (∑ e ∈ H.edges, ∑ P ∈ Finset.univ.powersetCard 2, if P ⊆ e then 1 else 0) =
        ∑ e ∈ H.edges, e.card.choose 2 := by
      apply Finset.sum_congr rfl
      intro e _
      rw [← Finset.sum_filter, ← Finset.card_eq_sum_ones]
      have heq : ((Finset.univ.powersetCard 2).filter (fun P => P ⊆ e)) =
          e.powersetCard 2 := by
        ext P
        simp [Finset.mem_powersetCard, and_comm]
      rw [heq, Finset.card_powersetCard]
    _ = ∑ _e ∈ H.edges, 10 := by
      apply Finset.sum_congr rfl
      intro e he
      rw [H.five_uniform e he]
      rfl
    _ = 10 * H.edges.card := by simp [Nat.mul_comm]

/-- Count (an unordered vertex pair, an ordered distinct edge pair containing
it) in two orders. All multiplicities come from the actual finite sets. -/
theorem pair_intersection_double_count (H : Simple5Hypergraph V) :
    (∑ P ∈ Finset.univ.powersetCard 2,
      (H.edges.filter (fun e => P ⊆ e)).offDiag.card) =
      ∑ p ∈ H.edges.offDiag, (p.1 ∩ p.2).card.choose 2 := by
  conv_lhs => simp only [offDiag_filter, Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro p _
  rw [← Finset.sum_filter, ← Finset.card_eq_sum_ones, contained_vertex_pairs,
    Finset.card_powersetCard]

theorem twice_le_offDiag_add_two (n : Nat) : 2 * n ≤ (n * n - n) + 2 := by
  cases n with
  | zero => simp
  | succ n =>
      have hsq : n ≤ n * n := Nat.le_mul_self n
      have heq : (n + 1) * (n + 1) - (n + 1) = n * n + n := by
        simp [Nat.add_mul, Nat.mul_add]
      rw [heq]
      omega

/-- At 20 vertices and 32 edges, at least 260 pair-of-pairs incidences exist. -/
theorem intersection_sum_ge_260 (H : Simple5Hypergraph V)
    (vertices20 : Fintype.card V = 20) (edges32 : H.edges.card = 32) :
    260 ≤ ∑ p ∈ H.edges.offDiag, (p.1 ∩ p.2).card.choose 2 := by
  have lower := Finset.sum_le_sum (s := (Finset.univ : Finset V).powersetCard 2)
    (fun P _ => twice_le_offDiag_add_two (H.edges.filter (fun e => P ⊆ e)).card)
  simp only [← Finset.offDiag_card, Finset.sum_add_distrib, ← Finset.mul_sum,
    Finset.sum_const, Finset.card_powersetCard, Finset.card_univ,
    nsmul_eq_mul, Nat.cast_id] at lower
  rw [sum_pair_degrees, pair_intersection_double_count, vertices20, edges32] at lower
  norm_num [Nat.choose] at lower
  omega

omit [Fintype V] in
/-- A distinct pair of five-element edges has at most six common vertex pairs;
a singleton intersection contributes none. -/
theorem intersection_sum_le_six_other (H : Simple5Hypergraph V) :
    (∑ p ∈ H.edges.offDiag, (p.1 ∩ p.2).card.choose 2) ≤
      6 * (otherPairs H).card := by
  calc
    _ ≤ ∑ p ∈ H.edges.offDiag, if (p.1 ∩ p.2).card ≠ 1 then 6 else 0 := by
      apply Finset.sum_le_sum
      intro p hp
      rcases Finset.mem_offDiag.mp hp with ⟨he, hf, hne⟩
      split_ifs with hi
      · exact (Nat.choose_le_choose 2 (H.distinct_edge_inter_card_le_four he hf hne)).trans
          (by decide)
      · simp [not_ne_iff.mp hi]
    _ = 6 * (otherPairs H).card := by
      rw [← Finset.sum_filter]
      simp [otherPairs, Nat.mul_comm]

theorem singletonPairs_le_948_of_eq (H : Simple5Hypergraph V)
    (vertices20 : Fintype.card V = 20) (edges32 : H.edges.card = 32) :
    (singletonPairs H).card ≤ 948 := by
  have lower := intersection_sum_ge_260 H vertices20 edges32
  have upper := intersection_sum_le_six_other H
  have partition := pair_partition H
  rw [Finset.offDiag_card, edges32] at partition
  omega

/-- With fewer than 32 edges there are already at most 930 distinct ordered
pairs. Consequently the same 948 bound holds for every edge count ≤32. -/
theorem singletonPairs_le_948 (H : Simple5Hypergraph V)
    (vertices20 : Fintype.card V = 20) (hE : H.edges.card ≤ 32) :
    (singletonPairs H).card ≤ 948 := by
  by_cases heq : H.edges.card = 32
  · exact singletonPairs_le_948_of_eq H vertices20 heq
  · have h31 : H.edges.card ≤ 31 := by omega
    have hproduct : H.edges.card * (H.edges.card - 1) ≤ 31 * 30 :=
      Nat.mul_le_mul h31 (Nat.sub_le_sub_right h31 1)
    have hsub := Finset.card_le_card (Finset.filter_subset
      (fun p : Finset V × Finset V => (p.1 ∩ p.2).card = 1) H.edges.offDiag)
    have hoff : H.edges.offDiag.card = H.edges.card * (H.edges.card - 1) := by
      rw [Finset.offDiag_card, Nat.mul_sub_left_distrib, Nat.mul_one]
    rw [hoff] at hsub
    change (singletonPairs H).card ≤ _ at hsub
    omega

end Aris4Math.GlobalPairs

namespace Aris4Math.TwentyVertices

open Aris4Math.EndpointCounting Aris4Math.CriticalCounting Aris4Math.NoLocks

/-- Only actual singleton-intersection pairs can contribute to the critical
event. Their structural count now replaces the generic 992 pair count. -/
theorem critical_sum_le (H : Simple5Hypergraph (Fin 20))
    (hE : H.edges.card ≤ 32) (k : Fin 20) :
    (∑ p ∈ H.edges.offDiag, lockedRatio (noLocks 20) (noLocks 20)
      (fun σ => Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k)) ≤
      948 * pairWeight 20 k := by
  classical
  calc
    _ ≤ ∑ p ∈ H.edges.offDiag,
        if (p.1 ∩ p.2).card = 1 then pairWeight 20 k else 0 := by
      apply Finset.sum_le_sum
      intro p hp
      rcases Finset.mem_offDiag.mp hp with ⟨he, hf, hne⟩
      split_ifs with hi
      · exact NoLocks.critical_ratio_le p.1 p.2 (H.five_uniform p.1 he)
          (H.five_uniform p.2 hf) hne k
      · rw [critical_ratio_zero_of_intersection _ _ p.1 p.2 k hi]
    _ = ((GlobalPairs.singletonPairs H).card : ℚ) * pairWeight 20 k := by
      rw [← Finset.sum_filter]
      simp [GlobalPairs.singletonPairs]
    _ ≤ _ := mul_le_mul_of_nonneg_right
      (by exact_mod_cast GlobalPairs.singletonPairs_le_948 H (by simp) hE)
      (pairWeight_nonneg k)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- Closed arithmetic identification of the twenty genuine per-position
probability bounds with Numeric.v20; no hypergraph enumeration is involved. -/
theorem twenty_sum_eq_numeric :
    (∑ k : Fin 20, min (32 * endpointWeight 20 k true)
      (min (32 * endpointWeight 20 k false) (948 * pairWeight 20 k))) =
      Numeric.totalBound Numeric.v20 := by
  decide +kernel

/-- Complete twenty-vertex branch of the original Property B problem. -/
theorem twenty_propertyB (H : Simple5Hypergraph (Fin 20))
    (hE : H.edges.card ≤ 32) : PropertyB H := by
  apply ConditionalUnion.propertyB_of_position_bounds H (noLocks 20) (noLocks 20)
    (fun k => 32 * endpointWeight 20 k true)
    (fun k => 32 * endpointWeight 20 k false)
    (fun k => 948 * pairWeight 20 k)
  · exact fun k => endpoint_sum_le H hE k true
  · exact fun k => endpoint_sum_le H hE k false
  · exact fun k => critical_sum_le H hE k
  · rw [twenty_sum_eq_numeric]
    exact Numeric.v20_lt_one

end Aris4Math.TwentyVertices

#print axioms Aris4Math.GlobalPairs.pair_intersection_double_count
#print axioms Aris4Math.GlobalPairs.singletonPairs_le_948
#print axioms Aris4Math.TwentyVertices.twenty_propertyB
