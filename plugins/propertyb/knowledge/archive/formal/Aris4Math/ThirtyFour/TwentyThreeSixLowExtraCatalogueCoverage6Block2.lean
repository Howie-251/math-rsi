import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows6_2 : List (List ℕ × (Degree → Witness)) := [
([0,0,1,0,0,0,0,0,0,0,0],![(10,50),(10,50)]),
([0,0,1,0,0,0,0,0,1,0,0],![(6,46),(6,46)]),
([0,0,1,0,0,0,0,1,0,0,0],![(6,69),(6,69)]),
([0,0,1,0,0,1,0,0,0,0,0],![(6,54),(6,54)]),
([0,0,1,0,0,1,0,1,0,0,0],![(2,3),(2,3)]),
([0,0,1,0,1,0,0,0,0,0,0],![(6,76),(6,76)]),
([0,0,1,0,1,0,0,0,1,0,0],![(2,5),(2,5)]),
([0,1,0,0,0,0,0,0,0,0,0],![(10,52),(10,52)])
]
theorem rows6_2_checked : rows6_2.all (fun row => decide (∀ d : Degree, Matched d none row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
