import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows5_4 : List (List ℕ × (Degree → Witness)) := [
([0,0,1,0,1,0,0,0,1,0,0],![(3,123),(3,123)]),
([0,1,0,0,0,0,0,0,0,0,0],![(11,103),(11,103)]),
([0,1,0,0,0,0,0,0,0,1,0],![(8,48),(8,48)]),
([0,1,0,0,0,0,0,1,0,0,0],![(8,91),(8,91)]),
([0,1,0,0,0,0,0,1,0,1,0],![(4,103),(4,103)]),
([0,1,0,0,0,0,1,0,0,0,0],![(7,32),(7,32)]),
([0,1,0,0,0,0,1,1,0,0,0],![(3,132),(3,132)]),
([0,1,0,0,1,0,0,0,0,0,0],![(7,80),(7,80)])
]
theorem rows5_4_checked : rows5_4.all (fun row => decide (∀ d : Degree, Matched d (some 5) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
