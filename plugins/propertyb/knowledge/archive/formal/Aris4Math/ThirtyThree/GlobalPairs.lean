import Aris4Math.GlobalPairs

/-! Global pair counting for the thirty-three-edge problem. All sets and
incidence multiplicities below come from the given hypergraph. -/

namespace Aris4Math.ThirtyThree.GlobalPairs

open Aris4Math.GlobalPairs
open scoped BigOperators

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- A parameter-free lower bound from counting vertex-pair/edge-pair incidences.
The right side uses ordered distinct edge pairs. -/
theorem intersection_sum_lower (H : Simple5Hypergraph V) :
    20 * H.edges.card ≤
      (∑ p ∈ H.edges.offDiag, (p.1 ∩ p.2).card.choose 2) +
        2 * (Fintype.card V).choose 2 := by
  have lower := Finset.sum_le_sum (s := (Finset.univ : Finset V).powersetCard 2)
    (fun P _ => twice_le_offDiag_add_two (H.edges.filter (fun e => P ⊆ e)).card)
  simp only [← Finset.offDiag_card, Finset.sum_add_distrib, ← Finset.mul_sum,
    Finset.sum_const, Finset.card_powersetCard, Finset.card_univ,
    nsmul_eq_mul, Nat.cast_id] at lower
  rw [sum_pair_degrees, pair_intersection_double_count] at lower
  omega

/-- At nineteen vertices and thirty-three edges there are at least 318 ordered
pair-of-pairs incidences. -/
theorem intersection_sum_ge_318 (H : Simple5Hypergraph V)
    (vertices19 : Fintype.card V = 19) (edges33 : H.edges.card = 33) :
    318 ≤ ∑ p ∈ H.edges.offDiag, (p.1 ∩ p.2).card.choose 2 := by
  have lower := intersection_sum_lower H
  rw [vertices19, edges33] at lower
  norm_num [Nat.choose] at lower
  omega

/-- The unrounded ordered-incidence estimate suffices here: at least 53 of the
1056 ordered distinct edge pairs are not singleton-intersecting. The sharper
parity-rounded cap 1002 is not needed for the nineteen-vertex theorem. -/
theorem singletonPairs_le_1003_of_eq (H : Simple5Hypergraph V)
    (vertices19 : Fintype.card V = 19) (edges33 : H.edges.card = 33) :
    (singletonPairs H).card ≤ 1003 := by
  have lower := intersection_sum_ge_318 H vertices19 edges33
  have upper := intersection_sum_le_six_other H
  have partition := pair_partition H
  rw [Finset.offDiag_card, edges33] at partition
  omega

/-- Fewer than 33 edges already have at most 992 ordered distinct pairs. -/
theorem singletonPairs_le_1003 (H : Simple5Hypergraph V)
    (vertices19 : Fintype.card V = 19) (hE : H.edges.card ≤ 33) :
    (singletonPairs H).card ≤ 1003 := by
  by_cases heq : H.edges.card = 33
  · exact singletonPairs_le_1003_of_eq H vertices19 heq
  · have h32 : H.edges.card ≤ 32 := by omega
    have hproduct : H.edges.card * (H.edges.card - 1) ≤ 32 * 31 :=
      Nat.mul_le_mul h32 (Nat.sub_le_sub_right h32 1)
    have hsub := Finset.card_le_card (Finset.filter_subset
      (fun p : Finset V × Finset V => (p.1 ∩ p.2).card = 1) H.edges.offDiag)
    have hoff : H.edges.offDiag.card = H.edges.card * (H.edges.card - 1) := by
      rw [Finset.offDiag_card, Nat.mul_sub_left_distrib, Nat.mul_one]
    rw [hoff] at hsub
    change (singletonPairs H).card ≤ _ at hsub
    omega

end Aris4Math.ThirtyThree.GlobalPairs
