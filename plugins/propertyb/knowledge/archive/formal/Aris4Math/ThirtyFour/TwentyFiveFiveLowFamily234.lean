import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric367
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family234
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}],[{0,1},{0,2},{1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{2,6},{0,3,6},{4,6},{0,7},{3,7},{4,5,7},{1,6,7},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}],{3,4,5,6,7,8},[{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case8826.big,⟨[{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}],{3,4,5,6,7},⟨0,![5,6,7,2,0,1,4,3,8]⟩,none⟩⟩,
⟨Case8827.big,⟨[{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}],{3,4,5,6,8},⟨0,![5,7,6,1,0,2,4,8,3]⟩,none⟩⟩,
⟨Case8828.big,⟨[{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}],{3,4,5,7,8},⟨0,![5,7,6,2,0,1,8,4,3]⟩,none⟩⟩,
⟨Case8829.big,⟨[{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}],{3,4,6,7,8},⟨0,![5,7,6,0,1,8,3,4,2]⟩,none⟩⟩,
⟨Case8830.big,⟨[{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}],{3,5,6,7,8},⟨0,![5,6,7,1,8,0,2,4,3]⟩,none⟩⟩,
⟨Case8831.big,⟨[{0,3,6},{4,5,7},{1,6,7},{3,4,8},{5,6,8},{2,7,8}],{4,5,6,7,8},⟨0,![7,6,5,8,1,0,4,2,3]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case8826.safe,Case8827.safe,Case8828.safe,Case8829.safe,Case8830.safe,Case8831.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family234
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
