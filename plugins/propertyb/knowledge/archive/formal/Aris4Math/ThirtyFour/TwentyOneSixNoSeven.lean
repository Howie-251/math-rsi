import Aris4Math.ThirtyFour.TwentyOneSixUnitActual
import Aris4Math.ThirtyFour.TwentyOneSixEquality
set_option simprocs false
namespace Aris4Math.ThirtyFour.TwentyOneSixNoSeven
open Aris4Math.ThirtyThree.QuadProfiles (count highLabels first second)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices high_inventory highPairSum)
open TwentyOneFiveStructure (eights mem_eights)

/-- The unique-six branch with no seven-degree point, from actual input only. -/
theorem propertyB_of_six_no_seven (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (x : Fin 21) (dx : H.degree x=6)
    (minimum : ∀y,y≠x→8≤H.degree y) : PropertyB H := by
  classical
  by_contra noB
  let U:=(eights H).filter (fun u=>H.codegree x u=1)
  have memU (u) : u∈U↔H.degree u=8 ∧ H.codegree x u=1 := by simp [U,mem_eights]
  have usub : U⊆eights H := Finset.filter_subset _ _
  have sub : eights H\U⊆H.badPartners x := by
    intro b hb
    obtain ⟨hb,bout⟩:=Finset.mem_sdiff.mp hb
    have db:=(mem_eights H b).mp hb
    have bx : b≠x := by intro eq;subst b;omega
    have low:=H.one_le_codegree cover bx.symm
    have notUnit : H.codegree x b≠1 := fun h=>bout ((memU b).mpr ⟨db,h⟩)
    exact Finset.mem_filter.mpr ⟨by simp [bx],by omega⟩
  have bad:=H.badPartners_card_le_excess cover x
  rw [dx] at bad
  simp only [Fintype.card_fin] at bad
  have split:=Finset.card_sdiff_add_card_eq_card usub
  have upper:=Finset.card_le_card sub
  have manyL:=TwentyOneSixEquality.eights_at_least_sixteen H size x dx minimum
  have manyU : 7≤U.card := by omega
  have degrees : ∀u∈U,H.degree u=8 := fun u hu=>((memU u).mp hu).1
  have unit : ∀u∈U,H.codegree x u=1 := fun u hu=>((memU u).mp hu).2
  obtain ⟨pairs,capacity⟩:=TwentyOneSixUnitActual.unit_set_structure_of_not_propertyB
    H cover size noB x dx U manyU degrees unit
  obtain ⟨b,u,v,e,db,hu,hv,uv,bout,he,xe,be,ue,ve,xb,ub,vb⟩:=
    TwentyOneSixEquality.select_equality_locks H cover size x dx minimum U memU pairs capacity
  have xu : x≠u := by have:=degrees u hu;intro eq;rw [←eq,dx] at this;omega
  have xv : x≠v := by have:=degrees v hv;intro eq;rw [←eq,dx] at this;omega
  have xne : x≠b := by intro eq;rw [←eq,dx] at db;omega
  have une : u≠b := by intro eq;exact bout (eq ▸ hu)
  have vne : v≠b := by intro eq;exact bout (eq ▸ hv)
  have ubl:=H.one_le_codegree cover une
  have vbl:=H.one_le_codegree cover vne
  let a : Fin 2:=⟨H.codegree u b-1,by omega⟩
  let c : Fin 2:=⟨H.codegree v b-1,by omega⟩
  have ae : a.val+1=H.codegree u b := by dsimp [a];omega
  have ce : c.val+1=H.codegree v b := by dsimp [c];omega
  let f:=fourVertices x u v b xu xv xne uv une vne
  have hd (j) : H.degree (f j)=TwentyOneSixQuad6888Data.degree j := by
    fin_cases j
    · exact dx
    · exact degrees u hu
    · exact degrees v hv
    · exact db
  have coeq (j) : H.codegree (f (first j)) (f (second j))=(![1,1,2,2,a.val+1,c.val+1] : Fin 6→ℕ) j := by
    have uu:=unit u hu;have vu:=unit v hv;have pp:=pairs u hu v hv uv
    fin_cases j <;> simp [f,fourVertices,first,second,ae,ce] <;> first | assumption | rfl
  have positive:=TwentyOneFiveLocal.common_quad H f e he (by
    intro j;fin_cases j <;> assumption)
  have inv0:=high_inventory H f 0
  have inv1:=high_inventory H f 1
  have inv3:=high_inventory H f 3
  have inv4:=high_inventory H f 4
  have inv5:=high_inventory H f 5
  rw [coeq] at inv0 inv1 inv3 inv4 inv5
  change count H f (highLabels 0)+count H f (highLabels 1)+count H f (highLabels 4)≤1 at inv0
  change count H f (highLabels 0)+count H f (highLabels 2)+count H f (highLabels 4)≤1 at inv1
  change count H f (highLabels 0)+count H f (highLabels 3)+count H f (highLabels 4)≤2 at inv3
  change count H f (highLabels 1)+count H f (highLabels 3)+count H f (highLabels 4)≤a.val+1 at inv4
  change count H f (highLabels 2)+count H f (highLabels 3)+count H f (highLabels 4)≤c.val+1 at inv5
  have q1 : count H f (highLabels 4)=1 := by omega
  have h0 : count H f (highLabels 0)=0 := by omega
  have h1 : count H f (highLabels 1)=0 := by omega
  have h2 : count H f (highLabels 2)=0 := by omega
  let h : Fin 2:=⟨count H f (highLabels 3),by omega⟩
  have ha : h.val≤a.val := by dsimp [h];omega
  have hc : h.val≤c.val := by dsimp [h];omega
  obtain ⟨i,pairMatch,highMatch⟩:=TwentyOneSixQuadCoverage.equality_coverage a c h ha hc
  apply noB
  apply TwentyOneSixQuad6888.propertyB_of_data H size f i hd
  · intro j;exact (coeq j).trans (pairMatch j)
  · intro j
    apply Eq.trans _ (highMatch j)
    fin_cases j
    · exact h0
    · exact h1
    · exact h2
    · rfl
    · exact q1
end Aris4Math.ThirtyFour.TwentyOneSixNoSeven
#print axioms Aris4Math.ThirtyFour.TwentyOneSixNoSeven.propertyB_of_six_no_seven
