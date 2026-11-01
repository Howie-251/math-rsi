import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk6_4 : List Row := [([1,1,1,0,1,0,0],Sum.inl (23,3),0),([1,1,1,0,1,0,1],Sum.inl (25,1),0),([1,1,1,0,1,1,0],Sum.inl (25,1),2),([1,1,1,0,2,0,0],Sum.inl (23,4),0),([1,1,1,1,0,0,0],Sum.inl (0,0),0),([1,1,1,1,1,0,0],Sum.inl (24,0),0),([1,1,1,1,2,0,0],Sum.inl (24,1),0),([1,1,2,0,0,0,0],Sum.inl (0,0),0),([1,1,2,0,0,1,0],Sum.inl (24,15),23),([1,1,2,0,1,0,0],Sum.inl (23,5),0),([1,1,2,0,1,1,0],Sum.inl (25,3),2),([1,1,2,0,2,0,0],Sum.inl (23,6),0),([1,2,0,0,0,0,0],Sum.inl (0,0),0),([1,2,0,0,0,0,1],Sum.inl (24,13),21),([1,2,0,0,1,0,0],Sum.inl (0,0),0),([1,2,0,0,1,0,1],Sum.inl (25,2),0),([1,2,0,0,2,0,0],Sum.inl (0,0),0),([1,2,1,0,0,0,0],Sum.inl (0,0),0),([1,2,1,0,0,0,1],Sum.inl (24,15),21),([1,2,1,0,1,0,0],Sum.inl (23,5),2),([1,2,1,0,1,0,1],Sum.inl (25,3),0),([1,2,1,0,2,0,0],Sum.inl (23,6),2),([1,2,2,0,0,0,0],Sum.inl (0,0),0),([1,2,2,0,1,0,0],Sum.inl (23,7),0),([1,2,2,0,2,0,0],Sum.inl (23,8),0),([2,0,0,0,0,0,0],Sum.inl (0,0),0),([2,0,0,0,1,0,0],Sum.inl (0,0),0),([2,0,0,0,2,0,0],Sum.inl (0,0),0),([2,0,0,1,0,0,0],Sum.inl (0,0),0),([2,0,0,1,1,0,0],Sum.inl (23,13),21),([2,0,0,1,2,0,0],Sum.inl (24,2),0),([2,0,0,2,0,0,0],Sum.inl (0,0),0)]
theorem checked_chunk6_4 : chunk6_4.all (fun row => decide (Valid 6 row.1 → Matched 6 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
