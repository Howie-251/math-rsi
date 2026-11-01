import Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem catalogue_eq : catalogue=chunk0++chunk1++chunk2++chunk3++chunk4++chunk5++chunk6++chunk7++chunk8++chunk9 := by decide +kernel
theorem certificate0 : ∀values∈chunk0,Valid values→Matched values := by decide +kernel
theorem certificate1 : ∀values∈chunk1,Valid values→Matched values := by decide +kernel
theorem certificate2 : ∀values∈chunk2,Valid values→Matched values := by decide +kernel
theorem certificate3 : ∀values∈chunk3,Valid values→Matched values := by decide +kernel
theorem certificate4 : ∀values∈chunk4,Valid values→Matched values := by decide +kernel
theorem certificate5 : ∀values∈chunk5,Valid values→Matched values := by decide +kernel
theorem certificate6 : ∀values∈chunk6,Valid values→Matched values := by decide +kernel
theorem certificate7 : ∀values∈chunk7,Valid values→Matched values := by decide +kernel
theorem certificate8 : ∀values∈chunk8,Valid values→Matched values := by decide +kernel
theorem certificate9 : ∀values∈chunk9,Valid values→Matched values := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue
