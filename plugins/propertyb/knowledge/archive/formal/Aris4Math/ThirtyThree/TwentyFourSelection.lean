import Aris4Math.Traces
import Aris4Math.LowDegree
import Aris4Math.ThirtyThree.TwentyFourUniqueBadPair

/-! Actual lock selection for the 24-vertex branch with 33 edges. -/
namespace Aris4Math.ThirtyThree.TwentyFourSelection

open scoped BigOperators
variable {V : Type*} [Fintype V] [DecidableEq V]

def sevenVertices (H : Simple5Hypergraph V) : Finset V :=
  Finset.univ.filter fun x => H.degree x = 7

theorem minimum_degree (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 24) (x : V) : 6 ≤ H.degree x := by
  have h := H.pairCovering_degree_bound cover x
  rw [vertices] at h
  omega

theorem six_card_ge_three (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 24) :
    3 ≤ H.sixVertices.card := by
  have each (x : V) : 7 ≤ H.degree x + if H.degree x = 6 then 1 else 0 := by
    have hd := minimum_degree H cover vertices x
    split_ifs <;> omega
  have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have budget : 7 * Fintype.card V ≤ 165 + H.sixVertices.card := by
    simpa [Finset.sum_add_distrib, H.sum_degrees, edges,
      Simple5Hypergraph.sixVertices, Nat.mul_comm] using h
  rw [vertices] at budget
  omega

theorem six_seven_budget (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 24) :
    27 ≤ 2 * H.sixVertices.card + (sevenVertices H).card := by
  have each (x : V) : 8 ≤ H.degree x +
      (if H.degree x = 6 then 2 else 0) + (if H.degree x = 7 then 1 else 0) := by
    have hd := minimum_degree H cover vertices x
    split_ifs <;> omega
  have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have sumtwo : (∑ x : V, if H.degree x = 6 then 2 else 0) =
      2 * H.sixVertices.card := by
    rw [← Finset.sum_filter]
    simp [Simple5Hypergraph.sixVertices, Nat.mul_comm]
  have budget : 8 * Fintype.card V ≤ 165 + 2 * H.sixVertices.card +
      (sevenVertices H).card := by
    simpa [Finset.sum_add_distrib, sumtwo, H.sum_degrees, edges,
      Simple5Hypergraph.sixVertices, sevenVertices, Nat.mul_comm] using h
  rw [vertices] at budget
  omega

/-- The two intended 24-point branches cover every original reduced input. -/
theorem five_six_or_many_seven (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 24) :
    5 ≤ H.sixVertices.card ∨ 19 ≤ (sevenVertices H).card := by
  have h := six_seven_budget H cover edges vertices
  omega

/-- Any bad partner of a degree-six point is its only bad partner. -/
theorem unit_of_other_bad (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 24) {x y z : V} (dx : H.degree x = 6)
    (xy : x ≠ y) (bad : 2 ≤ H.codegree x y) (xz : x ≠ z) (yz : y ≠ z) :
    H.codegree x z = 1 := by
  have one := H.badPartners_card_le_one_of_twenty_four cover vertices dx
  have memY : y ∈ H.badPartners x :=
    Finset.mem_filter.mpr ⟨Finset.mem_erase.mpr ⟨xy.symm, Finset.mem_univ _⟩, bad⟩
  have low := H.one_le_codegree cover xz
  by_contra hn
  have memZ : z ∈ H.badPartners x :=
    Finset.mem_filter.mpr ⟨Finset.mem_erase.mpr ⟨xz.symm, Finset.mem_univ _⟩, by omega⟩
  exact yz (Finset.card_le_one.mp one _ memY _ memZ)

/-- A six-degree codegree is at most two, from the full actual excess sum. -/
theorem six_codegree_le_two (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 24) {x y : V} (dx : H.degree x = 6)
    (xy : x ≠ y) : H.codegree x y ≤ 2 := by
  have h := Finset.single_le_sum (fun z _ => Nat.zero_le (H.codegree x z - 1))
    (Finset.mem_erase.mpr ⟨xy.symm, Finset.mem_univ y⟩)
  rw [H.sum_codegree_excess cover x, vertices, dx] at h
  omega

theorem exists_two_unit_six (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 24) :
    ∃ x y, x ≠ y ∧ H.degree x = 6 ∧ H.degree y = 6 ∧ H.codegree x y = 1 := by
  have many := six_card_ge_three H cover edges vertices
  obtain ⟨x, hx⟩ := Finset.card_pos.mp (show 0 < H.sixVertices.card by omega)
  have dx : H.degree x = 6 := (Finset.mem_filter.mp hx).2
  let B := insert x (H.badPartners x)
  have bsmall : B.card ≤ 2 := by
    have h1 := H.badPartners_card_le_one_of_twenty_four cover vertices dx
    have h2 := Finset.card_insert_le x (H.badPartners x)
    dsimp [B]
    omega
  have h := Finset.card_le_card_sdiff_add_card (s := H.sixVertices) (t := B)
  obtain ⟨y, hy⟩ := Finset.card_pos.mp (show 0 < (H.sixVertices \ B).card by omega)
  obtain ⟨hyL, hyB⟩ := Finset.mem_sdiff.mp hy
  have good : y ∈ H.goodPartners x := Finset.mem_sdiff.mpr ⟨Finset.mem_univ _, hyB⟩
  obtain ⟨yx, cxy⟩ := (H.mem_goodPartners cover x y).mp good
  exact ⟨x, y, yx.symm, dx, (Finset.mem_filter.mp hyL).2, cxy⟩

/-- Explicit five low locks with two disjoint exceptional pairs. -/
def FiveMatchingLocks (H : Simple5Hypergraph V) : Prop :=
  ∃ a b c d e : V,
    a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ a ≠ e ∧ b ≠ c ∧ b ≠ d ∧ b ≠ e ∧
    c ≠ d ∧ c ≠ e ∧ d ≠ e ∧
    (∀ x ∈ ({a,b,c,d,e} : Finset V), H.degree x = 6) ∧
    H.codegree a b = 2 ∧ H.codegree c d = 2 ∧
    H.codegree a c = 1 ∧ H.codegree a d = 1 ∧ H.codegree a e = 1 ∧
    H.codegree b c = 1 ∧ H.codegree b d = 1 ∧ H.codegree b e = 1 ∧
    H.codegree c e = 1 ∧ H.codegree d e = 1

omit [Fintype V] in
theorem exists_bad_of_not_unit (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (S : Finset V) (notunit : ¬ H.UnitCodegrees S) :
    ∃ a ∈ S, ∃ b ∈ S, a ≠ b ∧ 2 ≤ H.codegree a b := by
  unfold Simple5Hypergraph.UnitCodegrees at notunit
  push_neg at notunit
  obtain ⟨a,ha,b,hb,ab,nb⟩ := notunit
  have h := H.one_le_codegree cover ab
  exact ⟨a,ha,b,hb,ab,by omega⟩

/-- Any five low points without an independent four contain exactly two
disjoint bad pairs. The proof selects real points; no graph list is supplied. -/
theorem matching_five_of_no_unit_four (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (vertices : Fintype.card V = 24)
    (S : Finset V) (five : S.card = 5) (degrees : ∀ x ∈ S, H.degree x = 6)
    (noFour : ¬ ∃ T ⊆ S, T.card = 4 ∧ H.UnitCodegrees T) : FiveMatchingLocks H := by
  have notunit : ¬ H.UnitCodegrees S := by
    intro unit
    obtain ⟨T, subT, four⟩ := Finset.exists_subset_card_eq (show 4 ≤ S.card by omega)
    exact noFour ⟨T,subT,four,fun x hx y hy ne => unit x (subT hx) y (subT hy) ne⟩
  obtain ⟨a,ha,b,hb,ab,badAB⟩ := exists_bad_of_not_unit H cover S notunit
  have cab : H.codegree a b = 2 := by
    have upper := six_codegree_le_two H cover vertices (degrees a ha) ab
    omega
  let R := S \ {a,b}
  have absub : ({a,b} : Finset V) ⊆ S := by
    intro x hx
    rcases Finset.mem_insert.mp hx with rfl | hx
    · exact ha
    · exact Finset.mem_singleton.mp hx ▸ hb
  have rcard : R.card = 3 := by
    dsimp [R]
    rw [Finset.card_sdiff_of_subset absub, five]
    simp [ab]
  have memR (x : V) (hx : x ∈ R) : x ∈ S ∧ x ≠ a ∧ x ≠ b := by
    simpa only [R, Finset.mem_sdiff, Finset.mem_insert, Finset.mem_singleton,
      not_or] using hx
  have aunit (x : V) (hx : x ∈ R) : H.codegree a x = 1 :=
    unit_of_other_bad H cover vertices (degrees a ha) ab badAB
      (memR x hx).2.1.symm (memR x hx).2.2.symm
  have notR : ¬ H.UnitCodegrees R := by
    intro unitR
    apply noFour
    refine ⟨insert a R, Finset.insert_subset_iff.mpr ⟨ha,Finset.sdiff_subset⟩, ?_, ?_⟩
    · have an : a ∉ R := by simp [R]
      rw [Finset.card_insert_of_notMem an,rcard]
    · intro x hx y hy xy
      rcases Finset.mem_insert.mp hx with rfl | hx
      · rcases Finset.mem_insert.mp hy with rfl | hy
        · exact False.elim (xy rfl)
        · exact aunit y hy
      · rcases Finset.mem_insert.mp hy with rfl | hy
        · rw [H.codegree_comm]
          exact aunit x hx
        · exact unitR x hx y hy xy
  obtain ⟨c,hc,d,hd,cd,badCD⟩ := exists_bad_of_not_unit H cover R notR
  obtain ⟨hcS,ca,cb⟩ := memR c hc
  obtain ⟨hdS,da,db⟩ := memR d hd
  have ccd : H.codegree c d = 2 := by
    have upper := six_codegree_le_two H cover vertices (degrees c hcS) cd
    omega
  have cdcard : ({c,d} : Finset V).card = 2 := by simp [cd]
  have hdiff := Finset.card_le_card_sdiff_add_card (s := R) (t := {c,d})
  obtain ⟨e,he⟩ := Finset.card_pos.mp (show 0 < (R \ {c,d}).card by omega)
  obtain ⟨heR,hecd⟩ := Finset.mem_sdiff.mp he
  obtain ⟨heS,ea,eb⟩ := memR e heR
  have ec : e ≠ c := fun h => hecd (by simp [h])
  have ed : e ≠ d := fun h => hecd (by simp [h])
  have bunit (x : V) (hx : x ∈ R) : H.codegree b x = 1 := by
    apply unit_of_other_bad H cover vertices (degrees b hb) ab.symm
      (by simpa [H.codegree_comm] using badAB)
      (memR x hx).2.2.symm (memR x hx).2.1.symm
  refine ⟨a,b,c,d,e,ab,ca.symm,da.symm,ea.symm,cb.symm,db.symm,eb.symm,
    cd,ec.symm,ed.symm,?_,cab,ccd,aunit c hc,aunit d hd,aunit e heR,
    bunit c hc,bunit d hd,bunit e heR,?_,?_⟩
  · intro x hx
    have xs : x ∈ S := by
      simp only [Finset.mem_insert, Finset.mem_singleton] at hx
      rcases hx with rfl | rfl | rfl | rfl | rfl <;> assumption
    exact degrees x xs
  · exact unit_of_other_bad H cover vertices (degrees c hcS) cd badCD ec.symm ed.symm
  · apply unit_of_other_bad H cover vertices (degrees d hdS) cd.symm
      (by simpa [H.codegree_comm] using badCD) ed.symm ec.symm

/-- Complete first structural fork for the at-least-five-low-points branch. -/
theorem four_unit_or_five_matching (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 24) (many : 5 ≤ H.sixVertices.card) :
    (∃ S : Finset V, S.card = 4 ∧ (∀ x ∈ S, H.degree x = 6) ∧ H.UnitCodegrees S) ∨
    FiveMatchingLocks H := by
  by_cases four : ∃ S : Finset V,
      S.card = 4 ∧ (∀ x ∈ S, H.degree x = 6) ∧ H.UnitCodegrees S
  · exact Or.inl four
  · right
    obtain ⟨S,subS,five⟩ := Finset.exists_subset_card_eq many
    have degrees (x : V) (hx : x ∈ S) : H.degree x = 6 :=
      (Finset.mem_filter.mp (subS hx)).2
    apply matching_five_of_no_unit_four H cover vertices S five degrees
    rintro ⟨T,subT,hT,unit⟩
    exact four ⟨T,hT,fun x hx => degrees x (subT hx),unit⟩

/-- Ten seven-degree points cannot have every pair forbidden by codegree
or by crossing either of two pairs of three-element arms. -/
theorem exists_unit_pair_avoiding_crosses (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (vertices : Fintype.card V = 24)
    (T A B C D : Finset V) (many : 10 ≤ T.card)
    (degrees : ∀ x ∈ T, H.degree x = 7)
    (a3 : A.card ≤ 3) (b3 : B.card ≤ 3) (c3 : C.card ≤ 3) (d3 : D.card ≤ 3) :
    ∃ u ∈ T, ∃ v ∈ T, u ≠ v ∧ H.codegree u v = 1 ∧
      ¬ ((u ∈ A ∧ v ∈ B) ∨ (u ∈ B ∧ v ∈ A) ∨
         (u ∈ C ∧ v ∈ D) ∨ (u ∈ D ∧ v ∈ C)) := by
  let Bad := T.biUnion fun x => ({x} : Finset V) ×ˢ H.badPartners x
  let Cross := (A ×ˢ B) ∪ (B ×ˢ A) ∪ (C ×ˢ D) ∪ (D ×ˢ C)
  have badsize : Bad.card ≤ 5 * T.card := by
    calc
      Bad.card ≤ ∑ x ∈ T, (({x} : Finset V) ×ˢ H.badPartners x).card :=
        Finset.card_biUnion_le
      _ ≤ ∑ _x ∈ T, 5 := by
        apply Finset.sum_le_sum
        intro x hx
        have h := H.badPartners_card_le_excess cover x
        rw [vertices,degrees x hx] at h
        simpa only [Finset.card_product,Finset.card_singleton,one_mul] using h
      _ = 5 * T.card := by simp [Nat.mul_comm]
  have crosssize : Cross.card ≤ 36 := by
    have h1 := Finset.card_union_le (A ×ˢ B) (B ×ˢ A)
    have h2 := Finset.card_union_le ((A ×ˢ B) ∪ (B ×ˢ A)) (C ×ˢ D)
    have h3 := Finset.card_union_le (((A ×ˢ B) ∪ (B ×ˢ A)) ∪ (C ×ˢ D)) (D ×ˢ C)
    have ab : A.card * B.card ≤ 9 := by nlinarith
    have cd : C.card * D.card ≤ 9 := by nlinarith
    simp only [Finset.card_product] at h1 h2 h3
    dsimp [Cross]
    nlinarith
  have notcover : ¬ T.offDiag ⊆ Bad ∪ Cross := by
    intro hsub
    have h1 := Finset.card_le_card hsub
    have h2 := Finset.card_union_le Bad Cross
    rw [Finset.offDiag_card] at h1
    have hn : T.card * T.card ≤ 6 * T.card + 36 := by omega
    nlinarith
  obtain ⟨p,hp,hpout⟩ := Finset.not_subset.mp notcover
  obtain ⟨uT,vT,uv⟩ := Finset.mem_offDiag.mp hp
  have notbad : p ∉ Bad := fun h => hpout (Finset.mem_union_left _ h)
  have notcross : p ∉ Cross := fun h => hpout (Finset.mem_union_right _ h)
  have code : H.codegree p.1 p.2 = 1 := by
    have lo := H.one_le_codegree cover uv
    by_contra hn
    have bad : p.2 ∈ H.badPartners p.1 :=
      Finset.mem_filter.mpr ⟨Finset.mem_erase.mpr ⟨uv.symm,Finset.mem_univ _⟩,by omega⟩
    apply notbad
    exact Finset.mem_biUnion.mpr ⟨p.1,uT,
      Finset.mem_product.mpr ⟨Finset.mem_singleton_self _,bad⟩⟩
  refine ⟨p.1,uT,p.2,vT,uv,code,?_⟩
  simpa only [Cross,Finset.mem_union,Finset.mem_product,or_assoc] using notcross

omit [Fintype V] in
theorem avoid_one_arm (A B : Finset V) (disjoint : Disjoint A B) (u v : V)
    (nocross : ¬ ((u ∈ A ∧ v ∈ B) ∨ (u ∈ B ∧ v ∈ A))) :
    (u ∉ A ∧ v ∉ A) ∨ (u ∉ B ∧ v ∉ B) := by
  have notboth (w : V) : ¬ (w ∈ A ∧ w ∈ B) := by
    rintro ⟨hA,hB⟩
    exact Finset.disjoint_left.mp disjoint hA hB
  by_cases ua : u ∈ A
  · right
    exact ⟨fun ub => notboth u ⟨ua,ub⟩,fun vb => nocross (Or.inl ⟨ua,vb⟩)⟩
  · by_cases va : v ∈ A
    · right
      exact ⟨fun ub => nocross (Or.inr ⟨ub,va⟩),fun vb => notboth v ⟨va,vb⟩⟩
    · exact Or.inl ⟨ua,va⟩

omit [Fintype V] in
theorem edge_disjoint_of_arm (H : Simple5Hypergraph V)
    {x p : V} (bad : H.codegree x p = 2) (S E A : Finset V)
    (unit : ∀ q ∈ S, q ≠ x ∧ H.codegree x q = 1)
    (decomp : E = {x,p} ∪ A) (avoid : Disjoint A S) : Disjoint E S := by
  apply Finset.disjoint_left.mpr
  intro q qe qs
  rw [decomp] at qe
  rcases Finset.mem_union.mp qe with qp | qa
  · rcases Finset.mem_insert.mp qp with qx | qp
    · exact (unit q qs).1 qx
    · have qp := Finset.mem_singleton.mp qp
      have one := (unit q qs).2
      rw [qp,bad] at one
      contradiction
  · exact Finset.disjoint_left.mp avoid qa qs

/-- Five actual unit-codegree locks; each low center's real bad pair has an
edge avoiding all three high locks. This is the condition used by the table. -/
def MixedLocks (H : Simple5Hypergraph V) : Prop :=
  ∃ x y z u v : V,
    ({x,y,z,u,v} : Finset V).card = 5 ∧
    H.degree x = 6 ∧ H.degree y = 6 ∧
    H.degree z = 7 ∧ H.degree u = 7 ∧ H.degree v = 7 ∧
    H.UnitCodegrees {x,y,z,u,v} ∧
    (∀ P ∈ H.badLinkPairs x, ∃ E ∈ P, Disjoint E ({z,u,v} : Finset V)) ∧
    (∀ P ∈ H.badLinkPairs y, ∃ E ∈ P, Disjoint E ({z,u,v} : Finset V))

theorem mixed_locks_of_many_sevens (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 24)
    (many : 18 ≤ (sevenVertices H).card) : MixedLocks H := by
  obtain ⟨x,y,xy,dx,dy,cxy⟩ := exists_two_unit_six H cover edges vertices
  obtain ⟨px,Ex,Fx,Ax,Bx,pxx,cxpx,hEx,hFx,efx,interx,badx,
    ax,bx,ax3,bx3,disx,ex,fx⟩ :=
    TwentyFourUniqueBadPair.exists_unique_bad_pair_arms H cover vertices dx
  obtain ⟨py,Ey,Fy,Ay,By,pyy,cypy,hEy,hFy,efy,intery,bady,
    ay,by_,ay3,by3,disy,ey,fy⟩ :=
    TwentyFourUniqueBadPair.exists_unique_bad_pair_arms H cover vertices dy
  let C := sevenVertices H \ (H.badPartners x ∪ H.badPartners y)
  have csize : 16 ≤ C.card := by
    have h1 := Finset.card_le_card_sdiff_add_card (s := sevenVertices H)
      (t := H.badPartners x ∪ H.badPartners y)
    have h2 := Finset.card_union_le (H.badPartners x) (H.badPartners y)
    have hx := H.badPartners_card_le_one_of_twenty_four cover vertices dx
    have hy := H.badPartners_card_le_one_of_twenty_four cover vertices dy
    dsimp [C]
    omega
  have data (q : V) (hq : q ∈ C) :
      H.degree q = 7 ∧ q ≠ x ∧ q ≠ y ∧ H.codegree x q = 1 ∧ H.codegree y q = 1 := by
    obtain ⟨hq7,hqn⟩ := Finset.mem_sdiff.mp hq
    have dq : H.degree q = 7 := (Finset.mem_filter.mp hq7).2
    have qx : q ≠ x := by intro h; subst q; omega
    have qy : q ≠ y := by intro h; subst q; omega
    have xgood : q ∈ H.goodPartners x := by
      apply Finset.mem_sdiff.mpr
      refine ⟨Finset.mem_univ _, ?_⟩
      simp only [Finset.mem_insert,not_or]
      exact ⟨qx,fun h => hqn (Finset.mem_union_left _ h)⟩
    have ygood : q ∈ H.goodPartners y := by
      apply Finset.mem_sdiff.mpr
      refine ⟨Finset.mem_univ _, ?_⟩
      simp only [Finset.mem_insert,not_or]
      exact ⟨qy,fun h => hqn (Finset.mem_union_right _ h)⟩
    exact ⟨dq,qx,qy,(H.mem_goodPartners cover x q).mp xgood |>.2,
      (H.mem_goodPartners cover y q).mp ygood |>.2⟩
  let Arms := Ax ∪ Bx ∪ Ay ∪ By
  have armsize : Arms.card ≤ 12 := by
    have h1 := Finset.card_union_le Ax Bx
    have h2 := Finset.card_union_le (Ax ∪ Bx) Ay
    have h3 := Finset.card_union_le (Ax ∪ Bx ∪ Ay) By
    dsimp [Arms]
    omega
  have diff := Finset.card_le_card_sdiff_add_card (s := C) (t := Arms)
  obtain ⟨z,hz⟩ := Finset.card_pos.mp (show 0 < (C \ Arms).card by omega)
  obtain ⟨zC,znot⟩ := Finset.mem_sdiff.mp hz
  obtain ⟨dz,zx,zy,cxz,cyz⟩ := data z zC
  have zna : z ∉ Ax ∧ z ∉ Bx ∧ z ∉ Ay ∧ z ∉ By := by
    simpa only [Arms,Finset.mem_union,not_or,and_assoc] using znot
  let T := C \ insert z (H.badPartners z)
  have tsize : 10 ≤ T.card := by
    have h1 := Finset.card_le_card_sdiff_add_card (s := C) (t := insert z (H.badPartners z))
    have h2 := Finset.card_insert_le z (H.badPartners z)
    have h3 := H.badPartners_card_le_excess cover z
    rw [vertices,dz] at h3
    dsimp [T]
    omega
  have tdata (q : V) (hq : q ∈ T) : q ∈ C ∧ q ≠ z ∧ H.codegree z q = 1 := by
    obtain ⟨qC,qn⟩ := Finset.mem_sdiff.mp hq
    have good : q ∈ H.goodPartners z := Finset.mem_sdiff.mpr ⟨Finset.mem_univ _,qn⟩
    exact ⟨qC,(H.mem_goodPartners cover z q).mp good⟩
  obtain ⟨u,hu,v,hv,uv,cuv,nocross⟩ := exists_unit_pair_avoiding_crosses H cover vertices
    T Ax Bx Ay By tsize (fun q hq => (data q (tdata q hq).1).1)
    (by omega) (by omega) (by omega) (by omega)
  obtain ⟨uC,uz,czu⟩ := tdata u hu
  obtain ⟨vC,vz,czv⟩ := tdata v hv
  obtain ⟨du,ux,uy,cxu,cyu⟩ := data u uC
  obtain ⟨dv,vx,vy,cxv,cyv⟩ := data v vC
  have lowX (q : V) (hq : q ∈ ({z,u,v} : Finset V)) :
      q ≠ x ∧ H.codegree x q = 1 := by
    simp only [Finset.mem_insert,Finset.mem_singleton] at hq
    rcases hq with rfl | rfl | rfl <;> exact ⟨by assumption,by assumption⟩
  have lowY (q : V) (hq : q ∈ ({z,u,v} : Finset V)) :
      q ≠ y ∧ H.codegree y q = 1 := by
    simp only [Finset.mem_insert,Finset.mem_singleton] at hq
    rcases hq with rfl | rfl | rfl <;> exact ⟨by assumption,by assumption⟩
  have avoidance (A B E F : Finset V) (p w : V)
      (bad : H.codegree w p = 2)
      (unit : ∀ q ∈ ({z,u,v} : Finset V), q ≠ w ∧ H.codegree w q = 1)
      (e : E = {w,p} ∪ A) (f : F = {w,p} ∪ B)
      (dis : Disjoint A B) (za : z ∉ A) (zb : z ∉ B)
      (cross : ¬ ((u ∈ A ∧ v ∈ B) ∨ (u ∈ B ∧ v ∈ A))) :
      ∃ e ∈ ({E,F} : Finset (Finset V)), Disjoint e ({z,u,v} : Finset V) := by
    rcases avoid_one_arm A B dis u v cross with hA | hB
    · refine ⟨E,by simp,edge_disjoint_of_arm H bad _ E A unit e ?_⟩
      apply Finset.disjoint_right.mpr
      intro q hq
      simp only [Finset.mem_insert,Finset.mem_singleton] at hq
      rcases hq with rfl | rfl | rfl
      · exact za
      · exact hA.1
      · exact hA.2
    · refine ⟨F,by simp,edge_disjoint_of_arm H bad _ F B unit f ?_⟩
      apply Finset.disjoint_right.mpr
      intro q hq
      simp only [Finset.mem_insert,Finset.mem_singleton] at hq
      rcases hq with rfl | rfl | rfl
      · exact zb
      · exact hB.1
      · exact hB.2
  refine ⟨x,y,z,u,v,?_,dx,dy,dz,du,dv,?_,?_,?_⟩
  · simp [xy,zx.symm,zy.symm,ux.symm,uy.symm,uz.symm,vx.symm,vy.symm,vz.symm,uv]
  · intro a ha b hb ab
    simp only [Finset.mem_insert,Finset.mem_singleton] at ha hb
    rcases ha with rfl | rfl | rfl | rfl | rfl <;>
      rcases hb with rfl | rfl | rfl | rfl | rfl <;>
      first | exact (ab rfl).elim | assumption | (rw [H.codegree_comm]; assumption)
  · intro P hP
    rw [badx] at hP
    have pEq := Finset.mem_singleton.mp hP
    rw [pEq]
    exact avoidance Ax Bx Ex Fx px x cxpx lowX ex fx disx zna.1 zna.2.1
      (fun h => nocross (by rcases h with h | h; exact Or.inl h; exact Or.inr (Or.inl h)))
  · intro P hP
    rw [bady] at hP
    have pEq := Finset.mem_singleton.mp hP
    rw [pEq]
    exact avoidance Ay By Ey Fy py y cypy lowY ey fy disy zna.2.2.1 zna.2.2.2
      (fun h => nocross (Or.inr (Or.inr h)))

/-- Every actual 24-vertex reduced input has one of the three selected
configurations. The first branch retains its original at-least-five-low
hypothesis, needed to redirect a full four-point trace. -/
theorem selected_of_twenty_four (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (vertices : Fintype.card V = 24) :
    (5 ≤ H.sixVertices.card ∧
      ∃ S : Finset V, S.card = 4 ∧ (∀ x ∈ S, H.degree x = 6) ∧ H.UnitCodegrees S) ∨
    FiveMatchingLocks H ∨ MixedLocks H := by
  rcases five_six_or_many_seven H cover edges vertices with low | high
  · rcases four_unit_or_five_matching H cover vertices low with four | five
    · exact Or.inl ⟨low,four⟩
    · exact Or.inr (Or.inl five)
  · exact Or.inr (Or.inr (mixed_locks_of_many_sevens H cover edges vertices (by omega)))

end Aris4Math.ThirtyThree.TwentyFourSelection

#print axioms Aris4Math.ThirtyThree.TwentyFourSelection.five_six_or_many_seven
#print axioms Aris4Math.ThirtyThree.TwentyFourSelection.exists_two_unit_six
#print axioms Aris4Math.ThirtyThree.TwentyFourSelection.four_unit_or_five_matching
#print axioms Aris4Math.ThirtyThree.TwentyFourSelection.exists_unit_pair_avoiding_crosses
#print axioms Aris4Math.ThirtyThree.TwentyFourSelection.mixed_locks_of_many_sevens
#print axioms Aris4Math.ThirtyThree.TwentyFourSelection.selected_of_twenty_four
