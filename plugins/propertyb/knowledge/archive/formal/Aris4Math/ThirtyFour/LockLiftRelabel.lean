import Aris4Math.ThirtyFour.LockExtension
import Mathlib.Logic.Equiv.Fin.Basic

/-! Relabel the old locks while keeping the newly added last lock fixed. -/

namespace Aris4Math.ThirtyFour.LockLiftRelabel

variable {n v : ℕ}

/-- Conjugate σ ⊕ id through the standard Fin n ⊕ Fin 1 decomposition. -/
def lift (σ : Equiv.Perm (Fin n)) : Equiv.Perm (Fin (n + 1)) :=
  finSumFinEquiv.symm.trans
    ((Equiv.sumCongr σ (Equiv.refl (Fin 1))).trans finSumFinEquiv)

@[simp] theorem lift_castSucc (σ : Equiv.Perm (Fin n)) (i : Fin n) :
    lift σ i.castSucc = (σ i).castSucc := by
  simp only [lift, Equiv.trans_apply, finSumFinEquiv_symm_apply_castSucc,
    Equiv.sumCongr_apply, Sum.map_inl, finSumFinEquiv_apply_left]
  apply Fin.ext
  rfl

@[simp] theorem lift_last (σ : Equiv.Perm (Fin n)) :
    lift σ (Fin.last n) = Fin.last n := by
  simp only [lift, Equiv.trans_apply, finSumFinEquiv_symm_last,
    Equiv.sumCongr_apply, Sum.map_inr, Equiv.refl_apply, finSumFinEquiv_apply_right]
  apply Fin.ext
  simp

/-- Relabeling an actual extension restricts to exactly the prescribed old
relabeling, with the same actual new vertex retained. -/
theorem restrict_lift_trans (σ : Equiv.Perm (Fin n)) (f : Fin (n + 1) ↪ Fin v) :
    LockExtension.restrict ((lift σ).toEmbedding.trans f) =
      σ.toEmbedding.trans (LockExtension.restrict f) := by
  apply Function.Embedding.ext
  intro i
  change f (lift σ i.castSucc) = f ((σ i).castSucc)
  rw [lift_castSucc]

@[simp] theorem new_vertex_lift_trans (σ : Equiv.Perm (Fin n))
    (f : Fin (n + 1) ↪ Fin v) :
    ((lift σ).toEmbedding.trans f) (Fin.last n) = f (Fin.last n) := by
  change f (lift σ (Fin.last n)) = f (Fin.last n)
  rw [lift_last]

end Aris4Math.ThirtyFour.LockLiftRelabel

#print axioms Aris4Math.ThirtyFour.LockLiftRelabel.restrict_lift_trans
