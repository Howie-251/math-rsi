import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows3_0 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,0,0,0,0,0],![(17,33),(17,33)]),
([0,0,0,0,0,0,0,0,0,0,1],![(15,39),(15,39)]),
([0,0,0,0,0,0,0,0,0,1,0],![(14,0),(14,0)]),
([0,0,0,0,0,0,0,0,1,0,0],![(11,33),(11,33)]),
([0,0,0,0,0,0,0,1,0,0,0],![(11,60),(11,60)]),
([0,0,0,0,0,0,1,0,0,0,0],![(14,1),(14,1)]),
([0,0,0,0,0,0,1,0,0,1,0],![(9,0),(9,0)]),
([0,0,0,0,0,0,1,0,1,0,0],![(8,7),(8,7)])
]
theorem rows3_0_checked : rows3_0.all (fun row => decide (∀ d : Degree, Matched d (some 3) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
