import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk0
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk1
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk2
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk3
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk4
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk5
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk6
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk7
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk8
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk9
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk10
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk11
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk12
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk13
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk14
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk15
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk16
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk17
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows4Chunk18
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_eq4 : rows4.map Prod.fst = catalogue 4 := by decide +kernel
theorem rows_chunks4 : rows4=chunk4_0++chunk4_1++chunk4_2++chunk4_3++chunk4_4++chunk4_5++chunk4_6++chunk4_7++chunk4_8++chunk4_9++chunk4_10++chunk4_11++chunk4_12++chunk4_13++chunk4_14++chunk4_15++chunk4_16++chunk4_17++chunk4_18 := by decide +kernel
theorem rows_checked4 : rows4.all (fun row => decide (Valid 4 row.1 → Matched 4 row.1 row.2.1 row.2.2))=true := by
  rw [rows_chunks4]
  simp only [List.all_append,checked_chunk4_0,checked_chunk4_1,checked_chunk4_2,checked_chunk4_3,checked_chunk4_4,checked_chunk4_5,checked_chunk4_6,checked_chunk4_7,checked_chunk4_8,checked_chunk4_9,checked_chunk4_10,checked_chunk4_11,checked_chunk4_12,checked_chunk4_13,checked_chunk4_14,checked_chunk4_15,checked_chunk4_16,checked_chunk4_17,checked_chunk4_18,Bool.and_self]
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
