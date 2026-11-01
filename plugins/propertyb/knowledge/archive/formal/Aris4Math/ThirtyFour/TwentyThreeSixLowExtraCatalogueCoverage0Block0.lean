import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows0_0 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,0,0,0,0,0],![(17,100),(17,100)]),
([0,0,0,0,0,0,0,0,0,0,1],![(13,0),(13,0)]),
([0,0,0,0,0,0,0,0,0,1,0],![(11,100),(11,100)]),
([0,0,0,0,0,0,0,0,1,0,0],![(11,104),(11,104)]),
([0,0,0,0,0,0,0,1,0,0,0],![(11,110),(11,110)]),
([0,0,0,0,0,0,1,0,0,0,0],![(11,121),(11,121)]),
([0,0,0,0,0,0,1,0,1,0,0],![(7,51),(7,51)]),
([0,0,0,0,0,0,1,1,0,0,0],![(7,73),(7,73)])
]
theorem rows0_0_checked : rows0_0.all (fun row => decide (∀ d : Degree, Matched d (some 0) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
