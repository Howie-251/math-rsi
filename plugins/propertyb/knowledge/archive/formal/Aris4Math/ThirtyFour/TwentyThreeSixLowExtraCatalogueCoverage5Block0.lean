import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows5_0 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,0,0,0,0,0],![(17,0),(17,0)]),
([0,0,0,0,0,0,0,0,0,0,1],![(13,120),(13,120)]),
([0,0,0,0,0,0,0,0,0,1,0],![(14,33),(14,33)]),
([0,0,0,0,0,0,0,0,0,1,1],![(5,39),(5,39)]),
([0,0,0,0,0,0,0,0,1,0,0],![(14,34),(14,34)]),
([0,0,0,0,0,0,0,0,1,0,1],![(5,43),(5,43)]),
([0,0,0,0,0,0,0,0,1,1,0],![(9,33),(9,33)]),
([0,0,0,0,0,0,0,1,0,0,0],![(14,61),(14,61)])
]
theorem rows5_0_checked : rows5_0.all (fun row => decide (∀ d : Degree, Matched d (some 5) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
