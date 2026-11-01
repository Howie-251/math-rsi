import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows4_0 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,0,0,0,0,0],![(17,1),(17,1)]),
([0,0,0,0,0,0,0,0,0,0,1],![(13,99),(13,99)]),
([0,0,0,0,0,0,0,0,0,1,0],![(11,1),(11,1)]),
([0,0,0,0,0,0,0,0,1,0,0],![(11,7),(11,7)]),
([0,0,0,0,0,0,0,1,0,0,0],![(11,15),(11,15)]),
([0,0,0,0,0,0,1,0,0,0,0],![(14,37),(14,37)]),
([0,0,0,0,0,0,1,0,0,0,1],![(5,40),(5,40)]),
([0,0,0,0,0,0,1,0,1,0,0],![(8,33),(8,33)])
]
theorem rows4_0_checked : rows4_0.all (fun row => decide (∀ d : Degree, Matched d (some 4) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
