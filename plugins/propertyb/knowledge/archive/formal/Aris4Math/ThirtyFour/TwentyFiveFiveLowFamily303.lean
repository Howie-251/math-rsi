import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric465
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric466
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family303
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],[{0,1},{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{1,5},{3,5},{0,6},{2,6},{4,5,6},{0,7},{1,7},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case11177.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,4,5,6},⟨0,![5,6,0,1,2,3,4,7,8]⟩,none⟩⟩,
⟨Case11178.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,4,5,7},⟨0,![5,6,0,1,2,4,7,3,8]⟩,none⟩⟩,
⟨Case11179.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,4,5,8},⟨0,![5,6,0,1,2,3,8,7,4]⟩,none⟩⟩,
⟨Case11178.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,4,6,7},⟨0,![6,5,1,0,2,7,4,3,8]⟩,none⟩⟩,
⟨Case11179.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,4,6,8},⟨0,![6,5,1,0,2,8,3,7,4]⟩,none⟩⟩,
⟨Case11180.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,4,7,8},⟨0,![5,6,0,1,2,7,8,3,4]⟩,none⟩⟩,
⟨Case11181.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,5,6,7},⟨0,![5,6,0,1,7,3,4,2,8]⟩,none⟩⟩,
⟨Case11182.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,5,6,8},⟨0,![5,6,0,1,7,2,3,8,4]⟩,none⟩⟩,
⟨Case11183.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,5,7,8},⟨0,![5,6,0,1,7,3,8,2,4]⟩,none⟩⟩,
⟨Case11183.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,3,6,7,8},⟨0,![6,5,1,0,7,8,3,2,4]⟩,none⟩⟩,
⟨Case11184.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,4,5,6,7},⟨0,![5,6,1,7,0,2,4,3,8]⟩,none⟩⟩,
⟨Case11185.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,4,5,6,8},⟨0,![5,6,1,7,0,2,3,8,4]⟩,none⟩⟩,
⟨Case11186.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,4,5,7,8},⟨0,![5,6,0,7,1,3,8,2,4]⟩,none⟩⟩,
⟨Case11187.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,4,6,7,8},⟨0,![6,5,1,7,0,8,3,2,4]⟩,none⟩⟩,
⟨Case11188.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{2,5,6,7,8},⟨0,![5,6,0,7,8,1,3,2,4]⟩,none⟩⟩,
⟨Case11184.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{3,4,5,6,7},⟨0,![6,5,7,1,0,4,2,3,8]⟩,none⟩⟩,
⟨Case11185.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{3,4,5,6,8},⟨0,![6,5,7,1,0,3,2,8,4]⟩,none⟩⟩,
⟨Case11187.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{3,4,5,7,8},⟨0,![5,6,7,1,0,3,8,2,4]⟩,none⟩⟩,
⟨Case11186.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{3,4,6,7,8},⟨0,![6,5,7,0,1,8,3,2,4]⟩,none⟩⟩,
⟨Case11188.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{3,5,6,7,8},⟨0,![6,5,7,0,8,3,1,2,4]⟩,none⟩⟩,
⟨Case11189.big,⟨[{4,5,6},{2,5,7},{3,6,7},{2,3,8},{0,5,8},{1,6,8},{4,7,8}],{4,5,6,7,8},⟨0,![5,6,7,8,0,1,2,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case11177.safe,Case11178.safe,Case11179.safe,Case11178.safe,Case11179.safe,Case11180.safe,Case11181.safe,Case11182.safe,Case11183.safe,Case11183.safe,Case11184.safe,Case11185.safe,Case11186.safe,Case11187.safe,Case11188.safe,Case11184.safe,Case11185.safe,Case11187.safe,Case11186.safe,Case11188.safe,Case11189.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family303
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
