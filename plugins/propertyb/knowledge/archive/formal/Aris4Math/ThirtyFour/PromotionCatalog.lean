import Aris4Math.ThirtyFour.LockExtension
import Aris4Math.ThirtyFour.BoundedAllocations

/-! Actual lock extensions belong to the capacity-pruned local catalogue.
The list contains distinct old trace types. Capacities bound the new degree
and its codegrees with the old locks; no independence of edges is assumed. -/

namespace Aris4Math.ThirtyFour.PromotionCatalog

open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.LockExtension

variable {n v : ℕ}

theorem sum_promotion_codegree (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (i : Fin n) :
    (∑ T : Finset (Fin n), if i ∈ T then promotion H f T else 0) =
      H.codegree (f i.castSucc) (f (Fin.last n)) := by
  rw [← Finset.sum_filter]
  simp_rw [promotion_eq_through_fiber]
  rw [Finset.sum_card_fiberwise_eq_card_filter]
  unfold Simple5Hypergraph.codegree
  congr 1
  ext e
  simp only [Finset.mem_filter, Finset.mem_univ, true_and, mem_lockSignature]
  change ((e ∈ H.edges ∧ f (Fin.last n) ∈ e) ∧ f i.castSucc ∈ e) ↔ _
  tauto

/-- `none` charges one new incidence; `some i` charges its pair with old i. -/
def cost (T : Finset (Fin n)) : Option (Fin n) → ℕ
  | none => 1
  | some i => if i ∈ T then 1 else 0

def actualCap (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) : Option (Fin n) → ℕ
  | none => H.degree (f (Fin.last n))
  | some i => H.codegree (f i.castSucc) (f (Fin.last n))

theorem sum_promotion_cost (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (j : Option (Fin n)) :
    (∑ T : Finset (Fin n), promotion H f T * cost T j) = actualCap H f j := by
  cases j with
  | none => simpa [cost, actualCap] using sum_promotion_degree H f
  | some i =>
    simpa [cost, actualCap, mul_ite] using sum_promotion_codegree H f i

/-- Distinct listed types use no more capacity than all actual edge types. -/
theorem listed_budget (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (entries : List (Finset (Fin n) × ℕ))
    (distinct : (entries.map Prod.fst).Nodup) (j : Option (Fin n)) :
    (entries.map (fun e => promotion H f e.1 * cost e.1 j)).sum ≤ actualCap H f j := by
  calc
    _ = ((entries.map Prod.fst).map (fun T => promotion H f T * cost T j)).sum := by
      simp only [List.map_map, Function.comp_def]
    _ = ∑ T ∈ (entries.map Prod.fst).toFinset, promotion H f T * cost T j :=
      (List.sum_toFinset _ distinct).symm
    _ ≤ ∑ T : Finset (Fin n), promotion H f T * cost T j :=
      Finset.sum_le_sum_of_subset (Finset.subset_univ _)
    _ = actualCap H f j := sum_promotion_cost H f j

/-- Every actual promotion vector is retained by the recursive catalogue.
Bounds may be smaller than the old count if separately proved, e.g. from
a pair-codegree cap. -/
theorem actual_mem (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (entries : List (Finset (Fin n) × ℕ))
    (cap : Option (Fin n) → ℕ)
    (distinct : (entries.map Prod.fst).Nodup)
    (bounds : ∀ e ∈ entries, promotion H f e.1 ≤ e.2)
    (capacity : ∀ j, actualCap H f j ≤ cap j) :
    entries.map (fun e => promotion H f e.1) ∈
      BoundedAllocations.enumerate cost entries cap := by
  apply BoundedAllocations.mem_enumerate cost entries cap (promotion H f) bounds
  intro j
  exact (listed_budget H f entries distinct j).trans (capacity j)

/-- A catalogue built from the actual old inventory is complete. -/
theorem actual_mem_of_old (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (entries : List (Finset (Fin n) × ℕ))
    (cap : Option (Fin n) → ℕ)
    (distinct : (entries.map Prod.fst).Nodup)
    (bounds : ∀ e ∈ entries, count H (restrict f) e.1 ≤ e.2)
    (capacity : ∀ j, actualCap H f j ≤ cap j) :
    entries.map (fun e => promotion H f e.1) ∈
      BoundedAllocations.enumerate cost entries cap := by
  apply actual_mem H f entries cap distinct ?_ capacity
  intro e he
  exact (promotion_le_old H f e.1).trans (bounds e he)

/-- Exact readback of every nonempty promotion; the omitted empty promotion
is recovered from the new degree by LockExtension.count_new_singleton. -/
theorem decode_nonempty (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (entries : List (Finset (Fin n) × ℕ))
    (support : ∀ T, T ≠ ∅ → T ∉ entries.map Prod.fst → promotion H f T=0)
    (T : Finset (Fin n)) (nonempty : T ≠ ∅) :
    BoundedAllocations.decode entries (entries.map (fun e => promotion H f e.1)) T =
      promotion H f T := by
  rw [BoundedAllocations.decode_map]
  by_cases h : T ∈ entries.map Prod.fst
  · simp [h]
  · simp [h, support T nonempty h]

end Aris4Math.ThirtyFour.PromotionCatalog

#print axioms Aris4Math.ThirtyFour.PromotionCatalog.actual_mem
#print axioms Aris4Math.ThirtyFour.PromotionCatalog.decode_nonempty
