import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric477
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family324
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],[{0,2},{1,2},{0,3},{1,3},{2,3},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{2,7},{0,1,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}],{0,1,4,5,6,7,8},[{0,1,4,5,6},{0,1,4,5,7},{0,1,4,5,8},{0,1,4,6,7},{0,1,4,6,8},{0,1,4,7,8},{0,1,5,6,7},{0,1,5,6,8},{0,1,5,7,8},{0,1,6,7,8},{0,4,5,6,7},{0,4,5,6,8},{0,4,5,7,8},{0,4,6,7,8},{0,5,6,7,8},{1,4,5,6,7},{1,4,5,6,8},{1,4,5,7,8},{1,4,6,7,8},{1,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case11450.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,4,5,6},⟨0,![0,1,5,6,2,4,3,7,8]⟩,none⟩⟩,
⟨Case11451.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,4,5,7},⟨0,![0,1,5,6,2,3,7,4,8]⟩,none⟩⟩,
⟨Case11452.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,4,5,8},⟨0,![0,1,5,6,2,3,7,8,4]⟩,none⟩⟩,
⟨Case11453.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,4,6,7},⟨0,![0,1,6,5,2,7,3,4,8]⟩,none⟩⟩,
⟨Case11454.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,4,6,8},⟨0,![0,1,5,6,2,7,3,8,4]⟩,none⟩⟩,
⟨Case11455.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,4,7,8},⟨0,![0,1,6,5,2,8,7,3,4]⟩,none⟩⟩,
⟨Case11456.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,5,6,7},⟨0,![0,1,5,6,7,2,3,4,8]⟩,none⟩⟩,
⟨Case11457.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,5,6,8},⟨0,![0,1,5,6,7,2,3,8,4]⟩,none⟩⟩,
⟨Case11458.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,5,7,8},⟨0,![0,1,5,6,7,2,8,3,4]⟩,none⟩⟩,
⟨Case11459.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,1,6,7,8},⟨0,![0,1,6,5,7,8,2,3,4]⟩,none⟩⟩,
⟨Case11460.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,4,5,6,7},⟨0,![0,5,6,7,1,3,2,4,8]⟩,none⟩⟩,
⟨Case11461.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,4,5,6,8},⟨0,![0,5,6,7,1,3,2,8,4]⟩,none⟩⟩,
⟨Case11462.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,4,5,7,8},⟨0,![0,5,6,7,1,2,8,3,4]⟩,none⟩⟩,
⟨Case11463.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,4,6,7,8},⟨0,![0,5,7,6,1,8,2,3,4]⟩,none⟩⟩,
⟨Case11464.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{0,5,6,7,8},⟨0,![0,5,6,7,8,1,2,3,4]⟩,none⟩⟩,
⟨Case11460.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{1,4,5,6,7},⟨0,![5,0,6,7,1,3,2,4,8]⟩,none⟩⟩,
⟨Case11461.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{1,4,5,6,8},⟨0,![5,0,6,7,1,3,2,8,4]⟩,none⟩⟩,
⟨Case11462.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{1,4,5,7,8},⟨0,![5,0,6,7,1,2,8,3,4]⟩,none⟩⟩,
⟨Case11463.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{1,4,6,7,8},⟨0,![5,0,7,6,1,8,2,3,4]⟩,none⟩⟩,
⟨Case11464.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{1,5,6,7,8},⟨0,![5,0,6,7,8,1,2,3,4]⟩,none⟩⟩,
⟨Case11465.big,⟨[{0,1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}],{4,5,6,7,8},⟨0,![5,6,7,8,0,2,1,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case11450.safe,Case11451.safe,Case11452.safe,Case11453.safe,Case11454.safe,Case11455.safe,Case11456.safe,Case11457.safe,Case11458.safe,Case11459.safe,Case11460.safe,Case11461.safe,Case11462.safe,Case11463.safe,Case11464.safe,Case11460.safe,Case11461.safe,Case11462.safe,Case11463.safe,Case11464.safe,Case11465.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family324
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
