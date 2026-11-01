import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric438
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family279
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,1,5,6},{2,3,7},{4,5,8},{6,7,8}],[{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{2,5},{3,5},{2,6},{3,6},{4,6},{0,1,5,6},{0,7},{1,7},{2,3,7},{4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}],{0,1,5,6,7,8},[{0,1,5,6,7},{0,1,5,6,8},{0,1,5,7,8},{0,1,6,7,8},{0,5,6,7,8},{1,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case10518.big,⟨[{0,1,5,6},{2,3,7},{4,5,8},{6,7,8}],{0,1,5,6,7},⟨0,![0,1,6,7,5,3,2,4,8]⟩,none⟩⟩,
⟨Case10519.big,⟨[{0,1,5,6},{2,3,7},{4,5,8},{6,7,8}],{0,1,5,6,8},⟨0,![0,1,6,7,5,2,3,8,4]⟩,none⟩⟩,
⟨Case10520.big,⟨[{0,1,5,6},{2,3,7},{4,5,8},{6,7,8}],{0,1,5,7,8},⟨0,![0,1,6,7,5,2,8,4,3]⟩,none⟩⟩,
⟨Case10521.big,⟨[{0,1,5,6},{2,3,7},{4,5,8},{6,7,8}],{0,1,6,7,8},⟨0,![0,1,5,6,7,8,2,3,4]⟩,none⟩⟩,
⟨Case10522.big,⟨[{0,1,5,6},{2,3,7},{4,5,8},{6,7,8}],{0,5,6,7,8},⟨0,![0,5,7,8,6,2,1,4,3]⟩,none⟩⟩,
⟨Case10522.big,⟨[{0,1,5,6},{2,3,7},{4,5,8},{6,7,8}],{1,5,6,7,8},⟨0,![5,0,7,8,6,2,1,4,3]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case10518.safe,Case10519.safe,Case10520.safe,Case10521.safe,Case10522.safe,Case10522.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family279
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
