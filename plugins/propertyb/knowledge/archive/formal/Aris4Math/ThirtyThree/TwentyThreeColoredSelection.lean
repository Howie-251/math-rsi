import Aris4Math.ThirtyThree.TwentyThreeSelection

/-!
The colored ten-vertex selection lemma used by the one-low-vertex branch.
The proof counts closed vertex sets; it does not enumerate graphs.
-/
namespace Aris4Math.ThirtyThree.TwentyThreeColoredSelection

open scoped BigOperators
open TwentyThreeSelection
variable {V C : Type*} [Fintype V] [DecidableEq V] [DecidableEq C]

def neighbors (R : V → V → Prop) [DecidableRel R] (x : V) : Finset V :=
  Finset.univ.filter (R x)

omit [DecidableEq V] in
@[simp] theorem mem_neighbors (R : V → V → Prop) [DecidableRel R] (x y : V) :
    y ∈ neighbors R x ↔ R x y := by simp [neighbors]

/-- A nonempty closed set in a triangle-free graph of minimum degree three
contains the disjoint neighborhoods of the endpoints of one edge. -/
theorem closed_card_ge_six (R : V → V → Prop) [DecidableRel R]
    (minimum : ∀ x, 3 ≤ (neighbors R x).card)
    (triangleFree : ∀ x y z, R x y → R x z → R y z → False)
    (S : Finset V) (nonempty : S.Nonempty)
    (closed : ∀ x ∈ S, ∀ y, R x y → y ∈ S) : 6 ≤ S.card := by
  obtain ⟨u,hu⟩ := nonempty
  obtain ⟨v,hv⟩ := Finset.card_pos.mp (show 0 < (neighbors R u).card by
    have h := minimum u
    omega)
  have huv : R u v := (mem_neighbors R u v).mp hv
  have vS := closed u hu v huv
  have disjoint : Disjoint (neighbors R u) (neighbors R v) := by
    apply Finset.disjoint_left.mpr
    intro w hwu hwv
    exact triangleFree u v w huv ((mem_neighbors R u w).mp hwu)
      ((mem_neighbors R v w).mp hwv)
  have subset : neighbors R u ∪ neighbors R v ⊆ S := by
    intro w hw
    rcases Finset.mem_union.mp hw with h | h
    · exact closed u hu w ((mem_neighbors R u w).mp h)
    · exact closed v vS w ((mem_neighbors R v w).mp h)
  have budget := Finset.card_le_card subset
  rw [Finset.card_union_of_disjoint disjoint] at budget
  have degreeU := minimum u
  have degreeV := minimum v
  omega

/-- On ten vertices, minimum degree three and color classes of size at most
four force a triangle or an induced three-vertex path with differently colored
endpoints. This is a general graph theorem, not a finite graph search. -/
theorem colored_ten_selection (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ x y, R x y → R y x)
    (irreflexive : ∀ x, ¬ R x x)
    (vertices : Fintype.card V = 10)
    (minimum : ∀ x, 3 ≤ (neighbors R x).card)
    (color : V → C)
    (colorBound : ∀ c, (Finset.univ.filter fun x => color x = c).card ≤ 4) :
    ∃ a b c, a ≠ b ∧ a ≠ c ∧ b ≠ c ∧ R a c ∧ R b c ∧
      (R a b ∨ (¬ R a b ∧ color a ≠ color b)) := by
  classical
  by_contra none
  have distinct {a b : V} (h : R a b) : a ≠ b := by
    intro e
    subst b
    exact irreflexive a h
  have triangleFree (a b c : V) (ab : R a b) (ac : R a c) (bc : R b c) : False :=
    none ⟨a,b,c,distinct ab,distinct ac,distinct bc,ac,bc,Or.inl ab⟩
  have neighborColor (x a b : V) (xa : R x a) (xb : R x b) : color a = color b := by
    by_cases equal : a = b
    · exact congrArg color equal
    by_contra different
    have ab : ¬ R a b := triangleFree x a b xa xb
    exact none ⟨a,b,x,equal,distinct (symmetric x a xa),distinct (symmetric x b xb),
      symmetric x a xa,symmetric x b xb,Or.inr ⟨ab,different⟩⟩
  obtain ⟨u,hu⟩ := Finset.card_pos.mp
    (show 0 < (Finset.univ : Finset V).card by simp [vertices])
  obtain ⟨v,hv⟩ := Finset.card_pos.mp (show 0 < (neighbors R u).card by
    have h := minimum u
    omega)
  have uv : R u v := (mem_neighbors R u v).mp hv
  let S := Finset.univ.filter fun z =>
    (color z = color u ∧ ∀ w, R z w → color w = color v) ∨
    (color z = color v ∧ ∀ w, R z w → color w = color u)
  have uS : u ∈ S := by
    apply Finset.mem_filter.mpr
    exact ⟨Finset.mem_univ u,Or.inl ⟨rfl,fun w hw => neighborColor u w v hw uv⟩⟩
  have closed : ∀ z ∈ S, ∀ w, R z w → w ∈ S := by
    intro z hz w hzw
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_univ w, ?_⟩
    rcases (Finset.mem_filter.mp hz).2 with ⟨hz,hs⟩ | ⟨hz,hs⟩
    · exact Or.inr ⟨hs w hzw,fun q hq =>
        (neighborColor w q z hq (symmetric z w hzw)).trans hz⟩
    · exact Or.inl ⟨hs w hzw,fun q hq =>
        (neighborColor w q z hq (symmetric z w hzw)).trans hz⟩
  have small : S.card ≤ 8 := by
    let A := Finset.univ.filter fun z => color z = color u
    let B := Finset.univ.filter fun z => color z = color v
    have sub : S ⊆ A ∪ B := by
      intro z hz
      rcases (Finset.mem_filter.mp hz).2 with ⟨hz,_⟩ | ⟨hz,_⟩
      · exact Finset.mem_union_left B (Finset.mem_filter.mpr ⟨Finset.mem_univ z,hz⟩)
      · exact Finset.mem_union_right A (Finset.mem_filter.mpr ⟨Finset.mem_univ z,hz⟩)
    have h1 := Finset.card_le_card sub
    have h2 := Finset.card_union_le A B
    have hA := colorBound (color u)
    have hB := colorBound (color v)
    change A.card ≤ 4 at hA
    change B.card ≤ 4 at hB
    omega
  have large := closed_card_ge_six R minimum triangleFree S ⟨u,uS⟩ closed
  let T := Finset.univ \ S
  have total : T.card + S.card = 10 := by
    simpa [T,vertices] using Finset.card_sdiff_add_card_eq_card (Finset.subset_univ S)
  have Tnonempty : T.Nonempty := Finset.card_pos.mp (by omega)
  have Tclosed : ∀ z ∈ T, ∀ w, R z w → w ∈ T := by
    intro z hz w hzw
    apply Finset.mem_sdiff.mpr
    refine ⟨Finset.mem_univ w,?_⟩
    intro hw
    exact (Finset.mem_sdiff.mp hz).2 (closed w hw z (symmetric z w hzw))
  have Tlarge := closed_card_ge_six R minimum triangleFree T Tnonempty Tclosed
  omega

/-- A low/high bad pair leaves ten actual seven-degree common unit neighbors.
The already occupied bad-neighbor slots at x and y are removed explicitly. -/
theorem exists_ten_common_unit (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (highs : 17 ≤ (sevenVertices H).card)
    (x y : V) (dx : H.degree x = 6) (dy : H.degree y = 7)
    (bad : 2 ≤ H.codegree x y) :
    ∃ T : Finset V, T.card = 10 ∧ ∀ a ∈ T,
      H.degree a = 7 ∧ a ≠ x ∧ a ≠ y ∧
        H.codegree x a = 1 ∧ H.codegree y a = 1 := by
  have xy : x ≠ y := by intro h; rw [h] at dx; omega
  have ybad : y ∈ H.badPartners x := Finset.mem_filter.mpr
    ⟨Finset.mem_erase.mpr ⟨xy.symm,Finset.mem_univ y⟩,bad⟩
  have xbad : x ∈ H.badPartners y := Finset.mem_filter.mpr
    ⟨Finset.mem_erase.mpr ⟨xy,Finset.mem_univ x⟩,by simpa [H.codegree_comm y x] using bad⟩
  let A := (H.badPartners x).erase y
  let B := (H.badPartners y).erase x
  let F := insert y (A ∪ B)
  let P := sevenVertices H \ F
  have Asize : A.card ≤ 1 := by
    have h := six_badPartners_le_two H cover vertices dx
    dsimp [A]
    rw [Finset.card_erase_of_mem ybad]
    omega
  have Bsize : B.card ≤ 5 := by
    have h := seven_badPartners_le_six H cover vertices dy
    dsimp [B]
    rw [Finset.card_erase_of_mem xbad]
    omega
  have Fsize : F.card ≤ 7 := by
    have hu := Finset.card_union_le A B
    have hi := Finset.card_insert_le y (A ∪ B)
    dsimp [F]
    omega
  have Psize : 10 ≤ P.card := by
    have h := Finset.card_le_card_sdiff_add_card (s := sevenVertices H) (t := F)
    change (sevenVertices H).card ≤ P.card + F.card at h
    omega
  obtain ⟨T,sub,card⟩ := Finset.exists_subset_card_eq Psize
  refine ⟨T,card,?_⟩
  intro a ha
  obtain ⟨ha7,haF⟩ := Finset.mem_sdiff.mp (sub ha)
  have da : H.degree a = 7 := (mem_sevenVertices H a).mp ha7
  have ax : a ≠ x := by intro h; rw [h] at da; omega
  have ay : a ≠ y := fun h => haF (h ▸ Finset.mem_insert_self y (A ∪ B))
  have anotx : a ∉ H.badPartners x := by
    intro ha
    exact haF (Finset.mem_insert_of_mem (Finset.mem_union_left B
      (Finset.mem_erase.mpr ⟨ay,ha⟩)))
  have anoty : a ∉ H.badPartners y := by
    intro ha
    exact haF (Finset.mem_insert_of_mem (Finset.mem_union_right A
      (Finset.mem_erase.mpr ⟨ax,ha⟩)))
  have agoodx : a ∈ H.goodPartners x := Finset.mem_sdiff.mpr
    ⟨Finset.mem_univ a,by simpa only [Finset.mem_insert,not_or] using And.intro ax anotx⟩
  have agoody : a ∈ H.goodPartners y := Finset.mem_sdiff.mpr
    ⟨Finset.mem_univ a,by simpa only [Finset.mem_insert,not_or] using And.intro ay anoty⟩
  exact ⟨da,ax,ay,((H.mem_goodPartners cover x a).mp agoodx).2,
    ((H.mem_goodPartners cover y a).mp agoody).2⟩

/-- Apply the ten-vertex graph theorem to the actual unit-codegree graph.
Colors are actual unique edges through y, so different endpoint colors exclude
an actual edge through all of y,a,b. -/
theorem actual_colored_selection (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (y : V) (T : Finset V)
    (card : T.card = 10)
    (facts : ∀ a ∈ T, H.degree a = 7 ∧ a ≠ y ∧ H.codegree y a = 1) :
    ∃ a ∈ T, ∃ b ∈ T, ∃ c ∈ T,
      a ≠ b ∧ a ≠ c ∧ b ≠ c ∧ H.codegree a c = 1 ∧ H.codegree b c = 1 ∧
      (H.codegree a b = 1 ∨ ∀ e ∈ H.edges, ¬ (y ∈ e ∧ a ∈ e ∧ b ∈ e)) := by
  classical
  let R : ↥T → ↥T → Prop := fun a b => a ≠ b ∧ H.codegree a.val b.val = 1
  have Rdec : DecidableRel R := inferInstance
  have symmetric (a b : ↥T) (h : R a b) : R b a :=
    ⟨h.1.symm,(H.codegree_comm b.val a.val).trans h.2⟩
  have irreflexive (a : ↥T) : ¬ R a a := fun h => h.1 rfl
  have cardT : Fintype.card ↥T = 10 := by simpa using card
  have minimum (a : ↥T) : 3 ≤ (neighbors R a).card := by
    let D := Finset.univ \ neighbors R a
    have sub : D.image Subtype.val ⊆ insert a.val (H.badPartners a.val) := by
      intro z hz
      obtain ⟨b,hb,rfl⟩ := Finset.mem_image.mp hz
      by_cases equal : b.val = a.val
      · exact Finset.mem_insert.mpr (Or.inl equal)
      have ab : a ≠ b := by intro h; exact equal (congrArg Subtype.val h.symm)
      have notunit : H.codegree a.val b.val ≠ 1 := by
        intro unit
        exact (Finset.mem_sdiff.mp hb).2 ((mem_neighbors R a b).mpr ⟨ab,unit⟩)
      have lower := H.one_le_codegree cover (Ne.symm equal)
      apply Finset.mem_insert_of_mem
      exact Finset.mem_filter.mpr ⟨Finset.mem_erase.mpr ⟨equal,Finset.mem_univ b.val⟩,
        by omega⟩
    have hs := Finset.card_le_card sub
    rw [Finset.card_image_of_injective D Subtype.val_injective] at hs
    have hb := seven_badPartners_le_six H cover vertices (facts a.val a.property).1
    have hi := Finset.card_insert_le a.val (H.badPartners a.val)
    have budget : D.card + (neighbors R a).card = 10 := by
      simpa [D,card] using Finset.card_sdiff_add_card_eq_card
        (Finset.subset_univ (neighbors R a))
    omega
  have chosen (a : ↥T) : ∃ e ∈ H.edges, y ∈ e ∧ a.val ∈ e :=
    cover y a.val (facts a.val a.property).2.1.symm
  let color : ↥T → Finset V := fun a => Classical.choose (chosen a)
  have colorFacts (a : ↥T) : color a ∈ H.edges ∧ y ∈ color a ∧ a.val ∈ color a :=
    Classical.choose_spec (chosen a)
  have colorBound (e : Finset V) :
      (Finset.univ.filter fun a : ↥T => color a = e).card ≤ 4 := by
    let F := Finset.univ.filter fun a : ↥T => color a = e
    by_cases empty : F = ∅
    · change F.card ≤ 4
      simp [empty]
    obtain ⟨a,ha⟩ := Finset.nonempty_iff_ne_empty.mpr empty
    have colorA : color a = e := (Finset.mem_filter.mp ha).2
    have efacts := colorFacts a
    rw [colorA] at efacts
    have sub : F.image Subtype.val ⊆ e.erase y := by
      intro z hz
      obtain ⟨b,hb,rfl⟩ := Finset.mem_image.mp hz
      have cb : color b = e := (Finset.mem_filter.mp hb).2
      have bEdge := (colorFacts b).2.2
      rw [cb] at bEdge
      exact Finset.mem_erase.mpr ⟨(facts b.val b.property).2.1,bEdge⟩
    have hs := Finset.card_le_card sub
    rw [Finset.card_image_of_injective F Subtype.val_injective,
      Finset.card_erase_of_mem efacts.2.1,H.five_uniform e efacts.1] at hs
    exact hs
  obtain ⟨a,b,c,ab,ac,bc,cac,cbc,choice⟩ := colored_ten_selection R symmetric
    irreflexive cardT minimum color colorBound
  have distinct {a b : ↥T} (h : a ≠ b) : a.val ≠ b.val :=
    fun same => h (Subtype.ext same)
  refine ⟨a.val,a.property,b.val,b.property,c.val,c.property,
    distinct ab,distinct ac,distinct bc,cac.2,cbc.2,?_⟩
  rcases choice with hab | ⟨_,different⟩
  · exact Or.inl hab.2
  · right
    intro e he ⟨ey,ea,eb⟩
    have eqa : e = color a := H.edge_unique_of_codegree_one
      (facts a.val a.property).2.2 he (colorFacts a).1 ey ea
      (colorFacts a).2.1 (colorFacts a).2.2
    have eqb : e = color b := H.edge_unique_of_codegree_one
      (facts b.val b.property).2.2 he (colorFacts b).1 ey eb
      (colorFacts b).2.1 (colorFacts b).2.2
    exact different (eqa.symm.trans eqb)

/-- The full actual five-lock selection when a six-degree vertex has a
seven-degree bad partner. The forbidden triple comes from real edge colors. -/
theorem exists_locks_low_bad_high (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices : Fintype.card V = 23) (highs : 17 ≤ (sevenVertices H).card)
    (x y : V) (dx : H.degree x = 6) (dy : H.degree y = 7)
    (bad : 2 ≤ H.codegree x y) :
    ∃ f : Fin 5 → V, Function.Injective f ∧ f 0 = x ∧ f 1 = y ∧
      (∀ i, H.degree (f i) = if i = 0 then 6 else 7) ∧
      (2 ≤ H.codegree (f 0) (f 1) ∧ H.codegree (f 0) (f 1) ≤ 3) ∧
      (∀ i j, i < j → ¬ (i = 0 ∧ j = 1) → ¬ (i = 2 ∧ j = 3) →
        H.codegree (f i) (f j) = 1) ∧
      (H.codegree (f 2) (f 3) ≠ 1 → ∀ e ∈ H.edges,
        ¬ (f 1 ∈ e ∧ f 2 ∈ e ∧ f 3 ∈ e)) := by
  obtain ⟨T,card,facts⟩ := exists_ten_common_unit H cover vertices highs x y dx dy bad
  obtain ⟨a,ha,b,hb,c,hc,ab,ac,bc,cac,cbc,choice⟩ :=
    actual_colored_selection H cover vertices y T card
      (fun z hz => ⟨(facts z hz).1,(facts z hz).2.2.1,(facts z hz).2.2.2.2⟩)
  obtain ⟨da,ax,ay,cxa,cya⟩ := facts a ha
  obtain ⟨db,bx,by',cxb,cyb⟩ := facts b hb
  obtain ⟨dc,cx,cy,cxc,cyc⟩ := facts c hc
  have xy : x ≠ y := by intro h; rw [h] at dx; omega
  let f : Fin 5 → V := ![x,y,a,b,c]
  have finj : Function.Injective f := by
    intro i j heq
    fin_cases i <;> fin_cases j <;>
      simp [f,xy,xy.symm,ax,ax.symm,bx,bx.symm,cx,cx.symm,
        ay,ay.symm,by',by'.symm,cy,cy.symm,ab,ab.symm,ac,ac.symm,bc,bc.symm] at heq <;> rfl
  refine ⟨f,finj,rfl,rfl,?_,⟨bad,?_⟩,?_,?_⟩
  · intro i
    fin_cases i <;> simp [f,dx,dy,da,db,dc]
  · exact six_codegree_le_three H cover vertices dx xy
  · intro i j hij h01 h23
    fin_cases i <;> fin_cases j <;> simp only [Fin.lt_def] at hij <;> norm_num at hij <;>
      simp [Fin.ext_iff] at h01 <;> simp [Fin.ext_iff] at h23 <;>
      first | exact cxa | exact cxb | exact cxc | exact cya |
        exact cyb | exact cyc | exact cac | exact cbc
  · intro notunit
    rcases choice with unit | excluded
    · exact False.elim (notunit unit)
    · exact excluded

theorem exists_locks_low_bad_high_of_count (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges : H.edges.card = 33)
    (vertices : Fintype.card V = 23) (count : H.sixVertices.card = 1)
    (x y : V) (dx : H.degree x = 6) (dy : H.degree y = 7)
    (bad : 2 ≤ H.codegree x y) :
    ∃ f : Fin 5 → V, Function.Injective f ∧ f 0 = x ∧ f 1 = y ∧
      (∀ i, H.degree (f i) = if i = 0 then 6 else 7) ∧
      (2 ≤ H.codegree (f 0) (f 1) ∧ H.codegree (f 0) (f 1) ≤ 3) ∧
      (∀ i j, i < j → ¬ (i = 0 ∧ j = 1) → ¬ (i = 2 ∧ j = 3) →
        H.codegree (f i) (f j) = 1) ∧
      (H.codegree (f 2) (f 3) ≠ 1 → ∀ e ∈ H.edges,
        ¬ (f 1 ∈ e ∧ f 2 ∈ e ∧ f 3 ∈ e)) := by
  have budget := six_seven_budget H cover edges vertices
  exact exists_locks_low_bad_high H cover vertices (by omega) x y dx dy bad

end Aris4Math.ThirtyThree.TwentyThreeColoredSelection

#print axioms Aris4Math.ThirtyThree.TwentyThreeColoredSelection.colored_ten_selection
#print axioms Aris4Math.ThirtyThree.TwentyThreeColoredSelection.exists_ten_common_unit
#print axioms Aris4Math.ThirtyThree.TwentyThreeColoredSelection.actual_colored_selection
#print axioms Aris4Math.ThirtyThree.TwentyThreeColoredSelection.exists_locks_low_bad_high_of_count
