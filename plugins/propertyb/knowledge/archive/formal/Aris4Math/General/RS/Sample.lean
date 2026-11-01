import Aris4Math.General.RS.Algorithm
import Aris4Math.General.RS.Bernoulli
import Mathlib.Tactic.Positivity

namespace Aris4Math.General.RS

open scoped BigOperators
noncomputable section
attribute [local instance] Classical.propDecidable

variable {n : ℕ}

def permExpect (f : Equiv.Perm (Fin n) → ℝ) : ℝ :=
  (∑ σ, f σ) / (Fintype.card (Equiv.Perm (Fin n)) : ℝ)

def permProb (P : Equiv.Perm (Fin n) → Prop) : ℝ :=
  permExpect (fun σ => if P σ then 1 else 0)

def sampleExpect (p : ℝ)
    (f : (Fin n → Bool) → (Fin n → Bool) → Equiv.Perm (Fin n) → ℝ) : ℝ :=
  bernoulliExpect (1/2 : ℝ) (fun c =>
    bernoulliExpect p (fun b => permExpect (f c b)))

def sampleProb (p : ℝ)
    (P : (Fin n → Bool) → (Fin n → Bool) → Equiv.Perm (Fin n) → Prop) : ℝ :=
  sampleExpect p (fun c b σ => if P c b σ then 1 else 0)

def failureProb (E : Finset (Finset (Fin n))) (p : ℝ) : ℝ :=
  sampleProb p (Failure E)

theorem permCard_pos : (0 : ℝ) < (Fintype.card (Equiv.Perm (Fin n)) : ℝ) := by
  exact_mod_cast (Fintype.card_pos : 0 < Fintype.card (Equiv.Perm (Fin n)))

@[simp] theorem permExpect_const (r : ℝ) : permExpect (n := n) (fun _ => r) = r := by
  simp [permExpect, ne_of_gt (permCard_pos (n := n))]

theorem permExpect_mono {f g : Equiv.Perm (Fin n) → ℝ} (h : ∀ σ, f σ ≤ g σ) :
    permExpect f ≤ permExpect g := by
  exact div_le_div_of_nonneg_right (Finset.sum_le_sum fun σ _ => h σ)
    (le_of_lt permCard_pos)

theorem permExpect_add (f g : Equiv.Perm (Fin n) → ℝ) :
    permExpect (fun σ => f σ + g σ) = permExpect f + permExpect g := by
  simp [permExpect, Finset.sum_add_distrib, add_div]

@[simp] theorem sampleExpect_const (p r : ℝ) :
    sampleExpect (n := n) p (fun _ _ _ => r) = r := by
  simp [sampleExpect]

theorem sampleExpect_mono {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1)
    {f g : (Fin n → Bool) → (Fin n → Bool) → Equiv.Perm (Fin n) → ℝ}
    (h : ∀ c b σ, f c b σ ≤ g c b σ) : sampleExpect p f ≤ sampleExpect p g := by
  apply bernoulliExpect_mono (by norm_num) (by norm_num)
  intro c
  apply bernoulliExpect_mono hp hp1
  intro b
  exact permExpect_mono (h c b)

theorem sampleExpect_add (p : ℝ)
    (f g : (Fin n → Bool) → (Fin n → Bool) → Equiv.Perm (Fin n) → ℝ) :
    sampleExpect p (fun c b σ => f c b σ + g c b σ) = sampleExpect p f + sampleExpect p g := by
  simp only [sampleExpect, permExpect_add, bernoulliExpect_add]

@[simp] theorem sampleProb_true (p : ℝ) :
    sampleProb (n := n) p (fun _ _ _ => True) = 1 := by simp [sampleProb]

@[simp] theorem sampleProb_false (p : ℝ) :
    sampleProb (n := n) p (fun _ _ _ => False) = 0 := by simp [sampleProb]

theorem sampleProb_mono {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1)
    {P Q : (Fin n → Bool) → (Fin n → Bool) → Equiv.Perm (Fin n) → Prop}
    (h : ∀ c b σ, P c b σ → Q c b σ) : sampleProb p P ≤ sampleProb p Q := by
  apply sampleExpect_mono hp hp1
  intro c b σ
  by_cases hP : P c b σ
  · simp [hP, h c b σ hP]
  · simp [hP]; split_ifs <;> norm_num

theorem sampleProb_union_le {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1)
    (P Q : (Fin n → Bool) → (Fin n → Bool) → Equiv.Perm (Fin n) → Prop) :
    sampleProb p (fun c b σ => P c b σ ∨ Q c b σ) ≤ sampleProb p P + sampleProb p Q := by
  unfold sampleProb
  rw [← sampleExpect_add]
  apply sampleExpect_mono hp hp1
  intro c b σ
  by_cases hP : P c b σ <;> by_cases hQ : Q c b σ <;> simp [hP, hQ]

theorem sampleProb_finset_union_le {I : Type*} {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1)
    (s : Finset I)
    (P : I → (Fin n → Bool) → (Fin n → Bool) → Equiv.Perm (Fin n) → Prop) :
    sampleProb p (fun c b σ => ∃ i ∈ s, P i c b σ) ≤ ∑ i ∈ s, sampleProb p (P i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert i s hi ih =>
    simp only [Finset.mem_insert, exists_eq_or_imp, Finset.sum_insert hi]
    exact (sampleProb_union_le hp hp1 (P i) (fun c b σ => ∃ j ∈ s, P j c b σ)).trans
      (add_le_add_left ih _)

theorem sampleProb_no_order (p : ℝ) (P : (Fin n → Bool) → (Fin n → Bool) → Prop) :
    sampleProb p (fun c b _ => P c b) =
      bernoulliExpect (1/2 : ℝ) (fun c => bernoulliProb p (P c)) := by
  simp only [sampleProb, sampleExpect, permExpect_const, bernoulliProb]

theorem exists_not_of_sampleProb_lt_one (p : ℝ)
    (P : (Fin n → Bool) → (Fin n → Bool) → Equiv.Perm (Fin n) → Prop)
    (h : sampleProb p P < 1) : ∃ c b σ, ¬ P c b σ := by
  classical
  by_contra hn
  have hall : ∀ c b σ, P c b σ := by simpa only [not_exists, not_not] using hn
  have heq : P = (fun _ _ _ => True) := by
    funext c b σ
    exact propext ⟨fun _ => trivial, fun _ => hall c b σ⟩
  rw [heq, sampleProb_true] at h
  exact lt_irrefl _ h

theorem propertyB_of_failureProb_lt_one (E : Finset (Finset (Fin n))) (p : ℝ)
    (h : failureProb E p < 1) : PropertyB E := by
  obtain ⟨c, b, σ, hs⟩ := exists_not_of_sampleProb_lt_one p (Failure E) h
  exact ⟨finalColor E c b σ, bichromatic_of_not_failure E c b σ hs⟩

end
end Aris4Math.General.RS
