import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows5_1 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,0,1,0,0,1],![(5,66),(5,66)]),
([0,0,0,0,0,0,0,1,0,1,0],![(9,60),(9,60)]),
([0,0,0,0,0,0,0,1,1,0,0],![(9,82),(9,82)]),
([0,0,0,0,0,0,1,0,0,0,0],![(11,0),(11,0)]),
([0,0,0,0,0,0,1,0,1,0,0],![(8,38),(8,38)]),
([0,0,0,0,0,0,1,1,0,0,0],![(8,65),(8,65)]),
([0,0,0,0,0,0,1,1,1,0,0],![(4,0),(4,0)]),
([0,0,0,0,0,1,0,0,0,0,0],![(11,6),(11,6)])
]
theorem rows5_1_checked : rows5_1.all (fun row => decide (∀ d : Degree, Matched d (some 5) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
