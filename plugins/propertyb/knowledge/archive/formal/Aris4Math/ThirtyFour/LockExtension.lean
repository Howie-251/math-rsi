import Aris4Math.ThirtyThree.MultiLockRecovery
import Mathlib.Data.Fin.Embedding
import Mathlib.Data.Fin.SuccPred

/-! Exact trace promotion when one actual lock vertex is added.
Every old fiber is partitioned by membership of the new vertex in the same
edge. All promotion values are counts of actual edges; no profile validity or
independence assumption is used. -/

namespace Aris4Math.ThirtyFour.LockExtension

open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery

variable {n v : ℕ}

/-- Retain the first n actual locks. -/
def restrict (f : Fin (n + 1) ↪ Fin v) : Fin n ↪ Fin v :=
  Fin.castSuccEmb.trans f

/-- The old trace with the new, last lock adjoined. -/
def promoted (T : Finset (Fin n)) : Finset (Fin (n + 1)) :=
  insert (Fin.last n) (T.map Fin.castSuccEmb)

/-- Number of actual edges promoted from this old trace. This definition
includes the old empty trace, whose promotion is the new singleton trace. -/
def promotion (H : Simple5Hypergraph (Fin v)) (f : Fin (n + 1) ↪ Fin v)
    (T : Finset (Fin n)) : ℕ :=
  count H f (promoted T)

@[simp] theorem last_notMem_map (T : Finset (Fin n)) :
    Fin.last n ∉ T.map Fin.castSuccEmb := by
  simp [Finset.mem_map, Fin.castSuccEmb_apply, Fin.castSucc_ne_last]

@[simp] theorem castSucc_mem_map (T : Finset (Fin n)) (i : Fin n) :
    i.castSucc ∈ T.map Fin.castSuccEmb ↔ i ∈ T :=
  Finset.mem_map' Fin.castSuccEmb

@[simp] theorem castSucc_mem_promoted (T : Finset (Fin n)) (i : Fin n) :
    i.castSucc ∈ promoted T ↔ i ∈ T := by
  simp [promoted, Fin.castSucc_ne_last]

/-- A trace without the last label is exactly an old trace on an edge
avoiding the new actual vertex. -/
theorem signature_without_iff (f : Fin (n + 1) ↪ Fin v)
    (e : Finset (Fin v)) (T : Finset (Fin n)) :
    lockSignature f e = T.map Fin.castSuccEmb ↔
      lockSignature (restrict f) e = T ∧ f (Fin.last n) ∉ e := by
  constructor
  · intro same
    constructor
    · ext i
      have atOld := Finset.ext_iff.mp same i.castSucc
      simpa [restrict] using atOld
    · intro mem
      have atLast : Fin.last n ∈ lockSignature f e := (mem_lockSignature f e _).mpr mem
      rw [same] at atLast
      exact last_notMem_map T atLast
  · rintro ⟨old, absent⟩
    ext i
    refine Fin.lastCases ?_ (fun j => ?_) i
    · simp [absent]
    · have atOld := Finset.ext_iff.mp old j
      simpa [restrict] using atOld

/-- A trace with the last label is exactly an old trace on an edge
containing the new actual vertex. -/
theorem signature_with_iff (f : Fin (n + 1) ↪ Fin v)
    (e : Finset (Fin v)) (T : Finset (Fin n)) :
    lockSignature f e = promoted T ↔
      lockSignature (restrict f) e = T ∧ f (Fin.last n) ∈ e := by
  constructor
  · intro same
    constructor
    · ext i
      have atOld := Finset.ext_iff.mp same i.castSucc
      simpa [restrict] using atOld
    · apply (mem_lockSignature f e _).mp
      rw [same]
      exact Finset.mem_insert_self _ _
  · rintro ⟨old, present⟩
    ext i
    refine Fin.lastCases ?_ (fun j => ?_) i
    · simp [promoted, present]
    · have atOld := Finset.ext_iff.mp old j
      simpa [restrict] using atOld

theorem count_without_eq_filtered_old (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) (T : Finset (Fin n)) :
    count H f (T.map Fin.castSuccEmb) =
      ((fiber H.edges (lockSignature (restrict f)) T).filter
        fun e => f (Fin.last n) ∉ e).card := by
  unfold count multiplicity fiber
  congr 1
  ext e
  simp only [Finset.mem_filter, signature_without_iff]
  tauto

theorem promotion_eq_filtered_old (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) (T : Finset (Fin n)) :
    promotion H f T =
      ((fiber H.edges (lockSignature (restrict f)) T).filter
        fun e => f (Fin.last n) ∈ e).card := by
  unfold promotion count multiplicity fiber
  congr 1
  ext e
  simp only [Finset.mem_filter, signature_with_iff]
  tauto

/-- The exact split of every actual old fiber into its two possible new
traces. The equality also holds for the old empty trace. -/
theorem count_split (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) (T : Finset (Fin n)) :
    count H (restrict f) T =
      count H f (T.map Fin.castSuccEmb) + promotion H f T := by
  rw [count_without_eq_filtered_old, promotion_eq_filtered_old]
  have split := Finset.filter_card_add_filter_neg_card_eq_card
    (s := fiber H.edges (lockSignature (restrict f)) T)
    (fun e => f (Fin.last n) ∈ e)
  change (fiber H.edges (lockSignature (restrict f)) T).card = _
  omega

theorem promotion_le_old (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) (T : Finset (Fin n)) :
    promotion H f T ≤ count H (restrict f) T := by
  have split := count_split H f T
  omega

/-- The unpromoted new multiplicity is obtained by subtracting precisely
the promoted edges from this same old fiber. -/
theorem count_without_new (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) (T : Finset (Fin n)) :
    count H f (T.map Fin.castSuccEmb) = count H (restrict f) T - promotion H f T := by
  have split := count_split H f T
  omega

theorem count_with_new (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) (T : Finset (Fin n)) :
    count H f (insert (Fin.last n) (T.map Fin.castSuccEmb)) = promotion H f T := rfl

theorem promotion_eq_through_fiber (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) (T : Finset (Fin n)) :
    promotion H f T =
      ((H.edges.filter fun e => f (Fin.last n) ∈ e).filter
        fun e => lockSignature (restrict f) e = T).card := by
  unfold promotion count multiplicity fiber
  congr 1
  ext e
  simp only [Finset.mem_filter, signature_with_iff]
  tauto

/-- All old traces, including the empty one, partition the actual edges
through the new vertex. Thus promotions sum to its actual degree. -/
theorem sum_promotion_degree (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) :
    (∑ T : Finset (Fin n), promotion H f T) = H.degree (f (Fin.last n)) := by
  simp_rw [promotion_eq_through_fiber]
  have sum := Finset.sum_card_fiberwise_eq_card_filter
    (H.edges.filter fun e => f (Fin.last n) ∈ e)
    (Finset.univ : Finset (Finset (Fin n))) (lockSignature (restrict f))
  simpa [Simple5Hypergraph.degree] using sum

/-- A five-element old trace cannot also contain the new distinct lock
inside an actual five-element edge. -/
theorem promotion_eq_zero_of_large (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) (T : Finset (Fin n)) (large : 5 ≤ T.card) :
    promotion H f T = 0 := by
  apply count_eq_zero_of_large H f (promoted T)
  rw [promoted, Finset.card_insert_of_notMem (last_notMem_map T), Finset.card_map]
  omega

/-- When a local promotion table stores only nonempty old traces, the
new singleton count is the remaining part of the actual new degree. -/
theorem count_new_singleton (H : Simple5Hypergraph (Fin v))
    (f : Fin (n + 1) ↪ Fin v) :
    count H f {Fin.last n} = H.degree (f (Fin.last n)) -
      ∑ T ∈ (Finset.univ : Finset (Finset (Fin n))).erase ∅, promotion H f T := by
  have sum := Finset.sum_erase_add (s := (Finset.univ : Finset (Finset (Fin n))))
    (promotion H f) (Finset.mem_univ (∅ : Finset (Fin n)))
  rw [sum_promotion_degree] at sum
  have singleton : promotion H f ∅ = count H f {Fin.last n} := by
    simp [promotion, promoted]
  rw [singleton] at sum
  omega

end Aris4Math.ThirtyFour.LockExtension

#print axioms Aris4Math.ThirtyFour.LockExtension.count_split
#print axioms Aris4Math.ThirtyFour.LockExtension.sum_promotion_degree
#print axioms Aris4Math.ThirtyFour.LockExtension.promotion_eq_zero_of_large
#print axioms Aris4Math.ThirtyFour.LockExtension.count_new_singleton
