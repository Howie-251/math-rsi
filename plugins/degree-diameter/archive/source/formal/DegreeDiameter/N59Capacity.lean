import DegreeDiameter.N59ZeroCore

namespace DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Vertices outside the actual closed neighborhood. -/
def nonedgeVertices (G : SimpleGraph V) (n : V) : Finset V :=
  Finset.univ.filter (fun y => y ≠ n ∧ ¬ G.Adj n y)

/-- The actual defect budget outside a closed neighborhood. -/
def nonedgeDefectBudget (G : SimpleGraph V) (n : V) : ℤ :=
  ∑ y ∈ nonedgeVertices G n, defectMatrix G n y

/-- Genuine zero endpoints joined to n by a defect entry of weight two. -/
def heavyZeroRepeats (G : SimpleGraph V) (n : V) : Finset V :=
  Finset.univ.filter (fun y => zeroTriangleVertex G y ∧ defectMatrix G n y = 2)

/-- The indicator of two actual common zero neighbors. -/
def commonZeroPairIndicator (G : SimpleGraph V) (n y : V) : ℤ :=
  if (commonZeroNeighbors G n y).card = 2 then 1 else 0

@[simp] theorem mem_nonedgeVertices (G : SimpleGraph V) (n y : V) :
    y ∈ nonedgeVertices G n ↔ y ≠ n ∧ ¬ G.Adj n y := by simp [nonedgeVertices]

/-- An actual triangle contributes at least one to either incident defect entry. -/
theorem defect_incident_triangle_ge_one (G : SimpleGraph V) {n a b : V}
    (hna : G.Adj n a) (hnb : G.Adj n b) (hba : G.Adj b a) :
    1 ≤ defectMatrix G n a := by
  have hc : 0 < commonNeighborCount G n a := by
    apply Finset.card_pos.mpr
    exact ⟨b, by simp [hnb, hba]⟩
  rw [defect_off_diagonal G hna.ne]
  simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_pos hna]
  omega

/-- The actual row budget splits into graph edges and graph nonedges. -/
theorem n59_nonedges_add_neighbors (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hcard : Fintype.card V = 59) (n : V) :
    nonedgeDefectBudget G n + (∑ y ∈ G.neighborFinset n, defectMatrix G n y) = 6 := by
  have hrow : ∑ y, defectMatrix G n y = 6 := by simpa [hcard] using defect_row_sum G hreg n
  rw [← hrow]
  have hneigh : G.neighborFinset n = Finset.univ.filter (G.Adj n) := by ext y; simp
  rw [hneigh]
  unfold nonedgeDefectBudget nonedgeVertices
  rw [Finset.sum_filter, Finset.sum_filter, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro y _
  by_cases hy : y = n
  · subst y
    simp [defect_diagonal G hreg]
  · by_cases ha : G.Adj n y <;> simp [hy, ha]

/-- A nonzero-triangle root has at least two units of actual edge defect. -/
theorem nonzero_neighbor_defect_ge_two (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    {n : V} (hn : ¬ zeroTriangleVertex G n) :
    2 ≤ ∑ y ∈ G.neighborFinset n, defectMatrix G n y := by
  simp only [zeroTriangleVertex] at hn
  push_neg at hn
  obtain ⟨a, b, hna, hnb, hab⟩ := hn
  have hab' : a ≠ b := hab.ne
  have ha := defect_incident_triangle_ge_one G hna hnb hab.symm
  have hb := defect_incident_triangle_ge_one G hnb hna hab
  have hs : ({a, b} : Finset V) ⊆ G.neighborFinset n := by
    intro y hy
    simp only [Finset.mem_insert, Finset.mem_singleton] at hy
    rcases hy with rfl | rfl <;> simp [hna, hnb]
  have hle := Finset.sum_le_sum_of_subset_of_nonneg hs
    (fun y _ _ => defect_nonnegative G hreg hdiam n y)
  have habsum : ∑ y ∈ ({a, b} : Finset V), defectMatrix G n y =
      defectMatrix G n a + defectMatrix G n b := by simp [hab']
  rw [habsum] at hle
  omega

/-- Actual original order-59 hypotheses leave at most four nonedge-repeat
units at a vertex which belongs to a triangle. -/
theorem n59_nonzero_nonedge_budget_le_four (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 59) {n : V} (hn : ¬ zeroTriangleVertex G n) :
    nonedgeDefectBudget G n ≤ 4 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsplit := n59_nonedges_add_neighbors G hreg hcard n
  have hedge := nonzero_neighbor_defect_ge_two G hreg hdiam hn
  omega

/-- Filtering by the zero predicate cannot increase the genuine common-neighbor count. -/
theorem common_zero_count_le_common_count (G : SimpleGraph V) (n y : V) :
    (commonZeroNeighbors G n y).card ≤ commonNeighborCount G n y := by
  apply Finset.card_le_card
  intro z hz
  rw [mem_commonZeroNeighbors] at hz
  simpa using ⟨hz.1, hz.2.1⟩

/-- Every heavy zero endpoint lies outside the actual closed neighborhood. -/
theorem heavy_zero_repeat_nonedge (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8)
    {n y : V} (hy : y ∈ heavyZeroRepeats G n) : y ∈ nonedgeVertices G n := by
  have hy' : zeroTriangleVertex G y ∧ defectMatrix G n y = 2 := by simpa [heavyZeroRepeats] using hy
  rw [mem_nonedgeVertices]
  constructor
  · intro h
    subst y
    rw [defect_diagonal G hreg] at hy'
    omega
  · intro ha
    have hz := zero_vertex_edge_defect_zero G hy'.1 ha.symm
    rw [(defect_symmetric G).apply n y] at hz
    omega

/-- The local pair indicator plus a heavy-zero charge fits inside each actual
nonedge defect entry. This is a pointwise capacity inequality, not a certificate. -/
theorem common_zero_pair_capacity_pointwise (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    {n y : V} (hy : y ∈ nonedgeVertices G n) :
    commonZeroPairIndicator G n y + (if y ∈ heavyZeroRepeats G n then 1 else 0) ≤
      defectMatrix G n y := by
  rw [mem_nonedgeVertices] at hy
  have hnonneg := defect_nonnegative G hreg hdiam n y
  have hc := common_zero_count_le_common_count G n y
  have hB := defect_off_diagonal G hy.1.symm
  simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_neg hy.2] at hB
  by_cases htwo : (commonZeroNeighbors G n y).card = 2 <;>
    by_cases hh : y ∈ heavyZeroRepeats G n
  · have hh' : zeroTriangleVertex G y ∧ defectMatrix G n y = 2 := by simpa [heavyZeroRepeats] using hh
    simp [commonZeroPairIndicator, htwo, hh, hh'.2]
  · simp only [commonZeroPairIndicator, if_pos htwo, if_neg hh]
    omega
  · have hh' : zeroTriangleVertex G y ∧ defectMatrix G n y = 2 := by simpa [heavyZeroRepeats] using hh
    simp [commonZeroPairIndicator, htwo, hh, hh'.2]
  · simp [commonZeroPairIndicator, htwo, hh, hnonneg]

/-- The zero-triangle vertices in the actual neighborhood of n. -/
def zeroNeighbors (G : SimpleGraph V) (n : V) : Finset V :=
  (G.neighborFinset n).filter (zeroTriangleVertex G)

/-- Ordered heavy defect pairs among the actual zero neighbors of n. -/
def orderedHeavyZeroPairs (G : SimpleGraph V) (n : V) : Finset (V × V) :=
  (zeroNeighbors G n).offDiag.filter (fun p => defectMatrix G p.1 p.2 = 2)

@[simp] theorem mem_zeroNeighbors (G : SimpleGraph V) (n z : V) :
    z ∈ zeroNeighbors G n ↔ G.Adj n z ∧ zeroTriangleVertex G z := by simp [zeroNeighbors]

@[simp] theorem mem_orderedHeavyZeroPairs (G : SimpleGraph V) (n : V) (p : V × V) :
    p ∈ orderedHeavyZeroPairs G n ↔
      (G.Adj n p.1 ∧ zeroTriangleVertex G p.1) ∧
      (G.Adj n p.2 ∧ zeroTriangleVertex G p.2) ∧
      p.1 ≠ p.2 ∧ defectMatrix G p.1 p.2 = 2 := by
  simp [orderedHeavyZeroPairs, and_assoc]

private theorem sum_filter_card_swap {α β : Type*} (s : Finset α) (t : Finset β)
    (R : α → β → Prop) [∀ a b, Decidable (R a b)] :
    ∑ a ∈ s, (t.filter (R a)).card = ∑ b ∈ t, (s.filter (fun a => R a b)).card := by
  simp_rw [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]

/-- Each actual ordered heavy pair in a root's zero neighborhood has exactly
two common neighbors outside that root's closed neighborhood. -/
theorem ordered_heavy_pair_outside_witnesses_two (G : SimpleGraph V) {n : V} {p : V × V}
    (hp : p ∈ orderedHeavyZeroPairs G n) :
    ((nonedgeVertices G n).filter (fun y => G.Adj p.1 y ∧ G.Adj y p.2)).card = 2 := by
  rw [mem_orderedHeavyZeroPairs] at hp
  have hn : ¬ G.Adj p.1 p.2 := fun h => hp.1.2 n p.2 hp.1.1.symm h hp.2.1.1
  have hc : commonNeighborCount G p.1 p.2 = 3 := by
    have hB := defect_off_diagonal G hp.2.2.1
    simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_neg hn] at hB
    omega
  let C := (G.neighborFinset p.1).filter (fun y => G.Adj y p.2)
  have hnC : n ∈ C := by simp [C, hp.1.1.symm, hp.2.1.1]
  have heq : (nonedgeVertices G n).filter (fun y => G.Adj p.1 y ∧ G.Adj y p.2) = C.erase n := by
    ext y
    simp only [Finset.mem_filter, mem_nonedgeVertices, Finset.mem_erase]
    constructor
    · intro hy
      exact ⟨hy.1.1, by simpa [C] using hy.2⟩
    · rintro ⟨hyn, hyC⟩
      have hy' : G.Adj p.1 y ∧ G.Adj y p.2 := by simpa [C] using hyC
      exact ⟨⟨hyn, hp.1.2 n y hp.1.1.symm hy'.1⟩, hy'⟩
  rw [heq, Finset.card_erase_of_mem hnC]
  change commonNeighborCount G p.1 p.2 - 1 = 2
  omega

/-- Each root-outside vertex witnesses at most the two possible orientations
of its pair of common zero neighbors. -/
theorem ordered_heavy_pair_witness_capacity (G : SimpleGraph V)
    (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z)
    {n y : V} (hy : y ∈ nonedgeVertices G n) :
    ((orderedHeavyZeroPairs G n).filter (fun p => G.Adj p.1 y ∧ G.Adj y p.2)).card ≤
      if (commonZeroNeighbors G n y).card = 2 then 2 else 0 := by
  have hs : (orderedHeavyZeroPairs G n).filter (fun p => G.Adj p.1 y ∧ G.Adj y p.2) ⊆
      (commonZeroNeighbors G n y).offDiag := by
    intro p hp
    obtain ⟨hp, hpy⟩ := Finset.mem_filter.mp hp
    rw [mem_orderedHeavyZeroPairs] at hp
    rw [Finset.mem_offDiag, mem_commonZeroNeighbors, mem_commonZeroNeighbors]
    exact ⟨⟨hp.1.1, hpy.1, hp.1.2⟩, ⟨hp.2.1.1, hpy.2.symm, hp.2.1.2⟩, hp.2.2.1⟩
  have hle := Finset.card_le_card hs
  have hq := common_zero_neighbors_card_le_two G hm (mem_nonedgeVertices G n y |>.mp hy).1.symm
  rw [Finset.offDiag_card] at hle
  have hcases : (commonZeroNeighbors G n y).card = 0 ∨
      (commonZeroNeighbors G n y).card = 1 ∨ (commonZeroNeighbors G n y).card = 2 := by omega
  rcases hcases with hq0 | hq1 | hq2
  · norm_num only [hq0] at hle ⊢
    exact hle
  · norm_num only [hq1] at hle ⊢
    exact hle
  · norm_num only [hq2] at hle ⊢
    exact hle

/-- Genuine local double counting: the ordered heavy zero-neighbor pairs are
paid for by root-outside vertices with two actual common zero neighbors. -/
theorem ordered_heavy_pairs_le_pair_indicator_sum (G : SimpleGraph V)
    (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z) (n : V) :
    ((orderedHeavyZeroPairs G n).card : ℤ) ≤
      ∑ y ∈ nonedgeVertices G n, commonZeroPairIndicator G n y := by
  have hswap := sum_filter_card_swap (orderedHeavyZeroPairs G n) (nonedgeVertices G n)
    (fun p y => G.Adj p.1 y ∧ G.Adj y p.2)
  have hleft : (∑ p ∈ orderedHeavyZeroPairs G n,
      ((nonedgeVertices G n).filter (fun y => G.Adj p.1 y ∧ G.Adj y p.2)).card) =
      2 * (orderedHeavyZeroPairs G n).card := by
    rw [Finset.sum_congr rfl (fun p hp => ordered_heavy_pair_outside_witnesses_two G hp)]
    simp [mul_comm]
  have hright : (∑ y ∈ nonedgeVertices G n,
      ((orderedHeavyZeroPairs G n).filter (fun p => G.Adj p.1 y ∧ G.Adj y p.2)).card) ≤
      2 * ∑ y ∈ nonedgeVertices G n,
        (if (commonZeroNeighbors G n y).card = 2 then 1 else 0 : ℕ) := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro y hy
    have hh := ordered_heavy_pair_witness_capacity G hm hy
    split_ifs at hh ⊢ <;> omega
  have htwice := hleft.symm.trans_le (hswap.trans_le hright)
  have hnat : (orderedHeavyZeroPairs G n).card ≤ ∑ y ∈ nonedgeVertices G n,
      (if (commonZeroNeighbors G n y).card = 2 then 1 else 0 : ℕ) := by omega
  have hint : ((orderedHeavyZeroPairs G n).card : ℤ) ≤
      ((∑ y ∈ nonedgeVertices G n,
        (if (commonZeroNeighbors G n y).card = 2 then 1 else 0 : ℕ)) : ℤ) := by
    exact_mod_cast hnat
  simpa [commonZeroPairIndicator] using hint

/-- Summing the pointwise charge counts every actual heavy zero endpoint once. -/
theorem common_zero_pair_capacity_sum (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G) (n : V) :
    (∑ y ∈ nonedgeVertices G n, commonZeroPairIndicator G n y) +
      ((heavyZeroRepeats G n).card : ℤ) ≤ nonedgeDefectBudget G n := by
  have hfilter : (nonedgeVertices G n).filter (fun y => y ∈ heavyZeroRepeats G n) =
      heavyZeroRepeats G n := by
    ext y
    simp only [Finset.mem_filter]
    exact ⟨fun h => h.2, fun h => ⟨heavy_zero_repeat_nonedge G hreg h, h⟩⟩
  have hcount : (∑ y ∈ nonedgeVertices G n, (if y ∈ heavyZeroRepeats G n then 1 else 0 : ℤ)) =
      (heavyZeroRepeats G n).card := by
    rw [← Finset.sum_filter, hfilter]
    simp
  have hs := Finset.sum_le_sum (s := nonedgeVertices G n)
    (fun y hy => common_zero_pair_capacity_pointwise G hreg hdiam (n := n) hy)
  rw [Finset.sum_add_distrib, hcount] at hs
  exact hs

/-- Actual local capacity at a nonzero original order-59 root. The first term
counts ordered heavy pairs, hence equals twice the unordered heavy-pair count. -/
theorem n59_nonzero_local_heavy_capacity (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 59)
    (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z)
    {n : V} (hn : ¬ zeroTriangleVertex G n) :
    ((orderedHeavyZeroPairs G n).card : ℤ) + ((heavyZeroRepeats G n).card : ℤ) ≤ 4 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hp := ordered_heavy_pairs_le_pair_indicator_sum G hm n
  have hs := common_zero_pair_capacity_sum G hreg hdiam n
  have hb := n59_nonzero_nonedge_budget_le_four G hdeg hdiam hcard hn
  omega

/-- Actual vertices belonging to no triangle. -/
def zeroTriangleVertices (G : SimpleGraph V) : Finset V :=
  Finset.univ.filter (zeroTriangleVertex G)

/-- Actual vertices belonging to at least one triangle. -/
def nonzeroTriangleVertices (G : SimpleGraph V) : Finset V :=
  Finset.univ.filter (fun n => ¬ zeroTriangleVertex G n)

/-- All actual heavy defect endpoints of a row. -/
def heavyEndpoints (G : SimpleGraph V) (z : V) : Finset V :=
  Finset.univ.filter (fun y => defectMatrix G z y = 2)

/-- Ordered actual heavy pairs with both endpoints zero. -/
def globalHeavyZeroPairs (G : SimpleGraph V) : Finset (V × V) :=
  (zeroTriangleVertices G ×ˢ zeroTriangleVertices G).filter
    (fun p => defectMatrix G p.1 p.2 = 2)

private theorem heavy_zero_repeats_eq_filter (G : SimpleGraph V) (n : V) :
    heavyZeroRepeats G n = (zeroTriangleVertices G).filter (fun z => defectMatrix G n z = 2) := by
  ext z
  simp [heavyZeroRepeats, zeroTriangleVertices, and_assoc]

theorem matching_row_two_heavy_endpoints (G : SimpleGraph V) {z : V}
    (hm : matchingRow G z) : (heavyEndpoints G z).card = 2 := by
  obtain ⟨a, b, c, d, hab, hac, had, hbc, hbd, hcd, hr, _⟩ := hm
  have heq : heavyEndpoints G z = {a, b} := by
    ext y
    by_cases ha : y = a
    · subst y; simp [heavyEndpoints, hr, hab, hac, had]
    by_cases hb : y = b
    · subst y; simp [heavyEndpoints, hr, Ne.symm hab, hbc, hbd]
    by_cases hc : y = c
    · subst y; simp [heavyEndpoints, hr, Ne.symm hac, Ne.symm hbc, hcd]
    by_cases hd : y = d
    · subst y; simp [heavyEndpoints, hr, Ne.symm had, Ne.symm hbd, Ne.symm hcd]
    simp [heavyEndpoints, hr, ha, hb, hc, hd]
  rw [heq]
  simp [hab]

private theorem card_product_filter_eq_sum {α β : Type*} (s : Finset α) (t : Finset β)
    (R : α → β → Prop) [∀ a b, Decidable (R a b)] :
    ((s ×ˢ t).filter (fun p => R p.1 p.2)).card = ∑ a ∈ s, (t.filter (R a)).card := by
  simp_rw [Finset.card_eq_sum_ones, Finset.sum_filter, Finset.sum_product]

/-- The total number of directed heavy incidences at zero endpoints is exactly
2|Z|, split into ZZ incidences and heavy zero endpoints seen from nonzero roots. -/
theorem zero_heavy_degree_identity (G : SimpleGraph V)
    (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z) :
    (globalHeavyZeroPairs G).card +
      (∑ n ∈ nonzeroTriangleVertices G, (heavyZeroRepeats G n).card) =
      2 * (zeroTriangleVertices G).card := by
  have hall : (∑ n : V, (heavyZeroRepeats G n).card) = 2 * (zeroTriangleVertices G).card := by
    simp_rw [heavy_zero_repeats_eq_filter]
    rw [sum_filter_card_swap]
    have hcol (z : V) (hz : z ∈ zeroTriangleVertices G) :
        (Finset.univ.filter (fun n => defectMatrix G n z = 2)).card = 2 := by
      have heq : Finset.univ.filter (fun n => defectMatrix G n z = 2) = heavyEndpoints G z := by
        ext n
        simp [heavyEndpoints, (defect_symmetric G).apply z n]
      rw [heq]
      exact matching_row_two_heavy_endpoints G (hm z (by simpa [zeroTriangleVertices] using hz))
    rw [Finset.sum_congr rfl hcol]
    simp [mul_comm]
  have hzz : (globalHeavyZeroPairs G).card =
      ∑ z ∈ zeroTriangleVertices G, (heavyZeroRepeats G z).card := by
    unfold globalHeavyZeroPairs
    rw [card_product_filter_eq_sum (zeroTriangleVertices G) (zeroTriangleVertices G)
      (fun z y => defectMatrix G z y = 2)]
    simp_rw [heavy_zero_repeats_eq_filter]
  rw [hzz]
  change (∑ n ∈ Finset.univ.filter (zeroTriangleVertex G), (heavyZeroRepeats G n).card) +
    (∑ n ∈ Finset.univ.filter (fun n => ¬ zeroTriangleVertex G n), (heavyZeroRepeats G n).card) = _
  rw [Finset.sum_filter_add_sum_filter_not]
  exact hall

/-- Every ZZ heavy pair is covered by at least one genuine nonzero root's
ordered heavy zero-neighbor pairs. -/
theorem n59_global_heavy_zero_pairs_covered (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 59)
    (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z) :
    (globalHeavyZeroPairs G).card ≤
      ∑ n ∈ nonzeroTriangleVertices G, (orderedHeavyZeroPairs G n).card := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hs : globalHeavyZeroPairs G ⊆
      (nonzeroTriangleVertices G).biUnion (orderedHeavyZeroPairs G) := by
    intro p hp
    have hp' : (zeroTriangleVertex G p.1 ∧ zeroTriangleVertex G p.2) ∧
        defectMatrix G p.1 p.2 = 2 := by
      simpa [globalHeavyZeroPairs, zeroTriangleVertices] using hp
    obtain ⟨n, hzn, hny, hn⟩ :=
      n59_zero_heavy_has_nonzero_common_neighbor G hdeg hdiam hcard hm hp'.1.1 hp'.2
    have hne : p.1 ≠ p.2 := by
      intro he
      have hzero := defect_diagonal G hreg p.1
      rw [← he] at hp'
      omega
    apply Finset.mem_biUnion.mpr
    refine ⟨n, by simpa [nonzeroTriangleVertices] using hn, ?_⟩
    rw [mem_orderedHeavyZeroPairs]
    exact ⟨⟨hzn.symm, hp'.1.1⟩, ⟨hny, hp'.1.2⟩, hne, hp'.2⟩
  exact (Finset.card_le_card hs).trans Finset.card_biUnion_le

/-- New original-graph conditional bound: if zero-triangle vertices satisfy the
actual matching-row condition, at least twenty vertices lie in triangles. -/
theorem n59_nonzero_triangle_vertices_at_least_twenty (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 59)
    (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z) :
    20 ≤ (nonzeroTriangleVertices G).card := by
  have hdegree := zero_heavy_degree_identity G hm
  have hcover := n59_global_heavy_zero_pairs_covered G hdeg hdiam hcard hm
  have hlocal : (∑ n ∈ nonzeroTriangleVertices G,
      ((orderedHeavyZeroPairs G n).card + (heavyZeroRepeats G n).card)) ≤
      4 * (nonzeroTriangleVertices G).card := by
    calc
      _ ≤ ∑ _ ∈ nonzeroTriangleVertices G, 4 := by
        apply Finset.sum_le_sum
        intro n hn
        have hh := n59_nonzero_local_heavy_capacity G hdeg hdiam hcard hm
          (by simpa [nonzeroTriangleVertices] using hn)
        exact_mod_cast hh
      _ = _ := by simp [mul_comm]
  rw [Finset.sum_add_distrib] at hlocal
  have hpartition : (zeroTriangleVertices G).card + (nonzeroTriangleVertices G).card = 59 := by
    have hh := Finset.sum_filter_add_sum_filter_not Finset.univ (zeroTriangleVertex G) (fun _ => (1 : ℕ))
    simpa [zeroTriangleVertices, nonzeroTriangleVertices, hcard] using hh
  omega

end
end DegreeDiameter
