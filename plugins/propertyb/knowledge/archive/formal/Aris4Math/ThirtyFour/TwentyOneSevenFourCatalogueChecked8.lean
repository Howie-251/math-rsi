import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk0
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk1
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk2
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk3
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk4
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk5
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk6
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk7
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk8
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk9
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk10
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk11
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk12
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk13
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk14
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk15
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk16
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk17
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows8Chunk18
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_eq8 : rows8.map Prod.fst = catalogue 8 := by decide +kernel
theorem rows_chunks8 : rows8=chunk8_0++chunk8_1++chunk8_2++chunk8_3++chunk8_4++chunk8_5++chunk8_6++chunk8_7++chunk8_8++chunk8_9++chunk8_10++chunk8_11++chunk8_12++chunk8_13++chunk8_14++chunk8_15++chunk8_16++chunk8_17++chunk8_18 := by decide +kernel
theorem rows_checked8 : rows8.all (fun row => decide (Valid 8 row.1 → Matched 8 row.1 row.2.1 row.2.2))=true := by
  rw [rows_chunks8]
  simp only [List.all_append,checked_chunk8_0,checked_chunk8_1,checked_chunk8_2,checked_chunk8_3,checked_chunk8_4,checked_chunk8_5,checked_chunk8_6,checked_chunk8_7,checked_chunk8_8,checked_chunk8_9,checked_chunk8_10,checked_chunk8_11,checked_chunk8_12,checked_chunk8_13,checked_chunk8_14,checked_chunk8_15,checked_chunk8_16,checked_chunk8_17,checked_chunk8_18,Bool.and_self]
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
