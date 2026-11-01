import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk0
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk1
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk2
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk3
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk4
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk5
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk6
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk7
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk8
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk9
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk10
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows7Chunk11
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_eq7 : rows7.map Prod.fst = catalogue 7 := by decide +kernel
theorem rows_chunks7 : rows7=chunk7_0++chunk7_1++chunk7_2++chunk7_3++chunk7_4++chunk7_5++chunk7_6++chunk7_7++chunk7_8++chunk7_9++chunk7_10++chunk7_11 := by decide +kernel
theorem rows_checked7 : rows7.all (fun row => decide (Valid 7 row.1 → Matched 7 row.1 row.2.1 row.2.2))=true := by
  rw [rows_chunks7]
  simp only [List.all_append,checked_chunk7_0,checked_chunk7_1,checked_chunk7_2,checked_chunk7_3,checked_chunk7_4,checked_chunk7_5,checked_chunk7_6,checked_chunk7_7,checked_chunk7_8,checked_chunk7_9,checked_chunk7_10,checked_chunk7_11,Bool.and_self]
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
