import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows3_5 : List (List ℕ × (Degree → Witness)) := [
([0,1,0,0,1,0,0,0,0,1,0],![(3,80),(3,80)]),
([1,0,0,0,0,0,0,0,0,0,0],![(11,71),(11,71)]),
([1,0,0,0,0,0,0,0,0,1,0],![(8,109),(8,109)]),
([1,0,0,0,0,0,0,0,1,0,0],![(7,101),(7,101)]),
([1,0,0,0,0,0,1,0,0,0,0],![(8,130),(8,130)]),
([1,0,0,0,0,0,1,0,0,1,0],![(4,71),(4,71)]),
([1,0,0,0,0,0,1,0,1,0,0],![(3,85),(3,85)]),
([1,0,0,0,0,1,0,0,0,0,0],![(7,122),(7,122)])
]
theorem rows3_5_checked : rows3_5.all (fun row => decide (∀ d : Degree, Matched d (some 3) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
