import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk1_0 : List Row := [([0,0,0,0,0,0,0,0],Sum.inl (0,0),0),([0,0,0,0,0,0,0,1],Sum.inl (0,0),0),([0,0,0,0,0,0,1,0],Sum.inl (0,0),0),([0,0,0,0,0,0,1,1],Sum.inl (4,2),0),([0,0,0,0,0,1,0,0],Sum.inl (0,0),0),([0,0,0,0,0,1,0,1],Sum.inl (0,0),0),([0,0,0,0,0,1,1,0],Sum.inl (0,0),0),([0,0,0,0,0,2,0,0],Sum.inl (0,0),0),([0,0,0,0,1,0,0,0],Sum.inl (0,0),0),([0,0,0,0,1,0,0,1],Sum.inl (4,2),1),([0,0,0,0,1,0,1,0],Sum.inl (0,0),0),([0,0,0,0,1,0,1,1],Sum.inl (4,8),0),([0,0,0,0,1,1,0,0],Sum.inl (0,0),0),([0,0,0,0,1,1,0,1],Sum.inl (4,3),1),([0,0,0,0,1,1,1,0],Sum.inl (0,0),0),([0,0,0,0,1,2,0,0],Sum.inl (0,0),0),([0,0,0,1,0,0,0,0],Sum.inl (0,0),0),([0,0,0,1,0,0,0,1],Sum.inl (0,0),0),([0,0,0,1,0,0,1,0],Sum.inl (0,0),0),([0,0,0,1,0,0,1,1],Sum.inl (4,3),0),([0,0,0,1,0,1,0,0],Sum.inl (0,0),0),([0,0,0,1,0,1,0,1],Sum.inl (0,0),0),([0,0,0,1,0,1,1,0],Sum.inl (0,0),0),([0,0,0,1,0,2,0,0],Sum.inl (0,0),0),([0,0,0,1,1,0,0,0],Sum.inl (0,0),0),([0,0,0,1,1,0,1,0],Sum.inl (0,0),0),([0,0,0,1,1,1,0,0],Sum.inl (0,0),0),([0,0,0,1,1,1,1,0],Sum.inl (0,0),0),([0,0,0,1,1,2,0,0],Sum.inl (0,0),0),([0,0,0,2,0,0,0,0],Sum.inl (0,0),0),([0,0,0,2,0,0,1,0],Sum.inl (0,0),0),([0,0,0,2,0,1,0,0],Sum.inl (0,0),0)]
theorem checked_chunk1_0 : chunk1_0.all (fun row => decide (Valid 1 row.1 → Matched 1 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
