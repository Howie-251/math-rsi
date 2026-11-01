import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric242
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family152
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],[{0,1},{0,2},{1,2},{0,3},{1,3},{2,4},{3,4},{1,5},{3,5},{0,4,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{2,3,7},{5,6,7},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case5817.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,4,5,6},⟨0,![5,6,0,1,4,2,3,7,8]⟩,none⟩⟩,
⟨Case5818.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,4,5,7},⟨0,![5,6,0,1,4,3,8,2,7]⟩,none⟩⟩,
⟨Case5819.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,4,5,8},⟨0,![5,6,0,1,4,3,8,7,2]⟩,none⟩⟩,
⟨Case5818.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,4,6,7},⟨0,![6,5,1,0,4,8,3,2,7]⟩,none⟩⟩,
⟨Case5819.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,4,6,8},⟨0,![6,5,1,0,4,8,3,7,2]⟩,none⟩⟩,
⟨Case5820.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,4,7,8},⟨0,![5,6,0,1,4,7,8,2,3]⟩,none⟩⟩,
⟨Case5821.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,5,6,7},⟨0,![5,6,0,1,8,3,4,2,7]⟩,none⟩⟩,
⟨Case5822.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,5,6,8},⟨0,![5,6,0,1,8,3,4,7,2]⟩,none⟩⟩,
⟨Case5823.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,5,7,8},⟨0,![5,6,0,1,8,4,7,2,3]⟩,none⟩⟩,
⟨Case5823.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,3,6,7,8},⟨0,![6,5,1,0,8,7,4,2,3]⟩,none⟩⟩,
⟨Case5824.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,4,5,6,7},⟨0,![5,6,0,7,4,2,3,1,8]⟩,none⟩⟩,
⟨Case5825.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,4,5,6,8},⟨0,![5,6,0,7,3,1,4,8,2]⟩,none⟩⟩,
⟨Case5826.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,4,5,7,8},⟨0,![5,6,0,7,4,2,8,3,1]⟩,none⟩⟩,
⟨Case5827.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,4,6,7,8},⟨0,![6,5,0,7,3,8,4,1,2]⟩,none⟩⟩,
⟨Case5828.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{2,5,6,7,8},⟨0,![5,6,0,7,8,1,4,3,2]⟩,none⟩⟩,
⟨Case5824.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{3,4,5,6,7},⟨0,![6,5,7,0,4,3,2,1,8]⟩,none⟩⟩,
⟨Case5825.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{3,4,5,6,8},⟨0,![6,5,7,0,3,4,1,8,2]⟩,none⟩⟩,
⟨Case5827.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{3,4,5,7,8},⟨0,![5,6,7,0,3,4,8,1,2]⟩,none⟩⟩,
⟨Case5826.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{3,4,6,7,8},⟨0,![6,5,7,0,4,8,2,3,1]⟩,none⟩⟩,
⟨Case5828.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{3,5,6,7,8},⟨0,![6,5,7,0,8,4,1,3,2]⟩,none⟩⟩,
⟨Case5829.big,⟨[{0,4,5},{1,4,6},{2,3,7},{5,6,7},{2,5,8},{3,6,8},{4,7,8}],{4,5,6,7,8},⟨0,![5,6,7,8,1,2,3,0,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case5817.safe,Case5818.safe,Case5819.safe,Case5818.safe,Case5819.safe,Case5820.safe,Case5821.safe,Case5822.safe,Case5823.safe,Case5823.safe,Case5824.safe,Case5825.safe,Case5826.safe,Case5827.safe,Case5828.safe,Case5824.safe,Case5825.safe,Case5827.safe,Case5826.safe,Case5828.safe,Case5829.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family152
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
