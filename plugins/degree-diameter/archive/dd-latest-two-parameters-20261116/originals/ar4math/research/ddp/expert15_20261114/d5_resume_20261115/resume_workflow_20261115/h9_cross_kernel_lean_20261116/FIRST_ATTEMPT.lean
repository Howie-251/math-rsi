import DegreeDiameter.Portfolio.H9CrossGeometry

namespace DegreeDiameter.Portfolio.H9CrossKernel
open H9CrossRouting
variable {K : Type*} [Field K]

theorem cross_sub_right (p q r : Vec7 K) :
    cross p (fun i => q i - r i) = fun i => cross p q i - cross p r i := by
  funext i
  fin_cases i <;> simp [cross] <;> ring

theorem kernel_zero_0 (p q : Vec7 K) (hp : p 0 ≠ 0)
    (hc : cross p q = 0) (h0 : q 0 = 0) (h5 : q 5 = 0) (h6 : q 6 = 0) :
    q = 0 := by
  have h3 : q 3 = 0 := by
    have hz : p 0 * q 3 = 0 := by
      calc
        p 0 * q 3 = -(cross p q 0) := by simp [cross, h0, h5, h6] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h2 : q 2 = 0 := by
    have hz : p 0 * q 2 = 0 := by
      calc
        p 0 * q 2 = -(cross p q 5) := by simp [cross, h0, h5, h6, h3] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h1 : q 1 = 0 := by
    have hz : p 0 * q 1 = 0 := by
      calc
        p 0 * q 1 = cross p q 6 := by simp [cross, h0, h5, h6, h3, h2] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h4 : q 4 = 0 := by
    have hz : p 0 * q 4 = 0 := by
      calc
        p 0 * q 4 = cross p q 3 := by simp [cross, h0, h5, h6, h3, h2, h1] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  funext i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4
  · exact h5
  · exact h6

theorem kernel_zero_1 (p q : Vec7 K) (hp : p 1 ≠ 0)
    (hc : cross p q = 0) (h1 : q 1 = 0) (h4 : q 4 = 0) (h6 : q 6 = 0) :
    q = 0 := by
  have h3 : q 3 = 0 := by
    have hz : p 1 * q 3 = 0 := by
      calc
        p 1 * q 3 = -(cross p q 1) := by simp [cross, h1, h4, h6] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h2 : q 2 = 0 := by
    have hz : p 1 * q 2 = 0 := by
      calc
        p 1 * q 2 = cross p q 4 := by simp [cross, h1, h4, h6, h3] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h0 : q 0 = 0 := by
    have hz : p 1 * q 0 = 0 := by
      calc
        p 1 * q 0 = -(cross p q 6) := by simp [cross, h1, h4, h6, h3, h2] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h5 : q 5 = 0 := by
    have hz : p 1 * q 5 = 0 := by
      calc
        p 1 * q 5 = cross p q 3 := by simp [cross, h1, h4, h6, h3, h2, h0] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  funext i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4
  · exact h5
  · exact h6

theorem kernel_zero_2 (p q : Vec7 K) (hp : p 2 ≠ 0)
    (hc : cross p q = 0) (h2 : q 2 = 0) (h4 : q 4 = 0) (h5 : q 5 = 0) :
    q = 0 := by
  have h3 : q 3 = 0 := by
    have hz : p 2 * q 3 = 0 := by
      calc
        p 2 * q 3 = -(cross p q 2) := by simp [cross, h2, h4, h5] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h1 : q 1 = 0 := by
    have hz : p 2 * q 1 = 0 := by
      calc
        p 2 * q 1 = -(cross p q 4) := by simp [cross, h2, h4, h5, h3] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h0 : q 0 = 0 := by
    have hz : p 2 * q 0 = 0 := by
      calc
        p 2 * q 0 = cross p q 5 := by simp [cross, h2, h4, h5, h3, h1] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h6 : q 6 = 0 := by
    have hz : p 2 * q 6 = 0 := by
      calc
        p 2 * q 6 = cross p q 3 := by simp [cross, h2, h4, h5, h3, h1, h0] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  funext i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4
  · exact h5
  · exact h6

theorem kernel_zero_4 (p q : Vec7 K) (hp : p 4 ≠ 0)
    (hc : cross p q = 0) (h4 : q 4 = 0) (h1 : q 1 = 0) (h2 : q 2 = 0) :
    q = 0 := by
  have h3 : q 3 = 0 := by
    have hz : p 4 * q 3 = 0 := by
      calc
        p 4 * q 3 = cross p q 4 := by simp [cross, h4, h1, h2] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h6 : q 6 = 0 := by
    have hz : p 4 * q 6 = 0 := by
      calc
        p 4 * q 6 = -(cross p q 1) := by simp [cross, h4, h1, h2, h3] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h5 : q 5 = 0 := by
    have hz : p 4 * q 5 = 0 := by
      calc
        p 4 * q 5 = cross p q 2 := by simp [cross, h4, h1, h2, h3, h6] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h0 : q 0 = 0 := by
    have hz : p 4 * q 0 = 0 := by
      calc
        p 4 * q 0 = -(cross p q 3) := by simp [cross, h4, h1, h2, h3, h6, h5] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  funext i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4
  · exact h5
  · exact h6

theorem kernel_zero_5 (p q : Vec7 K) (hp : p 5 ≠ 0)
    (hc : cross p q = 0) (h5 : q 5 = 0) (h0 : q 0 = 0) (h2 : q 2 = 0) :
    q = 0 := by
  have h3 : q 3 = 0 := by
    have hz : p 5 * q 3 = 0 := by
      calc
        p 5 * q 3 = cross p q 5 := by simp [cross, h5, h0, h2] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h6 : q 6 = 0 := by
    have hz : p 5 * q 6 = 0 := by
      calc
        p 5 * q 6 = cross p q 0 := by simp [cross, h5, h0, h2, h3] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h4 : q 4 = 0 := by
    have hz : p 5 * q 4 = 0 := by
      calc
        p 5 * q 4 = -(cross p q 2) := by simp [cross, h5, h0, h2, h3, h6] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h1 : q 1 = 0 := by
    have hz : p 5 * q 1 = 0 := by
      calc
        p 5 * q 1 = -(cross p q 3) := by simp [cross, h5, h0, h2, h3, h6, h4] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  funext i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4
  · exact h5
  · exact h6

theorem kernel_zero_6 (p q : Vec7 K) (hp : p 6 ≠ 0)
    (hc : cross p q = 0) (h6 : q 6 = 0) (h0 : q 0 = 0) (h1 : q 1 = 0) :
    q = 0 := by
  have h3 : q 3 = 0 := by
    have hz : p 6 * q 3 = 0 := by
      calc
        p 6 * q 3 = cross p q 6 := by simp [cross, h6, h0, h1] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h5 : q 5 = 0 := by
    have hz : p 6 * q 5 = 0 := by
      calc
        p 6 * q 5 = -(cross p q 0) := by simp [cross, h6, h0, h1, h3] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h4 : q 4 = 0 := by
    have hz : p 6 * q 4 = 0 := by
      calc
        p 6 * q 4 = cross p q 1 := by simp [cross, h6, h0, h1, h3, h5] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  have h2 : q 2 = 0 := by
    have hz : p 6 * q 2 = 0 := by
      calc
        p 6 * q 2 = -(cross p q 3) := by simp [cross, h6, h0, h1, h3, h5, h4] <;> ring
        _ = 0 := by rw [hc]; simp
    exact (mul_eq_zero.mp hz).resolve_left hp
  funext i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4
  · exact h5
  · exact h6

abbrev Kernel (p : Vec7 K) := { q : Vec7 K // cross p q = 0 }

theorem projection_injective_of_kernel_zero (p : Vec7 K) (a b c : Fin 7)
    (hz : ∀ q : Vec7 K, cross p q = 0 → q a = 0 → q b = 0 → q c = 0 → q = 0) :
    Function.Injective (fun q : Kernel p => (![q.val a, q.val b, q.val c] : Fin 3 → K)) := by
  intro q r heq
  apply Subtype.ext
  have hd : cross p (fun i => q.val i - r.val i) = 0 := by
    rw [cross_sub_right, q.property, r.property]
    rfl
  have ha : q.val a - r.val a = 0 := by
    exact sub_eq_zero.mpr (congrFun heq 0)
  have hb : q.val b - r.val b = 0 := by
    exact sub_eq_zero.mpr (congrFun heq 1)
  have hc : q.val c - r.val c = 0 := by
    exact sub_eq_zero.mpr (congrFun heq 2)
  have h := hz (fun i => q.val i - r.val i) hd ha hb hc
  funext i
  exact sub_eq_zero.mp (congrFun h i)

/-- Every nonzero null point has a three-coordinate injection of its cross kernel.
No matrix rank lower bound is assumed. -/
theorem null_kernel_injects_three (p : Vec7 K) (hp : p ≠ 0) (hn : norm p = 0) :
    ∃ f : Kernel p → (Fin 3 → K), Function.Injective f := by
  by_cases h0n : p 0 ≠ 0
  · exact ⟨_, projection_injective_of_kernel_zero p 0 5 6
      (fun q hc ha hb hd => kernel_zero_0 p q h0n hc ha hb hd)⟩
  have h0 : p 0 = 0 := not_ne_iff.mp h0n
  by_cases h1n : p 1 ≠ 0
  · exact ⟨_, projection_injective_of_kernel_zero p 1 4 6
      (fun q hc ha hb hd => kernel_zero_1 p q h1n hc ha hb hd)⟩
  have h1 : p 1 = 0 := not_ne_iff.mp h1n
  by_cases h2n : p 2 ≠ 0
  · exact ⟨_, projection_injective_of_kernel_zero p 2 4 5
      (fun q hc ha hb hd => kernel_zero_2 p q h2n hc ha hb hd)⟩
  have h2 : p 2 = 0 := not_ne_iff.mp h2n
  by_cases h4n : p 4 ≠ 0
  · exact ⟨_, projection_injective_of_kernel_zero p 4 1 2
      (fun q hc ha hb hd => kernel_zero_4 p q h4n hc ha hb hd)⟩
  have h4 : p 4 = 0 := not_ne_iff.mp h4n
  by_cases h5n : p 5 ≠ 0
  · exact ⟨_, projection_injective_of_kernel_zero p 5 0 2
      (fun q hc ha hb hd => kernel_zero_5 p q h5n hc ha hb hd)⟩
  have h5 : p 5 = 0 := not_ne_iff.mp h5n
  by_cases h6n : p 6 ≠ 0
  · exact ⟨_, projection_injective_of_kernel_zero p 6 0 1
      (fun q hc ha hb hd => kernel_zero_6 p q h6n hc ha hb hd)⟩
  have h6 : p 6 = 0 := not_ne_iff.mp h6n
  have h3 : p 3 = 0 := by
    simpa [norm, h0, h1, h2, h4, h5, h6] using hn
  exfalso
  apply hp
  funext i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4
  · exact h5
  · exact h6

end DegreeDiameter.Portfolio.H9CrossKernel

#print axioms DegreeDiameter.Portfolio.H9CrossKernel.null_kernel_injects_three
#print axioms DegreeDiameter.Portfolio.H9CrossKernel.projection_injective_of_kernel_zero
