import Aris4Math.ThirtyFour.TwentyOneSevenFourRows1Chunk0
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows1Chunk1
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows1Chunk2
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows1Chunk3
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows1Chunk4
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows1Chunk5
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows1Chunk6
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows1Chunk7
import Aris4Math.ThirtyFour.TwentyOneSevenFourRows1Chunk8
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenFourActualCore (catalogue Valid)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem rows_eq1 : rows1.map Prod.fst = catalogue 1 := by decide +kernel
theorem rows_chunks1 : rows1=chunk1_0++chunk1_1++chunk1_2++chunk1_3++chunk1_4++chunk1_5++chunk1_6++chunk1_7++chunk1_8 := by decide +kernel
theorem rows_checked1 : rows1.all (fun row => decide (Valid 1 row.1 → Matched 1 row.1 row.2.1 row.2.2))=true := by
  rw [rows_chunks1]
  simp only [List.all_append,checked_chunk1_0,checked_chunk1_1,checked_chunk1_2,checked_chunk1_3,checked_chunk1_4,checked_chunk1_5,checked_chunk1_6,checked_chunk1_7,checked_chunk1_8,Bool.and_self]
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
