import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows3_4 : List (List ℕ × (Degree → Witness)) := [
([0,0,1,1,0,0,0,0,0,0,0],![(5,116),(5,116)]),
([0,1,0,0,0,0,0,0,0,0,0],![(11,48),(11,48)]),
([0,1,0,0,0,0,0,0,0,1,0],![(8,103),(8,103)]),
([0,1,0,0,0,0,0,1,0,0,0],![(7,98),(7,98)]),
([0,1,0,0,0,0,1,0,0,0,0],![(8,124),(8,124)]),
([0,1,0,0,0,0,1,0,0,1,0],![(4,48),(4,48)]),
([0,1,0,0,0,0,1,1,0,0,0],![(3,84),(3,84)]),
([0,1,0,0,1,0,0,0,0,0,0],![(7,119),(7,119)])
]
theorem rows3_4_checked : rows3_4.all (fun row => decide (∀ d : Degree, Matched d (some 3) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
