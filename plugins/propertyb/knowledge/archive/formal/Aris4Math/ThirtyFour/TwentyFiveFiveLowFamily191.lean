import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric306
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric307
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family191
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],[{0,1},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{3,6},{0,2,7},{3,7},{5,7},{4,6,7},{0,8},{2,3,8},{4,8},{5,6,8},{1,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case7359.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,4,5,6},⟨0,![5,6,4,2,1,0,3,8,7]⟩,none⟩⟩,
⟨Case7360.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,4,5,7},⟨0,![5,6,3,0,1,2,7,4,8]⟩,none⟩⟩,
⟨Case7361.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,4,5,8},⟨0,![5,6,3,0,2,1,7,8,4]⟩,none⟩⟩,
⟨Case7362.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,4,6,7},⟨0,![5,6,3,2,0,7,1,4,8]⟩,none⟩⟩,
⟨Case7363.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,4,6,8},⟨0,![5,6,1,0,2,7,3,8,4]⟩,none⟩⟩,
⟨Case7364.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,4,7,8},⟨0,![5,6,1,0,2,7,8,4,3]⟩,none⟩⟩,
⟨Case7365.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,5,6,7},⟨0,![5,6,2,0,7,1,3,4,8]⟩,none⟩⟩,
⟨Case7366.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,5,6,8},⟨0,![5,6,2,0,7,1,3,8,4]⟩,none⟩⟩,
⟨Case7367.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,5,7,8},⟨0,![5,6,1,0,7,2,8,4,3]⟩,none⟩⟩,
⟨Case7368.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,3,6,7,8},⟨0,![5,6,0,1,8,7,2,4,3]⟩,none⟩⟩,
⟨Case7369.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,4,5,6,7},⟨0,![5,6,3,7,0,2,1,4,8]⟩,none⟩⟩,
⟨Case7370.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,4,5,6,8},⟨0,![5,6,3,7,2,0,1,8,4]⟩,none⟩⟩,
⟨Case7371.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,4,5,7,8},⟨0,![5,6,2,7,0,1,8,3,4]⟩,none⟩⟩,
⟨Case7372.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,4,6,7,8},⟨0,![5,6,2,8,1,7,0,3,4]⟩,none⟩⟩,
⟨Case7373.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{2,5,6,7,8},⟨0,![5,6,2,8,7,1,0,4,3]⟩,none⟩⟩,
⟨Case7374.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{3,4,5,6,7},⟨0,![5,6,7,2,0,1,3,4,8]⟩,none⟩⟩,
⟨Case7375.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{3,4,5,6,8},⟨0,![6,5,7,2,1,0,3,8,4]⟩,none⟩⟩,
⟨Case7376.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{3,4,5,7,8},⟨0,![6,5,8,1,2,0,7,4,3]⟩,none⟩⟩,
⟨Case7377.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{3,4,6,7,8},⟨0,![6,5,8,2,0,7,1,3,4]⟩,none⟩⟩,
⟨Case7378.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{3,5,6,7,8},⟨0,![6,5,8,2,7,0,1,4,3]⟩,none⟩⟩,
⟨Case7379.big,⟨[{3,4,5},{0,2,7},{4,6,7},{2,3,8},{5,6,8},{1,7,8}],{4,5,6,7,8},⟨0,![6,5,8,7,1,2,0,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case7359.safe,Case7360.safe,Case7361.safe,Case7362.safe,Case7363.safe,Case7364.safe,Case7365.safe,Case7366.safe,Case7367.safe,Case7368.safe,Case7369.safe,Case7370.safe,Case7371.safe,Case7372.safe,Case7373.safe,Case7374.safe,Case7375.safe,Case7376.safe,Case7377.safe,Case7378.safe,Case7379.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family191
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
