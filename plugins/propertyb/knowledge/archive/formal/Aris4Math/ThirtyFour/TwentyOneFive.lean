import Aris4Math.ThirtyFour.TwentyOneFiveLocal

set_option simprocs false

namespace Aris4Math.ThirtyFour.TwentyOneFive
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.ThirtyThree.QuadProfiles (count first second highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices high_inventory highPairSum)
open Aris4Math.ThirtyFour.TwentyOneFiveStructure
open Aris4Math.ThirtyFour.TwentyOneFiveLocal
open Aris4Math.ThirtyFour.TwentyOneFiveClassification (Kind degrees Assumptions Residue)

theorem indexed_subset {V : Type*} [DecidableEq V] (S : Finset V) {n : ℕ} (size : n ≤ S.card) :
    ∃ f : Fin n ↪ V, ∀ i, f i ∈ S := by
  classical
  obtain ⟨T,sub,card⟩ := Finset.exists_subset_card_eq size
  let e : ↥T ≃ Fin n := Fintype.equivFinOfCardEq (by simpa using card)
  refine ⟨⟨fun i => (e.symm i).val,Subtype.val_injective.comp e.symm.injective⟩,?_⟩
  intro i; exact sub (e.symm i).property

variable (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
  (size : H.edges.card=34) (x : Fin 21) (dx : H.degree x=5) (noB : ¬ PropertyB H)
include cover size dx noB

theorem many_sevens (many : 3 ≤ (sevens H).card) : False := by
  classical
  obtain ⟨g,hg⟩ := indexed_subset (sevens H) many
  have dg (i : Fin 3) : H.degree (g i)=7 := (mem_sevens H _).mp (hg i)
  have xn (i : Fin 3) : x ≠ g i := by intro eq; rw [eq,dg] at dx; omega
  let f := fourVertices x (g 0) (g 1) (g 2) (xn 0) (xn 1) (xn 2)
    (g.injective.ne (by decide)) (g.injective.ne (by decide)) (g.injective.ne (by decide))
  have pair (i j : Fin 3) (ij : i ≠ j) :=
    seven_pair H cover size x dx noB (g i) (g j) (dg i) (dg j) (g.injective.ne ij)
  have p01 := pair 0 1 (by decide); have p02 := pair 0 2 (by decide); have p12 := pair 1 2 (by decide)
  obtain ⟨e,he,xe,ye,ze⟩ := triple_common H x (g 0) (g 1) (by omega)
  obtain ⟨e',he',xe',ye',we'⟩ := triple_common H x (g 0) (g 2) (by omega)
  have unit := ThirtyThree.TwentyOneStructure.all_unit_of_degree_five H cover (by simp) x dx (g 0) (xn 0)
  have eq := H.edge_unique_of_codegree_one unit he' he xe' ye' xe ye
  have we : g 2 ∈ e := eq ▸ we'
  have positive : 1 ≤ count H f (highLabels 4) := common_quad H f e he (by
    intro j; fin_cases j <;> simp [f,fourVertices,xe,ye,ze,we])
  have bound := high_inventory H f 0
  have quad : count H f (highLabels 4)=1 := by
    change count H f (highLabels 0)+count H f (highLabels 1)+count H f (highLabels 4) ≤ H.codegree x (g 0) at bound
    rw [unit] at bound; omega
  have hd : ∀ j, H.degree (f j)=degrees 0 j := by
    intro j; fin_cases j <;> simp [f,fourVertices,degrees,dx,dg]
  have ass : Assumptions 0 (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j)) := by
    simp only [Assumptions,show (0 : Kind)≠1 by decide,show (0 : Kind)≠2 by decide,show (1 : Kind)≠0 by decide,show (1 : Kind)≠2 by decide,show (2 : Kind)≠0 by decide,show (2 : Kind)≠1 by decide,not_false_eq_true,false_implies,true_implies,true_and,and_true,eq_self]
    exact ⟨p01.1,p02.1,p12.1,quad⟩
  have rr := residue H cover size noB f 0 hd ass
  rcases rr with ⟨bad,_,_,_⟩ | ⟨bad,_⟩
  · exact (by decide : (0 : Kind) ≠ 2) bad
  · exact (by decide : (0 : Kind) ≠ 3) bad

theorem two_sevens (minimum : ∀ y, y ≠ x → 7 ≤ H.degree y)
    (two : (sevens H).card=2) : False := by
  classical
  obtain ⟨g,hg⟩ := indexed_subset (sevens H) (show 2 ≤ (sevens H).card by omega)
  have dg (i : Fin 2) : H.degree (g i)=7 := (mem_sevens H _).mp (hg i)
  have xn (i : Fin 2) : x ≠ g i := by intro eq; rw [eq,dg] at dx; omega
  have yz : g 0 ≠ g 1 := g.injective.ne (by decide)
  have pair := seven_pair H cover size x dx noB _ _ (dg 0) (dg 1) yz
  obtain ⟨e,he,xe,ye,ze⟩ := triple_common H x (g 0) (g 1) (by omega)
  have eb := eights_budget H cover size x dx minimum
  have ec := H.five_uniform e he
  obtain ⟨w,hw,we⟩ := Finset.exists_mem_notMem_of_card_lt_card (s := e) (t := eights H) (by omega)
  have dw := (mem_eights H w).mp hw
  have xw : x ≠ w := by intro eq; rw [eq,dw] at dx; omega
  have yw : g 0 ≠ w := by intro eq; have := dg 0; rw [eq,dw] at this; omega
  have zw : g 1 ≠ w := by intro eq; have := dg 1; rw [eq,dw] at this; omega
  let f := fourVertices x (g 0) (g 1) w (xn 0) (xn 1) xw yz yw zw
  have hd : ∀ j, H.degree (f j)=degrees 1 j := by
    intro j; fin_cases j <;> simp [f,fourVertices,degrees,dx,dg,dw]
  have t0 := QuadIncidence.triple_count H f 0
  have t1 := QuadIncidence.triple_count H f 1
  have t2 := QuadIncidence.triple_count H f 2
  change tripleCodegree H x (g 0) (g 1)=_ at t0
  change tripleCodegree H x (g 0) w=_ at t1
  change tripleCodegree H x (g 1) w=_ at t2
  rw [pair.2] at t0
  rw [no_triple_outside H cover x (g 0) w dx (xn 0) e he xe ye we] at t1
  rw [no_triple_outside H cover x (g 1) w dx (xn 1) e he xe ze we] at t2
  have ass : Assumptions 1 (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j)) := by
    simp only [Assumptions,show (0 : Kind)≠1 by decide,show (0 : Kind)≠2 by decide,show (1 : Kind)≠0 by decide,show (1 : Kind)≠2 by decide,show (2 : Kind)≠0 by decide,show (2 : Kind)≠1 by decide,not_false_eq_true,false_implies,true_implies,true_and,and_true,eq_self]
    exact ⟨pair.1,t0.symm,t1.symm,t2.symm⟩
  have rr := residue H cover size noB f 1 hd ass
  rcases rr with ⟨bad,_,_,_⟩ | ⟨bad,_⟩
  · exact (by decide : (1 : Kind) ≠ 2) bad
  · exact (by decide : (1 : Kind) ≠ 3) bad

theorem one_seven (minimum : ∀ y, y ≠ x → 7 ≤ H.degree y)
    (one : (sevens H).card=1) : False := by
  classical
  obtain ⟨y,single⟩ := Finset.card_eq_one.mp one
  have dy : H.degree y=7 := (mem_sevens H y).mp (by simp [single])
  have xy : x ≠ y := by intro eq; rw [eq,dy] at dx; omega
  obtain ⟨e,he,xe,ye⟩ := cover x y xy
  let S := eights H \ e
  have eb := eights_budget H cover size x dx minimum
  have ec := H.five_uniform e he
  have bound := Finset.card_le_card_sdiff_add_card (s := eights H) (t := e)
  have large : 8 ≤ S.card := by dsimp [S]; omega
  have eight (z : Fin 21) (hz : z ∈ S) : H.degree z=8 :=
    (mem_eights H z).mp (Finset.mem_sdiff.mp hz).1
  have xn (z : Fin 21) (hz : z ∈ S) : x ≠ z := by intro eq; have := eight z hz; rw [← eq,dx] at this; omega
  have yn (z : Fin 21) (hz : z ∈ S) : y ≠ z := by intro eq; have := eight z hz; rw [← eq,dy] at this; omega
  have capacity (a : Finset (Fin 21)) (ha : a ∈ H.edges) (ya : y ∈ a) : (S ∩ a).card ≤ 1 := by
    apply Finset.card_le_one.mpr
    intro z hz w hw
    by_contra zw
    obtain ⟨hzS,hza⟩ := Finset.mem_inter.mp hz
    obtain ⟨hwS,hwa⟩ := Finset.mem_inter.mp hw
    let f := fourVertices x y z w xy (xn z hzS) (xn w hwS) (yn z hzS) (yn w hwS) zw
    have hd : ∀ j, H.degree (f j)=degrees 2 j := by
      intro j; fin_cases j
      · exact dx
      · exact dy
      · exact eight z hzS
      · exact eight w hwS
    have t0 := QuadIncidence.triple_count H f 0
    have t1 := QuadIncidence.triple_count H f 1
    change tripleCodegree H x y z=_ at t0
    change tripleCodegree H x y w=_ at t1
    rw [no_triple_outside H cover x y z dx xy e he xe ye (Finset.mem_sdiff.mp hzS).2] at t0
    rw [no_triple_outside H cover x y w dx xy e he xe ye (Finset.mem_sdiff.mp hwS).2] at t1
    have ass : Assumptions 2 (fun j => H.codegree (f (first j)) (f (second j)))
        (fun j => count H f (highLabels j)) := by
      simp only [Assumptions,show (0 : Kind)≠1 by decide,show (0 : Kind)≠2 by decide,show (1 : Kind)≠0 by decide,show (1 : Kind)≠2 by decide,show (2 : Kind)≠0 by decide,show (2 : Kind)≠1 by decide,not_false_eq_true,false_implies,true_implies,true_and,and_true,eq_self]
      exact ⟨t0.symm,t1.symm⟩
    have rr := residue H cover size noB f 2 hd ass
    have zero : ∀ j, count H f (highLabels j)=0 := by
      rcases rr with ⟨_,_,_,hh⟩ | ⟨bad,_⟩
      · exact hh
      · exact False.elim ((by decide : (2 : Kind) ≠ 3) bad)
    have t3 := QuadIncidence.triple_count H f 3
    change tripleCodegree H y z w=_ at t3
    rw [zero,zero] at t3
    have pos : 1 ≤ tripleCodegree H y z w := Finset.one_le_card.mpr
      ⟨a,Finset.mem_filter.mpr ⟨ha,ya,hza,hwa⟩⟩
    omega
  have upper := Incidence.codegree_capacity H y S 1 capacity
  have lower : S.card ≤ ∑ z ∈ S, H.codegree y z := by
    calc
      _ = ∑ _z ∈ S, 1 := by simp
      _ ≤ _ := Finset.sum_le_sum (fun z hz => H.one_le_codegree cover (yn z hz))
  rw [dy] at upper
  omega

theorem no_sevens (minimum : ∀ y, y ≠ x → 7 ≤ H.degree y)
    (zero : (sevens H).card=0) : False := by
  classical
  let L := eights H
  have eb := eights_budget H cover size x dx minimum
  have large : 15 ≤ L.card := by dsimp [L]; omega
  have degree (z : Fin 21) (hz : z ∈ L) : H.degree z=8 := (mem_eights H z).mp hz
  have xn (z : Fin 21) (hz : z ∈ L) : x ≠ z := by intro eq; have := degree z hz; rw [← eq,dx] at this; omega
  have capacity (e : Finset (Fin 21)) (he : e ∈ H.edges) (xe : x ∈ e) : (L ∩ e).card ≤ 2 := by
    by_contra hn
    obtain ⟨g,hg⟩ := indexed_subset (L ∩ e) (show 3 ≤ (L ∩ e).card by omega)
    have gl (i : Fin 3) := (Finset.mem_inter.mp (hg i)).1
    have ge (i : Fin 3) := (Finset.mem_inter.mp (hg i)).2
    let f := fourVertices x (g 0) (g 1) (g 2) (xn _ (gl 0)) (xn _ (gl 1)) (xn _ (gl 2))
      (g.injective.ne (by decide)) (g.injective.ne (by decide)) (g.injective.ne (by decide))
    have hd : ∀ j, H.degree (f j)=degrees 3 j := by
      intro j; fin_cases j
      · exact dx
      · exact degree _ (gl 0)
      · exact degree _ (gl 1)
      · exact degree _ (gl 2)
    have ass : Assumptions 3 (fun j => H.codegree (f (first j)) (f (second j)))
        (fun j => count H f (highLabels j)) :=
      ⟨fun h => False.elim ((by decide : (3 : Kind) ≠ 0) h),
       fun h => False.elim ((by decide : (3 : Kind) ≠ 1) h),
       fun h => False.elim ((by decide : (3 : Kind) ≠ 2) h)⟩
    have rr := residue H cover size noB f 3 hd ass
    have qzero : count H f (highLabels 4)=0 := by
      rcases rr with ⟨bad,_,_,_⟩ | ⟨_,hh⟩
      · exact False.elim ((by decide : (3 : Kind) ≠ 2) bad)
      · exact hh
    have pos := common_quad H f e he (by intro j; fin_cases j <;> simp [f,fourVertices,xe,ge])
    omega
  have upper := Incidence.codegree_capacity H x L 2 capacity
  have unit := ThirtyThree.TwentyOneStructure.all_unit_of_degree_five H cover (by simp) x dx
  have sum : (∑ z ∈ L, H.codegree x z)=L.card := by
    have each : ∀ z ∈ L, H.codegree x z=1 := fun z hz => unit z (xn z hz)
    simp only [Finset.sum_congr rfl each,Finset.sum_const,smul_eq_mul,Nat.mul_one]
  rw [sum,dx] at upper
  omega

omit noB in
theorem propertyB_of_degree_five : PropertyB H := by
  classical
  by_contra hn
  by_cases low : ∃ y, y ≠ x ∧ H.degree y ≤ 6
  · exact hn (other_low H cover size x dx low)
  have minimum (y : Fin 21) (yx : y ≠ x) : 7 ≤ H.degree y := by
    have : ¬ H.degree y ≤ 6 := fun h => low ⟨y,yx,h⟩
    omega
  have r := (sevens H).card
  by_cases many : 3 ≤ (sevens H).card
  · exact many_sevens H cover size x dx hn many
  by_cases two : (sevens H).card=2
  · exact two_sevens H cover size x dx hn minimum two
  by_cases one : (sevens H).card=1
  · exact one_seven H cover size x dx hn minimum one
  exact no_sevens H cover size x dx hn minimum (by omega)
end Aris4Math.ThirtyFour.TwentyOneFive
#print axioms Aris4Math.ThirtyFour.TwentyOneFive.propertyB_of_degree_five
