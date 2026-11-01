import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk6_5 : List Row := [([2,0,0,2,1,0,0],Sum.inl (24,6),21),([2,0,0,2,2,0,0],Sum.inl (24,7),0),([2,0,1,0,0,0,0],Sum.inl (0,0),0),([2,0,1,0,1,0,0],Sum.inl (0,0),0),([2,0,1,0,2,0,0],Sum.inl (0,0),0),([2,0,1,1,0,0,0],Sum.inl (0,0),0),([2,0,1,1,1,0,0],Sum.inl (23,15),21),([2,0,1,1,2,0,0],Sum.inl (24,3),0),([2,0,2,0,0,0,0],Sum.inl (0,0),0),([2,0,2,0,1,0,0],Sum.inl (0,0),0),([2,0,2,0,2,0,0],Sum.inl (0,0),0),([2,1,0,0,0,0,0],Sum.inl (0,0),0),([2,1,0,0,1,0,0],Sum.inl (0,0),0),([2,1,0,0,2,0,0],Sum.inl (0,0),0),([2,1,0,1,0,0,0],Sum.inl (0,0),0),([2,1,0,1,1,0,0],Sum.inl (23,15),23),([2,1,0,1,2,0,0],Sum.inl (24,3),2),([2,1,1,0,0,0,0],Sum.inl (0,0),0),([2,1,1,0,1,0,0],Sum.inl (23,4),21),([2,1,1,0,2,0,0],Sum.inl (23,9),0),([2,1,1,1,0,0,0],Sum.inl (0,0),0),([2,1,1,1,1,0,0],Sum.inl (24,1),21),([2,1,1,1,2,0,0],Sum.inl (24,4),0),([2,1,2,0,0,0,0],Sum.inl (0,0),0),([2,1,2,0,1,0,0],Sum.inl (23,6),21),([2,1,2,0,2,0,0],Sum.inl (23,10),0),([2,2,0,0,0,0,0],Sum.inl (0,0),0),([2,2,0,0,1,0,0],Sum.inl (0,0),0),([2,2,0,0,2,0,0],Sum.inl (0,0),0),([2,2,1,0,0,0,0],Sum.inl (0,0),0),([2,2,1,0,1,0,0],Sum.inl (23,6),23),([2,2,1,0,2,0,0],Sum.inl (23,10),2)]
theorem checked_chunk6_5 : chunk6_5.all (fun row => decide (Valid 6 row.1 → Matched 6 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
