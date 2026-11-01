import Aris4Math.ThirtyFour.TwentyFiveUnit7Checked
namespace Aris4Math.ThirtyFour.TwentyFiveUnit7Actual
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnit7Data TwentyFiveUnit7Checked
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem candidates_eq : ∀ c, (candidates c).toFinset =
  (Aris4Math.K6Classification.pairCompletion (Aris4Math.K6Classification.representative c)).filter (fun T => T.card≤4) := by decide +kernel
theorem candidates_complete (c : Fin 9) (T : Finset (Fin 6))
    (mem : T ∈ Aris4Math.K6Classification.pairCompletion (Aris4Math.K6Classification.representative c)) (small : T.card≤4) :
    T∈candidates c := by
  apply List.mem_toFinset.mp
  rw [candidates_eq]
  exact Finset.mem_filter.mpr ⟨mem,small⟩
theorem local_coverage (c : Fin 9) (chosen : Finset (Finset (Fin 6)))
  (mem : chosen ∈ choices (candidates c) ∅) :
  ∃ d : Fin 22, ∃ σ : Equiv.Perm (Fin 7),
    (extend (Aris4Math.K6Classification.representative c) chosen).image (fun T => T.map σ.toEmbedding)=catalogue d := by
  fin_cases c
  · exact checked_choice catalogue (Aris4Math.K6Classification.representative 0) _ witnesses0 checked0 chosen mem
  · exact checked_choice catalogue (Aris4Math.K6Classification.representative 1) _ witnesses1 checked1 chosen mem
  · exact checked_choice catalogue (Aris4Math.K6Classification.representative 2) _ witnesses2 checked2 chosen mem
  · exact checked_choice catalogue (Aris4Math.K6Classification.representative 3) _ witnesses3 checked3 chosen mem
  · exact checked_choice catalogue (Aris4Math.K6Classification.representative 4) _ witnesses4 checked4 chosen mem
  · exact checked_choice catalogue (Aris4Math.K6Classification.representative 5) _ witnesses5 checked5 chosen mem
  · exact checked_choice catalogue (Aris4Math.K6Classification.representative 6) _ witnesses6 checked6 chosen mem
  · exact checked_choice catalogue (Aris4Math.K6Classification.representative 7) _ witnesses7 checked7 chosen mem
  · exact checked_choice catalogue (Aris4Math.K6Classification.representative 8) _ witnesses8 checked8 chosen mem
theorem actual : Covers catalogue :=
  covers_succ Aris4Math.K6Classification.representative catalogue candidates six_covers candidates_complete local_coverage
end Aris4Math.ThirtyFour.TwentyFiveUnit7Actual
#print axioms Aris4Math.ThirtyFour.TwentyFiveUnit7Actual.actual
