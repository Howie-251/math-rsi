import Aris4Math.ThirtyThree.TwentyFourTripleLowData
import Aris4Math.ThirtyThree.ActualBadSlot
import Aris4Math.ThirtyThree.TwentyFourUniqueBadPair
import Aris4Math.K4Profiles

/-! Actual four-low single-triple input, including the selected real bad slots,
is connected to the conditional permutation bound. -/
namespace Aris4Math.ThirtyThree.TwentyFourTripleLow
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.TraceRecovery
open Aris4Math.ThirtyThree.TwentyFourTripleLowData
open Aris4Math.ThirtyThree.TwentyFourFourLowData (positions)

def loss (i : Fin 12) (s : Fin 4 → Fin 7) (k : ℕ) : ℚ :=
  ∑ j : Fin 4, if k = (positions i j).val+1 then (weightNumer i j (s j) : ℚ)/16796 else 0

theorem loss_at (i : Fin 12) (s : Fin 4 → Fin 7) (j : Fin 4) :
    loss i s ((positions i j).val+1) = (weightNumer i j (s j) : ℚ)/16796 := by
  unfold loss
  rw [Finset.sum_eq_single j]
  · simp
  · intro a _ aj
    have ne : (positions i j).val+1 ≠ (positions i a).val+1 := by
      intro h
      exact aj ((positions i).injective (Fin.ext (Nat.add_right_cancel h))).symm
    simp only [if_neg ne]
  · simp

theorem loss_zero (i : Fin 12) (s : Fin 4 → Fin 7) (k : ℕ)
    (outside : ∀ j, k ≠ (positions i j).val+1) : loss i s k = 0 := by
  simp [loss,outside]

theorem loss_sum (i : Fin 12) (s : Fin 4 → Fin 7) :
    (∑ k : Fin 24, loss i s (k.val+1)) =
      (∑ j : Fin 4, (weightNumer i j (s j) : ℚ))/16796 := by
  unfold loss
  rw [Finset.sum_comm,Finset.sum_div]
  apply Finset.sum_congr rfl
  intro j _
  have eq (k : Fin 24) : (k.val+1=(positions i j).val+1) ↔ k=positions i j := by
    constructor
    · intro h; exact Fin.ext (Nat.add_right_cancel h)
    · intro h; subst k; rfl
  simp only [eq,Finset.sum_ite_eq',Finset.mem_univ,if_true]

theorem strict_of_weight (i : Fin 12) (s : Fin 4 → Fin 7)
    (large : baseNumer i < 16796 + ∑ j : Fin 4, weightNumer i j (s j)) :
    (∑ k : Fin 24, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1))
        (Numeric.boundC (p i) (k.val+1) - loss i s (k.val+1)))) < 1 := by
  have each (k : Fin 24) :
      min (Numeric.boundA (p i) (k.val+1))
        (min (Numeric.boundB (p i) (k.val+1))
          (Numeric.boundC (p i) (k.val+1)-loss i s (k.val+1))) ≤
      min (Numeric.boundA (p i) (k.val+1))
        (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1))) -
        loss i s (k.val+1) := by
    by_cases locked : ∃ j, k = positions i j
    · obtain ⟨j,rfl⟩ := locked
      rw [(baseline i).2.2 j]
      exact (min_le_right _ _).trans (min_le_right _ _)
    · have zero : loss i s (k.val+1) = 0 := by
        apply loss_zero
        intro j eq
        exact locked ⟨j,Fin.ext (Nat.add_right_cancel eq)⟩
      simp only [zero,sub_zero,le_refl]
  have bound := Finset.sum_le_sum (s := Finset.univ) (fun k _ => each k)
  rw [Finset.sum_sub_distrib,(baseline i).2.1,loss_sum] at bound
  have lower : (baseNumer i : ℚ) < 16796 + ∑ j : Fin 4, (weightNumer i j (s j) : ℚ) := by
    exact_mod_cast large
  have qbound : (baseNumer i : ℚ)/16796 -
      (∑ j : Fin 4, (weightNumer i j (s j) : ℚ))/16796 < 1 := by
    linarith
  exact lt_of_le_of_lt bound qbound

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem slots_complete : ∀ j : Fin 4, ∀ T U : Finset (Fin 4),
    ActualBadSlot.Admissible counts j T U → ∃ s : Fin 7,
      (T = slotFirst j s ∧ U = slotSecond j s) ∨
      (U = slotFirst j s ∧ T = slotSecond j s) := by decide +kernel

theorem actual_counts (H : Simple5Hypergraph (Fin 24)) (S : Finset (Fin 24))
    (label : ↥S ≃ Fin 4) (unit : H.UnitCodegrees S)
    (degrees : ∀ x ∈ S, H.degree x = 6) (edges : H.edges.card = 33)
    (family : (H.multiTraces S).image (labelBlock S label) = K4Profiles.fullRepresentative4 1) :
    ∀ T, QuadProfiles.count H (lockVertices S label) T = counts T := by
  have formula : ∀ T : Finset (Fin 4),
      recoveredCount 33 6 (K4Profiles.fullRepresentative4 1) T = counts T := by
    decide +kernel
  intro T
  have h := actual_recovered_count H S label unit 6 degrees T
  rw [edges,family,formula] at h
  exact h

theorem actual_slots (H : Simple5Hypergraph (Fin 24)) (cover : H.PairCovering)
    (vertices : Fin 4 ↪ Fin 24) (degrees : ∀ j, H.degree (vertices j) = 6)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (hcounts : ∀ T, QuadProfiles.count H vertices T = counts T) :
    ∃ s : Fin 4 → Fin 7, ∀ j, ∃ E F,
      ({E,F} : Finset (Finset (Fin 24))) ∈ H.badLinkPairs (vertices j) ∧
      lockSignature vertices E = slotFirst j (s j) ∧
      lockSignature vertices F = slotSecond j (s j) := by
  have each (j : Fin 4) : ∃ s : Fin 7, ∃ E F,
      ({E,F} : Finset (Finset (Fin 24))) ∈ H.badLinkPairs (vertices j) ∧
      lockSignature vertices E = slotFirst j s ∧
      lockSignature vertices F = slotSecond j s := by
    have existsBad : (H.badLinkPairs (vertices j)).Nonempty := by
      have h := H.link_bad_pair_lower_bound cover (vertices j)
      rw [degrees j,Fintype.card_fin] at h
      apply Finset.card_pos.mp
      omega
    obtain ⟨T,U,E,F,bad,hE,hF,adm⟩ := ActualBadSlot.exists_actual_slot H vertices j
      (fun i ij => unit j i ij.symm) existsBad
    have count_eq : MultiLockRecovery.count H vertices = counts := by
      funext T
      exact hcounts T
    rw [count_eq] at adm
    obtain ⟨s,eqs | eqs⟩ := slots_complete j T U adm
    · exact ⟨s,E,F,bad,hE.trans eqs.1,hF.trans eqs.2⟩
    · exact ⟨s,F,E,by simpa [Finset.pair_comm] using bad,hF.trans eqs.1,hE.trans eqs.2⟩
  choose s h using each
  exact ⟨s,h⟩

/-- Actual four degree-six unit locks with a single triple trace suffice for
Property B at 24 vertices and 33 edges. Bad slots and positions are constructed
inside the proof, rather than supplied as additional hypotheses. -/
theorem propertyB_of_four_triple (H : Simple5Hypergraph (Fin 24)) (cover : H.PairCovering)
    (edges : H.edges.card = 33) (S : Finset (Fin 24)) (four : S.card = 4)
    (degrees : ∀ x ∈ S, H.degree x = 6) (unit : H.UnitCodegrees S)
    (B : Finset (Fin 24)) (subB : B ⊆ S) (three : B.card = 3)
    (family : H.multiTraces S = insert B ((S.powersetCard 2).filter fun P => ¬ P ⊆ B)) :
    PropertyB H := by
  obtain ⟨label,labeledB⟩ := K4Profiles.label_triple S B four subB three
  have labelled : (H.multiTraces S).image (labelBlock S label) = K4Profiles.fullRepresentative4 1 := by
    rw [labeled_traces_recovered H S unit label]
    have large : K6Classification.largeBlocks (H.multiTraces S) = {B} := by
      ext C
      simp only [K6Classification.largeBlocks,Finset.mem_filter,Finset.mem_singleton]
      constructor
      · rintro ⟨hC,big⟩
        rw [family] at hC
        rcases Finset.mem_insert.mp hC with eq | pair
        · exact eq
        · have size := (Finset.mem_powersetCard.mp (Finset.mem_filter.mp pair).1).2
          omega
      · rintro rfl
        exact ⟨by simp [family],by omega⟩
    simp [large,labeledB,K4Profiles.fullRepresentative4,K4Profiles.representative4]
  let vertices := lockVertices S label
  have member (j : Fin 4) : vertices j ∈ S := (label.symm j).property
  have vdegree (j : Fin 4) : H.degree (vertices j) = 6 := degrees _ (member j)
  have vunit (i j : Fin 4) (ij : i ≠ j) : H.codegree (vertices i) (vertices j) = 1 :=
    unit _ (member i) _ (member j) (fun h => ij (vertices.injective h))
  have hcounts : ∀ T, QuadProfiles.count H vertices T = counts T :=
    actual_counts H S label unit degrees edges labelled
  obtain ⟨s,slots⟩ := actual_slots H cover vertices vdegree vunit hcounts
  obtain ⟨i,large⟩ := order_covers s
  have real : RealizesProfile H vertices (positions i) (p i) 33 := by
    rw [p_eq]
    apply QuadProfiles.realizes_profile H vertices (positions i) counts hcounts
    rw [← p_eq]
    exact (baseline i).1
  apply CustomDeletion.propertyB_of_custom_deletion H vertices (positions i) (p i) real
    (by rfl) (loss i s)
  · intro j _
    obtain ⟨E,F,bad,hE,hF⟩ := slots j
    rw [loss_at,← slotWeight_eq]
    unfold slotWeight
    simp only [QuadProfiles.executableType_eq]
    exact ActualBadSlot.slot_weight_lower H vertices (positions i) (p i) j E F
      (slotFirst j (s j)) (slotSecond j (s j)) bad hE hF
  · intro k hk
    apply loss_zero
    intro j eq
    apply hk
    change k ∈ List.ofFn (fun j => (positions i j).val+1)
    rw [List.mem_ofFn]
    exact ⟨j,eq.symm⟩
  · exact strict_of_weight i s large

end Aris4Math.ThirtyThree.TwentyFourTripleLow

#print axioms Aris4Math.ThirtyThree.TwentyFourTripleLow.propertyB_of_four_triple
