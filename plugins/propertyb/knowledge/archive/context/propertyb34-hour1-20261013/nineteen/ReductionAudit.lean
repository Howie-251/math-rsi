import Aris4Math.ThirtyFour.Reduction
namespace T34ReductionAudit
universe u
/-- The remaining obligation is explicit. This is an audited conditional
assembly, not a proof of the unsolved all-vertex target. -/
theorem original_statement_from_remaining
    (remaining : Aris4Math.ThirtyFour.RemainingGoal)
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (uniform : ∀ e ∈ E, e.card = 5) (bound : E.card ≤ 34) :
    ∃ c : V → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x = true).card ∧
      (e.filter fun x => c x = true).card ≤ 4 := by
  classical
  letI : Fintype V := Fintype.ofFinite V
  exact (Aris4Math.ThirtyFour.target_iff_remaining_goal.mpr remaining) V ⟨E,uniform⟩ bound
end T34ReductionAudit
#print Aris4Math.Target34
#print Aris4Math.ThirtyFour.RemainingGoal
#check @Aris4Math.ThirtyFour.SmallVertices.propertyB_of_vertices_le_eighteen
#check @Aris4Math.ThirtyFour.exists_nineteen_to_twenty_five_counterexample
#check @Aris4Math.ThirtyFour.target_iff_remaining_goal
#check @T34ReductionAudit.original_statement_from_remaining
#print axioms Aris4Math.ThirtyFour.SmallVertices.propertyB_of_vertices_le_eighteen
#print axioms Aris4Math.ThirtyFour.target_iff_remaining_goal
#print axioms T34ReductionAudit.original_statement_from_remaining
