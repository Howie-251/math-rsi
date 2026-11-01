import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric428
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric429
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family270
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],[{0,1},{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{4,5},{2,3,4,6},{5,6},{1,7},{3,7},{2,5,7},{0,6,7},{0,8},{2,8},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case10290.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,5,6},⟨0,![5,6,0,1,2,3,4,7,8]⟩,none⟩⟩,
⟨Case10291.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,5,7},⟨0,![5,6,0,1,2,3,7,4,8]⟩,none⟩⟩,
⟨Case10291.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,5,8},⟨0,![6,5,1,0,2,3,7,8,4]⟩,none⟩⟩,
⟨Case10292.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,6,7},⟨0,![5,6,0,2,1,7,3,4,8]⟩,none⟩⟩,
⟨Case10292.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,6,8},⟨0,![6,5,2,0,1,7,3,8,4]⟩,none⟩⟩,
⟨Case10293.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,7,8},⟨0,![5,6,1,2,0,7,8,3,4]⟩,none⟩⟩,
⟨Case10294.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,5,6,7},⟨0,![5,6,0,1,7,2,3,4,8]⟩,none⟩⟩,
⟨Case10294.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,5,6,8},⟨0,![6,5,1,0,7,2,3,8,4]⟩,none⟩⟩,
⟨Case10295.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,5,7,8},⟨0,![5,6,0,1,7,2,8,3,4]⟩,none⟩⟩,
⟨Case10296.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,6,7,8},⟨0,![5,6,0,1,7,8,2,3,4]⟩,none⟩⟩,
⟨Case10297.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,4,5,6,7},⟨0,![5,6,0,7,1,2,3,4,8]⟩,none⟩⟩,
⟨Case10298.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,4,5,6,8},⟨0,![6,5,0,7,1,2,3,8,4]⟩,none⟩⟩,
⟨Case10299.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,4,5,7,8},⟨0,![5,6,0,7,1,2,8,3,4]⟩,none⟩⟩,
⟨Case10300.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,4,6,7,8},⟨0,![5,6,1,7,0,8,2,3,4]⟩,none⟩⟩,
⟨Case10301.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,5,6,7,8},⟨0,![5,6,0,7,8,1,2,3,4]⟩,none⟩⟩,
⟨Case10298.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,4,5,6,7},⟨0,![5,6,7,0,1,2,3,4,8]⟩,none⟩⟩,
⟨Case10297.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,4,5,6,8},⟨0,![6,5,7,0,1,2,3,8,4]⟩,none⟩⟩,
⟨Case10299.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,4,5,7,8},⟨0,![6,5,7,0,1,2,8,4,3]⟩,none⟩⟩,
⟨Case10300.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,4,6,7,8},⟨0,![6,5,7,1,0,8,2,4,3]⟩,none⟩⟩,
⟨Case10301.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,5,6,7,8},⟨0,![6,5,7,0,8,1,2,4,3]⟩,none⟩⟩,
⟨Case10302.big,⟨[{2,3,4,6},{2,5,7},{0,6,7},{3,5,8},{1,6,8},{4,7,8}],{4,5,6,7,8},⟨0,![5,6,7,8,0,1,2,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case10290.safe,Case10291.safe,Case10291.safe,Case10292.safe,Case10292.safe,Case10293.safe,Case10294.safe,Case10294.safe,Case10295.safe,Case10296.safe,Case10297.safe,Case10298.safe,Case10299.safe,Case10300.safe,Case10301.safe,Case10298.safe,Case10297.safe,Case10299.safe,Case10300.safe,Case10301.safe,Case10302.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family270
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
