import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric326
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric327
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family203
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],[{0,1},{0,2},{1,3},{2,3},{1,4},{2,4},{1,5},{2,5},{0,3,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,8},{1,2,8},{3,8},{4,6,8},{5,7,8}],{0,3,4,5,6,7,8},[{0,3,4,5,6},{0,3,4,5,7},{0,3,4,5,8},{0,3,4,6,7},{0,3,4,6,8},{0,3,4,7,8},{0,3,5,6,7},{0,3,5,6,8},{0,3,5,7,8},{0,3,6,7,8},{0,4,5,6,7},{0,4,5,6,8},{0,4,5,7,8},{0,4,6,7,8},{0,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case7840.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,4,5,6},⟨0,![0,5,6,1,2,3,4,7,8]⟩,none⟩⟩,
⟨Case7840.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,4,5,7},⟨0,![0,5,6,1,3,2,7,4,8]⟩,none⟩⟩,
⟨Case7841.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,4,5,8},⟨0,![0,5,6,3,1,2,7,8,4]⟩,none⟩⟩,
⟨Case7842.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,4,6,7},⟨0,![0,5,6,1,2,7,3,4,8]⟩,none⟩⟩,
⟨Case7843.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,4,6,8},⟨0,![0,5,6,2,1,7,3,8,4]⟩,none⟩⟩,
⟨Case7844.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,4,7,8},⟨0,![0,5,6,1,2,7,8,3,4]⟩,none⟩⟩,
⟨Case7842.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,5,6,7},⟨0,![0,5,6,1,7,2,4,3,8]⟩,none⟩⟩,
⟨Case7844.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,5,6,8},⟨0,![0,5,6,1,7,2,3,8,4]⟩,none⟩⟩,
⟨Case7843.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,5,7,8},⟨0,![0,5,6,2,7,1,8,3,4]⟩,none⟩⟩,
⟨Case7845.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,3,6,7,8},⟨0,![0,5,6,1,7,8,2,3,4]⟩,none⟩⟩,
⟨Case7846.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,4,5,6,7},⟨0,![0,5,6,7,1,2,3,4,8]⟩,none⟩⟩,
⟨Case7847.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,4,5,6,8},⟨0,![0,5,6,7,1,2,3,8,4]⟩,none⟩⟩,
⟨Case7847.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,4,5,7,8},⟨0,![0,5,6,7,2,1,8,3,4]⟩,none⟩⟩,
⟨Case7848.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,4,6,7,8},⟨0,![0,5,6,7,1,8,2,3,4]⟩,none⟩⟩,
⟨Case7848.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{0,5,6,7,8},⟨0,![0,5,6,7,8,1,3,2,4]⟩,none⟩⟩,
⟨Case7849.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{3,4,5,6,7},⟨0,![5,6,7,0,1,2,3,4,8]⟩,none⟩⟩,
⟨Case7850.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{3,4,5,6,8},⟨0,![5,6,7,1,0,2,3,8,4]⟩,none⟩⟩,
⟨Case7850.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{3,4,5,7,8},⟨0,![5,6,7,1,2,0,8,3,4]⟩,none⟩⟩,
⟨Case7851.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{3,4,6,7,8},⟨0,![5,6,7,0,1,8,2,3,4]⟩,none⟩⟩,
⟨Case7851.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{3,5,6,7,8},⟨0,![5,6,7,0,8,1,3,2,4]⟩,none⟩⟩,
⟨Case7852.big,⟨[{0,3,4,5},{3,6,7},{1,2,8},{4,6,8},{5,7,8}],{4,5,6,7,8},⟨0,![5,6,7,8,0,1,2,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case7840.safe,Case7840.safe,Case7841.safe,Case7842.safe,Case7843.safe,Case7844.safe,Case7842.safe,Case7844.safe,Case7843.safe,Case7845.safe,Case7846.safe,Case7847.safe,Case7847.safe,Case7848.safe,Case7848.safe,Case7849.safe,Case7850.safe,Case7850.safe,Case7851.safe,Case7851.safe,Case7852.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family203
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
