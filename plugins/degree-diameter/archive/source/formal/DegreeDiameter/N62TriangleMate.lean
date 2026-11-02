import DegreeDiameter.N62STouch

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

private theorem sum_three_le (f : V → ℤ) (h0 : ∀ x, 0 ≤ f x)
    {a b c : V} (hab : a ≠ b) (hac : a ≠ c) (hbc : b ≠ c) :
    f a + f b + f c ≤ ∑ x, f x := by
  have h := Finset.sum_le_sum_of_subset_of_nonneg
    (Finset.subset_univ ({a,b,c} : Finset V)) (fun x _ _ => h0 x)
  simpa [hab, hac, hbc, add_assoc] using h

private theorem second_common_neighbor (G : SimpleGraph V) {x y a : V}
    (hc : 2 ≤ commonNeighborCount G x y) :
    ∃ b, b ≠ a ∧ G.Adj x b ∧ G.Adj b y := by
  by_contra h
  push_neg at h
  have hs : (G.neighborFinset x).filter (fun z => G.Adj z y) ⊆ {a} := by
    intro b hb
    have hb' : G.Adj x b ∧ G.Adj b y := by simpa using hb
    by_cases hba : b = a
    · simp [hba]
    · exact False.elim (h b hba hb'.1 hb'.2)
  have := Finset.card_le_card hs
  simp only [Finset.card_singleton] at this
  change commonNeighborCount G x y ≤ 1 at this
  omega

/-- In an actual order-62 graph, every original edge has defect at most one. -/
theorem n62_edge_defect_le_one (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r a : V} (hra : G.Adj r a) :
    defectMatrix G r a ≤ 1 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hs : ∑ x, defectMatrix G r x = 3 := by simpa [hcard] using defect_row_sum G hreg r
  by_contra hn
  have hc : 2 ≤ commonNeighborCount G r a := by
    have hh := defect_off_diagonal G hra.ne
    simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_pos hra] at hh
    omega
  obtain ⟨b, _, hrb, hba⟩ := second_common_neighbor G (a := a) hc
  obtain ⟨c, hcb, hrc, hca⟩ := second_common_neighbor G (a := b) hc
  have hb := defect_incident_triangle_ge_one G hrb hra hba.symm
  have hc' := defect_incident_triangle_ge_one G hrc hra hca.symm
  have hl := sum_three_le (defectMatrix G r) (defect_nonnegative G hreg hdiam r)
    hba.ne' hca.ne' hcb.symm
  omega

private theorem row_three_of_positive (f : V → ℤ) (h0 : ∀ x, 0 ≤ f x)
    (hs : ∑ x, f x = 3) {a b c : V} (hab : a ≠ b) (hac : a ≠ c) (hbc : b ≠ c)
    (ha : 1 ≤ f a) (hb : 1 ≤ f b) (hc : 1 ≤ f c) :
    ∀ x, f x = (if x = a then 1 else 0) + (if x = b then 1 else 0) +
      (if x = c then 1 else 0) := by
  let g : V → ℤ := fun x => (if x = a then 1 else 0) +
    (if x = b then 1 else 0) + (if x = c then 1 else 0)
  have hle (x : V) : g x ≤ f x := by
    by_cases hxa : x = a
    · subst x; simpa [g, hab, hac] using ha
    by_cases hxb : x = b
    · subst x; simpa [g, Ne.symm hab, hbc] using hb
    by_cases hxc : x = c
    · subst x; simpa [g, Ne.symm hac, Ne.symm hbc] using hc
    simpa [g, hxa, hxb, hxc] using h0 x
  have hsum : ∑ x, (f x - g x) = 0 := by
    rw [Finset.sum_sub_distrib, hs]
    simp [g, Finset.sum_add_distrib]
  intro x
  have hx := (Finset.sum_eq_zero_iff_of_nonneg (fun y _ => sub_nonneg.mpr (hle y))).mp hsum
    x (Finset.mem_univ x)
  exact sub_eq_zero.mp hx

/-- The third unit repeat mate is derived from the actual triangle and row sum. -/
theorem n62_triangle_third_mate (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r a b : V}
    (hra : G.Adj r a) (hrb : G.Adj r b) (hab : G.Adj a b) :
    ∃ w, w ≠ r ∧ w ≠ a ∧ w ≠ b ∧ ¬ G.Adj r w ∧ threeUnitRow G r a b w := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have h0 := defect_nonnegative G hreg hdiam r
  have hs : ∑ x, defectMatrix G r x = 3 := by simpa [hcard] using defect_row_sum G hreg r
  have ha : defectMatrix G r a = 1 := by
    have := defect_incident_triangle_ge_one G hra hrb hab.symm
    have := n62_edge_defect_le_one G hdeg hdiam hcard hra
    omega
  have hb : defectMatrix G r b = 1 := by
    have := defect_incident_triangle_ge_one G hrb hra hab
    have := n62_edge_defect_le_one G hdeg hdiam hcard hrb
    omega
  have h1 := Finset.sum_erase_add (s := Finset.univ) (defectMatrix G r) (Finset.mem_univ a)
  have h2 := Finset.sum_erase_add (s := Finset.univ.erase a) (defectMatrix G r)
    (by simp [hab.ne'] : b ∈ Finset.univ.erase a)
  have hpos : 0 < ∑ x ∈ (Finset.univ.erase a).erase b, defectMatrix G r x := by omega
  obtain ⟨w, hw, hwpos⟩ := (Finset.sum_pos_iff_of_nonneg (fun x _ => h0 x)).mp hpos
  have hwa : w ≠ a := (Finset.mem_erase.mp (Finset.mem_erase.mp hw).2).1
  have hwb : w ≠ b := (Finset.mem_erase.mp hw).1
  have hwr : w ≠ r := by intro h; subst w; rw [defect_diagonal G hreg] at hwpos; omega
  have hrow : threeUnitRow G r a b w := row_three_of_positive (defectMatrix G r) h0 hs
    hab.ne hwa.symm hwb.symm (by omega) (by omega) (by omega)
  have hn := three_unit_triangle_row_third_nonadj G hab hra.symm hrb.symm hwa hwb hrow
  exact ⟨w, hwr, hwa, hwb, hn, hrow⟩

/-- The only edge in the neighborhood of a triangle vertex is its triangle edge. -/
theorem n62_triangle_within_root (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r a b : V}
    (hra : G.Adj r a) (hrb : G.Adj r b) (hab : G.Adj a b) :
    ∀ x y, G.Adj r x → G.Adj r y →
      (G.Adj x y ↔ (x = a ∧ y = b) ∨ (x = b ∧ y = a)) := by
  obtain ⟨w, _, _, _, hn, hrow⟩ := n62_triangle_third_mate G hdeg hdiam hcard hra hrb hab
  have only (x y : V) (hrx : G.Adj r x) (hry : G.Adj r y) (hxy : G.Adj x y) :
      x = a ∨ x = b := by
    have hx := defect_incident_triangle_ge_one G hrx hry hxy.symm
    by_contra h
    push_neg at h
    have hxw : x ≠ w := by rintro rfl; exact hn hrx
    simp [threeUnitRow] at hrow
    simp [hrow, h.1, h.2, hxw] at hx
  intro x y hrx hry
  constructor
  · intro hxy
    rcases only x y hrx hry hxy with rfl | rfl <;>
      rcases only y _ hry hrx hxy.symm with rfl | rfl
    · exact False.elim (G.irrefl hxy)
    · exact Or.inl ⟨rfl,rfl⟩
    · exact Or.inr ⟨rfl,rfl⟩
    · exact False.elim (G.irrefl hxy)
  · rintro (⟨rfl,rfl⟩ | ⟨rfl,rfl⟩)
    · exact hab
    · exact hab.symm


private theorem triangle_mate_nonadj_first (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r a b w : V}
    (hra : G.Adj r a) (hrb : G.Adj r b) (hab : G.Adj a b)
    (hwr : w ≠ r) (hwa : w ≠ a) (hwb : w ≠ b)
    (hrw : ¬ G.Adj r w) (hrow : threeUnitRow G r a b w) : ¬ G.Adj a w := by
  intro haw
  have hc : commonNeighborCount G r w = 2 := by
    have hh := defect_off_diagonal G hwr.symm
    have hw1 : defectMatrix G r w = 1 := by simp [threeUnitRow] at hrow; simp [hrow, hwa, hwb]
    simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_neg hrw] at hh
    omega
  obtain ⟨c, hca, hrc, hcw⟩ := second_common_neighbor G (a := a) (by omega : 2 ≤ commonNeighborCount G r w)
  have hbw : ¬ G.Adj b w := by
    intro hbw
    have hh := n62_triangle_within_root G hdeg hdiam hcard hra.symm hab hrb b w hab haw
    have cases := hh.mp hbw
    rcases cases with hh | hh
    · exact hrb.ne hh.1.symm
    · exact hwr hh.2
  have hcb : c ≠ b := by rintro rfl; exact hbw hcw
  have hs : ({a,c} : Finset V) ⊆ (G.neighborFinset r).filter (fun x => G.Adj x w) := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl <;> simp [hra, haw, hrc, hcw]
  have heq : ({a,c} : Finset V) = (G.neighborFinset r).filter (fun x => G.Adj x w) := by
    apply Finset.eq_of_subset_of_card_le hs
    simpa [commonNeighborCount, hca.symm] using (le_of_eq hc)
  have ht : STouchTemplate G r a b c w := {
    root_a := hra
    root_b := hrb
    root_c := hrc
    edge_ab := hab
    a_ne_c := hca.symm
    b_ne_c := hcb.symm
    w_ne_root := hwr
    root_w_nonadj := hrw
    within_root := n62_triangle_within_root G hdeg hdiam hcard hra hrb hab
    exceptional_parents := by
      intro x hrx
      have hm := congrArg (fun s : Finset V => x ∈ s) heq
      simpa [hrx] using hm.symm
    ordinary_parent_unique := by
      intro y hyr hry hyw x x' hrx hrx' hxy hx'y
      by_contra hxx'
      have hp := defect_positive_of_two_common_neighbors G hyr.symm hxx' hry hrx hxy hrx' hx'y
      have hya : y ≠ a := by rintro rfl; exact hry hra
      have hyb : y ≠ b := by rintro rfl; exact hry hrb
      simp [threeUnitRow] at hrow
      simp [hrow, hya, hyb, hyw] at hp
  }
  exact no_n62_stouch_template G hdeg hdiam hcard ht

/-- Every third repeat mate of an actual triangle vertex has no original
neighbor anywhere in that triangle. The proof constructs the forbidden actual
S_TOUCH parent structure; no global simple-defect assumption is used. -/
theorem n62_triangle_mate_no_triangle_neighbor (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r a b w : V}
    (hra : G.Adj r a) (hrb : G.Adj r b) (hab : G.Adj a b)
    (hwr : w ≠ r) (hwa : w ≠ a) (hwb : w ≠ b)
    (hrow : threeUnitRow G r a b w) :
    ¬ G.Adj r w ∧ ¬ G.Adj a w ∧ ¬ G.Adj b w := by
  have hrw := three_unit_triangle_row_third_nonadj G hab hra.symm hrb.symm hwa hwb hrow
  have haw := triangle_mate_nonadj_first G hdeg hdiam hcard hra hrb hab hwr hwa hwb hrw hrow
  have hrow' : threeUnitRow G r b a w := by
    intro x
    rw [hrow]
    ring
  have hbw := triangle_mate_nonadj_first G hdeg hdiam hcard hrb hra hab.symm hwr hwb hwa hrw hrow'
  exact ⟨hrw, haw, hbw⟩

/-- Original-graph existence statement: every triangle vertex has a unit
repeat mate outside the triangle and its entire actual neighborhood. -/
theorem n62_triangle_mate_exists (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r a b : V}
    (hra : G.Adj r a) (hrb : G.Adj r b) (hab : G.Adj a b) :
    ∃ w, w ≠ r ∧ w ≠ a ∧ w ≠ b ∧ threeUnitRow G r a b w ∧
      ¬ G.Adj r w ∧ ¬ G.Adj a w ∧ ¬ G.Adj b w := by
  obtain ⟨w, hwr, hwa, hwb, _, hrow⟩ := n62_triangle_third_mate G hdeg hdiam hcard hra hrb hab
  exact ⟨w, hwr, hwa, hwb, hrow,
    n62_triangle_mate_no_triangle_neighbor G hdeg hdiam hcard hra hrb hab hwr hwa hwb hrow⟩


private theorem row_mate_edge (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    {r a b w u : V} (hrow : threeUnitRow G r a b w)
    (hra : G.Adj r a) (hau : defectMatrix G a u = 1)
    (hanu : ¬ G.Adj a u) (hbnu : ¬ G.Adj b u) : G.Adj w u := by
  have hnonneg (x : V) : 0 ≤ adjacencyMatrix G r x * defectMatrix G x u := by
    apply mul_nonneg
    · simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply]
      split_ifs <;> omega
    · exact defect_nonnegative G hreg hdiam x u
  have hh := Finset.single_le_sum (fun x _ => hnonneg x) (Finset.mem_univ a)
  have hl : 1 ≤ (adjacencyMatrix G * defectMatrix G) r u := by
    simpa [Matrix.mul_apply, adjacencyMatrix, hra, hau] using hh
  unfold threeUnitRow at hrow
  have hmul : (defectMatrix G * adjacencyMatrix G) r u =
      adjacencyMatrix G a u + adjacencyMatrix G b u + adjacencyMatrix G w u := by
    rw [Matrix.mul_apply]
    simp_rw [hrow, add_mul, ite_mul]
    simp [Finset.sum_add_distrib]
  rw [adjacency_defect_commute G hreg, hmul] at hl
  by_contra hwu
  simp [adjacencyMatrix, hanu, hbnu, hwu] at hl

/-- The three actual repeat mates form a disjoint actual triangle. Their
reciprocal repeat rows return the original triangle. This proves the local
pairing without a global simplicity assumption or a supplied matrix model. -/
theorem n62_triangle_has_paired_triangle (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r a b : V}
    (hra : G.Adj r a) (hrb : G.Adj r b) (hab : G.Adj a b) :
    ∃ w u v, G.Adj w u ∧ G.Adj w v ∧ G.Adj u v ∧
      Disjoint ({r,a,b} : Finset V) ({w,u,v} : Finset V) ∧
      (∀ x ∈ ({r,a,b} : Finset V), ∀ y ∈ ({w,u,v} : Finset V), ¬ G.Adj x y) ∧
      threeUnitRow G r a b w ∧ threeUnitRow G a r b u ∧ threeUnitRow G b r a v ∧
      threeUnitRow G w u v r ∧ threeUnitRow G u w v a ∧ threeUnitRow G v w u b := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsum (x : V) : ∑ y, defectMatrix G x y = 3 := by
    simpa [hcard] using defect_row_sum G hreg x
  obtain ⟨w, hwr, hwa, hwb, hR, hrw, haw, hbw⟩ :=
    n62_triangle_mate_exists G hdeg hdiam hcard hra hrb hab
  obtain ⟨u, hua, hur, hub, hA, hau, hru, hbu⟩ :=
    n62_triangle_mate_exists G hdeg hdiam hcard hra.symm hab hrb
  obtain ⟨v, hvb, hvr, hva, hB, hbv, hrv, hav⟩ :=
    n62_triangle_mate_exists G hdeg hdiam hcard hrb.symm hab.symm hra
  have hu1 : defectMatrix G a u = 1 := by simp [threeUnitRow] at hA; simp [hA, hur, hub]
  have hv1 : defectMatrix G b v = 1 := by simp [threeUnitRow] at hB; simp [hB, hvr, hva]
  have hwu := row_mate_edge G hreg hdiam hR hra hu1 hau hbu
  have hwv : G.Adj w v := by
    have hR' : threeUnitRow G r b a w := by intro x; rw [hR]; ring
    exact row_mate_edge G hreg hdiam hR' hrb hv1 hbv hav
  have huv : G.Adj u v := by
    have hA' : threeUnitRow G a b r u := by intro x; rw [hA]; ring
    exact row_mate_edge G hreg hdiam hA' hab hv1 hbv hrv
  have hdis : Disjoint ({r,a,b} : Finset V) ({w,u,v} : Finset V) := by
    apply Finset.disjoint_left.mpr
    intro x hx hy
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx hy
    rcases hx with rfl | rfl | rfl <;> rcases hy with h | h | h
    · exact hwr h.symm
    · exact hur h.symm
    · exact hvr h.symm
    · exact hwa h.symm
    · exact hua h.symm
    · exact hva h.symm
    · exact hwb h.symm
    · exact hub h.symm
    · exact hvb h.symm
  have hsep : ∀ x ∈ ({r,a,b} : Finset V), ∀ y ∈ ({w,u,v} : Finset V), ¬ G.Adj x y := by
    intro x hx y hy
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx hy
    rcases hx with rfl | rfl | rfl <;> rcases hy with rfl | rfl | rfl
    exact hrw
    exact hru
    exact hrv
    exact haw
    exact hau
    exact hav
    exact hbw
    exact hbu
    exact hbv
  have hwr1 : defectMatrix G w r = 1 := by
    rw [(defect_symmetric G).apply r w]
    simp [threeUnitRow] at hR
    simp [hR, hwa, hwb]
  have hua1 : defectMatrix G u a = 1 := by rw [(defect_symmetric G).apply a u]; exact hu1
  have hvb1 : defectMatrix G v b = 1 := by rw [(defect_symmetric G).apply b v]; exact hv1
  have hW : threeUnitRow G w u v r := row_three_of_positive (defectMatrix G w)
    (defect_nonnegative G hreg hdiam w) (hsum w) huv.ne hur hvr
    (defect_incident_triangle_ge_one G hwu hwv huv.symm)
    (defect_incident_triangle_ge_one G hwv hwu huv) (by omega)
  have hU : threeUnitRow G u w v a := row_three_of_positive (defectMatrix G u)
    (defect_nonnegative G hreg hdiam u) (hsum u) hwv.ne hwa hva
    (defect_incident_triangle_ge_one G hwu.symm huv hwv.symm)
    (defect_incident_triangle_ge_one G huv hwu.symm hwv) (by omega)
  have hV : threeUnitRow G v w u b := row_three_of_positive (defectMatrix G v)
    (defect_nonnegative G hreg hdiam v) (hsum v) hwu.ne hwb hub
    (defect_incident_triangle_ge_one G hwv.symm huv.symm hwu.symm)
    (defect_incident_triangle_ge_one G huv.symm hwv.symm hwu) (by omega)
  exact ⟨w,u,v,hwu,hwv,huv,hdis,hsep,hR,hA,hB,hW,hU,hV⟩

end
end DegreeDiameter
