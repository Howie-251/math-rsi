import DegreeDiameter

#print DegreeDiameter.degreeAtMostEight
#print DegreeDiameter.diameterAtMostTwo
#print DegreeDiameter.Exists82
#print DegreeDiameter.IsExact82
#check @DegreeDiameter.card_le_one_add_eight_mul_degree
#check @DegreeDiameter.moore_bound
#check @DegreeDiameter.regular_of_card_gt_57
#check @DegreeDiameter.exists82_le_65
#print axioms DegreeDiameter.card_le_one_add_eight_mul_degree
#print axioms DegreeDiameter.moore_bound
#print axioms DegreeDiameter.regular_of_card_gt_57
#print axioms DegreeDiameter.exists82_le_65

attribute [local instance] Classical.propDecidable

/-- Independent statement-level caller using only the original raw graph hypotheses. -/
theorem original_graph_bound {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : ∀ v, G.degree v ≤ 8)
    (hpaths : ∀ u v, u ≠ v → G.Adj u v ∨ ∃ w, G.Adj u w ∧ G.Adj w v) :
    Fintype.card V ≤ 65 :=
  DegreeDiameter.moore_bound G hdeg hpaths

#print original_graph_bound
#print axioms original_graph_bound

#print DegreeDiameter.brownCoords
#print DegreeDiameter.brownDot
#print DegreeDiameter.brownAdj
#print DegreeDiameter.brown57
#check @DegreeDiameter.brown57_computable_degree
#check @DegreeDiameter.brown57_diameter
#check @DegreeDiameter.brown57_degree
#check @DegreeDiameter.exists82_57
#print axioms DegreeDiameter.brown57_computable_degree
#print axioms DegreeDiameter.brown57_diameter
#print axioms DegreeDiameter.brown57_degree
#print axioms DegreeDiameter.exists82_57

/-- A witness and a universal bound for the original order predicate, with no exactness claim. -/
theorem original_baseline : DegreeDiameter.Exists82 57 ∧
    ∀ n, DegreeDiameter.Exists82 n → n ≤ 65 :=
  ⟨DegreeDiameter.exists82_57, fun _ h => DegreeDiameter.exists82_le_65 h⟩
#print original_baseline
#print axioms original_baseline


#print DegreeDiameter.adjacencyMatrix
#print DegreeDiameter.onesMatrix
#print DegreeDiameter.defectMatrix
#print DegreeDiameter.commonNeighborCount
#check @DegreeDiameter.adjacency_sq_common_count
#check @DegreeDiameter.defect_diagonal
#check @DegreeDiameter.defect_symmetric
#check @DegreeDiameter.defect_off_diagonal
#check @DegreeDiameter.defect_nonnegative
#check @DegreeDiameter.defect_row_sum
#check @DegreeDiameter.adjacency_defect_commute
#check @DegreeDiameter.original_graph_defect_properties
#print axioms DegreeDiameter.adjacency_sq_common_count
#print axioms DegreeDiameter.defect_diagonal
#print axioms DegreeDiameter.defect_symmetric
#print axioms DegreeDiameter.defect_off_diagonal
#print axioms DegreeDiameter.defect_nonnegative
#print axioms DegreeDiameter.defect_row_sum
#print axioms DegreeDiameter.adjacency_defect_commute
#print axioms DegreeDiameter.original_graph_defect_properties


#check @DegreeDiameter.five_dvd_trace_fifth_of_trace_zero
#check @DegreeDiameter.five_dvd_adjacency_fifth
#check @DegreeDiameter.fifth_matrix_identity_59
#check @DegreeDiameter.fifth_trace_identity_59
#check @DegreeDiameter.no_n59_with_matching_zero_traces
#print axioms DegreeDiameter.five_dvd_trace_fifth_of_trace_zero
#print axioms DegreeDiameter.five_dvd_adjacency_fifth
#print axioms DegreeDiameter.fifth_matrix_identity_59
#print axioms DegreeDiameter.fifth_trace_identity_59
#print axioms DegreeDiameter.no_n59_with_matching_zero_traces


#print DegreeDiameter.triangleFree
#print DegreeDiameter.matchingRow
#check @DegreeDiameter.matching_row_square
#check @DegreeDiameter.matching_row_quadratic
#check @DegreeDiameter.matching_rows_square_trace
#check @DegreeDiameter.matching_rows_mixed_trace
#check @DegreeDiameter.triangle_free_cube_trace
#check @DegreeDiameter.no_n59_triangle_free_matching_rows
#print axioms DegreeDiameter.matching_row_square
#print axioms DegreeDiameter.matching_row_quadratic
#print axioms DegreeDiameter.matching_rows_square_trace
#print axioms DegreeDiameter.matching_rows_mixed_trace
#print axioms DegreeDiameter.triangle_free_cube_trace
#print axioms DegreeDiameter.no_n59_triangle_free_matching_rows


#check @DegreeDiameter.defect_zero_of_card_65
#check @DegreeDiameter.no_original_graph_card_65
#check @DegreeDiameter.original_graph_card_le_64
#check @DegreeDiameter.exists82_le_64
#print axioms DegreeDiameter.defect_zero_of_card_65
#print axioms DegreeDiameter.no_original_graph_card_65
#print axioms DegreeDiameter.original_graph_card_le_64
#print axioms DegreeDiameter.exists82_le_64

theorem original_baseline64 : DegreeDiameter.Exists82 57 ∧
    ∀ n, DegreeDiameter.Exists82 n → n ≤ 64 :=
  ⟨DegreeDiameter.exists82_57, fun _ h => DegreeDiameter.exists82_le_64 h⟩
#print original_baseline64
#print axioms original_baseline64


#check @DegreeDiameter.defect_zero_or_one_of_card_64
#check @DegreeDiameter.defect_pair_le_one_of_card_64
#check @DegreeDiameter.defect_square_identity_of_card_64
#check @DegreeDiameter.triangle_free_of_card_64
#check @DegreeDiameter.adjacency_defect_trace_zero_of_triangle_free
#check @DegreeDiameter.no_original_graph_card_64
#check @DegreeDiameter.original_graph_card_le_63
#check @DegreeDiameter.exists82_le_63
#print axioms DegreeDiameter.defect_zero_or_one_of_card_64
#print axioms DegreeDiameter.defect_pair_le_one_of_card_64
#print axioms DegreeDiameter.defect_square_identity_of_card_64
#print axioms DegreeDiameter.triangle_free_of_card_64
#print axioms DegreeDiameter.adjacency_defect_trace_zero_of_triangle_free
#print axioms DegreeDiameter.no_original_graph_card_64
#print axioms DegreeDiameter.original_graph_card_le_63
#print axioms DegreeDiameter.exists82_le_63

theorem original_baseline63 : DegreeDiameter.Exists82 57 ∧
    ∀ n, DegreeDiameter.Exists82 n → n ≤ 63 :=
  ⟨DegreeDiameter.exists82_57, fun _ h => DegreeDiameter.exists82_le_63 h⟩
#print original_baseline63
#print axioms original_baseline63


#check @DegreeDiameter.degree_bound_of_iso
#check @DegreeDiameter.diameter_bound_of_iso
#check @DegreeDiameter.finite_relabel
#check @DegreeDiameter.exists82_of_original_graph
#check @DegreeDiameter.exists82_iff_fin
#print axioms DegreeDiameter.degree_bound_of_iso
#print axioms DegreeDiameter.diameter_bound_of_iso
#print axioms DegreeDiameter.finite_relabel
#print axioms DegreeDiameter.exists82_of_original_graph
#print axioms DegreeDiameter.exists82_iff_fin


#check @DegreeDiameter.norm_twenty_nine_add_four_gen
#check @DegreeDiameter.not_isSquare_discriminant_of_norm
#print DegreeDiameter.cyclotomicLift
#check DegreeDiameter.cyclotomicLift_mul
#check DegreeDiameter.cyclotomicLift_eq_sum
#check DegreeDiameter.cyclotomicLift_natDegree
#check @DegreeDiameter.irreducible_of_cyclotomicLift_irreducible
#check @DegreeDiameter.irreducible_of_cyclotomic_lift
#print axioms DegreeDiameter.norm_twenty_nine_add_four_gen
#print axioms DegreeDiameter.not_isSquare_discriminant_of_norm
#print axioms DegreeDiameter.cyclotomicLift_mul
#print axioms DegreeDiameter.cyclotomicLift_eq_sum
#print axioms DegreeDiameter.cyclotomicLift_natDegree
#print axioms DegreeDiameter.irreducible_of_cyclotomicLift_irreducible
#print axioms DegreeDiameter.irreducible_of_cyclotomic_lift

-- New n59 local capacity inputs; dedicated executed audit: ReviewN59ZeroCore.lean.
#print DegreeDiameter.zeroTriangleVertex
#print DegreeDiameter.commonZeroNeighbors
#check @DegreeDiameter.common_zero_neighbors_card_le_two
#check @DegreeDiameter.zero_heavy_has_nonzero_common_neighbor
#check @DegreeDiameter.n59_zero_heavy_has_nonzero_common_neighbor
#print axioms DegreeDiameter.common_zero_neighbors_card_le_two
#print axioms DegreeDiameter.zero_heavy_has_nonzero_common_neighbor
#print axioms DegreeDiameter.n59_zero_heavy_has_nonzero_common_neighbor

-- Executed separately in ReviewN59Capacity.lean; no known-bound regression.
#print DegreeDiameter.nonzeroTriangleVertices
#check @DegreeDiameter.n59_nonzero_local_heavy_capacity
#check @DegreeDiameter.zero_heavy_degree_identity
#check @DegreeDiameter.n59_global_heavy_zero_pairs_covered
#check @DegreeDiameter.n59_nonzero_triangle_vertices_at_least_twenty
#print axioms DegreeDiameter.n59_nonzero_local_heavy_capacity
#print axioms DegreeDiameter.zero_heavy_degree_identity
#print axioms DegreeDiameter.n59_global_heavy_zero_pairs_covered
#print axioms DegreeDiameter.n59_nonzero_triangle_vertices_at_least_twenty

-- Executed independently in ReviewN62STouch.lean.
#check @DegreeDiameter.no_n62_stouch_template
#print axioms DegreeDiameter.no_n62_stouch_template

-- Dedicated actual type/axiom audit in ReviewN62TriangleMate.lean.
#check @DegreeDiameter.n62_triangle_has_paired_triangle
#print axioms DegreeDiameter.n62_triangle_has_paired_triangle

#check @DegreeDiameter.n62_triangle_count_even
#print axioms DegreeDiameter.n62_triangle_count_even

#check @DegreeDiameter.n62_unit_nonedge_pair_count_even
#print axioms DegreeDiameter.n62_unit_nonedge_pair_count_even

-- Dedicated executed original-caller audit: ReviewN62SimpleExclusion.lean.
#check @DegreeDiameter.no_n62_simple_defect_graph
#print axioms DegreeDiameter.no_n62_simple_defect_graph

-- Dedicated executed actual-parent audit: ReviewN62D2.lean.
#check @DegreeDiameter.no_n62_d2_match_template
#print axioms DegreeDiameter.no_n62_d2_match_template

-- Dedicated executed actual-parent audit: ReviewN62D0Bin.lean.
#check @DegreeDiameter.no_n62_d0_edge_bin_template
#print axioms DegreeDiameter.no_n62_d0_edge_bin_template

-- Dedicated actual-parent audit: ReviewN62D0Components.lean.
#check @DegreeDiameter.n62_d0_match_closed_component
#check @DegreeDiameter.n62_d0_bout_closed_component
#print axioms DegreeDiameter.n62_d0_match_closed_component
#print axioms DegreeDiameter.n62_d0_bout_closed_component

-- Dedicated actual counting/caller audit: ReviewN62DoubleParity.lean.
#check @DegreeDiameter.n62_double_repeat_pair_count_odd
#print axioms DegreeDiameter.n62_double_repeat_pair_count_odd

-- Dedicated actual-root coverage and global outlet audits.
#check @DegreeDiameter.n62_double_root_d1_or_closed_component
#print axioms DegreeDiameter.n62_double_root_d1_or_closed_component
#check @DegreeDiameter.n62_exists_d1_match_parent
#print axioms DegreeDiameter.n62_exists_d1_match_parent

-- Dedicated actual-component callers: ReviewN62RepeatComponents.lean.
#check @DegreeDiameter.n62_repeat_components_equitable
#check @DegreeDiameter.n62_repeat_component_degree_spec
#print axioms DegreeDiameter.n62_repeat_components_equitable
#print axioms DegreeDiameter.n62_repeat_component_degree_spec

-- Dedicated actual quotient identity callers: ReviewN62RepeatQuotient.lean.
#check @DegreeDiameter.n62_repeat_quotient_quadratic
#check @DegreeDiameter.n62_repeat_quotient_row_sum
#check @DegreeDiameter.n62_repeat_quotient_balance
#print axioms DegreeDiameter.n62_repeat_quotient_quadratic
#print axioms DegreeDiameter.n62_repeat_quotient_row_sum
#print axioms DegreeDiameter.n62_repeat_quotient_balance

-- Dedicated component parity/minimum/budget callers: ReviewN62RepeatComponentBounds.lean.
#check @DegreeDiameter.n62_repeat_component_size_even
#check @DegreeDiameter.n62_repeat_component_size_ge_four
#check @DegreeDiameter.n62_repeat_quotient_budget
#print axioms DegreeDiameter.n62_repeat_component_size_even
#print axioms DegreeDiameter.n62_repeat_component_size_ge_four
#print axioms DegreeDiameter.n62_repeat_quotient_budget

-- Dedicated original-graph trace/oddness callers: ReviewN62RepeatQuotientTrace.lean.
#check @DegreeDiameter.n62_repeat_quotient_trace_identity
#check @DegreeDiameter.n62_repeat_component_count_odd
#print axioms DegreeDiameter.n62_repeat_quotient_trace_identity
#print axioms DegreeDiameter.n62_repeat_component_count_odd

-- Dedicated original-graph triple-repeat geometry: ReviewN62TripleRepeat.lean.
#check @DegreeDiameter.n62_triple_common_rows
#check @DegreeDiameter.n62_triple_component_sizes
#print axioms DegreeDiameter.n62_triple_common_rows
#print axioms DegreeDiameter.n62_triple_component_sizes

-- Dedicated actual exclusive-side matching and component-weight callers.
#check @DegreeDiameter.tripleMatchingEquiv_adj_iff
#check @DegreeDiameter.n62_triple_exclusive_exterior_card
#print axioms DegreeDiameter.tripleMatchingEquiv_adj_iff
#print axioms DegreeDiameter.n62_triple_exclusive_exterior_card
#check @DegreeDiameter.n62_repeat_component_subset_budget
#check @DegreeDiameter.n62_no_six_components_three_internal_two
#print axioms DegreeDiameter.n62_repeat_component_subset_budget
#print axioms DegreeDiameter.n62_no_six_components_three_internal_two

-- Dedicated actual five-cell separation and four-label classification audits.
#check @DegreeDiameter.n62_triple_remaining_card
#check @DegreeDiameter.n62_triple_remaining_repeat_closed
#print axioms DegreeDiameter.n62_triple_remaining_card
#print axioms DegreeDiameter.n62_triple_remaining_repeat_closed
#check @DegreeDiameter.n62_four_block_classification
#print axioms DegreeDiameter.n62_four_block_classification

-- Dedicated actual matching labels and actual matrix classification callers.
#check @DegreeDiameter.n62_triple_actual_block_classification
#print axioms DegreeDiameter.n62_triple_actual_block_classification
