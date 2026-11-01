import Aris4Math.LinkWeightCertificates

/-! Convert corrections at real locked centers into one actual deletion set
per position. This module contains no endpoint or pair-probability hypotheses. -/

open scoped BigOperators

namespace Aris4Math.ProfileDeletion

open Aris4Math.Numeric Aris4Math.TypeCounting Aris4Math.LinkDeletion
open Aris4Math.LinkWeightCertificates

variable {v : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- At a correction position, delete exactly the actual bad pairs through its
unique locked vertex, with both ordered directions. -/
def correctionDeleted (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Profile) (k : Fin v) :
    Finset (Finset (Fin v) × Finset (Fin v)) :=
  Finset.univ.biUnion fun j =>
    if positions j = k ∧ k.val + 1 ∈ p.correctionCenters then
      directedBadPairs H (vertices j)
    else ∅

omit [DecidableEq ι] in
theorem correctionDeleted_at (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Profile) (j : ι)
    (hc : (positions j).val + 1 ∈ p.correctionCenters) :
    correctionDeleted H vertices positions p (positions j) =
      directedBadPairs H (vertices j) := by
  ext d
  simp only [correctionDeleted, Finset.mem_biUnion, Finset.mem_univ, true_and]
  constructor
  · rintro ⟨i, hi⟩
    by_cases h : positions i = positions j ∧ (positions j).val + 1 ∈ p.correctionCenters
    · rw [if_pos h] at hi
      have hij := positions.injective h.1
      simpa only [hij] using hi
    · simp only [if_neg h, Finset.notMem_empty] at hi
  · intro hd
    exact ⟨j, by simpa only [eq_self, true_and, if_pos hc] using hd⟩

omit [DecidableEq ι] in
theorem correctionDeleted_empty (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Profile) (k : Fin v)
    (hc : k.val + 1 ∉ p.correctionCenters) :
    correctionDeleted H vertices positions p k = ∅ := by
  ext d
  simp [correctionDeleted, hc]

omit [DecidableEq ι] in
theorem correctionDeleted_subset (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Profile) (k : Fin v) :
    correctionDeleted H vertices positions p k ⊆ H.edges.offDiag := by
  intro d hd
  obtain ⟨j, _, hj⟩ := Finset.mem_biUnion.mp hd
  by_cases h : positions j = k ∧ k.val + 1 ∈ p.correctionCenters
  · rw [if_pos h] at hj
    exact directed_bad_subset H (vertices j) hj
  · simp only [if_neg h, Finset.notMem_empty] at hj

omit [DecidableEq ι] in
theorem correctionDeleted_bad (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Profile) (k : Fin v)
    (d : Finset (Fin v) × Finset (Fin v))
    (hd : d ∈ correctionDeleted H vertices positions p k) : (d.1 ∩ d.2).card ≠ 1 := by
  obtain ⟨j, _, hj⟩ := Finset.mem_biUnion.mp hd
  by_cases h : positions j = k ∧ k.val + 1 ∈ p.correctionCenters
  · rw [if_pos h] at hj
    exact directed_bad_intersection H (vertices j) d hj
  · simp only [if_neg h, Finset.notMem_empty] at hj

theorem correction_is_locked (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Profile)
    (real : RealizesProfile H vertices positions p) (k : Fin v)
    (hc : k.val + 1 ∈ p.correctionCenters) : ∃ j, positions j = k := by
  have corr : ∀ n ∈ p.correctionCenters, n ∈ p.positions := by
    simpa only [List.all_eq_true, decide_eq_true_eq] using real.valid.2.2.2.2.2.2.1
  have hpos := List.mem_toFinset.mpr (corr _ hc)
  rw [real.positions_eq] at hpos
  obtain ⟨j, _, hj⟩ := Finset.mem_image.mp hpos
  exact ⟨j, Fin.ext (Nat.add_right_cancel hj)⟩

/-- It suffices to prove the local deletion inequality once for every actual
locked correction center. Noncorrection positions have zero deduction and an
empty deletion set. -/
theorem all_position_deletion_lower (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Profile)
    (real : RealizesProfile H vertices positions p)
    (center_lower : ∀ j, (positions j).val + 1 ∈ p.correctionCenters →
      deduction p ((positions j).val + 1) ≤
        ∑ d ∈ directedBadPairs H (vertices j),
          typeWeight p (positionType vertices positions) ((positions j).val + 1) d) :
    ∀ k : Fin v, deduction p (k.val + 1) ≤
      ∑ d ∈ correctionDeleted H vertices positions p k,
        typeWeight p (positionType vertices positions) (k.val + 1) d := by
  intro k
  by_cases hc : k.val + 1 ∈ p.correctionCenters
  · obtain ⟨j,hj⟩ := correction_is_locked H vertices positions p real k hc
    subst k
    rw [correctionDeleted_at H vertices positions p j hc]
    exact center_lower j hc
  · rw [correctionDeleted_empty H vertices positions p k hc]
    simp only [deduction, if_neg hc, Finset.sum_empty, le_refl]

end Aris4Math.ProfileDeletion

#print axioms Aris4Math.ProfileDeletion.correctionDeleted_at
#print axioms Aris4Math.ProfileDeletion.correctionDeleted_subset
#print axioms Aris4Math.ProfileDeletion.correctionDeleted_bad
#print axioms Aris4Math.ProfileDeletion.all_position_deletion_lower
