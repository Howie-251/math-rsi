import Aris4Math.Traces
import Aris4Math.Numeric
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Sort
import Mathlib.Algebra.BigOperators.Fin

/-! Exact aggregation by actual edge types.  In particular, diagonal type
pairs lose one possible second edge; off-diagonal types lose none. -/

open scoped BigOperators

namespace Aris4Math.TypeCounting

def lockSignature {V ι : Type*} [DecidableEq V] [Fintype ι] [DecidableEq ι]
    (vertices : ι ↪ V) (e : Finset V) : Finset ι :=
  Finset.univ.filter fun i => vertices i ∈ e

@[simp] theorem mem_lockSignature {V ι : Type*} [DecidableEq V]
    [Fintype ι] [DecidableEq ι] (vertices : ι ↪ V) (e : Finset V) (i : ι) :
    i ∈ lockSignature vertices e ↔ vertices i ∈ e := by
  simp [lockSignature]

def positionSignature {v : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]
    (vertices positions : ι ↪ Fin v) (e : Finset (Fin v)) : Finset ℕ :=
  (lockSignature vertices e).image fun i => (positions i).val + 1

/-- Canonical list of the one-based positions of the locks in an actual edge. -/
def positionType {v : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]
    (vertices positions : ι ↪ Fin v) (e : Finset (Fin v)) : List ℕ :=
  (positionSignature vertices positions e).sort (· ≤ ·)

variable {α β : Type*} [DecidableEq α] [DecidableEq β]

def fiber (E : Finset α) (classify : α → β) (t : β) : Finset α :=
  E.filter fun e => classify e = t

def multiplicity (E : Finset α) (classify : α → β) (t : β) : ℕ :=
  (fiber E classify t).card

/-- A table describes every actual object exactly once, with its true fiber size. -/
structure TableRealization (E : Finset α) (classify : α → List ℕ)
    (p : Numeric.Profile) : Prop where
  unique : (p.types.map Numeric.EdgeType.locks).Nodup
  covers : ∀ e ∈ E, classify e ∈ p.types.map Numeric.EdgeType.locks
  counts : ∀ t ∈ p.types, multiplicity E classify t.locks = t.count

structure RealizesProfile {v : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]
    (H : Simple5Hypergraph (Fin v)) (vertices positions : ι ↪ Fin v)
    (p : Numeric.Profile) (edgeCount : ℕ := 32) : Prop where
  vertex_count : p.v = v
  valid : Numeric.validProfile p edgeCount
  positions_eq : p.positions.toFinset = Finset.univ.image (fun i => (positions i).val + 1)
  table : TableRealization H.edges (positionType vertices positions) p

/-- This is an exact count of actual distinct ordered objects. -/
theorem pair_fiber_card (E : Finset α) (classify : α → β) (t u : β) :
    (E.offDiag.filter fun p => classify p.1 = t ∧ classify p.2 = u).card =
      multiplicity E classify t * (multiplicity E classify u - if t = u then 1 else 0) := by
  by_cases htu : t = u
  · subst u
    have he : (E.offDiag.filter fun p => classify p.1 = t ∧ classify p.2 = t) =
        (fiber E classify t).offDiag := by
      ext p
      simp [fiber, Finset.mem_offDiag]
      tauto
    rw [he, Finset.offDiag_card]
    simp [multiplicity, Nat.mul_sub_left_distrib]
  · have he : (E.offDiag.filter fun p => classify p.1 = t ∧ classify p.2 = u) =
        (fiber E classify t) ×ˢ (fiber E classify u) := by
      ext p
      simp only [Finset.mem_filter, Finset.mem_offDiag, Finset.mem_product, fiber]
      constructor
      · rintro ⟨⟨h1,h2,hne⟩, ht, hu⟩
        exact ⟨⟨h1,ht⟩,h2,hu⟩
      · rintro ⟨⟨h1,ht⟩,h2,hu⟩
        refine ⟨⟨h1,h2,?_⟩,ht,hu⟩
        intro heq
        exact htu (ht.symm.trans ((congrArg classify heq).trans hu))
    rw [he, Finset.card_product]
    simp [multiplicity, htu]

omit [DecidableEq α] in
/-- Grouping an actual weighted sum by a covering set of labels. -/
theorem sum_by_type (E : Finset α) (classify : α → β) (types : Finset β)
    (covers : ∀ e ∈ E, classify e ∈ types) (w : β → ℚ) :
    (∑ e ∈ E, w (classify e)) = ∑ t ∈ types, (multiplicity E classify t : ℚ) * w t := by
  calc
    _ = ∑ t ∈ types, ∑ e ∈ E with classify e = t, w (classify e) :=
      (Finset.sum_fiberwise_of_maps_to covers _).symm
    _ = _ := by
      apply Finset.sum_congr rfl
      intro t ht
      simp only [multiplicity, fiber]
      rw [Finset.sum_congr rfl (fun e he => congrArg w (Finset.mem_filter.mp he).2)]
      simp

/-- Double grouping preserves ordered direction and subtracts exactly the
same-edge diagonal, including for a type with zero or one member. -/
theorem pair_sum_by_type (E : Finset α) (classify : α → β) (types : Finset β)
    (covers : ∀ e ∈ E, classify e ∈ types) (w : β → β → ℚ) :
    (∑ p ∈ E.offDiag, w (classify p.1) (classify p.2)) =
      ∑ t ∈ types, ∑ u ∈ types,
        (multiplicity E classify t *
          (multiplicity E classify u - if t = u then 1 else 0) : ℕ) * w t u := by
  have hc : ∀ p ∈ E.offDiag, (classify p.1, classify p.2) ∈ types ×ˢ types := by
    intro p hp
    exact Finset.mem_product.mpr
      ⟨covers _ (Finset.mem_offDiag.mp hp).1, covers _ (Finset.mem_offDiag.mp hp).2.1⟩
  have h := sum_by_type E.offDiag (fun p => (classify p.1, classify p.2))
    (types ×ˢ types) hc (fun p => w p.1 p.2)
  rw [Finset.sum_product] at h
  apply h.trans
  apply Finset.sum_congr rfl
  intro t ht
  apply Finset.sum_congr rfl
  intro u hu
  congr 1
  unfold multiplicity fiber
  simp only [Prod.mk.injEq]
  exact_mod_cast pair_fiber_card E classify t u

theorem qsum_eq_sum (xs : List ℚ) : Numeric.qsum xs = xs.sum :=
  List.sum_eq_foldl.symm

theorem totalBound_eq_sum (p : Numeric.Profile) :
    Numeric.totalBound p = ∑ k : Fin p.v, Numeric.positionBound p (k.val + 1) := by
  rw [Numeric.totalBound, qsum_eq_sum, ← List.sum_toFinset _ (List.nodup_range (n := p.v))]
  have hr : (List.range p.v).toFinset = Finset.range p.v := by
    ext i
    simp
  rw [hr]
  exact Finset.sum_range (n := p.v) (fun i => Numeric.positionBound p (i + 1))

theorem totalBound_eq_sum_of_eq (p : Numeric.Profile) (v : ℕ) (hv : p.v = v) :
    Numeric.totalBound p = ∑ k : Fin v, Numeric.positionBound p (k.val + 1) := by
  subst v
  exact totalBound_eq_sum p

omit [DecidableEq α] in
/-- The list used by the arithmetic certificate has exactly the true
multiplicities, rather than independently stipulated coefficients. -/
theorem sum_by_table (E : Finset α) (classify : α → List ℕ) (p : Numeric.Profile)
    (real : TableRealization E classify p) (w : List ℕ → ℚ) :
    (∑ e ∈ E, w (classify e)) =
      Numeric.qsum (p.types.map fun t => (t.count : ℚ) * w t.locks) := by
  rw [sum_by_type E classify (p.types.map Numeric.EdgeType.locks).toFinset
    (fun e he => List.mem_toFinset.mpr (real.covers e he)),
    List.sum_toFinset _ real.unique, List.map_map, qsum_eq_sum]
  congr 1
  apply List.map_congr_left
  intro t ht
  simp only [Function.comp_def, real.counts t ht]

/-- The corresponding two-variable table formula counts actual ordered pairs. -/
theorem pair_sum_by_table (E : Finset α) (classify : α → List ℕ) (p : Numeric.Profile)
    (real : TableRealization E classify p) (w : List ℕ → List ℕ → ℚ) :
    (∑ e ∈ E.offDiag, w (classify e.1) (classify e.2)) =
      Numeric.qsum (p.types.flatMap fun t => p.types.map fun u =>
        (t.count * (u.count - if t.locks = u.locks then 1 else 0) : ℕ) * w t.locks u.locks) := by
  rw [pair_sum_by_type E classify (p.types.map Numeric.EdgeType.locks).toFinset
    (fun e he => List.mem_toFinset.mpr (real.covers e he)),
    List.sum_toFinset _ real.unique, List.map_map, qsum_eq_sum]
  simp_rw [List.sum_toFinset _ real.unique, List.map_map]
  have hs : ∀ xs : List Numeric.EdgeType,
      (xs.flatMap fun t => p.types.map fun u =>
        (t.count * (u.count - if t.locks = u.locks then 1 else 0) : ℕ) * w t.locks u.locks).sum =
      (xs.map fun t => (p.types.map fun u =>
        (t.count * (u.count - if t.locks = u.locks then 1 else 0) : ℕ) * w t.locks u.locks).sum).sum := by
    intro xs
    induction xs with
    | nil => simp
    | cons a xs ih => simp only [List.flatMap_cons, List.sum_append, List.map_cons,
        List.sum_cons, ih]
  rw [hs]
  simp only [Function.comp_def]
  apply congrArg List.sum
  apply List.map_congr_left
  intro t ht
  apply congrArg List.sum
  apply List.map_congr_left
  intro u hu
  simp only [real.counts t ht, real.counts u hu]

omit [DecidableEq α] in
/-- Aggregation into Numeric A or B. Single-edge event semantics are supplied
by a separate exact probability theorem; no counting assumptions remain here. -/
theorem edge_sum_numeric (E : Finset α) (classify : α → List ℕ) (p : Numeric.Profile)
    (real : TableRealization E classify p) (k : ℕ) (last : Bool) :
    (∑ e ∈ E, Numeric.edgeWeight p ⟨classify e, 0⟩ k last) =
      if last then Numeric.boundA p k else Numeric.boundB p k := by
  rw [sum_by_table E classify p real (fun t => Numeric.edgeWeight p ⟨t, 0⟩ k last)]
  cases last <;> rfl

/-- Aggregation into Numeric C in the ordinary no-cap case. The special
v20 cap is proved separately using actual single-intersection pairs. -/
theorem pair_sum_numeric (E : Finset α) (classify : α → List ℕ) (p : Numeric.Profile)
    (real : TableRealization E classify p) (noCap : p.emptyPairCap = none) (k : ℕ) :
    (∑ e ∈ E.offDiag, Numeric.pairWeight p ⟨classify e.1, 0⟩ ⟨classify e.2, 0⟩ k) =
      Numeric.boundC p k := by
  rw [pair_sum_by_table E classify p real
    (fun t u => Numeric.pairWeight p ⟨t, 0⟩ ⟨u, 0⟩ k)]
  unfold Numeric.boundC
  congr 1
  apply List.flatMap_congr
  intro t ht
  apply List.map_congr_left
  intro u hu
  simp only [Numeric.pairCount, noCap, Option.getD_none, ite_self]
  rfl

end Aris4Math.TypeCounting

#print axioms Aris4Math.TypeCounting.pair_fiber_card
#print axioms Aris4Math.TypeCounting.sum_by_type
#print axioms Aris4Math.TypeCounting.pair_sum_by_type
#print axioms Aris4Math.TypeCounting.edge_sum_numeric
#print axioms Aris4Math.TypeCounting.pair_sum_numeric
