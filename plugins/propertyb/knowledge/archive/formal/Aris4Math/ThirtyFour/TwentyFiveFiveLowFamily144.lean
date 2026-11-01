import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric222
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric223
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family144
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],[{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}],{0,1,2,5,6,7,8},[{0,1,2,5,6},{0,1,2,5,7},{0,1,2,5,8},{0,1,2,6,7},{0,1,2,6,8},{0,1,2,7,8},{0,1,5,6,7},{0,1,5,6,8},{0,1,5,7,8},{0,1,6,7,8},{0,2,5,6,7},{0,2,5,6,8},{0,2,5,7,8},{0,2,6,7,8},{0,5,6,7,8},{1,2,5,6,7},{1,2,5,6,8},{1,2,5,7,8},{1,2,6,7,8},{1,5,6,7,8},{2,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case5347.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,2,5,6},⟨0,![0,1,2,5,6,3,4,7,8]⟩,none⟩⟩,
⟨Case5348.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,2,5,7},⟨0,![0,1,2,5,6,3,8,4,7]⟩,none⟩⟩,
⟨Case5348.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,2,5,8},⟨0,![0,1,2,6,5,3,8,7,4]⟩,none⟩⟩,
⟨Case5349.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,2,6,7},⟨0,![0,1,2,5,6,7,3,4,8]⟩,none⟩⟩,
⟨Case5349.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,2,6,8},⟨0,![0,1,2,6,5,7,3,8,4]⟩,none⟩⟩,
⟨Case5350.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,2,7,8},⟨0,![0,1,2,5,6,7,8,3,4]⟩,none⟩⟩,
⟨Case5351.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,5,6,7},⟨0,![0,1,5,6,7,2,4,3,8]⟩,none⟩⟩,
⟨Case5351.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,5,6,8},⟨0,![0,1,5,7,6,2,4,8,3]⟩,none⟩⟩,
⟨Case5352.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,5,7,8},⟨0,![0,1,5,6,7,2,8,3,4]⟩,none⟩⟩,
⟨Case5353.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,1,6,7,8},⟨0,![0,1,5,6,7,8,2,3,4]⟩,none⟩⟩,
⟨Case5351.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,2,5,6,7},⟨0,![0,5,1,6,7,2,4,3,8]⟩,none⟩⟩,
⟨Case5351.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,2,5,6,8},⟨0,![0,5,1,7,6,2,4,8,3]⟩,none⟩⟩,
⟨Case5352.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,2,5,7,8},⟨0,![0,5,1,6,7,2,8,3,4]⟩,none⟩⟩,
⟨Case5353.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,2,6,7,8},⟨0,![0,5,1,6,7,8,2,3,4]⟩,none⟩⟩,
⟨Case5354.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{0,5,6,7,8},⟨0,![0,5,6,7,8,1,4,2,3]⟩,none⟩⟩,
⟨Case5351.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{1,2,5,6,7},⟨0,![5,0,1,6,7,2,4,3,8]⟩,none⟩⟩,
⟨Case5351.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{1,2,5,6,8},⟨0,![5,0,1,7,6,2,4,8,3]⟩,none⟩⟩,
⟨Case5352.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{1,2,5,7,8},⟨0,![5,0,1,6,7,2,8,3,4]⟩,none⟩⟩,
⟨Case5353.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{1,2,6,7,8},⟨0,![5,0,1,6,7,8,2,3,4]⟩,none⟩⟩,
⟨Case5354.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{1,5,6,7,8},⟨0,![5,0,6,7,8,1,4,2,3]⟩,none⟩⟩,
⟨Case5354.big,⟨[{0,1,2,5},{3,6,7},{4,6,8},{5,7,8}],{2,5,6,7,8},⟨0,![5,6,0,7,8,1,4,2,3]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case5347.safe,Case5348.safe,Case5348.safe,Case5349.safe,Case5349.safe,Case5350.safe,Case5351.safe,Case5351.safe,Case5352.safe,Case5353.safe,Case5351.safe,Case5351.safe,Case5352.safe,Case5353.safe,Case5354.safe,Case5351.safe,Case5351.safe,Case5352.safe,Case5353.safe,Case5354.safe,Case5354.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family144
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
