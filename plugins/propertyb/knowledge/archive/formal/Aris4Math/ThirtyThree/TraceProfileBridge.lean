import Aris4Math.TraceRecovery
import Aris4Math.TraceProfiles

/-! Common actual-input bridge for the new six- and eight-lock tables.
The total edge count is 33; actual type counts come from TraceRecovery. -/

namespace Aris4Math.ThirtyThree.TraceProfileBridge

open Aris4Math.TypeCounting Aris4Math.TraceRecovery
open Aris4Math.TraceProfiles (tableCount exists_entry_of_tableCount_pos)

def encode {n v : ℕ} (positions : Fin n ↪ Fin v) (T : Finset (Fin n)) : Finset ℕ :=
  T.image fun i => (positions i).val + 1

def decode {n v : ℕ} (positions : Fin n ↪ Fin v) (S : Finset ℕ) : Finset (Fin n) :=
  Finset.univ.filter fun i => (positions i).val + 1 ∈ S

theorem encode_injective {n v : ℕ} (positions : Fin n ↪ Fin v) :
    Function.Injective (encode positions) := by
  apply Finset.image_injective
  intro i j h
  exact positions.injective (Fin.ext (Nat.add_right_cancel h))

/-- A finite table row has canonical position labels, an inverse label subset,
and a lookup equal to its stored count. Closed tables establish this by kernel
computation; arbitrary hypergraph counts are derived separately below. -/
def RowData {n v : ℕ} (positions : Fin n ↪ Fin v) (p : Numeric.Profile) : Prop :=
  ∀ t ∈ p.types,
    t.locks.toFinset.sort (· ≤ ·) = t.locks ∧
    encode positions (decode positions t.locks.toFinset) = t.locks.toFinset ∧
    tableCount p t.locks.toFinset = t.count

instance {n v : ℕ} (positions : Fin n ↪ Fin v) (p : Numeric.Profile) :
    Decidable (RowData positions p) := by unfold RowData; infer_instance

/-- Computable row certificate; the canonical sort equality follows from
nodup and the displayed increasing order, rather than evaluating Finset.sort. -/
def RowCertificate {n v : ℕ} (positions : Fin n ↪ Fin v) (p : Numeric.Profile) : Prop :=
  ∀ t ∈ p.types,
    t.locks.Nodup ∧ t.locks.Pairwise (· ≤ ·) ∧
    encode positions (decode positions t.locks.toFinset) = t.locks.toFinset ∧
    tableCount p t.locks.toFinset = t.count

instance {n v : ℕ} (positions : Fin n ↪ Fin v) (p : Numeric.Profile) :
    Decidable (RowCertificate positions p) := by unfold RowCertificate; infer_instance

theorem rowData_of_certificate {n v : ℕ} (positions : Fin n ↪ Fin v)
    (p : Numeric.Profile) (h : RowCertificate positions p) : RowData positions p := by
  intro t ht
  obtain ⟨nodup,sorted,encoded,count⟩ := h t ht
  exact ⟨(List.toFinset_sort (· ≤ ·) nodup).mpr sorted,encoded,count⟩

/-- All entry counts and table coverage are constructed from the original H.
No realization or arbitrary actual-type certificate is an input. -/
theorem realizes_of_recovered_counts {n v : ℕ}
    (H : Simple5Hypergraph (Fin v)) (W : Finset (Fin v)) (label : ↥W ≃ Fin n)
    (unit : H.UnitCodegrees W) (degrees : ∀ x ∈ W, H.degree x = 6)
    (edges33 : H.edges.card = 33)
    (blocks : Finset (Finset (Fin n)))
    (family : (H.multiTraces W).image (labelBlock W label) = blocks)
    (positions : Fin n ↪ Fin v) (p : Numeric.Profile)
    (valid : Numeric.validProfile p 33) (vertices_eq : p.v = v)
    (positions_eq : p.positions.toFinset = Finset.univ.image (fun i => (positions i).val+1))
    (rows : RowData positions p)
    (numeric_counts : ∀ T : Finset (Fin n),
      recoveredCount 33 6 blocks T = tableCount p (encode positions T)) :
    RealizesProfile H (lockVertices W label) positions p 33 := by
  let vertices := lockVertices W label
  let classify := positionType vertices positions
  have actual (T : Finset (Fin n)) :
      (H.edges.filter fun e => lockedLabels vertices e = T).card =
        tableCount p (encode positions T) := by
    rw [actual_recovered_count H W label unit 6 degrees, edges33, family]
    exact numeric_counts T
  have type_eq (e : Finset (Fin v)) :
      classify e = (encode positions (lockedLabels vertices e)).sort (· ≤ ·) := rfl
  have eq_iff (e : Finset (Fin v)) (t : Numeric.EdgeType) (ht : t ∈ p.types) :
      classify e = t.locks ↔ lockedLabels vertices e = decode positions t.locks.toFinset := by
    obtain ⟨sorted, encoded, _⟩ := rows t ht
    constructor
    · intro h
      have eq := congrArg List.toFinset h
      rw [type_eq, Finset.sort_toFinset] at eq
      exact encode_injective positions (eq.trans encoded.symm)
    · intro h
      rw [type_eq, h, encoded, sorted]
  refine ⟨vertices_eq, valid, positions_eq, ?_⟩
  constructor
  · exact valid.2.2.2.1
  · intro e he
    have pos : 0 < tableCount p (encode positions (lockedLabels vertices e)) := by
      rw [← actual]
      exact Finset.card_pos.mpr ⟨e,Finset.mem_filter.mpr ⟨he,rfl⟩⟩
    obtain ⟨t,ht,same⟩ := exists_entry_of_tableCount_pos _ _ pos
    apply List.mem_map.mpr
    refine ⟨t,ht,?_⟩
    change t.locks = classify e
    rw [type_eq, ← same, (rows t ht).1]
  · intro t ht
    unfold multiplicity fiber
    have filter_eq : H.edges.filter (fun e => classify e = t.locks) =
        H.edges.filter (fun e => lockedLabels vertices e = decode positions t.locks.toFinset) := by
      apply Finset.filter_congr
      intro e _
      exact eq_iff e t ht
    change (H.edges.filter (fun e => classify e = t.locks)).card = t.count
    rw [filter_eq, actual, (rows t ht).2.1, (rows t ht).2.2]

end Aris4Math.ThirtyThree.TraceProfileBridge

#print axioms Aris4Math.ThirtyThree.TraceProfileBridge.realizes_of_recovered_counts
