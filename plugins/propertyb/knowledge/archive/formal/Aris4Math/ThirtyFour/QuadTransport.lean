import Aris4Math.ThirtyThree.QuadProfiles

/-! Exact transport of actual edge traces under a permutation of four locks.
Used to apply a numeric representative to a relabelled actual input. -/
namespace Aris4Math.ThirtyFour.QuadTransport
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.QuadProfiles
variable {v : ℕ}

def vertices (p : Equiv.Perm (Fin 4)) (f : Fin 4 ↪ Fin v) : Fin 4 ↪ Fin v :=
  p.toEmbedding.trans f

theorem signature_image (p : Equiv.Perm (Fin 4)) (f : Fin 4 ↪ Fin v)
    (e : Finset (Fin v)) :
    (lockSignature (vertices p f) e).image p = lockSignature f e := by
  ext j
  simp only [Finset.mem_image,mem_lockSignature]
  constructor
  · rintro ⟨i,hi,rfl⟩
    exact hi
  · intro h
    refine ⟨p.symm j,?_,p.apply_symm_apply j⟩
    simpa [vertices] using h

theorem count_permute (H : Simple5Hypergraph (Fin v))
    (p : Equiv.Perm (Fin 4)) (f : Fin 4 ↪ Fin v) (T : Finset (Fin 4)) :
    count H (vertices p f) T = count H f (T.image p) := by
  unfold count multiplicity fiber
  congr 1
  ext e
  simp only [Finset.mem_filter]
  constructor
  · rintro ⟨he,hT⟩
    refine ⟨he,?_⟩
    rw [← signature_image p f e,hT]
  · rintro ⟨he,hT⟩
    refine ⟨he,?_⟩
    apply Finset.image_injective p.injective
    rw [signature_image,hT]
end Aris4Math.ThirtyFour.QuadTransport
