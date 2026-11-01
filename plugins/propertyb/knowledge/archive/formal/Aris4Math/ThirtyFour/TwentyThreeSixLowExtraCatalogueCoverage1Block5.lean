import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows1_5 : List (List ℕ × (Degree → Witness)) := [
([1,0,0,0,0,0,1,0,1,0,0],![(3,51),(3,51)]),
([1,0,0,0,0,0,1,1,0,0,0],![(4,65),(4,65)]),
([1,0,0,0,0,1,0,0,0,0,0],![(8,134),(8,134)]),
([1,0,0,0,0,1,0,0,0,1,0],![(3,53),(3,53)]),
([1,0,0,0,0,1,0,1,0,0,0],![(4,87),(4,87)]),
([1,0,0,0,1,0,0,0,0,0,0],![(9,130),(9,130)]),
([1,0,0,0,1,0,0,0,0,1,0],![(4,61),(4,61)]),
([1,0,0,0,1,0,0,0,1,0,0],![(4,83),(4,83)])
]
theorem rows1_5_checked : rows1_5.all (fun row => decide (∀ d : Degree, Matched d (some 1) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
