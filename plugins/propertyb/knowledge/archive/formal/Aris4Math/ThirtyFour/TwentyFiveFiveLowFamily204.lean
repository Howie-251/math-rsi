import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric327
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric328
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family204
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],[{0,1},{0,2},{1,2},{2,3},{1,4},{2,4},{1,5},{2,5},{0,3,4,5},{0,6},{1,6},{3,6},{5,6},{0,7},{1,7},{2,7},{3,7},{4,6,7},{0,8},{1,3,8},{4,8},{2,6,8},{5,7,8}],{0,3,4,5,6,7,8},[{0,3,4,5,6},{0,3,4,5,7},{0,3,4,5,8},{0,3,4,6,7},{0,3,4,6,8},{0,3,4,7,8},{0,3,5,6,7},{0,3,5,6,8},{0,3,5,7,8},{0,3,6,7,8},{0,4,5,6,7},{0,4,5,6,8},{0,4,5,7,8},{0,4,6,7,8},{0,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case7853.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,4,5,6},⟨0,![0,5,6,2,1,3,4,7,8]⟩,none⟩⟩,
⟨Case7854.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,4,5,7},⟨0,![0,5,6,3,1,2,7,4,8]⟩,none⟩⟩,
⟨Case7855.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,4,5,8},⟨0,![0,5,6,1,3,2,8,7,4]⟩,none⟩⟩,
⟨Case7856.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,4,6,7},⟨0,![0,5,6,2,1,7,3,4,8]⟩,none⟩⟩,
⟨Case7857.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,4,6,8},⟨0,![0,5,6,2,1,7,3,8,4]⟩,none⟩⟩,
⟨Case7858.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,4,7,8},⟨0,![0,5,6,2,1,7,8,3,4]⟩,none⟩⟩,
⟨Case7859.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,5,6,7},⟨0,![0,5,6,2,7,1,4,3,8]⟩,none⟩⟩,
⟨Case7860.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,5,6,8},⟨0,![0,5,6,1,7,2,3,8,4]⟩,none⟩⟩,
⟨Case7861.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,5,7,8},⟨0,![0,5,6,2,7,1,8,3,4]⟩,none⟩⟩,
⟨Case7862.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,3,6,7,8},⟨0,![0,5,6,1,7,8,2,3,4]⟩,none⟩⟩,
⟨Case7863.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,4,5,6,7},⟨0,![0,6,5,7,1,2,4,3,8]⟩,none⟩⟩,
⟨Case7864.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,4,5,6,8},⟨0,![0,6,5,7,1,2,3,8,4]⟩,none⟩⟩,
⟨Case7865.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,4,5,7,8},⟨0,![0,5,6,7,2,1,8,3,4]⟩,none⟩⟩,
⟨Case7866.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,4,6,7,8},⟨0,![0,6,5,8,1,7,2,3,4]⟩,none⟩⟩,
⟨Case7867.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{0,5,6,7,8},⟨0,![0,6,5,8,7,1,3,2,4]⟩,none⟩⟩,
⟨Case7868.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{3,4,5,6,7},⟨0,![5,6,7,2,0,1,4,3,8]⟩,none⟩⟩,
⟨Case7869.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{3,4,5,6,8},⟨0,![5,6,7,1,0,2,3,8,4]⟩,none⟩⟩,
⟨Case7870.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{3,4,5,7,8},⟨0,![5,6,7,2,1,0,8,3,4]⟩,none⟩⟩,
⟨Case7871.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{3,4,6,7,8},⟨0,![5,6,7,1,0,8,2,3,4]⟩,none⟩⟩,
⟨Case7872.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{3,5,6,7,8},⟨0,![5,6,7,1,8,0,3,2,4]⟩,none⟩⟩,
⟨Case7873.big,⟨[{0,3,4,5},{4,6,7},{1,3,8},{2,6,8},{5,7,8}],{4,5,6,7,8},⟨0,![5,7,6,8,0,1,3,2,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case7853.safe,Case7854.safe,Case7855.safe,Case7856.safe,Case7857.safe,Case7858.safe,Case7859.safe,Case7860.safe,Case7861.safe,Case7862.safe,Case7863.safe,Case7864.safe,Case7865.safe,Case7866.safe,Case7867.safe,Case7868.safe,Case7869.safe,Case7870.safe,Case7871.safe,Case7872.safe,Case7873.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family204
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
