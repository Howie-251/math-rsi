import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric455
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family293
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],[{0,1},{0,2},{1,3},{2,3},{1,4},{2,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{4,6},{3,5,6},{0,7},{1,7},{2,7},{3,7},{4,5,7},{1,2,8},{0,3,4,8},{5,8},{6,7,8}],{0,3,4,5,6,7,8},[{0,3,4,5,6},{0,3,4,5,7},{0,3,4,5,8},{0,3,4,6,7},{0,3,4,6,8},{0,3,4,7,8},{0,3,5,6,7},{0,3,5,6,8},{0,3,5,7,8},{0,3,6,7,8},{0,4,5,6,7},{0,4,5,6,8},{0,4,5,7,8},{0,4,6,7,8},{0,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case10921.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,4,5,6},⟨0,![0,5,6,1,2,3,4,7,8]⟩,none⟩⟩,
⟨Case10921.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,4,5,7},⟨0,![0,5,6,2,1,3,7,4,8]⟩,none⟩⟩,
⟨Case10922.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,4,5,8},⟨0,![0,5,6,1,2,3,7,8,4]⟩,none⟩⟩,
⟨Case10923.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,4,6,7},⟨0,![0,5,6,1,2,7,3,4,8]⟩,none⟩⟩,
⟨Case10924.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,4,6,8},⟨0,![0,5,6,1,2,7,3,8,4]⟩,none⟩⟩,
⟨Case10924.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,4,7,8},⟨0,![0,5,6,2,1,7,8,3,4]⟩,none⟩⟩,
⟨Case10925.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,5,6,7},⟨0,![0,5,6,1,7,2,3,4,8]⟩,none⟩⟩,
⟨Case10926.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,5,6,8},⟨0,![0,5,6,1,7,3,2,8,4]⟩,none⟩⟩,
⟨Case10927.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,5,7,8},⟨0,![0,5,6,1,7,2,8,3,4]⟩,none⟩⟩,
⟨Case10928.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,3,6,7,8},⟨0,![0,5,6,1,7,8,2,3,4]⟩,none⟩⟩,
⟨Case10925.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,4,5,6,7},⟨0,![0,5,6,7,1,2,4,3,8]⟩,none⟩⟩,
⟨Case10927.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,4,5,6,8},⟨0,![0,5,6,7,1,2,3,8,4]⟩,none⟩⟩,
⟨Case10926.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,4,5,7,8},⟨0,![0,5,6,7,1,3,8,2,4]⟩,none⟩⟩,
⟨Case10928.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,4,6,7,8},⟨0,![0,5,6,7,1,8,3,2,4]⟩,none⟩⟩,
⟨Case10929.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{0,5,6,7,8},⟨0,![0,5,6,7,8,3,1,2,4]⟩,none⟩⟩,
⟨Case10930.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{3,4,5,6,7},⟨0,![5,6,7,0,1,2,3,4,8]⟩,none⟩⟩,
⟨Case10931.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{3,4,5,6,8},⟨0,![5,6,7,0,1,2,3,8,4]⟩,none⟩⟩,
⟨Case10931.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{3,4,5,7,8},⟨0,![5,6,7,1,0,2,8,3,4]⟩,none⟩⟩,
⟨Case10932.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{3,4,6,7,8},⟨0,![5,6,7,0,1,8,2,3,4]⟩,none⟩⟩,
⟨Case10933.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{3,5,6,7,8},⟨0,![5,6,7,0,8,2,1,3,4]⟩,none⟩⟩,
⟨Case10933.big,⟨[{3,5,6},{4,5,7},{1,2,8},{0,3,4,8},{6,7,8}],{4,5,6,7,8},⟨0,![5,6,7,8,0,2,3,1,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case10921.safe,Case10921.safe,Case10922.safe,Case10923.safe,Case10924.safe,Case10924.safe,Case10925.safe,Case10926.safe,Case10927.safe,Case10928.safe,Case10925.safe,Case10927.safe,Case10926.safe,Case10928.safe,Case10929.safe,Case10930.safe,Case10931.safe,Case10931.safe,Case10932.safe,Case10933.safe,Case10933.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family293
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
