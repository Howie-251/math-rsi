import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows0_2 : List (List ℕ × (Degree → Witness)) := [
([0,0,1,0,0,0,0,0,0,0,0],![(14,48),(14,48)]),
([0,0,1,0,0,0,0,0,0,0,1],![(5,42),(5,42)]),
([0,0,1,0,0,0,0,0,1,0,0],![(8,46),(8,46)]),
([0,0,1,0,0,0,0,1,0,0,0],![(8,69),(8,69)]),
([0,0,1,0,0,1,0,0,0,0,0],![(8,54),(8,54)]),
([0,0,1,0,0,1,0,1,0,0,0],![(3,3),(3,3)]),
([0,0,1,0,1,0,0,0,0,0,0],![(8,76),(8,76)]),
([0,0,1,0,1,0,0,0,1,0,0],![(3,5),(3,5)])
]
theorem rows0_2_checked : rows0_2.all (fun row => decide (∀ d : Degree, Matched d (some 0) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
