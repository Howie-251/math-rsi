import Aris4Math.ThirtyThree.CustomDeletion
import Aris4Math.ThirtyThree.DoubleLockAt
import Aris4Math.ThirtyThree.OrdinaryLink

/-! The actual (8,8) lock-pair case on twenty vertices. The additional
ordinary-link count is transferred to real deletion weights before applying
the exact corrected probability bound. -/

namespace Aris4Math.ThirtyThree.TwentyEight

open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.LinkWeightCertificates Aris4Math.LinkDeletion
open Aris4Math.ThirtyThree.DoubleLockAt Aris4Math.ThirtyThree.OrdinaryLink
open scoped BigOperators

def profile : Numeric.Profile := profileAt 20 10 11 8 8 [10,11]

def positions : Fin 2 ↪ Fin 20 := positionsAt 20 10 11 (by omega) (by omega) (by omega)

def loss (k : ℕ) : ℚ := if k = 10 ∨ k = 11 then 1239/24310 else 0

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem certificates :
    Numeric.validProfile profile 33 ∧
    IncidentWeightBound profile 10 (21/2210) ∧
    IncidentWeightBound profile 11 (21/2210) ∧
    (Numeric.pairWeight profile ⟨[10],0⟩ ⟨[10],0⟩ 10 +
      Numeric.pairWeight profile ⟨[10],0⟩ ⟨[10],0⟩ 10 = 126/12155) ∧
    (Numeric.pairWeight profile ⟨[11],0⟩ ⟨[11],0⟩ 11 +
      Numeric.pairWeight profile ⟨[11],0⟩ ⟨[11],0⟩ 11 = 126/12155) ∧
    (∑ k : Fin 20, min (Numeric.boundA profile (k.val+1))
      (min (Numeric.boundB profile (k.val+1))
        (Numeric.boundC profile (k.val+1) - loss (k.val+1)))) = 2421/2431 := by
  unfold Numeric.validProfile
  decide +kernel

/-- Transfer a single ordinary type to its actual unordered edge pairs. -/
theorem ordinary_weight_bound (H : Simple5Hypergraph (Fin 20)) (x y : Fin 20)
    (classify : Finset (Fin 20) → List ℕ) (k : ℕ)
    (single : ∀ e ∈ ordinaryEdges H x y, classify e = [k])
    (value : Numeric.pairWeight profile ⟨[k],0⟩ ⟨[k],0⟩ k +
      Numeric.pairWeight profile ⟨[k],0⟩ ⟨[k],0⟩ k = 126/12155) :
    ∀ p ∈ ordinaryBadPairs H x y,
      (126/12155 : ℚ) ≤ unorderedWeight (typeWeight profile classify k) p := by
  intro p hp
  obtain ⟨hsub, hcard⟩ := Finset.mem_powersetCard.mp (Finset.mem_filter.mp hp).1
  obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp hcard
  have ha : a ∈ ordinaryEdges H x y := hsub (by simp)
  have hb : b ∈ ordinaryEdges H x y := hsub (by simp)
  rw [unorderedWeight_pair _ a b hab]
  change (126/12155 : ℚ) ≤
    Numeric.pairWeight profile ⟨classify a,0⟩ ⟨classify b,0⟩ k +
    Numeric.pairWeight profile ⟨classify b,0⟩ ⟨classify a,0⟩ k
  rw [single a ha, single b hb, value]

/-- Complete (8,8) case, with real multiplicities and both actual center losses. -/
theorem propertyB_of_eight_eight (H : Simple5Hypergraph (Fin 20))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (x y : Fin 20) (hne : x ≠ y) (one : H.codegree x y = 1)
    (dx : H.degree x = 8) (dy : H.degree y = 8) : PropertyB H := by
  obtain ⟨valid, leftCert, rightCert, leftOrd, rightOrd, total⟩ := certificates
  let vertices := twoVertices x y hne
  let classify := positionType vertices positions
  have real : RealizesProfile H vertices positions profile 33 := by
    have h := realizes_profile_at H edges33 (a := 10) (b := 11)
      (by omega) (by omega) (by omega) x y hne one [10,11]
    simpa only [dx, dy] using h (by simpa only [dx, dy] using valid)
  have single_left (e : Finset (Fin 20)) (he : e ∈ ordinaryEdges H x y) : classify e = [10] := by
    obtain ⟨_, hx, hy⟩ := (mem_ordinaryEdges H x y e).mp he
    change positionType (twoVertices x y hne) (positionsAt 20 10 11 _ _ _) e = [10]
    rw [type_at]
    simp [classAt, hx, hy]
  have single_right (e : Finset (Fin 20)) (he : e ∈ ordinaryEdges H y x) : classify e = [11] := by
    obtain ⟨_, hy, hx⟩ := (mem_ordinaryEdges H y x e).mp he
    change positionType (twoVertices x y hne) (positionsAt 20 10 11 _ _ _) e = [11]
    rw [type_at]
    simp [classAt, hx, hy]
  have base_left : ∀ p ∈ H.badLinkPairs x,
      (21/2210 : ℚ) ≤ unorderedWeight (typeWeight profile classify 10) p := by
    apply unordered_bound_of_incident_bound
    intro a ha b hb hab
    apply realized_pair_weight_bound H.edges classify profile real.table 10 (21/2210)
      leftCert a b (Finset.mem_filter.mp ha).1 (Finset.mem_filter.mp hb).1 hab
    · exact (center_mem_positionType vertices positions a 0).mpr (Finset.mem_filter.mp ha).2
    · exact (center_mem_positionType vertices positions b 0).mpr (Finset.mem_filter.mp hb).2
  have base_right : ∀ p ∈ H.badLinkPairs y,
      (21/2210 : ℚ) ≤ unorderedWeight (typeWeight profile classify 11) p := by
    apply unordered_bound_of_incident_bound
    intro a ha b hb hab
    apply realized_pair_weight_bound H.edges classify profile real.table 11 (21/2210)
      rightCert a b (Finset.mem_filter.mp ha).1 (Finset.mem_filter.mp hb).1 hab
    · exact (center_mem_positionType vertices positions a 1).mpr (Finset.mem_filter.mp ha).2
    · exact (center_mem_positionType vertices positions b 1).mpr (Finset.mem_filter.mp hb).2
  have leftLoss := weight_lower_of_twenty_degree_eight H cover x y hne one
    (by simp) dx (typeWeight profile classify 10) base_left
    (ordinary_weight_bound H x y classify 10 single_left leftOrd)
  have rightLoss := weight_lower_of_twenty_degree_eight H cover y x hne.symm
    (by simpa only [H.codegree_comm y x] using one)
    (by simp) dy (typeWeight profile classify 11) base_right
    (ordinary_weight_bound H y x classify 11 single_right rightOrd)
  apply CustomDeletion.propertyB_of_custom_deletion H vertices positions profile real rfl loss
  · intro j _
    fin_cases j
    · change (1239/24310 : ℚ) ≤ ∑ d ∈ directedBadPairs H x, typeWeight profile classify 10 d
      rw [directed_bad_sum]
      exact leftLoss
    · change (1239/24310 : ℚ) ≤ ∑ d ∈ directedBadPairs H y, typeWeight profile classify 11 d
      rw [directed_bad_sum]
      exact rightLoss
  · intro k hk
    simp only [profile, profileAt, List.mem_cons, List.not_mem_nil, or_false] at hk
    exact if_neg hk
  · rw [total]
    norm_num

end Aris4Math.ThirtyThree.TwentyEight

#print axioms Aris4Math.ThirtyThree.TwentyEight.certificates
#print axioms Aris4Math.ThirtyThree.TwentyEight.propertyB_of_eight_eight
