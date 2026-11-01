import Aris4Math.TraceRecovery
import Aris4Math.TraceProfiles

/-! Actual four-lock labels and exact numerical profiles for v=24. -/

open scoped BigOperators

namespace Aris4Math.K4Profiles

open BlockClassification K6Classification TraceRecovery
open K6Traces (onGround onGround_card)
open TraceProfiles (tableCount exists_entry_of_tableCount_pos)

variable {V : Type*} [DecidableEq V]

def representative4 (k : Fin 3) : Finset (Finset (Fin 4)) :=
  match k.val with
  | 0 => ∅
  | 1 => {{0, 1, 2}}
  | _ => {Finset.univ}

def fullRepresentative4 (k : Fin 3) : Finset (Finset (Fin 4)) :=
  pairCompletion (representative4 k)

/-- Label the unique triple in a four-point set by the first three labels. -/
theorem label_triple (W B : Finset V) (four : W.card = 4) (sub : B ⊆ W) (three : B.card = 3) :
    ∃ label : ↥W ≃ Fin 4, labelBlock W label B = {0, 1, 2} := by
  let actual : Unit → Finset ↥W := fun _ => onGround W B
  let model : Unit → Finset (Fin 4) := fun _ => {0, 1, 2}
  have smallA (x : W) : (signature actual x).card ≤ 2 :=
    (Finset.card_le_univ _).trans (by decide)
  have smallB (x : Fin 4) : (signature model x).card ≤ 2 :=
    (Finset.card_le_univ _).trans (by decide)
  have single : ∀ i, (actual i).card = (model i).card := by
    intro i
    simp [actual, model, onGround_card W B sub, three]
  obtain ⟨label, hl⟩ := exists_equiv_map_blocks actual model smallA smallB
    (by simpa using four) single
    (fun i j h => False.elim (h (Subsingleton.elim i j)))
  exact ⟨label, hl ()⟩

/-- The paper's three K4 cases acquire explicit labels on the actual lock set. -/
theorem classify_four_labels (H : Simple5Hypergraph V) (W : Finset V)
    (four : W.card = 4) (unit : H.UnitCodegrees W) :
    ∃ k : Fin 3, ∃ label : ↥W ≃ Fin 4,
      (H.multiTraces W).image (labelBlock W label) = fullRepresentative4 k := by
  have anyLabel : Nonempty (↥W ≃ Fin 4) :=
    ⟨Fintype.equivOfCardEq (by simpa using four)⟩
  rcases H.classify_four_lock_traces W unit four with pairs | triple | full
  · let label := Classical.choice anyLabel
    refine ⟨0, label, ?_⟩
    rw [labeled_traces_recovered H W unit label]
    have empty : largeBlocks (H.multiTraces W) = ∅ := by
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro B hB
      rcases Finset.mem_filter.mp hB with ⟨hB, big⟩
      rw [pairs] at hB
      have size := (Finset.mem_powersetCard.mp hB).2
      omega
    simp [empty, fullRepresentative4, representative4]
  · obtain ⟨B, sub, three, family⟩ := triple
    obtain ⟨label, labeledB⟩ := label_triple W B four sub three
    refine ⟨1, label, ?_⟩
    rw [labeled_traces_recovered H W unit label]
    have large : largeBlocks (H.multiTraces W) = {B} := by
      ext C
      simp only [largeBlocks, Finset.mem_filter, Finset.mem_singleton]
      constructor
      · rintro ⟨hC, big⟩
        rw [family] at hC
        rcases Finset.mem_insert.mp hC with eq | pair
        · exact eq
        · have size := (Finset.mem_powersetCard.mp (Finset.mem_filter.mp pair).1).2
          omega
      · rintro rfl
        exact ⟨by simp [family], by omega⟩
    simp [large, labeledB, fullRepresentative4, representative4]
  · let label := Classical.choice anyLabel
    refine ⟨2, label, ?_⟩
    rw [labeled_traces_recovered H W unit label]
    have large : largeBlocks (H.multiTraces W) = {W} := by
      simp [largeBlocks, full, four]
    have labeledW : labelBlock W label W = Finset.univ := by
      ext i
      simp
    simp [large, labeledW, fullRepresentative4, representative4]

def profile24 (k : Fin 3) : Numeric.Profile :=
  match k.val with
  | 0 => Numeric.v24_K4_1
  | 1 => Numeric.v24_K4_2
  | _ => Numeric.v24_K4_3

def numericPosition24 (i : Fin 4) : Nat := i.val + 11

def positionType24 (T : Finset (Fin 4)) : Finset Nat := T.image numericPosition24

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- Fixed-table equality; actual multiplicities are established analytically. -/
theorem numeric_counts_match : ∀ k : Fin 3, ∀ T : Finset (Fin 4),
    recoveredCount 32 6 (fullRepresentative4 k) T = tableCount (profile24 k) (positionType24 T) := by
  decide +kernel

/-- The true edge-fiber count is exactly the Numeric table entry for that set
of one-based locked positions. The labeled family is a structural equality. -/
theorem actual_numeric_count (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 4) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 3) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative4 k)
    (T : Finset (Fin 4)) :
    (H.edges.filter (fun e => lockedLabels (lockVertices W label) e = T)).card =
      tableCount (profile24 k) (positionType24 T) := by
  rw [actual_recovered_count H W label unit 6 degrees, edges32, family]
  exact numeric_counts_match k T

/-- The four fixed permutation positions, zero-based for the event modules. -/
def positions24 : Fin 4 ↪ Fin 24 where
  toFun i := ⟨i.val + 10, by omega⟩
  inj' := by
    intro i j h
    apply Fin.ext
    have he := congrArg Fin.val h
    change i.val + 10 = j.val + 10 at he
    omega

def decode24 (S : Finset Nat) : Finset (Fin 4) :=
  Finset.univ.filter (fun i => numericPosition24 i ∈ S)

theorem positionType24_injective : Function.Injective positionType24 := by
  apply Finset.image_injective
  intro i j h
  apply Fin.ext
  dsimp [numericPosition24] at h
  omega

/-- Canonical position lists for a possibly non-Fin ambient vertex type. -/
def canonicalType24 (vertices : Fin 4 ↪ V) (e : Finset V) : List Nat :=
  (positionType24 (lockedLabels vertices e)).sort (· ≤ ·)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem profile24_data : ∀ k : Fin 3,
    Numeric.validProfile (profile24 k) ∧ (profile24 k).v = 24 ∧
    (profile24 k).positions.toFinset = Finset.univ.image (fun i => (positions24 i).val + 1) ∧
    ((profile24 k).types.all (fun t => decide (
      t.locks.Nodup ∧ t.locks.Pairwise (· ≤ ·) ∧
      positionType24 (decode24 t.locks.toFinset) = t.locks.toFinset ∧
      tableCount (profile24 k) t.locks.toFinset = t.count))) := by
  unfold Numeric.validProfile
  decide +kernel

theorem profile24_entry (k : Fin 3) (t : Numeric.EdgeType) (ht : t ∈ (profile24 k).types) :
    t.locks.toFinset.sort (· ≤ ·) = t.locks ∧
      positionType24 (decode24 t.locks.toFinset) = t.locks.toFinset ∧
      tableCount (profile24 k) t.locks.toFinset = t.count := by
  have h := List.all_eq_true.mp (profile24_data k).2.2.2 t ht
  rcases of_decide_eq_true h with ⟨nodup, sorted, encoded, count⟩
  exact ⟨(List.toFinset_sort (· ≤ ·) nodup).mpr sorted, encoded, count⟩

theorem canonicalType24_eq_iff (vertices : Fin 4 ↪ V) (e : Finset V)
    (k : Fin 3) (t : Numeric.EdgeType) (ht : t ∈ (profile24 k).types) :
    canonicalType24 vertices e = t.locks ↔
      lockedLabels vertices e = decode24 t.locks.toFinset := by
  have data := profile24_entry k t ht
  constructor
  · intro h
    have eq := congrArg List.toFinset h
    simp only [canonicalType24, Finset.sort_toFinset] at eq
    exact positionType24_injective (eq.trans data.2.1.symm)
  · intro h
    unfold canonicalType24
    rw [h, data.2.1, data.1]

/-- Every row in the numerical list is proved to have its stated actual fiber
size; no type-count row is introduced as an assumption. -/
theorem actual_entry_count (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 4) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 3) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative4 k)
    (t : Numeric.EdgeType) (ht : t ∈ (profile24 k).types) :
    TypeCounting.multiplicity H.edges (canonicalType24 (lockVertices W label)) t.locks = t.count := by
  unfold TypeCounting.multiplicity TypeCounting.fiber
  have eq : H.edges.filter (fun e => canonicalType24 (lockVertices W label) e = t.locks) =
      H.edges.filter (fun e => lockedLabels (lockVertices W label) e = decode24 t.locks.toFinset) := by
    apply Finset.filter_congr
    intro e _
    exact canonicalType24_eq_iff _ e k t ht
  rw [eq, actual_numeric_count H W label unit degrees edges32 k family]
  have data := profile24_entry k t ht
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
    (label : ↥W ≃ Fin 4) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 3) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative4 k) :
    ∀ e ∈ H.edges, canonicalType24 (lockVertices W label) e ∈
      (profile24 k).types.map Numeric.EdgeType.locks := by
  intro e he
  let T := lockedLabels (lockVertices W label) e
  have pos : 0 < tableCount (profile24 k) (positionType24 T) := by
    rw [← actual_numeric_count H W label unit degrees edges32 k family T]
    exact Finset.card_pos.mpr ⟨e, Finset.mem_filter.mpr ⟨he, rfl⟩⟩
  obtain ⟨t, ht, same⟩ := exists_entry_of_tableCount_pos _ _ pos
  apply List.mem_map.mpr
  refine ⟨t, ht, ?_⟩
  unfold canonicalType24
  change t.locks = (positionType24 T).sort (· ≤ ·)
  rw [← same, (profile24_entry k t ht).1]

/-- Full table realization on an arbitrary finite ambient vertex type. -/
theorem actual_table_realization (H : Simple5Hypergraph V) (W : Finset V)
    (label : ↥W ≃ Fin 4) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 3) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative4 k) :
    TypeCounting.TableRealization H.edges (canonicalType24 (lockVertices W label)) (profile24 k) where
  unique := (profile24_data k).1.2.2.2.1
  covers := actual_entries_cover H W label unit degrees edges32 k family
  counts := actual_entry_count H W label unit degrees edges32 k family

theorem positionType_eq_canonical (vertices : Fin 4 ↪ Fin 24) :
    TypeCounting.positionType vertices positions24 = canonicalType24 vertices := by
  funext e
  unfold TypeCounting.positionType TypeCounting.positionSignature canonicalType24 positionType24
  congr 2

/-- RealizesProfile connects the actual table, the actual locks, and the actual
zero-based locked positions to the pre-existing numerical profile. -/
theorem realizes_profile_of_representative (H : Simple5Hypergraph (Fin 24)) (W : Finset (Fin 24))
    (label : ↥W ≃ Fin 4) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6) (edges32 : H.edges.card = 32)
    (k : Fin 3) (family : (H.multiTraces W).image (labelBlock W label) = fullRepresentative4 k) :
    TypeCounting.RealizesProfile H (lockVertices W label) positions24 (profile24 k) where
  vertex_count := (profile24_data k).2.1
  valid := (profile24_data k).1
  positions_eq := (profile24_data k).2.2.1
  table := by
    rw [positionType_eq_canonical]
    exact actual_table_realization H W label unit degrees edges32 k family

/-- Every actual 24-vertex finite goal instance admits a real four-lock profile. -/
theorem exists_realized_profile24 (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
    ∃ k : Fin 3, ∃ vertices : Fin 4 ↪ Fin 24,
      TypeCounting.RealizesProfile H vertices positions24 (profile24 k) := by
  obtain ⟨W, four, degrees, unit⟩ := H.exists_four_six_degree_codegree_one cover edges32 (by simp)
  obtain ⟨k, label, family⟩ := classify_four_labels H W four unit
  exact ⟨k, lockVertices W label,
    realizes_profile_of_representative H W label unit degrees edges32 k family⟩

theorem profile24_uncorrected : ∀ k : Fin 3,
    (profile24 k).emptyPairCap = none ∧ (profile24 k).correctionCenters = [] := by
  decide

theorem profile24_lt_one (k : Fin 3) : Numeric.totalBound (profile24 k) < 1 := by
  rcases k with ⟨k, hk⟩
  interval_cases k
  · exact Numeric.v24_K4_1_lt_one
  · exact Numeric.v24_K4_2_lt_one
  · exact Numeric.v24_K4_3_lt_one

/-- The full true-table/numerical interface for the v=24 probability bridge. -/
theorem exists_realized_bounded_profile24 (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
    ∃ p : Numeric.Profile, ∃ vertices : Fin 4 ↪ Fin 24,
      TypeCounting.RealizesProfile H vertices positions24 p ∧
      p.emptyPairCap = none ∧ p.correctionCenters = [] ∧ Numeric.totalBound p < 1 := by
  obtain ⟨k, vertices, real⟩ := exists_realized_profile24 H cover edges32
  exact ⟨profile24 k, vertices, real, (profile24_uncorrected k).1,
    (profile24_uncorrected k).2, profile24_lt_one k⟩

end Aris4Math.K4Profiles

#print axioms Aris4Math.K4Profiles.classify_four_labels
#print axioms Aris4Math.K4Profiles.numeric_counts_match
#print axioms Aris4Math.K4Profiles.actual_numeric_count
#print axioms Aris4Math.K4Profiles.actual_entry_count
#print axioms Aris4Math.K4Profiles.actual_entries_cover
#print axioms Aris4Math.K4Profiles.exists_realized_profile24
#print axioms Aris4Math.K4Profiles.exists_realized_bounded_profile24
