import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows1_4 : List (List ℕ × (Degree → Witness)) := [
([0,1,0,0,1,0,0,0,0,0,0],![(8,133),(8,133)]),
([0,1,0,0,1,0,0,0,0,1,0],![(3,36),(3,36)]),
([0,1,0,0,1,0,0,1,0,0,0],![(4,91),(4,91)]),
([1,0,0,0,0,0,0,0,0,0,0],![(14,110),(14,110)]),
([1,0,0,0,0,0,0,0,0,1,0],![(8,107),(8,107)]),
([1,0,0,0,0,0,0,0,1,0,0],![(8,113),(8,113)]),
([1,0,0,0,0,0,0,1,0,0,0],![(9,109),(9,109)]),
([1,0,0,0,0,0,1,0,0,0,0],![(8,128),(8,128)])
]
theorem rows1_4_checked : rows1_4.all (fun row => decide (∀ d : Degree, Matched d (some 1) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
