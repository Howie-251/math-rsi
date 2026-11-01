import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows0_4 : List (List ℕ × (Degree → Witness)) := [
([0,1,1,0,0,0,0,0,0,0,0],![(9,48),(9,48)]),
([0,1,1,0,0,0,0,1,0,0,0],![(4,110),(4,110)]),
([0,1,1,0,1,0,0,0,0,0,0],![(4,131),(4,131)]),
([1,0,0,0,0,0,0,0,0,0,0],![(14,72),(14,72)]),
([1,0,0,0,0,0,0,0,0,0,1],![(5,68),(5,68)]),
([1,0,0,0,0,0,0,0,0,1,0],![(8,70),(8,70)]),
([1,0,0,0,0,0,0,0,1,0,0],![(8,89),(8,89)]),
([1,0,0,0,0,0,1,0,0,0,0],![(8,77),(8,77)])
]
theorem rows0_4_checked : rows0_4.all (fun row => decide (∀ d : Degree, Matched d (some 0) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
