import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows4_3 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,1,0,0,0,0,0,0,1],![(1,99),(1,99)]),
([0,0,1,0,0,0,0,0,0,0,0],![(11,120),(11,120)]),
([0,0,1,0,0,0,0,0,1,0,0],![(7,35),(7,35)]),
([0,0,1,0,0,0,0,1,0,0,0],![(7,62),(7,62)]),
([0,0,1,0,0,1,0,0,0,0,0],![(8,57),(8,57)]),
([0,0,1,0,0,1,0,1,0,0,0],![(3,102),(3,102)]),
([0,0,1,0,1,0,0,0,0,0,0],![(8,79),(8,79)]),
([0,0,1,0,1,0,0,0,1,0,0],![(3,108),(3,108)])
]
theorem rows4_3_checked : rows4_3.all (fun row => decide (∀ d : Degree, Matched d (some 4) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
