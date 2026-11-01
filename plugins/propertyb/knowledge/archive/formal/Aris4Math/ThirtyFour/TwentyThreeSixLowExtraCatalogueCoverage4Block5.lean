import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows4_5 : List (List ℕ × (Degree → Witness)) := [
([0,1,0,0,1,0,1,0,0,0,0],![(4,124),(4,124)]),
([1,0,0,0,0,0,0,0,0,0,0],![(11,130),(11,130)]),
([1,0,0,0,0,0,0,0,0,1,0],![(7,63),(7,63)]),
([1,0,0,0,0,0,0,0,1,0,0],![(7,85),(7,85)]),
([1,0,0,0,0,0,1,0,0,0,0],![(8,78),(8,78)]),
([1,0,0,0,0,0,1,0,1,0,0],![(3,101),(3,101)]),
([1,0,0,0,0,1,0,0,0,0,0],![(8,96),(8,96)]),
([1,0,0,0,0,1,0,0,0,1,0],![(3,105),(3,105)])
]
theorem rows4_5_checked : rows4_5.all (fun row => decide (∀ d : Degree, Matched d (some 4) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
