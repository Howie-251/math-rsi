import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk0_17 : List Row := [([2,2,0,1,0,0,0,0,0,0],Sum.inl (0,0),0),([2,2,0,1,0,0,0,0,0,1],Sum.inl (0,12),1),([2,2,0,1,0,0,1,0,0,0],Sum.inl (0,2),16),([2,2,0,1,0,0,1,0,0,1],Sum.inl (0,13),0),([2,2,0,1,0,0,2,0,0,0],Sum.inl (0,3),12),([2,2,0,2,0,0,0,0,0,0],Sum.inl (0,0),0),([2,2,0,2,0,0,1,0,0,0],Sum.inl (0,3),18),([2,2,0,2,0,0,2,0,0,0],Sum.inl (0,4),0)]
theorem checked_chunk0_17 : chunk0_17.all (fun row => decide (Valid 0 row.1 → Matched 0 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
