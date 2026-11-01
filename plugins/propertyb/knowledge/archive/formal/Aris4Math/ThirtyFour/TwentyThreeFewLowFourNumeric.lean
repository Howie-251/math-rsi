import Aris4Math.ThirtyFour.TwentyThreeFewLowFourData
namespace Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.LockExtension
open Aris4Math.ThirtyFour.PromotionCatalog
open Aris4Math.ThirtyFour.PromotionReconstruction
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 1000

namespace OneLow
open TwentyThreeFewLowBase (Case)
theorem coverage0 : (catalogue 0).all (fun values => decide (covered 0 values))=true := by decide +kernel

theorem coverage1 : (catalogue 1).all (fun values => decide (covered 1 values))=true := by decide +kernel

theorem coverage2 : (catalogue 2).all (fun values => decide (covered 2 values))=true := by decide +kernel

theorem coverage3 : (catalogue 3).all (fun values => decide (covered 3 values))=true := by decide +kernel

theorem coverage4 : (catalogue 4).all (fun values => decide (covered 4 values))=true := by decide +kernel

theorem coverage5 : (catalogue 5).all (fun values => decide (covered 5 values))=true := by decide +kernel

theorem coverage (c : Case) (values : List ℕ) (member : values∈catalogue c) : covered c values := by
  have all : (catalogue c).all (fun values => decide (covered c values))=true := by
    fin_cases c

    · exact coverage0

    · exact coverage1

    · exact coverage2

    · exact coverage3

    · exact coverage4

    · exact coverage5

  exact of_decide_eq_true (List.all_eq_true.mp all values member)

end OneLow

namespace TwoLow
open TwentyThreeFewLowBase (Case)
theorem coverage0 : (catalogue 0).all (fun values => decide (covered 0 values))=true := by decide +kernel

theorem coverage1 : (catalogue 1).all (fun values => decide (covered 1 values))=true := by decide +kernel

theorem coverage2 : (catalogue 2).all (fun values => decide (covered 2 values))=true := by decide +kernel

theorem coverage3 : (catalogue 3).all (fun values => decide (covered 3 values))=true := by decide +kernel

theorem coverage4 : (catalogue 4).all (fun values => decide (covered 4 values))=true := by decide +kernel

theorem coverage5 : (catalogue 5).all (fun values => decide (covered 5 values))=true := by decide +kernel

theorem coverage (c : Case) (values : List ℕ) (member : values∈catalogue c) : covered c values := by
  have all : (catalogue c).all (fun values => decide (covered c values))=true := by
    fin_cases c

    · exact coverage0

    · exact coverage1

    · exact coverage2

    · exact coverage3

    · exact coverage4

    · exact coverage5

  exact of_decide_eq_true (List.all_eq_true.mp all values member)

end TwoLow
end Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage
