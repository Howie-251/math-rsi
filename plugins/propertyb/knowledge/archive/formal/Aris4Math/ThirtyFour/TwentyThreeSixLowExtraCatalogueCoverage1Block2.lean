import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows1_2 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,1,0,0,0,0,0,0,1],![(1,33),(1,33)]),
([0,0,0,1,0,0,0,1,0,0,0],![(5,26),(5,26)]),
([0,0,0,1,1,0,0,0,0,0,0],![(5,30),(5,30)]),
([0,0,1,0,0,0,0,0,0,0,0],![(11,72),(11,72)]),
([0,0,1,0,0,0,0,0,1,0,0],![(7,108),(7,108)]),
([0,0,1,0,0,0,0,1,0,0,0],![(8,106),(8,106)]),
([0,0,1,0,0,1,0,0,0,0,0],![(7,129),(7,129)]),
([0,0,1,0,0,1,0,1,0,0,0],![(3,31),(3,31)])
]
theorem rows1_2_checked : rows1_2.all (fun row => decide (∀ d : Degree, Matched d (some 1) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
