import Aris4Math.ThirtyFour.PromotionCatalog
import Aris4Math.ThirtyFour.LockProjection

/-! Read a finite promotion certificate as the complete actual new inventory,
including the empty type and the new singleton. -/
namespace Aris4Math.ThirtyFour.PromotionReconstruction

open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.LockExtension
open Aris4Math.ThirtyFour.LockProjection

variable {n v : ℕ}

def oldTrace (U : Finset (Fin (n+1))) : Finset (Fin n) :=
  project Fin.castSuccEmb U

theorem without_last (U : Finset (Fin (n+1))) (absent : Fin.last n ∉ U) :
    U = (oldTrace U).map Fin.castSuccEmb := by
  ext i
  refine Fin.lastCases ?_ (fun j => ?_) i
  · simp [absent]
  · simp [oldTrace]

theorem with_last (U : Finset (Fin (n+1))) (present : Fin.last n ∈ U) :
    U = promoted (oldTrace U) := by
  ext i
  refine Fin.lastCases ?_ (fun j => ?_) i
  · simp [promoted, present]
  · simp [oldTrace]

/-- Recover the omitted empty promotion from the new vertex degree. -/
def fillEmpty (p : Finset (Fin n) → ℕ) (d : ℕ) (T : Finset (Fin n)) : ℕ :=
  if T=∅ then d-∑ S ∈ (Finset.univ : Finset (Finset (Fin n))).erase ∅, p S
  else p T

def extend (μ p : Finset (Fin n) → ℕ) (d : ℕ) (U : Finset (Fin (n+1))) : ℕ :=
  if Fin.last n ∈ U then fillEmpty p d (oldTrace U)
  else μ (oldTrace U)-fillEmpty p d (oldTrace U)

theorem fillEmpty_actual (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (p : Finset (Fin n) → ℕ) (d : ℕ)
    (actual : ∀ T, T≠∅ → p T=promotion H f T)
    (degree : H.degree (f (Fin.last n))=d) (T : Finset (Fin n)) :
    fillEmpty p d T=promotion H f T := by
  by_cases empty : T=∅
  · subst T
    have sums :
        (∑ S ∈ (Finset.univ : Finset (Finset (Fin n))).erase ∅, p S) =
        ∑ S ∈ (Finset.univ : Finset (Finset (Fin n))).erase ∅, promotion H f S := by
      apply Finset.sum_congr rfl
      intro S hS
      exact actual S (Finset.mem_erase.mp hS).1
    simp only [fillEmpty, if_pos rfl, sums]
    rw [← degree, ← count_new_singleton]
    simp [promotion, promoted]
  · simp [fillEmpty, empty, actual T empty]

/-- An exact actual-input connection, for all new types rather than only
the nonempty entries stored in a local table. -/
theorem extend_actual (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (μ p : Finset (Fin n) → ℕ) (d : ℕ)
    (old : ∀ T, count H (restrict f) T=μ T)
    (promotions : ∀ T, T≠∅ → p T=promotion H f T)
    (degree : H.degree (f (Fin.last n))=d) (U : Finset (Fin (n+1))) :
    count H f U=extend μ p d U := by
  unfold extend
  rw [fillEmpty_actual H f p d promotions degree]
  by_cases present : Fin.last n ∈ U
  · rw [if_pos present]
    conv_lhs => rw [with_last U present]
    rfl
  · rw [if_neg present]
    conv_lhs => rw [without_last U present]
    rw [count_without_new,old]

end Aris4Math.ThirtyFour.PromotionReconstruction

#print axioms Aris4Math.ThirtyFour.PromotionReconstruction.extend_actual
