import Aris4Math.ThirtyThree.TwentyThreeFourLowUnitNumeric
import Aris4Math.ThirtyThree.TwentyThreeFourLowUnitChoice

namespace Aris4Math.ThirtyThree.TwentyThreeFourLowUnit
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open TwentyThreeFourLowUnitData TwentyThreeFourLowUnitFacts
open TwentyThreeFourLowUnitNumeric TwentyThreeFourLowUnitChoice

theorem actual_profile (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 4 ↪ Fin 23)
    (c : Config) (actual : ∀ T, QuadProfiles.count H vertices T = counts (family c) T) :
    RealizesProfile H vertices (positions c) (p c) 33 := by
  have valid := profile_valid c
  rw [profiles_calculated,calculated_eq_profile] at valid ⊢
  exact QuadProfiles.realizes_profile H vertices (positions c) (counts (family c)) actual _ valid

theorem strict (r : Row) :
    (∑ k : Fin 23, min (Numeric.boundA (p (configOf r)) (k.val+1))
      (min (Numeric.boundB (p (configOf r)) (k.val+1))
        (Numeric.boundC (p (configOf r)) (k.val+1) - loss r (k.val+1)))) < 1 := by
  have heq : (∑ k : Fin 23, min (Numeric.boundA (p (configOf r)) (k.val+1))
      (min (Numeric.boundB (p (configOf r)) (k.val+1))
        (Numeric.boundC (p (configOf r)) (k.val+1) - loss r (k.val+1)))) =
      ∑ k : Fin 23, min (abc (configOf r) k).1
        (min (abc (configOf r) k).2.1 ((abc (configOf r) k).2.2 - loss r (k.val+1))) := by
    apply Finset.sum_congr rfl
    intro k _
    rw [(abc_exact (configOf r) k).1, (abc_exact (configOf r) k).2.1,
      (abc_exact (configOf r) k).2.2]
  rw [heq]
  exact strict_cached r

/-- Each center supplies an actual bad pair before the positions are chosen.
The same pair gives its two ordered weights at every later configuration. -/
theorem actual_slot (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (vertices : Fin 4 ↪ Fin 23) (k : Fin 3)
    (actual : ∀ T, QuadProfiles.count H vertices T = counts k T)
    (degrees : ∀ j, H.degree (vertices j) = 6)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (j : Fin 4) :
    ∃ b : Fin 7, ∀ c : Config, family c = k → weights c j b ≤
      ∑ d ∈ directedBadPairs H (vertices j),
        typeWeight (p c) (positionType vertices (positions c)) ((positions c j).val+1) d := by
  have cardpos := H.link_bad_pair_lower_bound cover (vertices j)
  rw [Fintype.card_fin,degrees] at cardpos
  have nonempty : (H.badLinkPairs (vertices j)).Nonempty :=
    Finset.card_pos.mp (by norm_num at cardpos ⊢; omega)
  obtain ⟨T,U,E,F,bad,hE,hF,adm⟩ := ActualBadSlot.exists_actual_slot H vertices j
    (fun i ij => unit j i (Ne.symm ij)) nonempty
  have actual' : ∀ T, MultiLockRecovery.count H vertices T = counts k T := actual
  have adm' : ActualBadSlot.Admissible (counts k) j T U := by
    simpa only [ActualBadSlot.Admissible,actual'] using adm
  obtain ⟨b,hb⟩ := slot_complete k j T U adm'
  refine ⟨b,fun c hc => ?_⟩
  rw [weights_exact,hc]
  have bound := ActualBadSlot.slot_weight_lower H vertices (positions c) (p c) j E F T U
    bad hE hF
  rcases hb with ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩
  · simpa only [QuadProfiles.executableType_eq] using bound
  · simpa only [QuadProfiles.executableType_eq,add_comm] using bound

/-- All three unit-codegree representatives are handled using real bad pairs,
with no selected slots or positional witnesses left as assumptions. -/
theorem propertyB_of_local_counts (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (vertices : Fin 4 ↪ Fin 23) (degrees : ∀ j, H.degree (vertices j) = 6)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (k : Fin 3) (actual : ∀ T, QuadProfiles.count H vertices T = counts k T) : PropertyB H := by
  classical
  have slots := fun j => actual_slot H cover vertices k actual degrees unit j
  choose b lower using slots
  let r := choice k (b 0) (b 1) (b 2) (b 3)
  let c := configOf r
  have chosen := choice_exact k (b 0) (b 1) (b 2) (b 3)
  have real : RealizesProfile H vertices (positions c) (p c) 33 :=
    actual_profile H vertices c (fun T => by rw [chosen.1]; exact actual T)
  apply CustomDeletion.propertyB_of_custom_deletion H vertices (positions c) (p c) real
    (by rw [profiles_calculated,calculated_eq_profile]; rfl) (loss r)
  · intro j _
    rw [loss_at,chosen.2 j]
    have bv : (![b 0,b 1,b 2,b 3] j) = b j := by fin_cases j <;> rfl
    rw [bv]
    exact lower j c chosen.1
  · exact loss_zeroOutside r
  · exact strict r

/-- Interface to the complete 50-representative four-low classification. -/
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (vertices : Fin 4 ↪ Fin 23) (degrees : ∀ j, H.degree (vertices j) = 6)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (k : Fin 3) (actual : ∀ T, QuadProfiles.count H vertices T =
      TwentyThreeFourLowCatalog.counts (k.castLE (by omega)) T) : PropertyB H := by
  apply propertyB_of_local_counts H cover vertices degrees unit k
  intro T
  exact (actual T).trans (counts_eq_catalog k T).symm

end Aris4Math.ThirtyThree.TwentyThreeFourLowUnit
#print axioms Aris4Math.ThirtyThree.TwentyThreeFourLowUnit.propertyB_of_counts
