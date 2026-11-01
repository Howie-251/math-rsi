import Aris4Math.ThirtyFour.TwentyFourSharedSingletons
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitData

namespace Aris4Math.ThirtyFour.TwentyFourSixLowResidualContradictions
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFourSixLowUnitData

/-- The same four-label argument handles intersecting and disjoint low triples.
The first/second-high classification must still supply the occurrence premise. -/
theorem impossible_three_typeA (H : Simple5Hypergraph (Fin 24))
    (low : Fin 6↪Fin 24) (high : Fin 3↪Fin 24) (i : Case) (kind : i=3 ∨ i=5)
    (counts : ∀T,count H low T=μ i T)
    (unit : ∀a b,a≠b→H.codegree (high a) (high b)=1)
    (occurs : ∀a j,∃e∈H.edges,lockSignature low e={a} ∧ high j∈e) : False := by
  let S : Finset (Fin 6) := {0,1,2,3}
  have small : ∀a∈S,count H low {a}≤2 := by
    intro a ha
    rw [counts]
    have numerical : ∀i : Case,i=3 ∨ i=5→∀a∈({0,1,2,3}:Finset (Fin 6)),μ i {a}≤2 := by
      decide +kernel
    exact numerical i kind a ha
  have bound := TwentyFourSharedSingletons.at_most_three H low high S unit small
    (fun a _ j=>occurs a j)
  have card : S.card=4 := by decide
  omega

/-- Three highs cannot have opposite A/B labels on every pair. -/
theorem impossible_binary_opposites (kind : Fin 3→Bool)
    (opposite : ∀i j,i≠j→kind i≠kind j) : False := by
  have injective : Function.Injective kind := fun i j eq=>by
    by_contra ne
    exact opposite i j ne eq
  have card := Fintype.card_le_of_injective kind injective
  norm_num at card
end Aris4Math.ThirtyFour.TwentyFourSixLowResidualContradictions
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowResidualContradictions.impossible_three_typeA
