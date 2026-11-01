import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows4_2 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,1,0,0,0,0,0,1],![(5,67),(5,67)]),
([0,0,0,0,1,0,0,0,0,1,0],![(8,61),(8,61)]),
([0,0,0,0,1,0,0,0,1,0,0],![(8,83),(8,83)]),
([0,0,0,0,1,0,1,0,0,0,0],![(9,64),(9,64)]),
([0,0,0,0,1,0,1,0,1,0,0],![(4,7),(4,7)]),
([0,0,0,0,1,1,0,0,0,0,0],![(9,86),(9,86)]),
([0,0,0,0,1,1,0,0,0,1,0],![(4,1),(4,1)]),
([0,0,0,1,0,0,0,0,0,0,0],![(15,28),(15,28)])
]
theorem rows4_2_checked : rows4_2.all (fun row => decide (∀ d : Degree, Matched d (some 4) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
