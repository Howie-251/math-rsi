import Aris4Math.ThirtyThree.PureLink
import Aris4Math.ThirtyThree.TwentyOneDeletion

/-! Two nonnegative multipliers bind the total bad-pair quota and the actual
pure-singleton bad-pair quota to all finite type-pair capacities. -/
namespace Aris4Math.ThirtyThree.TwentyTwoPureDeletion

open scoped BigOperators
open Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.TwentyOneDeletion Aris4Math.ThirtyThree.PureLink

variable {V : Type*} [Fintype V] [DecidableEq V]

def dualPenalty (P : Finset (Finset V)) (w : Finset V × Finset V → ℚ)
    (c d : ℚ) (z : Finset V × Finset V) : ℚ :=
  max 0 (c + (if z.1 ∈ P ∧ z.2 ∈ P then d else 0) - (w z+w (z.2,z.1))) / 2

theorem dualPenalty_nonneg (P : Finset (Finset V)) (w : Finset V × Finset V → ℚ)
    (c d : ℚ) (z : Finset V × Finset V) : 0 ≤ dualPenalty P w c d z :=
  div_nonneg (le_max_left _ _) (by norm_num)

theorem unordered_dual_penalty (P : Finset (Finset V)) (w : Finset V × Finset V → ℚ)
    (c d : ℚ) (a b : Finset V) (hne : a ≠ b) :
    c + (if {a,b} ⊆ P then d else 0) ≤ unorderedWeight w {a,b} +
      unorderedWeight (dualPenalty P w c d) {a,b} := by
  rw [unorderedWeight_pair w a b hne,unorderedWeight_pair (dualPenalty P w c d) a b hne]
  simp only [dualPenalty,Finset.insert_subset_iff,Finset.singleton_subset_iff]
  have hbonus : (if b ∈ P ∧ a ∈ P then d else 0) = (if a ∈ P ∧ b ∈ P then d else 0) := by
    by_cases ha : a ∈ P <;> by_cases hb : b ∈ P <;> simp [ha,hb]
  rw [hbonus,add_comm (w (b,a)) (w (a,b))]
  have h := le_max_right (0 : ℚ)
    (c + (if a ∈ P ∧ b ∈ P then d else 0) - (w (a,b)+w (b,a)))
  linarith

/-- Every real pair deficiency is paid once, by half in each orientation.
The subquota is on a literal filtered subfamily of the same bad pairs. -/
theorem dual_bad_weight_lower (H : Simple5Hypergraph V) (x : V)
    (P : Finset (Finset V)) (w : Finset V × Finset V → ℚ)
    (q r : ℕ) (c d : ℚ) (hq : q ≤ (H.badLinkPairs x).card)
    (hr : r ≤ ((H.badLinkPairs x).filter fun p => p ⊆ P).card)
    (hc : 0 ≤ c) (hd : 0 ≤ d) :
    (q : ℚ)*c + (r : ℚ)*d - (∑ z ∈ (H.incidentEdges x).offDiag,dualPenalty P w c d z) ≤
      ∑ z ∈ directedBadPairs H x,w z := by
  classical
  have each : ∀ p ∈ H.badLinkPairs x,
      c + (if p ⊆ P then d else 0) ≤ unorderedWeight w p +
        unorderedWeight (dualPenalty P w c d) p := by
    intro p hp
    obtain ⟨a,b,hne,rfl⟩ := Finset.card_eq_two.mp (badPair_card H x p hp)
    exact unordered_dual_penalty P w c d a b hne
  have hs := Finset.sum_le_sum each
  rw [Finset.sum_add_distrib,Finset.sum_add_distrib,← Finset.sum_filter] at hs
  simp only [Finset.sum_const,nsmul_eq_mul] at hs
  rw [← directed_bad_sum,← directed_bad_sum] at hs
  have hq' : (q:ℚ)*c ≤ ((H.badLinkPairs x).card:ℚ)*c :=
    mul_le_mul_of_nonneg_right (by exact_mod_cast hq) hc
  have hr' : (r:ℚ)*d ≤ (((H.badLinkPairs x).filter fun p => p ⊆ P).card:ℚ)*d :=
    mul_le_mul_of_nonneg_right (by exact_mod_cast hr) hd
  have hp := Finset.sum_le_sum_of_subset_of_nonneg (directed_bad_subset_incident H x)
    (fun z _ _ => dualPenalty_nonneg P w c d z)
  linarith

def typePenalty (p : Numeric.Profile) (k : ℕ) (c d : ℚ) (t u : List ℕ) : ℚ :=
  if k ∈ t ∧ k ∈ u then
    max 0 (c + (if t=[k] ∧ u=[k] then d else 0) -
      (Numeric.pairWeight p ⟨t,0⟩ ⟨u,0⟩ k + Numeric.pairWeight p ⟨u,0⟩ ⟨t,0⟩ k)) / 2
  else 0

def penaltySum (p : Numeric.Profile) (k : ℕ) (c d : ℚ) : ℚ :=
  Numeric.qsum (p.types.flatMap fun t => p.types.map fun u =>
    (t.count * (u.count - if t.locks=u.locks then 1 else 0) : ℕ) *
      typePenalty p k c d t.locks u.locks)

variable {v s edgeCount : ℕ}

theorem realized_penalty_sum (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin s ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount) (j : Fin s) (k : ℕ) (c d : ℚ)
    (hk : (positions j).val+1=k) :
    (∑ z ∈ (H.incidentEdges (vertices j)).offDiag,
      dualPenalty (pureEdges H vertices j) (typeWeight p (positionType vertices positions) k) c d z) =
        penaltySum p k c d := by
  rw [Simple5Hypergraph.incidentEdges,Aris4Math.GlobalPairs.offDiag_filter,Finset.sum_filter]
  calc
    _ = ∑ z ∈ H.edges.offDiag, typePenalty p k c d
        (positionType vertices positions z.1) (positionType vertices positions z.2) := by
      apply Finset.sum_congr rfl
      intro z hz
      obtain ⟨h1,h2,_⟩ := Finset.mem_offDiag.mp hz
      simp only [typePenalty,← hk,center_mem_positionType,dualPenalty,typeWeight,pureEdges,
        Finset.mem_filter,h1,h2,true_and,pure_iff_type vertices positions j]
    _ = _ := pair_sum_by_table H.edges (positionType vertices positions) p real.table (typePenalty p k c d)

theorem realized_dual_deduction (H : Simple5Hypergraph (Fin v)) (cover : H.PairCovering)
    (vertices positions : Fin s ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount) (j : Fin s) (k q r n : ℕ)
    (c d D : ℚ) (hk : (positions j).val+1=k)
    (hq : q ≤ (4*H.degree (vertices j)-(v-1)+2)/3)
    (hpure : (pureEdges H vertices j).card=n)
    (hr : r ≤ (4*n+2-(v-s))/3) (hc : 0 ≤ c) (hd : 0 ≤ d)
    (hfinite : D ≤ (q:ℚ)*c+(r:ℚ)*d-penaltySum p k c d) :
    D ≤ ∑ z ∈ directedBadPairs H (vertices j),typeWeight p (positionType vertices positions) k z := by
  have hq' : q ≤ (H.badLinkPairs (vertices j)).card :=
    hq.trans (by simpa only [Fintype.card_fin] using H.link_bad_pair_lower_bound cover (vertices j))
  have hr' : r ≤ (pureBadPairs H vertices j).card := by
    have h := pure_bad_pair_lower H vertices j
    rw [hpure] at h
    exact hr.trans h
  have h := dual_bad_weight_lower H (vertices j) (pureEdges H vertices j)
    (typeWeight p (positionType vertices positions) k) q r c d hq' hr' hc hd
  rw [realized_penalty_sum H vertices positions p real j k c d hk] at h
  exact hfinite.trans h

end Aris4Math.ThirtyThree.TwentyTwoPureDeletion

#print axioms Aris4Math.ThirtyThree.TwentyTwoPureDeletion.realized_dual_deduction
