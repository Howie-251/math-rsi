import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric425
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family266
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}],[{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{2,6},{3,4,6},{5,6},{1,7},{4,7},{3,5,7},{0,6,7},{0,8},{3,8},{4,5,8},{1,6,8},{2,7,8}],{3,4,5,6,7,8},[{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case10206.big,⟨[{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}],{3,4,5,6,7},⟨0,![5,6,7,0,1,2,3,4,8]⟩,none⟩⟩,
⟨Case10206.big,⟨[{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}],{3,4,5,6,8},⟨0,![6,5,7,1,0,2,3,8,4]⟩,none⟩⟩,
⟨Case10206.big,⟨[{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}],{3,4,5,7,8},⟨0,![6,7,5,1,2,0,8,3,4]⟩,none⟩⟩,
⟨Case10207.big,⟨[{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}],{3,4,6,7,8},⟨0,![5,6,7,0,1,8,2,3,4]⟩,none⟩⟩,
⟨Case10207.big,⟨[{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}],{3,5,6,7,8},⟨0,![5,7,6,0,8,1,3,2,4]⟩,none⟩⟩,
⟨Case10207.big,⟨[{3,4,6},{3,5,7},{0,6,7},{4,5,8},{1,6,8},{2,7,8}],{4,5,6,7,8},⟨0,![7,5,6,8,0,1,3,4,2]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case10206.safe,Case10206.safe,Case10206.safe,Case10207.safe,Case10207.safe,Case10207.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family266
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
