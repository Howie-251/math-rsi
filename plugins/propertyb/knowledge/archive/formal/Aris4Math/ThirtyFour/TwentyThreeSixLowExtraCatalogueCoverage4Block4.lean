import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows4_4 : List (List ℕ × (Degree → Witness)) := [
([0,0,1,0,1,1,0,0,0,0,0],![(4,120),(4,120)]),
([0,1,0,0,0,0,0,0,0,0,0],![(11,124),(11,124)]),
([0,1,0,0,0,0,0,0,0,1,0],![(7,36),(7,36)]),
([0,1,0,0,0,0,0,1,0,0,0],![(7,84),(7,84)]),
([0,1,0,0,0,0,1,0,0,0,0],![(8,56),(8,56)]),
([0,1,0,0,0,0,1,1,0,0,0],![(3,98),(3,98)]),
([0,1,0,0,1,0,0,0,0,0,0],![(8,97),(8,97)]),
([0,1,0,0,1,0,0,0,0,1,0],![(3,111),(3,111)])
]
theorem rows4_4_checked : rows4_4.all (fun row => decide (∀ d : Degree, Matched d (some 4) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
