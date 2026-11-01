import Aris4Math.SmallLockProfiles
import Mathlib.Tactic.FinCases

/-! Actual two-lock profiles for the 22- and 23-vertex branches.
The separate TripleLockProfiles module handles the 6,7,7 alternative. -/

namespace Aris4Math.DoubleLockProfiles

open TypeCounting

def twoVertices {v : ℕ} (x y : Fin v) (hne : x ≠ y) : Fin 2 ↪ Fin v where
  toFun := ![x, y]
  inj' := by
    intro i j heq
    fin_cases i <;> fin_cases j <;> simp_all

def twoPositions (v : ℕ) (hv : 12 ≤ v) : Fin 2 ↪ Fin v where
  toFun i := ⟨i.val + 10, by omega⟩
  inj' := by
    intro i j heq
    apply Fin.ext
    have h := congrArg Fin.val heq
    dsimp at h
    omega

def twoProfile (v d e : ℕ) (centers : List ℕ) : Numeric.Profile :=
  ⟨v, [11, 12], [⟨[], 33-d-e⟩, ⟨[11], d-1⟩, ⟨[12], e-1⟩, ⟨[11,12], 1⟩], none, centers⟩

def twoClass {v : ℕ} (x y : Fin v) (A : Finset (Fin v)) : List ℕ :=
  if x ∈ A then (if y ∈ A then [11, 12] else [11]) else (if y ∈ A then [12] else [])

theorem two_type {v : ℕ} (hv : 12 ≤ v) (x y : Fin v) (hne : x ≠ y)
    (A : Finset (Fin v)) :
    positionType (twoVertices x y hne) (twoPositions v hv) A = twoClass x y A := by
  have hs : lockSignature (twoVertices x y hne) A =
      if x ∈ A then (if y ∈ A then {0,1} else {0}) else (if y ∈ A then {1} else ∅) := by
    ext i
    fin_cases i <;> by_cases hx : x ∈ A <;> by_cases hy : y ∈ A <;>
      simp [lockSignature, twoVertices, hx, hy]
  unfold positionType positionSignature
  rw [hs]
  have hsort : ({11,12} : Finset ℕ).sort (· ≤ ·) = [11,12] := by
    exact (List.toFinset_sort (· ≤ ·) (by decide : ([11,12] : List ℕ).Nodup)).mpr (by decide)
  by_cases hx : x ∈ A <;> by_cases hy : y ∈ A <;>
    simp [twoPositions, twoClass, hx, hy, hsort]

theorem two_class_mem {v : ℕ} (x y : Fin v) (A : Finset (Fin v)) :
    twoClass x y A ∈ [[], [11], [12], [11,12]] := by
  unfold twoClass
  split_ifs <;> simp

theorem class_fiber {v : ℕ} (H : Simple5Hypergraph (Fin v)) (x y : Fin v)
    (i : Fin 4) :
    multiplicity H.edges (twoClass x y) (![[], [11], [12], [11,12]] i) =
      (H.edges.filter (fun A =>
        ![decide (x ∉ A ∧ y ∉ A), decide (x ∈ A ∧ y ∉ A),
          decide (x ∉ A ∧ y ∈ A), decide (x ∈ A ∧ y ∈ A)] i = true)).card := by
  unfold multiplicity fiber
  congr 1
  ext A
  fin_cases i <;> by_cases hx : x ∈ A <;> by_cases hy : y ∈ A <;>
    simp [twoClass, hx, hy]

theorem four_partition {α : Type*} (F : Finset α) (P Q : α → Prop)
    [DecidablePred P] [DecidablePred Q] :
    (F.filter (fun a => P a ∧ Q a)).card +
    (F.filter (fun a => P a ∧ ¬Q a)).card +
    (F.filter (fun a => ¬P a ∧ Q a)).card +
    (F.filter (fun a => ¬P a ∧ ¬Q a)).card = F.card := by
  have hp := Finset.filter_card_add_filter_neg_card_eq_card (s := F) P
  have hq := Finset.filter_card_add_filter_neg_card_eq_card (s := F.filter P) Q
  have hqn := Finset.filter_card_add_filter_neg_card_eq_card (s := F.filter (fun a => ¬P a)) Q
  simp only [Finset.filter_filter] at hq hqn
  omega

theorem two_counts {v : ℕ} (H : Simple5Hypergraph (Fin v)) (edges32 : H.edges.card = 32)
    (x y : Fin v) (codegree1 : H.codegree x y = 1) :
    multiplicity H.edges (twoClass x y) [] = 33 - H.degree x - H.degree y ∧
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
  rw [edges32] at hpart
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
    (edges32 : H.edges.card = 32) (hv : 12 ≤ v)
    (x y : Fin v) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (centers : List ℕ)
    (valid : Numeric.validProfile (twoProfile v (H.degree x) (H.degree y) centers)) :
    RealizesProfile H (twoVertices x y hne) (twoPositions v hv)
      (twoProfile v (H.degree x) (H.degree y) centers) := by
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
      have hc := two_counts H edges32 x y codegree1
      rcases ht with rfl | rfl | rfl | rfl
      · exact hc.1
      · exact hc.2.1
      · exact hc.2.2.1
      · exact hc.2.2.2

theorem realizes_v22_66 (H : Simple5Hypergraph (Fin 22)) (edges32 : H.edges.card = 32)
    (x y : Fin 22) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 6) (dy : H.degree y = 6) :
    RealizesProfile H (twoVertices x y hne) (twoPositions 22 (by decide)) Numeric.v22_66 := by
  have valid : Numeric.validProfile (twoProfile 22 (H.degree x) (H.degree y) []) := by
    rw [dx, dy]
    exact Numeric.v22_66_valid
  have real := realizes_two_profile H edges32 (by decide) x y hne codegree1 [] valid
  simpa only [dx, dy] using real

theorem realizes_v22_67 (H : Simple5Hypergraph (Fin 22)) (edges32 : H.edges.card = 32)
    (x y : Fin 22) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 6) (dy : H.degree y = 7) :
    RealizesProfile H (twoVertices x y hne) (twoPositions 22 (by decide)) Numeric.v22_67 := by
  have valid : Numeric.validProfile (twoProfile 22 (H.degree x) (H.degree y) [12]) := by
    rw [dx, dy]
    exact Numeric.v22_67_valid
  have real := realizes_two_profile H edges32 (by decide) x y hne codegree1 [12] valid
  simpa only [dx, dy] using real

theorem realizes_v22_77 (H : Simple5Hypergraph (Fin 22)) (edges32 : H.edges.card = 32)
    (x y : Fin 22) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 7) (dy : H.degree y = 7) :
    RealizesProfile H (twoVertices x y hne) (twoPositions 22 (by decide)) Numeric.v22_77 := by
  have valid : Numeric.validProfile (twoProfile 22 (H.degree x) (H.degree y) [11,12]) := by
    rw [dx, dy]
    exact Numeric.v22_77_valid
  have real := realizes_two_profile H edges32 (by decide) x y hne codegree1 [11,12] valid
  simpa only [dx, dy] using real

theorem realizes_v23_66 (H : Simple5Hypergraph (Fin 23)) (edges32 : H.edges.card = 32)
    (x y : Fin 23) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 6) (dy : H.degree y = 6) :
    RealizesProfile H (twoVertices x y hne) (twoPositions 23 (by decide)) Numeric.v23_66 := by
  have valid : Numeric.validProfile (twoProfile 23 (H.degree x) (H.degree y) [11,12]) := by
    rw [dx, dy]
    exact Numeric.v23_66_valid
  have real := realizes_two_profile H edges32 (by decide) x y hne codegree1 [11,12] valid
  simpa only [dx, dy] using real

/-- The actual low-degree alternative produces one of the three exact tables. -/
theorem exists_realized_profile22 (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
    ∃ vertices : Fin 2 ↪ Fin 22,
      RealizesProfile H vertices (twoPositions 22 (by decide)) Numeric.v22_66 ∨
      RealizesProfile H vertices (twoPositions 22 (by decide)) Numeric.v22_67 ∨
      RealizesProfile H vertices (twoPositions 22 (by decide)) Numeric.v22_77 := by
  obtain ⟨x, y, hne, hc, hdegrees⟩ := H.exists_two_locks_of_twenty_two cover edges32 (by simp)
  refine ⟨twoVertices x y hne, ?_⟩
  rcases hdegrees with ⟨dx,dy⟩ | ⟨dx,dy⟩ | ⟨dx,dy⟩
  · exact Or.inl (realizes_v22_66 H edges32 x y hne hc dx dy)
  · exact Or.inr (Or.inl (realizes_v22_67 H edges32 x y hne hc dx dy))
  · exact Or.inr (Or.inr (realizes_v22_77 H edges32 x y hne hc dx dy))

end Aris4Math.DoubleLockProfiles

#print axioms Aris4Math.DoubleLockProfiles.two_counts
#print axioms Aris4Math.DoubleLockProfiles.realizes_two_profile
#print axioms Aris4Math.DoubleLockProfiles.realizes_v23_66
#print axioms Aris4Math.DoubleLockProfiles.exists_realized_profile22
