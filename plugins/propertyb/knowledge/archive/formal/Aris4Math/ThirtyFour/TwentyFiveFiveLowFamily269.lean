import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric427
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric428
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family269
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],[{0,1},{1,2},{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{2,5},{4,5},{0,6},{2,3,4,6},{1,7},{0,2,7},{3,7},{5,6,7},{0,8},{2,8},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case10269.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,5,6},⟨0,![5,6,1,0,2,3,4,8,7]⟩,none⟩⟩,
⟨Case10270.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,5,7},⟨0,![5,6,1,0,2,3,7,4,8]⟩,none⟩⟩,
⟨Case10271.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,5,8},⟨0,![5,6,2,0,1,3,7,8,4]⟩,none⟩⟩,
⟨Case10272.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,6,7},⟨0,![5,6,0,2,1,7,3,4,8]⟩,none⟩⟩,
⟨Case10273.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,6,8},⟨0,![5,6,2,0,1,7,3,8,4]⟩,none⟩⟩,
⟨Case10274.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,4,7,8},⟨0,![5,6,1,2,0,7,8,3,4]⟩,none⟩⟩,
⟨Case10275.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,5,6,7},⟨0,![5,6,1,0,7,2,3,4,8]⟩,none⟩⟩,
⟨Case10276.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,5,6,8},⟨0,![5,6,1,0,7,2,3,8,4]⟩,none⟩⟩,
⟨Case10277.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,5,7,8},⟨0,![5,6,1,0,7,2,8,4,3]⟩,none⟩⟩,
⟨Case10278.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,3,6,7,8},⟨0,![5,6,0,1,7,8,2,3,4]⟩,none⟩⟩,
⟨Case10279.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,4,5,6,7},⟨0,![5,6,0,7,1,2,3,4,8]⟩,none⟩⟩,
⟨Case10280.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,4,5,6,8},⟨0,![5,6,1,7,0,2,3,8,4]⟩,none⟩⟩,
⟨Case10281.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,4,5,7,8},⟨0,![5,6,1,7,0,2,8,3,4]⟩,none⟩⟩,
⟨Case10282.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,4,6,7,8},⟨0,![5,6,1,7,0,8,2,3,4]⟩,none⟩⟩,
⟨Case10283.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{2,5,6,7,8},⟨0,![5,6,0,7,8,1,2,3,4]⟩,none⟩⟩,
⟨Case10284.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,4,5,6,7},⟨0,![6,5,7,0,1,2,3,4,8]⟩,none⟩⟩,
⟨Case10285.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,4,5,6,8},⟨0,![6,5,7,0,1,2,3,8,4]⟩,none⟩⟩,
⟨Case10286.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,4,5,7,8},⟨0,![5,6,7,0,1,2,8,4,3]⟩,none⟩⟩,
⟨Case10287.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,4,6,7,8},⟨0,![6,5,7,1,0,8,2,4,3]⟩,none⟩⟩,
⟨Case10288.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{3,5,6,7,8},⟨0,![6,5,8,0,7,1,2,4,3]⟩,none⟩⟩,
⟨Case10289.big,⟨[{2,3,4,6},{0,2,7},{5,6,7},{3,5,8},{1,6,8},{4,7,8}],{4,5,6,7,8},⟨0,![6,5,8,7,0,1,2,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case10269.safe,Case10270.safe,Case10271.safe,Case10272.safe,Case10273.safe,Case10274.safe,Case10275.safe,Case10276.safe,Case10277.safe,Case10278.safe,Case10279.safe,Case10280.safe,Case10281.safe,Case10282.safe,Case10283.safe,Case10284.safe,Case10285.safe,Case10286.safe,Case10287.safe,Case10288.safe,Case10289.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family269
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
