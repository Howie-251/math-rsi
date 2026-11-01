import Aris4Math.ThirtyThree.TwentyFourMixedNumeric
import Aris4Math.ThirtyThree.TwentyFourSelection

namespace Aris4Math.ThirtyThree.TwentyFourMixed
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TwentyFourMixedData
open Aris4Math.ThirtyThree.TwentyFourMixedFacts
open Aris4Math.ThirtyThree.TwentyFourMixedNumeric

theorem actual_profile (H : Simple5Hypergraph (Fin 24))
    (vertices : Fin 5 ↪ Fin 24) (c : Config)
    (actual : ∀ T, count H vertices T = counts (family c) T) :
    RealizesProfile H vertices (positions c) (p c) 33 := by
  have valid := profile_valid c
  rw [profiles_calculated, calculated_eq_profile] at valid ⊢
  refine ⟨rfl, valid, ?_, TripleProfiles.table_pruneZero _ _ _
    (raw_table H vertices (positions c) labels labels_nodup labels_all
      (counts (family c)) actual _)⟩
  simp [profile, TripleProfiles.pruneZero, rawProfile, canonicalType]

theorem actual_classification (H : Simple5Hypergraph (Fin 24))
    (vertices : Fin 5 ↪ Fin 24) (edges33 : H.edges.card = 33)
    (degrees : ∀ j, H.degree (vertices j) = degreeData j)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1) :
    ∃ t : Fin 32, ∀ T, count H vertices T = counts t T := by
  have hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low T := by
    apply upper_eq_of_low_data
    · simpa only [low, if_pos rfl] using edges33.symm
    · intro i
      rw [degrees]
      fin_cases i <;> decide +kernel
    · intro i j hij
      rw [unit i j hij]
      simp [low, Finset.card_pair hij]
  obtain ⟨t, ht⟩ := FiveLockClassification.actual_recovered_in_table
    H vertices unit low hlow
  exact ⟨t, fun T => (ht T).trans (counts_eq_recovered t T).symm⟩

theorem dual_lower (H : Simple5Hypergraph (Fin 24))
    (vertices : Fin 5 ↪ Fin 24) (c : Config)
    (real : RealizesProfile H vertices (positions c) (p c) 33) (j : Fin 5) :
    dualLoss c j ≤ ∑ d ∈ directedBadPairs H (vertices j),
      typeWeight (p c) (positionType vertices (positions c)) ((positions c j).val+1) d := by
  exact RefinedDeletion.realized_refined_deduction H vertices (positions c) (p c) real j
    (avoided j) (multipliers c j) (quotas c j) (dualLoss c j)
    (dual_exact c j).1 (dual_exact c j).2.1 (dual_exact c j).2.2.1
    (dual_exact c j).2.2.2

/-- A low center supplies a real bad slot before positions are selected. Its
two ordered weights are valid at every later position configuration. -/
theorem actual_low_slot (H : Simple5Hypergraph (Fin 24)) (cover : H.PairCovering)
    (vertices : Fin 5 ↪ Fin 24) (t : Fin 32)
    (actual : ∀ T, count H vertices T = counts t T)
    (degrees : ∀ j, H.degree (vertices j) = degreeData j)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (j : Fin 2)
    (avoid : ∀ P ∈ H.badLinkPairs (vertices (j.castLE (by omega))),
      ∃ E ∈ P, Disjoint E (({2,3,4} : Finset (Fin 5)).image vertices)) :
    ∃ b : Fin 8, ∀ c : Config,
      slotWeight c j (slot t j b) ≤
        ∑ d ∈ directedBadPairs H (vertices (j.castLE (by omega))),
          typeWeight (p c) (positionType vertices (positions c))
            ((positions c (j.castLE (by omega))).val+1) d := by
  let j5 : Fin 5 := j.castLE (by omega)
  have degree6 : H.degree (vertices j5) = 6 := by
    rw [degrees]
    exact if_pos j.isLt
  have cardpos := H.link_bad_pair_lower_bound cover (vertices j5)
  rw [Fintype.card_fin, degree6] at cardpos
  have nonempty : (H.badLinkPairs (vertices j5)).Nonempty :=
    Finset.card_pos.mp (by norm_num at cardpos ⊢; omega)
  obtain ⟨T,U,E,F,bad,hE,hF,adm⟩ := ActualBadSlot.exists_actual_slot H vertices j5
    (fun i hij => unit j5 i (Ne.symm hij)) nonempty
  have avoidTU := ActualBadSlot.slot_avoids_of_pair_avoids vertices E F {2,3,4}
    (avoid {E,F} bad)
  rw [hE,hF] at avoidTU
  have adm' : ActualBadSlot.Admissible (counts t) j5 T U := by
    simpa only [ActualBadSlot.Admissible, actual] using adm
  obtain ⟨b,hb⟩ := slot_complete t j T U adm' avoidTU
  refine ⟨b, fun c => ?_⟩
  have bound := ActualBadSlot.slot_weight_lower H vertices (positions c) (p c) j5
    E F T U bad hE hF
  rcases hb with ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩
  · simpa only [slotWeight, executableType_eq, j5] using bound
  · simpa only [slotWeight, executableType_eq, j5, add_comm] using bound

/-- Complete mixed five-lock caller: actual types and actual bad pairs select
the finite exact witness; no numeric or profile premise is exposed. -/
theorem propertyB_of_structured_locks (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (vertices : Fin 5 ↪ Fin 24)
    (degrees : ∀ j, H.degree (vertices j) = degreeData j)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (avoid : ∀ j : Fin 2, ∀ P ∈ H.badLinkPairs (vertices (j.castLE (by omega))),
      ∃ E ∈ P, Disjoint E (({2,3,4} : Finset (Fin 5)).image vertices)) : PropertyB H := by
  classical
  obtain ⟨t,actual⟩ := actual_classification H vertices edges33 degrees unit
  have slots := fun j => actual_low_slot H cover vertices t actual degrees unit j (avoid j)
  choose b lower using slots
  let r := choice t (b 0) (b 1)
  let c := configOf r
  have chosen := choice_exact t (b 0) (b 1)
  have real : RealizesProfile H vertices (positions c) (p c) 33 :=
    actual_profile H vertices c (fun T => by rw [chosen.1]; exact actual T)
  apply CustomDeletion.propertyB_of_custom_deletion H vertices (positions c) (p c)
    real (by rw [profiles_calculated, calculated_eq_profile]; rfl) (loss r)
  · intro j _
    rw [loss_at]
    by_cases hj : j.val < 2
    · let j2 : Fin 2 := ⟨j.val,hj⟩
      have jeq : j2.castLE (by omega) = j := Fin.ext rfl
      have bvec : ∀ i : Fin 2, (![b 0,b 1] i) = b i := by
        intro i
        fin_cases i <;> rfl
      have bound := chosen.2.1 j2
      split_ifs at bound with uses
      · rw [bvec,jeq] at bound
        have actualBound := lower j2 c
        rw [jeq] at actualBound
        exact bound.trans actualBound
      · rw [jeq] at bound
        exact bound.trans (dual_lower H vertices c real j)
    · exact (chosen.2.2 j (by omega)).trans (dual_lower H vertices c real j)
  · exact loss_zeroOutside r
  · exact strict r

theorem propertyB_of_mixed_locks (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (mixed : TwentyFourSelection.MixedLocks H) : PropertyB H := by
  obtain ⟨x,y,z,u,v,hcard,dx,dy,dz,du,dv,unit,avoidX,avoidY⟩ := mixed
  let fn : Fin 5 → Fin 24 := ![x,y,z,u,v]
  have imageAll : Finset.univ.image fn = ({x,y,z,u,v} : Finset (Fin 24)) := by
    have univ5 : (Finset.univ : Finset (Fin 5)) = {0,1,2,3,4} := by decide
    rw [univ5]
    simp [fn]
  have inj : Function.Injective fn := by
    have hinj : Set.InjOn fn (Finset.univ : Finset (Fin 5)) :=
      Finset.card_image_iff.mp (by rw [imageAll,hcard]; rfl)
    exact fun a b h => hinj (Finset.mem_univ a) (Finset.mem_univ b) h
  let vertices : Fin 5 ↪ Fin 24 := ⟨fn,inj⟩
  have inSet (j : Fin 5) : vertices j ∈ ({x,y,z,u,v} : Finset (Fin 24)) := by
    rw [← imageAll]
    exact Finset.mem_image.mpr ⟨j,Finset.mem_univ j,rfl⟩
  have degrees : ∀ j, H.degree (vertices j) = degreeData j := by
    intro j
    fin_cases j
    · exact dx
    · exact dy
    · exact dz
    · exact du
    · exact dv
  have unit' : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1 :=
    fun i j hij => unit _ (inSet i) _ (inSet j) (vertices.injective.ne hij)
  have imageHigh : (({2,3,4} : Finset (Fin 5)).image vertices) = {z,u,v} := by
    simp [vertices,fn]
  apply propertyB_of_structured_locks H cover edges33 vertices degrees unit'
  intro j P hP
  rw [imageHigh]
  fin_cases j
  · exact avoidX P hP
  · exact avoidY P hP

theorem propertyB_of_many_sevens (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (many : 18 ≤ (TwentyFourSelection.sevenVertices H).card) : PropertyB H := by
  exact propertyB_of_mixed_locks H cover edges33
    (TwentyFourSelection.mixed_locks_of_many_sevens H cover edges33 (Fintype.card_fin 24) many)

end Aris4Math.ThirtyThree.TwentyFourMixed

#print axioms Aris4Math.ThirtyThree.TwentyFourMixed.propertyB_of_structured_locks
#print axioms Aris4Math.ThirtyThree.TwentyFourMixed.propertyB_of_mixed_locks
#print axioms Aris4Math.ThirtyThree.TwentyFourMixed.propertyB_of_many_sevens
