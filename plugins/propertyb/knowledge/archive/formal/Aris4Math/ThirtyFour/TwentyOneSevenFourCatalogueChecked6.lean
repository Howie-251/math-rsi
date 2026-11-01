import Aris4Math.ThirtyFour.TwentyOneSevenFourRows6Chunk0
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows6Chunk1
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows6Chunk2
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows6Chunk3
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows6Chunk4
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows6Chunk5
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows6Chunk6
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_eq6 : rows6.map Prod.fst = catalogue 6 := by decide +kernel
theorem rows_chunks6 : rows6=chunk6_0++chunk6_1++chunk6_2++chunk6_3++chunk6_4++chunk6_5++chunk6_6 := by decide +kernel
theorem rows_checked6 : rows6.all (fun row => decide (Valid 6 row.1 → Matched 6 row.1 row.2.1 row.2.2))=true := by
  rw [rows_chunks6]
  simp only [List.all_append,checked_chunk6_0,checked_chunk6_1,checked_chunk6_2,checked_chunk6_3,checked_chunk6_4,checked_chunk6_5,checked_chunk6_6,Bool.and_self]
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
