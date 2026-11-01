import Aris4Math.ThirtyFour.Assembly
import Aris4Math.ThirtyFour.TwentyOneSevenOne
namespace T34TwentyOneSevenOneAudit
universe u
theorem original_branch (E : Finset (Finset (Fin 21)))
    (uniform : ∀ e ∈ E, e.card=5) (size : E.card=34)
    (cover : ∀ x y : Fin 21, x≠y → ∃ e∈E, x∈e ∧ y∈e)
    (minimum : ∀x : Fin 21,7≤(E.filter fun e=>x∈e).card)
    (one : ((Finset.univ : Finset (Fin 21)).filter
      (fun x=>(E.filter fun e=>x∈e).card=7)).card=1) :
    ∃ c : Fin 21 → Bool, ∀ e∈E,
      1≤(e.filter fun x=>c x=true).card ∧ (e.filter fun x=>c x=true).card≤4 := by
  exact Aris4Math.ThirtyFour.TwentyOneSevenOne.propertyB_of_one_seven
    ⟨E,uniform⟩ cover size minimum one

theorem conditional_original
    (remaining : Aris4Math.ThirtyFour.Assembly.RemainingGoal)
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (uniform : ∀e∈E,e.card=5) (size : E.card≤34) :
    ∃c : V→Bool,∀e∈E,
      1≤(e.filter fun x=>c x=true).card ∧ (e.filter fun x=>c x=true).card≤4 := by
  classical
  letI : Fintype V:=Fintype.ofFinite V
  exact (Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal.mpr remaining) V ⟨E,uniform⟩ size
end T34TwentyOneSevenOneAudit
#print Aris4Math.ThirtyFour.TwentyOneSevenOne.propertyB_of_one_seven
#print Aris4Math.ThirtyFour.Assembly.RemainingGoal
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenOne.propertyB_of_one_seven
#print axioms Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal
#print axioms T34TwentyOneSevenOneAudit.original_branch
#print axioms T34TwentyOneSevenOneAudit.conditional_original
