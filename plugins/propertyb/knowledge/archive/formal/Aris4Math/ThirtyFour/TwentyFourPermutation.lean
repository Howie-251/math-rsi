import Aris4Math.ThirtyFour.LockRelabel

namespace Aris4Math.ThirtyFour.TwentyFourPermutation
/-- A compact genuine permutation built from five swaps. The input is a
factoradic index; bijectivity comes from composition, not a 720-row test. -/
def perm (p : Fin 720) : Equiv.Perm (Fin 6) :=
  (((((Equiv.swap 0 (⟨p.val%6,by omega⟩ : Fin 6)).trans
      (Equiv.swap 1 ⟨1+(p.val/6)%5,by omega⟩)).trans
      (Equiv.swap 2 ⟨2+(p.val/30)%4,by omega⟩)).trans
      (Equiv.swap 3 ⟨3+(p.val/120)%3,by omega⟩)).trans
      (Equiv.swap 4 ⟨4+(p.val/360)%2,by omega⟩))
/-- A new lock label i denotes the old label perm p i. Hence the actual
count at T is read at the forward image of T, as used by the lookup table. -/
theorem count_comp {v : ℕ} (H : Simple5Hypergraph (Fin v)) (f : Fin 6↪Fin v)
    (p : Fin 720) (T : Finset (Fin 6)) :
    Aris4Math.ThirtyThree.MultiLockRecovery.count H ((perm p).toEmbedding.trans f) T =
      Aris4Math.ThirtyThree.MultiLockRecovery.count H f (T.map (perm p).toEmbedding) :=
  LockRelabel.count_comp_perm H f (perm p) T
end Aris4Math.ThirtyFour.TwentyFourPermutation
#print axioms Aris4Math.ThirtyFour.TwentyFourPermutation.count_comp
