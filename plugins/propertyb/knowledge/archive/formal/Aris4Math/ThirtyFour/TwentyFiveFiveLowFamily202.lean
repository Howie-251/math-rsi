import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric326
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family202
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],[{0,1},{0,2},{1,2},{2,3},{1,4},{2,4},{1,5},{2,5},{0,3,4,5},{0,6},{1,6},{3,6},{5,6},{0,7},{1,7},{3,7},{4,7},{2,6,7},{0,8},{2,8},{1,3,8},{4,6,8},{5,7,8}],{0,3,4,5,6,7,8},[{0,3,4,5,6},{0,3,4,5,7},{0,3,4,5,8},{0,3,4,6,7},{0,3,4,6,8},{0,3,4,7,8},{0,3,5,6,7},{0,3,5,6,8},{0,3,5,7,8},{0,3,6,7,8},{0,4,5,6,7},{0,4,5,6,8},{0,4,5,7,8},{0,4,6,7,8},{0,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case7827.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,4,5,6},⟨0,![0,5,6,2,1,3,4,7,8]⟩,none⟩⟩,
⟨Case7827.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,4,5,7},⟨0,![0,5,6,2,3,1,7,4,8]⟩,none⟩⟩,
⟨Case7828.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,4,5,8},⟨0,![0,5,6,1,2,3,7,8,4]⟩,none⟩⟩,
⟨Case7829.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,4,6,7},⟨0,![0,5,6,2,1,7,3,4,8]⟩,none⟩⟩,
⟨Case7830.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,4,6,8},⟨0,![0,5,6,2,1,7,3,8,4]⟩,none⟩⟩,
⟨Case7831.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,4,7,8},⟨0,![0,5,6,1,2,7,8,3,4]⟩,none⟩⟩,
⟨Case7829.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,5,6,7},⟨0,![0,5,6,2,7,1,4,3,8]⟩,none⟩⟩,
⟨Case7831.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,5,6,8},⟨0,![0,5,6,1,7,2,3,8,4]⟩,none⟩⟩,
⟨Case7830.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,5,7,8},⟨0,![0,5,6,2,7,1,8,3,4]⟩,none⟩⟩,
⟨Case7832.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,3,6,7,8},⟨0,![0,5,6,1,7,8,2,3,4]⟩,none⟩⟩,
⟨Case7833.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,4,5,6,7},⟨0,![0,6,5,7,1,2,3,4,8]⟩,none⟩⟩,
⟨Case7834.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,4,5,6,8},⟨0,![0,6,5,7,1,2,3,8,4]⟩,none⟩⟩,
⟨Case7834.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,4,5,7,8},⟨0,![0,6,5,7,2,1,8,3,4]⟩,none⟩⟩,
⟨Case7835.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,4,6,7,8},⟨0,![0,6,5,8,1,7,2,3,4]⟩,none⟩⟩,
⟨Case7835.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{0,5,6,7,8},⟨0,![0,6,5,8,7,1,3,2,4]⟩,none⟩⟩,
⟨Case7836.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,4,5,6,7},⟨0,![5,6,7,2,0,1,3,4,8]⟩,none⟩⟩,
⟨Case7837.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,4,5,6,8},⟨0,![5,6,7,1,0,2,3,8,4]⟩,none⟩⟩,
⟨Case7837.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,4,5,7,8},⟨0,![5,6,7,1,2,0,8,3,4]⟩,none⟩⟩,
⟨Case7838.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,4,6,7,8},⟨0,![5,6,7,1,0,8,2,3,4]⟩,none⟩⟩,
⟨Case7838.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{3,5,6,7,8},⟨0,![5,6,7,1,8,0,3,2,4]⟩,none⟩⟩,
⟨Case7839.big,⟨[{0,3,4,5},{2,6,7},{1,3,8},{4,6,8},{5,7,8}],{4,5,6,7,8},⟨0,![5,7,6,8,0,1,2,3,4]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case7827.safe,Case7827.safe,Case7828.safe,Case7829.safe,Case7830.safe,Case7831.safe,Case7829.safe,Case7831.safe,Case7830.safe,Case7832.safe,Case7833.safe,Case7834.safe,Case7834.safe,Case7835.safe,Case7835.safe,Case7836.safe,Case7837.safe,Case7837.safe,Case7838.safe,Case7838.safe,Case7839.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family202
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
