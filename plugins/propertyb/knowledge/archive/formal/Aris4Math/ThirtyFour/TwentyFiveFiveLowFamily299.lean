import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric461
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric462
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family299
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],[{0,1},{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{3,6},{4,5,6},{0,2,7},{1,3,7},{4,7},{5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case11083.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,4,5,6},⟨0,![5,6,3,4,0,1,2,8,7]⟩,none⟩⟩,
⟨Case11084.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,4,5,7},⟨0,![5,6,2,3,0,1,7,4,8]⟩,none⟩⟩,
⟨Case11085.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,4,5,8},⟨0,![5,6,2,3,0,1,7,8,4]⟩,none⟩⟩,
⟨Case11086.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,4,6,7},⟨0,![5,6,2,3,0,7,1,4,8]⟩,none⟩⟩,
⟨Case11087.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,4,6,8},⟨0,![5,6,1,3,0,7,2,8,4]⟩,none⟩⟩,
⟨Case11088.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,4,7,8},⟨0,![5,6,0,2,1,7,8,4,3]⟩,none⟩⟩,
⟨Case11086.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,5,6,7},⟨0,![6,5,3,2,7,0,1,4,8]⟩,none⟩⟩,
⟨Case11087.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,5,6,8},⟨0,![6,5,3,1,7,0,2,8,4]⟩,none⟩⟩,
⟨Case11088.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,5,7,8},⟨0,![6,5,2,0,7,1,8,4,3]⟩,none⟩⟩,
⟨Case11089.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,3,6,7,8},⟨0,![5,6,1,2,7,8,0,3,4]⟩,none⟩⟩,
⟨Case11090.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,4,5,6,7},⟨0,![5,6,3,7,0,2,1,4,8]⟩,none⟩⟩,
⟨Case11091.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,4,5,6,8},⟨0,![5,6,3,7,0,1,2,8,4]⟩,none⟩⟩,
⟨Case11092.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,4,5,7,8},⟨0,![5,6,1,8,0,2,7,4,3]⟩,none⟩⟩,
⟨Case11093.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,4,6,7,8},⟨0,![5,6,1,8,0,7,2,4,3]⟩,none⟩⟩,
⟨Case11094.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{2,5,6,7,8},⟨0,![5,6,2,8,7,1,0,3,4]⟩,none⟩⟩,
⟨Case11090.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{3,4,5,6,7},⟨0,![6,5,7,3,2,0,1,4,8]⟩,none⟩⟩,
⟨Case11091.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{3,4,5,6,8},⟨0,![6,5,7,3,1,0,2,8,4]⟩,none⟩⟩,
⟨Case11092.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{3,4,5,7,8},⟨0,![6,5,8,1,2,0,7,4,3]⟩,none⟩⟩,
⟨Case11094.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{3,4,6,7,8},⟨0,![6,5,8,2,1,7,0,3,4]⟩,none⟩⟩,
⟨Case11093.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{3,5,6,7,8},⟨0,![6,5,8,1,7,0,2,4,3]⟩,none⟩⟩,
⟨Case11095.big,⟨[{4,5,6},{0,2,7},{1,3,7},{2,4,8},{3,5,8},{6,7,8}],{4,5,6,7,8},⟨0,![5,6,7,8,1,2,0,4,3]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case11083.safe,Case11084.safe,Case11085.safe,Case11086.safe,Case11087.safe,Case11088.safe,Case11086.safe,Case11087.safe,Case11088.safe,Case11089.safe,Case11090.safe,Case11091.safe,Case11092.safe,Case11093.safe,Case11094.safe,Case11090.safe,Case11091.safe,Case11092.safe,Case11094.safe,Case11093.safe,Case11095.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family299
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
