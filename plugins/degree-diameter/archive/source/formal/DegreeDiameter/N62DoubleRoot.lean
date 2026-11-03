import DegreeDiameter.N62D0Components

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- The actual parents of y in the neighborhood of r. -/
def rootParents (G : SimpleGraph V) (r y : V) : Finset V :=
  (G.neighborFinset r).filter (fun x => G.Adj x y)

@[simp] theorem mem_rootParents (G : SimpleGraph V) (r y x : V) :
    x ∈ rootParents G r y ↔ G.Adj r x ∧ G.Adj x y := by simp [rootParents]

/-- Local graph-only parent data derived from one actual double repeat.
The structure does not contain any assumed defect row. -/
structure DoubleRootParentData (G : SimpleGraph V) (r w a : V) : Prop where
  w_ne_root : w ≠ r
  a_ne_root : a ≠ r
  w_ne_a : w ≠ a
  root_w_nonadj : ¬ G.Adj r w
  root_a_nonadj : ¬ G.Adj r a
  root_independent : ∀ x y, G.Adj r x → G.Adj r y → ¬ G.Adj x y
  w_parent_card : (rootParents G r w).card = 3
  a_parent_card : (rootParents G r a).card = 2
  ordinary_parent : ∀ y, y ≠ r → ¬ G.Adj r y → y ≠ w → y ≠ a →
    ∃! x, G.Adj r x ∧ G.Adj x y

private theorem row_two_one_of_lower (f : V → ℤ) (h0 : ∀ x, 0 ≤ f x)
    (hs : ∑ x, f x = 3) {a b : V} (hab : a ≠ b) (ha : 2 ≤ f a) (hb : 1 ≤ f b) :
    ∀ x, f x = 2 * (if x = a then 1 else 0) + (if x = b then 1 else 0) := by
  let g : V → ℤ := fun x => 2 * (if x = a then 1 else 0) + (if x = b then 1 else 0)
  have hle (x : V) : g x ≤ f x := by
    by_cases hxa : x = a
    · subst x; simpa [g,hab] using ha
    by_cases hxb : x = b
    · subst x; simpa [g,Ne.symm hab] using hb
    simpa [g,hxa,hxb] using h0 x
  have hsum : ∑ x, (f x - g x) = 0 := by
    rw [Finset.sum_sub_distrib,hs]
    simp [g,Finset.sum_add_distrib,Finset.mul_sum]
  intro x
  have hx := (Finset.sum_eq_zero_iff_of_nonneg (fun y _ => sub_nonneg.mpr (hle y))).mp hsum
    x (Finset.mem_univ x)
  exact sub_eq_zero.mp hx

/-- Either endpoint of an actual double repeat lies in no original triangle. -/
theorem n62_double_endpoint_zero_triangle (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w : V} (hb : defectMatrix G r w = 2) :
    zeroTriangleVertex G r := by
  have hn : ¬ G.Adj r w := by
    intro ha
    have := n62_edge_defect_le_one G hdeg hdiam hcard ha
    omega
  intro x y hrx hry hxy
  obtain ⟨c,_,_,_,_,hr⟩ := n62_triangle_third_mate G hdeg hdiam hcard hrx hry hxy
  have hwx : w ≠ x := by rintro rfl; exact hn hrx
  have hwy : w ≠ y := by rintro rfl; exact hn hry
  have heq := hr w
  simp only [hwx,hwy,if_false,zero_add,threeUnitRow] at heq
  split_ifs at heq <;> omega

private theorem residual_unit_row (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w : V} (hb : defectMatrix G r w = 2) :
    ∃ a, a ≠ w ∧ twoOneRow G r w a := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have h0 := defect_nonnegative G hreg hdiam r
  have hsum : ∑ x, defectMatrix G r x = 3 := by simpa [hcard] using defect_row_sum G hreg r
  have he := Finset.sum_erase_add (s := Finset.univ) (defectMatrix G r) (Finset.mem_univ w)
  have hpos : 0 < ∑ x ∈ Finset.univ.erase w, defectMatrix G r x := by omega
  obtain ⟨a,ha,hapos⟩ := (Finset.sum_pos_iff_of_nonneg (fun x _ => h0 x)).mp hpos
  have haw := (Finset.mem_erase.mp ha).1
  exact ⟨a,haw,row_two_one_of_lower (defectMatrix G r) h0 hsum haw.symm (by omega) (by omega)⟩

/-- One actual double entry constructs the full root parent normal form:
three parents of w, two of a, and exactly one for every ordinary external point. -/
theorem n62_double_root_normal_form (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w : V} (hb : defectMatrix G r w = 2) :
    ∃ a, DoubleRootParentData G r w a ∧ twoOneRow G r w a ∧
      zeroTriangleVertex G r ∧ zeroTriangleVertex G w := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hrz := n62_double_endpoint_zero_triangle G hdeg hdiam hcard hb
  have hwb : defectMatrix G w r = 2 := by rw [(defect_symmetric G).apply r w]; exact hb
  have hwz := n62_double_endpoint_zero_triangle G hdeg hdiam hcard hwb
  have hwr : w ≠ r := by intro hh; rw [hh,defect_diagonal G hreg] at hb; omega
  have hrwn : ¬ G.Adj r w := by
    intro ha
    have := zero_vertex_edge_defect_zero G hrz ha
    omega
  obtain ⟨a,haw,hR⟩ := residual_unit_row G hdeg hdiam hcard hb
  have hra : defectMatrix G r a = 1 := by simp [twoOneRow] at hR; simp [hR,haw]
  have har : a ≠ r := by intro hh; rw [hh,defect_diagonal G hreg] at hra; omega
  have hran : ¬ G.Adj r a := by
    intro ha
    have := zero_vertex_edge_defect_zero G hrz ha
    omega
  have hpcw : (rootParents G r w).card = 3 := by
    have hh := defect_off_diagonal G hwr.symm
    simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hrwn] at hh
    change commonNeighborCount G r w = 3
    omega
  have hpca : (rootParents G r a).card = 2 := by
    have hh := defect_off_diagonal G har.symm
    simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hran] at hh
    change commonNeighborCount G r a = 2
    omega
  refine ⟨a,⟨hwr,har,haw.symm,hrwn,hran,hrz,hpcw,hpca,?_⟩,hR,hrz,hwz⟩
  intro y hyr hry hyw hya
  have hry0 : defectMatrix G r y = 0 := by simp [twoOneRow] at hR; simp [hR,hyw,hya]
  have hcy : (rootParents G r y).card = 1 := by
    have hh := defect_off_diagonal G hyr.symm
    simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hry] at hh
    change commonNeighborCount G r y = 1
    omega
  obtain ⟨x,hx⟩ := Finset.card_eq_one.mp hcy
  have hxm : x ∈ rootParents G r y := by rw [hx]; simp
  refine ⟨x,(mem_rootParents G r y x).mp hxm,?_⟩
  intro z hz
  have hzm : z ∈ rootParents G r y := (mem_rootParents G r y z).mpr hz
  simpa [hx] using hzm

/-- Adjacency of the two exceptional vertices forces disjoint actual parent sets. -/
theorem double_root_edge_parents_disjoint (G : SimpleGraph V) {r w a : V}
    (hwz : zeroTriangleVertex G w) (hwa : G.Adj w a) :
    Disjoint (rootParents G r w) (rootParents G r a) := by
  apply Finset.disjoint_left.mpr
  intro x hxw hxa
  have h1 := (mem_rootParents G r w x).mp hxw
  have h2 := (mem_rootParents G r a x).mp hxa
  exact hwz x a h1.2.symm hwa h2.2

/-- The local parent overlap has precisely the three possible sizes 0,1,2;
positive overlap forces the exceptional pair to be an original nonedge. -/
theorem n62_double_root_overlap_classification (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w : V} (hb : defectMatrix G r w = 2) :
    ∃ a, DoubleRootParentData G r w a ∧ twoOneRow G r w a ∧
      (((rootParents G r w) ∩ (rootParents G r a)).card = 0 ∨
       (((rootParents G r w) ∩ (rootParents G r a)).card = 1 ∧ ¬ G.Adj w a) ∨
       (((rootParents G r w) ∩ (rootParents G r a)).card = 2 ∧ ¬ G.Adj w a)) := by
  obtain ⟨a,hp,hR,_,hwz⟩ := n62_double_root_normal_form G hdeg hdiam hcard hb
  have hle := Finset.card_le_card (Finset.inter_subset_right :
    rootParents G r w ∩ rootParents G r a ⊆ rootParents G r a)
  rw [hp.a_parent_card] at hle
  have hnonzero (hpos : 0 < (rootParents G r w ∩ rootParents G r a).card) : ¬ G.Adj w a := by
    intro ha
    have hd := double_root_edge_parents_disjoint G (r := r) hwz ha
    have hz := Finset.disjoint_iff_inter_eq_empty.mp hd
    rw [hz] at hpos
    simp at hpos
  refine ⟨a,hp,hR,?_⟩
  by_cases h0 : (rootParents G r w ∩ rootParents G r a).card = 0
  · exact Or.inl h0
  by_cases h1 : (rootParents G r w ∩ rootParents G r a).card = 1
  · exact Or.inr (Or.inl ⟨h1,hnonzero (by omega)⟩)
  · exact Or.inr (Or.inr ⟨by omega,hnonzero (by omega)⟩)


/-- An actual overlap of size two supplies the existing D2_MATCH caller. -/
theorem double_root_overlap_two_template (G : SimpleGraph V) {r w a : V}
    (hp : DoubleRootParentData G r w a) (hwz : zeroTriangleVertex G w)
    (h2 : (rootParents G r w ∩ rootParents G r a).card = 2) :
    ∃ i j k, D2MatchTemplate G r i j k w a := by
  have he : rootParents G r w ∩ rootParents G r a = rootParents G r a :=
    Finset.eq_of_subset_of_card_le Finset.inter_subset_right (by rw [hp.a_parent_card,h2])
  have hsub : rootParents G r a ⊆ rootParents G r w := by
    intro x hx
    have : x ∈ rootParents G r w ∩ rootParents G r a := by rw [he]; exact hx
    exact (Finset.mem_inter.mp this).1
  obtain ⟨i,j,hij,hA⟩ := Finset.card_eq_two.mp hp.a_parent_card
  have him : i ∈ rootParents G r a := by rw [hA]; simp
  have hjm : j ∈ rootParents G r a := by rw [hA]; simp
  have hi := (mem_rootParents G r a i).mp him
  have hj := (mem_rootParents G r a j).mp hjm
  have hiw := (mem_rootParents G r w i).mp (hsub him)
  have hjw := (mem_rootParents G r w j).mp (hsub hjm)
  have hlt : (rootParents G r a).card < (rootParents G r w).card := by
    rw [hp.a_parent_card,hp.w_parent_card]; omega
  obtain ⟨k,hkwm,hkam⟩ := Finset.exists_mem_notMem_of_card_lt_card hlt
  have hk := (mem_rootParents G r w k).mp hkwm
  have hki : k ≠ i := by intro hh; subst k; exact hkam him
  have hkj : k ≠ j := by intro hh; subst k; exact hkam hjm
  have hW : rootParents G r w = {i,j,k} := by
    have hs : ({i,j,k} : Finset V) ⊆ rootParents G r w := by
      simp [Finset.insert_subset_iff,hsub him,hsub hjm,hkwm]
    exact (Finset.eq_of_subset_of_card_le hs (by simp [hp.w_parent_card,hij,hki.symm,hkj.symm])).symm
  have hnwa : ¬ G.Adj w a := fun ha => hwz i a hiw.2.symm ha hi.2
  refine ⟨i,j,k,⟨hi.1,hj.1,hk.1,hij,hki.symm,hkj.symm,hp.w_ne_root,
    hp.a_ne_root,hp.w_ne_a,hp.root_w_nonadj,hp.root_a_nonadj,hnwa,
    hp.root_independent,?_,?_,?_⟩⟩
  · intro x hrx
    have hx : (G.Adj r x ∧ G.Adj x w) ↔ x = i ∨ x = j ∨ x = k := by
      have := mem_rootParents G r w x
      rw [hW] at this
      simpa using this.symm
    simpa [hrx] using hx
  · intro x hrx
    have hx : (G.Adj r x ∧ G.Adj x a) ↔ x = i ∨ x = j := by
      have := mem_rootParents G r a x
      rw [hA] at this
      simpa using this.symm
    simpa [hrx] using hx
  · intro y hyr hry hyw hya x x' hrx hrx' hxy hx'y
    obtain ⟨z,_,hz⟩ := hp.ordinary_parent y hyr hry hyw hya
    exact (hz x ⟨hrx,hxy⟩).trans (hz x' ⟨hrx',hx'y⟩).symm

/-- Existing D2 exclusion removes actual overlap two from a double root. -/
theorem n62_double_root_overlap_two_impossible (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w a : V}
    (hp : DoubleRootParentData G r w a) (hwz : zeroTriangleVertex G w)
    (h2 : (rootParents G r w ∩ rootParents G r a).card = 2) : False := by
  obtain ⟨i,j,k,h⟩ := double_root_overlap_two_template G hp hwz h2
  exact no_n62_d2_match_template G hdeg hdiam hcard h

/-- Actual D1 branch, expressed using finite parent sets and original
adjacency only. Its parent data is constructed from actual double entries. -/
structure D1MatchParentTemplate (G : SimpleGraph V) (r w a : V) : Prop where
  parents : DoubleRootParentData G r w a
  w_a_nonadj : ¬ G.Adj w a
  parent_overlap_one : (rootParents G r w ∩ rootParents G r a).card = 1

/-- Every actual double root is D0 or D1; overlap-two templates have been
connected to and eliminated by the existing actual D2 theorem. -/
theorem n62_double_root_d0_or_d1 (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w : V} (hb : defectMatrix G r w = 2) :
    ∃ a, twoOneRow G r w a ∧
      ((DoubleRootParentData G r w a ∧ Disjoint (rootParents G r w) (rootParents G r a)) ∨
       D1MatchParentTemplate G r w a) := by
  obtain ⟨a,hp,hR,hcases⟩ := n62_double_root_overlap_classification G hdeg hdiam hcard hb
  have hwr : defectMatrix G w r = 2 := by rw [(defect_symmetric G).apply r w]; exact hb
  have hwz := n62_double_endpoint_zero_triangle G hdeg hdiam hcard hwr
  refine ⟨a,hR,?_⟩
  rcases hcases with h0 | ⟨h1,hn⟩ | ⟨h2,_⟩
  · exact Or.inl ⟨hp,Finset.disjoint_iff_inter_eq_empty.mpr (Finset.card_eq_zero.mp h0)⟩
  · exact Or.inr ⟨hp,hn,h1⟩
  · exact False.elim (n62_double_root_overlap_two_impossible G hdeg hdiam hcard hp hwz h2)


/-- Disjoint actual parent sets provide all labeled D0 template fields. -/
theorem double_root_disjoint_parent_template (G : SimpleGraph V) {r w a : V}
    (hp : DoubleRootParentData G r w a)
    (hd : Disjoint (rootParents G r w) (rootParents G r a)) :
    ∃ i j k p q, D0ParentTemplate G r i j k p q w a := by
  obtain ⟨i,j,k,hij,hik,hjk,hW⟩ := Finset.card_eq_three.mp hp.w_parent_card
  obtain ⟨p,q,hpq,hA⟩ := Finset.card_eq_two.mp hp.a_parent_card
  have him : i ∈ rootParents G r w := by rw [hW]; simp
  have hjm : j ∈ rootParents G r w := by rw [hW]; simp
  have hkm : k ∈ rootParents G r w := by rw [hW]; simp
  have hpm : p ∈ rootParents G r a := by rw [hA]; simp
  have hqm : q ∈ rootParents G r a := by rw [hA]; simp
  have hi := (mem_rootParents G r w i).mp him
  have hj := (mem_rootParents G r w j).mp hjm
  have hk := (mem_rootParents G r w k).mp hkm
  have hpp := (mem_rootParents G r a p).mp hpm
  have hqq := (mem_rootParents G r a q).mp hqm
  have hsep (x y : V) (hx : x ∈ rootParents G r w) (hy : y ∈ rootParents G r a) : x ≠ y := by
    intro hh; subst y
    exact Finset.disjoint_left.mp hd hx hy
  refine ⟨i,j,k,p,q,⟨hi.1,hj.1,hk.1,hpp.1,hqq.1,hij,hik,hjk,hpq,
    hsep i p him hpm,hsep i q him hqm,hsep j p hjm hpm,hsep j q hjm hqm,
    hsep k p hkm hpm,hsep k q hkm hqm,hp.w_ne_root,hp.a_ne_root,
    hp.root_w_nonadj,hp.root_a_nonadj,hp.w_ne_a,hp.root_independent,?_,?_,?_⟩⟩
  · intro x hrx
    have hx := mem_rootParents G r w x
    rw [hW] at hx
    simpa [hrx] using hx.symm
  · intro x hrx
    have hx := mem_rootParents G r a x
    rw [hA] at hx
    simpa [hrx] using hx.symm
  · intro y hyr hry hyw hya x x' hrx hrx' hxy hx'y
    obtain ⟨z,_,hz⟩ := hp.ordinary_parent y hyr hry hyw hya
    exact (hz x ⟨hrx,hxy⟩).trans (hz x' ⟨hrx',hx'y⟩).symm

/-- Original actual-double caller: D1 parent overlap one, or a fully
constructed existing D0 parent template. No supplied local template is assumed. -/
theorem n62_double_root_template_coverage (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w : V} (hb : defectMatrix G r w = 2) :
    ∃ a, twoOneRow G r w a ∧
      (D1MatchParentTemplate G r w a ∨ ∃ i j k p q, D0ParentTemplate G r i j k p q w a) := by
  obtain ⟨a,hR,hd | h1⟩ := n62_double_root_d0_or_d1 G hdeg hdiam hcard hb
  · exact ⟨a,hR,Or.inr (double_root_disjoint_parent_template G hd.1 hd.2)⟩
  · exact ⟨a,hR,Or.inl h1⟩

/-- The actual D0 nonadjacent branch immediately supplies a closed component. -/
theorem n62_double_root_d0_match_closed (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w a : V}
    (hp : DoubleRootParentData G r w a)
    (hd : Disjoint (rootParents G r w) (rootParents G r a))
    (hwa : ¬ G.Adj w a) : ∃ b, ClosedDoubleFour G r w b a := by
  obtain ⟨i,j,k,p,q,h⟩ := double_root_disjoint_parent_template G hp hd
  obtain ⟨b,hb,_⟩ := n62_d0_match_closed_component G hdeg hdiam hcard h hwa
  exact ⟨b,hb⟩


private def swap_d0_parents (G : SimpleGraph V) {r i j k p q w a : V}
    (h : D0ParentTemplate G r i j k p q w a) : D0ParentTemplate G r i j k q p w a where
  root_i := h.root_i
  root_j := h.root_j
  root_k := h.root_k
  root_b := h.root_d
  root_d := h.root_b
  i_ne_j := h.i_ne_j
  i_ne_k := h.i_ne_k
  j_ne_k := h.j_ne_k
  b_ne_d := h.b_ne_d.symm
  i_ne_b := h.i_ne_d
  i_ne_d := h.i_ne_b
  j_ne_b := h.j_ne_d
  j_ne_d := h.j_ne_b
  k_ne_b := h.k_ne_d
  k_ne_d := h.k_ne_b
  w_ne_root := h.w_ne_root
  a_ne_root := h.a_ne_root
  root_w_nonadj := h.root_w_nonadj
  root_a_nonadj := h.root_a_nonadj
  w_ne_a := h.w_ne_a
  root_independent := h.root_independent
  w_parents := h.w_parents
  a_parents := by intro x hx; rw [h.a_parents x hx]; tauto
  ordinary_parent_unique := h.ordinary_parent_unique

private theorem d0_edge_no_first_parent_repeat (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k p q w a : V}
    (h : D0ParentTemplate G r i j k p q w a) (hwa : G.Adj w a)
    (hwp : defectMatrix G w p = 1) : False := by
  have hne : w ≠ p := by rintro rfl; exact h.root_w_nonadj h.root_b
  have hn : ¬ G.Adj w p := by
    intro hh
    have := (h.w_parents p h.root_b).mp hh.symm
    rcases this with hh | hh | hh
    · exact h.i_ne_b hh.symm
    · exact h.j_ne_b hh.symm
    · exact h.k_ne_b hh.symm
  have hwitness := bin_common_neighbor_of_unit_repeat G (a := a) hne hn hwp
  apply no_n62_d0_edge_bin_template G hdeg hdiam hcard (r := r) (i := i) (j := j)
    (k := k) (b := p) (d := q) (w := w) (a := a)
  exact {
    root_i := h.root_i
    root_j := h.root_j
    root_k := h.root_k
    root_b := h.root_b
    root_d := h.root_d
    i_ne_j := h.i_ne_j
    i_ne_k := h.i_ne_k
    j_ne_k := h.j_ne_k
    b_ne_d := h.b_ne_d
    i_ne_b := h.i_ne_b
    i_ne_d := h.i_ne_d
    j_ne_b := h.j_ne_b
    j_ne_d := h.j_ne_d
    k_ne_b := h.k_ne_b
    k_ne_d := h.k_ne_d
    w_ne_root := h.w_ne_root
    a_ne_root := h.a_ne_root
    root_w_nonadj := h.root_w_nonadj
    root_a_nonadj := h.root_a_nonadj
    root_independent := h.root_independent
    w_parents := h.w_parents
    a_parents := h.a_parents
    ordinary_parent_unique := h.ordinary_parent_unique
    edge_wa := hwa
    bin_common_neighbor := hwitness }

private theorem adjacency_defect_transpose_entry (G : SimpleGraph V) (x y : V) :
    (adjacencyMatrix G * defectMatrix G) x y = (defectMatrix G * adjacencyMatrix G) y x := by
  simp only [Matrix.mul_apply]
  apply Finset.sum_congr rfl
  intro z _
  have ha : adjacencyMatrix G x z = adjacencyMatrix G z x := by
    simp [adjacencyMatrix,SimpleGraph.adj_comm]
  rw [ha,(defect_symmetric G).apply y z]
  ring


/-- The actual adjacent D0 branch supplies BOUT after its residual repeat
is constructed and the two BIN possibilities are excluded. -/
theorem n62_d0_edge_closed_from_parents (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k p q w a : V}
    (h : D0ParentTemplate G r i j k p q w a) (hwa : G.Adj w a) :
    ∃ b, ClosedDoubleFour G r w b a := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hR := n62_d0_parent_root_row G hdeg hdiam hcard h
  have hwr : defectMatrix G w r = 2 := by
    rw [(defect_symmetric G).apply r w]
    simp [twoOneRow] at hR
    simp [hR,h.w_ne_a]
  obtain ⟨b,hbr,hW⟩ := residual_unit_row G hdeg hdiam hcard hwr
  have hwb : defectMatrix G w b = 1 := by simp [twoOneRow] at hW; simp [hW,hbr]
  have hwz := n62_double_endpoint_zero_triangle G hdeg hdiam hcard hwr
  have hnwb : ¬ G.Adj w b := by
    intro hh
    have := zero_vertex_edge_defect_zero G hwz hh
    omega
  have hrb : G.Adj r b := by
    by_contra hn
    have hbn : ¬ G.Adj b r := fun hh => hn hh.symm
    have heq := adjacency_defect_transpose_entry G r w
    rw [adjacency_defect_commute G hreg,two_one_row_mul_adjacency G hR,
      two_one_row_mul_adjacency G hW] at heq
    simp [adjacencyMatrix,hwa.symm,hbn] at heq
  have hbi : b ≠ i := by
    intro hh
    have hiw := (h.w_parents i h.root_i).mpr (by simp)
    exact hnwb (hh.symm ▸ hiw.symm)
  have hbj : b ≠ j := by
    intro hh
    have hjw := (h.w_parents j h.root_j).mpr (by simp)
    exact hnwb (hh.symm ▸ hjw.symm)
  have hbk : b ≠ k := by
    intro hh
    have hkw := (h.w_parents k h.root_k).mpr (by simp)
    exact hnwb (hh.symm ▸ hkw.symm)
  have hbp : b ≠ p := by
    intro hh
    rw [hh] at hwb
    exact d0_edge_no_first_parent_repeat G hdeg hdiam hcard h hwa hwb
  have hbq : b ≠ q := by
    intro hh
    rw [hh] at hwb
    exact d0_edge_no_first_parent_repeat G hdeg hdiam hcard (swap_d0_parents G h) hwa hwb
  have hbout := d0_bout_template_of_unit_repeat G h hwa hrb hbi hbj hbk hbp hbq hwb
  exact ⟨b,(n62_d0_bout_closed_component G hdeg hdiam hcard hbout).1⟩

/-- Actual local heavy-root coverage: each double entry either has a D1
parent representative at its root, or belongs to a closed alternating B4.
No global defect bound or local certificate is required. -/
theorem n62_double_root_d1_or_closed_component (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w : V} (hb : defectMatrix G r w = 2) :
    (∃ a, D1MatchParentTemplate G r w a) ∨ (∃ a b, ClosedDoubleFour G r w b a) := by
  obtain ⟨a,_,h1 | h0⟩ := n62_double_root_template_coverage G hdeg hdiam hcard hb
  · exact Or.inl ⟨a,h1⟩
  · obtain ⟨i,j,k,p,q,h⟩ := h0
    by_cases hwa : G.Adj w a
    · obtain ⟨b,hb⟩ := n62_d0_edge_closed_from_parents G hdeg hdiam hcard h hwa
      exact Or.inr ⟨a,b,hb⟩
    · obtain ⟨b,hb,_⟩ := n62_d0_match_closed_component G hdeg hdiam hcard h hwa
      exact Or.inr ⟨a,b,hb⟩

end
end DegreeDiameter
