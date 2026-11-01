import Aris4Math.ProfileApplication
import Aris4Math.GlobalPairs

/-! Capacity-sensitive link deletion through a finite threshold inequality.
This connects all type-pair slots, including zero-weight slots, to the actual
bad pairs. Finite callers choose and check their threshold exactly. -/

open scoped BigOperators

namespace Aris4Math.ThirtyThree.TwentyOneDeletion

open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Half the deficiency of the two-direction unordered weight. Summing over
both directions contributes exactly one unordered deficiency. -/
def penalty (w : Finset V × Finset V → ℚ) (c : ℚ) (d : Finset V × Finset V) : ℚ :=
  max 0 (c - (w d + w (d.2,d.1))) / 2

theorem penalty_nonneg (w : Finset V × Finset V → ℚ) (c : ℚ)
    (d : Finset V × Finset V) : 0 ≤ penalty w c d :=
  div_nonneg (le_max_left _ _) (by norm_num)

theorem unordered_with_penalty (w : Finset V × Finset V → ℚ) (c : ℚ)
    (a b : Finset V) (hne : a ≠ b) :
    c ≤ unorderedWeight w {a,b} + unorderedWeight (penalty w c) {a,b} := by
  rw [unorderedWeight_pair w a b hne, unorderedWeight_pair (penalty w c) a b hne]
  simp only [penalty]
  rw [add_comm (w (b,a)) (w (a,b))]
  have h := le_max_right (0 : ℚ) (c - (w (a,b) + w (b,a)))
  linarith

theorem directed_bad_subset_incident (H : Simple5Hypergraph V) (x : V) :
    directedBadPairs H x ⊆ (H.incidentEdges x).offDiag := by
  intro d hd
  obtain ⟨p,hp,hdp⟩ := Finset.mem_biUnion.mp hd
  obtain ⟨ha,hb,hne⟩ := Finset.mem_offDiag.mp hdp
  have hsub := badPair_subset H x p hp
  exact Finset.mem_offDiag.mpr ⟨hsub ha,hsub hb,hne⟩

/-- Count q actual bad unordered pairs at threshold c, paying for every possible
incident-pair deficiency. This preserves capacities without assuming which
slots are bad or that their weights are positive. -/
theorem threshold_bad_weight_lower (H : Simple5Hypergraph V) (x : V)
    (w : Finset V × Finset V → ℚ) (q : ℕ) (c : ℚ)
    (hq : q ≤ (H.badLinkPairs x).card) (hc : 0 ≤ c) :
    (q : ℚ)*c - (∑ d ∈ (H.incidentEdges x).offDiag, penalty w c d) ≤
      ∑ d ∈ directedBadPairs H x, w d := by
  have each : ∀ p ∈ H.badLinkPairs x,
      c ≤ unorderedWeight w p + unorderedWeight (penalty w c) p := by
    intro p hp
    obtain ⟨a,b,hne,rfl⟩ := Finset.card_eq_two.mp (badPair_card H x p hp)
    exact unordered_with_penalty w c a b hne
  have hsum := Finset.sum_le_sum each
  rw [Finset.sum_add_distrib] at hsum
  simp only [Finset.sum_const,nsmul_eq_mul] at hsum
  rw [← directed_bad_sum,← directed_bad_sum] at hsum
  have hcard : (q : ℚ)*c ≤ ((H.badLinkPairs x).card : ℚ)*c :=
    mul_le_mul_of_nonneg_right (by exact_mod_cast hq) hc
  have hp := Finset.sum_le_sum_of_subset_of_nonneg (directed_bad_subset_incident H x)
    (fun d _ _ => penalty_nonneg w c d)
  linarith

/-- The type-pair deficiency is zero unless both edges contain the center. -/
def typePenalty (p : Numeric.Profile) (k : ℕ) (c : ℚ) (t u : List ℕ) : ℚ :=
  if k ∈ t ∧ k ∈ u then
    max 0 (c - (Numeric.pairWeight p ⟨t,0⟩ ⟨u,0⟩ k +
      Numeric.pairWeight p ⟨u,0⟩ ⟨t,0⟩ k)) / 2
  else 0

def penaltySum (p : Numeric.Profile) (k : ℕ) (c : ℚ) : ℚ :=
  Numeric.qsum (p.types.flatMap fun t => p.types.map fun u =>
    (t.count * (u.count - if t.locks = u.locks then 1 else 0) : ℕ) *
      typePenalty p k c t.locks u.locks)

/-- A computable threshold; callers prove the needed inequality directly for
finite data, rather than assuming a general sorting optimization theorem. -/
def threshold (p : Numeric.Profile) (k : ℕ) : ℚ :=
  if Numeric.linkQLower p k = 0 then 0 else
    ((Numeric.linkSlots p k).insertionSort (· ≤ ·)).getD (Numeric.linkQLower p k - 1) 0

variable {v edgeCount : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]

theorem realized_penalty_sum (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount) (j : ι) (k : ℕ) (c : ℚ)
    (hk : (positions j).val + 1 = k) :
    (∑ d ∈ (H.incidentEdges (vertices j)).offDiag,
      penalty (typeWeight p (positionType vertices positions) k) c d) = penaltySum p k c := by
  rw [Simple5Hypergraph.incidentEdges,Aris4Math.GlobalPairs.offDiag_filter,Finset.sum_filter]
  calc
    _ = ∑ d ∈ H.edges.offDiag, typePenalty p k c
        (positionType vertices positions d.1) (positionType vertices positions d.2) := by
      apply Finset.sum_congr rfl
      intro d _
      simp only [typePenalty,← hk,center_mem_positionType,penalty,typeWeight]
    _ = _ := pair_sum_by_table H.edges (positionType vertices positions) p real.table
      (typePenalty p k c)

/-- All real capacities, probability weights, and bad-pair counts are bound to H.
A caller supplies only an explicitly checked finite threshold comparison. -/
theorem realized_threshold_deduction (H : Simple5Hypergraph (Fin v))
    (cover : H.PairCovering) (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount) (j : ι) (k q : ℕ) (c D : ℚ)
    (hk : (positions j).val + 1 = k)
    (hq : q ≤ (4 * H.degree (vertices j) - (v-1) + 2)/3)
    (hc : 0 ≤ c) (finite_bound : D ≤ (q : ℚ)*c - penaltySum p k c) :
    D ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight p (positionType vertices positions) k d := by
  have hactual : q ≤ (H.badLinkPairs (vertices j)).card :=
    hq.trans (by simpa only [Fintype.card_fin] using H.link_bad_pair_lower_bound cover (vertices j))
  have h := threshold_bad_weight_lower H (vertices j)
    (typeWeight p (positionType vertices positions) k) q c hactual hc
  rw [realized_penalty_sum H vertices positions p real j k c hk] at h
  exact finite_bound.trans h

end Aris4Math.ThirtyThree.TwentyOneDeletion

#print axioms Aris4Math.ThirtyThree.TwentyOneDeletion.realized_threshold_deduction
