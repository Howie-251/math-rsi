import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows3_3 : List (List ℕ × (Degree → Witness)) := [
([0,0,1,0,0,0,1,0,1,0,0],![(4,33),(4,33)]),
([0,0,1,0,0,0,1,1,0,0,0],![(4,60),(4,60)]),
([0,0,1,0,0,1,0,0,0,0,0],![(8,125),(8,125)]),
([0,0,1,0,0,1,0,0,0,1,0],![(4,37),(4,37)]),
([0,0,1,0,0,1,0,1,0,0,0],![(3,92),(3,92)]),
([0,0,1,0,1,0,0,0,0,0,0],![(8,131),(8,131)]),
([0,0,1,0,1,0,0,0,0,1,0],![(4,64),(4,64)]),
([0,0,1,0,1,0,0,0,1,0,0],![(3,93),(3,93)])
]
theorem rows3_3_checked : rows3_3.all (fun row => decide (∀ d : Degree, Matched d (some 3) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
