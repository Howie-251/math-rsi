import DegreeDiameter.N62TriangleMate

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Actual D2_MATCH root adjacency and parent sets. Every field concerns
vertices and adjacency; no defect row or capacity certificate is assumed. -/
structure D2MatchTemplate (G : SimpleGraph V) (r i j k w a : V) : Prop where
  root_i : G.Adj r i
  root_j : G.Adj r j
  root_k : G.Adj r k
  i_ne_j : i ≠ j
  i_ne_k : i ≠ k
  j_ne_k : j ≠ k
  w_ne_root : w ≠ r
  a_ne_root : a ≠ r
  w_ne_a : w ≠ a
  root_w_nonadj : ¬ G.Adj r w
  root_a_nonadj : ¬ G.Adj r a
  w_a_nonadj : ¬ G.Adj w a
  root_independent : ∀ x y, G.Adj r x → G.Adj r y → ¬ G.Adj x y
  w_parents : ∀ x, G.Adj r x → (G.Adj x w ↔ x = i ∨ x = j ∨ x = k)
  a_parents : ∀ x, G.Adj r x → (G.Adj x a ↔ x = i ∨ x = j)
  ordinary_parent_unique : ∀ y, y ≠ r → ¬ G.Adj r y → y ≠ w → y ≠ a →
    ∀ x x', G.Adj r x → G.Adj r x' → G.Adj x y → G.Adj x' y → x = x'

/-- Exact actual defect row with a double and a unit entry. -/
def twoOneRow (G : SimpleGraph V) (v a b : V) : Prop :=
  ∀ x, defectMatrix G v x = 2 * (if x = a then 1 else 0) + (if x = b then 1 else 0)

/-- The actual ordinary singleton-parent class at the specified root neighbor. -/
def d2Class (G : SimpleGraph V) (r w a i : V) : Finset V :=
  Finset.univ.filter (fun x => x ≠ r ∧ ¬ G.Adj r x ∧ x ≠ w ∧ x ≠ a ∧ G.Adj i x)

@[simp] theorem mem_d2Class (G : SimpleGraph V) (r w a i x : V) :
    x ∈ d2Class G r w a i ↔ x ≠ r ∧ ¬ G.Adj r x ∧ x ≠ w ∧ x ≠ a ∧ G.Adj i x := by
  simp [d2Class]

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

/-- Four saturated rows derived solely from the actual D2 parent structure. -/
theorem n62_d2_four_rows (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) :
    twoOneRow G r w a ∧ twoOneRow G i j k ∧ twoOneRow G j i k ∧ twoOneRow G w r a := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsum (v : V) : ∑ x, defectMatrix G v x = 3 := by
    simpa [hcard] using defect_row_sum G hreg v
  have h0 := defect_nonnegative G hreg hdiam
  have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
  have hjw : G.Adj j w := (h.w_parents j h.root_j).mpr (by simp)
  have hkw : G.Adj k w := (h.w_parents k h.root_k).mpr (by simp)
  have hia : G.Adj i a := (h.a_parents i h.root_i).mpr (by simp)
  have hja : G.Adj j a := (h.a_parents j h.root_j).mpr (by simp)
  have hrw := double_of_three_common G h.w_ne_root.symm h.root_w_nonadj
    h.i_ne_j h.i_ne_k h.j_ne_k h.root_i hiw h.root_j hjw h.root_k hkw
  have hra := defect_positive_of_two_common_neighbors G h.a_ne_root.symm h.i_ne_j
    h.root_a_nonadj h.root_i hia h.root_j hja
  have hR : twoOneRow G r w a := row_two_one_of_lower (defectMatrix G r) (h0 r) (hsum r)
    h.w_ne_a hrw (by omega)
  have hij := double_of_three_common G h.i_ne_j
    (h.root_independent i j h.root_i h.root_j) h.w_ne_root.symm h.a_ne_root.symm h.w_ne_a
    h.root_i.symm h.root_j hiw hjw.symm hia hja.symm
  have hik := defect_positive_of_two_common_neighbors G h.i_ne_k h.w_ne_root.symm
    (h.root_independent i k h.root_i h.root_k) h.root_i.symm h.root_k hiw hkw.symm
  have hjk := defect_positive_of_two_common_neighbors G h.j_ne_k h.w_ne_root.symm
    (h.root_independent j k h.root_j h.root_k) h.root_j.symm h.root_k hjw hkw.symm
  have hI : twoOneRow G i j k := row_two_one_of_lower (defectMatrix G i) (h0 i) (hsum i)
    h.j_ne_k hij (by omega)
  have hji : 2 ≤ defectMatrix G j i := by rw [(defect_symmetric G).apply i j]; exact hij
  have hJ : twoOneRow G j i k := row_two_one_of_lower (defectMatrix G j) (h0 j) (hsum j)
    h.i_ne_k hji (by omega)
  have hwa := defect_positive_of_two_common_neighbors G h.w_ne_a h.i_ne_j h.w_a_nonadj
    hiw.symm hia hjw.symm hja
  have hwr : 2 ≤ defectMatrix G w r := by rw [(defect_symmetric G).apply r w]; exact hrw
  have hW : twoOneRow G w r a := row_two_one_of_lower (defectMatrix G w) (h0 w) (hsum w)
    h.a_ne_root.symm hwr (by omega)
  exact ⟨hR,hI,hJ,hW⟩

/-- Two distinct positive repeat entries at nonneighbors already rule out
an actual triangle at a vertex of an original order-62 graph. -/
theorem n62_two_nonadj_repeats_zero_triangle (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {v a b : V} (hab : a ≠ b)
    (hna : ¬ G.Adj v a) (hnb : ¬ G.Adj v b)
    (hpa : 0 < defectMatrix G v a) (hpb : 0 < defectMatrix G v b) : zeroTriangleVertex G v := by
  intro x y hvx hvy hxy
  obtain ⟨w,_,_,_,_,hrow⟩ := n62_triangle_third_mate G hdeg hdiam hcard hvx hvy hxy
  have haw : a = w := by
    by_contra hn
    have hax : a ≠ x := by rintro rfl; exact hna hvx
    have hay : a ≠ y := by rintro rfl; exact hna hvy
    simp [threeUnitRow] at hrow
    simp [hrow,hax,hay,hn] at hpa
  have hbw : b = w := by
    by_contra hn
    have hbx : b ≠ x := by rintro rfl; exact hnb hvx
    have hby : b ≠ y := by rintro rfl; exact hnb hvy
    simp [threeUnitRow] at hrow
    simp [hrow,hbx,hby,hn] at hpb
  exact hab (haw.trans hbw.symm)

/-- All five named nonroot vertices are triangle-free, derived from the
actual saturated rows. No even-triangle-budget certificate is needed. -/
theorem n62_d2_named_zero_triangles (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) :
    zeroTriangleVertex G i ∧ zeroTriangleVertex G j ∧ zeroTriangleVertex G k ∧
      zeroTriangleVertex G w ∧ zeroTriangleVertex G a := by
  obtain ⟨hR,hI,hJ,hW⟩ := n62_d2_four_rows G hdeg hdiam hcard h
  unfold twoOneRow at hR hI hJ hW
  have hi := n62_two_nonadj_repeats_zero_triangle G hdeg hdiam hcard h.j_ne_k
    (h.root_independent i j h.root_i h.root_j) (h.root_independent i k h.root_i h.root_k)
    (by simp [hI,h.j_ne_k]) (by simp [hI,h.j_ne_k.symm])
  have hj := n62_two_nonadj_repeats_zero_triangle G hdeg hdiam hcard h.i_ne_k
    (h.root_independent j i h.root_j h.root_i) (h.root_independent j k h.root_j h.root_k)
    (by simp [hJ,h.i_ne_k]) (by simp [hJ,h.i_ne_k.symm])
  have hki : 0 < defectMatrix G k i := by
    rw [(defect_symmetric G).apply i k]; simp [hI,h.j_ne_k.symm]
  have hkj : 0 < defectMatrix G k j := by
    rw [(defect_symmetric G).apply j k]; simp [hJ,h.i_ne_k.symm]
  have hk := n62_two_nonadj_repeats_zero_triangle G hdeg hdiam hcard h.i_ne_j
    (h.root_independent k i h.root_k h.root_i) (h.root_independent k j h.root_k h.root_j) hki hkj
  have hw := n62_two_nonadj_repeats_zero_triangle G hdeg hdiam hcard h.a_ne_root.symm
    (fun ha => h.root_w_nonadj ha.symm) h.w_a_nonadj
    (by simp [hW,h.a_ne_root.symm]) (by simp [hW,h.a_ne_root])
  have har : 0 < defectMatrix G a r := by
    rw [(defect_symmetric G).apply r a]; simp [hR,h.w_ne_a.symm]
  have haw : 0 < defectMatrix G a w := by
    rw [(defect_symmetric G).apply w a]; simp [hW,h.a_ne_root]
  have ha := n62_two_nonadj_repeats_zero_triangle G hdeg hdiam hcard h.w_ne_root.symm
    (fun ha => h.root_a_nonadj ha.symm) (fun ha => h.w_a_nonadj ha.symm) har haw
  exact ⟨hi,hj,hk,hw,ha⟩


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

/-- Multiplication by the actual adjacency matrix for a derived double-unit row. -/
theorem two_one_row_mul_adjacency (G : SimpleGraph V) {v a b y : V}
    (hr : twoOneRow G v a b) :
    (defectMatrix G * adjacencyMatrix G) v y =
      2 * adjacencyMatrix G a y + adjacencyMatrix G b y := by
  unfold twoOneRow at hr
  rw [Matrix.mul_apply]
  simp_rw [hr,add_mul,mul_assoc,ite_mul]
  simp [Finset.sum_add_distrib,Finset.mul_sum]

private theorem adjacency_nonneg (G : SimpleGraph V) (x y : V) :
    0 ≤ adjacencyMatrix G x y := by
  simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply]
  split_ifs <;> omega

/-- A genuine neighbor contributes its nonnegative defect entry to AB=BA. -/
theorem defect_neighbor_le_commuted (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    {v x y : V} (hvx : G.Adj v x) :
    defectMatrix G x y ≤ (defectMatrix G * adjacencyMatrix G) v y := by
  have hh := Finset.single_le_sum
    (fun z _ => mul_nonneg (adjacency_nonneg G v z) (defect_nonnegative G hreg hdiam z y))
    (Finset.mem_univ x)
  have hl : defectMatrix G x y ≤ (adjacencyMatrix G * defectMatrix G) v y := by
    simpa [Matrix.mul_apply,adjacencyMatrix,hvx] using hh
  rwa [adjacency_defect_commute G hreg] at hl

private theorem three_neighbors_le_commuted (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    {v x z t y : V} (hxz : x ≠ z) (hxt : x ≠ t) (hzt : z ≠ t)
    (hvx : G.Adj v x) (hvz : G.Adj v z) (hvt : G.Adj v t) :
    defectMatrix G x y + defectMatrix G z y + defectMatrix G t y ≤
      (defectMatrix G * adjacencyMatrix G) v y := by
  have hh := Finset.sum_le_sum_of_subset_of_nonneg
    (Finset.subset_univ ({x,z,t} : Finset V))
    (fun u _ _ => mul_nonneg (adjacency_nonneg G v u) (defect_nonnegative G hreg hdiam u y))
  have hl : defectMatrix G x y + defectMatrix G z y + defectMatrix G t y ≤
      (adjacencyMatrix G * defectMatrix G) v y := by
    simpa [Matrix.mul_apply,adjacencyMatrix,hvx,hvz,hvt,hxz,hxt,hzt,add_assoc] using hh
  rwa [adjacency_defect_commute G hreg] at hl

/-- The exceptional vertex a has exactly one further unit repeat, and it
is an actual ordinary child of k, with no original adjacency to a. -/
theorem n62_d2_third_repeat_in_class (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) :
    ∃ c ∈ d2Class G r w a k, threeUnitRow G a r w c ∧ ¬ G.Adj a c := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain ⟨hR,hI,hJ,hW⟩ := n62_d2_four_rows G hdeg hdiam hcard h
  have hsum : ∑ x, defectMatrix G a x = 3 := by
    simpa [hcard] using defect_row_sum G hreg a
  have hra : defectMatrix G r a = 1 := by simp [twoOneRow] at hR; simp [hR,h.w_ne_a.symm]
  have hwa : defectMatrix G w a = 1 := by simp [twoOneRow] at hW; simp [hW,h.a_ne_root]
  have har : defectMatrix G a r = 1 := by rw [(defect_symmetric G).apply r a]; exact hra
  have haw : defectMatrix G a w = 1 := by rw [(defect_symmetric G).apply w a]; exact hwa
  obtain ⟨c,hcr,hcw,hA⟩ := row_third_from_two (defectMatrix G a)
    (defect_nonnegative G hreg hdiam a) hsum h.w_ne_root.symm har haw
  have hac : defectMatrix G a c = 1 := by simp [hA,hcr,hcw]
  have hca : defectMatrix G c a = 1 := by rw [(defect_symmetric G).apply a c]; exact hac
  have hcaNe : c ≠ a := by intro hh; subst c; rw [defect_diagonal G hreg] at hac; omega
  have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
  have hjw : G.Adj j w := (h.w_parents j h.root_j).mpr (by simp)
  have hia : G.Adj i a := (h.a_parents i h.root_i).mpr (by simp)
  have hja : G.Adj j a := (h.a_parents j h.root_j).mpr (by simp)
  have hka : ¬ G.Adj k a := by
    rw [h.a_parents k h.root_k]
    simp [h.i_ne_k.symm,h.j_ne_k.symm]
  have hrc : ¬ G.Adj r c := by
    intro hh
    have hl := defect_neighbor_le_commuted G hreg hdiam hh (y := a)
    rw [two_one_row_mul_adjacency G hR] at hl
    simp [hca,adjacencyMatrix,h.w_a_nonadj] at hl
  have hic : ¬ G.Adj i c := by
    intro hh
    have hl := three_neighbors_le_commuted G hreg hdiam h.w_ne_root.symm hcr.symm hcw.symm
      h.root_i.symm hiw hh (y := a)
    rw [two_one_row_mul_adjacency G hI] at hl
    simp [hra,hwa,hca,adjacencyMatrix,hja,hka] at hl
  have hjc : ¬ G.Adj j c := by
    intro hh
    have hl := three_neighbors_le_commuted G hreg hdiam h.w_ne_root.symm hcr.symm hcw.symm
      h.root_j.symm hjw hh (y := a)
    rw [two_one_row_mul_adjacency G hJ] at hl
    simp [hra,hwa,hca,adjacencyMatrix,hia,hka] at hl
  have hkc : G.Adj k c := by
    have hl := defect_neighbor_le_commuted G hreg hdiam hia (y := c)
    rw [two_one_row_mul_adjacency G hI] at hl
    by_contra hn
    simp [hac,adjacencyMatrix,hjc,hn] at hl
  have hanc : ¬ G.Adj a c := by
    intro hh
    have hz := (n62_d2_named_zero_triangles G hdeg hdiam hcard h).2.2.2.2
    have hh0 := zero_vertex_edge_defect_zero G hz hh
    omega
  exact ⟨c,by simp [hcr,hrc,hcw,hcaNe,hkc],hA,hanc⟩

/-- The k-row has no repeats at any actual neighbor of i or j. -/
theorem n62_d2_k_repeat_zero_on_two_neighborhoods (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) :
    ∀ x, G.Adj i x ∨ G.Adj j x → defectMatrix G k x = 0 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain ⟨_,hI,hJ,_⟩ := n62_d2_four_rows G hdeg hdiam hcard h
  intro x hx
  have h0 := defect_nonnegative G hreg hdiam x k
  rw [(defect_symmetric G).apply x k]
  rcases hx with hx | hx
  · have hl := defect_neighbor_le_commuted G hreg hdiam hx (y := k)
    rw [two_one_row_mul_adjacency G hI] at hl
    have hjk := h.root_independent j k h.root_j h.root_k
    simp [adjacencyMatrix,hjk] at hl
    omega
  · have hl := defect_neighbor_le_commuted G hreg hdiam hx (y := k)
    rw [two_one_row_mul_adjacency G hJ] at hl
    have hik := h.root_independent i k h.root_i h.root_k
    simp [adjacencyMatrix,hik] at hl
    omega


private theorem d2_neighbor_three (G : SimpleGraph V) {r i j k w a u : V}
    (h : D2MatchTemplate G r i j k w a) (hru : G.Adj r u)
    (huw : G.Adj u w) (hua : G.Adj u a) :
    G.neighborFinset u = insert r (insert w (insert a (d2Class G r w a u))) := by
  ext x
  constructor
  · intro hx
    have hux : G.Adj u x := by simpa using hx
    by_cases hxr : x = r
    · simp [hxr]
    by_cases hxw : x = w
    · simp [hxw]
    by_cases hxa : x = a
    · simp [hxa]
    have hrx : ¬ G.Adj r x := fun hh => h.root_independent u x hru hh hux
    simp [hxr,hxw,hxa,hrx,hux]
  · intro hx
    simp only [Finset.mem_insert] at hx
    rcases hx with rfl | rfl | rfl | hx
    · simpa using hru.symm
    · simpa using huw
    · simpa using hua
    · simpa using ((mem_d2Class G r w a u x).mp hx).2.2.2.2

private theorem d2_neighbor_two (G : SimpleGraph V) {r i j k w a u : V}
    (h : D2MatchTemplate G r i j k w a) (hru : G.Adj r u)
    (huw : G.Adj u w) (hua : ¬ G.Adj u a) :
    G.neighborFinset u = insert r (insert w (d2Class G r w a u)) := by
  ext x
  constructor
  · intro hx
    have hux : G.Adj u x := by simpa using hx
    by_cases hxr : x = r
    · simp [hxr]
    by_cases hxw : x = w
    · simp [hxw]
    have hxa : x ≠ a := by rintro rfl; exact hua hux
    have hrx : ¬ G.Adj r x := fun hh => h.root_independent u x hru hh hux
    simp [hxr,hxw,hxa,hrx,hux]
  · intro hx
    simp only [Finset.mem_insert] at hx
    rcases hx with rfl | rfl | hx
    · simpa using hru.symm
    · simpa using huw
    · simpa using ((mem_d2Class G r w a u x).mp hx).2.2.2.2

/-- Exact actual neighbor decompositions for the three distinguished parents. -/
theorem d2_neighborhoods (G : SimpleGraph V) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) :
    G.neighborFinset i = insert r (insert w (insert a (d2Class G r w a i))) ∧
    G.neighborFinset j = insert r (insert w (insert a (d2Class G r w a j))) ∧
    G.neighborFinset k = insert r (insert w (d2Class G r w a k)) := by
  have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
  have hjw : G.Adj j w := (h.w_parents j h.root_j).mpr (by simp)
  have hkw : G.Adj k w := (h.w_parents k h.root_k).mpr (by simp)
  have hia : G.Adj i a := (h.a_parents i h.root_i).mpr (by simp)
  have hja : G.Adj j a := (h.a_parents j h.root_j).mpr (by simp)
  have hka : ¬ G.Adj k a := by
    rw [h.a_parents k h.root_k]
    simp [h.i_ne_k.symm,h.j_ne_k.symm]
  exact ⟨d2_neighbor_three G h h.root_i hiw hia,
    d2_neighbor_three G h h.root_j hjw hja,d2_neighbor_two G h h.root_k hkw hka⟩

/-- The actual singleton-parent classes have sizes five, five, and six. -/
theorem n62_d2_class_sizes (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) :
    (d2Class G r w a i).card = 5 ∧ (d2Class G r w a j).card = 5 ∧
      (d2Class G r w a k).card = 6 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain ⟨hi,hj,hk⟩ := d2_neighborhoods G h
  have hci : (G.neighborFinset i).card = 8 := hreg i
  have hcj : (G.neighborFinset j).card = 8 := hreg j
  have hck : (G.neighborFinset k).card = 8 := hreg k
  rw [hi] at hci
  rw [hj] at hcj
  rw [hk] at hck
  simp [h.w_ne_root.symm,h.a_ne_root.symm,h.w_ne_a] at hci hcj hck
  exact ⟨by omega,by omega,by omega⟩

/-- Ordinary actual parent classes are disjoint, from the explicit singleton
parent rule rather than an assumed partition. -/
theorem d2_classes_disjoint (G : SimpleGraph V) {r i j k w a u v : V}
    (h : D2MatchTemplate G r i j k w a) (hru : G.Adj r u) (hrv : G.Adj r v) (huv : u ≠ v) :
    Disjoint (d2Class G r w a u) (d2Class G r w a v) := by
  apply Finset.disjoint_left.mpr
  intro x hx hy
  have hx' := (mem_d2Class G r w a u x).mp hx
  have hy' := (mem_d2Class G r w a v x).mp hy
  exact huv (h.ordinary_parent_unique x hx'.1 hx'.2.1 hx'.2.2.1 hx'.2.2.2.1
    u v hru hrv hx'.2.2.2.2 hy'.2.2.2.2)

/-- The two exact class-sum commutation equations on which the remaining
D2 capacity argument operates; both use actual neighbor decompositions. -/
theorem n62_d2_class_commutation (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) :
    ∀ y, (defectMatrix G r y + defectMatrix G w y + defectMatrix G a y +
      ∑ x ∈ d2Class G r w a i, defectMatrix G x y =
      2 * adjacencyMatrix G j y + adjacencyMatrix G k y) ∧
    (defectMatrix G r y + defectMatrix G w y + defectMatrix G a y +
      ∑ x ∈ d2Class G r w a j, defectMatrix G x y =
      2 * adjacencyMatrix G i y + adjacencyMatrix G k y) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain ⟨hi,hj,_⟩ := d2_neighborhoods G h
  obtain ⟨_,hI,hJ,_⟩ := n62_d2_four_rows G hdeg hdiam hcard h
  intro y
  have hleft (v : V) : (adjacencyMatrix G * defectMatrix G) v y =
      ∑ x ∈ G.neighborFinset v, defectMatrix G x y := by
    simp [adjacencyMatrix]
  have hci := congrArg (fun M : Matrix V V ℤ => M i y) (adjacency_defect_commute G hreg)
  have hcj := congrArg (fun M : Matrix V V ℤ => M j y) (adjacency_defect_commute G hreg)
  dsimp only at hci hcj
  rw [hleft,hi,two_one_row_mul_adjacency G hI] at hci
  rw [hleft,hj,two_one_row_mul_adjacency G hJ] at hcj
  simp [h.w_ne_root.symm,h.a_ne_root.symm,h.w_ne_a] at hci hcj
  constructor <;> linarith


/-- An actual ordinary class member has exactly its stated root parent. -/
theorem d2_class_parent (G : SimpleGraph V) {r i j k w a u v x : V}
    (h : D2MatchTemplate G r i j k w a) (hru : G.Adj r u) (hrv : G.Adj r v)
    (hx : x ∈ d2Class G r w a u) : G.Adj v x ↔ v = u := by
  have hx' := (mem_d2Class G r w a u x).mp hx
  constructor
  · intro hvx
    exact h.ordinary_parent_unique x hx'.1 hx'.2.1 hx'.2.2.1 hx'.2.2.2.1
      v u hrv hru hvx hx'.2.2.2.2
  · rintro rfl
    exact hx'.2.2.2.2

/-- Actual pointwise defect counts between the three singleton classes.
The c-row premise is supplied by n62_d2_third_repeat_in_class. -/
theorem n62_d2_class_repeat_weights (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a c : V}
    (h : D2MatchTemplate G r i j k w a) (hc : c ∈ d2Class G r w a k)
    (hA : threeUnitRow G a r w c) :
    (∀ x ∈ d2Class G r w a i, ∑ y ∈ d2Class G r w a j, defectMatrix G x y = 2) ∧
    (∀ y ∈ d2Class G r w a j, ∑ x ∈ d2Class G r w a i, defectMatrix G y x = 2) ∧
    (∀ q ∈ d2Class G r w a k,
      (∑ x ∈ d2Class G r w a i, defectMatrix G x q = 1 - (if q = c then 1 else 0)) ∧
      (∑ y ∈ d2Class G r w a j, defectMatrix G y q = 1 - (if q = c then 1 else 0))) := by
  obtain ⟨hR,_,_,hW⟩ := n62_d2_four_rows G hdeg hdiam hcard h
  unfold twoOneRow at hR hW
  unfold threeUnitRow at hA
  have hcomm := n62_d2_class_commutation G hdeg hdiam hcard h
  constructor
  · intro x hx
    have hx' := (mem_d2Class G r w a i x).mp hx
    have hxnc : x ≠ c := by
      rintro rfl
      exact Finset.disjoint_left.mp (d2_classes_disjoint G h h.root_i h.root_k h.i_ne_k) hx hc
    have hkx : ¬ G.Adj k x := by rw [d2_class_parent G h h.root_i h.root_k hx]; exact h.i_ne_k.symm
    have hh := (hcomm x).2
    simp [hR,hW,hA,hx'.1,hx'.2.2.1,hx'.2.2.2.1,hxnc,adjacencyMatrix,hx'.2.2.2.2,hkx] at hh
    simpa only [(defect_symmetric G).apply] using hh
  constructor
  · intro y hy
    have hy' := (mem_d2Class G r w a j y).mp hy
    have hync : y ≠ c := by
      rintro rfl
      exact Finset.disjoint_left.mp (d2_classes_disjoint G h h.root_j h.root_k h.j_ne_k) hy hc
    have hky : ¬ G.Adj k y := by rw [d2_class_parent G h h.root_j h.root_k hy]; exact h.j_ne_k.symm
    have hh := (hcomm y).1
    simp [hR,hW,hA,hy'.1,hy'.2.2.1,hy'.2.2.2.1,hync,adjacencyMatrix,hy'.2.2.2.2,hky] at hh
    simpa only [(defect_symmetric G).apply] using hh
  · intro q hq
    have hq' := (mem_d2Class G r w a k q).mp hq
    have hiq : ¬ G.Adj i q := by rw [d2_class_parent G h h.root_k h.root_i hq]; exact h.i_ne_k
    have hjq : ¬ G.Adj j q := by rw [d2_class_parent G h h.root_k h.root_j hq]; exact h.j_ne_k
    have hh := hcomm q
    simp [hR,hW,hA,hq'.1,hq'.2.2.1,hq'.2.2.2.1,adjacencyMatrix,hiq,hjq,hq'.2.2.2.2] at hh
    constructor <;> omega


private theorem class_capacity_saturated (f : V → V → ℤ) (X Y Z : Finset V)
    (h0 : ∀ x y, 0 ≤ f x y) (hrow : ∀ x, ∑ y, f x y = 3)
    (hd : Disjoint Y Z) (hY : ∀ x ∈ X, ∑ y ∈ Y, f x y = 2)
    (htot : ∑ x ∈ X, ∑ z ∈ Z, f x z = (X.card : ℤ)) :
    ∀ x ∈ X, (∑ z ∈ Z, f x z = 1) ∧ ∀ y, y ∉ Y ∪ Z → f x y = 0 := by
  have hcap (x : V) (hx : x ∈ X) : ∑ z ∈ Z, f x z ≤ 1 := by
    have hl := Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ (Y ∪ Z))
      (fun y _ _ => h0 x y)
    rw [Finset.sum_union hd,hY x hx,hrow x] at hl
    omega
  have hz : ∑ x ∈ X, (1 - ∑ z ∈ Z, f x z) = 0 := by
    rw [Finset.sum_sub_distrib,htot]
    simp
  intro x hx
  have hval := (Finset.sum_eq_zero_iff_of_nonneg (fun x hx => sub_nonneg.mpr (hcap x hx))).mp hz x hx
  have hZ : ∑ z ∈ Z, f x z = 1 := by omega
  refine ⟨hZ,?_⟩
  intro y hy
  have hfull : ∑ z ∈ Y ∪ Z, f x z = 3 := by
    rw [Finset.sum_union hd,hY x hx,hZ]
    norm_num
  have hl := Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ (insert y (Y ∪ Z)))
    (fun z _ _ => h0 x z)
  rw [Finset.sum_insert hy,hfull,hrow x] at hl
  have hh0 := h0 x y
  omega

/-- Every actual row in either five-point class spends two units on the
opposite class and exactly one on C3, and vanishes everywhere else. The
finite capacity equality is derived from the original graph and parent data. -/
theorem n62_d2_class_support (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) :
    (∀ x ∈ d2Class G r w a i,
      (∑ y ∈ d2Class G r w a j, defectMatrix G x y = 2) ∧
      (∑ q ∈ d2Class G r w a k, defectMatrix G x q = 1) ∧
      ∀ y, y ∉ d2Class G r w a j ∪ d2Class G r w a k → defectMatrix G x y = 0) ∧
    (∀ y ∈ d2Class G r w a j,
      (∑ x ∈ d2Class G r w a i, defectMatrix G y x = 2) ∧
      (∑ q ∈ d2Class G r w a k, defectMatrix G y q = 1) ∧
      ∀ x, x ∉ d2Class G r w a i ∪ d2Class G r w a k → defectMatrix G y x = 0) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsum (v : V) : ∑ x, defectMatrix G v x = 3 := by
    simpa [hcard] using defect_row_sum G hreg v
  obtain ⟨c,hc,hA,_⟩ := n62_d2_third_repeat_in_class G hdeg hdiam hcard h
  obtain ⟨hij,hji,hk⟩ := n62_d2_class_repeat_weights G hdeg hdiam hcard h hc hA
  obtain ⟨hci,hcj,hck⟩ := n62_d2_class_sizes G hdeg hdiam hcard h
  have htotI : ∑ x ∈ d2Class G r w a i, ∑ q ∈ d2Class G r w a k,
      defectMatrix G x q = ((d2Class G r w a i).card : ℤ) := by
    rw [Finset.sum_comm]
    calc
      _ = ∑ q ∈ d2Class G r w a k, (1 - (if q = c then 1 else 0) : ℤ) := by
        apply Finset.sum_congr rfl
        intro q hq
        exact (hk q hq).1
      _ = _ := by simp [Finset.sum_sub_distrib,hc,hci,hck]
  have htotJ : ∑ y ∈ d2Class G r w a j, ∑ q ∈ d2Class G r w a k,
      defectMatrix G y q = ((d2Class G r w a j).card : ℤ) := by
    rw [Finset.sum_comm]
    calc
      _ = ∑ q ∈ d2Class G r w a k, (1 - (if q = c then 1 else 0) : ℤ) := by
        apply Finset.sum_congr rfl
        intro q hq
        exact (hk q hq).2
      _ = _ := by simp [Finset.sum_sub_distrib,hc,hcj,hck]
  have hI := class_capacity_saturated (defectMatrix G)
    (d2Class G r w a i) (d2Class G r w a j) (d2Class G r w a k)
    (defect_nonnegative G hreg hdiam) hsum
    (d2_classes_disjoint G h h.root_j h.root_k h.j_ne_k) hij htotI
  have hJ := class_capacity_saturated (defectMatrix G)
    (d2Class G r w a j) (d2Class G r w a i) (d2Class G r w a k)
    (defect_nonnegative G hreg hdiam) hsum
    (d2_classes_disjoint G h h.root_i h.root_k h.i_ne_k) hji htotJ
  exact ⟨fun x hx => ⟨hij x hx,hI x hx⟩,fun y hy => ⟨hji y hy,hJ y hy⟩⟩


private theorem common_one_of_defect_zero (G : SimpleGraph V) {x y : V}
    (hxy : x ≠ y) (hn : ¬ G.Adj x y) (hb : defectMatrix G x y = 0) :
    commonNeighborCount G x y = 1 := by
  have hh := defect_off_diagonal G hxy
  simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hn] at hh
  omega

/-- Actual ordinary adjacency counts used by the D2 final counting step.
Each C1 vertex has exactly one neighbor in C2 and C3. Each C3 vertex obeys
the displayed one-common-neighbor equation for both five-point classes. -/
theorem n62_d2_class_neighbor_counts (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) :
    (∀ x ∈ d2Class G r w a i,
      ((d2Class G r w a j).filter (fun y => G.Adj y x)).card = 1 ∧
      ((d2Class G r w a k).filter (fun q => G.Adj q x)).card = 1) ∧
    (∀ q ∈ d2Class G r w a k,
      (if G.Adj a q then 1 else 0) + ((d2Class G r w a i).filter (fun x => G.Adj x q)).card = 1 ∧
      (if G.Adj a q then 1 else 0) + ((d2Class G r w a j).filter (fun y => G.Adj y q)).card = 1) := by
  obtain ⟨_,hI,hJ,_⟩ := n62_d2_four_rows G hdeg hdiam hcard h
  obtain ⟨hi,hj,hk⟩ := d2_neighborhoods G h
  obtain ⟨hzi,_,hzk,_,_⟩ := n62_d2_named_zero_triangles G hdeg hdiam hcard h
  have hiw : G.Adj i w := (h.w_parents i h.root_i).mpr (by simp)
  have hia : G.Adj i a := (h.a_parents i h.root_i).mpr (by simp)
  have hkw : G.Adj k w := (h.w_parents k h.root_k).mpr (by simp)
  unfold twoOneRow at hI hJ
  constructor
  · intro x hx
    have hx' := (mem_d2Class G r w a i x).mp hx
    have hxne (v : V) (hrv : G.Adj r v) : x ≠ v := by rintro rfl; exact hx'.2.1 hrv
    have hwx : ¬ G.Adj w x := hzi w x hiw hx'.2.2.2.2
    have hax : ¬ G.Adj a x := hzi a x hia hx'.2.2.2.2
    have hjx : ¬ G.Adj j x := by rw [d2_class_parent G h h.root_i h.root_j hx]; exact h.i_ne_j.symm
    have hkx : ¬ G.Adj k x := by rw [d2_class_parent G h h.root_i h.root_k hx]; exact h.i_ne_k.symm
    have hbJ : defectMatrix G j x = 0 := by simp [hJ,hxne i h.root_i,hxne k h.root_k]
    have hbK := n62_d2_k_repeat_zero_on_two_neighborhoods G hdeg hdiam hcard h x (Or.inl hx'.2.2.2.2)
    have hcJ := common_one_of_defect_zero G (hxne j h.root_j).symm hjx hbJ
    have hcK := common_one_of_defect_zero G (hxne k h.root_k).symm hkx hbK
    simp [commonNeighborCount,Finset.filter_insert,hj,hx'.2.1,hwx,hax] at hcJ
    simp [commonNeighborCount,Finset.filter_insert,hk,hx'.2.1,hwx] at hcK
    exact ⟨hcJ,hcK⟩
  · intro q hq
    have hq' := (mem_d2Class G r w a k q).mp hq
    have hqne (v : V) (hrv : G.Adj r v) : q ≠ v := by rintro rfl; exact hq'.2.1 hrv
    have hwq : ¬ G.Adj w q := hzk w q hkw hq'.2.2.2.2
    have hiq : ¬ G.Adj i q := by rw [d2_class_parent G h h.root_k h.root_i hq]; exact h.i_ne_k
    have hjq : ¬ G.Adj j q := by rw [d2_class_parent G h h.root_k h.root_j hq]; exact h.j_ne_k
    have hbI : defectMatrix G i q = 0 := by simp [hI,hqne j h.root_j,hqne k h.root_k]
    have hbJ : defectMatrix G j q = 0 := by simp [hJ,hqne i h.root_i,hqne k h.root_k]
    have hcI := common_one_of_defect_zero G (hqne i h.root_i).symm hiq hbI
    have hcJ := common_one_of_defect_zero G (hqne j h.root_j).symm hjq hbJ
    by_cases haq : G.Adj a q
    · simp [commonNeighborCount,Finset.filter_insert,hi,hq'.2.1,hwq,haq] at hcI
      simp [commonNeighborCount,Finset.filter_insert,hj,hq'.2.1,hwq,haq] at hcJ
      constructor <;> simp [haq] <;> omega
    · simp [commonNeighborCount,Finset.filter_insert,hi,hq'.2.1,hwq,haq] at hcI
      simp [commonNeighborCount,Finset.filter_insert,hj,hq'.2.1,hwq,haq] at hcJ
      exact ⟨by simpa [haq] using hcI,by simpa [haq] using hcJ⟩


private theorem sum_filter_card_swap {α β : Type*} (s : Finset α) (t : Finset β)
    (R : α → β → Prop) [∀ a b, Decidable (R a b)] :
    ∑ a ∈ s, (t.filter (R a)).card = ∑ b ∈ t, (s.filter (fun a => R a b)).card := by
  simp_rw [Finset.card_eq_sum_ones,Finset.sum_filter]
  rw [Finset.sum_comm]

/-- Original-graph exclusion of D2_MATCH. The template contains only actual
adjacency and parent data; all repeat rows, class capacities, and the final
commutation contradiction are derived from that graph. -/
theorem no_n62_d2_match_template (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : D2MatchTemplate G r i j k w a) : False := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain ⟨c,hc,hA,hanc⟩ := n62_d2_third_repeat_in_class G hdeg hdiam hcard h
  obtain ⟨hci,_,hck⟩ := n62_d2_class_sizes G hdeg hdiam hcard h
  obtain ⟨hxi,hqk⟩ := n62_d2_class_neighbor_counts G hdeg hdiam hcard h
  have hedges : ∑ q ∈ d2Class G r w a k,
      ((d2Class G r w a i).filter (fun x => G.Adj x q)).card = 5 := by
    rw [sum_filter_card_swap]
    calc
      _ = ∑ x ∈ d2Class G r w a i, 1 := by
        apply Finset.sum_congr rfl
        intro x hx
        simpa only [SimpleGraph.adj_comm] using (hxi x hx).2
      _ = 5 := by simp [hci]
  have hsum := Finset.sum_congr (s₁ := d2Class G r w a k) rfl (fun q hq => (hqk q hq).1)
  rw [Finset.sum_add_distrib,hedges] at hsum
  have hright : (∑ q ∈ d2Class G r w a k, (1 : ℕ)) = 6 := by simp [hck]
  rw [hright] at hsum
  have hapos : 0 < ∑ q ∈ d2Class G r w a k, (if G.Adj a q then 1 else 0 : ℕ) := by
    omega
  obtain ⟨d,hd,hda⟩ := (Finset.sum_pos_iff_of_nonneg (fun _ _ => Nat.zero_le _)).mp hapos
  have had : G.Adj a d := by by_contra hn; simp [hn] at hda
  have hdc : d ≠ c := by rintro rfl; exact hanc had
  have hdnI : ∀ x ∈ d2Class G r w a i, ¬ G.Adj x d := by
    have hh := (hqk d hd).1
    simp only [if_pos had] at hh
    have hzero : ((d2Class G r w a i).filter (fun x => G.Adj x d)).card = 0 := by omega
    intro x hx hxd
    have hempty := Finset.card_eq_zero.mp hzero
    have hm : x ∈ (d2Class G r w a i).filter (fun x => G.Adj x d) := by simp [hx,hxd]
    rw [hempty] at hm
    exact Finset.not_mem_empty x hm
  have hdnK : ∀ q ∈ d2Class G r w a k, ¬ G.Adj q d := by
    have hzk := (n62_d2_named_zero_triangles G hdeg hdiam hcard h).2.2.1
    intro q hq
    exact hzk q d ((mem_d2Class G r w a k q).mp hq).2.2.2.2
      ((mem_d2Class G r w a k d).mp hd).2.2.2.2
  have hcol := (n62_d2_class_repeat_weights G hdeg hdiam hcard h hc hA).2.2 d hd |>.1
  simp [hdc] at hcol
  have hpos : 0 < ∑ x ∈ d2Class G r w a i, defectMatrix G x d := by omega
  obtain ⟨x,hx,hxd⟩ := (Finset.sum_pos_iff_of_nonneg
    (fun x _ => defect_nonnegative G hreg hdiam x d)).mp hpos
  have hmatch := (hxi x hx).1
  have hmpos : 0 < ((d2Class G r w a j).filter (fun y => G.Adj y x)).card := by omega
  obtain ⟨y,hy⟩ := Finset.card_pos.mp hmpos
  have hy' := Finset.mem_filter.mp hy
  have hsupp := (n62_d2_class_support G hdeg hdiam hcard h).2 y hy'.1
  have hzero : (defectMatrix G * adjacencyMatrix G) y d = 0 := by
    rw [Matrix.mul_apply]
    apply Finset.sum_eq_zero
    intro z _
    by_cases hz : z ∈ d2Class G r w a i ∪ d2Class G r w a k
    · have hzn : ¬ G.Adj z d := by
        rcases Finset.mem_union.mp hz with hz | hz
        · exact hdnI z hz
        · exact hdnK z hz
      simp [adjacencyMatrix,hzn]
    · rw [hsupp.2.2 z hz]
      simp
  have hl := defect_neighbor_le_commuted G hreg hdiam hy'.2 (y := d)
  rw [hzero] at hl
  omega

end
end DegreeDiameter
