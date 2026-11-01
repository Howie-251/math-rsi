import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows0Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows0Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows1Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows2Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows3Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows4Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows5Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows6Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows7Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows8Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows9Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows10Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows11Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows12Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows13Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows14Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows15Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows16Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows17Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows18Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows19Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows19Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows20Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit8Rows21Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit8Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit8Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected0 : rows0.map Row.selected=choices (candidates 0) ∅ := by decide +kernel
theorem checked0 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 0))
  (choices (candidates 0) ∅) witnesses0 := by
  rw [← selected0]
  apply checked_rows
  simp only [rows0,List.all_append,TwentyFiveUnit8Rows0Batch0.checked,TwentyFiveUnit8Rows0Batch1.checked,Bool.true_and]
theorem selected1 : rows1.map Row.selected=choices (candidates 1) ∅ := by decide +kernel
theorem checked1 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 1))
  (choices (candidates 1) ∅) witnesses1 := by
  rw [← selected1]
  apply checked_rows
  simp only [rows1,List.all_append,TwentyFiveUnit8Rows1Batch0.checked,Bool.true_and]
theorem selected2 : rows2.map Row.selected=choices (candidates 2) ∅ := by decide +kernel
theorem checked2 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 2))
  (choices (candidates 2) ∅) witnesses2 := by
  rw [← selected2]
  apply checked_rows
  simp only [rows2,List.all_append,TwentyFiveUnit8Rows2Batch0.checked,Bool.true_and]
theorem selected3 : rows3.map Row.selected=choices (candidates 3) ∅ := by decide +kernel
theorem checked3 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 3))
  (choices (candidates 3) ∅) witnesses3 := by
  rw [← selected3]
  apply checked_rows
  simp only [rows3,List.all_append,TwentyFiveUnit8Rows3Batch0.checked,Bool.true_and]
theorem selected4 : rows4.map Row.selected=choices (candidates 4) ∅ := by decide +kernel
theorem checked4 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 4))
  (choices (candidates 4) ∅) witnesses4 := by
  rw [← selected4]
  apply checked_rows
  simp only [rows4,List.all_append,TwentyFiveUnit8Rows4Batch0.checked,Bool.true_and]
theorem selected5 : rows5.map Row.selected=choices (candidates 5) ∅ := by decide +kernel
theorem checked5 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 5))
  (choices (candidates 5) ∅) witnesses5 := by
  rw [← selected5]
  apply checked_rows
  simp only [rows5,List.all_append,TwentyFiveUnit8Rows5Batch0.checked,Bool.true_and]
theorem selected6 : rows6.map Row.selected=choices (candidates 6) ∅ := by decide +kernel
theorem checked6 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 6))
  (choices (candidates 6) ∅) witnesses6 := by
  rw [← selected6]
  apply checked_rows
  simp only [rows6,List.all_append,TwentyFiveUnit8Rows6Batch0.checked,Bool.true_and]
theorem selected7 : rows7.map Row.selected=choices (candidates 7) ∅ := by decide +kernel
theorem checked7 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 7))
  (choices (candidates 7) ∅) witnesses7 := by
  rw [← selected7]
  apply checked_rows
  simp only [rows7,List.all_append,TwentyFiveUnit8Rows7Batch0.checked,Bool.true_and]
theorem selected8 : rows8.map Row.selected=choices (candidates 8) ∅ := by decide +kernel
theorem checked8 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 8))
  (choices (candidates 8) ∅) witnesses8 := by
  rw [← selected8]
  apply checked_rows
  simp only [rows8,List.all_append,TwentyFiveUnit8Rows8Batch0.checked,Bool.true_and]
theorem selected9 : rows9.map Row.selected=choices (candidates 9) ∅ := by decide +kernel
theorem checked9 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 9))
  (choices (candidates 9) ∅) witnesses9 := by
  rw [← selected9]
  apply checked_rows
  simp only [rows9,List.all_append,TwentyFiveUnit8Rows9Batch0.checked,Bool.true_and]
theorem selected10 : rows10.map Row.selected=choices (candidates 10) ∅ := by decide +kernel
theorem checked10 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 10))
  (choices (candidates 10) ∅) witnesses10 := by
  rw [← selected10]
  apply checked_rows
  simp only [rows10,List.all_append,TwentyFiveUnit8Rows10Batch0.checked,Bool.true_and]
theorem selected11 : rows11.map Row.selected=choices (candidates 11) ∅ := by decide +kernel
theorem checked11 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 11))
  (choices (candidates 11) ∅) witnesses11 := by
  rw [← selected11]
  apply checked_rows
  simp only [rows11,List.all_append,TwentyFiveUnit8Rows11Batch0.checked,Bool.true_and]
theorem selected12 : rows12.map Row.selected=choices (candidates 12) ∅ := by decide +kernel
theorem checked12 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 12))
  (choices (candidates 12) ∅) witnesses12 := by
  rw [← selected12]
  apply checked_rows
  simp only [rows12,List.all_append,TwentyFiveUnit8Rows12Batch0.checked,Bool.true_and]
theorem selected13 : rows13.map Row.selected=choices (candidates 13) ∅ := by decide +kernel
theorem checked13 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 13))
  (choices (candidates 13) ∅) witnesses13 := by
  rw [← selected13]
  apply checked_rows
  simp only [rows13,List.all_append,TwentyFiveUnit8Rows13Batch0.checked,Bool.true_and]
theorem selected14 : rows14.map Row.selected=choices (candidates 14) ∅ := by decide +kernel
theorem checked14 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 14))
  (choices (candidates 14) ∅) witnesses14 := by
  rw [← selected14]
  apply checked_rows
  simp only [rows14,List.all_append,TwentyFiveUnit8Rows14Batch0.checked,Bool.true_and]
theorem selected15 : rows15.map Row.selected=choices (candidates 15) ∅ := by decide +kernel
theorem checked15 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 15))
  (choices (candidates 15) ∅) witnesses15 := by
  rw [← selected15]
  apply checked_rows
  simp only [rows15,List.all_append,TwentyFiveUnit8Rows15Batch0.checked,Bool.true_and]
theorem selected16 : rows16.map Row.selected=choices (candidates 16) ∅ := by decide +kernel
theorem checked16 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 16))
  (choices (candidates 16) ∅) witnesses16 := by
  rw [← selected16]
  apply checked_rows
  simp only [rows16,List.all_append,TwentyFiveUnit8Rows16Batch0.checked,Bool.true_and]
theorem selected17 : rows17.map Row.selected=choices (candidates 17) ∅ := by decide +kernel
theorem checked17 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 17))
  (choices (candidates 17) ∅) witnesses17 := by
  rw [← selected17]
  apply checked_rows
  simp only [rows17,List.all_append,TwentyFiveUnit8Rows17Batch0.checked,Bool.true_and]
theorem selected18 : rows18.map Row.selected=choices (candidates 18) ∅ := by decide +kernel
theorem checked18 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 18))
  (choices (candidates 18) ∅) witnesses18 := by
  rw [← selected18]
  apply checked_rows
  simp only [rows18,List.all_append,TwentyFiveUnit8Rows18Batch0.checked,Bool.true_and]
theorem selected19 : rows19.map Row.selected=choices (candidates 19) ∅ := by decide +kernel
theorem checked19 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 19))
  (choices (candidates 19) ∅) witnesses19 := by
  rw [← selected19]
  apply checked_rows
  simp only [rows19,List.all_append,TwentyFiveUnit8Rows19Batch0.checked,TwentyFiveUnit8Rows19Batch1.checked,Bool.true_and]
theorem selected20 : rows20.map Row.selected=choices (candidates 20) ∅ := by decide +kernel
theorem checked20 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 20))
  (choices (candidates 20) ∅) witnesses20 := by
  rw [← selected20]
  apply checked_rows
  simp only [rows20,List.all_append,TwentyFiveUnit8Rows20Batch0.checked,Bool.true_and]
theorem selected21 : rows21.map Row.selected=choices (candidates 21) ∅ := by decide +kernel
theorem checked21 : List.Forall₂ (Checks catalogue (TwentyFiveUnit7Data.catalogue 21))
  (choices (candidates 21) ∅) witnesses21 := by
  rw [← selected21]
  apply checked_rows
  simp only [rows21,List.all_append,TwentyFiveUnit8Rows21Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit8Checked
