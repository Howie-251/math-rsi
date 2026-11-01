import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk4_18 : List Row := [([2,2,0,2,0,0,0,0,0,0],Sum.inl (0,0),0),([2,2,0,2,0,0,1,0,0,0],Sum.inl (10,11),21),([2,2,0,2,0,0,2,0,0,0],Sum.inl (10,12),0)]
theorem checked_chunk4_18 : chunk4_18.all (fun row => decide (Valid 4 row.1 → Matched 4 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
