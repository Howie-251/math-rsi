import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk1_8 : List Row := [([2,0,0,2,0,2,0,0],Sum.inl (0,0),0),([2,1,0,0,0,0,0,0],Sum.inl (0,0),0),([2,1,0,0,0,0,0,1],Sum.inl (3,15),3),([2,1,0,0,0,1,0,0],Sum.inl (0,0),0),([2,1,0,0,0,1,0,1],Sum.inl (4,0),2),([2,1,0,0,0,2,0,0],Sum.inl (0,0),0),([2,1,0,1,0,0,0,0],Sum.inl (0,0),0),([2,1,0,1,0,0,0,1],Sum.inl (4,0),4),([2,1,0,1,0,1,0,0],Sum.inl (2,4),0),([2,1,0,1,0,1,0,1],Sum.inl (4,1),0),([2,1,0,1,0,2,0,0],Sum.inl (2,5),0),([2,1,0,2,0,0,0,0],Sum.inl (0,0),0),([2,1,0,2,0,1,0,0],Sum.inl (2,5),1),([2,1,0,2,0,2,0,0],Sum.inl (2,6),0),([2,2,0,0,0,0,0,0],Sum.inl (0,0),0),([2,2,0,0,0,1,0,0],Sum.inl (0,0),0),([2,2,0,0,0,2,0,0],Sum.inl (0,0),0),([2,2,0,1,0,0,0,0],Sum.inl (0,0),0),([2,2,0,1,0,1,0,0],Sum.inl (2,5),3),([2,2,0,1,0,2,0,0],Sum.inl (2,6),2),([2,2,0,2,0,0,0,0],Sum.inl (0,0),0),([2,2,0,2,0,1,0,0],Sum.inl (2,6),4),([2,2,0,2,0,2,0,0],Sum.inl (2,7),0)]
theorem checked_chunk1_8 : chunk1_8.all (fun row => decide (Valid 1 row.1 → Matched 1 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
