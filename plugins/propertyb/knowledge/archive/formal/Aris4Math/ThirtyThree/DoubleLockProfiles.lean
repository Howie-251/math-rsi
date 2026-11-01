import Aris4Math.DoubleTripleLockProfiles

/-! Realization of the actual thirty-three-edge double-lock profiles.
Old position and class geometry are reused; only the actual total changes. -/

namespace Aris4Math.ThirtyThree.DoubleLockProfiles

open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles

def twoProfile (v d e : ℕ) (centers : List ℕ) : Numeric.Profile :=
  ⟨v, [11, 12], [⟨[], 34-d-e⟩, ⟨[11], d-1⟩, ⟨[12], e-1⟩, ⟨[11,12], 1⟩], none, centers⟩

theorem two_counts {v : ℕ} (H : Simple5Hypergraph (Fin v)) (edges33 : H.edges.card = 33)
    (x y : Fin v) (codegree1 : H.codegree x y = 1) :
    multiplicity H.edges (twoClass x y) [] = 34 - H.degree x - H.degree y ∧
    multiplicity H.edges (twoClass x y) [11] = H.degree x - 1 ∧
    multiplicity H.edges (twoClass x y) [12] = H.degree y - 1 ∧
    multiplicity H.edges (twoClass x y) [11,12] = 1 := by
  have hx := Finset.filter_card_add_filter_neg_card_eq_card
    (s := H.edges.filter (fun A => x ∈ A)) (fun A => y ∈ A)
  have hy := Finset.filter_card_add_filter_neg_card_eq_card
    (s := H.edges.filter (fun A => y ∈ A)) (fun A => x ∈ A)
  simp only [Finset.filter_filter] at hx hy
  have hpart := four_partition H.edges (fun A => x ∈ A) (fun A => y ∈ A)
  change (H.edges.filter (fun A => x ∈ A ∧ y ∈ A)).card = 1 at codegree1
  have hy1 : H.edges.filter (fun A => y ∈ A ∧ x ∈ A) = H.edges.filter (fun A => x ∈ A ∧ y ∈ A) := by
    ext A; simp [and_comm]
  have hy0 : H.edges.filter (fun A => y ∈ A ∧ x ∉ A) = H.edges.filter (fun A => x ∉ A ∧ y ∈ A) := by
    ext A; simp [and_comm]
  rw [hy1, hy0] at hy
  change _ + _ = H.degree x at hx
  change _ + _ = H.degree y at hy
  rw [edges33] at hpart
  have h0 := class_fiber H x y 0
  have h1 := class_fiber H x y 1
  have h2 := class_fiber H x y 2
  have h3 := class_fiber H x y 3
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, decide_eq_true_eq] at h0 h1 h2 h3
  rw [h0, h1, h2, h3]
  omega

/-- Any actual codegree-one pair realizes its full four-row table. Validity
of the chosen numeric data is checked separately, rather than assumed of H. -/
theorem realizes_two_profile {v : ℕ} (H : Simple5Hypergraph (Fin v))
    (edges33 : H.edges.card = 33) (hv : 12 ≤ v)
    (x y : Fin v) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (centers : List ℕ)
    (valid : Numeric.validProfile (twoProfile v (H.degree x) (H.degree y) centers) 33) :
    RealizesProfile H (twoVertices x y hne) (twoPositions v hv)
      (twoProfile v (H.degree x) (H.degree y) centers) 33 := by
  refine ⟨rfl, valid, ?_, ?_⟩
  · have hu : (Finset.univ : Finset (Fin 2)) = {0,1} := by decide
    simp [twoProfile, hu, twoPositions]
  · constructor
    · simp [twoProfile]
    · intro A hA
      simpa only [two_type, twoProfile, List.map_cons, List.map_nil] using two_class_mem x y A
    · have heq : positionType (twoVertices x y hne) (twoPositions v hv) = twoClass x y :=
        funext (two_type hv x y hne)
      rw [heq]
      intro t ht
      simp only [twoProfile, List.mem_cons, List.not_mem_nil, or_false] at ht
      have hc := two_counts H edges33 x y codegree1
      rcases ht with rfl | rfl | rfl | rfl
      · exact hc.1
      · exact hc.2.1
      · exact hc.2.2.1
      · exact hc.2.2.2


end Aris4Math.ThirtyThree.DoubleLockProfiles
