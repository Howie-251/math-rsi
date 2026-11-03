import DegreeDiameter.N59Capacity

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Actual S_TOUCH adjacency/parent data. No defect row, matrix equation,
capacity inequality, or contradiction is assumed in this predicate. -/
structure STouchTemplate (G : SimpleGraph V) (r a b c w : V) : Prop where
  root_a : G.Adj r a
  root_b : G.Adj r b
  root_c : G.Adj r c
  edge_ab : G.Adj a b
  a_ne_c : a ≠ c
  b_ne_c : b ≠ c
  w_ne_root : w ≠ r
  root_w_nonadj : ¬ G.Adj r w
  within_root : ∀ x y, G.Adj r x → G.Adj r y →
    (G.Adj x y ↔ (x = a ∧ y = b) ∨ (x = b ∧ y = a))
  exceptional_parents : ∀ x, G.Adj r x → (G.Adj x w ↔ x = a ∨ x = c)
  ordinary_parent_unique : ∀ y, y ≠ r → ¬ G.Adj r y → y ≠ w →
    ∀ x x', G.Adj r x → G.Adj r x' → G.Adj x y → G.Adj x' y → x = x'

/-- A full actual row with three unit entries. -/
def threeUnitRow (G : SimpleGraph V) (v a b c : V) : Prop :=
  ∀ x, defectMatrix G v x = (if x = a then 1 else 0) +
    (if x = b then 1 else 0) + (if x = c then 1 else 0)

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

private theorem row_third_exists (f : V → ℤ) (h0 : ∀ x, 0 ≤ f x)
    (hs : ∑ x, f x = 3) {a b : V} (hab : a ≠ b) (ha : f a = 1) (hb : f b = 1) :
    ∃ c, c ≠ a ∧ c ≠ b ∧ 1 ≤ f c := by
  have h1 := Finset.sum_erase_add (s := Finset.univ) f (Finset.mem_univ a)
  have h2 := Finset.sum_erase_add (s := Finset.univ.erase a) f (by simp [Ne.symm hab] : b ∈ Finset.univ.erase a)
  have hpos : 0 < ∑ x ∈ (Finset.univ.erase a).erase b, f x := by omega
  obtain ⟨c, hc, hfc⟩ := (Finset.sum_pos_iff_of_nonneg (fun x _ => h0 x)).mp hpos
  have hca : c ≠ a := (Finset.mem_erase.mp (Finset.mem_erase.mp hc).2).1
  exact ⟨c, hca, (Finset.mem_erase.mp hc).1, by omega⟩

private theorem common_count_ge_two (G : SimpleGraph V) {x y u v : V} (huv : u ≠ v)
    (hxu : G.Adj x u) (huy : G.Adj u y) (hxv : G.Adj x v) (hvy : G.Adj v y) :
    2 ≤ commonNeighborCount G x y := by
  have hs : ({u, v} : Finset V) ⊆ (G.neighborFinset x).filter (fun z => G.Adj z y) := by
    intro z hz
    simp only [Finset.mem_insert, Finset.mem_singleton] at hz
    rcases hz with rfl | rfl <;> simp [hxu, huy, hxv, hvy]
  simpa [commonNeighborCount, huv] using Finset.card_le_card hs

private theorem edge_defect_ge_two (G : SimpleGraph V) {x y u v : V}
    (hxy : G.Adj x y) (huv : u ≠ v)
    (hxu : G.Adj x u) (huy : G.Adj u y) (hxv : G.Adj x v) (hvy : G.Adj v y) :
    2 ≤ defectMatrix G x y := by
  have hc := common_count_ge_two G huv hxu huy hxv hvy
  rw [defect_off_diagonal G hxy.ne]
  simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_pos hxy]
  omega

/-- With a triangle already present, the third point of a saturated repeat row
cannot be an actual neighbor. -/
theorem three_unit_triangle_row_third_nonadj (G : SimpleGraph V) {r a b t : V}
    (hra : G.Adj r a) (hrb : G.Adj r b) (hab : G.Adj a b)
    (htr : t ≠ r) (hta : t ≠ a) (hr : threeUnitRow G b r a t) : ¬ G.Adj b t := by
  unfold threeUnitRow at hr
  intro hbt
  have hbt1 : defectMatrix G b t = 1 := by simp [hr, htr, hta]
  have hbr1 : defectMatrix G b r = 1 := by simp [hr, hra.ne, Ne.symm htr]
  have hba1 : defectMatrix G b a = 1 := by simp [hr, hra.ne', Ne.symm hta]
  have hcnt : 0 < commonNeighborCount G b t := by
    have hh := defect_off_diagonal G hbt.ne
    simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_pos hbt] at hh
    omega
  obtain ⟨u, hu⟩ := Finset.card_pos.mp hcnt
  have hu' : G.Adj b u ∧ G.Adj u t := by simpa using hu
  have hbu := defect_incident_triangle_ge_one G hu'.1 hbt hu'.2.symm
  have huCases : u = r ∨ u = a ∨ u = t := by
    by_contra hn
    push_neg at hn
    simp [hr, hn.1, hn.2.1, hn.2.2] at hbu
  rcases huCases with rfl | rfl | rfl
  · have hh := edge_defect_ge_two G hrb.symm hta.symm hab.symm hra.symm hbt hu'.2.symm
    omega
  · have hh := edge_defect_ge_two G hab.symm htr.symm hrb.symm hra hbt hu'.2.symm
    omega
  · exact G.irrefl hu'.2

/-- The parent structure itself forces the b,c defect entry to vanish. -/
theorem stouch_b_c_defect_zero (G : SimpleGraph V) {r a b c w : V}
    (h : STouchTemplate G r a b c w) : defectMatrix G b c = 0 := by
  have hab : a ≠ b := h.edge_ab.ne
  have hac : ¬ G.Adj a c := by
    rw [h.within_root a c h.root_a h.root_c]
    simp [hab, Ne.symm h.b_ne_c, Ne.symm h.a_ne_c]
  have hbc : ¬ G.Adj b c := by
    rw [h.within_root b c h.root_b h.root_c]
    simp [Ne.symm hab, Ne.symm h.a_ne_c]
  have heq : (G.neighborFinset b).filter (fun y => G.Adj y c) = {r} := by
    ext y
    constructor
    · intro hy
      have hy' : G.Adj b y ∧ G.Adj y c := by simpa using hy
      by_cases hyr : y = r
      · simp [hyr]
      exfalso
      by_cases hry : G.Adj r y
      · have hby := (h.within_root b y h.root_b hry).mp hy'.1
        have hya : y = a := by rcases hby with hh | hh; exact False.elim (hab hh.1.symm); exact hh.2
        subst y
        exact hac hy'.2
      · by_cases hyw : y = w
        · subst y
          have hp := (h.exceptional_parents b h.root_b).mp hy'.1
          exact hp.elim (fun hh => hab hh.symm) h.b_ne_c
        · exact h.b_ne_c (h.ordinary_parent_unique y hyr hry hyw b c h.root_b h.root_c hy'.1 hy'.2.symm)
    · intro hy
      have hyr : y = r := by simpa using hy
      subst y
      simp [h.root_b.symm, h.root_c]
  have hc : commonNeighborCount G b c = 1 := by simp [commonNeighborCount, heq]
  rw [defect_off_diagonal G h.b_ne_c, hc]
  simp [adjacencyMatrix, hbc]

private theorem three_row_mul (G : SimpleGraph V) {v a b c y : V}
    (hr : threeUnitRow G v a b c) :
    (defectMatrix G * adjacencyMatrix G) v y =
      adjacencyMatrix G a y + adjacencyMatrix G b y + adjacencyMatrix G c y := by
  unfold threeUnitRow at hr
  rw [Matrix.mul_apply]
  simp_rw [hr, add_mul, ite_mul]
  simp [Finset.sum_add_distrib]

private theorem adjacency_nonnegative (G : SimpleGraph V) (x y : V) :
    0 ≤ adjacencyMatrix G x y := by
  simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply]
  split_ifs <;> omega

private theorem three_row_one_lower (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    {v a b c x y : V} (hr : threeUnitRow G v a b c) (hvx : G.Adj v x) :
    defectMatrix G x y ≤ adjacencyMatrix G a y + adjacencyMatrix G b y + adjacencyMatrix G c y := by
  have hh := Finset.single_le_sum
    (fun z _ => mul_nonneg (adjacency_nonnegative G v z) (defect_nonnegative G hreg hdiam z y))
    (Finset.mem_univ x)
  have hl : defectMatrix G x y ≤ (adjacencyMatrix G * defectMatrix G) v y := by
    simpa [Matrix.mul_apply, adjacencyMatrix, hvx] using hh
  rw [adjacency_defect_commute G hreg, three_row_mul G hr] at hl
  exact hl

private theorem three_row_two_lower (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    {v a b c x z y : V} (hr : threeUnitRow G v a b c)
    (hxz : x ≠ z) (hvx : G.Adj v x) (hvz : G.Adj v z) :
    defectMatrix G x y + defectMatrix G z y ≤
      adjacencyMatrix G a y + adjacencyMatrix G b y + adjacencyMatrix G c y := by
  have hh := Finset.sum_le_sum_of_subset_of_nonneg
    (Finset.subset_univ ({x, z} : Finset V))
    (fun u _ _ => mul_nonneg (adjacency_nonnegative G v u) (defect_nonnegative G hreg hdiam u y))
  have hl : defectMatrix G x y + defectMatrix G z y ≤
      (adjacencyMatrix G * defectMatrix G) v y := by
    simpa [Matrix.mul_apply, adjacencyMatrix, hvx, hvz, hxz] using hh
  rw [adjacency_defect_commute G hreg, three_row_mul G hr] at hl
  exact hl

/-- New S_TOUCH exclusion from an actual original order-62 graph and explicit
local adjacency/parent data. All three saturated defect rows are derived.
No global simplicity hypothesis on B is required. -/
theorem no_n62_stouch_template (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r a b c w : V}
    (h : STouchTemplate G r a b c w) : False := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsum (v : V) : ∑ x, defectMatrix G v x = 3 := by
    simpa [hcard] using defect_row_sum G hreg v
  have hnonneg := defect_nonnegative G hreg hdiam
  have hab : a ≠ b := h.edge_ab.ne
  have haw : a ≠ w := by rintro rfl; exact h.root_w_nonadj h.root_a
  have hbw : b ≠ w := by rintro rfl; exact h.root_w_nonadj h.root_b
  have hawAdj : G.Adj a w := (h.exceptional_parents a h.root_a).mpr (Or.inl rfl)
  have hcwAdj : G.Adj c w := (h.exceptional_parents c h.root_c).mpr (Or.inr rfl)
  have hbwNon : ¬ G.Adj b w := by
    intro hh
    exact ((h.exceptional_parents b h.root_b).mp hh).elim (fun hh => hab hh.symm) h.b_ne_c
  have hacNon : ¬ G.Adj a c := by
    rw [h.within_root a c h.root_a h.root_c]
    simp [hab, Ne.symm h.b_ne_c]
  have hraPos := defect_incident_triangle_ge_one G h.root_a h.root_b h.edge_ab.symm
  have hrbPos := defect_incident_triangle_ge_one G h.root_b h.root_a h.edge_ab
  have hrwPos : 1 ≤ defectMatrix G r w := by
    have := defect_positive_of_two_common_neighbors G h.w_ne_root.symm h.a_ne_c
      h.root_w_nonadj h.root_a hawAdj h.root_c hcwAdj
    omega
  have hR : threeUnitRow G r a b w :=
    row_three_of_positive (defectMatrix G r) (hnonneg r) (hsum r) hab haw hbw hraPos hrbPos hrwPos
  unfold threeUnitRow at hR
  have har1 : defectMatrix G a r = 1 := by
    rw [(defect_symmetric G).apply r a]
    simp [hR, hab, haw]
  have habPos := defect_incident_triangle_ge_one G h.edge_ab h.root_a.symm h.root_b
  have hacPos : 1 ≤ defectMatrix G a c := by
    have := defect_positive_of_two_common_neighbors G h.a_ne_c h.w_ne_root.symm hacNon
      h.root_a.symm h.root_c hawAdj hcwAdj.symm
    omega
  have hA : threeUnitRow G a r b c :=
    row_three_of_positive (defectMatrix G a) (hnonneg a) (hsum a)
      h.root_b.ne h.root_c.ne h.b_ne_c (by omega) habPos hacPos
  unfold threeUnitRow at hA
  have hbr1 : defectMatrix G b r = 1 := by
    rw [(defect_symmetric G).apply r b]
    simp [hR, Ne.symm hab, hbw]
  have hba1 : defectMatrix G b a = 1 := by
    rw [(defect_symmetric G).apply a b]
    simp [hA, h.root_b.ne', h.b_ne_c]
  obtain ⟨t, htr, hta, hbtPos⟩ := row_third_exists (defectMatrix G b) (hnonneg b)
    (hsum b) h.root_a.ne hbr1 hba1
  have hB : threeUnitRow G b r a t :=
    row_three_of_positive (defectMatrix G b) (hnonneg b) (hsum b)
      h.root_a.ne htr.symm hta.symm (by omega) (by omega) hbtPos
  unfold threeUnitRow at hB
  have hbt1 : defectMatrix G b t = 1 := by simp [hB, htr, hta]
  have htb : t ≠ b := by
    intro ht
    subst t
    rw [defect_diagonal G hreg] at hbt1
    omega
  have hbtNon := three_unit_triangle_row_third_nonadj G h.root_a h.root_b h.edge_ab htr hta hB
  have hrtNon : ¬ G.Adj r t := by
    intro hrt
    have hatNon : ¬ G.Adj a t := by
      rw [h.within_root a t h.root_a hrt]
      simp [hab, htb]
    have hl := three_row_one_lower G hreg hdiam hR h.root_b (y := t)
    have hwt : G.Adj w t := by
      by_contra hwt
      simp [hbt1, adjacencyMatrix, hatNon, hbtNon, hwt] at hl
    have htCases := (h.exceptional_parents t hrt).mp hwt.symm
    have htc : t = c := htCases.resolve_left hta
    have hbc0 := stouch_b_c_defect_zero G h
    rw [htc] at hbt1
    omega
  have htw : t ≠ w := by
    intro htw
    subst t
    have hrw1 : defectMatrix G r w = 1 := by simp [hR, Ne.symm haw, Ne.symm hbw]
    have hl := three_row_two_lower G hreg hdiam hA h.root_b.ne h.root_a.symm h.edge_ab (y := w)
    simp [hrw1, hbt1, adjacencyMatrix, h.root_w_nonadj, hbwNon, hcwAdj] at hl
  have hct : G.Adj c t := by
    have hl := three_row_one_lower G hreg hdiam hA h.edge_ab (y := t)
    by_contra hct
    simp [hbt1, adjacencyMatrix, hrtNon, hbtNon, hct] at hl
  have hatNon : ¬ G.Adj a t := by
    intro hat
    exact h.a_ne_c (h.ordinary_parent_unique t htr hrtNon htw a c h.root_a h.root_c hat hct)
  have hwt : G.Adj w t := by
    have hl := three_row_one_lower G hreg hdiam hR h.root_b (y := t)
    by_contra hwt
    simp [hbt1, adjacencyMatrix, hatNon, hbtNon, hwt] at hl
  have hctPos := defect_incident_triangle_ge_one G hct hcwAdj hwt
  have hl := three_row_two_lower G hreg hdiam hR h.b_ne_c h.root_b h.root_c (y := t)
  simp only [hbt1, adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_neg hatNon,
    if_neg hbtNon, if_pos hwt] at hl
  omega

end
end DegreeDiameter
