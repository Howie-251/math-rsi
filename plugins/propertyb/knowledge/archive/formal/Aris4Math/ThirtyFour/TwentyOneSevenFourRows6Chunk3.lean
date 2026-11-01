import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def chunk6_3 : List Row := [([1,0,1,0,0,0,0],Sum.inl (0,0),0),([1,0,1,0,0,0,1],Sum.inl (0,0),0),([1,0,1,0,0,1,0],Sum.inl (24,9),23),([1,0,1,0,1,0,0],Sum.inl (0,0),0),([1,0,1,0,1,0,1],Sum.inl (0,0),0),([1,0,1,0,1,1,0],Sum.inl (25,0),2),([1,0,1,0,2,0,0],Sum.inl (0,0),0),([1,0,1,1,0,0,0],Sum.inl (0,0),0),([1,0,1,1,0,1,0],Sum.inl (25,7),23),([1,0,1,1,1,0,0],Sum.inl (23,14),0),([1,0,1,1,1,1,0],Sum.inl (25,9),2),([1,0,1,1,2,0,0],Sum.inl (23,15),0),([1,0,2,0,0,0,0],Sum.inl (0,0),0),([1,0,2,0,0,1,0],Sum.inl (24,13),23),([1,0,2,0,1,0,0],Sum.inl (0,0),0),([1,0,2,0,1,1,0],Sum.inl (25,2),2),([1,0,2,0,2,0,0],Sum.inl (0,0),0),([1,1,0,0,0,0,0],Sum.inl (0,0),0),([1,1,0,0,0,0,1],Sum.inl (24,9),21),([1,1,0,0,0,1,0],Sum.inl (0,0),0),([1,1,0,0,1,0,0],Sum.inl (0,0),0),([1,1,0,0,1,0,1],Sum.inl (25,0),0),([1,1,0,0,1,1,0],Sum.inl (0,0),0),([1,1,0,0,2,0,0],Sum.inl (0,0),0),([1,1,0,1,0,0,0],Sum.inl (0,0),0),([1,1,0,1,0,0,1],Sum.inl (25,7),21),([1,1,0,1,1,0,0],Sum.inl (23,14),2),([1,1,0,1,1,0,1],Sum.inl (25,9),0),([1,1,0,1,2,0,0],Sum.inl (23,15),2),([1,1,1,0,0,0,0],Sum.inl (0,0),0),([1,1,1,0,0,0,1],Sum.inl (24,11),21),([1,1,1,0,0,1,0],Sum.inl (24,11),23)]
theorem checked_chunk6_3 : chunk6_3.all (fun row => decide (Valid 6 row.1 → Matched 6 row.1 row.2.1 row.2.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
