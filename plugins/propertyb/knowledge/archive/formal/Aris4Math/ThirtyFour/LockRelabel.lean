import Aris4Math.ThirtyThree.MultiLockRecovery

/-! Relabel actual locks without changing the underlying hypergraph.
The image on the right is essential: a new label `i` denotes the old lock
`σ i`. This transports every actual type count to an orbit representative. -/

namespace Aris4Math.ThirtyFour.LockRelabel

open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery

variable {n v : ℕ}

theorem signature_comp_perm (f : Fin n ↪ Fin v) (σ : Equiv.Perm (Fin n))
    (e : Finset (Fin v)) :
    (lockSignature (σ.toEmbedding.trans f) e).map σ.toEmbedding =
      lockSignature f e := by
  ext i
  simp

theorem count_comp_perm (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (σ : Equiv.Perm (Fin n)) (T : Finset (Fin n)) :
    count H (σ.toEmbedding.trans f) T = count H f (T.map σ.toEmbedding) := by
  unfold count multiplicity fiber
  congr 1
  apply Finset.filter_congr
  intro e _
  constructor
  · intro h
    rw [← signature_comp_perm f σ e, h]
  · intro h
    apply Finset.map_injective σ.toEmbedding
    rw [signature_comp_perm, h]

end Aris4Math.ThirtyFour.LockRelabel
