import Aris4Math.ThirtyThree.Main

/-! Independent spelling of T33 for semantic and transitive-axiom inspection.
This module imports the actual proof; it does not supply a second independent proof. -/
namespace ReviewAudit33
universe u

/-- Arbitrary finite vertex types, arbitrary finite simple edge sets, exact five-uniformity,
and only the original edge bound. -/
theorem original_statement
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (five_uniform : ∀ e ∈ E, e.card = 5) (at_most_33 : E.card ≤ 33) :
    ∃ c : V → Bool, ∀ e ∈ E,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 := by
  classical
  letI : Fintype V := Fintype.ofFinite V
  exact Aris4Math.two_colorable_of_at_most_thirty_three V ⟨E,five_uniform⟩ at_most_33

/-- Literal two-color interpretation: every edge contains both a true-colored
vertex and a false-colored vertex. No balanced-color-class condition is imposed. -/
theorem both_colors_in_every_edge
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (five_uniform : ∀ e ∈ E, e.card = 5) (at_most_33 : E.card ≤ 33) :
    ∃ c : V → Bool, ∀ e ∈ E,
      (∃ x ∈ e, c x = true) ∧ (∃ y ∈ e, c y = false) := by
  classical
  obtain ⟨c,hc⟩ := original_statement V E five_uniform at_most_33
  refine ⟨c,?_⟩
  intro e he
  obtain ⟨lower,upper⟩ := hc e he
  obtain ⟨x,hx⟩ := Finset.card_pos.mp (show 0 < (e.filter fun z => c z = true).card by omega)
  have red := Finset.mem_filter.mp hx
  refine ⟨⟨x,red.1,red.2⟩,?_⟩
  have exists_other : ∃ y ∈ e, c y ≠ true := by
    by_contra hn
    push_neg at hn
    have all_red : (e.filter fun z => c z = true) = e := Finset.filter_eq_self.mpr hn
    rw [all_red,five_uniform e he] at upper
    omega
  obtain ⟨y,hy,other⟩ := exists_other
  refine ⟨y,hy,?_⟩
  cases cy : c y <;> simp_all

/-- Equivalent lower bound without project-specific hypergraph or Property B aliases. -/
theorem original_lower_bound
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (five_uniform : ∀ e ∈ E, e.card = 5)
    (no_coloring : ¬ ∃ c : V → Bool, ∀ e ∈ E,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4) : 34 ≤ E.card := by
  classical
  letI : Fintype V := Fintype.ofFinite V
  exact Aris4Math.non_propertyB_edges_ge_thirty_four V ⟨E,five_uniform⟩ no_coloring

end ReviewAudit33

#print Aris4Math.Simple5Hypergraph
#print Aris4Math.PropertyB
#print Aris4Math.Target33
#check @Aris4Math.ThirtyThree.twenty_three_propertyB
#check @Aris4Math.propertyB_of_at_most_thirty_three
#check @Aris4Math.two_colorable_of_at_most_thirty_three
#check @Aris4Math.non_propertyB_edges_ge_thirty_four
#check @ReviewAudit33.original_statement
#check @ReviewAudit33.both_colors_in_every_edge
#check @ReviewAudit33.original_lower_bound
#print axioms Aris4Math.ThirtyThree.twenty_three_propertyB
#print axioms Aris4Math.ThirtyThree.finite_goal
#print axioms Aris4Math.propertyB_of_at_most_thirty_three
#print axioms Aris4Math.two_colorable_of_at_most_thirty_three
#print axioms Aris4Math.non_propertyB_edges_ge_thirty_four
#print axioms ReviewAudit33.original_statement
#print axioms ReviewAudit33.both_colors_in_every_edge
#print axioms ReviewAudit33.original_lower_bound
