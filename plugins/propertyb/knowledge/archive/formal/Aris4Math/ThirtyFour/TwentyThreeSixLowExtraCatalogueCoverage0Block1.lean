import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows0_1 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,1,0,0,0,0,0],![(11,125),(11,125)]),
([0,0,0,0,0,1,0,0,0,1,0],![(7,53),(7,53)]),
([0,0,0,0,0,1,0,1,0,0,0],![(7,92),(7,92)]),
([0,0,0,0,1,0,0,0,0,0,0],![(11,131),(11,131)]),
([0,0,0,0,1,0,0,0,0,1,0],![(7,75),(7,75)]),
([0,0,0,0,1,0,0,0,1,0,0],![(7,93),(7,93)]),
([0,0,0,1,0,0,0,0,0,0,0],![(15,116),(15,116)]),
([0,0,0,1,0,0,0,0,0,0,1],![(1,0),(1,0)])
]
theorem rows0_1_checked : rows0_1.all (fun row => decide (∀ d : Degree, Matched d (some 0) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
