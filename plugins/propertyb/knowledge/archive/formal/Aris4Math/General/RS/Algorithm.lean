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

private theorem bool_eq_not_of_ne {a q : Bool} (h : a ≠ q) : a = !q := by
  cases a <;> cases q <;> simp_all

theorem new_mono_pair_event (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n))
    (f : Finset (Fin n)) (hf : f ∈ E) (hsize : 2 ≤ f.card) (q : Bool)
    (hfinal : Mono f (finalColor E c b σ) q) (hinit : ¬ Mono f c q) :
    ∃ g ∈ E, f ≠ g ∧ PairEvent f g c b σ q := by
  classical
  have hsome : ∃ z ∈ f, c z ≠ q := by
    simpa only [Mono, not_forall, exists_prop] using hinit
  let S := f.filter (fun z => c z ≠ q)
  have hS : S.Nonempty := by
    obtain ⟨z, hz, hc⟩ := hsome
    exact ⟨z, Finset.mem_filter.mpr ⟨hz, hc⟩⟩
  obtain ⟨x, hxS, hmax⟩ := Finset.exists_max_image S σ hS
  have hxf : x ∈ f := (Finset.mem_filter.mp hxS).1
  have hcx : c x ≠ q := (Finset.mem_filter.mp hxS).2
  have hxflip : x ∈ flippedAfter E c b σ n :=
    mem_flipped_of_final_ne E c b σ x (by rw [hfinal x hxf]; exact Ne.symm hcx)
  obtain ⟨hb, g, hg, hxg, hgmono, hgdisj⟩ := flippedAfter_mem_trigger E c b σ n x hxflip
  have hinter : f ∩ g = {x} := by
    ext z
    constructor
    · intro hz
      obtain ⟨hzf, hzg⟩ := Finset.mem_inter.mp hz
      apply Finset.mem_singleton.mpr
      by_contra hne
      have hcz : c z ≠ q := by rw [hgmono z hzg]; exact hcx
      have hzS : z ∈ S := Finset.mem_filter.mpr ⟨hzf, hcz⟩
      have hlt : σ z < σ x :=
        lt_of_le_of_ne (hmax z hzS) (fun heq => hne (σ.injective heq))
      have hzflip : z ∈ flippedAfter E c b σ n :=
        mem_flipped_of_final_ne E c b σ z (by rw [hfinal z hzf]; exact Ne.symm hcz)
      exact Finset.disjoint_left.mp hgdisj hzg
        (flippedAfter_mem_earlier E c b σ (σ x).val z hzflip hlt)
    · intro hz
      rw [Finset.mem_singleton] at hz
      subst z
      exact Finset.mem_inter.mpr ⟨hxf, hxg⟩
  have hfg : f ≠ g := by
    intro heq
    have hsingle : f = {x} := by simpa only [← heq, Finset.inter_self] using hinter
    have hcard : f.card = 1 := by rw [hsingle]; simp
    omega
  refine ⟨g, hg, hfg, x, hinter, hb, ?_, ?_, ?_⟩
  · simpa only [bool_eq_not_of_ne hcx] using hgmono
  · intro z hz hcz
    have hzf : z ∈ f := Finset.mem_of_mem_erase hz
    have hne : z ≠ x := (Finset.mem_erase.mp hz).1
    have hczne : c z ≠ q := by rw [hcz]; cases q <;> decide
    have hzS : z ∈ S := Finset.mem_filter.mpr ⟨hzf, hczne⟩
    have hzflip : z ∈ flippedAfter E c b σ n :=
      mem_flipped_of_final_ne E c b σ z (by rw [hfinal z hzf]; exact Ne.symm hczne)
    exact ⟨(flippedAfter_mem_trigger E c b σ n z hzflip).1,
      lt_of_le_of_ne (hmax z hzS) (fun heq => hne (σ.injective heq))⟩
  · intro z hz hzb
    have hzg : z ∈ g := Finset.mem_of_mem_erase hz
    have hne : z ≠ x := (Finset.mem_erase.mp hz).1
    have hle : σ x ≤ σ z :=
      eligible_witness_not_before E c b σ g hg (c x) hgmono (σ x).val hgdisj z hzg hzb
    exact lt_of_le_of_ne hle (fun heq => hne (σ.injective heq.symm))

theorem failure_covered (E : Finset (Finset (Fin n))) (k : ℕ)
    (hk : 2 ≤ k) (hu : Uniform E k) (c b : Fin n → Bool)
    (σ : Equiv.Perm (Fin n)) (hfail : Failure E c b σ) :
    ResidualEvent E c b ∨
      ∃ f ∈ E, ∃ g ∈ E, f ≠ g ∧ ∃ q : Bool, PairEvent f g c b σ q := by
  classical
  obtain ⟨f, hf, q, hfinal⟩ := hfail
  by_cases hinit : Mono f c q
  · exact Or.inl (same_color_residual E c b σ f hf q hinit hfinal)
  · obtain ⟨g, hg, hfg, hpair⟩ :=
      new_mono_pair_event E c b σ f hf (by rw [hu f hf]; exact hk) q hfinal hinit
    exact Or.inr ⟨f, hf, g, hg, hfg, q, hpair⟩

theorem bichromatic_of_not_failure (E : Finset (Finset (Fin n)))
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) (h : ¬ Failure E c b σ) :
    Bichromatic E (finalColor E c b σ) := by
  classical
  intro e he
  constructor
  · by_contra hnone
    apply h
    refine ⟨e, he, false, ?_⟩
    intro x hx
    cases hc : finalColor E c b σ x with
    | false => rfl
    | true => exact False.elim (hnone ⟨x, hx, hc⟩)
  · by_contra hnone
    apply h
    refine ⟨e, he, true, ?_⟩
    intro x hx
    cases hc : finalColor E c b σ x with
    | false => exact False.elim (hnone ⟨x, hx, hc⟩)
    | true => rfl

end Aris4Math.General.RS
