import Aris4Math.ThirtyFour.TwentyOneEightStructure
namespace Aris4Math.ThirtyFour.TwentyOneEightRules
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.QuadProfiles (count first second highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open TwentyOneEightGraph (eights Unit)

/-- Every actual nonunit pair in the eight-degree set has codegree two. -/
theorem nonunit_two (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,8≤H.degree v) (noB : ¬PropertyB H)
    (x y : Fin 21) (hx : x∈eights H) (hy : y∈eights H) (xy : x≠y) (nonunit : ¬Unit H x y) :
    H.codegree x y=2 := by
  have lower:=H.one_le_codegree cover xy
  have upper:=TwentyOneEightStructure.pair_le_two H cover size minimum noB x hx y hy xy
  have ne : H.codegree x y≠1 := fun eq=>nonunit ⟨xy,eq⟩
  omega

theorem path_isolate (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,8≤H.degree v) (noB : ¬PropertyB H) :
    ∀x∈eights H,∀a∈eights H,∀b∈eights H,∀z∈eights H,
      a≠b→x≠z→a≠z→b≠z→Unit H x a→Unit H x b→
      ¬Unit H x z→¬Unit H a z→¬Unit H b z→False := by
  intro x hx a ha b hb z hz ab xz az bz xa xb nxz naz nbz
  have nab:=TwentyOneEightStructure.triangle_free H cover size noB x hx a ha b hb xa xb
  have cxz:=nonunit_two H cover size minimum noB x z hx hz xz nxz
  have cab:=nonunit_two H cover size minimum noB a b ha hb ab nab
  have caz:=nonunit_two H cover size minimum noB a z ha hz az naz
  have cbz:=nonunit_two H cover size minimum noB b z hb hz bz nbz
  let f:=fourVertices x a b z xa.1 xb.1 xz ab az bz
  have degrees (j) : H.degree (f j)=8 := by
    fin_cases j
    · exact (Finset.mem_filter.mp hx).2
    · exact (Finset.mem_filter.mp ha).2
    · exact (Finset.mem_filter.mp hb).2
    · exact (Finset.mem_filter.mp hz).2
  have res:=TwentyOneEightStructure.quad_residual H cover size minimum noB f degrees
  apply res.1
  funext j
  fin_cases j <;> simp [f,fourVertices,first,second,xa.2,xb.2,cxz,cab,caz,cbz]

theorem cycle_common (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,8≤H.degree v) (noB : ¬PropertyB H) :
    ∀x∈eights H,∀z∈eights H,∀a∈eights H,∀b∈eights H,
      x≠z→a≠b→Unit H x a→Unit H x b→Unit H z a→Unit H z b→
      ¬Unit H x z→¬Unit H a b→∃e∈H.edges,x∈e ∧ z∈e ∧ a∈e ∧ b∈e := by
  intro x hx z hz a ha b hb xz ab xa xb za zb nxz nab
  have cxz:=nonunit_two H cover size minimum noB x z hx hz xz nxz
  have cab:=nonunit_two H cover size minimum noB a b ha hb ab nab
  let f:=fourVertices x z a b xz xa.1 xb.1 za.1 zb.1 ab
  have degrees (j) : H.degree (f j)=8 := by
    fin_cases j
    · exact (Finset.mem_filter.mp hx).2
    · exact (Finset.mem_filter.mp hz).2
    · exact (Finset.mem_filter.mp ha).2
    · exact (Finset.mem_filter.mp hb).2
  have res:=TwentyOneEightStructure.quad_residual H cover size minimum noB f degrees
  have coeq : (fun j=>H.codegree (f (first j)) (f (second j)))=(![2,1,1,1,1,2] : Fin 6→ℕ) := by
    funext j
    fin_cases j <;> simp [f,fourVertices,first,second,xa.2,xb.2,za.2,zb.2,cxz,cab]
  have one : count H f (highLabels 4)=1 :=res.2.1 coeq
  obtain ⟨e,he⟩:=Finset.card_pos.mp (by omega : 0<count H f (highLabels 4))
  obtain ⟨he,sig⟩:=Finset.mem_filter.mp he
  have mem (i : Fin 4) : f i∈e := by
    apply (mem_lockSignature f e i).mp
    rw [sig]
    fin_cases i <;> decide
  exact ⟨e,he,mem 0,mem 1,mem 2,mem 3⟩
end Aris4Math.ThirtyFour.TwentyOneEightRules
#print axioms Aris4Math.ThirtyFour.TwentyOneEightRules.path_isolate
#print axioms Aris4Math.ThirtyFour.TwentyOneEightRules.cycle_common
