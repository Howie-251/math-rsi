import Aris4Math.K6Traces
import Aris4Math.Numeric
import Aris4Math.TypeCounting
import Mathlib.Tactic.IntervalCases

/-! Actual labeled trace multiplicities and the numerical six-lock profiles. -/

open scoped BigOperators

namespace Aris4Math.TraceProfiles

open K6Classification K6Traces

variable {V : Type*} [DecidableEq V]

/-- Actual lock vertices, indexed by the labels in the six-point representative. -/
def lockVertices (W : Finset V) (label : ↥W ≃ Fin 6) : Fin 6 ↪ V :=
  label.symm.toEmbedding.trans (Function.Embedding.subtype (fun x => x ∈ W))

/-- The exact subset of lock labels carried by an actual edge. -/
abbrev lockedLabels {ι : Type*} [Fintype ι] [DecidableEq ι]
    (vertices : ι ↪ V) (e : Finset V) : Finset ι := TypeCounting.lockSignature vertices e

@[simp] theorem mem_lockedLabels {ι : Type*} [Fintype ι] [DecidableEq ι]
    (vertices : ι ↪ V) (e : Finset V) (i : ι) :
    i ∈ lockedLabels vertices e ↔ vertices i ∈ e := by simp [lockedLabels, TypeCounting.lockSignature]

/-- Convert a label subset back into the actual vertex subset. -/
def unlabel (W : Finset V) (label : ↥W ≃ Fin 6) (T : Finset (Fin 6)) : Finset V :=
  T.map (lockVertices W label)

omit [DecidableEq V] in
theorem unlabel_subset (W : Finset V) (label : ↥W ≃ Fin 6) (T : Finset (Fin 6)) :
    unlabel W label T ⊆ W := by
  intro x hx
  obtain ⟨i, _, rfl⟩ := Finset.mem_map.mp hx
  exact (label.symm i).property

omit [DecidableEq V] in
@[simp] theorem unlabel_card (W : Finset V) (label : ↥W ≃ Fin 6) (T : Finset (Fin 6)) :
    (unlabel W label T).card = T.card := Finset.card_map _

@[simp] theorem label_unlabel (W : Finset V) (label : ↥W ≃ Fin 6) (T : Finset (Fin 6)) :
    labelBlock W label (unlabel W label T) = T := by
  ext i
  rw [mem_labelBlock]
  change lockVertices W label i ∈ T.map (lockVertices W label) ↔ i ∈ T
  exact Finset.mem_map' _

theorem labelBlock_injective (W : Finset V) (label : ↥W ≃ Fin 6)
    {B C : Finset V} (hB : B ⊆ W) (hC : C ⊆ W)
    (same : labelBlock W label B = labelBlock W label C) : B = C := by
  apply onGround_injective W hB hC
  exact Finset.map_injective label.toEmbedding same

theorem labels_eq_iff_trace (W : Finset V) (label : ↥W ≃ Fin 6)
    (e : Finset V) (T : Finset (Fin 6)) :
    lockedLabels (lockVertices W label) e = T ↔ e ∩ W = unlabel W label T := by
  have hl : labelBlock W label (e ∩ W) = lockedLabels (lockVertices W label) e := by
    ext i
    simp [lockVertices]
  constructor
  · intro h
    apply labelBlock_injective W label Finset.inter_subset_right (unlabel_subset W label T)
    rw [hl, h, label_unlabel]
  · intro h
    rw [← hl, h, label_unlabel]

/-- Actual edge-fiber count equals the already-defined exact trace multiplicity. -/
theorem labeled_fiber_card (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) (T : Finset (Fin 6)) :
    (H.edges.filter (fun e => lockedLabels (lockVertices W label) e = T)).card =
      H.typeCount W (unlabel W label T) := by
  unfold Simple5Hypergraph.typeCount
  congr 1
  apply Finset.filter_congr
  intro e _
  exact labels_eq_iff_trace W label e T

/-- The generic type-count formula forced by a full block family, fixed lock
degree, and total edge count. Subtraction is justified by the exact count lemmas. -/
def recoveredCount (edges degree : Nat) (blocks : Finset (Finset (Fin 6)))
    (T : Finset (Fin 6)) : Nat :=
  if T = ∅ then
    edges - blocks.card - ∑ i : Fin 6, (degree - (blocks.filter (fun B => i ∈ B)).card)
  else if T.card = 1 then
    ∑ i ∈ T, (degree - (blocks.filter (fun B => i ∈ B)).card)
  else if T ∈ blocks then 1 else 0

theorem labeled_blocks_card (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) :
    ((H.multiTraces W).image (labelBlock W label)).card = (H.multiTraces W).card := by
  apply Finset.card_image_of_injOn
  intro B hB C hC h
  exact labelBlock_injective W label (H.multiTraces_subset W hB) (H.multiTraces_subset W hC) h

theorem labeled_incidence_card (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) (i : Fin 6) :
    (((H.multiTraces W).image (labelBlock W label)).filter (fun B => i ∈ B)).card =
      ((H.multiTraces W).filter (fun B => lockVertices W label i ∈ B)).card := by
  rw [Finset.filter_image]
  have eq : (H.multiTraces W).filter (fun B => i ∈ labelBlock W label B) =
      (H.multiTraces W).filter (fun B => lockVertices W label i ∈ B) := by
    apply Finset.filter_congr
    intro B _
    exact mem_labelBlock W label B i
  rw [eq]
  apply Finset.card_image_of_injOn
  intro B hB C hC h
  exact labelBlock_injective W label
    (H.multiTraces_subset W (Finset.mem_filter.mp hB).1)
    (H.multiTraces_subset W (Finset.mem_filter.mp hC).1) h

theorem labeled_singleton_count (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) (unit : H.UnitCodegrees W) (degree : Nat)
    (degrees : ∀ x ∈ W, H.degree x = degree) (i : Fin 6) :
    H.typeCount W (unlabel W label {i}) =
      degree - (((H.multiTraces W).image (labelBlock W label)).filter (fun B => i ∈ B)).card := by
  rw [labeled_incidence_card]
  have h := H.singleton_typeCount_eq W unit (label.symm i).property
  rw [degrees _ (label.symm i).property] at h
  simpa [unlabel, lockVertices] using h

theorem singleton_sum_labels (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) :
    (∑ x ∈ W, H.typeCount W {x}) = ∑ i : Fin 6, H.typeCount W (unlabel W label {i}) := by
  apply Finset.sum_bij (fun x hx => label ⟨x, hx⟩) (fun _ _ => Finset.mem_univ _)
  · intro x hx y hy eq
    exact congrArg Subtype.val (label.injective eq)
  · intro i _
    exact ⟨(label.symm i).val, (label.symm i).property, label.apply_symm_apply i⟩
  · intro x hx
    simp [unlabel, lockVertices]

theorem unlabel_mem_blocks (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) (T : Finset (Fin 6)) :
    unlabel W label T ∈ H.multiTraces W ↔
      T ∈ (H.multiTraces W).image (labelBlock W label) := by
  constructor
  · intro h
    exact Finset.mem_image.mpr ⟨unlabel W label T, h, label_unlabel W label T⟩
  · intro h
    obtain ⟨B, hB, eq⟩ := Finset.mem_image.mp h
    have same : B = unlabel W label T := labelBlock_injective W label
      (H.multiTraces_subset W hB) (unlabel_subset W label T)
      (eq.trans (label_unlabel W label T).symm)
    exact same ▸ hB

/-- Derive every exact type count of the actual hypergraph from its full
labeled block family. Empty, singleton, and large types are all proved here. -/
theorem actual_recovered_count (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) (unit : H.UnitCodegrees W) (degree : Nat)
    (degrees : ∀ x ∈ W, H.degree x = degree) (T : Finset (Fin 6)) :
    (H.edges.filter (fun e => lockedLabels (lockVertices W label) e = T)).card =
      recoveredCount H.edges.card degree ((H.multiTraces W).image (labelBlock W label)) T := by
  rw [labeled_fiber_card]
  by_cases empty : T = ∅
  · subst T
    simp only [recoveredCount, unlabel, Finset.map_empty]
    rw [H.empty_typeCount_eq W unit, singleton_sum_labels H W label, labeled_blocks_card]
    congr 1
    apply Finset.sum_congr rfl
    intro i _
    exact labeled_singleton_count H W label unit degree degrees i
  by_cases one : T.card = 1
  · obtain ⟨i, rfl⟩ := Finset.card_eq_one.mp one
    simpa [recoveredCount] using labeled_singleton_count H W label unit degree degrees i
  · have large : 2 ≤ (unlabel W label T).card := by
      rw [unlabel_card]
      have pos : 0 < T.card := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr empty)
      omega
    rw [H.typeCount_large W _ unit large]
    simp only [unlabel_mem_blocks, recoveredCount, if_neg empty, if_neg one]

/-- Select the exact existing numeric profile, including the diagnostic bad type. -/
def profile25 (k : Fin 9) : Numeric.Profile :=
  match k.val with
  | 0 => Numeric.v25_K6_1
  | 1 => Numeric.v25_K6_2
  | 2 => Numeric.v25_K6_3
  | 3 => Numeric.v25_K6_4
  | 4 => Numeric.v25_K6_5
  | 5 => Numeric.v25_K6_6
  | 6 => Numeric.v25_K6_7
  | 7 => Numeric.v25_K6_8
  | _ => Numeric.v25_K6_9

/-- One-based positions used by Numeric. The permutation modules use one less. -/
def numericPosition25 (i : Fin 6) : Nat := i.val + 10

def positionType25 (T : Finset (Fin 6)) : Finset Nat := T.image numericPosition25

/-- A table is interpreted by its actual lock sets, independent of list order. -/
def tableCount (p : Numeric.Profile) (S : Finset Nat) : Nat :=
  ((p.types.filter (fun t => t.locks.toFinset = S)).map Numeric.EdgeType.count).sum

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- Closed data equality for 9 × 64 exact label subsets. Arbitrary hypergraph
type multiplicities are handled by actual_recovered_count, not by this check. -/
theorem numeric_counts_match : ∀ k : Fin 9, ∀ T : Finset (Fin 6),
    recoveredCount 32 6 (fullRepresentative k) T = tableCount (profile25 k) (positionType25 T) := by
  decide +kernel

/-- The true edge-fiber count is exactly the Numeric table entry for that set
of one-based locked positions. The labeled family is a structural equality. -/
theorem actual_numeric_count (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 9) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative k)
    (T : Finset (Fin 6)) :
    (H.edges.filter (fun e => lockedLabels (lockVertices W label) e = T)).card =
      tableCount (profile25 k) (positionType25 T) := by
  rw [actual_recovered_count H W label unit 6 degrees, edges32, family]
  exact numeric_counts_match k T

/-- The six fixed permutation positions, zero-based for the event modules. -/
def positions25 : Fin 6 ↪ Fin 25 where
  toFun i := ⟨i.val + 9, by omega⟩
  inj' := by
    intro i j h
    apply Fin.ext
    have he := congrArg Fin.val h
    change i.val + 9 = j.val + 9 at he
    omega

def decode25 (S : Finset Nat) : Finset (Fin 6) :=
  Finset.univ.filter (fun i => numericPosition25 i ∈ S)

theorem positionType25_injective : Function.Injective positionType25 := by
  apply Finset.image_injective
  intro i j h
  apply Fin.ext
  dsimp [numericPosition25] at h
  omega

/-- Canonical position lists for a possibly non-Fin ambient vertex type. -/
def canonicalType25 (vertices : Fin 6 ↪ V) (e : Finset V) : List Nat :=
  (positionType25 (lockedLabels vertices e)).sort (· ≤ ·)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem profile25_data : ∀ k : Fin 9,
    Numeric.validProfile (profile25 k) ∧ (profile25 k).v = 25 ∧
    (profile25 k).positions.toFinset = Finset.univ.image (fun i => (positions25 i).val + 1) ∧
    ((profile25 k).types.all (fun t => decide (
      t.locks.Nodup ∧ t.locks.Pairwise (· ≤ ·) ∧
      positionType25 (decode25 t.locks.toFinset) = t.locks.toFinset ∧
      tableCount (profile25 k) t.locks.toFinset = t.count))) := by
  unfold Numeric.validProfile
  decide +kernel

theorem profile25_entry (k : Fin 9) (t : Numeric.EdgeType) (ht : t ∈ (profile25 k).types) :
    t.locks.toFinset.sort (· ≤ ·) = t.locks ∧
      positionType25 (decode25 t.locks.toFinset) = t.locks.toFinset ∧
      tableCount (profile25 k) t.locks.toFinset = t.count := by
  have h := List.all_eq_true.mp (profile25_data k).2.2.2 t ht
  rcases of_decide_eq_true h with ⟨nodup, sorted, encoded, count⟩
  exact ⟨(List.toFinset_sort (· ≤ ·) nodup).mpr sorted, encoded, count⟩

theorem canonicalType25_eq_iff (vertices : Fin 6 ↪ V) (e : Finset V)
    (k : Fin 9) (t : Numeric.EdgeType) (ht : t ∈ (profile25 k).types) :
    canonicalType25 vertices e = t.locks ↔
      lockedLabels vertices e = decode25 t.locks.toFinset := by
  have data := profile25_entry k t ht
  constructor
  · intro h
    have eq := congrArg List.toFinset h
    simp only [canonicalType25, Finset.sort_toFinset] at eq
    exact positionType25_injective (eq.trans data.2.1.symm)
  · intro h
    unfold canonicalType25
    rw [h, data.2.1, data.1]

/-- Every row in the numerical list is proved to have its stated actual fiber
size; no type-count row is introduced as an assumption. -/
theorem actual_entry_count (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 9) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative k)
    (t : Numeric.EdgeType) (ht : t ∈ (profile25 k).types) :
    TypeCounting.multiplicity H.edges (canonicalType25 (lockVertices W label)) t.locks = t.count := by
  unfold TypeCounting.multiplicity TypeCounting.fiber
  have eq : H.edges.filter (fun e => canonicalType25 (lockVertices W label) e = t.locks) =
      H.edges.filter (fun e => lockedLabels (lockVertices W label) e = decode25 t.locks.toFinset) := by
    apply Finset.filter_congr
    intro e _
    exact canonicalType25_eq_iff _ e k t ht
  rw [eq, actual_numeric_count H W label unit degrees edges32 k family]
  have data := profile25_entry k t ht
  rw [data.2.1, data.2.2]

theorem exists_entry_of_tableCount_pos (p : Numeric.Profile) (S : Finset Nat)
    (positive : 0 < tableCount p S) :
    ∃ t ∈ p.types, t.locks.toFinset = S := by
  by_contra h
  have empty : p.types.filter (fun t => t.locks.toFinset = S) = [] := by
    apply List.filter_eq_nil_iff.mpr
    intro t ht
    intro eq
    exact h ⟨t, ht, of_decide_eq_true eq⟩
  simp [tableCount, empty] at positive

/-- Every actual edge occurs in the table: missing rows cannot hide edges. -/
theorem actual_entries_cover (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 9) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative k) :
    ∀ e ∈ H.edges, canonicalType25 (lockVertices W label) e ∈
      (profile25 k).types.map Numeric.EdgeType.locks := by
  intro e he
  let T := lockedLabels (lockVertices W label) e
  have pos : 0 < tableCount (profile25 k) (positionType25 T) := by
    rw [← actual_numeric_count H W label unit degrees edges32 k family T]
    exact Finset.card_pos.mpr ⟨e, Finset.mem_filter.mpr ⟨he, rfl⟩⟩
  obtain ⟨t, ht, same⟩ := exists_entry_of_tableCount_pos _ _ pos
  apply List.mem_map.mpr
  refine ⟨t, ht, ?_⟩
  unfold canonicalType25
  change t.locks = (positionType25 T).sort (· ≤ ·)
  rw [← same, (profile25_entry k t ht).1]

/-- Full table realization on an arbitrary finite ambient vertex type. -/
theorem actual_table_realization (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 6) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 9) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative k) :
    TypeCounting.TableRealization H.edges (canonicalType25 (lockVertices W label)) (profile25 k) where
  unique := (profile25_data k).1.2.2.2.1
  covers := actual_entries_cover H W label unit degrees edges32 k family
  counts := actual_entry_count H W label unit degrees edges32 k family

theorem positionType_eq_canonical (vertices : Fin 6 ↪ Fin 25) :
    TypeCounting.positionType vertices positions25 = canonicalType25 vertices := by
  funext e
  unfold TypeCounting.positionType TypeCounting.positionSignature canonicalType25 positionType25
  congr 2

/-- RealizesProfile connects the actual table, the actual locks, and the actual
zero-based locked positions to the pre-existing numerical profile. -/
theorem realizes_profile_of_representative (H : Simple5Hypergraph (Fin 25)) (W : Finset (Fin 25))
    (label : ↥W ≃ Fin 6) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 9) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative k) :
    TypeCounting.RealizesProfile H (lockVertices W label) positions25 (profile25 k) where
  vertex_count := (profile25_data k).2.1
  valid := (profile25_data k).1
  positions_eq := (profile25_data k).2.2.1
  table := by
    rw [positionType_eq_canonical]
    exact actual_table_realization H W label unit degrees edges32 k family

/-- Structural hypotheses alone produce a true realization of a successful
six-lock numeric profile for every 25-vertex finite goal instance. -/
theorem exists_realized_profile25 (H : Simple5Hypergraph (Fin 25))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
    ∃ k : Fin 9, k ≠ 2 ∧ k ≠ 3 ∧ ∃ vertices : Fin 6 ↪ Fin 25,
      TypeCounting.RealizesProfile H vertices positions25 (profile25 k) := by
  obtain ⟨W, _, degrees, unit, k, hk2, hk3, label, family⟩ :=
    exists_full_labeled_six_good_locks H cover edges32 (by simp)
  exact ⟨k, hk2, hk3, lockVertices W label,
    realizes_profile_of_representative H W label unit degrees edges32 k family⟩

theorem profile25_uncorrected : ∀ k : Fin 9,
    (profile25 k).emptyPairCap = none ∧ (profile25 k).correctionCenters = [] := by
  decide

/-- Reuse the existing exact rational certificates after excluding K6-4. -/
theorem profile25_lt_one (k : Fin 9) (good : k ≠ 3) : Numeric.totalBound (profile25 k) < 1 := by
  rcases k with ⟨k, hk⟩
  interval_cases k
  · exact Numeric.v25_K6_1_lt_one
  · exact Numeric.v25_K6_2_lt_one
  · exact Numeric.v25_K6_3_lt_one
  · exact False.elim (good rfl)
  · exact Numeric.v25_K6_5_lt_one
  · exact Numeric.v25_K6_6_lt_one
  · exact Numeric.v25_K6_7_lt_one
  · exact Numeric.v25_K6_8_lt_one
  · exact Numeric.v25_K6_9_lt_one

/-- The complete structural/numerical interface for the v=25 probability
bridge: true table realization and a proved strict bound, with no corrections. -/
theorem exists_realized_bounded_profile25 (H : Simple5Hypergraph (Fin 25))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
    ∃ p : Numeric.Profile, ∃ vertices : Fin 6 ↪ Fin 25,
      TypeCounting.RealizesProfile H vertices positions25 p ∧
      p.emptyPairCap = none ∧ p.correctionCenters = [] ∧ Numeric.totalBound p < 1 := by
  obtain ⟨k, _, good, vertices, real⟩ := exists_realized_profile25 H cover edges32
  exact ⟨profile25 k, vertices, real, (profile25_uncorrected k).1,
    (profile25_uncorrected k).2, profile25_lt_one k good⟩

end Aris4Math.TraceProfiles

#print axioms Aris4Math.TraceProfiles.actual_recovered_count
#print axioms Aris4Math.TraceProfiles.numeric_counts_match
#print axioms Aris4Math.TraceProfiles.actual_numeric_count
#print axioms Aris4Math.TraceProfiles.actual_entry_count
#print axioms Aris4Math.TraceProfiles.actual_entries_cover
#print axioms Aris4Math.TraceProfiles.realizes_profile_of_representative
#print axioms Aris4Math.TraceProfiles.exists_realized_profile25
#print axioms Aris4Math.TraceProfiles.exists_realized_bounded_profile25
