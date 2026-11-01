import Aris4Math.ThirtyFour.TwentyThreeFewSixSelection
import Aris4Math.ThirtyThree.TwentyThreeSelection

/-! Actual common-unit seven-degree vertices for the one- and two-six
branches at 23 vertices and 34 edges. The incidence budget is reproved with
170 incidences; only edge-count-independent selection lemmas are reused.
-/

namespace Aris4Math.ThirtyFour.TwentyThreeLowUnitSelection

open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyThreeSelection
  (sevenVertices min_degree_six commonUnitSevens commonUnitSevens_budget
    commonUnitSevens_degrees commonUnitSevens_unit exists_indexed_subset)
open TwentyThreeFewSixSelection (IsResidual nonunit propertyB_of_five_residuals)

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The original 34 edges give 170 incidences, hence t+2r ≥ 14. -/
theorem six_seven_budget (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 34) (vertices : Fintype.card V = 23) :
    14 ≤ 2 * H.sixVertices.card + (sevenVertices H).card := by
  have each (x : V) : 8 ≤ H.degree x +
      (if H.degree x = 6 then 2 else 0) + (if H.degree x = 7 then 1 else 0) := by
    have minimum := min_degree_six H cover vertices x
    split_ifs <;> omega
  have total := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have sixsum : (∑ x : V, if H.degree x = 6 then 2 else 0) =
      2 * H.sixVertices.card := by
    rw [← Finset.sum_filter]
    simp [Simple5Hypergraph.sixVertices, Nat.mul_comm]
  have bound : 8 * Fintype.card V ≤ 170 + 2 * H.sixVertices.card +
      (sevenVertices H).card := by
    simpa only [Finset.sum_add_distrib, sixsum, H.sum_degrees, edges,
      Finset.sum_boole, Finset.sum_const, Finset.card_univ, nsmul_eq_mul,
      Simple5Hypergraph.sixVertices, sevenVertices, Nat.mul_comm] using total
  rw [vertices] at bound
  omega

/-- U consists of the actual seven-degree vertices that avoid all bad
partners of every actual six-degree vertex. -/
def unitSevens (H : Simple5Hypergraph V) : Finset V :=
  commonUnitSevens H H.sixVertices

theorem unitSevens_degree (H : Simple5Hypergraph V) {y : V}
    (hy : y ∈ unitSevens H) : H.degree y = 7 :=
  commonUnitSevens_degrees H H.sixVertices hy

theorem unitSevens_unit (H : Simple5Hypergraph V) (cover : H.PairCovering)
    {x y : V} (dx : H.degree x = 6) (hy : y ∈ unitSevens H) :
    x ≠ y ∧ H.codegree x y = 1 := by
  apply commonUnitSevens_unit H cover H.sixVertices
    (fun z hz => (Finset.mem_filter.mp hz).2)
  · exact Finset.mem_filter.mpr ⟨Finset.mem_univ x, dx⟩
  · exact hy

/-- Removing at most two exceptional neighbors for each low vertex gives
the actual bound |U|+4r ≥ 14. -/
theorem unitSevens_budget (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges : H.edges.card = 34) (vertices : Fintype.card V = 23) :
    14 ≤ (unitSevens H).card + 4 * H.sixVertices.card := by
  have degreeBudget := six_seven_budget H cover edges vertices
  have deletionBudget := commonUnitSevens_budget H cover vertices H.sixVertices
    (fun x hx => (Finset.mem_filter.mp hx).2)
  change (sevenVertices H).card ≤ (unitSevens H).card +
    2 * H.sixVertices.card at deletionBudget
  omega

theorem unitSevens_card_ge_ten_of_one (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges : H.edges.card = 34)
    (vertices : Fintype.card V = 23) (one : H.sixVertices.card = 1) :
    10 ≤ (unitSevens H).card := by
  have budget := unitSevens_budget H cover edges vertices
  omega

theorem unitSevens_card_ge_six_of_two (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges : H.edges.card = 34)
    (vertices : Fintype.card V = 23) (two : H.sixVertices.card = 2) :
    6 ≤ (unitSevens H).card := by
  have budget := unitSevens_budget H cover edges vertices
  omega

/-- Five genuine high locks, all unit to every low vertex of the same H.
This is a selection result; it does not assert a trace classification. -/
theorem exists_five_unit_sevens (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges : H.edges.card = 34)
    (vertices : Fintype.card V = 23)
    (few : H.sixVertices.card = 1 ∨ H.sixVertices.card = 2) :
    ∃ f : Fin 5 ↪ V, (∀ i, f i ∈ unitSevens H) ∧
      (∀ i, H.degree (f i) = 7) ∧
      (∀ x, H.degree x = 6 → ∀ i, x ≠ f i ∧ H.codegree x (f i) = 1) := by
  have budget := unitSevens_budget H cover edges vertices
  have many : 5 ≤ (unitSevens H).card := by rcases few with h | h <;> omega
  obtain ⟨f, inj, inside⟩ := exists_indexed_subset (unitSevens H) many
  refine ⟨⟨f, inj⟩, inside, ?_, ?_⟩
  · intro i
    exact unitSevens_degree H (inside i)
  · intro x dx i
    exact unitSevens_unit H cover dx (inside i)

/-- Every actual five-set in U is available to the local classifier with
its required degrees and low-high unit codegrees already proved. Only the
real trace classification remains as a premise of this conditional branch. -/
theorem one_six_propertyB_of_residual_classification (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges : H.edges.card = 34)
    (vertices : Fintype.card V = 23) (one : H.sixVertices.card = 1)
    (classify : ¬ PropertyB H → ∀ f : Fin 5 ↪ V,
      (∀ i, H.degree (f i) = 7) →
      (∀ x, H.degree x = 6 → ∀ i, H.codegree x (f i) = 1) →
      IsResidual (fun i j => nonunit H (f i) (f j))) : PropertyB H := by
  apply propertyB_of_five_residuals H (unitSevens H)
    (unitSevens_card_ge_ten_of_one H cover edges vertices one)
  intro notB f inside
  apply classify notB f
  · intro i
    exact unitSevens_degree H (inside i)
  · intro x dx i
    exact (unitSevens_unit H cover dx (inside i)).2

end Aris4Math.ThirtyFour.TwentyThreeLowUnitSelection

#print axioms Aris4Math.ThirtyFour.TwentyThreeLowUnitSelection.unitSevens_card_ge_ten_of_one
#print axioms Aris4Math.ThirtyFour.TwentyThreeLowUnitSelection.unitSevens_card_ge_six_of_two
#print axioms Aris4Math.ThirtyFour.TwentyThreeLowUnitSelection.exists_five_unit_sevens
#print axioms Aris4Math.ThirtyFour.TwentyThreeLowUnitSelection.one_six_propertyB_of_residual_classification
