import Aris4Math.General.Structure.Clique
import Mathlib.Combinatorics.SimpleGraph.Extremal.Turan
import Mathlib.Combinatorics.SimpleGraph.DegreeSum
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-! Turán's bound for the actual ordered single-intersection count. -/
namespace Aris4Math.General.RS

universe u

noncomputable instance singleGraphDecidableRel {V : Type u} (E : Finset (Finset V)) :
    DecidableRel (singleGraph E).Adj := Classical.decRel _

/-- Each member of the original ordered-pair finset is precisely a dart of the
single-intersection graph on the original edges. -/
noncomputable def singlePairsDartEquiv {V : Type u} (E : Finset (Finset V)) :
    ↥(singlePairs E) ≃ (singleGraph E).Dart := by
  classical
  refine {
    toFun := fun p => ?_
    invFun := fun d => ?_
    left_inv := ?_
    right_inv := ?_ }
  · have hp := p.property
    simp only [singlePairs, Finset.mem_filter, Finset.mem_product] at hp
    exact ⟨(⟨p.val.1, hp.1.1⟩, ⟨p.val.2, hp.1.2⟩),
      ⟨fun h => hp.2.1 (congrArg Subtype.val h), hp.2.2⟩⟩
  · exact ⟨(d.fst.val, d.snd.val), by
      simp only [singlePairs, Finset.mem_filter, Finset.mem_product]
      exact ⟨⟨d.fst.property, d.snd.property⟩,
        ⟨fun h => d.adj.1 (Subtype.ext h), d.adj.2⟩⟩⟩
  · intro p
    apply Subtype.ext
    rfl
  · intro d
    apply SimpleGraph.Dart.ext
    apply Prod.ext <;> apply Subtype.ext <;> rfl

/-- The RS count is an oriented count, hence twice the number of graph edges. -/
theorem gamma_eq_twice_singleGraph_edges {V : Type u} (E : Finset (Finset V)) :
    gamma E = 2 * (singleGraph E).edgeFinset.card := by
  classical
  calc
    gamma E = Fintype.card ↥(singlePairs E) := by simp [gamma]
    _ = Fintype.card (singleGraph E).Dart := Fintype.card_congr (singlePairsDartEquiv E)
    _ = 2 * (singleGraph E).edgeFinset.card :=
      (singleGraph E).dart_card_eq_twice_card_edges

/-- A finite-clique cardinality bound supplies the standard forbidden-clique
interface used by Turán's theorem. -/
theorem singleGraph_cliqueFree_of_card_le {V : Type u} (E : Finset (Finset V))
    (r : ℕ)
    (hcl : ∀ s : Finset {e : Finset V // e ∈ E},
      (singleGraph E).IsClique (s : Set _) → s.card ≤ r) :
    (singleGraph E).CliqueFree (r + 1) := by
  intro s hs
  have hcard := hcl s hs.isClique
  have heq := hs.card_eq
  omega

/-- The standard Turán estimate, translated to the ordered RS count of the
same arbitrary original edge family. -/
theorem singleGraph_gamma_bound {V : Type u} (E : Finset (Finset V))
    {r : ℕ} (hr : 1 ≤ r) (hcf : (singleGraph E).CliqueFree (r + 1)) :
    (gamma E : ℝ) ≤ (1 - 1 / (r : ℝ)) * (E.card : ℝ) ^ 2 := by
  classical
  have hc : (singleGraph E).edgeFinset.card ≤
      (SimpleGraph.turanGraph E.card r).edgeFinset.card := by
    simpa only [SimpleGraph.card_edgeFinset_turanGraph, Fintype.card_coe] using
      hcf.card_edgeFinset_le
  have hn : r * gamma E ≤ (r - 1) * E.card ^ 2 := by
    rw [gamma_eq_twice_singleGraph_edges]
    calc
      r * (2 * (singleGraph E).edgeFinset.card) =
          (2 * r) * (singleGraph E).edgeFinset.card := by ac_rfl
      _ ≤ (2 * r) * (SimpleGraph.turanGraph E.card r).edgeFinset.card :=
        Nat.mul_le_mul_left _ hc
      _ ≤ (r - 1) * E.card ^ 2 := SimpleGraph.mul_card_edgeFinset_turanGraph_le
  have hreal : (r : ℝ) * (gamma E : ℝ) ≤ ((r : ℝ) - 1) * (E.card : ℝ) ^ 2 := by
    exact_mod_cast hn
  have hrpos : (0 : ℝ) < (r : ℝ) := by exact_mod_cast hr
  rw [one_sub_div hrpos.ne', div_mul_eq_mul_div, le_div_iff₀ hrpos]
  nlinarith

/-- Fully assembled structural bound for a finite uniform edge family.  The
clique premise is supplied by the public-point dichotomy inside the proof. -/
theorem gamma_le_cliqueBudget {V : Type u} [Fintype V]
    (E : Finset (Finset V)) {k : ℕ} (hU : Uniform E k) (hk : 2 ≤ k) :
    (gamma E : ℝ) ≤
      (1 - 1 / (cliqueBudget k (Fintype.card V) : ℝ)) * (E.card : ℝ) ^ 2 := by
  classical
  have hr : 1 ≤ cliqueBudget k (Fintype.card V) := by
    exact (by omega : 1 ≤ k * k - k + 1).trans (le_max_left _ _)
  apply singleGraph_gamma_bound E hr
  apply singleGraph_cliqueFree_of_card_le
  exact singleGraph_isClique_card_le_cliqueBudget hU hk

end Aris4Math.General.RS
