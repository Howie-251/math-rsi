import DegreeDiameter.N62D2

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Actual D0_EDGE_BIN parent data. The BIN choice is witnessed by an
additional genuine common neighbor of w and b besides a; no defect entry
or complete defect row is assumed. -/
structure D0EdgeBinTemplate (G : SimpleGraph V) (r i j k b d w a : V) : Prop where
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
  edge_wa : G.Adj w a
  root_independent : ∀ x y, G.Adj r x → G.Adj r y → ¬ G.Adj x y
  w_parents : ∀ x, G.Adj r x → (G.Adj x w ↔ x = i ∨ x = j ∨ x = k)
  a_parents : ∀ x, G.Adj r x → (G.Adj x a ↔ x = b ∨ x = d)
  bin_common_neighbor : ∃ t, t ≠ a ∧ G.Adj w t ∧ G.Adj b t
  ordinary_parent_unique : ∀ y, y ≠ r → ¬ G.Adj r y → y ≠ w → y ≠ a →
    ∀ x x', G.Adj r x → G.Adj r x' → G.Adj x y → G.Adj x' y → x = x'

/-- The fixed unit-repeat BIN choice has the actual adjacency witness used
in the template. Thus the graph-only predicate does not impose a stronger
local branch condition than B[w,b]=1. -/
theorem bin_common_neighbor_of_unit_repeat (G : SimpleGraph V) {w b a : V}
    (hwb : w ≠ b) (hn : ¬ G.Adj w b) (hb : defectMatrix G w b = 1) :
    ∃ t, t ≠ a ∧ G.Adj w t ∧ G.Adj b t := by
  have hc : commonNeighborCount G w b = 2 := by
    have hh := defect_off_diagonal G hwb
    simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hn] at hh
    omega
  have hlt : ({a} : Finset V).card < ((G.neighborFinset w).filter (fun t => G.Adj t b)).card := by
    change ({a} : Finset V).card < commonNeighborCount G w b
    simp [hc]
  obtain ⟨t,ht,hta⟩ := Finset.exists_mem_notMem_of_card_lt_card hlt
  have ht' : G.Adj w t ∧ G.Adj t b := by simpa using ht
  exact ⟨t,by simpa using hta,ht'.1,ht'.2.symm⟩

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


/-- The actual root and w rows are forced by common-neighbor multiplicity
and the original row sum three. -/
theorem n62_d0_bin_root_rows (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k b d w a : V}
    (h : D0EdgeBinTemplate G r i j k b d w a) :
    twoOneRow G r w a ∧ twoOneRow G w r b := by
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
    h.edge_wa.ne hrw (by omega)
  have hbw : ¬ G.Adj b w := by
    rw [h.w_parents b h.root_b]
    simp [h.i_ne_b.symm,h.j_ne_b.symm,h.k_ne_b.symm]
  have hwbNe : w ≠ b := by rintro rfl; exact h.root_w_nonadj h.root_b
  obtain ⟨t,hta,hwt,hbt⟩ := h.bin_common_neighbor
  have hwb := defect_positive_of_two_common_neighbors G hwbNe hta.symm
    (fun hh => hbw hh.symm) h.edge_wa hba.symm hwt hbt.symm
  have hwr : 2 ≤ defectMatrix G w r := by rw [(defect_symmetric G).apply r w]; exact hrw
  have hW : twoOneRow G w r b := row_two_one_of_lower (defectMatrix G w) (h0 w) (hsum w)
    h.root_b.ne hwr (by omega)
  exact ⟨hR,hW⟩

private theorem bin_parent_common_set (G : SimpleGraph V) {r i j k b d w a x : V}
    (h : D0EdgeBinTemplate G r i j k b d w a) (hrx : G.Adj r x) (hix : i ≠ x) :
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
theorem n62_d0_bin_parent_repeat_profile (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k b d w a : V}
    (h : D0EdgeBinTemplate G r i j k b d w a) :
    ∀ x, G.Adj r x → defectMatrix G i x =
      (if x = j then 1 else 0) + (if x = k then 1 else 0) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  intro x hrx
  by_cases hxi : x = i
  · subst x
    simp [defect_diagonal G hreg,h.i_ne_j,h.i_ne_k]
  have hc := bin_parent_common_set G h hrx (Ne.symm hxi)
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


/-- The third actual repeat of i lies outside the closed root neighborhood
and differs from w. Its row is derived from the complete root-parent profile. -/
theorem n62_d0_bin_third_repeat (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k b d w a : V}
    (h : D0EdgeBinTemplate G r i j k b d w a) :
    ∃ c, c ≠ r ∧ ¬ G.Adj r c ∧ c ≠ w ∧ threeUnitRow G i j k c := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsum : ∑ x, defectMatrix G i x = 3 := by
    simpa [hcard] using defect_row_sum G hreg i
  have hp := n62_d0_bin_parent_repeat_profile G hdeg hdiam hcard h
  have hij : defectMatrix G i j = 1 := by simpa [h.j_ne_k] using hp j h.root_j
  have hik : defectMatrix G i k = 1 := by simpa [h.j_ne_k.symm] using hp k h.root_k
  obtain ⟨c,hcj,hck,hI⟩ := row_third_from_two (defectMatrix G i)
    (defect_nonnegative G hreg hdiam i) hsum h.j_ne_k hij hik
  have hic : defectMatrix G i c = 1 := by simp [hI,hcj,hck]
  obtain ⟨hR,hW⟩ := n62_d0_bin_root_rows G hdeg hdiam hcard h
  unfold twoOneRow at hR hW
  have hiw : i ≠ w := by rintro rfl; exact h.root_w_nonadj h.root_i
  have hia : i ≠ a := by rintro rfl; exact h.root_a_nonadj h.root_i
  have hir : defectMatrix G i r = 0 := by
    rw [(defect_symmetric G).apply r i]
    simp [hR,hiw,hia]
  have hiw0 : defectMatrix G i w = 0 := by
    rw [(defect_symmetric G).apply w i]
    simp [hW,h.root_i.ne',h.i_ne_b]
  have hcr : c ≠ r := by intro hh; rw [hh] at hic; omega
  have hcw : c ≠ w := by intro hh; rw [hh] at hic; omega
  have hrc : ¬ G.Adj r c := by
    intro hh
    have hc0 := hp c hh
    simp [hcj,hck] at hc0
    omega
  exact ⟨c,hcr,hrc,hcw,hI⟩

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

/-- Original-graph D0_EDGE_BIN exclusion from actual parent data and a
genuine additional common-neighbor witness. Every complete repeat row is
derived; no matrix or capacity certificate is accepted by this caller. -/
theorem no_n62_d0_edge_bin_template (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k b d w a : V}
    (h : D0EdgeBinTemplate G r i j k b d w a) : False := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain ⟨hR,hW⟩ := n62_d0_bin_root_rows G hdeg hdiam hcard h
  obtain ⟨c,hcr,hrc,_,hI⟩ := n62_d0_bin_third_repeat G hdeg hdiam hcard h
  have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
  have hjw : G.Adj j w := (h.w_parents j h.root_j).mpr (by simp)
  have hkw : G.Adj k w := (h.w_parents k h.root_k).mpr (by simp)
  have hba : G.Adj b a := (h.a_parents b h.root_b).mpr (by simp)
  have hbi : ¬ G.Adj b i := h.root_independent b i h.root_b h.root_i
  have hic : defectMatrix G i c = 1 := by
    have hcj : c ≠ j := by rintro rfl; exact hrc h.root_j
    have hck : c ≠ k := by rintro rfl; exact hrc h.root_k
    simp [threeUnitRow] at hI
    simp [hI,hcj,hck]
  have hcw : ¬ G.Adj c w := by
    intro hcwa
    have hh := adjacency_defect_transpose_entry G i w
    rw [adjacency_defect_commute G hreg,three_unit_row_mul G hI,
      two_one_row_mul_adjacency G hW] at hh
    simp [adjacencyMatrix,hjw,hkw,hcwa,h.root_i,hbi] at hh
  have hwc : ¬ G.Adj w c := fun hh => hcw hh.symm
  have hac : G.Adj a c := by
    have hl := defect_neighbor_le_commuted G hreg hdiam h.root_i (y := c)
    rw [two_one_row_mul_adjacency G hR] at hl
    by_contra hn
    simp [hic,adjacencyMatrix,hwc,hn] at hl
  have hbc : G.Adj b c := by
    have hl := defect_neighbor_le_commuted G hreg hdiam hiw.symm (y := c)
    rw [two_one_row_mul_adjacency G hW] at hl
    by_contra hn
    simp [hic,adjacencyMatrix,hrc,hn] at hl
  have hbcPos := defect_incident_triangle_ge_one G hbc hba hac
  have hl := two_neighbors_le_commuted G hreg hdiam h.i_ne_b h.root_i h.root_b (y := c)
  rw [two_one_row_mul_adjacency G hR] at hl
  simp [hic,adjacencyMatrix,hwc,hac] at hl
  omega

end
end DegreeDiameter
