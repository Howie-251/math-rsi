import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows1_0 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,0,0,0,0,0],![(17,61),(17,61)]),
([0,0,0,0,0,0,0,0,0,0,1],![(15,66),(15,66)]),
([0,0,0,0,0,0,0,0,0,1,0],![(11,61),(11,61)]),
([0,0,0,0,0,0,0,0,1,0,0],![(11,83),(11,83)]),
([0,0,0,0,0,0,0,1,0,0,0],![(14,14),(14,14)]),
([0,0,0,0,0,0,1,0,0,0,0],![(11,65),(11,65)]),
([0,0,0,0,0,0,1,0,1,0,0],![(7,17),(7,17)]),
([0,0,0,0,0,0,1,1,0,0,0],![(8,12),(8,12)])
]
theorem rows1_0_checked : rows1_0.all (fun row => decide (∀ d : Degree, Matched d (some 1) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
