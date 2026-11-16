import DegreeDiameter.Portfolio.H9CrossStar
import DegreeDiameter.Portfolio.F9Graph56862Field
import Mathlib.Data.Fintype.EquivFin

/-! Normalization for the actual a+3b, t²=-1 encoding used by H9.
The finite point/line certificate is separate from these algebraic proofs. -/
namespace DegreeDiameter.Portfolio.H9CrossNormalize
open H9CrossRouting H9CrossKernel H9CrossGeometry H9CrossStar
set_option maxRecDepth 20000
set_option maxHeartbeats 2000000

abbrev F9 := F9Graph56862.F

/-- The inverse table of the actual byte encoding, including inverse(0)=0. -/
def inverse : F9 → F9
  | .c0 => .c0 | .c1 => .c1 | .c2 => .c2
  | .c3 => .c6 | .c4 => .c5 | .c5 => .c4
  | .c6 => .c3 | .c7 => .c8 | .c8 => .c7

instance : Field F9 where
  __ := inferInstanceAs (CommRing F9)
  inv := inverse
  mul_inv_cancel := by decide +kernel
  inv_zero := rfl
  exists_pair_ne := ⟨.c0, .c1, by decide⟩
  nnqsmul := _
  qsmul := _

theorem field_card : Nat.card F9 = 9 := by
  rw [Nat.card_eq_fintype_card]
  decide +kernel

theorem field_char_three : (3 : F9) = 0 := by decide +kernel
theorem encoded_t_square : (F9Graph56862.F.c3 : F9) ^ 2 + 1 = 0 := by
  decide +kernel

/-- Exact byte-level addition used in the saved finite checker. -/
theorem encoded_add : ∀ a b : Fin 9,
    F9Graph56862.F.code (F9Graph56862.F.ofCode a.val + F9Graph56862.F.ofCode b.val) =
      (a.val % 3 + b.val % 3) % 3 + 3 * ((a.val / 3 + b.val / 3) % 3) := by
  decide +kernel

/-- Adding 9 before subtraction computes ac-bd modulo three in Nat. -/
theorem encoded_mul : ∀ a b : Fin 9,
    F9Graph56862.F.code (F9Graph56862.F.ofCode a.val * F9Graph56862.F.ofCode b.val) =
      ((a.val % 3 * (b.val % 3) + 9 - a.val / 3 * (b.val / 3)) % 3) +
        3 * ((a.val % 3 * (b.val / 3) + a.val / 3 * (b.val % 3)) % 3) := by
  decide +kernel

/-- First nonzero coordinate is one, exactly as in check.cpp::normalize. -/
def Normalized {K : Type*} [Field K] (p : Vec7 K) : Prop :=
  ∃ i : Fin 7, p i = 1 ∧ ∀ j : Fin 7, j < i → p j = 0

section General
variable {K : Type*} [Field K]

theorem normalized_ne_zero {p : Vec7 K} (hp : Normalized p) : p ≠ 0 := by
  obtain ⟨i, hi, _⟩ := hp
  intro hz
  have h := congrFun hz i
  rw [hi] at h
  exact one_ne_zero h

/-- Normalized representatives have no nontrivial scalar collisions. -/
theorem normalized_scalar_unique {p q : Vec7 K}
    (hp : Normalized p) (hq : Normalized q) {a b : K}
    (ha : a ≠ 0) (hb : b ≠ 0)
    (he : (fun i => a * p i) = (fun i => b * q i)) : p = q ∧ a = b := by
  obtain ⟨i, hi, hpi⟩ := hp
  obtain ⟨j, hj, hqj⟩ := hq
  have hij : i = j := by
    rcases lt_trichotomy i j with h | h | h
    · have he' := congrFun he i
      rw [hi, hqj i h, mul_one, mul_zero] at he'
      exact False.elim (ha he')
    · exact h
    · have he' := congrFun he j
      rw [hpi j h, hj, mul_zero, mul_one] at he'
      exact False.elim (hb he'.symm)
  subst j
  have hab : a = b := by simpa [hi, hj] using congrFun he i
  constructor
  · funext k
    apply mul_left_cancel₀ ha
    simpa [hab] using congrFun he k
  · exact hab

theorem scalar_ne_zero {p : Vec7 K} (hp : Normalized p) {a : K} (ha : a ≠ 0) :
    (fun i => a * p i) ≠ 0 := by
  obtain ⟨i, hi, _⟩ := hp
  intro hz
  have h := congrFun hz i
  apply ha
  simpa [hi] using h

def normalizeAt (p : Vec7 K) (i : Fin 7) : Vec7 K := fun j => (p i)⁻¹ * p j

theorem normalizeAt_normalized (p : Vec7 K) (i : Fin 7) (hi : p i ≠ 0)
    (hz : ∀ j : Fin 7, j < i → p j = 0) : Normalized (normalizeAt p i) := by
  refine ⟨i, ?_, ?_⟩
  · exact inv_mul_cancel₀ hi
  · intro j hj
    simp [normalizeAt, hz j hj]

theorem norm_scalar (p : Vec7 K) (a : K) :
    norm (fun i => a * p i) = a ^ 2 * norm p := by
  simp [norm]
  ring

theorem cross_scalar_closed {p q : Vec7 K} (hq : cross p q = 0) (a : K) :
    cross p (fun i => a * q i) = 0 := by
  rw [cross_right_scalar, hq]
  funext i
  simp

theorem norm_scalar_closed {q : Vec7 K} (hq : norm q = 0) (a : K) :
    norm (fun i => a * q i) = 0 := by rw [norm_scalar, hq, mul_zero]

/-- The saved full-span and basis checks imply cross-zero for any two
points on each actual line, including the center and every star point. -/
theorem cross_line_span (r w : Vec7 K) (hc : cross r w = 0) (a b c d : K) :
    cross (fun i => a * r i + b * w i) (fun i => c * r i + d * w i) = 0 := by
  have he : cross (fun i => a * r i + b * w i) (fun i => c * r i + d * w i) =
      fun i => (a * d - b * c) * cross r w i := by
    funext i
    fin_cases i <;> simp [cross] <;> ring
  rw [he, hc]
  funext i
  simp

/-- These are exactly the checked star fields; injection of 729 vectors is
proved below, rather than supplied as another certificate premise. -/
structure StarInput (p : Vec7 K) where
  point : Fin 91 → Vec7 K
  normalized : ∀ i, Normalized (point i)
  distinct : Function.Injective point
  null : ∀ i, norm (point i) = 0
  cross_zero : ∀ i, cross p (point i) = 0

abbrev StarDomain (K : Type*) [Field K] := Option (Fin 91 × {a : K // a ≠ 0})

def starVector {p : Vec7 K} (s : StarInput p) : StarDomain K → Kernel p
  | none => ⟨0, by funext i; fin_cases i <;> simp [cross]⟩
  | some (i, a) => ⟨fun j => a.val * s.point i j,
      cross_scalar_closed (s.cross_zero i) a.val⟩

theorem starVector_injective {p : Vec7 K} (s : StarInput p) :
    Function.Injective (starVector s) := by
  intro x y he
  have hv := congrArg Subtype.val he
  cases x with
  | none =>
    cases y with
    | none => rfl
    | some y =>
      exfalso
      exact scalar_ne_zero (s.normalized y.1) y.2.property hv.symm
  | some x =>
    cases y with
    | none =>
      exfalso
      exact scalar_ne_zero (s.normalized x.1) x.2.property hv
    | some y =>
      obtain ⟨hpq, hab⟩ := normalized_scalar_unique
        (s.normalized x.1) (s.normalized y.1) x.2.property y.2.property hv
      have hi := s.distinct hpq
      have ha : x.2 = y.2 := Subtype.ext hab
      exact congrArg some (Prod.ext hi ha)

end General

theorem nonzero_scalar_card : Fintype.card {a : F9 // a ≠ 0} = 8 := by
  decide +kernel

theorem starDomain_card : Fintype.card (StarDomain F9) = 729 := by
  simp only [StarDomain, Fintype.card_option, Fintype.card_prod,
    Fintype.card_fin, nonzero_scalar_card]

noncomputable def star729 {p : Vec7 F9} (s : StarInput p) : Fin 729 → Kernel p :=
  starVector s ∘ (Fintype.equivFinOfCardEq starDomain_card).symm

theorem star729_injective {p : Vec7 F9} (s : StarInput p) :
    Function.Injective (star729 s) :=
  (starVector_injective s).comp (Fintype.equivFinOfCardEq starDomain_card).symm.injective

/-- Actual order-nine field call: only the finite geometry input remains to
be imported; the 729 map, membership and injection are constructed here. -/
theorem star729_complete {p : Vec7 F9} (hp : p ≠ 0) (hn : norm p = 0)
    (s : StarInput p) : Function.Surjective (star729 s) :=
  star729_surjective field_card p hp hn (star729 s) (star729_injective s)


def actualPoint0 : Vec7 F9 := ![F9Graph56862.F.c1,F9Graph56862.F.c0,F9Graph56862.F.c0,F9Graph56862.F.c0,F9Graph56862.F.c0,F9Graph56862.F.c0,F9Graph56862.F.c0]

/-- The actual sorted union of the ten cached lines incident with point 0. -/
def actualStar0Point (i : Fin 91) : Vec7 F9 :=
  if i.val < 81 then
    ![1, 0, 0, 0, 0, F9Graph56862.F.ofCode (i.val / 9), F9Graph56862.F.ofCode (i.val % 9)]
  else if i.val < 90 then
    ![0, 0, 0, 0, 0, 1, F9Graph56862.F.ofCode (i.val - 81)]
  else ![0, 0, 0, 0, 0, 0, 1]

/-- A small left inverse replaces a quadratic pairwise equality check. -/
def actualStar0Index (q : Vec7 F9) : Nat :=
  if q 0 = 1 then 9 * F9Graph56862.F.code (q 5) + F9Graph56862.F.code (q 6)
  else if q 5 = 1 then 81 + F9Graph56862.F.code (q 6) else 90

theorem actualStar0_left_inverse :
    ∀ i : Fin 91, actualStar0Index (actualStar0Point i) = i.val := by decide +kernel

def actualStar0 : StarInput actualPoint0 where
  point := actualStar0Point
  normalized := by unfold Normalized; decide +kernel
  distinct := by
    intro i j he
    apply Fin.ext
    have h := congrArg actualStar0Index he
    simpa only [actualStar0_left_inverse] using h
  null := by decide +kernel
  cross_zero := by decide +kernel

theorem actualPoint0_nonzero : actualPoint0 ≠ 0 := by decide +kernel
theorem actualPoint0_null : norm actualPoint0 = 0 := by decide +kernel

/-- A real star extracted from the accepted binary input: no finite geometry
hypothesis, no rank premise, and no assumed 729-vector injection. -/
theorem actualStar0_729_complete : Function.Bijective (star729 actualStar0) := by
  exact ⟨star729_injective actualStar0,
    star729_complete actualPoint0_nonzero actualPoint0_null actualStar0⟩

end DegreeDiameter.Portfolio.H9CrossNormalize

#print axioms DegreeDiameter.Portfolio.H9CrossNormalize.normalized_scalar_unique
#print axioms DegreeDiameter.Portfolio.H9CrossNormalize.star729_complete

#print axioms DegreeDiameter.Portfolio.H9CrossNormalize.actualStar0_729_complete
