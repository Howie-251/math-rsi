import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric477
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric478
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family325
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],[{0,2},{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{3,7},{2,4,7},{5,6,7},{2,8},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,4,5,6,7,8},[{0,1,4,5,6},{0,1,4,5,7},{0,1,4,5,8},{0,1,4,6,7},{0,1,4,6,8},{0,1,4,7,8},{0,1,5,6,7},{0,1,5,6,8},{0,1,5,7,8},{0,1,6,7,8},{0,4,5,6,7},{0,4,5,6,8},{0,4,5,7,8},{0,4,6,7,8},{0,5,6,7,8},{1,4,5,6,7},{1,4,5,6,8},{1,4,5,7,8},{1,4,6,7,8},{1,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case11466.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,4,5,6},⟨0,![0,1,6,5,3,4,2,8,7]⟩,none⟩⟩,
⟨Case11467.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,4,5,7},⟨0,![0,1,5,6,2,3,7,4,8]⟩,none⟩⟩,
⟨Case11467.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,4,5,8},⟨0,![0,1,6,5,3,2,7,8,4]⟩,none⟩⟩,
⟨Case11468.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,4,6,7},⟨0,![0,1,5,6,2,7,3,4,8]⟩,none⟩⟩,
⟨Case11469.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,4,6,8},⟨0,![0,1,5,6,2,7,3,8,4]⟩,none⟩⟩,
⟨Case11470.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,4,7,8},⟨0,![0,1,5,6,2,8,7,3,4]⟩,none⟩⟩,
⟨Case11469.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,5,6,7},⟨0,![0,1,6,5,7,2,3,4,8]⟩,none⟩⟩,
⟨Case11468.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,5,6,8},⟨0,![0,1,6,5,7,2,3,8,4]⟩,none⟩⟩,
⟨Case11470.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,5,7,8},⟨0,![0,1,6,5,8,2,7,4,3]⟩,none⟩⟩,
⟨Case11471.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,1,6,7,8},⟨0,![0,1,6,5,8,7,2,3,4]⟩,none⟩⟩,
⟨Case11472.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,4,5,6,7},⟨0,![0,5,6,7,3,2,1,4,8]⟩,none⟩⟩,
⟨Case11472.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,4,5,6,8},⟨0,![0,5,7,6,2,3,1,8,4]⟩,none⟩⟩,
⟨Case11473.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,4,5,7,8},⟨0,![0,5,6,7,1,2,8,3,4]⟩,none⟩⟩,
⟨Case11474.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,4,6,7,8},⟨0,![0,5,6,7,1,8,2,4,3]⟩,none⟩⟩,
⟨Case11474.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{0,5,6,7,8},⟨0,![0,5,7,6,8,1,2,3,4]⟩,none⟩⟩,
⟨Case11472.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{1,4,5,6,7},⟨0,![5,0,6,7,3,2,1,4,8]⟩,none⟩⟩,
⟨Case11472.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{1,4,5,6,8},⟨0,![5,0,7,6,2,3,1,8,4]⟩,none⟩⟩,
⟨Case11473.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{1,4,5,7,8},⟨0,![5,0,6,7,1,2,8,3,4]⟩,none⟩⟩,
⟨Case11474.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{1,4,6,7,8},⟨0,![5,0,6,7,1,8,2,4,3]⟩,none⟩⟩,
⟨Case11474.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{1,5,6,7,8},⟨0,![5,0,7,6,8,1,2,3,4]⟩,none⟩⟩,
⟨Case11475.big,⟨[{2,4,7},{5,6,7},{3,5,8},{4,6,8},{0,1,7,8}],{4,5,6,7,8},⟨0,![5,6,8,7,1,2,0,4,3]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case11466.safe,Case11467.safe,Case11467.safe,Case11468.safe,Case11469.safe,Case11470.safe,Case11469.safe,Case11468.safe,Case11470.safe,Case11471.safe,Case11472.safe,Case11472.safe,Case11473.safe,Case11474.safe,Case11474.safe,Case11472.safe,Case11472.safe,Case11473.safe,Case11474.safe,Case11474.safe,Case11475.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family325
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
