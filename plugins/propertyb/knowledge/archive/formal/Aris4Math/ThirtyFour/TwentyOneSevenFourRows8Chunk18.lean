import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk8_18 : List Row := [([1,2,0,2,0,0,1,0,0,0,0],Sum.inl (27,7),4),([1,2,0,2,0,0,1,1,0,0,0],Sum.inl (28,14),0),([1,2,0,2,0,0,2,0,0,0,0],Sum.inl (27,8),0)]
theorem checked_chunk8_18 : chunk8_18.all (fun row => decide (Valid 8 row.1 → Matched 8 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
