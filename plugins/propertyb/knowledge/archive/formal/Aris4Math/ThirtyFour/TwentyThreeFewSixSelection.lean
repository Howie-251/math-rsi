import Aris4Math.ThirtyFour.FiveVertexClusterBound
import Aris4Math.Structure
import Mathlib.Data.Fintype.Pi

/-! The analytic final step of the one-degree-six 23-point branch.
The three five-vertex graphs are checked in the kernel. Arbitrary three- and
four-point patterns are extended to actual five-point subsets before applying
the local classification. The classification of actual hypergraph traces is
an explicit caller obligation; this module does not claim that classification.
-/

namespace Aris4Math.ThirtyFour.TwentyThreeFewSixSelection

open FiveVertexClusterBound

/-- Shapes 0, 1, 2 are respectively 2K2+K1, K3+2K1 and K3+K2.
The labels are vertices, not edge multiplicities. -/
def residualGraph (shape : Fin 3) (i j : Fin 5) : Prop :=
  i ≠ j ∧
    if shape = 0 then
      (i < 2 ∧ j < 2) ∨ (2 ≤ i ∧ i < 4 ∧ 2 ≤ j ∧ j < 4)
    else
      (i < 3 ∧ j < 3) ∨ (shape = 2 ∧ 3 ≤ i ∧ 3 ≤ j)

instance (shape : Fin 3) : DecidableRel (residualGraph shape) :=
  fun i j => by unfold residualGraph; infer_instance

set_option synthInstance.maxSize 1000 in
theorem residual_no_path : ∀ shape, ¬ HasInducedP3 (residualGraph shape) := by
  unfold HasInducedP3
  decide +kernel

set_option synthInstance.maxSize 1000 in
theorem residual_no_clique : ∀ shape, ¬ HasFour (residualGraph shape) := by
  unfold HasFour Function.Injective
  decide +kernel

set_option synthInstance.maxSize 1000 in
theorem residual_no_independent :
    ∀ shape, ¬ HasFour (fun i j => ¬ residualGraph shape i j) := by
  unfold HasFour Function.Injective
  decide +kernel

/-- A local classifier need only supply the graph shape and its relabeling.
In particular, it need not produce global connected components. -/
def IsResidual (R : Fin 5 → Fin 5 → Prop) : Prop :=
  ∃ shape : Fin 3, ∃ σ : Equiv.Perm (Fin 5),
    ∀ i j, R i j ↔ residualGraph shape (σ i) (σ j)

theorem no_path_of_residual {R : Fin 5 → Fin 5 → Prop}
    (residual : IsResidual R) : ¬ HasInducedP3 R := by
  obtain ⟨shape, σ, same⟩ := residual
  rintro ⟨a, b, c, ab, ac, bc, rab, rbc, rac⟩
  exact residual_no_path shape ⟨σ a, σ b, σ c, σ.injective.ne ab,
    σ.injective.ne ac, σ.injective.ne bc, (same a b).mp rab,
    (same b c).mp rbc, fun h => rac ((same a c).mpr h)⟩

theorem no_clique_of_residual {R : Fin 5 → Fin 5 → Prop}
    (residual : IsResidual R) : ¬ HasFour R := by
  obtain ⟨shape, σ, same⟩ := residual
  rintro ⟨f, inj, pairs⟩
  exact residual_no_clique shape ⟨σ ∘ f, σ.injective.comp inj,
    fun i j ij => (same (f i) (f j)).mp (pairs i j ij)⟩

theorem no_independent_of_residual {R : Fin 5 → Fin 5 → Prop}
    (residual : IsResidual R) : ¬ HasFour (fun i j => ¬ R i j) := by
  obtain ⟨shape, σ, same⟩ := residual
  rintro ⟨f, inj, pairs⟩
  exact residual_no_independent shape ⟨σ ∘ f, σ.injective.comp inj,
    fun i j ij h => pairs i j ij ((same (f i) (f j)).mpr h)⟩

section ActualFiveSets

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Enlarge an actual subset, then label its five distinct vertices. -/
theorem exists_five_containing (many : 5 ≤ Fintype.card V)
    (S : Finset V) (small : S.card ≤ 5) :
    ∃ f : Fin 5 ↪ V, ∀ x ∈ S, ∃ i, f i = x := by
  classical
  obtain ⟨T, sub, _, card⟩ := Finset.exists_subsuperset_card_eq
    (Finset.subset_univ S) small (by simpa using many)
  let e : ↥T ≃ Fin 5 := Fintype.equivFinOfCardEq (by simpa using card)
  let f : Fin 5 ↪ V :=
    ⟨fun i => (e.symm i).val, Subtype.val_injective.comp e.symm.injective⟩
  refine ⟨f, ?_⟩
  intro x hx
  exact ⟨e ⟨x, sub hx⟩, by simp [f]⟩

/-- Pull a three-vertex induced path into one actual five-set. -/
theorem no_path_of_every_five (R : V → V → Prop)
    (many : 5 ≤ Fintype.card V)
    (fiveRules : ∀ f : Fin 5 ↪ V,
      ¬ HasInducedP3 (fun i j => R (f i) (f j))) : ¬ HasInducedP3 R := by
  rintro ⟨a, b, c, ab, ac, bc, rab, rbc, rac⟩
  obtain ⟨f, covers⟩ := exists_five_containing many {a, b, c}
    (by
      have first := Finset.card_insert_le a ({b, c} : Finset V)
      have second := Finset.card_insert_le b ({c} : Finset V)
      simp only [Finset.card_singleton] at second
      omega)
  obtain ⟨ia, ea⟩ := covers a (by simp)
  obtain ⟨ib, eb⟩ := covers b (by simp)
  obtain ⟨ic, ec⟩ := covers c (by simp)
  apply fiveRules f
  refine ⟨ia, ib, ic, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · rintro rfl
    exact ab (ea.symm.trans eb)
  · rintro rfl
    exact ac (ea.symm.trans ec)
  · rintro rfl
    exact bc (eb.symm.trans ec)
  · simpa only [ea, eb] using rab
  · simpa only [eb, ec] using rbc
  · simpa only [ea, ec] using rac

/-- The same extension transports any four-point pairwise relation.
It is used once for cliques and once for independent sets. -/
theorem no_four_of_every_five (P : V → V → Prop)
    (many : 5 ≤ Fintype.card V)
    (fiveRules : ∀ f : Fin 5 ↪ V, ¬ HasFour (fun i j => P (f i) (f j))) :
    ¬ HasFour P := by
  classical
  rintro ⟨g, inj, pairs⟩
  have small : ((Finset.univ : Finset (Fin 4)).image g).card ≤ 5 := by
    have bound := Finset.card_image_le (s := (Finset.univ : Finset (Fin 4))) (f := g)
    simp only [Finset.card_univ, Fintype.card_fin] at bound
    omega
  obtain ⟨f, covers⟩ := exists_five_containing many (Finset.univ.image g) small
  have preimages : ∀ i : Fin 4, ∃ j : Fin 5, f j = g i := by
    intro i
    exact covers (g i) (Finset.mem_image.mpr ⟨i, Finset.mem_univ i, rfl⟩)
  choose h hh using preimages
  apply fiveRules f
  refine ⟨h, ?_, ?_⟩
  · intro i j eq
    apply inj
    rw [← hh i, ← hh j, eq]
  · intro i j ij
    simpa only [hh] using pairs i j ij

/-- A classifier for every actual five-set implies the analytic nine-vertex
bound. No enumeration of graphs on the ambient vertex type occurs here. -/
theorem card_le_nine_of_every_five (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ a b, R a b → R b a) (irreflexive : ∀ a, ¬ R a a)
    (fiveRules : ∀ f : Fin 5 ↪ V, IsResidual (fun i j => R (f i) (f j))) :
    Fintype.card V ≤ 9 := by
  by_cases many : 5 ≤ Fintype.card V
  · exact card_le_nine R symmetric irreflexive
      (no_path_of_every_five R many (fun f => no_path_of_residual (fiveRules f)))
      (no_four_of_every_five R many (fun f => no_clique_of_residual (fiveRules f)))
      (no_four_of_every_five (fun a b => ¬ R a b) many
        (fun f => no_independent_of_residual (fiveRules f)))
  · omega

end ActualFiveSets

section ActualHypergraph

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The nonunit graph is computed from actual edge incidences. The diagonal
is excluded explicitly, so no degree hypothesis is needed for irreflexivity. -/
def nonunit (H : Simple5Hypergraph V) (x y : V) : Prop :=
  x ≠ y ∧ H.codegree x y ≠ 1

instance (H : Simple5Hypergraph V) : DecidableRel (nonunit H) :=
  fun x y => by unfold nonunit; infer_instance

/-- An actual-H classification is assumed only under noncolorability.
The remaining obligation is to derive this local residual alternative from
the real trace counts and their strict coloring certificates. -/
theorem propertyB_of_five_residuals (H : Simple5Hypergraph V) (U : Finset V)
    (many : 10 ≤ U.card)
    (classify : ¬ PropertyB H → ∀ f : Fin 5 ↪ V, (∀ i, f i ∈ U) →
      IsResidual (fun i j => nonunit H (f i) (f j))) : PropertyB H := by
  classical
  by_contra notB
  let R : ↥U → ↥U → Prop := fun x y => nonunit H x.val y.val
  have symmetric : ∀ x y, R x y → R y x := by
    intro x y h
    exact ⟨h.1.symm, by simpa only [H.codegree_comm y.val x.val] using h.2⟩
  have irreflexive : ∀ x, ¬ R x x := by
    intro x h
    exact h.1 rfl
  have fiveRules : ∀ f : Fin 5 ↪ ↥U, IsResidual (fun i j => R (f i) (f j)) := by
    intro f
    let g : Fin 5 ↪ V := ⟨fun i => (f i).val, Subtype.val_injective.comp f.injective⟩
    exact classify notB g (fun i => (f i).property)
  have bound := card_le_nine_of_every_five R symmetric irreflexive fiveRules
  have small : U.card ≤ 9 := by simpa using bound
  omega

end ActualHypergraph

end Aris4Math.ThirtyFour.TwentyThreeFewSixSelection

#print axioms Aris4Math.ThirtyFour.TwentyThreeFewSixSelection.card_le_nine_of_every_five
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewSixSelection.propertyB_of_five_residuals
