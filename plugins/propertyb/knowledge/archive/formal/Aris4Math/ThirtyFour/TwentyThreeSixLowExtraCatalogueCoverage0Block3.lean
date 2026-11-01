import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows0_3 : List (List ℕ × (Degree → Witness)) := [
([0,1,0,0,0,0,0,0,0,0,0],![(14,49),(14,49)]),
([0,1,0,0,0,0,0,0,0,0,1],![(5,45),(5,45)]),
([0,1,0,0,0,0,0,0,0,1,0],![(8,47),(8,47)]),
([0,1,0,0,0,0,0,1,0,0,0],![(8,88),(8,88)]),
([0,1,0,0,0,0,1,0,0,0,0],![(8,55),(8,55)]),
([0,1,0,0,0,0,1,1,0,0,0],![(3,9),(3,9)]),
([0,1,0,0,1,0,0,0,0,0,0],![(8,94),(8,94)]),
([0,1,0,0,1,0,0,0,0,1,0],![(3,11),(3,11)])
]
theorem rows0_3_checked : rows0_3.all (fun row => decide (∀ d : Degree, Matched d (some 0) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
