import Aris4Math.ThirtyThree.AvoidedLink
import Aris4Math.ThirtyThree.TwentyOneDeletion
import Aris4Math.ThirtyThree.CustomDeletion

/-! Overlapping avoided-lock quotas combined by a finite nonnegative dual.
The penalty is charged on all actual incident edge pairs before aggregation by
their realized types, retaining the exact diagonal capacities. -/
namespace Aris4Math.ThirtyThree.RefinedDeletion

open scoped BigOperators
open Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.TwentyOneDeletion Aris4Math.ThirtyThree.AvoidedLink

variable {V : Type*} [Fintype V] [DecidableEq V]
variable {ι : Type*} [Fintype ι]

def quotaWeight (P : ι → Finset (Finset V)) (a : ι → ℚ)
    (p : Finset (Finset V)) : ℚ :=
  ∑ i, if p ⊆ P i then a i else 0

def dualPenalty (P : ι → Finset (Finset V)) (a : ι → ℚ)
    (w : Finset V × Finset V → ℚ) (z : Finset V × Finset V) : ℚ :=
  max 0 (quotaWeight P a {z.1, z.2} - (w z + w (z.2,z.1))) / 2

omit [Fintype V] in
theorem dualPenalty_nonneg (P : ι → Finset (Finset V)) (a : ι → ℚ)
    (w : Finset V × Finset V → ℚ) (z : Finset V × Finset V) :
    0 ≤ dualPenalty P a w z :=
  div_nonneg (le_max_left _ _) (by norm_num)

omit [Fintype V] in
theorem unordered_dual_penalty (P : ι → Finset (Finset V)) (a : ι → ℚ)
    (w : Finset V × Finset V → ℚ) (e f : Finset V) (hne : e ≠ f) :
    quotaWeight P a {e,f} ≤ unorderedWeight w {e,f} +
      unorderedWeight (dualPenalty P a w) {e,f} := by
  rw [unorderedWeight_pair w e f hne,
    unorderedWeight_pair (dualPenalty P a w) e f hne]
  simp only [dualPenalty, Finset.pair_comm f e]
  rw [add_comm (w (f,e)) (w (e,f))]
  have h := le_max_right (0 : ℚ) (quotaWeight P a {e,f} - (w (e,f) + w (f,e)))
  linarith

/-- Arbitrarily many overlapping subquotas are paid by the same actual bad
pairs. The half-penalty in each direction prevents double charging. -/
theorem dual_bad_weight_lower (H : Simple5Hypergraph V) (x : V)
    (P : ι → Finset (Finset V)) (a : ι → ℚ) (q : ι → ℕ)
    (w : Finset V × Finset V → ℚ) (ha : ∀ i, 0 ≤ a i)
    (hq : ∀ i, q i ≤ ((H.badLinkPairs x).filter fun p => p ⊆ P i).card) :
    (∑ i, (q i : ℚ) * a i) -
      (∑ z ∈ (H.incidentEdges x).offDiag, dualPenalty P a w z) ≤
      ∑ z ∈ directedBadPairs H x, w z := by
  classical
  have hquota : (∑ i, (q i : ℚ) * a i) ≤
      ∑ p ∈ H.badLinkPairs x, quotaWeight P a p := by
    unfold quotaWeight
    rw [Finset.sum_comm]
    apply Finset.sum_le_sum
    intro i _
    rw [← Finset.sum_filter]
    simp only [Finset.sum_const, nsmul_eq_mul]
    exact mul_le_mul_of_nonneg_right (by exact_mod_cast hq i) (ha i)
  have each : ∀ p ∈ H.badLinkPairs x,
      quotaWeight P a p ≤ unorderedWeight w p + unorderedWeight (dualPenalty P a w) p := by
    intro p hp
    obtain ⟨e,f,hne,rfl⟩ := Finset.card_eq_two.mp (badPair_card H x p hp)
    exact unordered_dual_penalty P a w e f hne
  have hs := Finset.sum_le_sum each
  rw [Finset.sum_add_distrib, ← directed_bad_sum, ← directed_bad_sum] at hs
  have hp := Finset.sum_le_sum_of_subset_of_nonneg (directed_bad_subset_incident H x)
    (fun z _ _ => dualPenalty_nonneg P a w z)
  linarith

/-- All quota assumptions in the general dual inequality now come from the
actual edge families of H; only the chosen nonnegative multipliers remain. -/
theorem avoided_dual_lower (H : Simple5Hypergraph V) (x : V)
    (R : ι → Finset V) (a : ι → ℚ) (q : ι → ℕ)
    (w : Finset V × Finset V → ℚ) (ha : ∀ i, 0 ≤ a i)
    (hx : ∀ i, x ∉ R i)
    (hq : ∀ i, q i ≤
      (4 * (avoidedEdges H x (R i)).card + 2 - (Fintype.card V - 1 - (R i).card)) / 3) :
    (∑ i, (q i : ℚ) * a i) -
      (∑ z ∈ (H.incidentEdges x).offDiag,
        dualPenalty (fun i => avoidedEdges H x (R i)) a w z) ≤
      ∑ z ∈ directedBadPairs H x, w z := by
  apply dual_bad_weight_lower H x _ a q w ha
  intro i
  exact (hq i).trans (avoided_bad_pair_lower H x (R i) (hx i))

variable {v s edgeCount : ℕ}

def avoidedPositions (positions : Fin s ↪ Fin v) (R : Finset (Fin s)) : Finset ℕ :=
  R.image fun i => (positions i).val + 1

theorem disjoint_positionType (vertices positions : Fin s ↪ Fin v)
    (R : Finset (Fin s)) (e : Finset (Fin v)) :
    Disjoint e (R.image vertices) ↔
      Disjoint (positionType vertices positions e).toFinset (avoidedPositions positions R) := by
  constructor
  · intro h
    apply Finset.disjoint_left.mpr
    intro k hk hR
    obtain ⟨i, hi, hik⟩ := Finset.mem_image.mp hR
    subst k
    have hie := (center_mem_positionType vertices positions e i).mp
      (List.mem_toFinset.mp hk)
    exact Finset.disjoint_left.mp h hie (Finset.mem_image.mpr ⟨i, hi, rfl⟩)
  · intro h
    apply Finset.disjoint_left.mpr
    intro z hz hR
    obtain ⟨i, hi, hiz⟩ := Finset.mem_image.mp hR
    subst z
    exact Finset.disjoint_left.mp h
      (List.mem_toFinset.mpr ((center_mem_positionType vertices positions e i).mpr hz))
      (Finset.mem_image.mpr ⟨i, hi, rfl⟩)

def selectedType (k : ℕ) (R : Finset ℕ) (t : List ℕ) : Prop :=
  k ∈ t ∧ Disjoint t.toFinset R

instance (k : ℕ) (R : Finset ℕ) (t : List ℕ) : Decidable (selectedType k R t) :=
  inferInstanceAs (Decidable (k ∈ t ∧ Disjoint t.toFinset R))

theorem selectedType_iff (vertices positions : Fin s ↪ Fin v)
    (j : Fin s) (R : Finset (Fin s)) (e : Finset (Fin v)) :
    selectedType ((positions j).val + 1) (avoidedPositions positions R)
      (positionType vertices positions e) ↔ vertices j ∈ e ∧ Disjoint e (R.image vertices) := by
  rw [selectedType, center_mem_positionType, ← disjoint_positionType]

def avoidedCount (p : Numeric.Profile) (k : ℕ) (R : Finset ℕ) : ℕ :=
  (p.types.map fun t => if selectedType k R t.locks then t.count else 0).sum

theorem avoidedCount_cast (p : Numeric.Profile) (k : ℕ) (R : Finset ℕ) :
    (avoidedCount p k R : ℚ) =
      Numeric.qsum (p.types.map fun t => (t.count : ℚ) *
        (if selectedType k R t.locks then 1 else 0)) := by
  rw [avoidedCount, Nat.cast_list_sum, qsum_eq_sum, List.map_map]
  congr 1
  apply List.map_congr_left
  intro t _
  simp only [Function.comp_def]
  split_ifs <;> simp

/-- A subset-of-locks quota uses exactly the sum of the realized type counts
whose traces contain the center and avoid that subset. -/
theorem realized_avoided_count (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin s ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount)
    (j : Fin s) (R : Finset (Fin s)) :
    (avoidedEdges H (vertices j) (R.image vertices)).card =
      avoidedCount p ((positions j).val + 1) (avoidedPositions positions R) := by
  have heq : (avoidedCount p ((positions j).val + 1) (avoidedPositions positions R) : ℚ) =
      ((avoidedEdges H (vertices j) (R.image vertices)).card : ℚ) := by
    rw [avoidedCount_cast, ← sum_by_table H.edges (positionType vertices positions) p real.table
      (fun t => if selectedType ((positions j).val + 1) (avoidedPositions positions R) t
        then 1 else 0), ← Finset.sum_filter]
    simp only [Finset.sum_const, nsmul_eq_mul, mul_one]
    congr 1
    apply congrArg Finset.card
    ext e
    simp only [Finset.mem_filter, mem_avoidedEdges, selectedType_iff]
  exact_mod_cast heq.symm

def typeQuota (k : ℕ) (R : ι → Finset ℕ) (a : ι → ℚ) (t u : List ℕ) : ℚ :=
  ∑ i, if selectedType k (R i) t ∧ selectedType k (R i) u then a i else 0

def typePenalty (p : Numeric.Profile) (k : ℕ) (R : ι → Finset ℕ) (a : ι → ℚ)
    (t u : List ℕ) : ℚ :=
  if k ∈ t ∧ k ∈ u then
    max 0 (typeQuota k R a t u -
      (Numeric.pairWeight p ⟨t,0⟩ ⟨u,0⟩ k + Numeric.pairWeight p ⟨u,0⟩ ⟨t,0⟩ k)) / 2
  else 0

def penaltySum (p : Numeric.Profile) (k : ℕ) (R : ι → Finset ℕ) (a : ι → ℚ) : ℚ :=
  Numeric.qsum (p.types.flatMap fun t => p.types.map fun u =>
    (t.count * (u.count - if t.locks = u.locks then 1 else 0) : ℕ) *
      typePenalty p k R a t.locks u.locks)

theorem quotaWeight_types (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin s ↪ Fin v) (j : Fin s)
    (R : ι → Finset (Fin s)) (a : ι → ℚ)
    (e f : Finset (Fin v)) (he : e ∈ H.edges) (hf : f ∈ H.edges) :
    quotaWeight (fun i => avoidedEdges H (vertices j) ((R i).image vertices)) a {e,f} =
      typeQuota ((positions j).val + 1) (fun i => avoidedPositions positions (R i)) a
        (positionType vertices positions e) (positionType vertices positions f) := by
  simp only [quotaWeight, typeQuota, Finset.insert_subset_iff, Finset.singleton_subset_iff,
    mem_avoidedEdges, he, hf, true_and, selectedType_iff]

/-- Full ordered capacities are precisely n_t(n_u-[t=u]); each unordered
deficiency is charged by one half in its two directions. -/
theorem realized_penalty_sum (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin s ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount) (j : Fin s)
    (R : ι → Finset (Fin s)) (a : ι → ℚ) :
    (∑ z ∈ (H.incidentEdges (vertices j)).offDiag,
      dualPenalty (fun i => avoidedEdges H (vertices j) ((R i).image vertices)) a
        (typeWeight p (positionType vertices positions) ((positions j).val + 1)) z) =
      penaltySum p ((positions j).val + 1) (fun i => avoidedPositions positions (R i)) a := by
  rw [Simple5Hypergraph.incidentEdges, Aris4Math.GlobalPairs.offDiag_filter, Finset.sum_filter]
  calc
    _ = ∑ z ∈ H.edges.offDiag,
        typePenalty p ((positions j).val + 1) (fun i => avoidedPositions positions (R i)) a
          (positionType vertices positions z.1) (positionType vertices positions z.2) := by
      apply Finset.sum_congr rfl
      intro z hz
      obtain ⟨h1,h2,_⟩ := Finset.mem_offDiag.mp hz
      simp only [dualPenalty, quotaWeight_types H vertices positions j R a z.1 z.2 h1 h2,
        typePenalty, center_mem_positionType, typeWeight]
    _ = _ := pair_sum_by_table H.edges (positionType vertices positions) p real.table
      (typePenalty p ((positions j).val + 1) (fun i => avoidedPositions positions (R i)) a)

/-- The numerical certificate is connected to the same actual H on both
sides. The caller supplies only finite nonnegative multipliers, computable quota
inequalities, and a computable final bound. -/
theorem realized_refined_deduction (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin s ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount) (j : Fin s)
    (R : ι → Finset (Fin s)) (a : ι → ℚ) (q : ι → ℕ) (D : ℚ)
    (ha : ∀ i, 0 ≤ a i) (hj : ∀ i, j ∉ R i)
    (hq : ∀ i, q i ≤
      (4 * avoidedCount p ((positions j).val + 1) (avoidedPositions positions (R i)) + 2 -
        (v - 1 - (R i).card)) / 3)
    (hfinite : D ≤ (∑ i, (q i : ℚ) * a i) -
      penaltySum p ((positions j).val + 1) (fun i => avoidedPositions positions (R i)) a) :
    D ≤ ∑ z ∈ directedBadPairs H (vertices j),
      typeWeight p (positionType vertices positions) ((positions j).val + 1) z := by
  have hx : ∀ i, vertices j ∉ (R i).image vertices := by
    intro i hi
    obtain ⟨l, hl, he⟩ := Finset.mem_image.mp hi
    exact hj i ((vertices.injective he) ▸ hl)
  have hactual : ∀ i, q i ≤
      (4 * (avoidedEdges H (vertices j) ((R i).image vertices)).card + 2 -
        (Fintype.card (Fin v) - 1 - ((R i).image vertices).card)) / 3 := by
    intro i
    rw [realized_avoided_count H vertices positions p real j (R i),
      Finset.card_image_of_injective _ vertices.injective, Fintype.card_fin]
    exact hq i
  have h := avoided_dual_lower H (vertices j) (fun i => (R i).image vertices) a q
    (typeWeight p (positionType vertices positions) ((positions j).val + 1)) ha hx hactual
  rw [realized_penalty_sum H vertices positions p real j R a] at h
  exact hfinite.trans h

/-- A realized profile with finite avoided-lock dual certificates gives a
coloring of the original hypergraph. This is the actual probability caller;
finite classification and construction of `real` remain the branch's work. -/
theorem propertyB_of_refined_deletion (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin s ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount)
    (noCap : p.emptyPairCap = none) (loss : ℕ → ℚ)
    (R : Fin s → ι → Finset (Fin s)) (a : Fin s → ι → ℚ) (q : Fin s → ι → ℕ)
    (ha : ∀ j, (positions j).val + 1 ∈ p.correctionCenters → ∀ i, 0 ≤ a j i)
    (hj : ∀ j, (positions j).val + 1 ∈ p.correctionCenters → ∀ i, j ∉ R j i)
    (hq : ∀ j, (positions j).val + 1 ∈ p.correctionCenters → ∀ i, q j i ≤
      (4 * avoidedCount p ((positions j).val + 1) (avoidedPositions positions (R j i)) + 2 -
        (v - 1 - (R j i).card)) / 3)
    (hfinite : ∀ j, (positions j).val + 1 ∈ p.correctionCenters →
      loss ((positions j).val + 1) ≤ (∑ i, (q j i : ℚ) * a j i) -
        penaltySum p ((positions j).val + 1)
          (fun i => avoidedPositions positions (R j i)) (a j))
    (zeroOutside : ∀ k, k ∉ p.correctionCenters → loss k = 0)
    (strict : (∑ k : Fin v, min (Numeric.boundA p (k.val + 1))
      (min (Numeric.boundB p (k.val + 1))
        (Numeric.boundC p (k.val + 1) - loss (k.val + 1)))) < 1) : PropertyB H := by
  apply CustomDeletion.propertyB_of_custom_deletion H vertices positions p real noCap loss
    _ zeroOutside strict
  intro j hc
  exact realized_refined_deduction H vertices positions p real j (R j) (a j) (q j)
    (loss ((positions j).val + 1)) (ha j hc) (hj j hc) (hq j hc) (hfinite j hc)

end Aris4Math.ThirtyThree.RefinedDeletion

#print axioms Aris4Math.ThirtyThree.RefinedDeletion.avoided_dual_lower
#print axioms Aris4Math.ThirtyThree.RefinedDeletion.realized_avoided_count
#print axioms Aris4Math.ThirtyThree.RefinedDeletion.realized_refined_deduction
#print axioms Aris4Math.ThirtyThree.RefinedDeletion.propertyB_of_refined_deletion
