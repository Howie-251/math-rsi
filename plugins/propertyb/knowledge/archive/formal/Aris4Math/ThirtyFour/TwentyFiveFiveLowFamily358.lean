import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric486
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family358
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,1,5,6,7},{2,5,8},{3,6,8},{4,7,8}],[{0,2},{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{3,5},{4,5},{2,6},{4,6},{2,7},{3,7},{0,1,5,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}],{0,1,5,6,7,8},[{0,1,5,6,7},{0,1,5,6,8},{0,1,5,7,8},{0,1,6,7,8},{0,5,6,7,8},{1,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case11679.big,⟨[{0,1,5,6,7},{2,5,8},{3,6,8},{4,7,8}],{0,1,5,6,7},⟨0,![0,1,5,6,7,2,3,4,8]⟩,none⟩⟩,
⟨Case11680.big,⟨[{0,1,5,6,7},{2,5,8},{3,6,8},{4,7,8}],{0,1,5,6,8},⟨0,![0,1,5,6,7,2,3,8,4]⟩,none⟩⟩,
⟨Case11680.big,⟨[{0,1,5,6,7},{2,5,8},{3,6,8},{4,7,8}],{0,1,5,7,8},⟨0,![0,1,5,7,6,2,8,3,4]⟩,none⟩⟩,
⟨Case11680.big,⟨[{0,1,5,6,7},{2,5,8},{3,6,8},{4,7,8}],{0,1,6,7,8},⟨0,![0,1,7,5,6,8,2,3,4]⟩,none⟩⟩,
⟨Case11681.big,⟨[{0,1,5,6,7},{2,5,8},{3,6,8},{4,7,8}],{0,5,6,7,8},⟨0,![0,5,6,7,8,1,2,3,4]⟩,none⟩⟩,
⟨Case11681.big,⟨[{0,1,5,6,7},{2,5,8},{3,6,8},{4,7,8}],{1,5,6,7,8},⟨0,![5,0,6,7,8,1,2,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case11679.safe,Case11680.safe,Case11680.safe,Case11680.safe,Case11681.safe,Case11681.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family358
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
