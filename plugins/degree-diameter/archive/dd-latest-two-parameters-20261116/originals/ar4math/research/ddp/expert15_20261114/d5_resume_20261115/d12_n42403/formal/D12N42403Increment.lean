import DegreeDiameter.Portfolio.SingleExtension
import Mathlib.Combinatorics.SimpleGraph.Finite

/-! The actual twelve pins and the exact single-vertex operation.
This is an explicitly CONDITIONAL increment theorem, not a closed theorem
about the actual old42402 graph. Its source D5 and R4-certificate premises
are printed in Audit.lean and must not be omitted in reporting. -/
namespace DegreeDiameter.D12N42403
open SimpleGraph
open DegreeDiameter.Portfolio
abbrev OldVertex := Fin 42402
def pins : Finset OldVertex :=
  {979, 4045, 4563, 5711, 6513, 7312, 8156, 15138, 21547, 29557, 37599, 41421}
def pinSet : Set OldVertex := (pins : Set OldVertex)
theorem pins_card : pins.card = 12 := by decide
theorem candidate_card : Fintype.card (Option OldVertex) = 42403 := by simp
def graph (source : SimpleGraph OldVertex) : SimpleGraph (Option OldVertex) :=
  singleVertexExtension source pinSet
theorem old_edges_exact (source : SimpleGraph OldVertex) (u v : OldVertex) :
    (graph source).Adj (some u) (some v) ↔ source.Adj u v := Iff.rfl
theorem new_edges_exact (source : SimpleGraph OldVertex) (v : OldVertex) :
    (graph source).Adj none (some v) ↔ v ∈ pins := Iff.rfl

theorem new_degree_exact (source : SimpleGraph OldVertex) :
    (graph source).degree none = 12 := by
  classical
  have h : (graph source).neighborFinset none = pins.image some := by
    ext v
    cases v <;> simp [SimpleGraph.mem_neighborFinset, graph,
      singleVertexExtension, pinSet]
  rw [SimpleGraph.degree, h, Finset.card_image_of_injective _ Option.some_injective]
  exact pins_card

theorem old_degree_exact (source : SimpleGraph OldVertex) (u : OldVertex) :
    (graph source).degree (some u) = source.degree u + if u ∈ pins then 1 else 0 := by
  classical
  have hi : (source.neighborFinset u).image some |>.card = source.degree u := by
    rw [Finset.card_image_of_injective _ Option.some_injective]
    rfl
  by_cases hu : u ∈ pins
  · have h : (graph source).neighborFinset (some u) =
        insert none ((source.neighborFinset u).image some) := by
      ext v
      cases v <;> simp [SimpleGraph.mem_neighborFinset, graph,
        singleVertexExtension, pinSet, hu]
    have hn : none ∉ (source.neighborFinset u).image some := by simp
    rw [SimpleGraph.degree, h, Finset.card_insert_of_notMem hn, hi]
    simp [hu]
  · have h : (graph source).neighborFinset (some u) =
        (source.neighborFinset u).image some := by
      ext v
      cases v <;> simp [SimpleGraph.mem_neighborFinset, graph,
        singleVertexExtension, pinSet, hu]
    rw [SimpleGraph.degree, h, hi]
    simp [hu]

theorem maximum_degree_at_most_twelve (source : SimpleGraph OldVertex)
    (hold : ∀ u, source.degree u ≤ 12)
    (hspare : ∀ u ∈ pins, source.degree u ≤ 11) :
    ∀ v, (graph source).degree v ≤ 12 := by
  intro v
  cases v with
  | none => exact new_degree_exact source ▸ Nat.le_refl 12
  | some u =>
    rw [old_degree_exact]
    by_cases hu : u ∈ pins
    · simpa [hu] using Nat.add_le_add_right (hspare u hu) 1
    · simpa [hu] using hold u

theorem conditional_diameter_at_most_five (source : SimpleGraph OldVertex)
    (hsource : DiameterAtMost source 5)
    (certificate : ParentDepthCertificate source pinSet 4) :
    DiameterAtMost (graph source) 5 :=
  singleVertexExtension_diameterAtMostFive_of_parentDepth source pinSet hsource certificate

end DegreeDiameter.D12N42403

#check DegreeDiameter.D12N42403.conditional_diameter_at_most_five
#print axioms DegreeDiameter.D12N42403.pins_card
#print axioms DegreeDiameter.D12N42403.new_degree_exact
#print axioms DegreeDiameter.D12N42403.old_degree_exact
#print axioms DegreeDiameter.D12N42403.maximum_degree_at_most_twelve
#print axioms DegreeDiameter.D12N42403.conditional_diameter_at_most_five
