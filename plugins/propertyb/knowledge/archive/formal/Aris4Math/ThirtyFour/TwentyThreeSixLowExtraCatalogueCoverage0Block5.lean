import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows0_5 : List (List ℕ × (Degree → Witness)) := [
([1,0,0,0,0,0,1,0,1,0,0],![(3,17),(3,17)]),
([1,0,0,0,0,1,0,0,0,0,0],![(8,95),(8,95)]),
([1,0,0,0,0,1,0,0,0,1,0],![(3,19),(3,19)]),
([1,0,1,0,0,0,0,0,0,0,0],![(9,71),(9,71)]),
([1,0,1,0,0,0,0,0,1,0,0],![(4,104),(4,104)]),
([1,0,1,0,0,1,0,0,0,0,0],![(4,125),(4,125)]),
([1,1,0,0,0,0,0,0,0,0,0],![(9,90),(9,90)]),
([1,1,0,0,0,0,0,0,0,1,0],![(4,100),(4,100)])
]
theorem rows0_5_checked : rows0_5.all (fun row => decide (∀ d : Degree, Matched d (some 0) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
