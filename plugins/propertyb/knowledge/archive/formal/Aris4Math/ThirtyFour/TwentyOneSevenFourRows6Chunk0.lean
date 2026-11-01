import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk6_0 : List Row := [([0,0,0,0,0,0,0],Sum.inl (0,0),0),([0,0,0,0,0,0,1],Sum.inl (0,0),0),([0,0,0,0,0,1,0],Sum.inl (0,0),0),([0,0,0,0,0,1,1],Sum.inl (25,10),0),([0,0,0,0,1,0,0],Sum.inl (0,0),0),([0,0,0,0,1,0,1],Sum.inl (0,0),0),([0,0,0,0,1,1,0],Sum.inl (0,0),0),([0,0,0,0,2,0,0],Sum.inl (0,0),0),([0,0,0,1,0,0,0],Sum.inl (0,0),0),([0,0,0,1,0,0,1],Sum.inl (25,4),0),([0,0,0,1,0,1,0],Sum.inl (25,4),2),([0,0,0,1,0,1,1],Sum.inl (25,13),0),([0,0,0,1,1,0,0],Sum.inl (0,0),0),([0,0,0,1,1,0,1],Sum.inl (25,5),0),([0,0,0,1,1,1,0],Sum.inl (25,5),2),([0,0,0,1,2,0,0],Sum.inl (0,0),0),([0,0,0,2,0,0,0],Sum.inl (0,0),0),([0,0,0,2,1,0,0],Sum.inl (0,0),0),([0,0,0,2,2,0,0],Sum.inl (0,0),0),([0,0,1,0,0,0,0],Sum.inl (0,0),0),([0,0,1,0,0,0,1],Sum.inl (0,0),0),([0,0,1,0,0,1,0],Sum.inl (24,8),2),([0,0,1,0,0,1,1],Sum.inl (25,11),0),([0,0,1,0,1,0,0],Sum.inl (0,0),0),([0,0,1,0,1,0,1],Sum.inl (0,0),0),([0,0,1,0,1,1,0],Sum.inl (24,9),2),([0,0,1,0,2,0,0],Sum.inl (0,0),0),([0,0,1,1,0,0,0],Sum.inl (0,0),0),([0,0,1,1,0,1,0],Sum.inl (25,6),2),([0,0,1,1,1,0,0],Sum.inl (0,0),0),([0,0,1,1,1,1,0],Sum.inl (25,7),2),([0,0,1,1,2,0,0],Sum.inl (0,0),0)]
theorem checked_chunk6_0 : chunk6_0.all (fun row => decide (Valid 6 row.1 → Matched 6 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
