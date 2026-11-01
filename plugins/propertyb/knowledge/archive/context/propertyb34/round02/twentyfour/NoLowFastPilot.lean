import Aris4Math.ThirtyFour.TwentyFourNoLowCoverageData
namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
open TwentyFourNoLowSixData
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def MatchedAt (b : Bool) (values : List ℕ) (selected : Case×Perm) : Prop :=
  (∀T,T.card≤2→low b (T.map (perm selected.2).toEmbedding)=upper selected.1 T) ∧
  (∀T,3≤T.card→vector values (T.map (perm selected.2).toEmbedding)=μ selected.1 T)
instance (b : Bool) (values : List ℕ) (selected : Case×Perm) : Decidable (MatchedAt b values selected) := by unfold MatchedAt;infer_instance
def values0 : List ℕ := [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
theorem choice0 : choose true values0=(39,60) := by decide +kernel
theorem fixed0 : MatchedAt true values0 (39,60) := by decide +kernel
theorem original0 : Matched true values0 := by unfold Matched;rw [choice0];exact fixed0
def values1 : List ℕ := [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
theorem choice1 : choose true values1=(39,120) := by decide +kernel
theorem fixed1 : MatchedAt true values1 (39,120) := by decide +kernel
theorem original1 : Matched true values1 := by unfold Matched;rw [choice1];exact fixed1
def values2 : List ℕ := [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
theorem choice2 : choose true values2=(39,0) := by decide +kernel
theorem fixed2 : MatchedAt true values2 (39,0) := by decide +kernel
theorem original2 : Matched true values2 := by unfold Matched;rw [choice2];exact fixed2
def values3 : List ℕ := [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
theorem choice3 : choose true values3=(20,1) := by decide +kernel
theorem fixed3 : MatchedAt true values3 (20,1) := by decide +kernel
theorem original3 : Matched true values3 := by unfold Matched;rw [choice3];exact fixed3
def values4 : List ℕ := [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
theorem choice4 : choose true values4=(20,0) := by decide +kernel
theorem fixed4 : MatchedAt true values4 (20,0) := by decide +kernel
theorem original4 : Matched true values4 := by unfold Matched;rw [choice4];exact fixed4
end Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
