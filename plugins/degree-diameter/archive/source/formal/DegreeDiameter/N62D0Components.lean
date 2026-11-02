import DegreeDiameter.N62D0Bin

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Actual shared D0 parent data, with no defect rows supplied. -/
structure D0ParentTemplate (G : SimpleGraph V) (r i j k b d w a : V) : Prop where
  root_i : G.Adj r i
  root_j : G.Adj r j
  root_k : G.Adj r k
  root_b : G.Adj r b
  root_d : G.Adj r d
  i_ne_j : i ≠ j
  i_ne_k : i ≠ k
  j_ne_k : j ≠ k
  b_ne_d : b ≠ d
  i_ne_b : i ≠ b
  i_ne_d : i ≠ d
  j_ne_b : j ≠ b
  j_ne_d : j ≠ d
  k_ne_b : k ≠ b
  k_ne_d : k ≠ d
  w_ne_root : w ≠ r
  a_ne_root : a ≠ r
  root_w_nonadj : ¬ G.Adj r w
  root_a_nonadj : ¬ G.Adj r a
  w_ne_a : w ≠ a
  root_independent : ∀ x y, G.Adj r x → G.Adj r y → ¬ G.Adj x y
  w_parents : ∀ x, G.Adj r x → (G.Adj x w ↔ x = i ∨ x = j ∨ x = k)
  a_parents : ∀ x, G.Adj r x → (G.Adj x a ↔ x = b ∨ x = d)
  ordinary_parent_unique : ∀ y, y ≠ r → ¬ G.Adj r y → y ≠ w → y ≠ a →
    ∀ x x', G.Adj r x → G.Adj r x' → G.Adj x y → G.Adj x' y → x = x'

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

private theorem double_of_three_common (G : SimpleGraph V) {x y p q t : V}
    (hxy : x ≠ y) (hn : ¬ G.Adj x y) (hpq : p ≠ q) (hpt : p ≠ t) (hqt : q ≠ t)
    (hxp : G.Adj x p) (hpy : G.Adj p y) (hxq : G.Adj x q) (hqy : G.Adj q y)
    (hxt : G.Adj x t) (hty : G.Adj t y) : 2 ≤ defectMatrix G x y := by
  have hs : ({p,q,t} : Finset V) ⊆ (G.neighborFinset x).filter (fun z => G.Adj z y) := by
    intro z hz
    simp only [Finset.mem_insert,Finset.mem_singleton] at hz
    rcases hz with rfl | rfl | rfl <;> simp [hxp,hpy,hxq,hqy,hxt,hty]
  have hc : 3 ≤ commonNeighborCount G x y := by
    simpa [commonNeighborCount,hpq,hpt,hqt] using Finset.card_le_card hs
  rw [defect_off_diagonal G hxy]
  simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hn]
  omega

private theorem row_third_from_two (f : V → ℤ) (h0 : ∀ x, 0 ≤ f x)
    (hs : ∑ x, f x = 3) {a b : V} (hab : a ≠ b) (ha : f a = 1) (hb : f b = 1) :
    ∃ c, c ≠ a ∧ c ≠ b ∧ ∀ x, f x = (if x = a then 1 else 0) +
      (if x = b then 1 else 0) + (if x = c then 1 else 0) := by
  have h1 := Finset.sum_erase_add (s := Finset.univ) f (Finset.mem_univ a)
  have h2 := Finset.sum_erase_add (s := Finset.univ.erase a) f
    (by simp [Ne.symm hab] : b ∈ Finset.univ.erase a)
  have hpos : 0 < ∑ x ∈ (Finset.univ.erase a).erase b, f x := by omega
  obtain ⟨c,hc,hfc⟩ := (Finset.sum_pos_iff_of_nonneg (fun x _ => h0 x)).mp hpos
  have hca : c ≠ a := (Finset.mem_erase.mp (Finset.mem_erase.mp hc).2).1
  have hcb : c ≠ b := (Finset.mem_erase.mp hc).1
  let g : V → ℤ := fun x => (if x = a then 1 else 0) +
    (if x = b then 1 else 0) + (if x = c then 1 else 0)
  have hle (x : V) : g x ≤ f x := by
    by_cases hxa : x = a
    · subst x; simp [g,hab,hca.symm,ha]
    by_cases hxb : x = b
    · subst x; simp [g,hab.symm,hcb.symm,hb]
    by_cases hxc : x = c
    · subst x; simp [g,hca,hcb]; omega
    simpa [g,hxa,hxb,hxc] using h0 x
  have hsum : ∑ x, (f x - g x) = 0 := by
    rw [Finset.sum_sub_distrib,hs]
    simp [g,Finset.sum_add_distrib]
  refine ⟨c,hca,hcb,?_⟩
  intro x
  have hx := (Finset.sum_eq_zero_iff_of_nonneg (fun y _ => sub_nonneg.mpr (hle y))).mp hsum
    x (Finset.mem_univ x)
  exact sub_eq_zero.mp hx


theorem n62_d0_parent_root_row (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k b d w a : V}
    (h : D0ParentTemplate G r i j k b d w a) :
    twoOneRow G r w a := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsum (v : V) : ∑ x, defectMatrix G v x = 3 := by
    simpa [hcard] using defect_row_sum G hreg v
  have h0 := defect_nonnegative G hreg hdiam
  have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
  have hjw : G.Adj j w := (h.w_parents j h.root_j).mpr (by simp)
  have hkw : G.Adj k w := (h.w_parents k h.root_k).mpr (by simp)
  have hba : G.Adj b a := (h.a_parents b h.root_b).mpr (by simp)
  have hda : G.Adj d a := (h.a_parents d h.root_d).mpr (by simp)
  have hrw := double_of_three_common G h.w_ne_root.symm h.root_w_nonadj
    h.i_ne_j h.i_ne_k h.j_ne_k h.root_i hiw h.root_j hjw h.root_k hkw
  have hra := defect_positive_of_two_common_neighbors G h.a_ne_root.symm h.b_ne_d
    h.root_a_nonadj h.root_b hba h.root_d hda
  have hR : twoOneRow G r w a := row_two_one_of_lower (defectMatrix G r) (h0 r) (hsum r)
    h.w_ne_a hrw (by omega)
  exact hR

private theorem d0_parent_common_set (G : SimpleGraph V) {r i j k b d w a x : V}
    (h : D0ParentTemplate G r i j k b d w a) (hrx : G.Adj r x) (hix : i ≠ x) :
    (G.neighborFinset i).filter (fun y => G.Adj y x) =
      insert r (if G.Adj x w then {w} else ∅) := by
  have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
  have hia : ¬ G.Adj i a := by rw [h.a_parents i h.root_i]; simp [h.i_ne_b,h.i_ne_d]
  ext y
  constructor
  · intro hy
    have hy' : G.Adj i y ∧ G.Adj y x := by simpa using hy
    by_cases hyr : y = r
    · simp [hyr]
    by_cases hyw : y = w
    · subst y
      simp [hy'.2.symm]
    exfalso
    have hya : y ≠ a := by rintro rfl; exact hia hy'.1
    have hry : ¬ G.Adj r y := fun hh => h.root_independent i y h.root_i hh hy'.1
    exact hix (h.ordinary_parent_unique y hyr hry hyw hya i x h.root_i hrx hy'.1 hy'.2.symm)
  · intro hy
    simp only [Finset.mem_insert] at hy
    rcases hy with rfl | hy
    · simp [h.root_i.symm,hrx]
    · by_cases hxw : G.Adj x w
      · have hyw : y = w := by simpa [hxw] using hy
        subst y
        simp [hiw,hxw.symm]
      · simp [hxw] at hy

/-- Actual common-neighbor counts fix the entire i-row on the root
neighborhood; its only unit entries there are j and k. -/
theorem n62_d0_parent_repeat_profile (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k b d w a : V}
    (h : D0ParentTemplate G r i j k b d w a) :
    ∀ x, G.Adj r x → defectMatrix G i x =
      (if x = j then 1 else 0) + (if x = k then 1 else 0) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  intro x hrx
  by_cases hxi : x = i
  · subst x
    simp [defect_diagonal G hreg,h.i_ne_j,h.i_ne_k]
  have hc := d0_parent_common_set G h hrx (Ne.symm hxi)
  have hixn := h.root_independent i x h.root_i hrx
  rw [defect_off_diagonal G (Ne.symm hxi)]
  simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hixn,add_zero]
  by_cases hxj : x = j
  · subst x
    have hjw : G.Adj j w := (h.w_parents j h.root_j).mpr (by simp)
    simp [commonNeighborCount,hc,hjw,h.w_ne_root.symm,h.j_ne_k]
  by_cases hxk : x = k
  · subst x
    have hkw : G.Adj k w := (h.w_parents k h.root_k).mpr (by simp)
    simp [commonNeighborCount,hc,hkw,h.w_ne_root.symm,h.j_ne_k.symm]
  have hxw : ¬ G.Adj x w := by rw [h.w_parents x hrx]; simp [hxi,hxj,hxk]
  simp [commonNeighborCount,hc,hxw,hxj,hxk]


private theorem three_unit_row_mul (G : SimpleGraph V) {v a b c y : V}
    (hr : threeUnitRow G v a b c) :
    (defectMatrix G * adjacencyMatrix G) v y =
      adjacencyMatrix G a y + adjacencyMatrix G b y + adjacencyMatrix G c y := by
  unfold threeUnitRow at hr
  rw [Matrix.mul_apply]
  simp_rw [hr,add_mul,ite_mul]
  simp [Finset.sum_add_distrib]

private theorem adjacency_defect_transpose_entry (G : SimpleGraph V) (x y : V) :
    (adjacencyMatrix G * defectMatrix G) x y = (defectMatrix G * adjacencyMatrix G) y x := by
  simp only [Matrix.mul_apply]
  apply Finset.sum_congr rfl
  intro z _
  have ha : adjacencyMatrix G x z = adjacencyMatrix G z x := by
    simp [adjacencyMatrix,SimpleGraph.adj_comm]
  rw [ha,(defect_symmetric G).apply y z]
  ring

private theorem two_neighbors_le_commuted (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    {v x z y : V} (hxz : x ≠ z) (hvx : G.Adj v x) (hvz : G.Adj v z) :
    defectMatrix G x y + defectMatrix G z y ≤ (defectMatrix G * adjacencyMatrix G) v y := by
  have h0 (t : V) : 0 ≤ adjacencyMatrix G v t * defectMatrix G t y := by
    apply mul_nonneg
    · simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply]
      split_ifs <;> omega
    · exact defect_nonnegative G hreg hdiam t y
  have hh := Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ ({x,z} : Finset V))
    (fun t _ _ => h0 t)
  have hl : defectMatrix G x y + defectMatrix G z y ≤ (adjacencyMatrix G * defectMatrix G) v y := by
    simpa [Matrix.mul_apply,adjacencyMatrix,hvx,hvz,hxz] using hh
  rwa [adjacency_defect_commute G hreg] at hl

private def D0ParentTemplate.rotate (G : SimpleGraph V) {r i j k p q w a : V}
    (h : D0ParentTemplate G r i j k p q w a) : D0ParentTemplate G r j k i p q w a where
  root_i := h.root_j
  root_j := h.root_k
  root_k := h.root_i
  root_b := h.root_b
  root_d := h.root_d
  i_ne_j := h.j_ne_k
  i_ne_k := h.i_ne_j.symm
  j_ne_k := h.i_ne_k.symm
  b_ne_d := h.b_ne_d
  i_ne_b := h.j_ne_b
  i_ne_d := h.j_ne_d
  j_ne_b := h.k_ne_b
  j_ne_d := h.k_ne_d
  k_ne_b := h.i_ne_b
  k_ne_d := h.i_ne_d
  w_ne_root := h.w_ne_root
  a_ne_root := h.a_ne_root
  root_w_nonadj := h.root_w_nonadj
  root_a_nonadj := h.root_a_nonadj
  w_ne_a := h.w_ne_a
  root_independent := h.root_independent
  w_parents := by intro x hx; rw [h.w_parents x hx]; tauto
  a_parents := h.a_parents
  ordinary_parent_unique := h.ordinary_parent_unique

private theorem d0_third_repeat (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k p q w a b : V}
    (h : D0ParentTemplate G r i j k p q w a)
    (hW : twoOneRow G w r b) (hib : i ≠ b) :
    ∃ c, c ≠ r ∧ ¬ G.Adj r c ∧ c ≠ w ∧ threeUnitRow G i j k c := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsum : ∑ x, defectMatrix G i x = 3 := by
    simpa [hcard] using defect_row_sum G hreg i
  have hp := n62_d0_parent_repeat_profile G hdeg hdiam hcard h
  have hij : defectMatrix G i j = 1 := by simpa [h.j_ne_k] using hp j h.root_j
  have hik : defectMatrix G i k = 1 := by simpa [h.j_ne_k.symm] using hp k h.root_k
  obtain ⟨c,hcj,hck,hI⟩ := row_third_from_two (defectMatrix G i)
    (defect_nonnegative G hreg hdiam i) hsum h.j_ne_k hij hik
  have hic : defectMatrix G i c = 1 := by simp [hI,hcj,hck]
  have hR := n62_d0_parent_root_row G hdeg hdiam hcard h
  unfold twoOneRow at hR hW
  have hiw : i ≠ w := by rintro rfl; exact h.root_w_nonadj h.root_i
  have hia : i ≠ a := by rintro rfl; exact h.root_a_nonadj h.root_i
  have hir : defectMatrix G i r = 0 := by
    rw [(defect_symmetric G).apply r i]
    simp [hR,hiw,hia]
  have hiw0 : defectMatrix G i w = 0 := by
    rw [(defect_symmetric G).apply w i]
    simp [hW,h.root_i.ne',hib]
  have hcr : c ≠ r := by intro hh; rw [hh] at hic; omega
  have hcw : c ≠ w := by intro hh; rw [hh] at hic; omega
  have hrc : ¬ G.Adj r c := by
    intro hh
    have hc0 := hp c hh
    simp [hcj,hck] at hc0
    omega
  exact ⟨c,hcr,hrc,hcw,hI⟩

private theorem d0_third_links (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k p q w a b : V}
    (h : D0ParentTemplate G r i j k p q w a)
    (hW : twoOneRow G w r b) (hib : i ≠ b) :
    ∃ c, ¬ G.Adj r c ∧ defectMatrix G i c = 1 ∧ G.Adj a c ∧ G.Adj b c := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain ⟨c,_,hrc,_,hI⟩ := d0_third_repeat G hdeg hdiam hcard h hW hib
  have hic : defectMatrix G i c = 1 := by
    have hcj : c ≠ j := by rintro rfl; exact hrc h.root_j
    have hck : c ≠ k := by rintro rfl; exact hrc h.root_k
    simp [threeUnitRow] at hI
    simp [hI,hcj,hck]
  have hR := n62_d0_parent_root_row G hdeg hdiam hcard h
  have hra : defectMatrix G r a = 1 := by simp [twoOneRow] at hR; simp [hR,h.w_ne_a.symm]
  have hja : ¬ G.Adj j a := by rw [h.a_parents j h.root_j]; simp [h.j_ne_b,h.j_ne_d]
  have hka : ¬ G.Adj k a := by rw [h.a_parents k h.root_k]; simp [h.k_ne_b,h.k_ne_d]
  have hac : G.Adj a c := by
    have hl := defect_neighbor_le_commuted G hreg hdiam h.root_i.symm (y := a)
    rw [three_unit_row_mul G hI] at hl
    by_contra hn
    have hca : ¬ G.Adj c a := fun hh => hn hh.symm
    simp [hra,adjacencyMatrix,hja,hka,hca] at hl
  have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
  have hbc : G.Adj b c := by
    have hl := defect_neighbor_le_commuted G hreg hdiam hiw.symm (y := c)
    rw [two_one_row_mul_adjacency G hW] at hl
    by_contra hn
    simp [hic,adjacencyMatrix,hrc,hn] at hl
  exact ⟨c,hrc,hic,hac,hbc⟩

/-- The alternating four rows are rows of the actual defect matrix. -/
def ClosedDoubleFour (G : SimpleGraph V) (r w b a : V) : Prop :=
  r ≠ w ∧ r ≠ b ∧ r ≠ a ∧ w ≠ b ∧ w ≠ a ∧ b ≠ a ∧
  twoOneRow G r w a ∧ twoOneRow G w r b ∧
  twoOneRow G a b r ∧ twoOneRow G b a w

private theorem d0_close_rows (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k p q w a b : V}
    (h : D0ParentTemplate G r i j k p q w a)
    (hW : twoOneRow G w r b) (hib : i ≠ b) (hjb : j ≠ b) (hkb : k ≠ b)
    (hbr : b ≠ r) (hba : b ≠ a) :
    ClosedDoubleFour G r w b a ∧ ¬ G.Adj a b := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hR := n62_d0_parent_root_row G hdeg hdiam hcard h
  have hrot := h.rotate G
  have hrot2 := hrot.rotate G
  obtain ⟨ci,hrci,hici,haci,hbci⟩ := d0_third_links G hdeg hdiam hcard h hW hib
  obtain ⟨cj,hrcj,hjcj,hacj,hbcj⟩ := d0_third_links G hdeg hdiam hcard hrot hW hjb
  obtain ⟨ck,hrck,hkck,hack,hbck⟩ := d0_third_links G hdeg hdiam hcard hrot2 hW hkb
  have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
  have hjw : G.Adj j w := (h.w_parents j h.root_j).mpr (by simp)
  have hkw : G.Adj k w := (h.w_parents k h.root_k).mpr (by simp)
  have hdij : ci ≠ cj := by
    intro hh; subst cj
    have hl := two_neighbors_le_commuted G hreg hdiam h.i_ne_j hiw.symm hjw.symm (y := ci)
    rw [two_one_row_mul_adjacency G hW] at hl
    simp [hici,hjcj,adjacencyMatrix,hrci,hbci] at hl
  have hdik : ci ≠ ck := by
    intro hh; subst ck
    have hl := two_neighbors_le_commuted G hreg hdiam h.i_ne_k hiw.symm hkw.symm (y := ci)
    rw [two_one_row_mul_adjacency G hW] at hl
    simp [hici,hkck,adjacencyMatrix,hrci,hbci] at hl
  have hdjk : cj ≠ ck := by
    intro hh; subst ck
    have hl := two_neighbors_le_commuted G hreg hdiam h.j_ne_k hjw.symm hkw.symm (y := cj)
    rw [two_one_row_mul_adjacency G hW] at hl
    simp [hjcj,hkck,adjacencyMatrix,hrcj,hbcj] at hl
  have hcn : 3 ≤ commonNeighborCount G a b := by
    have hs : ({ci,cj,ck} : Finset V) ⊆ (G.neighborFinset a).filter (fun t => G.Adj t b) := by
      intro t ht
      simp only [Finset.mem_insert,Finset.mem_singleton] at ht
      rcases ht with rfl | rfl | rfl <;> simp [haci,hacj,hack,hbci.symm,hbcj.symm,hbck.symm]
    simpa [commonNeighborCount,hdij,hdik,hdjk] using Finset.card_le_card hs
  have hnab : ¬ G.Adj a b := by
    intro hh
    have hh1 := n62_edge_defect_le_one G hdeg hdiam hcard hh
    have hh2 := defect_off_diagonal G hba.symm
    simp [adjacencyMatrix,hh] at hh2
    omega
  have hab2 := double_of_three_common G hba.symm hnab hdij hdik hdjk
    haci hbci.symm hacj hbcj.symm hack hbck.symm
  have har : defectMatrix G a r = 1 := by
    rw [(defect_symmetric G).apply r a]
    simp [twoOneRow] at hR
    simp [hR,h.w_ne_a.symm]
  have hsum (v : V) : ∑ x, defectMatrix G v x = 3 := by
    simpa [hcard] using defect_row_sum G hreg v
  have hA : twoOneRow G a b r := row_two_one_of_lower (defectMatrix G a)
    (defect_nonnegative G hreg hdiam a) (hsum a) hbr hab2 (by omega)
  have hwb : defectMatrix G w b = 1 := by simp [twoOneRow] at hW; simp [hW,hbr]
  have hbw : defectMatrix G b w = 1 := by rw [(defect_symmetric G).apply w b]; exact hwb
  have hba2 : 2 ≤ defectMatrix G b a := by rw [(defect_symmetric G).apply a b]; exact hab2
  have hB : twoOneRow G b a w := row_two_one_of_lower (defectMatrix G b)
    (defect_nonnegative G hreg hdiam b) (hsum b) h.w_ne_a.symm hba2 (by omega)
  have hwbne : w ≠ b := by intro hh; rw [hh,defect_diagonal G hreg] at hwb; omega
  exact ⟨⟨h.w_ne_root.symm,hbr.symm,h.a_ne_root.symm,hwbne,h.w_ne_a,hba,hR,hW,hA,hB⟩,hnab⟩

/-- A D0_MATCH root constructs an actual closed alternating double/unit
four-cycle in B; its four vertices are independent in the original graph. -/
theorem n62_d0_match_closed_component (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k p q w a : V}
    (h : D0ParentTemplate G r i j k p q w a) (hwa : ¬ G.Adj w a) :
    ∃ b, ClosedDoubleFour G r w b a ∧
      ¬ G.Adj r w ∧ ¬ G.Adj r b ∧ ¬ G.Adj r a ∧
      ¬ G.Adj w b ∧ ¬ G.Adj w a ∧ ¬ G.Adj b a := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hR := n62_d0_parent_root_row G hdeg hdiam hcard h
  have h0 := defect_nonnegative G hreg hdiam
  have hsum : ∑ x, defectMatrix G w x = 3 := by
    simpa [hcard] using defect_row_sum G hreg w
  have hwr : defectMatrix G w r = 2 := by
    rw [(defect_symmetric G).apply r w]
    simp [twoOneRow] at hR
    simp [hR,h.w_ne_a]
  have hx0 (x : V) (hrx : G.Adj r x) : defectMatrix G w x = 0 := by
    have hl := defect_neighbor_le_commuted G hreg hdiam hrx (y := w)
    rw [two_one_row_mul_adjacency G hR] at hl
    have haw : ¬ G.Adj a w := fun hh => hwa hh.symm
    simp [adjacencyMatrix,haw] at hl
    rw [(defect_symmetric G).apply x w]
    exact le_antisymm hl (h0 x w)
  have herase := Finset.sum_erase_add (s := Finset.univ) (defectMatrix G w) (Finset.mem_univ r)
  have hpos : 0 < ∑ x ∈ Finset.univ.erase r, defectMatrix G w x := by omega
  obtain ⟨b,hb,hwbpos⟩ := (Finset.sum_pos_iff_of_nonneg (fun x _ => h0 w x)).mp hpos
  have hbr : b ≠ r := (Finset.mem_erase.mp hb).1
  have hW : twoOneRow G w r b := row_two_one_of_lower (defectMatrix G w) (h0 w) hsum
    hbr.symm (by omega) (by omega)
  have hrb : ¬ G.Adj r b := by intro hh; have := hx0 b hh; omega
  have hib : i ≠ b := by rintro rfl; exact hrb h.root_i
  have hjb : j ≠ b := by rintro rfl; exact hrb h.root_j
  have hkb : k ≠ b := by rintro rfl; exact hrb h.root_k
  have hba : b ≠ a := by
    intro hba
    obtain ⟨c,_,_,_,hI⟩ := d0_third_repeat G hdeg hdiam hcard h hW hib
    have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
    have hja : ¬ G.Adj j a := by rw [h.a_parents j h.root_j]; simp [h.j_ne_b,h.j_ne_d]
    have hka : ¬ G.Adj k a := by rw [h.a_parents k h.root_k]; simp [h.k_ne_b,h.k_ne_d]
    have hra1 : defectMatrix G r a = 1 := by simp [twoOneRow] at hR; simp [hR,h.w_ne_a.symm]
    have hwa1 : defectMatrix G w a = 1 := by
      simp [twoOneRow] at hW
      simp [hW,← hba,hbr]
    have hl := two_neighbors_le_commuted G hreg hdiam h.w_ne_root.symm
      h.root_i.symm hiw (y := a)
    rw [three_unit_row_mul G hI] at hl
    simp only [hra1,hwa1,adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hja,if_neg hka] at hl
    split_ifs at hl <;> omega
  obtain ⟨hclosed,hnab⟩ := d0_close_rows G hdeg hdiam hcard h hW hib hjb hkb hbr hba
  have hB : twoOneRow G b a w := hclosed.2.2.2.2.2.2.2.2.2
  have hnwb : ¬ G.Adj w b := by
    intro hh
    have heq := adjacency_defect_transpose_entry G r b
    rw [adjacency_defect_commute G hreg,two_one_row_mul_adjacency G hR,
      two_one_row_mul_adjacency G hB] at heq
    have har : ¬ G.Adj a r := fun hh => h.root_a_nonadj hh.symm
    have hwrn : ¬ G.Adj w r := fun hh => h.root_w_nonadj hh.symm
    simp [adjacencyMatrix,hh,hnab,har,hwrn] at heq
  exact ⟨b,hclosed,h.root_w_nonadj,hrb,h.root_a_nonadj,hnwb,hwa,
    fun hh => hnab hh.symm⟩

/-- BOUT branch choice expressed entirely by actual root labels and two
actual common neighbors of w and b. -/
structure D0EdgeBoutTemplate (G : SimpleGraph V) (r i j k p q w a b : V) : Prop where
  parents : D0ParentTemplate G r i j k p q w a
  edge_wa : G.Adj w a
  root_b : G.Adj r b
  b_ne_i : b ≠ i
  b_ne_j : b ≠ j
  b_ne_k : b ≠ k
  b_ne_p : b ≠ p
  b_ne_q : b ≠ q
  bout_common_neighbors : ∃ t u, t ≠ u ∧ G.Adj w t ∧ G.Adj t b ∧ G.Adj w u ∧ G.Adj u b

/-- An actual unit nonedge repeat supplies exactly the kind of common-neighbor
witness accepted by the BOUT template. -/
theorem bout_common_neighbors_of_unit_repeat (G : SimpleGraph V) {w b : V}
    (hwb : w ≠ b) (hn : ¬ G.Adj w b) (hb : defectMatrix G w b = 1) :
    ∃ t u, t ≠ u ∧ G.Adj w t ∧ G.Adj t b ∧ G.Adj w u ∧ G.Adj u b := by
  obtain ⟨t,_,hwt,hbt⟩ := bin_common_neighbor_of_unit_repeat G (a := w) hwb hn hb
  obtain ⟨u,hut,hwu,hbu⟩ := bin_common_neighbor_of_unit_repeat G (a := t) hwb hn hb
  exact ⟨t,u,hut.symm,hwt,hbt.symm,hwu,hbu.symm⟩

/-- A D0_EDGE_BOUT branch closes the same four actual defect rows. Within
these four vertices the original graph has exactly the opposite edges rb and wa. -/
theorem n62_d0_bout_closed_component (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k p q w a b : V}
    (h : D0EdgeBoutTemplate G r i j k p q w a b) :
    ClosedDoubleFour G r w b a ∧ G.Adj r b ∧ G.Adj w a ∧
      ¬ G.Adj r w ∧ ¬ G.Adj r a ∧ ¬ G.Adj w b ∧ ¬ G.Adj b a := by
  have hp := h.parents
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hR := n62_d0_parent_root_row G hdeg hdiam hcard hp
  have hbw : ¬ G.Adj b w := by
    rw [hp.w_parents b h.root_b]
    simp [h.b_ne_i,h.b_ne_j,h.b_ne_k]
  have hwbne : w ≠ b := by rintro rfl; exact hp.root_w_nonadj h.root_b
  have hba : b ≠ a := by rintro rfl; exact hp.root_a_nonadj h.root_b
  have hbr : b ≠ r := h.root_b.ne'
  obtain ⟨t,u,htu,hwt,htb,hwu,hub⟩ := h.bout_common_neighbors
  have hwbpos := defect_positive_of_two_common_neighbors G hwbne htu
    (fun hh => hbw hh.symm) hwt htb hwu hub
  have hwr : defectMatrix G w r = 2 := by
    rw [(defect_symmetric G).apply r w]
    simp [twoOneRow] at hR
    simp [hR,hp.w_ne_a]
  have hsum : ∑ x, defectMatrix G w x = 3 := by
    simpa [hcard] using defect_row_sum G hreg w
  have hW : twoOneRow G w r b := row_two_one_of_lower (defectMatrix G w)
    (defect_nonnegative G hreg hdiam w) hsum hbr.symm (by omega) (by omega)
  obtain ⟨hc,hnab⟩ := d0_close_rows G hdeg hdiam hcard hp hW
    h.b_ne_i.symm h.b_ne_j.symm h.b_ne_k.symm hbr hba
  exact ⟨hc,h.root_b,h.edge_wa,hp.root_w_nonadj,hp.root_a_nonadj,
    fun hh => hbw hh.symm,fun hh => hnab hh.symm⟩


/-- The four derived rows admit no positive defect edge to any outside vertex. -/
theorem closedDoubleFour_no_external_repeat (G : SimpleGraph V) {r w b a v x : V}
    (h : ClosedDoubleFour G r w b a) (hv : v = r ∨ v = w ∨ v = b ∨ v = a)
    (hxr : x ≠ r) (hxw : x ≠ w) (hxb : x ≠ b) (hxa : x ≠ a) :
    defectMatrix G v x = 0 := by
  rcases h with ⟨_,_,_,_,_,_,hR,hW,hA,hB⟩
  unfold twoOneRow at hR hW hA hB
  rcases hv with rfl | rfl | rfl | rfl <;> simp [hR,hW,hA,hB,hxr,hxw,hxb,hxa]

/-- Complete semantic bridge from the actual BOUT unit-repeat branch to
its graph-only common-neighbor template. -/
theorem d0_bout_template_of_unit_repeat (G : SimpleGraph V) {r i j k p q w a b : V}
    (hp : D0ParentTemplate G r i j k p q w a) (hwa : G.Adj w a)
    (hrb : G.Adj r b) (hbi : b ≠ i) (hbj : b ≠ j) (hbk : b ≠ k)
    (hbp : b ≠ p) (hbq : b ≠ q) (hwb : defectMatrix G w b = 1) :
    D0EdgeBoutTemplate G r i j k p q w a b := by
  have hn : ¬ G.Adj w b := by
    intro hh
    have := (hp.w_parents b hrb).mp hh.symm
    tauto
  have hne : w ≠ b := by rintro rfl; exact hp.root_w_nonadj hrb
  exact ⟨hp,hwa,hrb,hbi,hbj,hbk,hbp,hbq,
    bout_common_neighbors_of_unit_repeat G hne hn hwb⟩

end
end DegreeDiameter
