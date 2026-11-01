import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows1_1 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,1,0,0,0,0,0],![(11,87),(11,87)]),
([0,0,0,0,0,1,0,0,0,1,0],![(7,19),(7,19)]),
([0,0,0,0,0,1,0,1,0,0,0],![(8,20),(8,20)]),
([0,0,0,0,1,0,0,0,0,0,0],![(14,15),(14,15)]),
([0,0,0,0,1,0,0,0,0,1,0],![(8,13),(8,13)]),
([0,0,0,0,1,0,0,0,1,0,0],![(8,21),(8,21)]),
([0,0,0,0,1,0,0,1,0,0,0],![(9,14),(9,14)]),
([0,0,0,1,0,0,0,0,0,0,0],![(13,33),(13,33)])
]
theorem rows1_1_checked : rows1_1.all (fun row => decide (∀ d : Degree, Matched d (some 1) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
