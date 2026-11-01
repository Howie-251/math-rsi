import Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch3
open TwentyFiveConditionalRows TwentyFiveNineLowClassifiedData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows3.all (fun r => decide (FamilyCheck (fun _ => 6) TwentyFiveNineLowInventory.big r))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch3
