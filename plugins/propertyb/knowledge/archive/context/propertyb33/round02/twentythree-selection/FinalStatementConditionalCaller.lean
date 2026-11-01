import Aris4Math.ThirtyThree.Assembly

/-! Independent spelling of T33 for semantic and transitive-axiom inspection.
This module imports the actual proof; it does not supply a second independent proof. -/
namespace ReviewAudit33
universe u
variable (target : Aris4Math.Target33.{u})
include target

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
  exact target V ⟨E,five_uniform⟩ at_most_33

/-- Literal two-color interpretation: every edge contains both a true-colored
vertex and a false-colored vertex. No balanced-color-class condition is imposed. -/
theorem both_colors_in_every_edge
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (five_uniform : ∀ e ∈ E, e.card = 5) (at_most_33 : E.card ≤ 33) :
    ∃ c : V → Bool, ∀ e ∈ E,
      (∃ x ∈ e, c x = true) ∧ (∃ y ∈ e, c y = false) := by
  classical
  obtain ⟨c,hc⟩ := original_statement target V E five_uniform at_most_33
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
  by_contra hn
  exact no_coloring (target V ⟨E,five_uniform⟩ (by change E.card ≤ 33; omega))

end ReviewAudit33


namespace Aris4Math.ThirtyThree
universe u
example (branch23 : ∀ H : Simple5Hypergraph (Fin 23), H.PairCovering →
    H.edges.card = 33 → PropertyB H) : Target33.{u} :=
  target_of_remaining_goal (fun H edges33 cover => branch23 H cover edges33)
end Aris4Math.ThirtyThree
