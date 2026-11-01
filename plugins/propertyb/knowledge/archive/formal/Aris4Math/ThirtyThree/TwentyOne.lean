import Aris4Math.ThirtyThree.TwentyOnePairAssembly
import Aris4Math.ThirtyThree.TwentyOneTriples

/-! Complete 21-point assembly: actual structural selection supplies either a
proved pair case or one of the complete labelled triple configurations. -/

namespace Aris4Math.ThirtyThree.TwentyOneAssembly

open TwentyOneStructure TwentyOnePairAssembly TripleProfiles TwentyOneTriples

def Matches (d e f a b c t : ℕ) (i : Fin 24) : Prop :=
  d = (data i).d ∧ e = (data i).e ∧ f = (data i).f ∧
  a = (data i).a ∧ b = (data i).b ∧ c = (data i).c ∧ t = (data i).t

instance (d e f a b c t : ℕ) (i : Fin 24) : Decidable (Matches d e f a b c t i) := by
  unfold Matches; infer_instance

theorem covers677 : ∀ c t : Fin 3, 1 ≤ c.val → t.val ≤ c.val →
    ∃ i, Matches 6 7 7 2 2 c.val t.val i := by decide +kernel

theorem covers777 : ∀ a b c t : Fin 3,
    1 ≤ a.val → 1 ≤ b.val → 1 ≤ c.val →
    t.val ≤ a.val → t.val ≤ b.val → t.val ≤ c.val →
    ∃ i, Matches 7 7 7 a.val b.val c.val t.val i := by decide +kernel

theorem actual_matches (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (x y z : Fin 21) (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (hcase : TripleCase H x y z) :
    ∃ i, Matches (H.degree x) (H.degree y) (H.degree z)
      (H.codegree x y) (H.codegree x z) (H.codegree y z) (tripleCodegree H x y z) i := by
  have lowerxy := H.one_le_codegree cover xy
  have lowerxz := H.one_le_codegree cover xz
  have loweryz := H.one_le_codegree cover yz
  obtain ⟨txy,txz,tyz⟩ := tripleCodegree_le_pairs H x y z
  rcases hcase with ⟨dx,dy,dz,cxy,cxz,cyz,none⟩ |
    ⟨dx,dy,dz,cxy,cxz,cyz⟩ | ⟨dx,dy,dz,cxy,cxz,cyz,none⟩ |
    ⟨dx,dy,dz,cxy,cxz,cyz⟩
  · have ht := tripleCodegree_zero H x y z none
    refine ⟨0,?_⟩
    rw [dx,dy,dz,cxy,cxz,cyz,ht]
    decide +kernel
  · have tbound : tripleCodegree H x y z < 3 := by omega
    obtain ⟨i,hi⟩ := covers677 ⟨H.codegree y z,by omega⟩
      ⟨tripleCodegree H x y z,tbound⟩ loweryz tyz
    exact ⟨i,by simpa only [dx,dy,dz,cxy,cxz] using hi⟩
  · have ht := tripleCodegree_zero H x y z none
    refine ⟨6,?_⟩
    rw [dx,dy,dz,cxy,cxz,cyz,ht]
    decide +kernel
  · have tbound : tripleCodegree H x y z < 3 := by omega
    obtain ⟨i,hi⟩ := covers777 ⟨H.codegree x y,by omega⟩ ⟨H.codegree x z,by omega⟩
      ⟨H.codegree y z,by omega⟩ ⟨tripleCodegree H x y z,tbound⟩
      lowerxy lowerxz loweryz txy txz tyz
    exact ⟨i,by simpa only [dx,dy,dz] using hi⟩

theorem propertyB_of_tripleCase (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (x y z : Fin 21) (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (hcase : TripleCase H x y z) : PropertyB H := by
  obtain ⟨i,dx,dy,dz,cxy,cxz,cyz,ht⟩ := actual_matches H cover x y z xy xz yz hcase
  have cyx := (H.codegree_comm y x).trans cxy
  have czx := (H.codegree_comm z x).trans cxz
  have czy := (H.codegree_comm z y).trans cyz
  apply propertyB_of_triple_data H cover edges33 (threeVertices x y z xy xz yz) i
  · intro j
    fin_cases j
    · exact dx
    · exact dy
    · exact dz
  · intro j l ne
    fin_cases j <;> fin_cases l
    · exact False.elim (ne rfl)
    · exact cxy
    · exact cxz
    · exact cyx
    · exact False.elim (ne rfl)
    · exact cyz
    · exact czx
    · exact czy
    · exact False.elim (ne rfl)
  · exact ht

end Aris4Math.ThirtyThree.TwentyOneAssembly

namespace Aris4Math.ThirtyThree

theorem twenty_one_propertyB (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) : PropertyB H := by
  obtain pair | triple := TwentyOneStructure.exists_locks_of_twenty_one H cover edges33 (by simp)
  · obtain ⟨x,y,ne,hcase⟩ := pair
    exact TwentyOnePairAssembly.propertyB_of_pairCase H cover edges33 x y ne hcase
  · obtain ⟨x,y,z,xy,xz,yz,hcase⟩ := triple
    exact TwentyOneAssembly.propertyB_of_tripleCase H cover edges33 x y z xy xz yz hcase

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.TwentyOneAssembly.actual_matches
#print axioms Aris4Math.ThirtyThree.twenty_one_propertyB
