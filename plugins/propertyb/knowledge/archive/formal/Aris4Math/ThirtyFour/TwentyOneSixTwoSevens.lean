import Aris4Math.ThirtyFour.TwentyOneSixStructure
import Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
import Aris4Math.ThirtyFour.TwentyOneSixFive67788Local
import Aris4Math.ThirtyFour.TwentyOneFive

/-! The actual unique-six / exactly-two-seven branch. The final five vertices
are selected from the actual eight-degree set and actual common-pair edges. -/

namespace Aris4Math.ThirtyFour.TwentyOneSixTwoSevens

open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.ThirtyThree.QuadProfiles (count first second highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open Aris4Math.ThirtyFour.TwentyOneFiveStructure (eights mem_eights)
open Aris4Math.ThirtyFour.TwentyOneSixStructure
open Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
  (co6778 Assumptions6778 Residue6778 actual6778)

theorem eights_at_least_twelve (H : Simple5Hypergraph (Fin 21))
    (size : H.edges.card=34) (x y z : Fin 21)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (dx : H.degree x=6) (dy : H.degree y=7) (dz : H.degree z=7)
    (others : ∀ v, v ≠ x → v ≠ y → v ≠ z → 8 ≤ H.degree v) :
    12 ≤ (eights H).card := by
  have each (v : Fin 21) : 9 ≤ H.degree v+(if v=x then 3 else 0)+
      (if v=y then 2 else 0)+(if v=z then 2 else 0)+
      (if H.degree v=8 then 1 else 0) := by
    by_cases vx : v=x
    · subst v; simp [dx,xy,xz]
    by_cases vy : v=y
    · subst v; simp [dy,xy.symm,yz]
    by_cases vz : v=z
    · subst v; simp [dz,xz.symm,yz.symm]
    have lower := others v vx vy vz
    by_cases eight : H.degree v=8
    · simp [vx,vy,vz,eight]
    · simp only [vx,vy,vz,eight,if_false,add_zero]; omega
  have sum := Finset.sum_le_sum (s := Finset.univ) (fun v _ => each v)
  have bound : 189 ≤ 170+3+2+2+(eights H).card := by
    simpa [Finset.sum_add_distrib,H.sum_degrees,size,eights] using sum
  omega

/-- The actual 6778 classifier forces a unit neighbor of x outside the
relevant common triples to be unit to both seven-degree points. -/
theorem force_units (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬ PropertyB H)
    (x y z u : Fin 21) (xy : x ≠ y) (xz : x ≠ z) (xu : x ≠ u)
    (yz : y ≠ z) (yu : y ≠ u) (zu : z ≠ u)
    (dx : H.degree x=6) (dy : H.degree y=7) (dz : H.degree z=7) (du : H.degree u=8)
    (unit : H.codegree x u=1) (same : H.codegree x y=H.codegree x z)
    (tail : H.codegree y z=3-H.codegree x y)
    (bound : H.codegree x y=1 ∨ H.codegree x y=2)
    (caseA : H.codegree x y=1 → tripleCodegree H x y z=1 ∧
      tripleCodegree H x y u=0 ∧ tripleCodegree H x z u=0)
    (caseB : H.codegree x y=2 → tripleCodegree H x y z=0) :
    H.codegree x y=1 ∧ H.codegree y u=1 ∧ H.codegree z u=1 := by
  have bu := (residual_678 H cover size noB x y u xy xu yu dx dy du).2.2
  have cu := (residual_678 H cover size noB x z u xz xu zu dx dz du).2.2
  have bl := H.one_le_codegree cover yu
  have cl := H.one_le_codegree cover zu
  let a : Fin 2 := ⟨H.codegree x y-1,by omega⟩
  let b : Fin 2 := ⟨H.codegree y u-1,by omega⟩
  let c : Fin 2 := ⟨H.codegree z u-1,by omega⟩
  have pa : a.val+1=H.codegree x y := by dsimp [a]; omega
  have pb : b.val+1=H.codegree y u := by dsimp [b]; omega
  have pc : c.val+1=H.codegree z u := by dsimp [c]; omega
  let f := fourVertices x y z u xy xz xu yz yu zu
  have hd : ∀ j, H.degree (f j)=TwentyOneSixQuad6778Data.degree j := by
    intro j; fin_cases j <;> simp [f,fourVertices,TwentyOneSixQuad6778Data.degree,dx,dy,dz,du]
  have hc : ∀ j, H.codegree (f (first j)) (f (second j))=
      co6778 (a.val+1) (b.val+1) (c.val+1) j := by
    intro j
    fin_cases j <;> simp [f,fourVertices,first,second,co6778,pa,pb,pc,unit,same,tail]
  have t0 := QuadIncidence.triple_count H f 0
  have t1 := QuadIncidence.triple_count H f 1
  have t2 := QuadIncidence.triple_count H f 2
  change tripleCodegree H x y z=count H f (highLabels 0)+count H f (highLabels 4) at t0
  change tripleCodegree H x y u=count H f (highLabels 1)+count H f (highLabels 4) at t1
  change tripleCodegree H x z u=count H f (highLabels 2)+count H f (highLabels 4) at t2
  have ass : Assumptions6778 (a.val+1) (fun j => count H f (highLabels j)) := by
    rw [pa]
    constructor
    · intro one
      obtain ⟨xyz,xyu,xzu⟩ := caseA one
      exact ⟨t0.symm.trans xyz,t1.symm.trans xyu,t2.symm.trans xzu⟩
    · intro two
      exact t0.symm.trans (caseB two)
  have result := actual6778 H size noB f a b c hd hc ass
  simpa [Residue6778,co6778,pa,pb,pc] using result

theorem eight_edge_capacity (H : Simple5Hypergraph (Fin 21))
    (y z : Fin 21) (yz : y ≠ z) (dy : H.degree y=7) (dz : H.degree z=7)
    (e : Finset (Fin 21)) (he : e ∈ H.edges) (ye : y ∈ e) (ze : z ∈ e) :
    ((eights H) ∩ e).card ≤ 3 := by
  have sub : ((eights H) ∩ e) ∪ {y,z} ⊆ e := by
    intro v hv
    rcases Finset.mem_union.mp hv with hv | hv
    · exact (Finset.mem_inter.mp hv).2
    · simp only [Finset.mem_insert,Finset.mem_singleton] at hv
      rcases hv with rfl | rfl <;> assumption
  have dis : Disjoint ((eights H) ∩ e) ({y,z} : Finset (Fin 21)) := by
    apply Finset.disjoint_left.mpr
    intro v hv hpair
    have dv := (mem_eights H v).mp (Finset.mem_inter.mp hv).1
    simp only [Finset.mem_insert,Finset.mem_singleton] at hpair
    rcases hpair with rfl | rfl <;> omega
  have bound := Finset.card_le_card sub
  rw [Finset.card_union_of_disjoint dis,H.five_uniform e he] at bound
  have two : ({y,z} : Finset (Fin 21)).card=2 := by simp [yz]
  omega

/-- The only low vertices are the displayed degree-six point and two sevens.
All remaining hypotheses concern the original actual degree function. -/
theorem propertyB_of_two_sevens (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34) (x y z : Fin 21)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (dx : H.degree x=6) (dy : H.degree y=7) (dz : H.degree z=7)
    (others : ∀ v, v ≠ x → v ≠ y → v ≠ z → 8 ≤ H.degree v) : PropertyB H := by
  by_contra noB
  have many := eights_at_least_twelve H size x y z xy xz yz dx dy dz others
  have bad := H.badPartners_card_le_excess cover x
  have bad4 : (H.badPartners x).card ≤ 4 := by simpa [dx] using bad
  let T := eights H \ H.badPartners x
  have tlarge : 8 ≤ T.card := by
    have bound := Finset.card_le_card_sdiff_add_card (s := eights H) (t := H.badPartners x)
    change (eights H).card ≤ T.card+(H.badPartners x).card at bound
    omega
  have td (u : Fin 21) (hu : u ∈ T) : H.degree u=8 :=
    (mem_eights H u).mp (Finset.mem_sdiff.mp hu).1
  have apart (u : Fin 21) (hu : u ∈ T) : x ≠ u ∧ y ≠ u ∧ z ≠ u := by
    have du := td u hu
    constructor
    · intro eq; rw [←eq,dx] at du; omega
    constructor
    · intro eq; rw [←eq,dy] at du; omega
    · intro eq; rw [←eq,dz] at du; omega
  have tu (u : Fin 21) (hu : u ∈ T) : H.codegree x u=1 := by
    have lower := H.one_le_codegree cover (apart u hu).1
    have notbad := (Finset.mem_sdiff.mp hu).2
    by_contra ne
    apply notbad
    exact Finset.mem_filter.mpr
      ⟨Finset.mem_erase.mpr ⟨(apart u hu).1.symm,Finset.mem_univ u⟩,by omega⟩
  rcases residual_677 H cover size noB x y z xy xz yz dx dy dz with residueA | residueB
  · obtain ⟨xy1,xz1,yz2,xyz1⟩ := residueA
    let E := H.edges.filter fun e => y ∈ e ∧ z ∈ e
    have ecard : E.card=2 := yz2
    let B := E.biUnion fun e => (eights H) ∩ e
    have bsmall : B.card ≤ 6 := by
      calc
        _ ≤ ∑ e ∈ E, ((eights H) ∩ e).card := Finset.card_biUnion_le
        _ ≤ ∑ _e ∈ E, 3 := by
          apply Finset.sum_le_sum
          intro e he
          obtain ⟨he,ye,ze⟩ := Finset.mem_filter.mp he
          exact eight_edge_capacity H y z yz dy dz e he ye ze
        _ = 6 := by simp [ecard]
    let S := T \ B
    have slarge : 2 ≤ S.card := by
      have bound := Finset.card_le_card_sdiff_add_card (s := T) (t := B)
      change T.card ≤ S.card+B.card at bound
      omega
    have st : S ⊆ T := Finset.sdiff_subset
    have avoids (u : Fin 21) (hu : u ∈ S) (e : Finset (Fin 21))
        (he : e ∈ H.edges) (ye : y ∈ e) (ze : z ∈ e) : u ∉ e := by
      intro ue
      apply (Finset.mem_sdiff.mp hu).2
      exact Finset.mem_biUnion.mpr ⟨e,Finset.mem_filter.mpr ⟨he,ye,ze⟩,
        Finset.mem_inter.mpr ⟨(Finset.mem_sdiff.mp (st hu)).1,ue⟩⟩
    obtain ⟨e,he,xe,ye,ze⟩ := TwentyOneFiveLocal.triple_common H x y z (by omega)
    have clean (u : Fin 21) (hu : u ∈ S) :
        tripleCodegree H x y u=0 ∧ tripleCodegree H x z u=0 ∧ tripleCodegree H y z u=0 := by
      refine ⟨?_,?_,?_⟩
      · apply ThirtyThree.TwentyOnePairAssembly.tripleCodegree_zero
        intro g hg hxyu
        have eq := H.edge_unique_of_codegree_one xy1 hg he hxyu.1 hxyu.2.1 xe ye
        exact avoids u hu e he ye ze (eq ▸ hxyu.2.2)
      · apply ThirtyThree.TwentyOnePairAssembly.tripleCodegree_zero
        intro g hg hxzu
        have eq := H.edge_unique_of_codegree_one xz1 hg he hxzu.1 hxzu.2.1 xe ze
        exact avoids u hu e he ye ze (eq ▸ hxzu.2.2)
      · apply ThirtyThree.TwentyOnePairAssembly.tripleCodegree_zero
        intro g hg hyzu
        exact avoids u hu g hg hyzu.1 hyzu.2.1 hyzu.2.2
    have units (u : Fin 21) (hu : u ∈ S) :
        H.codegree x u=1 ∧ H.codegree y u=1 ∧ H.codegree z u=1 := by
      have ad := apart u (st hu)
      have cc := clean u hu
      have result := force_units H cover size noB x y z u xy xz ad.1 yz ad.2.1 ad.2.2
        dx dy dz (td u (st hu)) (tu u (st hu)) (by omega) (by omega) (Or.inl xy1)
        (fun _ => ⟨xyz1,cc.1,cc.2.1⟩) (by intro two; omega)
      exact ⟨tu u (st hu),result.2⟩
    obtain ⟨u,hu,v,hv,uv⟩ := Finset.one_lt_card.mp (by omega : 1 < S.card)
    have du := td u (st hu)
    have dv := td v (st hv)
    have ua := apart u (st hu)
    have va := apart v (st hv)
    have uu := units u hu
    have vu := units v hv
    have uc := clean u hu
    have vc := clean v hv
    have uv1 := H.one_le_codegree cover uv
    have uv2 := unit_eight_pair H cover size noB x u v ua.1 va.1 uv dx du dv uu.1 vu.1
    let b : Fin 2 := ⟨H.codegree u v-1,by omega⟩
    have pb : b.val+1=H.codegree u v := by dsimp [b]; omega
    let f : Fin 5 ↪ Fin 21 := ⟨![x,y,z,u,v],by
      intro i j eq
      fin_cases i <;> fin_cases j <;>
        simp [xy,xy.symm,xz,xz.symm,yz,yz.symm,ua.1,ua.1.symm,va.1,va.1.symm,
          ua.2.1,ua.2.1.symm,ua.2.2,ua.2.2.symm,va.2.1,va.2.1.symm,
          va.2.2,va.2.2.symm,uv,uv.symm] at eq ⊢⟩
    have hd : ∀ j, H.degree (f j)=TwentyOneSixFive67788Data.degree j := by
      intro j
      fin_cases j <;> simp [f,TwentyOneSixFive67788Data.degree,dx,dy,dz,du,dv]
    have hc : ∀ i j, i ≠ j → H.codegree (f i) (f j)=TwentyOneSixFive67788Local.pair b i j := by
      have yx := H.codegree_comm y x
      have zx := H.codegree_comm z x; have zy := H.codegree_comm z y
      have ux := H.codegree_comm u x; have uy := H.codegree_comm u y; have uz := H.codegree_comm u z
      have vx := H.codegree_comm v x; have vy := H.codegree_comm v y; have vz := H.codegree_comm v z
      have vuc := H.codegree_comm v u
      intro i j ne
      fin_cases i <;> fin_cases j <;>
        simp +decide [f,TwentyOneSixFive67788Local.pair] at ne ⊢ <;> omega
    have cleanReverse (p q t : Fin 21) : tripleCodegree H p q t=tripleCodegree H q p t := by
      simp only [tripleCodegree,and_left_comm]
    have uyx := (cleanReverse y x u).trans uc.1
    have uzx := (cleanReverse z x u).trans uc.2.1
    have uzy := (cleanReverse z y u).trans uc.2.2
    have vyx := (cleanReverse y x v).trans vc.1
    have vzx := (cleanReverse z x v).trans vc.2.1
    have vzy := (cleanReverse z y v).trans vc.2.2
    apply noB
    apply TwentyOneSixFive67788Local.propertyB_of_five H size f b hd hc xyz1
    intro i j ne t
    fin_cases i <;> fin_cases j <;> fin_cases t <;>
      simp [f,TwentyOneSixFive67788Local.root,TwentyOneSixFive67788Local.tail] at ne ⊢ <;> omega
  · obtain ⟨xy2,xz2,yz1,xyz0⟩ := residueB
    obtain ⟨u,hu⟩ := Finset.card_pos.mp (show 0 < T.card by omega)
    have ad := apart u hu
    have result := force_units H cover size noB x y z u xy xz ad.1 yz ad.2.1 ad.2.2
      dx dy dz (td u hu) (tu u hu) (by omega) (by omega) (Or.inr xy2)
      (by intro one; omega) (fun _ => xyz0)
    omega

end Aris4Math.ThirtyFour.TwentyOneSixTwoSevens

#print axioms Aris4Math.ThirtyFour.TwentyOneSixTwoSevens.propertyB_of_two_sevens
