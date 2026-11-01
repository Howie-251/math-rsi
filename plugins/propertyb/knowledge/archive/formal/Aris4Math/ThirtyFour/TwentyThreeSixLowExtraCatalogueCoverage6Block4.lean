import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows6_4 : List (List ℕ × (Degree → Witness)) := [
([1,0,0,0,0,0,0,0,1,0,0],![(6,89),(6,89)]),
([1,0,0,0,0,0,1,0,0,0,0],![(6,77),(6,77)]),
([1,0,0,0,0,0,1,0,1,0,0],![(2,17),(2,17)]),
([1,0,0,0,0,1,0,0,0,0,0],![(6,95),(6,95)]),
([1,0,0,0,0,1,0,0,0,1,0],![(2,19),(2,19)])
]
theorem rows6_4_checked : rows6_4.all (fun row => decide (∀ d : Degree, Matched d none row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
