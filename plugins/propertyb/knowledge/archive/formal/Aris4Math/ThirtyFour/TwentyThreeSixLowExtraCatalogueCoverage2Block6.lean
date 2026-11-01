import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows2_6 : List (List ℕ × (Degree → Witness)) := [
([1,0,0,0,0,1,0,0,1,0,0],![(4,90),(4,90)])
]
theorem rows2_6_checked : rows2_6.all (fun row => decide (∀ d : Degree, Matched d (some 2) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
