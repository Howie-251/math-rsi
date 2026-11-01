import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows6_0 : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,0,0,0,0,0],![(16,0),(16,0)]),
([0,0,0,0,0,0,0,0,0,0,1],![(12,41),(12,41)]),
([0,0,0,0,0,0,0,0,0,1,0],![(10,2),(10,2)]),
([0,0,0,0,0,0,0,0,1,0,0],![(10,8),(10,8)]),
([0,0,0,0,0,0,0,1,0,0,0],![(10,16),(10,16)]),
([0,0,0,0,0,0,1,0,0,0,0],![(10,4),(10,4)]),
([0,0,0,0,0,0,1,0,1,0,0],![(6,0),(6,0)]),
([0,0,0,0,0,0,1,1,0,0,0],![(6,12),(6,12)])
]
theorem rows6_0_checked : rows6_0.all (fun row => decide (∀ d : Degree, Matched d none row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
