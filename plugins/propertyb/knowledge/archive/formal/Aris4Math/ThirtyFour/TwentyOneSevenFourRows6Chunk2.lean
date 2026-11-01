import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk6_2 : List Row := [([0,1,2,0,1,1,0],Sum.inl (24,15),2),([0,1,2,0,2,0,0],Sum.inl (0,0),0),([0,2,0,0,0,0,0],Sum.inl (0,0),0),([0,2,0,0,0,0,1],Sum.inl (24,12),0),([0,2,0,0,1,0,0],Sum.inl (0,0),0),([0,2,0,0,1,0,1],Sum.inl (24,13),0),([0,2,0,0,2,0,0],Sum.inl (0,0),0),([0,2,1,0,0,0,0],Sum.inl (0,0),0),([0,2,1,0,0,0,1],Sum.inl (24,14),0),([0,2,1,0,1,0,0],Sum.inl (0,0),0),([0,2,1,0,1,0,1],Sum.inl (24,15),0),([0,2,1,0,2,0,0],Sum.inl (0,0),0),([0,2,2,0,0,0,0],Sum.inl (0,0),0),([0,2,2,0,1,0,0],Sum.inl (0,0),0),([0,2,2,0,2,0,0],Sum.inl (0,0),0),([1,0,0,0,0,0,0],Sum.inl (0,0),0),([1,0,0,0,0,0,1],Sum.inl (0,0),0),([1,0,0,0,0,1,0],Sum.inl (0,0),0),([1,0,0,0,1,0,0],Sum.inl (0,0),0),([1,0,0,0,1,0,1],Sum.inl (0,0),0),([1,0,0,0,1,1,0],Sum.inl (0,0),0),([1,0,0,0,2,0,0],Sum.inl (0,0),0),([1,0,0,1,0,0,0],Sum.inl (0,0),0),([1,0,0,1,0,0,1],Sum.inl (25,5),21),([1,0,0,1,0,1,0],Sum.inl (25,5),23),([1,0,0,1,1,0,0],Sum.inl (23,12),0),([1,0,0,1,1,0,1],Sum.inl (25,8),0),([1,0,0,1,1,1,0],Sum.inl (25,8),2),([1,0,0,1,2,0,0],Sum.inl (23,13),0),([1,0,0,2,0,0,0],Sum.inl (0,0),0),([1,0,0,2,1,0,0],Sum.inl (24,5),0),([1,0,0,2,2,0,0],Sum.inl (24,6),0)]
theorem checked_chunk6_2 : chunk6_2.all (fun row => decide (Valid 6 row.1 → Matched 6 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
