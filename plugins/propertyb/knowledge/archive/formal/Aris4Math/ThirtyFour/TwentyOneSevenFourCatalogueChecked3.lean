import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk0
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk1
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk2
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk3
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk4
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk5
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk6
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk7
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk8
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk9
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk10
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk11
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk12
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk13
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk14
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk15
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk16
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk17
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows3Chunk18
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_eq3 : rows3.map Prod.fst = catalogue 3 := by decide +kernel
theorem rows_chunks3 : rows3=chunk3_0++chunk3_1++chunk3_2++chunk3_3++chunk3_4++chunk3_5++chunk3_6++chunk3_7++chunk3_8++chunk3_9++chunk3_10++chunk3_11++chunk3_12++chunk3_13++chunk3_14++chunk3_15++chunk3_16++chunk3_17++chunk3_18 := by decide +kernel
theorem rows_checked3 : rows3.all (fun row => decide (Valid 3 row.1 → Matched 3 row.1 row.2.1 row.2.2))=true := by
  rw [rows_chunks3]
  simp only [List.all_append,checked_chunk3_0,checked_chunk3_1,checked_chunk3_2,checked_chunk3_3,checked_chunk3_4,checked_chunk3_5,checked_chunk3_6,checked_chunk3_7,checked_chunk3_8,checked_chunk3_9,checked_chunk3_10,checked_chunk3_11,checked_chunk3_12,checked_chunk3_13,checked_chunk3_14,checked_chunk3_15,checked_chunk3_16,checked_chunk3_17,checked_chunk3_18,Bool.and_self]
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
