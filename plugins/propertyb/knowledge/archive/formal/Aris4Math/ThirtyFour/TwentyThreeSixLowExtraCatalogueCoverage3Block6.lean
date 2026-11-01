import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows3_6 : List (List ℕ × (Degree → Witness)) := [
([1,0,0,0,0,1,0,0,0,1,0],![(3,81),(3,81)])
]
theorem rows3_6_checked : rows3_6.all (fun row => decide (∀ d : Degree, Matched d (some 3) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
