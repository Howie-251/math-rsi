import Aris4Math.ThirtyFour.TwentyOneSixFiveSelection
import Aris4Math.ThirtyFour.TwentyOneSixUnitActual
namespace Aris4Math.ThirtyFour.TwentyOneSixOneSeven
open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.ThirtyThree.QuadProfiles (count highLabels first second)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open TwentyOneSixStructure
open TwentyOneFiveStructure (eights mem_eights)

/-- The full actual four-lock residual, with no profile supplied by the caller. -/
theorem pair_residual (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬PropertyB H) (x y u v : Fin 21)
    (xy : x≠y) (xu : x≠u) (xv : x≠v) (yu : y≠u) (yv : y≠v) (uv : u≠v)
    (dx : H.degree x=6) (dy : H.degree y=7) (du : H.degree u=8) (dv : H.degree v=8)
    (unitu : H.codegree x u=1) (unitv : H.codegree x v=1) (pairuv : H.codegree u v=2) :
    (H.codegree x y=2 ∧ H.codegree y u=1 ∧ H.codegree y v=1 ∧
      tripleCodegree H x y u=0 ∧ tripleCodegree H x y v=0) ∨
    (H.codegree x y=1 ∧ H.codegree y u=H.codegree y v ∧
      ∀e∈H.edges,x∈e→y∈e→u∈e→v∈e→False) := by
  have ru:=residual_678 H cover size noB x y u xy xu yu dx dy du
  have rv:=residual_678 H cover size noB x y v xy xv yv dx dy dv
  have al:=H.one_le_codegree cover xy
  have bl:=H.one_le_codegree cover yu
  have cl:=H.one_le_codegree cover yv
  let a : Fin 2:=⟨H.codegree x y-1,by omega⟩
  let b : Fin 2:=⟨H.codegree y u-1,by omega⟩
  let c : Fin 2:=⟨H.codegree y v-1,by omega⟩
  have ae : a.val+1=H.codegree x y := by dsimp [a];omega
  have be : b.val+1=H.codegree y u := by dsimp [b];omega
  have ce : c.val+1=H.codegree y v := by dsimp [c];omega
  let f:=fourVertices x y u v xy xu xv yu yv uv
  have hd (j) : H.degree (f j)=TwentyOneSixQuad6788Data.degree j := by
    fin_cases j <;> simp [f,fourVertices,TwentyOneSixQuad6788Data.degree,dx,dy,du,dv]
  have hc (j) : H.codegree (f (first j)) (f (second j))=
      TwentyOneSixQuadCoverage.co6788 (a.val+1) (b.val+1) (c.val+1) j := by
    fin_cases j <;> simp [f,fourVertices,first,second,TwentyOneSixQuadCoverage.co6788,
      ae,be,ce,unitu,unitv,pairuv]
  have raw:=TwentyOneSixQuadCoverage.actual6788 H size noB f a b c hd hc (by trivial)
  rcases raw with two | one
  · left
    have t0:=QuadIncidence.triple_count H f 0
    have t1:=QuadIncidence.triple_count H f 1
    change tripleCodegree H x y u=count H f (highLabels 0)+count H f (highLabels 4) at t0
    change tripleCodegree H x y v=count H f (highLabels 1)+count H f (highLabels 4) at t1
    have rest : H.codegree x y=2 ∧ H.codegree y u=1 ∧ H.codegree y v=1 ∧
        count H f (highLabels 0)+count H f (highLabels 4)=0 ∧
        count H f (highLabels 1)+count H f (highLabels 4)=0 := by
      simpa [TwentyOneSixQuadCoverage.co6788,ae,be,ce] using two
    exact ⟨rest.1,rest.2.1,rest.2.2.1,t0.trans rest.2.2.2.1,t1.trans rest.2.2.2.2⟩
  · right
    have rest : H.codegree x y=1 ∧ H.codegree y u=H.codegree y v ∧ count H f (highLabels 4)=0 := by
      simpa [TwentyOneSixQuadCoverage.co6788,ae,be,ce] using one
    refine ⟨rest.1,rest.2.1,?_⟩
    intro e he xe ye ue ve
    have positive:=TwentyOneFiveLocal.common_quad H f e he (by
      intro j;fin_cases j <;> simp [f,fourVertices,xe,ye,ue,ve])
    omega

/-- Complete actual unique-six / one-seven branch. -/
theorem propertyB_of_one_seven (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (x y : Fin 21) (xy : x≠y) (dx : H.degree x=6) (dy : H.degree y=7)
    (others : ∀z,z≠x→z≠y→8≤H.degree z) : PropertyB H := by
  classical
  by_contra noB
  have manyL : 14≤(eights H).card := by
    have each (z : Fin 21) : 9≤H.degree z+(if z=x then 3 else 0)+
        (if z=y then 2 else 0)+(if H.degree z=8 then 1 else 0) := by
      by_cases zx : z=x
      · subst z;simp [dx,xy]
      by_cases zy : z=y
      · subst z;simp [dy,xy.symm]
      have low:=others z zx zy
      by_cases d8 : H.degree z=8
      · simp [zx,zy,d8]
      · simp only [zx,zy,d8,if_false,add_zero];omega
    have sum:=Finset.sum_le_sum (s:=Finset.univ) (fun z _=>each z)
    have bound : 189≤170+3+2+(eights H).card := by
      simpa [Finset.sum_add_distrib,H.sum_degrees,size,eights] using sum
    omega
  let U:=(eights H).filter (fun u=>H.codegree x u=1)
  have memU (u) : u∈U↔H.degree u=8 ∧ H.codegree x u=1 := by simp [U,mem_eights]
  have degrees (u) (hu : u∈U) : H.degree u=8 := ((memU u).mp hu).1
  have unit (u) (hu : u∈U) : H.codegree x u=1 := ((memU u).mp hu).2
  have apart (u) (hu : u∈U) : x≠u ∧ y≠u := by
    have du:=degrees u hu
    constructor <;> intro eq
    · rw [←eq,dx] at du;omega
    · rw [←eq,dy] at du;omega
  have usub : U⊆eights H := Finset.filter_subset _ _
  have sub : eights H\U⊆H.badPartners x\{y} := by
    intro u hu
    obtain ⟨hu,out⟩:=Finset.mem_sdiff.mp hu
    have du:=(mem_eights H u).mp hu
    have ux : u≠x := by intro eq;subst u;omega
    have uy : u≠y := by intro eq;subst u;omega
    have lower:=H.one_le_codegree cover ux.symm
    have notUnit : H.codegree x u≠1 := fun h=>out ((memU u).mpr ⟨du,h⟩)
    exact Finset.mem_sdiff.mpr ⟨Finset.mem_filter.mpr ⟨by simp [ux],by omega⟩,by simpa using uy⟩
  have bad:=TwentyOneSixIncidence.outside_bad_budget H cover x dx {y} (by simpa using xy)
  simp only [Finset.sum_singleton] at bad
  have upper:=Finset.card_le_card sub
  have split:=Finset.card_sdiff_add_card_eq_card usub
  have manyU : 10≤U.card := by omega
  obtain ⟨pairs,capacity⟩:=TwentyOneSixUnitActual.unit_set_structure_of_not_propertyB H cover size noB
    x dx U (by omega) degrees unit
  have residual (u v) (hu : u∈U) (hv : v∈U) (uv : u≠v) :=
    pair_residual H cover size noB x y u v xy (apart u hu).1 (apart v hv).1
      (apart u hu).2 (apart v hv).2 uv dx dy (degrees u hu) (degrees v hv)
      (unit u hu) (unit v hv) (pairs u hu v hv uv)
  have another (u : Fin 21) : ∃v∈U,v≠u := by
    obtain ⟨v,hv,out⟩:=Finset.exists_mem_notMem_of_card_lt_card (s:={u}) (t:=U) (by simpa using manyU.trans' (by decide : 2≤10))
    exact ⟨v,hv,by simpa using out⟩
  have cxy : H.codegree x y=1 := by
    by_contra notOne
    have clean (u) (hu : u∈U) : H.codegree x y=2 ∧ tripleCodegree H x y u=0 := by
      obtain ⟨v,hv,vu⟩:=another u
      rcases residual u v hu hv vu.symm with two | one
      · exact ⟨two.1,two.2.2.2.1⟩
      · omega
    obtain ⟨u,hu⟩:=Finset.card_pos.mp (by omega : 0<U.card)
    have c2:=(clean u hu).1
    have many : 11≤U.card := by rw [c2] at bad;omega
    have extra (e) (he : e∈H.edges) (xe : x∈e) (ye : y∈e) : (U∩e).card+1≤2 := by
      have empty : U∩e=∅ := by
        apply Finset.eq_empty_iff_forall_notMem.mpr
        intro u hu
        obtain ⟨hu,ue⟩:=Finset.mem_inter.mp hu
        have zero:=(clean u hu).2
        have positive : 1≤tripleCodegree H x y u := Finset.one_le_card.mpr
          ⟨e,Finset.mem_filter.mpr ⟨he,xe,ye,ue⟩⟩
        omega
      simp [empty]
    have bound:=Incidence.extra_capacity H x y U 2 capacity extra
    have sum : (∑u∈U,H.codegree x u)=U.card := by
      calc
        _=∑_u∈U,1 := Finset.sum_congr rfl unit
        _=_ := by simp
    rw [sum,dx,c2] at bound
    omega
  have equal (u v) (hu : u∈U) (hv : v∈U) : H.codegree y u=H.codegree y v := by
    by_cases uv : u=v
    · subst v;rfl
    rcases residual u v hu hv uv with two | one
    · omega
    · exact one.2.1
  have unity (u) (hu : u∈U) : H.codegree y u=1 := by
    have lower:=H.one_le_codegree cover (apart u hu).2
    by_contra hn
    have allBad : U⊆H.badPartners y := by
      intro v hv
      have eq:=equal u v hu hv
      exact Finset.mem_filter.mpr ⟨by simp [(apart v hv).2.symm],by omega⟩
    have bound:=H.badPartners_card_le_excess cover y
    rw [dy] at bound
    simp only [Fintype.card_fin] at bound
    have card:=Finset.card_le_card allBad
    omega
  obtain ⟨e,he,xe,ye⟩:=cover x y xy
  have capE : (U∩e).card≤1 := by
    apply Finset.card_le_one.mpr
    intro u hu v hv
    obtain ⟨hu,ue⟩:=Finset.mem_inter.mp hu
    obtain ⟨hv,ve⟩:=Finset.mem_inter.mp hv
    by_contra uv
    rcases residual u v hu hv uv with two | one
    · omega
    · exact one.2.2 e he xe ye ue ve
  let S:=U\e
  have large : 7≤S.card := by
    have splitS:=Finset.card_sdiff_add_card_inter U e
    change 7≤(U\e).card
    omega
  have subS : S⊆U := Finset.sdiff_subset
  have clean (u) (hu : u∈S) : tripleCodegree H x y u=0 := by
    apply Finset.card_eq_zero.mpr
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro a ha
    obtain ⟨ha,xa,ya,ua⟩:=Finset.mem_filter.mp ha
    have eq:=H.edge_unique_of_codegree_one cxy ha he xa ya xe ye
    exact (Finset.mem_sdiff.mp hu).2 (eq ▸ ua)
  exact noB (TwentyOneSixFiveSelection.propertyB_of_unit_set H size x y 1 xy dx dy cxy S large
    (fun u hu=>degrees u (subS hu)) (fun u hu=>⟨unit u (subS hu),unity u (subS hu)⟩)
    (fun u hu v hv uv=>pairs u (subS hu) v (subS hv) uv) clean)
end Aris4Math.ThirtyFour.TwentyOneSixOneSeven
#print axioms Aris4Math.ThirtyFour.TwentyOneSixOneSeven.propertyB_of_one_seven
