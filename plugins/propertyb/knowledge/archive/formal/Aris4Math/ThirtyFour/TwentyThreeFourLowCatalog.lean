import Aris4Math.ThirtyThree.TwentyThreeFourLowActual

/-! The 34-edge four-low inventory reuses the already kernel-checked
33-edge catalogue. Every nonempty trace is identical; only the empty trace
increases by one. The actual-H caller still uses H.edges.card = 34. -/
namespace Aris4Math.ThirtyFour.TwentyThreeFourLowCatalog
open Aris4Math.ThirtyThree
open QuadProfiles (first second highLabels)
open TwentyThreeFourLowCatalog (co high highBudget)

def counts (k : Fin 50) (T : Finset (Fin 4)) : ℕ :=
  ThirtyThree.TwentyThreeFourLowCatalog.counts k T + if T=∅ then 1 else 0

/-- Positive empty count prevents truncated subtraction at the old edge budget. -/
theorem recovered_succ (m : ℕ) (degrees : Fin 4 → ℕ) (co : Fin 6 → ℕ)
    (high : Fin 5 → ℕ)
    (positive : 0 < QuadProfiles.recovered m degrees co high ∅) (T : Finset (Fin 4)) :
    QuadProfiles.recovered (m+1) degrees co high T =
      QuadProfiles.recovered m degrees co high T + if T=∅ then 1 else 0 := by
  by_cases empty : T=∅
  · subst T
    simp only [QuadProfiles.recovered, ↓reduceIte, Nat.sub_sub] at positive ⊢
    omega
  · simp only [QuadProfiles.recovered, if_neg empty, Nat.add_zero]

private theorem old_empty_positive : ∀ k : Fin 50,
    0 < ThirtyThree.TwentyThreeFourLowCatalog.counts k ∅ := by decide +kernel

/-- Reuse all 464 labelled inputs and their relabelings without enumerating
a second classification domain. -/
theorem classify (r : Fin 56) (a b c d : Fin 3) (q : Fin 2)
    (budget : highBudget r a b c d q) :
    ∃ k : Fin 50, ∃ σ : Fin 4 ≃ Fin 4, ∀ T,
      QuadProfiles.recovered 34 (fun _ => 6) (co r) (high a b c d q) (T.image σ) =
        counts k T := by
  obtain ⟨k, σ, hk⟩ := ThirtyThree.TwentyThreeFourLowCatalog.classify r a b c d q budget
  have positive : 0 < QuadProfiles.recovered 33 (fun _ => 6) (co r)
      (high a b c d q) ∅ := by
    have empty := hk ∅
    simp only [Finset.image_empty] at empty
    rw [empty]
    exact old_empty_positive k
  refine ⟨k, σ, ?_⟩
  intro T
  rw [show (34 : ℕ)=33+1 from rfl, recovered_succ 33 _ _ _ positive, hk T]
  simp only [counts, Finset.image_eq_empty]

theorem actual_representative (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges34 : H.edges.card = 34)
    (vertices : Fin 4 ↪ Fin 23) (degrees : ∀ i, H.degree (vertices i) = 6) :
    ∃ k : Fin 50, ∃ w : Fin 4 ↪ Fin 23,
      (∀ i, H.degree (w i) = 6) ∧
      (∀ T, QuadProfiles.count H w T = counts k T) := by
  obtain ⟨r,pairs⟩ := TwentyThreeFourLowActual.actual_pair_values H cover vertices degrees
  have bounds := TwentyThreeFourLowStructure.actual_high_bounds H cover vertices degrees
  let a : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 0),bounds.1 0⟩
  let b : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 1),bounds.1 1⟩
  let c : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 2),bounds.1 2⟩
  let d : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 3),bounds.1 3⟩
  let q : Fin 2 := ⟨QuadProfiles.count H vertices (highLabels 4),bounds.2⟩
  have actual : ∀ i, QuadProfiles.count H vertices (highLabels i) = high a b c d q i := by
    intro i
    fin_cases i <;> rfl
  obtain ⟨k,σ,hk⟩ := classify r a b c d q
    (TwentyThreeFourLowActual.actual_high_budget H vertices r pairs a b c d q actual)
  refine ⟨k,σ.toEmbedding.trans vertices,(fun i => degrees (σ i)),?_⟩
  intro T
  rw [TwentyThreeFourLowActual.count_relabel,QuadProfiles.actual_recovered,edges34]
  rw [show (fun i => H.degree (vertices i)) = (fun _ => 6) from funext degrees]
  rw [show (fun i => H.codegree (vertices (first i)) (vertices (second i))) = co r from funext pairs]
  rw [show (fun i => QuadProfiles.count H vertices (highLabels i)) = high a b c d q from funext actual]
  exact hk T

theorem actual_representative_perm (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges34 : H.edges.card = 34)
    (vertices : Fin 4 ↪ Fin 23) (degrees : ∀ i, H.degree (vertices i) = 6) :
    ∃ k : Fin 50, ∃ σ : Equiv.Perm (Fin 4),
      ∀ T, QuadProfiles.count H (σ.toEmbedding.trans vertices) T = counts k T := by
  obtain ⟨r,pairs⟩ := TwentyThreeFourLowActual.actual_pair_values H cover vertices degrees
  have bounds := TwentyThreeFourLowStructure.actual_high_bounds H cover vertices degrees
  let a : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 0),bounds.1 0⟩
  let b : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 1),bounds.1 1⟩
  let c : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 2),bounds.1 2⟩
  let d : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 3),bounds.1 3⟩
  let q : Fin 2 := ⟨QuadProfiles.count H vertices (highLabels 4),bounds.2⟩
  have actual : ∀ i, QuadProfiles.count H vertices (highLabels i) = high a b c d q i := by
    intro i
    fin_cases i <;> rfl
  obtain ⟨k,σ,hk⟩ := classify r a b c d q
    (TwentyThreeFourLowActual.actual_high_budget H vertices r pairs a b c d q actual)
  refine ⟨k,σ,?_⟩
  intro T
  rw [TwentyThreeFourLowActual.count_relabel,QuadProfiles.actual_recovered,edges34]
  rw [show (fun i => H.degree (vertices i)) = (fun _ => 6) from funext degrees]
  rw [show (fun i => H.codegree (vertices (first i)) (vertices (second i))) = co r from funext pairs]
  rw [show (fun i => QuadProfiles.count H vertices (highLabels i)) = high a b c d q from funext actual]
  exact hk T

end Aris4Math.ThirtyFour.TwentyThreeFourLowCatalog
#print axioms Aris4Math.ThirtyFour.TwentyThreeFourLowCatalog.actual_representative
