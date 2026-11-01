import Aris4Math.ThirtyThree.MultiLockRecovery

/-! Projection of genuine edge types onto any selected subset of locks.
All counts still range over all edges of the same hypergraph. -/

namespace Aris4Math.ThirtyFour.LockProjection

open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery

variable {m n v : ℕ}

/-- The old labels retained by a lock embedding. -/
def project (g : Fin m ↪ Fin n) (U : Finset (Fin n)) : Finset (Fin m) :=
  lockSignature g U

@[simp] theorem mem_project (g : Fin m ↪ Fin n) (U : Finset (Fin n)) (i : Fin m) :
    i ∈ project g U ↔ g i ∈ U := mem_lockSignature g U i

theorem signature_comp (g : Fin m ↪ Fin n) (f : Fin n ↪ Fin v)
    (e : Finset (Fin v)) :
    lockSignature (g.trans f) e = project g (lockSignature f e) := by
  ext i
  simp

theorem count_comp_filter (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (g : Fin m ↪ Fin n) (T : Finset (Fin m)) :
    count H (g.trans f) T =
      ∑ U ∈ Finset.univ.filter (fun U => project g U=T), count H f U := by
  rw [sum_counts]
  unfold count multiplicity fiber
  congr 1
  apply Finset.filter_congr
  intro e _
  simp only [Finset.mem_filter,Finset.mem_univ,true_and,signature_comp]

/-- Complete actual type projection, including the empty type and all edges. -/
theorem count_comp (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (g : Fin m ↪ Fin n) (T : Finset (Fin m)) :
    count H (g.trans f) T =
      ∑ U : Finset (Fin n), if project g U=T then count H f U else 0 := by
  rw [← Finset.sum_filter]
  exact count_comp_filter H f g T

theorem count_le_projected (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (g : Fin m ↪ Fin n) (U : Finset (Fin n)) :
    count H f U ≤ count H (g.trans f) (project g U) := by
  apply Finset.card_le_card
  intro e he
  obtain ⟨inside,typed⟩ := Finset.mem_filter.mp he
  apply Finset.mem_filter.mpr
  refine ⟨inside,?_⟩
  rw [signature_comp,typed]

end Aris4Math.ThirtyFour.LockProjection

#print axioms Aris4Math.ThirtyFour.LockProjection.count_comp
