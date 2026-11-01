import Aris4Math.ThirtyThree.TwentyOneTripleData

namespace Aris4Math.ThirtyThree.TwentyOneTriples

open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.TripleProfiles Aris4Math.ThirtyThree.TwentyOneDeletion
open Aris4Math.ThirtyThree.OrdinaryLink

theorem other_ne (j : Fin 3) : j ≠ other j := by fin_cases j <;> decide

/-- The ordinary family contains actual edges of the profile's singleton type.
Its two guaranteed bad pairs supply the stronger deletion at the middle lock. -/
theorem ordinary_center_deduction (H : Simple5Hypergraph (Fin 21))
    (vertices positions : Fin 3 ↪ Fin 21) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p 33) (j l : Fin 3) (hne : j ≠ l)
    (hd : H.degree (vertices j) = 7) (hc : H.codegree (vertices j) (vertices l) = 1)
    (hk : (positions j).val+1 = 11)
    (pure : ∀ t ∈ p.types, 11 ∈ t.locks → (positions l).val+1 ∉ t.locks → t.locks = [11])
    (weight : (126/12155 : ℚ) ≤ Numeric.pairWeight p ⟨[11],0⟩ ⟨[11],0⟩ 11 +
      Numeric.pairWeight p ⟨[11],0⟩ ⟨[11],0⟩ 11) :
    (252/12155 : ℚ) ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight p (positionType vertices positions) 11 d := by
  have hr : 2 ≤ (ordinaryBadPairs H (vertices j) (vertices l)).card := by
    have h := ordinary_bad_pair_budget_of_codegree_one H (vertices j) (vertices l)
      (fun he => hne (vertices.injective he)) hc
    rw [hd] at h
    norm_num only [Fintype.card_fin] at h
    omega
  have hpure (e : Finset (Fin 21)) (he : e ∈ ordinaryEdges H (vertices j) (vertices l)) :
      positionType vertices positions e = [11] := by
    obtain ⟨heH,hje,hle⟩ := (mem_ordinaryEdges _ _ _ _).mp he
    obtain ⟨t,ht,heq⟩ := List.mem_map.mp (real.table.covers e heH)
    have hj : 11 ∈ t.locks := by
      rw [heq,← hk,center_mem_positionType]
      exact hje
    have hl : (positions l).val+1 ∉ t.locks := by
      rw [heq,center_mem_positionType]
      exact hle
    exact heq.symm.trans (pure t ht hj hl)
  have hh := enhanced_directed_bad_weight_lower H (vertices j) (vertices l)
    (typeWeight p (positionType vertices positions) 11) 0 2 0 (126/12155)
    (Nat.zero_le _) hr (by norm_num) (by norm_num) ?_ ?_
  · norm_num at hh ⊢
    exact hh
  · intro S _
    unfold unorderedWeight
    apply Finset.sum_nonneg
    intro d _
    exact ProfileProbability.numeric_pairWeight_nonneg _ _ _ _
  · intro S hS
    obtain ⟨hsub,hcard⟩ := Finset.mem_powersetCard.mp (Finset.mem_filter.mp hS).1
    obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp hcard
    rw [unorderedWeight_pair _ a b hab]
    dsimp only [typeWeight]
    rw [hpure a (hsub (by simp)),hpure b (hsub (by simp))]
    exact weight

/-- One of the 24 explicit labelled configurations, now bound to the actual
three vertices of H, implies Property B. -/
theorem propertyB_of_triple_data (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (vertices : Fin 3 ↪ Fin 21) (i : Fin 24)
    (hd : ∀ j, H.degree (vertices j) = degree i j)
    (hc : ∀ j l, j ≠ l → H.codegree (vertices j) (vertices l) = codegree i j l)
    (ht : tripleCodegree H (vertices 0) (vertices 1) (vertices 2) = (data i).t) :
    PropertyB H := by
  obtain ⟨hv,hs,hboost,hbounds⟩ := certificates i
  have hm : ∀ T, count H vertices T = μ i T := by
    intro T
    rw [actual_recovered,triple_count_eq,edges33,hd 0,hd 1,hd 2,
      hc 0 1 (by decide),hc 0 2 (by decide),hc 1 2 (by decide),ht]
    rfl
  have real : RealizesProfile H vertices (positions i) (p i) 33 := by
    rw [p_eq] at hv ⊢
    exact realizes_profile H vertices (positions i) (μ i) hm _ hv
  apply CustomDeletion.propertyB_of_custom_deletion H vertices (positions i) (p i) real rfl (loss i)
  · intro j _
    have hbound := hbounds j
    dsimp only at hbound
    by_cases h : (data i).boost ∧ (positions i j).val+1=11
    · rw [if_pos h] at hbound
      obtain ⟨h7,h1,hpure,hw⟩ := hbound
      rw [loss,if_pos h,h.2]
      apply ordinary_center_deduction H vertices (positions i) (p i) real j (other j)
        (other_ne j) ((hd j).trans h7) ((hc j (other j) (other_ne j)).trans h1) h.2
      · simpa only [h.2] using hpure
      · exact hw
    · rw [if_neg h] at hbound
      rw [loss,if_neg h]
      apply realized_threshold_deduction H cover vertices (positions i) (p i) real j _
        (q (degree i j)) (threshold (p i) ((positions i j).val+1)) _ rfl
      · simp only [hd,q]; exact le_rfl
      · exact hbound.1
      · exact hbound.2
  · intro k hk
    have hx : ¬ ((data i).boost ∧ k=11) := by
      rintro ⟨hb,rfl⟩
      exact hk (hboost hb)
    simp only [loss,if_neg hx,Numeric.deduction,if_neg hk]
  · exact hs

end Aris4Math.ThirtyThree.TwentyOneTriples

#print axioms Aris4Math.ThirtyThree.TwentyOneTriples.certificates

#print axioms Aris4Math.ThirtyThree.TwentyOneTriples.propertyB_of_triple_data
