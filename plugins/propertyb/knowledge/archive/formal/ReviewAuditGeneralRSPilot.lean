import Aris4Math.General.RS.PilotMain
import Aris4Math.General.RS.SampleLaw

/-! Independent statement and trust-basis audit for the RS Lean pilot.
The pilot below is written directly in the original finite-edge vocabulary. -/
namespace GeneralRSPilotAudit

universe u
open Aris4Math.General.RS

theorem original_seventeen_statement (V : Type u) [Finite V]
    (E : Finset (Finset V))
    (uniform : ∀ e ∈ E, e.card = 17) (edges : E.card ≤ 131072) :
    ∃ coloring : V → Bool, ∀ e ∈ E,
      (∃ red ∈ e, coloring red = true) ∧
      (∃ blue ∈ e, coloring blue = false) := by
  exact propertyB_seventeen_of_at_most_two_pow V E uniform edges

theorem general_rs_criterion (V : Type u) [Finite V]
    (E : Finset (Finset V)) (k : ℕ) (large : 2 ≤ k)
    (uniform : ∀ e ∈ E, e.card = k) (p : ℝ) (positive : 0 < p) (atMostOne : p ≤ 1)
    (numeric : 1 - (1-(1-p)^k)^((E.card : ℝ)/(2 : ℝ)^(k-1)) +
      (gamma E : ℝ)/((2 : ℝ)^(k-1))^2 *
        (∫ y in (0 : ℝ)..p, (1-y^2)^(k-1)) < 1) :
    ∃ coloring : V → Bool, ∀ e ∈ E,
      (∃ red ∈ e, coloring red = true) ∧
      (∃ blue ∈ e, coloring blue = false) := by
  exact propertyB_of_rs_bound E k large uniform positive atMostOne numeric

end GeneralRSPilotAudit

#print Aris4Math.General.RS.Uniform
#print Aris4Math.General.RS.Bichromatic
#print Aris4Math.General.RS.PropertyB
#print Aris4Math.General.RS.PilotTarget
#print Aris4Math.General.RS.singlePairs
#print Aris4Math.General.RS.gamma
#print Aris4Math.General.RS.ak
#print Aris4Math.General.RS.jk
#print Aris4Math.General.RS.FlipWitness
#print Aris4Math.General.RS.flippedAfter
#print Aris4Math.General.RS.finalColor
#print Aris4Math.General.RS.Failure
#print Aris4Math.General.RS.sampleWeight
#print Aris4Math.General.RS.sampleExpect
#print Aris4Math.General.RS.sampleProb
#print Aris4Math.General.RS.rsFailureProbability
#check Aris4Math.General.RS.rs_recoloring_failure_le
#check Aris4Math.General.RS.propertyB_of_rs_bound
#print Aris4Math.General.RS.propertyB_seventeen_of_at_most_two_pow
#print axioms Aris4Math.General.RS.sum_sampleWeight
#print axioms Aris4Math.General.RS.sampleWeight_nonneg
#print axioms Aris4Math.General.RS.rs_recoloring_failure_le
#print axioms Aris4Math.General.RS.propertyB_of_rs_bound
#print axioms Aris4Math.General.RS.propertyB_seventeen_of_at_most_two_pow
#print axioms GeneralRSPilotAudit.original_seventeen_statement
#print axioms GeneralRSPilotAudit.general_rs_criterion
