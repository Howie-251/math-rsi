import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk7_11 : List Row := [([1,1,0,1,0,1,1,1,0,0],Sum.inl (26,12),0),([1,1,0,1,1,0,0,0,0,0],Sum.inl (0,0),0),([1,1,0,1,1,0,0,0,1,0],Sum.inl (26,11),19),([1,1,0,1,1,0,1,0,0,0],Sum.inl (26,1),10),([1,1,0,1,1,0,1,0,1,0],Sum.inl (26,12),1),([1,1,1,0,0,0,0,0,0,0],Sum.inl (0,0),0),([1,1,1,0,0,0,0,0,0,1],Sum.inl (26,10),12),([1,1,1,0,0,0,0,0,0,2],Sum.inl (27,2),3),([1,1,1,0,0,0,1,0,0,0],Sum.inl (0,0),0),([1,1,1,0,0,0,1,0,0,1],Sum.inl (26,11),12),([1,1,1,1,0,0,0,0,0,0],Sum.inl (0,0),0),([1,1,1,1,0,0,0,0,0,1],Sum.inl (26,11),18),([1,1,1,1,0,0,1,0,0,0],Sum.inl (26,1),16),([1,1,1,1,0,0,1,0,0,1],Sum.inl (26,12),3)]
theorem checked_chunk7_11 : chunk7_11.all (fun row => decide (Valid 7 row.1 → Matched 7 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
