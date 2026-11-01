import Aris4Math.General.RS.Sample
import Aris4Math.General.RS.OrderCounting
import Aris4Math.General.RS.Integral

namespace Aris4Math.General.RS
open scoped BigOperators
open MeasureTheory
noncomputable section
attribute [local instance] Classical.propDecidable

/-- The product-law calculation for the independent color and eligibility
coordinates. It makes no independence assertion about overlapping edges. -/
theorem bernoulliExpect_two_coordinate_prod {V : Type*} [Fintype V]
    (r p : ℝ) (Q : V → Bool → Bool → ℝ) :
    bernoulliExpect r (fun c => bernoulliExpect p (fun b => ∏ v, Q v (c v) (b v))) =
      ∏ v, ((1-r) * ((1-p)*Q v false false + p*Q v false true) +
        r * ((1-p)*Q v true false + p*Q v true true)) := by
  have hb (c : V → Bool) := bernoulliExpect_coordinate_prod p (fun v b => Q v (c v) b)
  simp_rw [hb]
  exact bernoulliExpect_coordinate_prod r (fun v c => (1-p)*Q v c false + p*Q v c true)

/-- Local factor for a vertex of the first edge away from the common pivot. -/
def pairLeftFactor (q c b : Bool) (t : ℝ) : ℝ :=
  if c = !q then if b then t else 0 else 1

/-- Local factor for a vertex of the witness edge away from the common pivot. -/
def pairRightFactor (q c b : Bool) (t : ℝ) : ℝ :=
  if c = !q then if b then 1-t else 1 else 0

def pairPivotFactor (q c b : Bool) : ℝ := if c = !q ∧ b = true then 1 else 0

def pairIntegrand {n : ℕ} (F G : Finset (Fin n)) (x : Fin n) (q : Bool)
    (c b : Fin n → Bool) (t : ℝ) : ℝ :=
  pairPivotFactor q (c x) (b x) *
    (∏ z ∈ F, pairLeftFactor q (c z) (b z) t) *
    (∏ z ∈ G, pairRightFactor q (c z) (b z) t)

lemma pairLeft_prod {n : ℕ} (F : Finset (Fin n)) (q : Bool)
    (c b : Fin n → Bool) (t : ℝ) :
    (∏ z ∈ F, pairLeftFactor q (c z) (b z) t) =
      (if (∀ z ∈ F, c z = !q → b z = true) then 1 else 0) *
        t ^ (F.filter (fun z => c z = !q)).card := by
  classical
  have hf (z : Fin n) : pairLeftFactor q (c z) (b z) t =
      (if c z = !q → b z = true then (1 : ℝ) else 0) *
        (if c z = !q then t else 1) := by
    by_cases hc : c z = !q <;> cases hb : b z <;> simp [pairLeftFactor, hc]
  simp_rw [hf]
  rw [Finset.prod_mul_distrib, Finset.prod_boole]
  apply congrArg₂ (· * ·)
  · by_cases h : ∀ z ∈ F, c z = !q → b z = true <;> simp [h]
  · rw [← Finset.prod_filter]
    simp

lemma pairRight_prod {n : ℕ} (G : Finset (Fin n)) (q : Bool)
    (c b : Fin n → Bool) (t : ℝ) :
    (∏ z ∈ G, pairRightFactor q (c z) (b z) t) =
      (if (∀ z ∈ G, c z = !q) then 1 else 0) *
        (1-t) ^ (G.filter (fun z => b z = true)).card := by
  classical
  have hf (z : Fin n) : pairRightFactor q (c z) (b z) t =
      (if c z = !q then (1 : ℝ) else 0) *
        (if b z = true then 1-t else 1) := by
    by_cases hc : c z = !q <;> cases hb : b z <;> simp [pairRightFactor, hc]
  simp_rw [hf]
  rw [Finset.prod_mul_distrib, Finset.prod_boole]
  apply congrArg₂ (· * ·)
  · by_cases h : ∀ z ∈ G, c z = !q <;> simp [h]
  · rw [← Finset.prod_filter]
    simp

def pairGuard {n : ℕ} (F G : Finset (Fin n)) (x : Fin n) (q : Bool)
    (c b : Fin n → Bool) : Prop :=
  c x = !q ∧ b x = true ∧ (∀ z ∈ F, c z = !q → b z = true) ∧
    (∀ z ∈ G, c z = !q)

def pairLocalEvent {n : ℕ} (F G : Finset (Fin n)) (x : Fin n) (q : Bool)
    (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) : Prop :=
  pairGuard F G x q c b ∧
    BeforeAfter (F.filter (fun z => c z = !q)) (G.filter (fun z => b z = true)) x σ

lemma pairIntegrand_guard {n : ℕ} (F G : Finset (Fin n)) (x : Fin n) (q : Bool)
    (c b : Fin n → Bool) (t : ℝ) :
    pairIntegrand F G x q c b t = if pairGuard F G x q c b then
      t ^ (F.filter (fun z => c z = !q)).card *
        (1-t) ^ (G.filter (fun z => b z = true)).card else 0 := by
  rw [pairIntegrand, pairLeft_prod, pairRight_prod]
  unfold pairPivotFactor pairGuard
  split_ifs <;> simp_all

lemma permProb_card {n : ℕ} (P : Equiv.Perm (Fin n) → Prop) :
    permProb P = (Fintype.card {σ : Equiv.Perm (Fin n) // P σ} : ℝ) /
      Fintype.card (Equiv.Perm (Fin n)) := by
  classical
  simp [permProb, permExpect, Fintype.card_subtype, Finset.sum_boole]

lemma permProb_pairLocal {n : ℕ} (F G : Finset (Fin n)) (x : Fin n)
    (hFG : Disjoint F G) (hxF : x ∉ F) (hxG : x ∉ G) (q : Bool)
    (c b : Fin n → Bool) :
    permProb (pairLocalEvent F G x q c b) =
      ∫ t in (0 : ℝ)..1, pairIntegrand F G x q c b t := by
  classical
  have hd : Disjoint (F.filter (fun z => c z = !q)) (G.filter (fun z => b z = true)) :=
    hFG.mono (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  have hxA : x ∉ F.filter (fun z => c z = !q) := fun h => hxF (Finset.mem_of_mem_filter _ h)
  have hxB : x ∉ G.filter (fun z => b z = true) := fun h => hxG (Finset.mem_of_mem_filter _ h)
  by_cases hguard : pairGuard F G x q c b
  · have heq : pairLocalEvent F G x q c b =
        BeforeAfter (F.filter (fun z => c z = !q)) (G.filter (fun z => b z = true)) x := by
      funext σ; exact propext (by simp [pairLocalEvent, hguard])
    rw [heq, permProb_card, beforeAfter_ratio _ _ _ hd hxA hxB]
    simp_rw [pairIntegrand_guard, if_pos hguard]
    exact (beta_nat _ _).symm
  · have heq : pairLocalEvent F G x q c b = (fun _ => False) := by
      funext σ; exact propext (by simp [pairLocalEvent, hguard])
    rw [heq]
    simp [permProb, pairIntegrand_guard, hguard]

lemma bernoulliExpect_intervalIntegral {V : Type*} [Fintype V] (p : ℝ)
    (f : (V → Bool) → ℝ → ℝ) (hf : ∀ b, Continuous (f b)) :
    bernoulliExpect p (fun b => ∫ t in (0 : ℝ)..1, f b t) =
      ∫ t in (0 : ℝ)..1, bernoulliExpect p (fun b => f b t) := by
  classical
  unfold bernoulliExpect
  rw [intervalIntegral.integral_finset_sum]
  · apply Finset.sum_congr rfl
    intro b _
    rw [intervalIntegral.integral_const_mul]
  · intro b _
    exact (continuous_const.mul (hf b)).intervalIntegrable 0 1

lemma continuous_bernoulliExpect {V : Type*} [Fintype V] (p : ℝ)
    (f : (V → Bool) → ℝ → ℝ) (hf : ∀ b, Continuous (f b)) :
    Continuous (fun t => bernoulliExpect p (fun b => f b t)) := by
  unfold bernoulliExpect
  exact continuous_finset_sum _ (fun b _ => continuous_const.mul (hf b))

lemma pairIntegrand_continuous {n : ℕ} (F G : Finset (Fin n)) (x : Fin n) (q : Bool)
    (c b : Fin n → Bool) : Continuous (pairIntegrand F G x q c b) := by
  have heq : pairIntegrand F G x q c b = (fun t =>
      if pairGuard F G x q c b then t ^ (F.filter (fun z => c z = !q)).card *
        (1-t) ^ (G.filter (fun z => b z = true)).card else 0) := by
    funext t; exact pairIntegrand_guard F G x q c b t
  rw [heq]
  by_cases h : pairGuard F G x q c b <;> simp only [h, ite_true, ite_false] <;> fun_prop

lemma pairIntegrand_eq_prod {n : ℕ} (F G : Finset (Fin n)) (x : Fin n) (q : Bool)
    (c b : Fin n → Bool) (t : ℝ) :
    pairIntegrand F G x q c b t =
      ∏ v : Fin n,
        (if v = x then pairPivotFactor q (c v) (b v) else 1) *
        (if v ∈ F then pairLeftFactor q (c v) (b v) t else 1) *
        (if v ∈ G then pairRightFactor q (c v) (b v) t else 1) := by
  simp only [Finset.prod_mul_distrib, Fintype.prod_ite_eq', Fintype.prod_ite_mem,
    pairIntegrand]

lemma pairIntegrand_average {n : ℕ} (F G : Finset (Fin n)) (x : Fin n)
    (hFG : Disjoint F G) (hxF : x ∉ F) (hxG : x ∉ G) (q : Bool) (p t : ℝ) :
    bernoulliExpect (1/2 : ℝ) (fun c =>
      bernoulliExpect p (fun b => pairIntegrand F G x q c b t)) =
        (p/2) * ((1+p*t)/2)^F.card * ((1-p*t)/2)^G.card := by
  classical
  simp_rw [pairIntegrand_eq_prod]
  rw [bernoulliExpect_two_coordinate_prod (1/2 : ℝ) p (fun v cc bb =>
    (if v = x then pairPivotFactor q cc bb else 1) *
      (if v ∈ F then pairLeftFactor q cc bb t else 1) *
      (if v ∈ G then pairRightFactor q cc bb t else 1))]
  have hfactor (v : Fin n) :
      (1-(1/2 : ℝ)) * ((1-p) *
          ((if v = x then pairPivotFactor q false false else 1) *
           (if v ∈ F then pairLeftFactor q false false t else 1) *
           (if v ∈ G then pairRightFactor q false false t else 1)) + p *
          ((if v = x then pairPivotFactor q false true else 1) *
           (if v ∈ F then pairLeftFactor q false true t else 1) *
           (if v ∈ G then pairRightFactor q false true t else 1))) +
      (1/2 : ℝ) * ((1-p) *
          ((if v = x then pairPivotFactor q true false else 1) *
           (if v ∈ F then pairLeftFactor q true false t else 1) *
           (if v ∈ G then pairRightFactor q true false t else 1)) + p *
          ((if v = x then pairPivotFactor q true true else 1) *
           (if v ∈ F then pairLeftFactor q true true t else 1) *
           (if v ∈ G then pairRightFactor q true true t else 1))) =
      (if v = x then p/2 else 1) *
        (if v ∈ F then (1+p*t)/2 else 1) * (if v ∈ G then (1-p*t)/2 else 1) := by
    by_cases hvx : v = x
    · subst v
      cases q <;> simp [hxF, hxG, pairPivotFactor] <;> ring
    · by_cases hvF : v ∈ F
      · have hvG : v ∉ G := fun h => Finset.disjoint_left.mp hFG hvF h
        cases q <;> simp [hvx, hvF, hvG, pairLeftFactor] <;> ring
      · by_cases hvG : v ∈ G <;> cases q <;>
          simp [hvx, hvF, hvG, pairRightFactor] <;> ring
  simp_rw [hfactor]
  simp only [Finset.prod_mul_distrib, Fintype.prod_ite_eq', Fintype.prod_ite_mem, Finset.prod_const]

lemma sampleProb_pairLocal_integral {n : ℕ} (F G : Finset (Fin n)) (x : Fin n)
    (hFG : Disjoint F G) (hxF : x ∉ F) (hxG : x ∉ G) (q : Bool) (p : ℝ) :
    sampleProb p (fun c b σ => pairLocalEvent F G x q c b σ) =
      ∫ t in (0 : ℝ)..1,
        (p/2) * ((1+p*t)/2)^F.card * ((1-p*t)/2)^G.card := by
  unfold sampleProb sampleExpect
  change bernoulliExpect (1/2 : ℝ) (fun c => bernoulliExpect p
    (fun b => permProb (pairLocalEvent F G x q c b))) = _
  simp_rw [permProb_pairLocal F G x hFG hxF hxG q]
  have hb (c : Fin n → Bool) := bernoulliExpect_intervalIntegral p
    (fun b t => pairIntegrand F G x q c b t) (pairIntegrand_continuous F G x q c)
  simp_rw [hb]
  rw [bernoulliExpect_intervalIntegral (1/2 : ℝ)
    (fun c t => bernoulliExpect p (fun b => pairIntegrand F G x q c b t))]
  · apply intervalIntegral.integral_congr
    intro t _
    exact pairIntegrand_average F G x hFG hxF hxG q p t
  · intro c
    exact continuous_bernoulliExpect p _ (pairIntegrand_continuous F G x q c)

lemma pairEvent_iff_local {n : ℕ} (f g : Finset (Fin n)) (x : Fin n)
    (hfg : f ∩ g = {x}) (q : Bool) (c b : Fin n → Bool) (σ : Equiv.Perm (Fin n)) :
    PairEvent f g c b σ q ↔ pairLocalEvent (f.erase x) (g.erase x) x q c b σ := by
  classical
  have hxf : x ∈ f := (Finset.mem_inter.mp (hfg.symm ▸ Finset.mem_singleton_self x)).1
  have hxg : x ∈ g := (Finset.mem_inter.mp (hfg.symm ▸ Finset.mem_singleton_self x)).2
  constructor
  · rintro ⟨y, hy, hby, hmono, hF, hG⟩
    have hyx : y = x := Finset.singleton_injective (hy.symm.trans hfg)
    subst y
    refine ⟨⟨hmono x hxg, hby, ?_, ?_⟩, ?_, ?_⟩
    · intro z hz hc
      exact (hF z hz hc).1
    · intro z hz
      exact hmono z (Finset.mem_of_mem_erase hz)
    · intro z hz
      obtain ⟨hz, hc⟩ := Finset.mem_filter.mp hz
      exact (hF z hz hc).2
    · intro z hz
      obtain ⟨hz, hb⟩ := Finset.mem_filter.mp hz
      exact hG z hz hb
  · rintro ⟨⟨hcx, hbx, hF, hG⟩, hbefore, hafter⟩
    refine ⟨x, hfg, hbx, ?_, ?_, ?_⟩
    · intro z hz
      by_cases hzx : z = x
      · simpa [hzx] using hcx
      · exact hG z (Finset.mem_erase.mpr ⟨hzx, hz⟩)
    · intro z hz hc
      exact ⟨hF z hz hc, hbefore z (Finset.mem_filter.mpr ⟨hz, hc⟩)⟩
    · intro z hz hb
      exact hafter z (Finset.mem_filter.mpr ⟨hz, hb⟩)

lemma sampleProb_pairLocal_eq_jk {n k : ℕ} (F G : Finset (Fin n)) (x : Fin n)
    (hFG : Disjoint F G) (hxF : x ∉ F) (hxG : x ∉ G)
    (hF : F.card = k-1) (hG : G.card = k-1) (hk : 1 ≤ k) (q : Bool) (p : ℝ) :
    sampleProb p (fun c b σ => pairLocalEvent F G x q c b σ) =
      jk k p / (2 : ℝ)^(2*k-1) := by
  rw [sampleProb_pairLocal_integral F G x hFG hxF hxG, hF, hG]
  have hpow : (2 : ℝ)^(2*k-1) = 2 * 2^(k-1) * 2^(k-1) := by
    rw [show 2*k-1 = (k-1)+(k-1)+1 by omega, pow_add, pow_add]
    ring
  have hf (t : ℝ) :
      (p/2) * ((1+p*t)/2)^(k-1) * ((1-p*t)/2)^(k-1) =
      (p / (2 : ℝ)^(2*k-1)) * ((1-p*t)^(k-1) * (1+p*t)^(k-1)) := by
    rw [div_pow, div_pow, hpow]
    field_simp
  simp_rw [hf]
  rw [intervalIntegral.integral_const_mul]
  calc
    _ = (p * (∫ t in (0 : ℝ)..1, (1-p*t)^(k-1) * (1+p*t)^(k-1))) /
        (2 : ℝ)^(2*k-1) := by ring
    _ = _ := by rw [jk_rescale]

/-- Exact probability of a genuine ordered single-intersection pair event,
for one specified final color. -/
theorem sampleProb_pairEvent_singleton {n k : ℕ} (f g : Finset (Fin n)) (x : Fin n)
    (hfg : f ∩ g = {x}) (hf : f.card = k) (hg : g.card = k) (hk : 1 ≤ k)
    (q : Bool) (p : ℝ) :
    sampleProb p (fun c b σ => PairEvent f g c b σ q) = jk k p / (2 : ℝ)^(2*k-1) := by
  classical
  have hxf : x ∈ f := (Finset.mem_inter.mp (hfg.symm ▸ Finset.mem_singleton_self x)).1
  have hxg : x ∈ g := (Finset.mem_inter.mp (hfg.symm ▸ Finset.mem_singleton_self x)).2
  have hFG : Disjoint (f.erase x) (g.erase x) := by
    apply Finset.disjoint_left.mpr
    intro z hzF hzG
    have hz : z ∈ f ∩ g := Finset.mem_inter.mpr
      ⟨Finset.mem_of_mem_erase hzF, Finset.mem_of_mem_erase hzG⟩
    have hzx : z = x := by simpa only [hfg, Finset.mem_singleton] using hz
    exact (Finset.mem_erase.mp hzF).1 hzx
  have heq : (fun c b σ => PairEvent f g c b σ q) =
      (fun c b σ => pairLocalEvent (f.erase x) (g.erase x) x q c b σ) := by
    funext c b σ
    exact propext (pairEvent_iff_local f g x hfg q c b σ)
  rw [heq]
  apply sampleProb_pairLocal_eq_jk _ _ _ hFG (Finset.notMem_erase _ _) (Finset.notMem_erase _ _)
    (by rw [Finset.card_erase_of_mem hxf, hf])
    (by rw [Finset.card_erase_of_mem hxg, hg]) hk

 theorem sampleProb_pairEvent {n k : ℕ} (f g : Finset (Fin n))
    (hfg : (f ∩ g).card = 1) (hf : f.card = k) (hg : g.card = k) (hk : 1 ≤ k)
    (q : Bool) (p : ℝ) :
    sampleProb p (fun c b σ => PairEvent f g c b σ q) = jk k p / (2 : ℝ)^(2*k-1) := by
  obtain ⟨x, hx⟩ := Finset.card_eq_one.mp hfg
  exact sampleProb_pairEvent_singleton f g x hx hf hg hk q p

 theorem sampleProb_pairEvent_eq_zero {n : ℕ} (f g : Finset (Fin n))
    (hfg : (f ∩ g).card ≠ 1) (q : Bool) (p : ℝ) :
    sampleProb p (fun c b σ => PairEvent f g c b σ q) = 0 := by
  have heq : (fun c b σ => PairEvent f g c b σ q) = (fun _ _ _ => False) := by
    funext c b σ
    apply propext
    constructor
    · rintro ⟨x, hx, _⟩
      exact hfg (by rw [hx]; simp)
    · exact False.elim
  rw [heq, sampleProb_false]

/-- The complete pair formula, including pairs which do not meet in one vertex. -/
theorem sampleProb_pairEvent_formula {n k : ℕ} (f g : Finset (Fin n))
    (hf : f.card = k) (hg : g.card = k) (hk : 1 ≤ k) (q : Bool) (p : ℝ) :
    sampleProb p (fun c b σ => PairEvent f g c b σ q) =
      if (f ∩ g).card = 1 then jk k p / (2 : ℝ)^(2*k-1) else 0 := by
  classical
  by_cases hfg : (f ∩ g).card = 1
  · rw [if_pos hfg]
    exact sampleProb_pairEvent f g hfg hf hg hk q p
  · rw [if_neg hfg]
    exact sampleProb_pairEvent_eq_zero f g hfg q p

end
end Aris4Math.General.RS
