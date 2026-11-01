import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows4_1 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,1,1,0,0,0],![(8,60),(8,60)]),
([0,0,0,0,0,1,0,0,0,0,0],![(14,38),(14,38)]),
([0,0,0,0,0,1,0,0,0,0,1],![(5,44),(5,44)]),
([0,0,0,0,0,1,0,0,0,1,0],![(8,34),(8,34)]),
([0,0,0,0,0,1,0,1,0,0,0],![(8,82),(8,82)]),
([0,0,0,0,0,1,1,0,0,0,0],![(9,37),(9,37)]),
([0,0,0,0,0,1,1,1,0,0,0],![(4,15),(4,15)]),
([0,0,0,0,1,0,0,0,0,0,0],![(14,65),(14,65)])
]
theorem rows4_1_checked : rows4_1.all (fun row => decide (∀ d : Degree, Matched d (some 4) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
