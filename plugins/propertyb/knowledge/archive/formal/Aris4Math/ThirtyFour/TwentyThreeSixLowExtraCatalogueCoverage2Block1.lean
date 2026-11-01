import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows2_1 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,1,0,0,0,0,0],![(14,7),(14,7)]),
([0,0,0,0,0,1,0,0,0,1,0],![(8,1),(8,1)]),
([0,0,0,0,0,1,0,0,1,0,0],![(9,6),(9,6)]),
([0,0,0,0,0,1,0,1,0,0,0],![(8,23),(8,23)]),
([0,0,0,0,1,0,0,0,0,0,0],![(11,86),(11,86)]),
([0,0,0,0,1,0,0,0,0,1,0],![(7,11),(7,11)]),
([0,0,0,0,1,0,0,0,1,0,0],![(8,22),(8,22)]),
([0,0,0,1,0,0,0,0,0,0,0],![(13,60),(13,60)])
]
theorem rows2_1_checked : rows2_1.all (fun row => decide (∀ d : Degree, Matched d (some 2) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
