import Aris4Math.ThirtyFour.Assembly
import Aris4Math.ThirtyFour.TwentyOneSevenMany
namespace T34TwentyOneSevenManyAudit
universe u
theorem original_branch (E : Finset (Finset (Fin 21)))
    (uniform : ∀e∈E,e.card=5) (size : E.card=34)
    (cover : ∀x y : Fin 21,x≠y→∃e∈E,x∈e ∧ y∈e)
    (many : 5≤((Finset.univ : Finset (Fin 21)).filter
      (fun x=>(E.filter fun e=>x∈e).card=7)).card) :
    ∃c : Fin 21→Bool,∀e∈E,
      1≤(e.filter fun x=>c x=true).card ∧ (e.filter fun x=>c x=true).card≤4 := by
  exact Aris4Math.ThirtyFour.TwentyOneSevenMany.propertyB_of_many_sevens
    ⟨E,uniform⟩ cover size many

theorem conditional_original
    (remaining : Aris4Math.ThirtyFour.Assembly.RemainingGoal)
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (uniform : ∀e∈E,e.card=5) (size : E.card≤34) :
    ∃c : V→Bool,∀e∈E,
      1≤(e.filter fun x=>c x=true).card ∧ (e.filter fun x=>c x=true).card≤4 := by
  classical
  letI : Fintype V:=Fintype.ofFinite V
  exact (Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal.mpr remaining) V ⟨E,uniform⟩ size
end T34TwentyOneSevenManyAudit
#print Aris4Math.ThirtyFour.TwentyOneSevenMany.propertyB_of_many_sevens
#print Aris4Math.ThirtyFour.Assembly.RemainingGoal
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenMany.propertyB_of_many_sevens
#print axioms Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal
#print axioms T34TwentyOneSevenManyAudit.original_branch
#print axioms T34TwentyOneSevenManyAudit.conditional_original
