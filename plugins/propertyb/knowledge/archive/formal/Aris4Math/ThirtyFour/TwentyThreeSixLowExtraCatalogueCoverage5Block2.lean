import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows5_2 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,1,0,0,0,1,0],![(8,37),(8,37)]),
([0,0,0,0,0,1,0,1,0,0,0],![(8,87),(8,87)]),
([0,0,0,0,0,1,0,1,0,1,0],![(4,6),(4,6)]),
([0,0,0,0,1,0,0,0,0,0,0],![(11,14),(11,14)]),
([0,0,0,0,1,0,0,0,0,1,0],![(8,64),(8,64)]),
([0,0,0,0,1,0,0,0,1,0,0],![(8,86),(8,86)]),
([0,0,0,0,1,0,0,0,1,1,0],![(4,14),(4,14)]),
([0,0,0,1,0,0,0,0,0,0,0],![(15,24),(15,24)])
]
theorem rows5_2_checked : rows5_2.all (fun row => decide (∀ d : Degree, Matched d (some 5) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
