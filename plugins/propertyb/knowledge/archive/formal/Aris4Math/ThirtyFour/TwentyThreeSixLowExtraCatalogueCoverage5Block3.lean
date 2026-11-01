import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows5_3 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,1,0,0,0,0,0,0,1],![(1,120),(1,120)]),
([0,0,1,0,0,0,0,0,0,0,0],![(11,99),(11,99)]),
([0,0,1,0,0,0,0,0,1,0,0],![(8,49),(8,49)]),
([0,0,1,0,0,0,0,1,0,0,0],![(8,72),(8,72)]),
([0,0,1,0,0,0,0,1,1,0,0],![(4,99),(4,99)]),
([0,0,1,0,0,1,0,0,0,0,0],![(7,31),(7,31)]),
([0,0,1,0,0,1,0,1,0,0,0],![(3,129),(3,129)]),
([0,0,1,0,1,0,0,0,0,0,0],![(7,58),(7,58)])
]
theorem rows5_3_checked : rows5_3.all (fun row => decide (∀ d : Degree, Matched d (some 5) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
