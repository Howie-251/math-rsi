import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows2_5 : List (List ℕ × (Degree → Witness)) := [
([0,1,0,1,0,0,0,0,0,0,0],![(5,117),(5,117)]),
([1,0,0,0,0,0,0,0,0,0,0],![(11,90),(11,90)]),
([1,0,0,0,0,0,0,0,0,1,0],![(7,105),(7,105)]),
([1,0,0,0,0,0,0,0,1,0,0],![(8,114),(8,114)]),
([1,0,0,0,0,0,1,0,0,0,0],![(7,126),(7,126)]),
([1,0,0,0,0,0,1,0,1,0,0],![(3,59),(3,59)]),
([1,0,0,0,0,1,0,0,0,0,0],![(8,135),(8,135)]),
([1,0,0,0,0,1,0,0,0,1,0],![(3,63),(3,63)])
]
theorem rows2_5_checked : rows2_5.all (fun row => decide (∀ d : Degree, Matched d (some 2) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
