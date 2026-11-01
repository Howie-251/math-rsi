import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric50
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family30
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,1,3},{2,4,5},{3,6,7},{4,6,8},{5,7,8}],[{0,2},{1,2},{0,1,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}],{3,4,5,6,7,8},[{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case1201.big,⟨[{0,1,3},{2,4,5},{3,6,7},{4,6,8},{5,7,8}],{3,4,5,6,7},⟨0,![6,7,5,2,3,4,0,1,8]⟩,none⟩⟩,
⟨Case1202.big,⟨[{0,1,3},{2,4,5},{3,6,7},{4,6,8},{5,7,8}],{3,4,5,6,8},⟨0,![6,7,5,4,0,3,2,8,1]⟩,none⟩⟩,
⟨Case1202.big,⟨[{0,1,3},{2,4,5},{3,6,7},{4,6,8},{5,7,8}],{3,4,5,7,8},⟨0,![6,7,5,4,3,0,8,2,1]⟩,none⟩⟩,
⟨Case1203.big,⟨[{0,1,3},{2,4,5},{3,6,7},{4,6,8},{5,7,8}],{3,4,6,7,8},⟨0,![5,6,7,3,4,8,0,1,2]⟩,none⟩⟩,
⟨Case1203.big,⟨[{0,1,3},{2,4,5},{3,6,7},{4,6,8},{5,7,8}],{3,5,6,7,8},⟨0,![5,6,7,3,8,4,1,0,2]⟩,none⟩⟩,
⟨Case1204.big,⟨[{0,1,3},{2,4,5},{3,6,7},{4,6,8},{5,7,8}],{4,5,6,7,8},⟨0,![6,7,5,8,1,2,3,4,0]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case1201.safe,Case1202.safe,Case1202.safe,Case1203.safe,Case1203.safe,Case1204.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family30
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
