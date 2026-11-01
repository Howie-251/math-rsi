import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage0
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueCoverage6
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
theorem coverage (b : Pattern) (values : List ℕ) (mem : values∈catalogue b) (d : Degree)
    (normalized : b=none ∨ b=some 0) : ∃ w : Witness, Matched d b values w := by
  rcases normalized with rfl | rfl
  · exact coverage6 values mem d
  · exact coverage0 values mem d
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
