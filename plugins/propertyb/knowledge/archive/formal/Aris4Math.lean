import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# A verification spine for the Property B proof

`Target` is a proposition, not a proved theorem. The theorems below establish
the finite-event and weighted-deletion interface used in P6/P7 of
`proofs/PROBABILITY_LEMMAS.md`. They do not establish its hypergraph inputs.
All weights are rational; subtraction is ordinary subtraction, not truncated
natural-number subtraction. The finite sample space need not be enumerated.
-/

open scoped BigOperators

namespace Aris4Math

universe u v w

/-- D1: simple edges (a finite set of finite sets), each with five vertices. -/
structure Simple5Hypergraph (V : Type u) where
  edges : Finset (Finset V)
  five_uniform : ∀ e ∈ edges, e.card = 5

/-- D2 in its literal count form: every edge has between one and four red vertices.
No balance, regularity, pair-covering, or restriction on vertex count is imposed. -/
def PropertyB {V : Type u} (H : Simple5Hypergraph V) : Prop :=
  ∃ c : V → Bool, ∀ e ∈ H.edges,
    1 ≤ (e.filter (fun x => c x = true)).card ∧
    (e.filter (fun x => c x = true)).card ≤ 4

/-- The original target T. This declaration deliberately asserts no proof of T. -/
def Target : Prop :=
  ∀ (V : Type u) [Fintype V] (H : Simple5Hypergraph V),
    H.edges.card ≤ 32 → PropertyB H

section FiniteEvents

variable {Ω : Type u} {K : Type v} [DecidableEq Ω]

/-- The finite union bound, before any probability normalization. -/
theorem card_event_cover_le
    (bad : Finset Ω) (positions : Finset K) (event : K → Finset Ω)
    (cover : bad ⊆ positions.biUnion event) :
    bad.card ≤ ∑ k ∈ positions, (event k).card := by
  exact (Finset.card_le_card cover).trans Finset.card_biUnion_le

/-- P7a and its existence consequence. Inputs `A,B,C,D` are bounds measured
in sample-space counts (probability bounds multiplied by the sample size).
The strict comparison itself guarantees the sample space is nonempty.

The hypotheses are the unproved application interface: event coverage,
three event bounds, and the final strict arithmetic inequality. -/
theorem exists_outside_bad_of_min_bounds
    (sample bad : Finset Ω) (positions : Finset K) (event : K → Finset Ω)
    (A B C D : K → ℚ)
    (cover : bad ⊆ positions.biUnion event)
    (boundA : ∀ k ∈ positions, ((event k).card : ℚ) ≤ A k)
    (boundB : ∀ k ∈ positions, ((event k).card : ℚ) ≤ B k)
    (boundC : ∀ k ∈ positions, ((event k).card : ℚ) ≤ C k - D k)
    (strict : (∑ k ∈ positions, min (A k) (min (B k) (C k - D k))) <
      (sample.card : ℚ)) :
    ∃ outcome ∈ sample, outcome ∉ bad := by
  have hcard : (bad.card : ℚ) ≤ ∑ k ∈ positions, ((event k).card : ℚ) := by
    rw [← Nat.cast_sum]
    exact_mod_cast card_event_cover_le bad positions event cover
  have hmin : (∑ k ∈ positions, ((event k).card : ℚ)) ≤
      ∑ k ∈ positions, min (A k) (min (B k) (C k - D k)) := by
    apply Finset.sum_le_sum
    intro k hk
    exact le_min (boundA k hk) (le_min (boundB k hk) (boundC k hk))
  have hltRat : (bad.card : ℚ) < (sample.card : ℚ) :=
    lt_of_le_of_lt (hcard.trans hmin) strict
  have hlt : bad.card < sample.card := by exact_mod_cast hltRat
  by_contra no_good
  have all_bad : sample ⊆ bad := by
    intro outcome hsample
    by_contra hbad
    exact no_good ⟨outcome, hsample, hbad⟩
  exact (not_le_of_gt hlt) (Finset.card_le_card all_bad)

end FiniteEvents

section WeightedDeletion

variable {P : Type w} [DecidableEq P]

/-- P6: disjoint, individually identified bad pairs may be deleted with their
actual weights. Finsets prevent repeated deletion; nonnegative weights permit
enlarging the contributing set. Weights may be zero and need not be symmetric.
For the application, P is the type of ordered distinct edge pairs. -/
theorem weighted_deletion_bound
    (all contributing deleted : Finset P) (weight : P → ℚ) (d : ℚ)
    (contributing_subset : contributing ⊆ all)
    (deleted_subset : deleted ⊆ all)
    (separate : Disjoint contributing deleted)
    (nonnegative : ∀ p ∈ all, 0 ≤ weight p)
    (deletion_lower_bound : d ≤ ∑ p ∈ deleted, weight p) :
    (∑ p ∈ contributing, weight p) ≤ (∑ p ∈ all, weight p) - d := by
  have union_subset : contributing ∪ deleted ⊆ all :=
    Finset.union_subset contributing_subset deleted_subset
  have hsum : (∑ p ∈ contributing ∪ deleted, weight p) ≤
      ∑ p ∈ all, weight p := by
    apply Finset.sum_le_sum_of_subset_of_nonneg union_subset
    intro p hp _
    exact nonnegative p hp
  rw [Finset.sum_union separate] at hsum
  linarith

/-- Even when C decreases by d, the minimum need not decrease by d.
This is the exact P7b identity, proved for arbitrary rational inputs and d ≥ 0. -/
theorem minimum_decrease (L C d : ℚ) (hd : 0 ≤ d) :
    min L C - min L (C - d) = max 0 (d - max 0 (C - L)) := by
  rcases le_total C L with hCL | hLC
  · have hCdL : C - d ≤ L := by linarith
    have hCL0 : C - L ≤ 0 := by linarith
    rw [min_eq_right hCL, min_eq_right hCdL, max_eq_left hCL0]
    rw [sub_zero, max_eq_right hd]
    linarith
  · rw [min_eq_left hLC, max_eq_right (sub_nonneg.mpr hLC)]
    rcases le_total (C - d) L with hCdL | hLCd
    · rw [min_eq_right hCdL, max_eq_right (by linarith)]
      linarith
    · rw [min_eq_left hLCd, max_eq_left (by linarith)]
      linarith

end WeightedDeletion

section CombinedInterface

variable {Ω : Type u} {K : Type v} {P : Type w}
  [DecidableEq Ω] [DecidableEq P]

/-- P6 followed by P7 in one theorem. Every position has its own sets and
weights, so deleting a pair at two different positions is allowed; deleting
one pair twice at the same position is impossible in a Finset.

No probability formula, greedy-algorithm coverage, or structural selection
lemma is hidden here: they are explicit hypotheses of this interface. -/
theorem exists_outside_bad_of_weighted_deletion
    (sample bad : Finset Ω) (positions : Finset K) (event : K → Finset Ω)
    (all contributing deleted : K → Finset P) (weight : K → P → ℚ)
    (A B D : K → ℚ)
    (cover : bad ⊆ positions.biUnion event)
    (boundA : ∀ k ∈ positions, ((event k).card : ℚ) ≤ A k)
    (boundB : ∀ k ∈ positions, ((event k).card : ℚ) ≤ B k)
    (pair_cover : ∀ k ∈ positions,
      ((event k).card : ℚ) ≤ ∑ p ∈ contributing k, weight k p)
    (contributing_subset : ∀ k ∈ positions, contributing k ⊆ all k)
    (deleted_subset : ∀ k ∈ positions, deleted k ⊆ all k)
    (separate : ∀ k ∈ positions, Disjoint (contributing k) (deleted k))
    (nonnegative : ∀ k ∈ positions, ∀ p ∈ all k, 0 ≤ weight k p)
    (deletion_lower_bound : ∀ k ∈ positions,
      D k ≤ ∑ p ∈ deleted k, weight k p)
    (strict : (∑ k ∈ positions,
      min (A k) (min (B k) ((∑ p ∈ all k, weight k p) - D k))) <
      (sample.card : ℚ)) :
    ∃ outcome ∈ sample, outcome ∉ bad := by
  apply exists_outside_bad_of_min_bounds sample bad positions event A B
    (fun k => ∑ p ∈ all k, weight k p) D cover boundA boundB
  · intro k hk
    exact (pair_cover k hk).trans
      (weighted_deletion_bound (all k) (contributing k) (deleted k) (weight k) (D k)
        (contributing_subset k hk) (deleted_subset k hk) (separate k hk)
        (nonnegative k hk) (deletion_lower_bound k hk))
  · exact strict

end CombinedInterface

end Aris4Math

#print axioms Aris4Math.card_event_cover_le
#print axioms Aris4Math.exists_outside_bad_of_min_bounds
#print axioms Aris4Math.weighted_deletion_bound
#print axioms Aris4Math.minimum_decrease
#print axioms Aris4Math.exists_outside_bad_of_weighted_deletion
