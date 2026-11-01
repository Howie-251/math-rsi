import Aris4Math.ThirtyThree.DoubleLockProfiles

/-! Actual double-lock tables at any two ordered, legal one-based positions.
This supports the twenty-vertex positions 10,11 and the twenty-two-vertex
positions 11,12 through the same real-edge counting interface. -/

namespace Aris4Math.ThirtyThree.DoubleLockAt

open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles

def positionsAt (v a b : ℕ) (ha : 1 ≤ a) (hab : a < b) (hb : b ≤ v) : Fin 2 ↪ Fin v where
  toFun := ![⟨a-1, by omega⟩, ⟨b-1, by omega⟩]
  inj' := by
    intro i j heq
    fin_cases i <;> fin_cases j
    · rfl
    · have hval := congrArg Fin.val heq
      change a - 1 = b - 1 at hval
      omega
    · have hval := congrArg Fin.val heq
      change b - 1 = a - 1 at hval
      omega
    · rfl

def profileAt (v a b d e : ℕ) (centers : List ℕ) : Numeric.Profile :=
  ⟨v, [a,b], [⟨[],34-d-e⟩, ⟨[a],d-1⟩, ⟨[b],e-1⟩, ⟨[a,b],1⟩], none, centers⟩

def classAt {v : ℕ} (a b : ℕ) (x y : Fin v) (A : Finset (Fin v)) : List ℕ :=
  if x ∈ A then (if y ∈ A then [a,b] else [a]) else (if y ∈ A then [b] else [])

theorem type_at {v a b : ℕ} (ha : 1 ≤ a) (hab : a < b) (hb : b ≤ v)
    (x y : Fin v) (hne : x ≠ y) (A : Finset (Fin v)) :
    positionType (twoVertices x y hne) (positionsAt v a b ha hab hb) A = classAt a b x y A := by
  have hs : lockSignature (twoVertices x y hne) A =
      if x ∈ A then (if y ∈ A then {0,1} else {0}) else (if y ∈ A then {1} else ∅) := by
    ext i
    fin_cases i <;> by_cases hx : x ∈ A <;> by_cases hy : y ∈ A <;>
      simp [lockSignature, twoVertices, hx, hy]
  unfold positionType positionSignature
  rw [hs]
  have habne : a ≠ b := ne_of_lt hab
  have hsort : ({a,b} : Finset ℕ).sort (· ≤ ·) = [a,b] := by
    simpa using (List.toFinset_sort (· ≤ ·)
      (by simp [habne] : ([a,b] : List ℕ).Nodup)).mpr (by simp [le_of_lt hab])
  have ha1 : a-1+1 = a := by omega
  have hb1 : b-1+1 = b := by omega
  by_cases hx : x ∈ A <;> by_cases hy : y ∈ A <;>
    simp [positionsAt, classAt, hx, hy, ha1, hb1, hsort]

/-- Each new label denotes exactly the same actual fiber as its old 11,12 label. -/
theorem fiber_at_eq {v a b : ℕ} (hab : a < b)
    (H : Simple5Hypergraph (Fin v)) (x y : Fin v) (i : Fin 4) :
    multiplicity H.edges (classAt a b x y) (![[],[a],[b],[a,b]] i) =
      multiplicity H.edges (twoClass x y) (![[],[11],[12],[11,12]] i) := by
  unfold multiplicity fiber
  congr 1
  ext A
  have habne : a ≠ b := ne_of_lt hab
  have hbane : b ≠ a := Ne.symm habne
  fin_cases i <;> by_cases hx : x ∈ A <;> by_cases hy : y ∈ A <;>
    simp [classAt, twoClass, hx, hy, habne, hbane]

/-- This theorem builds the realization from H, its actual degrees and codegree.
The only data hypothesis is finite well-formedness, checked for each caller. -/
theorem realizes_profile_at {v a b : ℕ}
    (H : Simple5Hypergraph (Fin v)) (edges33 : H.edges.card = 33)
    (ha : 1 ≤ a) (hab : a < b) (hb : b ≤ v)
    (x y : Fin v) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (centers : List ℕ)
    (valid : Numeric.validProfile (profileAt v a b (H.degree x) (H.degree y) centers) 33) :
    RealizesProfile H (twoVertices x y hne) (positionsAt v a b ha hab hb)
      (profileAt v a b (H.degree x) (H.degree y) centers) 33 := by
  have habne : a ≠ b := ne_of_lt hab
  have hbane : b ≠ a := Ne.symm habne
  have ha1 : a-1+1 = a := by omega
  have hb1 : b-1+1 = b := by omega
  refine ⟨rfl, valid, ?_, ?_⟩
  · have hu : (Finset.univ : Finset (Fin 2)) = {0,1} := by decide
    simp [profileAt, hu, positionsAt, ha1, hb1]
  · constructor
    · simp [profileAt, habne]
    · intro A _
      rw [type_at]
      by_cases hx : x ∈ A <;> by_cases hy : y ∈ A <;>
        simp [profileAt, classAt, hx, hy]
    · have heq : positionType (twoVertices x y hne) (positionsAt v a b ha hab hb) =
          classAt a b x y := funext (type_at ha hab hb x y hne)
      rw [heq]
      intro t ht
      simp only [profileAt, List.mem_cons, List.not_mem_nil, or_false] at ht
      have counts := ThirtyThree.DoubleLockProfiles.two_counts H edges33 x y codegree1
      have h0 := fiber_at_eq hab H x y 0
      have h1 := fiber_at_eq hab H x y 1
      have h2 := fiber_at_eq hab H x y 2
      have h3 := fiber_at_eq hab H x y 3
      simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
        Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons] at h0 h1 h2 h3
      rcases ht with rfl | rfl | rfl | rfl
      · exact h0.trans counts.1
      · exact h1.trans counts.2.1
      · exact h2.trans counts.2.2.1
      · exact h3.trans counts.2.2.2

end Aris4Math.ThirtyThree.DoubleLockAt

#print axioms Aris4Math.ThirtyThree.DoubleLockAt.realizes_profile_at
