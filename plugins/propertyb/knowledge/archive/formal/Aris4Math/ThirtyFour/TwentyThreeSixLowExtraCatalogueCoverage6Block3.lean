import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows6_3 : List (List ℕ × (Degree → Witness)) := [
([0,1,0,0,0,0,0,0,0,1,0],![(6,47),(6,47)]),
([0,1,0,0,0,0,0,1,0,0,0],![(6,88),(6,88)]),
([0,1,0,0,0,0,1,0,0,0,0],![(6,55),(6,55)]),
([0,1,0,0,0,0,1,1,0,0,0],![(2,9),(2,9)]),
([0,1,0,0,1,0,0,0,0,0,0],![(6,94),(6,94)]),
([0,1,0,0,1,0,0,0,0,1,0],![(2,11),(2,11)]),
([1,0,0,0,0,0,0,0,0,0,0],![(10,74),(10,74)]),
([1,0,0,0,0,0,0,0,0,1,0],![(6,70),(6,70)])
]
theorem rows6_3_checked : rows6_3.all (fun row => decide (∀ d : Degree, Matched d none row.1 (row.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
