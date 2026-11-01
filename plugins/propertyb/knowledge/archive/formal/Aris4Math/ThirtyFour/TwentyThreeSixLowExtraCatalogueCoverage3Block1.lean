import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows3_1 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,1,1,0,0,0],![(8,15),(8,15)]),
([0,0,0,0,0,1,0,0,0,0,0],![(11,37),(11,37)]),
([0,0,0,0,0,1,0,0,0,1,0],![(8,6),(8,6)]),
([0,0,0,0,0,1,0,1,0,0,0],![(7,3),(7,3)]),
([0,0,0,0,1,0,0,0,0,0,0],![(11,64),(11,64)]),
([0,0,0,0,1,0,0,0,0,1,0],![(8,14),(8,14)]),
([0,0,0,0,1,0,0,0,1,0,0],![(7,5),(7,5)]),
([0,0,0,1,0,0,0,0,0,0,0],![(13,82),(13,82)])
]
theorem rows3_1_checked : rows3_1.all (fun row => decide (∀ d : Degree, Matched d (some 3) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
