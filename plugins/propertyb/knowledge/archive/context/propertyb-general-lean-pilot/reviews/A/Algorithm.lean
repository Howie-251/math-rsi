import Aris4Math.General.RS.Definitions
import Mathlib.Data.Finset.Max
import Mathlib.Data.Fintype.Perm

namespace Aris4Math.General.RS

variable {n : ℕ}

def FlipWitness (E : Finset (Finset (Fin n))) (c : Fin n → Bool)
    (flipped : Finset (Fin n)) (x : Fin n) : Prop :=
  ∃ e ∈ E, x ∈ e ∧ Mono e c (c x) ∧ Disjoint e flipped

noncomputable def flippedAfter (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) : ℕ → Finset (Fin n)
  | 0 => ∅
  | t + 1 => by
      classical
      exact if ht : t < n then
        let x := σ.symm ⟨t, ht⟩
        if b x = true ∧ FlipWitness E c (flippedAfter E c b σ t) x then
          insert x (flippedAfter E c b σ t)
        else flippedAfter E c b σ t
      else flippedAfter E c b σ t

noncomputable def finalColor (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) (x : Fin n) : Bool :=
  if x ∈ flippedAfter E c b σ n then !(c x) else c x

def Failure (E : Finset (Finset (Fin n))) (c b : Fin n → Bool)
    (σ : Equiv.Perm (Fin n)) : Prop :=
  ∃ e ∈ E, ∃ q : Bool, Mono e (finalColor E c b σ) q

def ResidualEvent (E : Finset (Finset (Fin n))) (c b : Fin n → Bool) : Prop :=
  ∃ e ∈ E, (∃ q : Bool, Mono e c q) ∧ ∀ x ∈ e, b x = false

def PairEvent (f g : Finset (Fin n)) (c b : Fin n → Bool)
    (σ : Equiv.Perm (Fin n)) (q : Bool) : Prop :=
  ∃ x : Fin n, f ∩ g = {x} ∧ b x = true ∧ Mono g c (!q) ∧
    (∀ z ∈ f.erase x, c z = !q → b z = true ∧ σ z < σ x) ∧
    (∀ z ∈ g.erase x, b z = true → σ x < σ z)

theorem flippedAfter_step_subset (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) (t : ℕ) :
    flippedAfter E c b σ t ⊆ flippedAfter E c b σ (t + 1) := by
  classical
  simp only [flippedAfter]
  split_ifs <;> simp

theorem flippedAfter_mono (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) :
    Monotone (flippedAfter E c b σ) :=
  monotone_nat_of_le_succ (flippedAfter_step_subset E c b σ)

theorem flippedAfter_mem_before (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) (t : ℕ)
    (x : Fin n) (hx : x ∈ flippedAfter E c b σ t) : (σ x).val < t := by
  classical
  induction t with
  | zero => simp [flippedAfter] at hx
  | succ t ih =>
    simp only [flippedAfter] at hx
    split_ifs at hx with ht hflip
    · rcases Finset.mem_insert.mp hx with hnew | hold
      · subst x
        simp
      · exact Nat.lt.step (ih hold)
    · exact Nat.lt.step (ih hx)
    · exact Nat.lt.step (ih hx)

theorem flippedAfter_of_trigger (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) (x : Fin n)
    (hb : b x = true)
    (hw : FlipWitness E c (flippedAfter E c b σ (σ x).val) x) :
    x ∈ flippedAfter E c b σ ((σ x).val + 1) := by
  classical
  simp only [flippedAfter, dif_pos (σ x).isLt]
  simp [hb, hw]

theorem flippedAfter_mem_trigger (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) (t : ℕ)
    (x : Fin n) (hx : x ∈ flippedAfter E c b σ t) :
    b x = true ∧ FlipWitness E c (flippedAfter E c b σ (σ x).val) x := by
  classical
  induction t with
  | zero => simp [flippedAfter] at hx
  | succ t ih =>
    simp only [flippedAfter] at hx
    split_ifs at hx with ht hflip
    · rcases Finset.mem_insert.mp hx with hnew | hold
      · subst x
        simpa only [Equiv.apply_symm_apply] using hflip
      · exact ih hold
    · exact ih hx
    · exact ih hx

theorem flippedAfter_mem_earlier (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) (t : ℕ)
    (x : Fin n) (hx : x ∈ flippedAfter E c b σ n)
    (ht : (σ x).val < t) : x ∈ flippedAfter E c b σ t := by
  obtain ⟨hb, hw⟩ := flippedAfter_mem_trigger E c b σ n x hx
  exact flippedAfter_mono E c b σ (Nat.succ_le_of_lt ht)
    (flippedAfter_of_trigger E c b σ x hb hw)

theorem mem_flipped_of_final_ne (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) (x : Fin n)
    (h : finalColor E c b σ x ≠ c x) : x ∈ flippedAfter E c b σ n := by
  classical
  by_contra hx
  exact h (by simp [finalColor, hx])

theorem not_mem_flipped_of_final_eq (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) (x : Fin n)
    (h : finalColor E c b σ x = c x) : x ∉ flippedAfter E c b σ n := by
  classical
  intro hx
  have hnot : !(c x) = c x := by simpa [finalColor, hx] using h
  cases hcx : c x <;> simp [hcx] at hnot

theorem same_color_residual (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n))
    (e : Finset (Fin n)) (he : e ∈ E) (q : Bool)
    (hinit : Mono e c q) (hfinal : Mono e (finalColor E c b σ) q) :
    ResidualEvent E c b := by
  classical
  have hno : Disjoint e (flippedAfter E c b σ n) := by
    apply Finset.disjoint_left.mpr
    intro x hx
    exact not_mem_flipped_of_final_eq E c b σ x ((hfinal x hx).trans (hinit x hx).symm)
  refine ⟨e, he, ⟨q, hinit⟩, ?_⟩
  intro x hx
  by_cases hb : b x = true
  · have hw : FlipWitness E c (flippedAfter E c b σ (σ x).val) x := by
      refine ⟨e, he, hx, ?_, ?_⟩
      · simpa only [hinit x hx] using hinit
      · exact hno.mono_right (flippedAfter_mono E c b σ (Nat.le_of_lt (σ x).isLt))
    have hflip := flippedAfter_of_trigger E c b σ x hb hw
    have hlast := flippedAfter_mono E c b σ (Nat.succ_le_of_lt (σ x).isLt) hflip
    exact False.elim (Finset.disjoint_left.mp hno hx hlast)
  · cases hbx : b x <;> simp_all

theorem eligible_witness_not_before (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n))
    (g : Finset (Fin n)) (hg : g ∈ E) (q : Bool)
    (hmono : Mono g c q) (t : ℕ) (hdisj : Disjoint g (flippedAfter E c b σ t))
    (z : Fin n) (hz : z ∈ g) (hb : b z = true) : t ≤ (σ z).val := by
  classical
  by_contra hle
  have hlt : (σ z).val < t := Nat.lt_of_not_ge hle
  have hw : FlipWitness E c (flippedAfter E c b σ (σ z).val) z := by
    refine ⟨g, hg, hz, ?_, ?_⟩
    · simpa only [hmono z hz] using hmono
    · exact hdisj.mono_right (flippedAfter_mono E c b σ (Nat.le_of_lt hlt))
  have hmem := flippedAfter_mono E c b σ (Nat.succ_le_of_lt hlt)
    (flippedAfter_of_trigger E c b σ z hb hw)
  exact Finset.disjoint_left.mp hdisj hz hmem

end Aris4Math.General.RS
