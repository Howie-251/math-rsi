import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric92
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family62
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],[{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4},{2,4},{3,4},{0,5},{1,5},{0,6},{1,6},{2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case2223.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,5,6},⟨0,![5,6,0,1,4,2,3,7,8]⟩,none⟩⟩,
⟨Case2223.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,5,7},⟨0,![5,6,1,0,4,2,7,3,8]⟩,none⟩⟩,
⟨Case2224.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,5,8},⟨0,![5,6,0,1,4,2,7,8,3]⟩,none⟩⟩,
⟨Case2224.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,6,7},⟨0,![5,6,0,1,4,7,2,3,8]⟩,none⟩⟩,
⟨Case2223.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,6,8},⟨0,![5,6,1,0,4,7,2,8,3]⟩,none⟩⟩,
⟨Case2223.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,4,7,8},⟨0,![5,6,0,1,4,7,8,2,3]⟩,none⟩⟩,
⟨Case2225.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,5,6,7},⟨0,![5,6,0,1,8,2,3,4,7]⟩,none⟩⟩,
⟨Case2225.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,5,6,8},⟨0,![5,6,0,1,8,3,2,7,4]⟩,none⟩⟩,
⟨Case2225.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,5,7,8},⟨0,![5,6,0,1,8,4,7,2,3]⟩,none⟩⟩,
⟨Case2225.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,3,6,7,8},⟨0,![5,6,0,1,8,7,4,3,2]⟩,none⟩⟩,
⟨Case2226.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,4,5,6,7},⟨0,![5,6,0,7,4,2,1,3,8]⟩,none⟩⟩,
⟨Case2226.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,4,5,6,8},⟨0,![5,6,0,7,4,1,2,8,3]⟩,none⟩⟩,
⟨Case2226.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,4,5,7,8},⟨0,![5,6,0,7,4,3,8,2,1]⟩,none⟩⟩,
⟨Case2226.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,4,6,7,8},⟨0,![5,6,0,7,4,8,3,1,2]⟩,none⟩⟩,
⟨Case2227.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{2,5,6,7,8},⟨0,![5,6,0,7,8,1,2,3,4]⟩,none⟩⟩,
⟨Case2226.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,4,5,6,7},⟨0,![5,6,7,0,4,2,3,1,8]⟩,none⟩⟩,
⟨Case2226.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,4,5,6,8},⟨0,![5,6,7,0,4,3,2,8,1]⟩,none⟩⟩,
⟨Case2226.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,4,5,7,8},⟨0,![5,6,7,0,4,1,8,2,3]⟩,none⟩⟩,
⟨Case2226.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,4,6,7,8},⟨0,![5,6,7,0,4,8,1,3,2]⟩,none⟩⟩,
⟨Case2227.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{3,5,6,7,8},⟨0,![5,6,7,0,8,1,3,2,4]⟩,none⟩⟩,
⟨Case2228.big,⟨[{0,1,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}],{4,5,6,7,8},⟨0,![5,6,7,8,0,1,3,4,2]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case2223.safe,Case2223.safe,Case2224.safe,Case2224.safe,Case2223.safe,Case2223.safe,Case2225.safe,Case2225.safe,Case2225.safe,Case2225.safe,Case2226.safe,Case2226.safe,Case2226.safe,Case2226.safe,Case2227.safe,Case2226.safe,Case2226.safe,Case2226.safe,Case2226.safe,Case2227.safe,Case2228.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family62
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
