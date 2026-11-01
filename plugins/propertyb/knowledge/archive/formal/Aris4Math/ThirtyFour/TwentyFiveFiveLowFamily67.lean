import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric104
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric105
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family67
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],[{0,1},{1,2},{0,3},{1,3},{2,3},{1,4},{0,2,4},{3,4},{0,5},{2,5},{0,6},{2,6},{1,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case2516.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,5,6},⟨0,![5,6,0,1,2,3,4,7,8]⟩,none⟩⟩,
⟨Case2517.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,5,7},⟨0,![5,6,1,0,4,3,8,2,7]⟩,none⟩⟩,
⟨Case2518.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,5,8},⟨0,![5,6,0,1,2,4,8,7,3]⟩,none⟩⟩,
⟨Case2518.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,6,7},⟨0,![5,6,0,1,2,8,4,3,7]⟩,none⟩⟩,
⟨Case2517.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,6,8},⟨0,![5,6,1,0,4,8,3,7,2]⟩,none⟩⟩,
⟨Case2519.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,7,8},⟨0,![5,6,0,1,4,7,8,2,3]⟩,none⟩⟩,
⟨Case2520.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,5,6,7},⟨0,![5,6,1,0,8,3,4,2,7]⟩,none⟩⟩,
⟨Case2520.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,5,6,8},⟨0,![5,6,1,0,8,4,3,7,2]⟩,none⟩⟩,
⟨Case2521.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,5,7,8},⟨0,![5,6,1,0,8,4,7,2,3]⟩,none⟩⟩,
⟨Case2521.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,6,7,8},⟨0,![5,6,1,0,8,7,4,3,2]⟩,none⟩⟩,
⟨Case2522.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,4,5,6,7},⟨0,![5,6,0,7,1,4,3,2,8]⟩,none⟩⟩,
⟨Case2522.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,4,5,6,8},⟨0,![5,6,0,7,1,3,4,8,2]⟩,none⟩⟩,
⟨Case2523.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,4,5,7,8},⟨0,![5,6,0,7,3,4,8,2,1]⟩,none⟩⟩,
⟨Case2523.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,4,6,7,8},⟨0,![5,6,0,7,3,8,4,1,2]⟩,none⟩⟩,
⟨Case2524.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,5,6,7,8},⟨0,![5,6,0,7,8,3,4,1,2]⟩,none⟩⟩,
⟨Case2525.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,4,5,6,7},⟨0,![6,5,7,0,4,2,3,1,8]⟩,none⟩⟩,
⟨Case2525.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,4,5,6,8},⟨0,![6,5,7,0,4,3,2,8,1]⟩,none⟩⟩,
⟨Case2526.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,4,5,7,8},⟨0,![5,6,7,0,4,1,8,2,3]⟩,none⟩⟩,
⟨Case2526.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,4,6,7,8},⟨0,![5,6,7,0,4,8,1,3,2]⟩,none⟩⟩,
⟨Case2527.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,5,6,7,8},⟨0,![6,5,7,0,8,1,2,3,4]⟩,none⟩⟩,
⟨Case2528.big,⟨[{0,2,4},{1,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{4,5,6,7,8},⟨0,![6,5,8,7,0,1,2,4,3]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case2516.safe,Case2517.safe,Case2518.safe,Case2518.safe,Case2517.safe,Case2519.safe,Case2520.safe,Case2520.safe,Case2521.safe,Case2521.safe,Case2522.safe,Case2522.safe,Case2523.safe,Case2523.safe,Case2524.safe,Case2525.safe,Case2525.safe,Case2526.safe,Case2526.safe,Case2527.safe,Case2528.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family67
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
