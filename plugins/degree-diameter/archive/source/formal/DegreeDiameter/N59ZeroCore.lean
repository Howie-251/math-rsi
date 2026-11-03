import DegreeDiameter.MatchingZero

namespace DegreeDiameter

open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section

variable {V : Type*} [Fintype V]

/-- A vertex belongs to no actual triangle: its actual neighborhood is independent. -/
def zeroTriangleVertex (G : SimpleGraph V) (z : V) : Prop :=
  ∀ u v, G.Adj z u → G.Adj z v → ¬ G.Adj u v

/-- Actual common neighbors which belong to no triangle. -/
def commonZeroNeighbors (G : SimpleGraph V) (u v : V) : Finset V :=
  (G.neighborFinset u).filter (fun z => G.Adj z v ∧ zeroTriangleVertex G z)

@[simp] theorem mem_commonZeroNeighbors (G : SimpleGraph V) (u v z : V) :
    z ∈ commonZeroNeighbors G u v ↔ G.Adj u z ∧ G.Adj z v ∧ zeroTriangleVertex G z := by
  simp [commonZeroNeighbors, and_assoc]

/-- Every positive actual entry in a matching row has one of its two weights. -/
theorem matching_row_positive_value (G : SimpleGraph V) {u v : V}
    (hm : matchingRow G u) (hpos : 0 < defectMatrix G u v) :
    defectMatrix G u v = 1 ∨ defectMatrix G u v = 2 := by
  obtain ⟨a, b, c, d, hab, hac, had, hbc, hbd, hcd, hr, _⟩ := hm
  have hv : v = a ∨ v = b ∨ v = c ∨ v = d := by
    by_contra h
    push_neg at h
    simp [hr, h.1, h.2.1, h.2.2.1, h.2.2.2] at hpos
  rcases hv with rfl | rfl | rfl | rfl <;>
    simp [hr, hab, hac, had, hbc, hbd, hcd, Ne.symm hab, Ne.symm hac,
      Ne.symm had, Ne.symm hbc, Ne.symm hbd, Ne.symm hcd]

/-- Two distinct equal-weight positive endpoints in the same matching row are
adjacent in the original graph. -/
theorem matching_row_equal_positive_adj (G : SimpleGraph V) {u v w : V}
    (hm : matchingRow G u) (hvw : v ≠ w) (hv : 0 < defectMatrix G u v)
    (heq : defectMatrix G u v = defectMatrix G u w) : G.Adj v w := by
  obtain ⟨a, b, c, d, hab, hac, had, hbc, hbd, hcd, hr, eab, ecd, _⟩ := hm
  have support (x : V) (hx : 0 < defectMatrix G u x) :
      x = a ∨ x = b ∨ x = c ∨ x = d := by
    by_contra h
    push_neg at h
    simp [hr, h.1, h.2.1, h.2.2.1, h.2.2.2] at hx
  have hw : 0 < defectMatrix G u w := heq ▸ hv
  rcases support v hv with rfl | rfl | rfl | rfl <;>
    rcases support w hw with rfl | rfl | rfl | rfl <;>
    simp_all [hr, Ne.symm hab, Ne.symm hac, Ne.symm had, Ne.symm hbc,
      Ne.symm hbd, Ne.symm hcd, SimpleGraph.adj_comm]

/-- Three independent vertices with matching rows cannot form a positive
triangle in the actual defect matrix. -/
theorem independent_matching_rows_no_defect_triangle (G : SimpleGraph V)
    {u v w : V} (hu : matchingRow G u) (hv : matchingRow G v)
    (hw : matchingRow G w) (huv : u ≠ v) (huw : u ≠ w) (hvw : v ≠ w)
    (nuv : ¬ G.Adj u v) (nuw : ¬ G.Adj u w) (nvw : ¬ G.Adj v w) :
    ¬ (0 < defectMatrix G u v ∧ 0 < defectMatrix G u w ∧ 0 < defectMatrix G v w) := by
  rintro ⟨puv, puw, pvw⟩
  have cuv := matching_row_positive_value G hu puv
  have cuw := matching_row_positive_value G hu puw
  have cvw := matching_row_positive_value G hv pvw
  have n1 : defectMatrix G u v ≠ defectMatrix G u w :=
    fun h => nvw (matching_row_equal_positive_adj G hu hvw puv h)
  have n2 : defectMatrix G u v ≠ defectMatrix G v w := by
    intro h
    apply nuw
    apply matching_row_equal_positive_adj G hv huw
    · simpa only [(defect_symmetric G).apply u v] using puv
    · simpa only [(defect_symmetric G).apply u v] using h
  have n3 : defectMatrix G u w ≠ defectMatrix G v w := by
    intro h
    apply nuv
    apply matching_row_equal_positive_adj G hw huv
    · simpa only [(defect_symmetric G).apply u w] using puw
    · simpa only [(defect_symmetric G).apply u w, (defect_symmetric G).apply v w] using h
  omega

/-- Two distinct genuine common neighbors force a positive defect entry at a
nonadjacent, distinct pair. -/
theorem defect_positive_of_two_common_neighbors (G : SimpleGraph V)
    {u v r s : V} (huv : u ≠ v) (hrs : r ≠ s) (hn : ¬ G.Adj u v)
    (hur : G.Adj u r) (hrv : G.Adj r v) (hus : G.Adj u s) (hsv : G.Adj s v) :
    0 < defectMatrix G u v := by
  have hs : ({r, s} : Finset V) ⊆ (G.neighborFinset u).filter (fun x => G.Adj x v) := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl <;> simp [hur, hrv, hus, hsv]
  have hc : 2 ≤ commonNeighborCount G u v := by
    simpa [commonNeighborCount, hrs] using Finset.card_le_card hs
  rw [defect_off_diagonal G huv]
  simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_neg hn]
  omega

/-- Under matching-row semantics only at zero-triangle vertices, every distinct
pair has at most two actual common zero-triangle neighbors. -/
theorem common_zero_neighbors_card_le_two (G : SimpleGraph V)
    (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z)
    {r s : V} (hrs : r ≠ s) : (commonZeroNeighbors G r s).card ≤ 2 := by
  by_contra h
  obtain ⟨u, v, w, hu, hv, hw, huv, huw, hvw⟩ :=
    Finset.two_lt_card_iff.mp (by omega : 2 < (commonZeroNeighbors G r s).card)
  rw [mem_commonZeroNeighbors] at hu hv hw
  have nuv : ¬ G.Adj u v := fun huv' => hu.2.2 r v hu.1.symm huv' hv.1
  have nuw : ¬ G.Adj u w := fun huw' => hu.2.2 r w hu.1.symm huw' hw.1
  have nvw : ¬ G.Adj v w := fun hvw' => hv.2.2 r w hv.1.symm hvw' hw.1
  apply independent_matching_rows_no_defect_triangle G (hm u hu.2.2) (hm v hv.2.2)
    (hm w hw.2.2) huv huw hvw nuv nuw nvw
  exact ⟨defect_positive_of_two_common_neighbors G huv hrs nuv
      hu.1.symm hv.1 hu.2.1 hv.2.1.symm,
    defect_positive_of_two_common_neighbors G huw hrs nuw
      hu.1.symm hw.1 hu.2.1 hw.2.1.symm,
    defect_positive_of_two_common_neighbors G hvw hrs nvw
      hv.1.symm hw.1 hv.2.1 hw.2.1.symm⟩

/-- An actual graph edge incident with a zero-triangle vertex has zero defect. -/
theorem zero_vertex_edge_defect_zero (G : SimpleGraph V) {u v : V}
    (hz : zeroTriangleVertex G u) (ha : G.Adj u v) : defectMatrix G u v = 0 := by
  have hc : commonNeighborCount G u v = 0 := by
    apply Finset.card_eq_zero.mpr
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro w hw
    have hw' : G.Adj u w ∧ G.Adj w v := by simpa using hw
    exact hz v w ha hw'.1 hw'.2.symm
  rw [defect_off_diagonal G ha.ne, hc]
  simp [adjacencyMatrix, ha]

/-- A heavy defect pair with a zero endpoint has an actual common neighbor
which lies in a triangle. Matching rows are required only at zero vertices. -/
theorem zero_heavy_has_nonzero_common_neighbor (G : SimpleGraph V)
    (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z)
    {u v : V} (hu : zeroTriangleVertex G u) (huv : u ≠ v)
    (hb : defectMatrix G u v = 2) :
    ∃ w, G.Adj u w ∧ G.Adj w v ∧ ¬ zeroTriangleVertex G w := by
  have hn : ¬ G.Adj u v := by
    intro ha
    have := zero_vertex_edge_defect_zero G hu ha
    omega
  have hc : commonNeighborCount G u v = 3 := by
    have hh := defect_off_diagonal G huv
    simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_neg hn] at hh
    omega
  by_contra h
  push_neg at h
  have heq : commonZeroNeighbors G u v =
      (G.neighborFinset u).filter (fun w => G.Adj w v) := by
    ext w
    simp only [mem_commonZeroNeighbors, Finset.mem_filter, SimpleGraph.mem_neighborFinset]
    exact ⟨fun hw => ⟨hw.1, hw.2.1⟩,
      fun hw => ⟨hw.1, hw.2, h w hw.1 hw.2⟩⟩
  have hle := common_zero_neighbors_card_le_two G hm huv
  rw [heq] at hle
  change commonNeighborCount G u v ≤ 2 at hle
  omega

/-- Original order-59 caller, deriving the needed distinctness from the actual
zero diagonal of the graph's defect matrix. -/
theorem n59_zero_heavy_has_nonzero_common_neighbor (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 59)
    (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z)
    {u v : V} (hu : zeroTriangleVertex G u) (hb : defectMatrix G u v = 2) :
    ∃ w, G.Adj u w ∧ G.Adj w v ∧ ¬ zeroTriangleVertex G w := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have huv : u ≠ v := by
    rintro rfl
    rw [defect_diagonal G hreg] at hb
    omega
  exact zero_heavy_has_nonzero_common_neighbor G hm hu huv hb

end
end DegreeDiameter
