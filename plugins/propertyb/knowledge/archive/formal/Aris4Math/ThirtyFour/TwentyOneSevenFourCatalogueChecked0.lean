import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk0
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk1
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk2
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk3
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk4
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk5
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk6
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk7
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk8
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk9
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk10
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk11
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk12
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk13
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk14
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk15
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk16
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows0Chunk17
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_eq0 : rows0.map Prod.fst = catalogue 0 := by decide +kernel
theorem rows_chunks0 : rows0=chunk0_0++chunk0_1++chunk0_2++chunk0_3++chunk0_4++chunk0_5++chunk0_6++chunk0_7++chunk0_8++chunk0_9++chunk0_10++chunk0_11++chunk0_12++chunk0_13++chunk0_14++chunk0_15++chunk0_16++chunk0_17 := by decide +kernel
theorem rows_checked0 : rows0.all (fun row => decide (Valid 0 row.1 → Matched 0 row.1 row.2.1 row.2.2))=true := by
  rw [rows_chunks0]
  simp only [List.all_append,checked_chunk0_0,checked_chunk0_1,checked_chunk0_2,checked_chunk0_3,checked_chunk0_4,checked_chunk0_5,checked_chunk0_6,checked_chunk0_7,checked_chunk0_8,checked_chunk0_9,checked_chunk0_10,checked_chunk0_11,checked_chunk0_12,checked_chunk0_13,checked_chunk0_14,checked_chunk0_15,checked_chunk0_16,checked_chunk0_17,Bool.and_self]
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
