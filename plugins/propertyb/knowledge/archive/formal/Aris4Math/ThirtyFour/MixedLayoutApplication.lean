import Aris4Math.ThirtyFour.MixedLayoutCounts

/-! A computable mixed-layout certificate produces a coloring of the original
hypergraph. Every layout uses one fixed family of actual bad pairs. -/
namespace Aris4Math.ThirtyFour.MixedLayoutApplication
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.MultiLockRecovery (canonicalType count)
open Aris4Math.ThirtyFour.MixedLayoutCounts
variable {n v edgeCount : ℕ} {L Q : Type*} [Fintype L] [Fintype Q]

def weights (positions : L → Fin n ↪ Fin v) (p : L → Numeric.Profile)
    (l : L) (j : Fin n) (T U : Trace n) : ℚ :=
  Numeric.pairWeight (p l) ⟨canonicalType (positions l) T,0⟩
    ⟨canonicalType (positions l) U,0⟩ ((positions l j).val+1)

def centerLoss (positions : Fin n ↪ Fin v) (D : Fin n → ℚ) (k : ℕ) : ℚ :=
  ∑ j, if (positions j).val+1=k then D j else 0

def a (positions : L → Fin n ↪ Fin v) (p : L → Numeric.Profile) (l : L) (j : Fin n) : ℚ :=
  min (Numeric.boundA (p l) ((positions l j).val+1))
    (Numeric.boundB (p l) ((positions l j).val+1))
def c (positions : L → Fin n ↪ Fin v) (p : L → Numeric.Profile) (l : L) (j : Fin n) : ℚ :=
  Numeric.boundC (p l) ((positions l j).val+1)
def free (positions : Fin n ↪ Fin v) (p : Numeric.Profile) : ℚ :=
  ∑ k ∈ Finset.univ.filter (fun k => ¬ ∃ j, positions j=k),
    min (Numeric.boundA p (k.val+1)) (min (Numeric.boundB p (k.val+1)) (Numeric.boundC p (k.val+1)))

theorem loss_at (positions : Fin n ↪ Fin v) (D : Fin n → ℚ) (j : Fin n) :
    centerLoss positions D ((positions j).val+1)=D j := by
  classical
  unfold centerLoss
  rw [Finset.sum_eq_single j]
  · simp
  · intro i _ ne
    have neq : (positions i).val+1 ≠ (positions j).val+1 := by
      intro eq
      exact ne (positions.injective (Fin.ext (Nat.add_right_cancel eq)))
    simp only [if_neg neq]
  · simp

theorem loss_outside (positions : Fin n ↪ Fin v) (D : Fin n → ℚ) (k : Fin v)
    (outside : ¬ ∃ j, positions j=k) : centerLoss positions D (k.val+1)=0 := by
  apply Finset.sum_eq_zero
  intro j _
  have ne : (positions j).val+1 ≠ k.val+1 := by
    intro eq; exact outside ⟨j,Fin.ext (Nat.add_right_cancel eq)⟩
  simp only [if_neg ne]

theorem sum_decompose (positions : Fin n ↪ Fin v) (F : Fin v → ℚ) :
    (∑ k, F k) = (∑ k ∈ Finset.univ.filter (fun k => ¬ ∃ j, positions j=k), F k) +
      ∑ j, F (positions j) := by
  classical
  have image : Finset.univ.filter (fun k => ∃ j, positions j=k) = Finset.univ.image positions := by
    ext k; simp
  have split := Finset.sum_filter_not_add_sum_filter (s := Finset.univ)
    (p := fun k => ∃ j, positions j=k) F
  rw [image,Finset.sum_image] at split
  · exact split.symm
  · intro i _ j _ eq; exact positions.injective eq

theorem bound_decompose (positions : Fin n ↪ Fin v) (p : Numeric.Profile) (D : Fin n → ℚ) :
    (∑ k : Fin v, min (Numeric.boundA p (k.val+1))
      (min (Numeric.boundB p (k.val+1)) (Numeric.boundC p (k.val+1)-centerLoss positions D (k.val+1)))) =
      free positions p + ∑ j, min
        (min (Numeric.boundA p ((positions j).val+1)) (Numeric.boundB p ((positions j).val+1)))
        (Numeric.boundC p ((positions j).val+1)-D j) := by
  rw [sum_decompose positions]
  congr 1
  · apply Finset.sum_congr rfl
    intro k hk
    rw [loss_outside positions D k (Finset.mem_filter.mp hk).2,sub_zero]
  · apply Finset.sum_congr rfl
    intro j _
    rw [loss_at,min_assoc]

theorem propertyB_of_layout_bound (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount)
    (nocap : p.emptyPairCap=none)
    (centers : ∀ j, (positions j).val+1 ∈ p.correctionCenters)
    (strict : free positions p + ∑ j, min
      (min (Numeric.boundA p ((positions j).val+1)) (Numeric.boundB p ((positions j).val+1)))
      (Numeric.boundC p ((positions j).val+1)-
        ∑ z ∈ directedBadPairs H (vertices j),
          typeWeight p (positionType vertices positions) ((positions j).val+1) z) < 1) : PropertyB H := by
  let D (j : Fin n) := ∑ z ∈ directedBadPairs H (vertices j),
    typeWeight p (positionType vertices positions) ((positions j).val+1) z
  apply ThirtyThree.CustomDeletion.propertyB_of_custom_deletion H vertices positions p real nocap
    (centerLoss positions D)
  · intro j _
    rw [loss_at]
  · intro k absent
    apply Finset.sum_eq_zero
    intro j _
    have ne : (positions j).val+1 ≠ k := by intro eq; exact absent (eq ▸ centers j)
    simp only [if_neg ne]
  · rw [bound_decompose]
    exact strict

/-- Complete actual-input mixed-layout interface, without assuming an
unrelated numerical bad vector or taking a worst case separately per layout. -/
theorem propertyB_of_mixed_layouts (H : Simple5Hypergraph (Fin v))
    (vertices : Fin n ↪ Fin v) (labels : Finset (Trace n)) (μ : Trace n → ℕ)
    (counts : ∀ T, count H vertices T=μ T) (covers : ∀ T, 0<μ T → T ∈ labels)
    (positions : L → Fin n ↪ Fin v) (p : L → Numeric.Profile)
    (real : ∀ l, RealizesProfile H vertices (positions l) (p l) edgeCount)
    (nocap : ∀ l, (p l).emptyPairCap=none)
    (centers : ∀ l j, (positions l j).val+1 ∈ (p l).correctionCenters)
    (gamma : L → ℚ) (beta : L → Fin n → ℚ)
    (R : Fin n → Q → Trace n) (delta : Fin n → Q → ℚ) (quota : Fin n → Q → ℕ)
    (gn : ∀ l, 0 ≤ gamma l) (mass : ∑ l, gamma l=1)
    (bn : ∀ l j, 0 ≤ beta l j) (bg : ∀ l j, beta l j ≤ gamma l)
    (dn : ∀ j q, 0 ≤ delta j q) (avoids : ∀ j q, j ∉ R j q)
    (valid : ∀ j q, quota j q ≤ (4*available labels μ j (R j q)+2-(v-1-(R j q).card))/3)
    (strict : (∑ l, gamma l*free (positions l) (p l)) +
      (∑ l, ∑ j, ((gamma l-beta l j)*a positions p l j+beta l j*c positions p l j)) -
      (∑ j, ((∑ q, (quota j q : ℚ)*delta j q)-
        penalty labels μ beta (weights positions p) j (R j) (delta j))) < 1) : PropertyB H := by
  let D := actualDeduction H vertices (weights positions p)
  let lower (j : Fin n) := (∑ q, (quota j q : ℚ)*delta j q)-
    penalty labels μ beta (weights positions p) j (R j) (delta j)
  have deduction (j : Fin n) : lower j ≤ ∑ l, beta l j*D l j :=
    mixed_deduction H vertices labels μ counts covers beta (weights positions p) j
      (R j) (delta j) (quota j) (dn j) (avoids j) (valid j)
  have bound := MixedLayoutDual.average_le gamma beta (a positions p) (c positions p) D
    (fun l => free (positions l) (p l)) lower bn bg deduction
  obtain ⟨l,success⟩ := MixedLayoutDual.exists_strict_of_average gamma
    (fun l => free (positions l) (p l)+∑ j, min (a positions p l j) (c positions p l j-D l j))
    gn mass (bound.trans_lt strict)
  apply propertyB_of_layout_bound H vertices (positions l) (p l) (real l) (nocap l) (centers l)
  exact success
end Aris4Math.ThirtyFour.MixedLayoutApplication
#print axioms Aris4Math.ThirtyFour.MixedLayoutApplication.propertyB_of_mixed_layouts
