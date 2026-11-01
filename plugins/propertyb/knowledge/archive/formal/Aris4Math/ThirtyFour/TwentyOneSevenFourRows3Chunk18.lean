import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk3_18 : List Row := [([2,1,0,2,0,0,2,0,0,0],Sum.inl (5,9),0),([2,2,0,0,0,0,0,0,0,0],Sum.inl (0,0),0),([2,2,0,0,0,0,0,0,0,1],Sum.inl (6,4),0),([2,2,0,0,0,0,0,0,0,2],Sum.inl (6,10),0),([2,2,0,0,0,0,1,0,0,0],Sum.inl (0,0),0),([2,2,0,0,0,0,1,0,0,1],Sum.inl (6,5),0),([2,2,0,0,0,0,2,0,0,0],Sum.inl (0,0),0),([2,2,0,1,0,0,0,0,0,0],Sum.inl (0,0),0),([2,2,0,1,0,0,0,0,0,1],Sum.inl (6,5),1),([2,2,0,1,0,0,1,0,0,0],Sum.inl (5,8),3),([2,2,0,1,0,0,1,0,0,1],Sum.inl (6,6),0),([2,2,0,1,0,0,2,0,0,0],Sum.inl (5,9),2),([2,2,0,2,0,0,0,0,0,0],Sum.inl (0,0),0),([2,2,0,2,0,0,1,0,0,0],Sum.inl (5,9),4),([2,2,0,2,0,0,2,0,0,0],Sum.inl (5,10),0)]
theorem checked_chunk3_18 : chunk3_18.all (fun row => decide (Valid 3 row.1 → Matched 3 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
