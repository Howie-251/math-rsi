import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows2_4 : List (List ℕ × (Degree → Witness)) := [
([0,1,0,0,0,0,1,0,1,0,0],![(4,38),(4,38)]),
([0,1,0,0,0,0,1,1,0,0,0],![(3,73),(3,73)]),
([0,1,0,0,0,1,0,0,0,0,0],![(9,124),(9,124)]),
([0,1,0,0,0,1,0,0,0,1,0],![(4,34),(4,34)]),
([0,1,0,0,0,1,0,1,0,0,0],![(4,82),(4,82)]),
([0,1,0,0,1,0,0,0,0,0,0],![(8,136),(8,136)]),
([0,1,0,0,1,0,0,0,0,1,0],![(3,75),(3,75)]),
([0,1,0,0,1,0,0,0,1,0,0],![(4,86),(4,86)])
]
theorem rows2_4_checked : rows2_4.all (fun row => decide (∀ d : Degree, Matched d (some 2) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
