import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric482
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family336
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],[{0,1},{1,2},{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{0,7},{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case11571.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,4,5,6},⟨0,![5,6,2,0,1,3,4,7,8]⟩,none⟩⟩,
⟨Case11572.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,4,5,7},⟨0,![5,6,1,0,2,3,7,4,8]⟩,none⟩⟩,
⟨Case11573.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,4,5,8},⟨0,![5,6,1,0,2,3,7,8,4]⟩,none⟩⟩,
⟨Case11572.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,4,6,7},⟨0,![5,6,1,2,0,7,3,4,8]⟩,none⟩⟩,
⟨Case11573.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,4,6,8},⟨0,![5,6,1,2,0,7,3,8,4]⟩,none⟩⟩,
⟨Case11574.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,4,7,8},⟨0,![5,6,0,1,2,7,8,3,4]⟩,none⟩⟩,
⟨Case11575.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,5,6,7},⟨0,![5,6,1,0,7,2,3,4,8]⟩,none⟩⟩,
⟨Case11576.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,5,6,8},⟨0,![5,6,1,0,7,2,3,8,4]⟩,none⟩⟩,
⟨Case11577.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,5,7,8},⟨0,![5,6,1,0,7,2,8,3,4]⟩,none⟩⟩,
⟨Case11578.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,3,6,7,8},⟨0,![5,6,0,1,7,8,2,3,4]⟩,none⟩⟩,
⟨Case11575.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,4,5,6,7},⟨0,![5,6,1,7,0,3,2,4,8]⟩,none⟩⟩,
⟨Case11576.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,4,5,6,8},⟨0,![5,6,1,7,0,3,2,8,4]⟩,none⟩⟩,
⟨Case11578.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,4,5,7,8},⟨0,![5,6,0,7,1,2,8,3,4]⟩,none⟩⟩,
⟨Case11577.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,4,6,7,8},⟨0,![5,6,1,7,0,8,2,3,4]⟩,none⟩⟩,
⟨Case11579.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{2,5,6,7,8},⟨0,![5,6,0,7,8,1,2,3,4]⟩,none⟩⟩,
⟨Case11580.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{3,4,5,6,7},⟨0,![6,5,7,0,1,2,3,4,8]⟩,none⟩⟩,
⟨Case11581.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{3,4,5,6,8},⟨0,![5,6,7,0,1,2,3,8,4]⟩,none⟩⟩,
⟨Case11582.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{3,4,5,7,8},⟨0,![6,5,7,0,1,2,8,3,4]⟩,none⟩⟩,
⟨Case11582.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{3,4,6,7,8},⟨0,![6,5,7,1,0,8,2,3,4]⟩,none⟩⟩,
⟨Case11583.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{3,5,6,7,8},⟨0,![6,5,8,0,7,1,2,3,4]⟩,none⟩⟩,
⟨Case11583.big,⟨[{2,3,4,7},{5,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}],{4,5,6,7,8},⟨0,![6,5,8,7,0,2,1,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case11571.safe,Case11572.safe,Case11573.safe,Case11572.safe,Case11573.safe,Case11574.safe,Case11575.safe,Case11576.safe,Case11577.safe,Case11578.safe,Case11575.safe,Case11576.safe,Case11578.safe,Case11577.safe,Case11579.safe,Case11580.safe,Case11581.safe,Case11582.safe,Case11582.safe,Case11583.safe,Case11583.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family336
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
