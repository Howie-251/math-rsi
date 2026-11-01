import Aris4Math.Main

/-! Entry point for human review of the original statement.
Run `lake env lean ReviewAudit.lean` in the `formal` directory.
This spells out the original target independently of its project aliases;
it uses the existing proof, rather than providing a second proof. -/

namespace ReviewAudit

universe u

theorem original_statement
    (V : Type u) [Finite V]
    (E : Finset (Finset V))
    (five_uniform : ∀ e ∈ E, e.card = 5)
    (at_most_32 : E.card ≤ 32) :
    ∃ c : V → Bool, ∀ e ∈ E,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 := by
  classical
  letI : Fintype V := Fintype.ofFinite V
  exact Aris4Math.two_colorable_of_at_most_thirty_two
    V ⟨E, five_uniform⟩ at_most_32

end ReviewAudit

#print Aris4Math.Simple5Hypergraph
#print Aris4Math.PropertyB
#print Aris4Math.Target
#check @Aris4Math.propertyB_of_at_most_thirty_two
#check @Aris4Math.two_colorable_of_at_most_thirty_two
#check @Aris4Math.non_propertyB_edges_ge_thirty_three
#check @ReviewAudit.original_statement
#print axioms Aris4Math.finite_goal
#print axioms Aris4Math.propertyB_of_at_most_thirty_two
#print axioms Aris4Math.two_colorable_of_at_most_thirty_two
#print axioms Aris4Math.non_propertyB_edges_ge_thirty_three
#print axioms ReviewAudit.original_statement
