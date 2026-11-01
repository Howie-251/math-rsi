import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric457
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family296
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],[{0,1},{0,2},{1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{1,6},{0,3,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}],{0,3,4,5,6,7,8},[{0,3,4,5,6},{0,3,4,5,7},{0,3,4,5,8},{0,3,4,6,7},{0,3,4,6,8},{0,3,4,7,8},{0,3,5,6,7},{0,3,5,6,8},{0,3,5,7,8},{0,3,6,7,8},{0,4,5,6,7},{0,4,5,6,8},{0,4,5,7,8},{0,4,6,7,8},{0,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case10975.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,4,5,6},⟨0,![0,6,5,1,2,3,4,8,7]⟩,none⟩⟩,
⟨Case10976.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,4,5,7},⟨0,![0,5,6,1,2,3,7,4,8]⟩,none⟩⟩,
⟨Case10977.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,4,5,8},⟨0,![0,5,6,1,2,3,7,8,4]⟩,none⟩⟩,
⟨Case10977.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,4,6,7},⟨0,![0,6,5,1,2,7,3,4,8]⟩,none⟩⟩,
⟨Case10976.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,4,6,8},⟨0,![0,6,5,1,2,7,3,8,4]⟩,none⟩⟩,
⟨Case10978.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,4,7,8},⟨0,![0,6,5,1,2,8,7,3,4]⟩,none⟩⟩,
⟨Case10979.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,5,6,7},⟨0,![0,5,6,1,7,2,3,4,8]⟩,none⟩⟩,
⟨Case10979.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,5,6,8},⟨0,![0,6,5,1,7,3,2,8,4]⟩,none⟩⟩,
⟨Case10980.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,5,7,8},⟨0,![0,5,6,1,7,2,8,3,4]⟩,none⟩⟩,
⟨Case10980.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,3,6,7,8},⟨0,![0,6,5,1,7,8,2,4,3]⟩,none⟩⟩,
⟨Case10981.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,4,5,6,7},⟨0,![0,5,6,7,1,3,2,4,8]⟩,none⟩⟩,
⟨Case10981.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,4,5,6,8},⟨0,![0,6,5,7,1,2,3,8,4]⟩,none⟩⟩,
⟨Case10982.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,4,5,7,8},⟨0,![0,5,6,7,1,2,8,4,3]⟩,none⟩⟩,
⟨Case10982.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,4,6,7,8},⟨0,![0,6,5,7,1,8,2,3,4]⟩,none⟩⟩,
⟨Case10983.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{0,5,6,7,8},⟨0,![0,5,6,7,8,1,2,3,4]⟩,none⟩⟩,
⟨Case10984.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{3,4,5,6,7},⟨0,![5,6,7,0,1,3,2,4,8]⟩,none⟩⟩,
⟨Case10984.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{3,4,5,6,8},⟨0,![5,7,6,0,1,2,3,8,4]⟩,none⟩⟩,
⟨Case10985.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{3,4,5,7,8},⟨0,![5,6,7,0,1,2,8,4,3]⟩,none⟩⟩,
⟨Case10985.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{3,4,6,7,8},⟨0,![5,7,6,0,1,8,2,3,4]⟩,none⟩⟩,
⟨Case10986.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{3,5,6,7,8},⟨0,![5,6,7,0,8,1,2,3,4]⟩,none⟩⟩,
⟨Case10987.big,⟨[{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}],{4,5,6,7,8},⟨0,![5,7,6,8,0,1,2,4,3]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case10975.safe,Case10976.safe,Case10977.safe,Case10977.safe,Case10976.safe,Case10978.safe,Case10979.safe,Case10979.safe,Case10980.safe,Case10980.safe,Case10981.safe,Case10981.safe,Case10982.safe,Case10982.safe,Case10983.safe,Case10984.safe,Case10984.safe,Case10985.safe,Case10985.safe,Case10986.safe,Case10987.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family296
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
