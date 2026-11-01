import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows5_5 : List (List ℕ × (Degree → Witness)) := [
([0,1,0,0,1,0,0,0,0,1,0],![(3,119),(3,119)]),
([1,0,0,0,0,0,0,0,0,0,0],![(11,109),(11,109)]),
([1,0,0,0,0,0,0,0,0,1,0],![(8,71),(8,71)]),
([1,0,0,0,0,0,0,0,1,0,0],![(8,90),(8,90)]),
([1,0,0,0,0,0,0,0,1,1,0],![(4,109),(4,109)]),
([1,0,0,0,0,0,1,0,0,0,0],![(7,59),(7,59)]),
([1,0,0,0,0,0,1,0,1,0,0],![(3,126),(3,126)]),
([1,0,0,0,0,1,0,0,0,0,0],![(7,81),(7,81)])
]
theorem rows5_5_checked : rows5_5.all (fun row => decide (∀ d : Degree, Matched d (some 5) row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
