import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows1_3 : List (List ℕ × (Degree → Witness)) := [
([0,0,1,0,1,0,0,0,0,0,0],![(8,127),(8,127)]),
([0,0,1,0,1,0,0,0,1,0,0],![(3,35),(3,35)]),
([0,0,1,0,1,0,0,1,0,0,0],![(4,72),(4,72)]),
([0,1,0,0,0,0,0,0,0,0,0],![(11,91),(11,91)]),
([0,1,0,0,0,0,0,0,0,1,0],![(7,111),(7,111)]),
([0,1,0,0,0,0,0,1,0,0,0],![(8,112),(8,112)]),
([0,1,0,0,0,0,1,0,0,0,0],![(7,132),(7,132)]),
([0,1,0,0,0,0,1,1,0,0,0],![(3,32),(3,32)])
]
theorem rows1_3_checked : rows1_3.all (fun row => decide (∀ d : Degree, Matched d (some 1) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
