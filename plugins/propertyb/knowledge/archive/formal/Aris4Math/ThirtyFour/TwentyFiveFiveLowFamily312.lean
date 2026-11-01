import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric469
import Aris4Math.ThirtyFour.TwentyFiveFiveLowNumeric470
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Family312
def family : TwentyFiveLowColorPruning.Family 9 := ⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],[{0,1},{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{1,7},{0,2,7},{3,4,7},{5,6,7},{0,8},{1,3,8},{2,5,8},{4,6,8},{7,8}],{2,3,4,5,6,7,8},[{2,3,4,5,6},{2,3,4,5,7},{2,3,4,5,8},{2,3,4,6,7},{2,3,4,6,8},{2,3,4,7,8},{2,3,5,6,7},{2,3,5,6,8},{2,3,5,7,8},{2,3,6,7,8},{2,4,5,6,7},{2,4,5,6,8},{2,4,5,7,8},{2,4,6,7,8},{2,5,6,7,8},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,7,8},{3,4,6,7,8},{3,5,6,7,8},{4,5,6,7,8}],none⟩
theorem checked : decide (TwentyFiveLowColorPruning.Check 5 family)=true := by decide +kernel
def rows : List (Row 9) := [⟨Case11269.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,4,5,6},⟨0,![6,5,3,4,1,2,0,8,7]⟩,none⟩⟩,
⟨Case11270.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,4,5,7},⟨0,![5,6,2,0,1,3,7,4,8]⟩,none⟩⟩,
⟨Case11270.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,4,5,8},⟨0,![6,5,0,2,3,1,7,8,4]⟩,none⟩⟩,
⟨Case11271.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,4,6,7},⟨0,![5,6,3,1,0,7,2,4,8]⟩,none⟩⟩,
⟨Case11272.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,4,6,8},⟨0,![6,5,3,2,0,7,1,8,4]⟩,none⟩⟩,
⟨Case11273.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,4,7,8},⟨0,![6,5,2,0,1,8,7,3,4]⟩,none⟩⟩,
⟨Case11272.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,5,6,7},⟨0,![5,6,2,3,7,0,1,4,8]⟩,none⟩⟩,
⟨Case11271.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,5,6,8},⟨0,![6,5,1,3,7,0,2,8,4]⟩,none⟩⟩,
⟨Case11273.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,5,7,8},⟨0,![5,6,0,2,8,1,7,4,3]⟩,none⟩⟩,
⟨Case11274.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,3,6,7,8},⟨0,![5,6,0,1,7,8,2,3,4]⟩,none⟩⟩,
⟨Case11275.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,4,5,6,7},⟨0,![5,6,2,7,3,0,1,4,8]⟩,none⟩⟩,
⟨Case11276.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,4,5,6,8},⟨0,![5,6,2,7,3,0,1,8,4]⟩,none⟩⟩,
⟨Case11277.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,4,5,7,8},⟨0,![5,6,0,8,2,1,7,4,3]⟩,none⟩⟩,
⟨Case11278.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,4,6,7,8},⟨0,![5,6,2,8,1,7,0,4,3]⟩,none⟩⟩,
⟨Case11279.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{2,5,6,7,8},⟨0,![5,6,1,8,7,0,2,3,4]⟩,none⟩⟩,
⟨Case11276.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{3,4,5,6,7},⟨0,![6,5,7,2,0,3,1,4,8]⟩,none⟩⟩,
⟨Case11275.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{3,4,5,6,8},⟨0,![6,5,7,2,0,3,1,8,4]⟩,none⟩⟩,
⟨Case11277.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{3,4,5,7,8},⟨0,![6,5,8,0,1,2,7,3,4]⟩,none⟩⟩,
⟨Case11279.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{3,4,6,7,8},⟨0,![6,5,8,1,0,7,2,4,3]⟩,none⟩⟩,
⟨Case11278.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{3,5,6,7,8},⟨0,![6,5,8,2,7,1,0,3,4]⟩,none⟩⟩,
⟨Case11280.big,⟨[{0,2,7},{3,4,7},{5,6,7},{1,3,8},{2,5,8},{4,6,8}],{4,5,6,7,8},⟨0,![5,6,7,8,1,2,0,4,3]⟩,none⟩⟩]
theorem rows_checked : rows.all (fun r => decide (Check 5 r))=true := by decide +kernel
theorem source_complete : rows.map source=family.lows.map (fun low => (family.listed.toFinset,low)) := by decide +kernel
theorem rows_safe : ∀ r∈rows,Safe (standard 5) r.target := by
  simp only [rows,List.forall_mem_cons]
  exact ⟨Case11269.safe,Case11270.safe,Case11270.safe,Case11271.safe,Case11272.safe,Case11273.safe,Case11272.safe,Case11271.safe,Case11273.safe,Case11274.safe,Case11275.safe,Case11276.safe,Case11277.safe,Case11278.safe,Case11279.safe,Case11276.safe,Case11275.safe,Case11277.safe,Case11279.safe,Case11278.safe,Case11280.safe,List.forall_mem_nil _⟩
theorem safe : ∀ low∈family.lows,Safe (colors low) family.listed.toFinset :=
  from_rows 5 family.listed.toFinset family.lows rows source_complete rows_checked rows_safe
end Family312
end Aris4Math.ThirtyFour.TwentyFiveFiveLow
