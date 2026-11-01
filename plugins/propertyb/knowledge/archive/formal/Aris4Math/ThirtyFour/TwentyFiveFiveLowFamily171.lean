import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric276
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric277
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family171
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],[{0,1},{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{5,6},{1,7},{0,2,7},{4,7},{3,6,7},{0,8},{2,8},{1,3,8},{4,6,8},{5,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case6631.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,4,5,6},⟨0,![5,6,1,4,0,2,3,8,7]⟩,none⟩⟩,
⟨Case6632.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,4,5,7},⟨0,![5,6,0,3,2,1,7,4,8]⟩,none⟩⟩,
⟨Case6633.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,4,5,8},⟨0,![6,5,2,3,0,1,7,8,4]⟩,none⟩⟩,
⟨Case6634.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,4,6,7},⟨0,![5,6,3,1,2,7,0,4,8]⟩,none⟩⟩,
⟨Case6635.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,4,6,8},⟨0,![6,5,2,3,0,7,1,8,4]⟩,none⟩⟩,
⟨Case6636.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,4,7,8},⟨0,![5,6,0,2,1,7,8,3,4]⟩,none⟩⟩,
⟨Case6637.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,5,6,7},⟨0,![5,6,2,0,7,3,1,4,8]⟩,none⟩⟩,
⟨Case6638.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,5,6,8},⟨0,![6,5,1,2,7,0,3,8,4]⟩,none⟩⟩,
⟨Case6639.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,5,7,8},⟨0,![5,6,1,2,7,0,8,3,4]⟩,none⟩⟩,
⟨Case6640.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,3,6,7,8},⟨0,![6,5,2,0,7,8,1,3,4]⟩,none⟩⟩,
⟨Case6641.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,4,5,6,7},⟨0,![5,6,1,7,0,2,3,4,8]⟩,none⟩⟩,
⟨Case6642.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,4,5,6,8},⟨0,![5,6,2,7,0,1,3,8,4]⟩,none⟩⟩,
⟨Case6643.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,4,5,7,8},⟨0,![5,6,1,8,2,0,7,3,4]⟩,none⟩⟩,
⟨Case6644.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,4,6,7,8},⟨0,![5,6,2,8,0,7,1,4,3]⟩,none⟩⟩,
⟨Case6645.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{2,5,6,7,8},⟨0,![5,6,1,8,7,0,2,3,4]⟩,none⟩⟩,
⟨Case6646.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,4,5,6,7},⟨0,![6,5,7,1,2,3,0,4,8]⟩,none⟩⟩,
⟨Case6647.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,4,5,6,8},⟨0,![6,5,7,3,0,2,1,8,4]⟩,none⟩⟩,
⟨Case6648.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,4,5,7,8},⟨0,![6,5,7,2,1,0,8,4,3]⟩,none⟩⟩,
⟨Case6649.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,4,6,7,8},⟨0,![6,5,8,1,2,7,0,4,3]⟩,none⟩⟩,
⟨Case6650.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,5,6,7,8},⟨0,![6,5,8,0,7,2,1,3,4]⟩,none⟩⟩,
⟨Case6651.big,⟨[{2,4,5},{0,2,7},{3,6,7},{1,3,8},{4,6,8},{5,7,8}],{4,5,6,7,8},⟨0,![6,5,7,8,0,2,1,4,3]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case6631.safe,Case6632.safe,Case6633.safe,Case6634.safe,Case6635.safe,Case6636.safe,Case6637.safe,Case6638.safe,Case6639.safe,Case6640.safe,Case6641.safe,Case6642.safe,Case6643.safe,Case6644.safe,Case6645.safe,Case6646.safe,Case6647.safe,Case6648.safe,Case6649.safe,Case6650.safe,Case6651.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family171
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
