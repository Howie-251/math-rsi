import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric58
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric59
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family35
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],[{0,1},{1,2},{1,3},{0,2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case1408.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,4,5,6},⟨0,![5,6,0,1,4,2,3,8,7]⟩,none⟩⟩,
⟨Case1409.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,4,5,7},⟨0,![5,6,0,1,3,2,7,4,8]⟩,none⟩⟩,
⟨Case1410.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,4,5,8},⟨0,![5,6,0,2,3,1,7,8,4]⟩,none⟩⟩,
⟨Case1411.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,4,6,7},⟨0,![5,6,1,0,2,7,3,4,8]⟩,none⟩⟩,
⟨Case1412.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,4,6,8},⟨0,![5,6,2,3,0,7,1,8,4]⟩,none⟩⟩,
⟨Case1413.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,4,7,8},⟨0,![5,6,1,0,2,7,8,3,4]⟩,none⟩⟩,
⟨Case1414.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,5,6,7},⟨0,![5,6,2,3,7,0,1,4,8]⟩,none⟩⟩,
⟨Case1415.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,5,6,8},⟨0,![5,6,0,2,7,1,3,8,4]⟩,none⟩⟩,
⟨Case1416.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,5,7,8},⟨0,![5,6,0,2,8,1,7,4,3]⟩,none⟩⟩,
⟨Case1417.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,3,6,7,8},⟨0,![5,6,1,0,8,7,2,4,3]⟩,none⟩⟩,
⟨Case1418.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,4,5,6,7},⟨0,![6,5,3,7,2,1,0,4,8]⟩,none⟩⟩,
⟨Case1419.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,4,5,6,8},⟨0,![5,6,2,7,3,0,1,8,4]⟩,none⟩⟩,
⟨Case1420.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,4,5,7,8},⟨0,![6,5,1,8,2,0,7,4,3]⟩,none⟩⟩,
⟨Case1421.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,4,6,7,8},⟨0,![6,5,2,8,0,7,1,4,3]⟩,none⟩⟩,
⟨Case1422.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{2,5,6,7,8},⟨0,![5,6,2,8,7,0,1,4,3]⟩,none⟩⟩,
⟨Case1423.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{3,4,5,6,7},⟨0,![6,5,7,3,2,1,0,4,8]⟩,none⟩⟩,
⟨Case1424.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{3,4,5,6,8},⟨0,![5,6,7,3,1,2,0,8,4]⟩,none⟩⟩,
⟨Case1425.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{3,4,5,7,8},⟨0,![6,5,8,0,1,2,7,3,4]⟩,none⟩⟩,
⟨Case1426.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{3,4,6,7,8},⟨0,![6,5,8,2,0,7,1,4,3]⟩,none⟩⟩,
⟨Case1427.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{3,5,6,7,8},⟨0,![5,6,7,2,8,0,1,3,4]⟩,none⟩⟩,
⟨Case1428.big,⟨[{0,2,3},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{4,5,6,7,8},⟨0,![6,5,7,8,1,2,0,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case1408.safe,Case1409.safe,Case1410.safe,Case1411.safe,Case1412.safe,Case1413.safe,Case1414.safe,Case1415.safe,Case1416.safe,Case1417.safe,Case1418.safe,Case1419.safe,Case1420.safe,Case1421.safe,Case1422.safe,Case1423.safe,Case1424.safe,Case1425.safe,Case1426.safe,Case1427.safe,Case1428.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family35
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
