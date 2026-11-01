import Aris4Math.ThirtyFour.TwentyFiveUnit8Checked
import Aris4Math.ThirtyFour.TwentyFiveUnit7Actual
namespace Aris4Math.ThirtyFour.TwentyFiveUnit8Actual
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnit8Data TwentyFiveUnit8Checked
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem candidates_eq : ∀ c, (candidates c).toFinset =
  (Aris4Math.K6Classification.pairCompletion (TwentyFiveUnit7Data.catalogue c)).filter (fun T => T.card≤4) := by decide +kernel
theorem candidates_complete (c : Fin 22) (T : Finset (Fin 7))
    (mem : T ∈ Aris4Math.K6Classification.pairCompletion (TwentyFiveUnit7Data.catalogue c)) (small : T.card≤4) :
    T∈candidates c := by
  apply List.mem_toFinset.mp
  rw [candidates_eq]
  exact Finset.mem_filter.mpr ⟨mem,small⟩
theorem local_coverage (c : Fin 22) (chosen : Finset (Finset (Fin 7)))
  (mem : chosen ∈ choices (candidates c) ∅) :
  ∃ d : Fin 65, ∃ σ : Equiv.Perm (Fin 8),
    (extend (TwentyFiveUnit7Data.catalogue c) chosen).image (fun T => T.map σ.toEmbedding)=catalogue d := by
  fin_cases c
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 0) _ witnesses0 checked0 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 1) _ witnesses1 checked1 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 2) _ witnesses2 checked2 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 3) _ witnesses3 checked3 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 4) _ witnesses4 checked4 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 5) _ witnesses5 checked5 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 6) _ witnesses6 checked6 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 7) _ witnesses7 checked7 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 8) _ witnesses8 checked8 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 9) _ witnesses9 checked9 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 10) _ witnesses10 checked10 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 11) _ witnesses11 checked11 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 12) _ witnesses12 checked12 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 13) _ witnesses13 checked13 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 14) _ witnesses14 checked14 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 15) _ witnesses15 checked15 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 16) _ witnesses16 checked16 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 17) _ witnesses17 checked17 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 18) _ witnesses18 checked18 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 19) _ witnesses19 checked19 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 20) _ witnesses20 checked20 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit7Data.catalogue 21) _ witnesses21 checked21 chosen mem
theorem actual : Covers catalogue :=
  covers_succ TwentyFiveUnit7Data.catalogue catalogue candidates TwentyFiveUnit7Actual.actual candidates_complete local_coverage
end Aris4Math.ThirtyFour.TwentyFiveUnit8Actual
#print axioms Aris4Math.ThirtyFour.TwentyFiveUnit8Actual.actual
