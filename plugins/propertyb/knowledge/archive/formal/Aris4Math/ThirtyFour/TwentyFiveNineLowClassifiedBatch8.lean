import Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch8
open TwentyFiveConditionalRows TwentyFiveNineLowClassifiedData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows8.all (fun r => decide (FamilyCheck (fun _ => 6) TwentyFiveNineLowInventory.big r))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch8
