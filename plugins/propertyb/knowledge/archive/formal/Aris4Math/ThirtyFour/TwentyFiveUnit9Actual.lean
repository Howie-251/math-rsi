import Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
import Aris4Math.ThirtyFour.TwentyFiveUnit8Actual
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Actual
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnit9Data TwentyFiveUnit9Checked
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem candidates_eq : ∀ c, (candidates c).toFinset =
  (Aris4Math.K6Classification.pairCompletion (TwentyFiveUnit8Data.catalogue c)).filter (fun T => T.card≤4) := by decide +kernel
theorem candidates_complete (c : Fin 65) (T : Finset (Fin 8))
    (mem : T ∈ Aris4Math.K6Classification.pairCompletion (TwentyFiveUnit8Data.catalogue c)) (small : T.card≤4) :
    T∈candidates c := by
  apply List.mem_toFinset.mp
  rw [candidates_eq]
  exact Finset.mem_filter.mpr ⟨mem,small⟩
theorem local_coverage (c : Fin 65) (chosen : Finset (Finset (Fin 8)))
  (mem : chosen ∈ choices (candidates c) ∅) :
  ∃ d : Fin 374, ∃ σ : Equiv.Perm (Fin 9),
    (extend (TwentyFiveUnit8Data.catalogue c) chosen).image (fun T => T.map σ.toEmbedding)=catalogue d := by
  fin_cases c
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 0) _ witnesses0 checked0 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 1) _ witnesses1 checked1 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 2) _ witnesses2 checked2 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 3) _ witnesses3 checked3 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 4) _ witnesses4 checked4 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 5) _ witnesses5 checked5 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 6) _ witnesses6 checked6 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 7) _ witnesses7 checked7 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 8) _ witnesses8 checked8 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 9) _ witnesses9 checked9 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 10) _ witnesses10 checked10 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 11) _ witnesses11 checked11 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 12) _ witnesses12 checked12 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 13) _ witnesses13 checked13 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 14) _ witnesses14 checked14 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 15) _ witnesses15 checked15 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 16) _ witnesses16 checked16 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 17) _ witnesses17 checked17 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 18) _ witnesses18 checked18 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 19) _ witnesses19 checked19 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 20) _ witnesses20 checked20 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 21) _ witnesses21 checked21 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 22) _ witnesses22 checked22 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 23) _ witnesses23 checked23 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 24) _ witnesses24 checked24 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 25) _ witnesses25 checked25 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 26) _ witnesses26 checked26 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 27) _ witnesses27 checked27 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 28) _ witnesses28 checked28 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 29) _ witnesses29 checked29 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 30) _ witnesses30 checked30 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 31) _ witnesses31 checked31 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 32) _ witnesses32 checked32 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 33) _ witnesses33 checked33 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 34) _ witnesses34 checked34 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 35) _ witnesses35 checked35 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 36) _ witnesses36 checked36 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 37) _ witnesses37 checked37 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 38) _ witnesses38 checked38 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 39) _ witnesses39 checked39 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 40) _ witnesses40 checked40 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 41) _ witnesses41 checked41 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 42) _ witnesses42 checked42 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 43) _ witnesses43 checked43 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 44) _ witnesses44 checked44 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 45) _ witnesses45 checked45 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 46) _ witnesses46 checked46 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 47) _ witnesses47 checked47 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 48) _ witnesses48 checked48 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 49) _ witnesses49 checked49 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 50) _ witnesses50 checked50 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 51) _ witnesses51 checked51 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 52) _ witnesses52 checked52 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 53) _ witnesses53 checked53 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 54) _ witnesses54 checked54 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 55) _ witnesses55 checked55 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 56) _ witnesses56 checked56 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 57) _ witnesses57 checked57 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 58) _ witnesses58 checked58 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 59) _ witnesses59 checked59 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 60) _ witnesses60 checked60 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 61) _ witnesses61 checked61 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 62) _ witnesses62 checked62 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 63) _ witnesses63 checked63 chosen mem
  · exact checked_choice catalogue (TwentyFiveUnit8Data.catalogue 64) _ witnesses64 checked64 chosen mem
theorem actual : Covers catalogue :=
  covers_succ TwentyFiveUnit8Data.catalogue catalogue candidates TwentyFiveUnit8Actual.actual candidates_complete local_coverage
end Aris4Math.ThirtyFour.TwentyFiveUnit9Actual
#print axioms Aris4Math.ThirtyFour.TwentyFiveUnit9Actual.actual
