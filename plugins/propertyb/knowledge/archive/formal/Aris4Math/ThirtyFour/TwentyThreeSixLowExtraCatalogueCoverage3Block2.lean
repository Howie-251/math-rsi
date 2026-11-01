import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows3_2 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,1,0,0,0,0,0,0,1],![(1,82),(1,82)]),
([0,0,0,1,0,0,0,0,0,1,0],![(5,24),(5,24)]),
([0,0,0,1,0,0,1,0,0,0,0],![(5,28),(5,28)]),
([0,0,1,0,0,0,0,0,0,0,0],![(14,100),(14,100)]),
([0,0,1,0,0,0,0,0,0,1,0],![(9,99),(9,99)]),
([0,0,1,0,0,0,0,0,1,0,0],![(8,104),(8,104)]),
([0,0,1,0,0,0,0,1,0,0,0],![(8,110),(8,110)]),
([0,0,1,0,0,0,1,0,0,0,0],![(9,120),(9,120)])
]
theorem rows3_2_checked : rows3_2.all (fun row => decide (∀ d : Degree, Matched d (some 3) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
