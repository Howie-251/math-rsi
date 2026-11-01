import Aris4Math.ThirtyFour.MixedLayoutDual
import Aris4Math.ThirtyThree.ActualBadSlot

/-! Position-independent actual bad pairs, combined across layouts before
charging any capacity penalty. The finite data are tied to the original H. -/
namespace Aris4Math.ThirtyFour.MixedLayoutCounts
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open Aris4Math.ThirtyThree.AvoidedLink
open Aris4Math.ThirtyThree.RefinedDeletion
variable {n v : ℕ} {L Q : Type*} [Fintype L] [Fintype Q]

abbrev Trace (n : ℕ) := Finset (Fin n)
def mixedWeight (beta : L → Fin n → ℚ) (w : L → Fin n → Trace n → Trace n → ℚ)
    (j : Fin n) (T U : Trace n) : ℚ := ∑ l, beta l j*w l j T U

def traceQuota (j : Fin n) (R : Q → Trace n) (delta : Q → ℚ) (T U : Trace n) : ℚ :=
  ∑ q, if j ∈ T ∧ j ∈ U ∧ Disjoint T (R q) ∧ Disjoint U (R q) then delta q else 0

def tracePenalty (beta : L → Fin n → ℚ) (w : L → Fin n → Trace n → Trace n → ℚ)
    (j : Fin n) (R : Q → Trace n) (delta : Q → ℚ) (T U : Trace n) : ℚ :=
  if j ∈ T ∧ j ∈ U then
    max 0 (traceQuota j R delta T U -
      (mixedWeight beta w j T U+mixedWeight beta w j U T))/2
  else 0

def penalty (labels : Finset (Trace n)) (μ : Trace n → ℕ)
    (beta : L → Fin n → ℚ) (w : L → Fin n → Trace n → Trace n → ℚ)
    (j : Fin n) (R : Q → Trace n) (delta : Q → ℚ) : ℚ :=
  ∑ T ∈ labels, ∑ U ∈ labels,
    (μ T*(μ U-if T=U then 1 else 0) : ℕ)*tracePenalty beta w j R delta T U

def available (labels : Finset (Trace n)) (μ : Trace n → ℕ)
    (j : Fin n) (R : Trace n) : ℕ :=
  ∑ T ∈ labels.filter (fun T => j ∈ T ∧ Disjoint T R), μ T

def actualDeduction (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (w : L → Fin n → Trace n → Trace n → ℚ) (l : L) (j : Fin n) : ℚ :=
  ∑ z ∈ directedBadPairs H (vertices j),
    w l j (lockSignature vertices z.1) (lockSignature vertices z.2)

theorem covers_actual (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (labels : Finset (Trace n)) (μ : Trace n → ℕ)
    (counts : ∀ T, count H vertices T=μ T)
    (covers : ∀ T, 0<μ T → T ∈ labels) :
    ∀ e ∈ H.edges, lockSignature vertices e ∈ labels := by
  intro e he
  apply covers
  rw [← counts]
  exact Finset.card_pos.mpr ⟨e,Finset.mem_filter.mpr ⟨he,rfl⟩⟩

theorem available_actual (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (labels : Finset (Trace n)) (μ : Trace n → ℕ)
    (counts : ∀ T, count H vertices T=μ T)
    (covers : ∀ T, 0<μ T → T ∈ labels) (j : Fin n) (R : Trace n) :
    (avoidedEdges H (vertices j) (R.image vertices)).card=available labels μ j R := by
  have cov := covers_actual H vertices labels μ counts covers
  have hs := Aris4Math.ThirtyThree.MultiLockRecovery.sum_counts H vertices
    (labels.filter fun T => j ∈ T ∧ Disjoint T R)
  simp_rw [counts] at hs
  unfold available
  rw [hs]
  congr 1
  ext e
  simp only [mem_avoidedEdges,Finset.mem_filter]
  constructor
  · rintro ⟨he,hj,hr⟩
    exact ⟨he,cov e he,(mem_lockSignature vertices e j).mpr hj,
      (ThirtyThree.ActualBadSlot.signature_disjoint vertices e R).mpr hr⟩
  · rintro ⟨he,_,hj,hr⟩
    exact ⟨he,(mem_lockSignature vertices e j).mp hj,
      (ThirtyThree.ActualBadSlot.signature_disjoint vertices e R).mp hr⟩

theorem actual_quota_types (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (j : Fin n) (R : Q → Trace n) (delta : Q → ℚ)
    (E F : Finset (Fin v)) (he : E ∈ H.edges) (hf : F ∈ H.edges) :
    quotaWeight (fun q => avoidedEdges H (vertices j) ((R q).image vertices)) delta {E,F} =
      traceQuota j R delta (lockSignature vertices E) (lockSignature vertices F) := by
  simp only [quotaWeight,traceQuota,Finset.insert_subset_iff,Finset.singleton_subset_iff,
    mem_avoidedEdges,he,hf,true_and,mem_lockSignature,
    ThirtyThree.ActualBadSlot.signature_disjoint]
  apply Finset.sum_congr rfl
  intro q _
  congr 1
  apply propext
  tauto

theorem penalty_actual (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (labels : Finset (Trace n)) (μ : Trace n → ℕ)
    (counts : ∀ T, count H vertices T=μ T) (covers : ∀ T, 0<μ T → T ∈ labels)
    (beta : L → Fin n → ℚ) (w : L → Fin n → Trace n → Trace n → ℚ)
    (j : Fin n) (R : Q → Trace n) (delta : Q → ℚ) :
    (∑ z ∈ (H.incidentEdges (vertices j)).offDiag,
      dualPenalty (fun q => avoidedEdges H (vertices j) ((R q).image vertices)) delta
        (fun z => mixedWeight beta w j (lockSignature vertices z.1) (lockSignature vertices z.2)) z) =
      penalty labels μ beta w j R delta := by
  rw [Simple5Hypergraph.incidentEdges,Aris4Math.GlobalPairs.offDiag_filter,Finset.sum_filter]
  calc
    _ = ∑ z ∈ H.edges.offDiag,
        tracePenalty beta w j R delta (lockSignature vertices z.1) (lockSignature vertices z.2) := by
      apply Finset.sum_congr rfl
      intro z hz
      obtain ⟨he,hf,_⟩ := Finset.mem_offDiag.mp hz
      simp only [tracePenalty,mem_lockSignature,dualPenalty,
        actual_quota_types H vertices j R delta z.1 z.2 he hf]
    _ = _ := by
      rw [pair_sum_by_type H.edges (lockSignature vertices) labels
        (covers_actual H vertices labels μ counts covers)]
      unfold penalty
      have hm (T) : multiplicity H.edges (lockSignature vertices) T=μ T := counts T
      simp_rw [hm]

/-- Actual deductions from every layout are combined on the same H before
applying the subfamily quotas and complete ordered pair capacities. -/
theorem mixed_deduction (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (labels : Finset (Trace n)) (μ : Trace n → ℕ)
    (counts : ∀ T, count H vertices T=μ T) (covers : ∀ T, 0<μ T → T ∈ labels)
    (beta : L → Fin n → ℚ) (w : L → Fin n → Trace n → Trace n → ℚ)
    (j : Fin n) (R : Q → Trace n) (delta : Q → ℚ) (quota : Q → ℕ)
    (dn : ∀ q, 0 ≤ delta q) (avoids : ∀ q, j ∉ R q)
    (valid : ∀ q, quota q ≤ (4*available labels μ j (R q)+2-(v-1-(R q).card))/3) :
    (∑ q, (quota q : ℚ)*delta q)-penalty labels μ beta w j R delta ≤
      ∑ l, beta l j*actualDeduction H vertices w l j := by
  have hx : ∀ q, vertices j ∉ (R q).image vertices := by
    intro q h
    obtain ⟨i,hi,eq⟩ := Finset.mem_image.mp h
    exact avoids q (vertices.injective eq ▸ hi)
  have hq : ∀ q, quota q ≤
      (4*(avoidedEdges H (vertices j) ((R q).image vertices)).card+2-
        (Fintype.card (Fin v)-1-((R q).image vertices).card))/3 := by
    intro q
    rw [available_actual H vertices labels μ counts covers,
      Fintype.card_fin,Finset.card_image_of_injective _ vertices.injective]
    exact valid q
  have bound := avoided_dual_lower H (vertices j) (fun q => (R q).image vertices) delta quota
    (fun z => mixedWeight beta w j (lockSignature vertices z.1) (lockSignature vertices z.2)) dn hx hq
  rw [penalty_actual H vertices labels μ counts covers beta w j R delta] at bound
  have eq : (∑ z ∈ directedBadPairs H (vertices j),
      mixedWeight beta w j (lockSignature vertices z.1) (lockSignature vertices z.2)) =
      ∑ l, beta l j*actualDeduction H vertices w l j := by
    simp only [mixedWeight,actualDeduction,Finset.mul_sum]
    rw [Finset.sum_comm]
  exact bound.trans_eq eq
end Aris4Math.ThirtyFour.MixedLayoutCounts
#print axioms Aris4Math.ThirtyFour.MixedLayoutCounts.mixed_deduction
