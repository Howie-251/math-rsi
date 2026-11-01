import Aris4Math.ThirtyFour.TwentyOneSixFiveLocal
import Aris4Math.ThirtyFour.Incidence
namespace Aris4Math.ThirtyFour.TwentyOneSixFiveSelection
set_option maxHeartbeats 0
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open TwentyOneSixFiveCoverage

/-- Select the two common neighbors and a third lock from actual incidence. -/
theorem propertyB_of_unit_set (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y : Fin 21) (kind : Kind) (xy : x≠y) (dx : H.degree x=6)
    (dy : H.degree y=6+kind.val) (cxy : H.codegree x y=2-kind.val)
    (S : Finset (Fin 21)) (large : 7≤S.card)
    (degrees : ∀u∈S,H.degree u=8)
    (units : ∀u∈S,H.codegree x u=1 ∧ H.codegree y u=1)
    (pairs : ∀u∈S,∀v∈S,u≠v→H.codegree u v=2)
    (clean : ∀u∈S,tripleCodegree H x y u=0) : PropertyB H := by
  classical
  have apart (u) (hu : u∈S) : x≠u ∧ y≠u := by
    have du:=degrees u hu
    have kbound:=kind.isLt
    constructor <;> intro eq
    · rw [←eq,dx] at du;omega
    · rw [←eq,dy] at du;omega
  have existsEdge : ∃e∈H.edges,x∈e ∧ 2≤(S∩e).card := by
    by_contra noEdge
    push_neg at noEdge
    have cap:=Incidence.codegree_capacity H x S 1 (fun e he xe=>by have:=noEdge e he xe;omega)
    have sum : (∑u∈S,H.codegree x u)=S.card := by
      calc
        _=∑_u∈S,1 := Finset.sum_congr rfl (fun u hu=>(units u hu).1)
        _=_ := by simp
    rw [sum,dx] at cap
    omega
  obtain ⟨e,he,xe,two⟩:=existsEdge
  obtain ⟨u,hu,v,hv,uv⟩:=Finset.one_lt_card.mp (by omega : 1<(S∩e).card)
  obtain ⟨hu,ue⟩:=Finset.mem_inter.mp hu
  obtain ⟨hv,ve⟩:=Finset.mem_inter.mp hv
  have third : (S\{u,v}).Nonempty := by
    apply Finset.card_pos.mp
    have bound:=Finset.card_sdiff_add_card_inter S ({u,v}:Finset (Fin 21))
    have inter:=Finset.card_le_card (Finset.inter_subset_right : S∩{u,v}⊆({u,v}:Finset (Fin 21)))
    have small : ({u,v}:Finset (Fin 21)).card≤2 := Finset.card_insert_le _ _
    omega
  obtain ⟨w,hw⟩:=third
  obtain ⟨hw,wn⟩:=Finset.mem_sdiff.mp hw
  have uw : u≠w := by intro eq;apply wn; simp [←eq]
  have vw : v≠w := by intro eq;apply wn; simp [←eq]
  let f : Fin 5↪Fin 21:=⟨![x,y,u,v,w],by
    intro i j eq
    fin_cases i <;> fin_cases j <;> simp_all [apart u hu,apart v hv,apart w hw,Ne.symm]⟩
  have hd (j) : H.degree (f j)=degree kind j := by
    fin_cases j <;> simp [f,degree,dx,dy,degrees u hu,degrees v hv,degrees w hw]
  have hc (i j : Fin 5) (ne : i≠j) : H.codegree (f i) (f j)=pair kind i j := by
    have u1:=units u hu;have v1:=units v hv;have w1:=units w hw
    have p1:=pairs u hu v hv uv;have p2:=pairs u hu w hw uw;have p3:=pairs v hv w hw vw
    have yx:=H.codegree_comm y x
    have ux:=H.codegree_comm u x;have vx:=H.codegree_comm v x;have wx:=H.codegree_comm w x
    have uy:=H.codegree_comm u y;have vy:=H.codegree_comm v y;have wy:=H.codegree_comm w y
    have vu:=H.codegree_comm v u;have wu:=H.codegree_comm w u;have wv:=H.codegree_comm w v
    fin_cases i <;> fin_cases j <;> simp +decide [f,pair] at ne ⊢ <;> omega
  have common : tripleCodegree H x u v=1 := by
    have lower : 1≤tripleCodegree H x u v := Finset.one_le_card.mpr
      ⟨e,Finset.mem_filter.mpr ⟨he,xe,ue,ve⟩⟩
    have upper:=(ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x u v).1
    have unit:=(units u hu).1
    omega
  apply TwentyOneSixFiveLocal.propertyB_of_five H size f kind hd hc
  · intro j
    fin_cases j <;> simp [f,TwentyOneSixFiveLocal.tail,clean u hu,clean v hv,clean w hw]
  · exact common
end Aris4Math.ThirtyFour.TwentyOneSixFiveSelection
#print axioms Aris4Math.ThirtyFour.TwentyOneSixFiveSelection.propertyB_of_unit_set
