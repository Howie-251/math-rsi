import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows6_1 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,1,0,0,0,0,0],![(10,10),(10,10)]),
([0,0,0,0,0,1,0,0,0,1,0],![(6,1),(6,1)]),
([0,0,0,0,0,1,0,1,0,0,0],![(6,20),(6,20)]),
([0,0,0,0,1,0,0,0,0,0,0],![(10,18),(10,18)]),
([0,0,0,0,1,0,0,0,0,1,0],![(6,13),(6,13)]),
([0,0,0,0,1,0,0,0,1,0,0],![(6,21),(6,21)]),
([0,0,0,1,0,0,0,0,0,0,0],![(12,27),(12,27)]),
([0,0,0,1,0,0,0,0,0,0,1],![(0,0),(0,0)])
]
theorem rows6_1_checked : rows6_1.all (fun row => decide (∀ d : Degree, Matched d none row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
