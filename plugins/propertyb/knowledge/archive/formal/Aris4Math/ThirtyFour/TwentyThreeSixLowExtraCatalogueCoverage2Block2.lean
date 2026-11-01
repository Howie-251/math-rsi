import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows2_2 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,1,0,0,0,0,0,0,1],![(1,60),(1,60)]),
([0,0,0,1,0,0,0,0,1,0,0],![(5,25),(5,25)]),
([0,0,0,1,0,1,0,0,0,0,0],![(5,29),(5,29)]),
([0,0,1,0,0,0,0,0,0,0,0],![(11,49),(11,49)]),
([0,0,1,0,0,0,0,0,1,0,0],![(8,99),(8,99)]),
([0,0,1,0,0,0,0,1,0,0,0],![(7,102),(7,102)]),
([0,0,1,0,0,1,0,0,0,0,0],![(8,120),(8,120)]),
([0,0,1,0,0,1,0,0,1,0,0],![(4,49),(4,49)])
]
theorem rows2_2_checked : rows2_2.all (fun row => decide (∀ d : Degree, Matched d (some 2) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
