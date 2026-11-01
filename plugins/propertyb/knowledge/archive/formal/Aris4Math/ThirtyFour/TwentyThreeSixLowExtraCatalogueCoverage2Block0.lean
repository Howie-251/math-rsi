import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows2_0 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,0,0,0,0,0],![(17,34),(17,34)]),
([0,0,0,0,0,0,0,0,0,0,1],![(15,43),(15,43)]),
([0,0,0,0,0,0,0,0,0,1,0],![(11,34),(11,34)]),
([0,0,0,0,0,0,0,0,1,0,0],![(14,6),(14,6)]),
([0,0,0,0,0,0,0,1,0,0,0],![(11,82),(11,82)]),
([0,0,0,0,0,0,1,0,0,0,0],![(11,38),(11,38)]),
([0,0,0,0,0,0,1,0,1,0,0],![(8,0),(8,0)]),
([0,0,0,0,0,0,1,1,0,0,0],![(7,9),(7,9)])
]
theorem rows2_0_checked : rows2_0.all (fun row => decide (∀ d : Degree, Matched d (some 2) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
