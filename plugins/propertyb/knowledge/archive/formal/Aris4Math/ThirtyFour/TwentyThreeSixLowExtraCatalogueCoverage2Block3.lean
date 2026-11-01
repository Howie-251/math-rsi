import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows2_3 : List (List ℕ × (Degree → Witness)) := [
([0,0,1,0,0,1,0,1,0,0,0],![(3,62),(3,62)]),
([0,0,1,0,1,0,0,0,0,0,0],![(7,123),(7,123)]),
([0,0,1,0,1,0,0,0,1,0,0],![(3,58),(3,58)]),
([0,1,0,0,0,0,0,0,0,0,0],![(14,104),(14,104)]),
([0,1,0,0,0,0,0,0,0,1,0],![(8,100),(8,100)]),
([0,1,0,0,0,0,0,0,1,0,0],![(9,103),(9,103)]),
([0,1,0,0,0,0,0,1,0,0,0],![(8,115),(8,115)]),
([0,1,0,0,0,0,1,0,0,0,0],![(8,121),(8,121)])
]
theorem rows2_3_checked : rows2_3.all (fun row => decide (∀ d : Degree, Matched d (some 2) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
