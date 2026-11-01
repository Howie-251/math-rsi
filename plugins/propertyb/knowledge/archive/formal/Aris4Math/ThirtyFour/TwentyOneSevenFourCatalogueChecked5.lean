import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk0
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk1
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk2
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk3
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk4
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk5
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk6
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk7
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk8
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk9
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk10
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk11
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows5Chunk12
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_eq5 : rows5.map Prod.fst = catalogue 5 := by decide +kernel
theorem rows_chunks5 : rows5=chunk5_0++chunk5_1++chunk5_2++chunk5_3++chunk5_4++chunk5_5++chunk5_6++chunk5_7++chunk5_8++chunk5_9++chunk5_10++chunk5_11++chunk5_12 := by decide +kernel
theorem rows_checked5 : rows5.all (fun row => decide (Valid 5 row.1 → Matched 5 row.1 row.2.1 row.2.2))=true := by
  rw [rows_chunks5]
  simp only [List.all_append,checked_chunk5_0,checked_chunk5_1,checked_chunk5_2,checked_chunk5_3,checked_chunk5_4,checked_chunk5_5,checked_chunk5_6,checked_chunk5_7,checked_chunk5_8,checked_chunk5_9,checked_chunk5_10,checked_chunk5_11,checked_chunk5_12,Bool.and_self]
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
