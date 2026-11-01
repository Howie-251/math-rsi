import Aris4Math.ThirtyThree.TripleProfiles
import Aris4Math.ProfileApplication
import Aris4Math.ThirtyThree.TwentyOneDeletion

/-! Two actual locks with arbitrary codegree, including zero singleton rows. -/

namespace Aris4Math.ThirtyFour.NineteenPairs

open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.ThirtyThree.DoubleLockAt Aris4Math.ThirtyThree.TripleProfiles

def rawPairProfile (v a b d e l : ℕ) (centers : List ℕ) : Numeric.Profile :=
  ⟨v,[a,b],[⟨[],34+l-d-e⟩,⟨[a],d-l⟩,⟨[b],e-l⟩,⟨[a,b],l⟩],none,centers⟩

def pairProfile (v a b d e l : ℕ) (centers : List ℕ) : Numeric.Profile :=
  pruneZero (rawPairProfile v a b d e l centers)

theorem two_counts_lambda {v : ℕ} (H : Simple5Hypergraph (Fin v))
    (edges34 : H.edges.card = 34) (x y : Fin v) :
    multiplicity H.edges (twoClass x y) [] = 34 + H.codegree x y - H.degree x - H.degree y ∧
    multiplicity H.edges (twoClass x y) [11] = H.degree x - H.codegree x y ∧
    multiplicity H.edges (twoClass x y) [12] = H.degree y - H.codegree x y ∧
    multiplicity H.edges (twoClass x y) [11,12] = H.codegree x y := by
  have hx := Finset.filter_card_add_filter_neg_card_eq_card
    (s := H.edges.filter (fun A => x ∈ A)) (fun A => y ∈ A)
  have hy := Finset.filter_card_add_filter_neg_card_eq_card
    (s := H.edges.filter (fun A => y ∈ A)) (fun A => x ∈ A)
  simp only [Finset.filter_filter] at hx hy
  have hpart := four_partition H.edges (fun A => x ∈ A) (fun A => y ∈ A)
  have hc : (H.edges.filter (fun A => x ∈ A ∧ y ∈ A)).card = H.codegree x y := rfl
  have hy1 : H.edges.filter (fun A => y ∈ A ∧ x ∈ A) = H.edges.filter (fun A => x ∈ A ∧ y ∈ A) := by
    ext A; simp [and_comm]
  have hy0 : H.edges.filter (fun A => y ∈ A ∧ x ∉ A) = H.edges.filter (fun A => x ∉ A ∧ y ∈ A) := by
    ext A; simp [and_comm]
  rw [hy1,hy0] at hy
  change _ + _ = H.degree x at hx
  change _ + _ = H.degree y at hy
  rw [edges34] at hpart
  have h0 := class_fiber H x y 0
  have h1 := class_fiber H x y 1
  have h2 := class_fiber H x y 2
  have h3 := class_fiber H x y 3
  simp only [Matrix.cons_val_zero,Matrix.cons_val_one,Matrix.cons_val_two,
    Matrix.cons_val_three,Matrix.head_cons,Matrix.tail_cons,decide_eq_true_eq] at h0 h1 h2 h3
  rw [h0,h1,h2,h3]
  omega

theorem realizes_pair_profile {v a b : ℕ} (H : Simple5Hypergraph (Fin v))
    (edges34 : H.edges.card = 34) (ha : 1 ≤ a) (hab : a < b) (hb : b ≤ v)
    (x y : Fin v) (hne : x ≠ y) (centers : List ℕ)
    (valid : Numeric.validProfile
      (pairProfile v a b (H.degree x) (H.degree y) (H.codegree x y) centers) 34) :
    RealizesProfile H (twoVertices x y hne) (positionsAt v a b ha hab hb)
      (pairProfile v a b (H.degree x) (H.degree y) (H.codegree x y) centers) 34 := by
  have habne : a ≠ b := ne_of_lt hab
  have ha1 : a-1+1 = a := by omega
  have hb1 : b-1+1 = b := by omega
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ ?_⟩
  · have hu : (Finset.univ : Finset (Fin 2)) = {0,1} := by decide
    simp [pairProfile,pruneZero,rawPairProfile,hu,positionsAt,ha1,hb1]
  · constructor
    · simp [rawPairProfile,habne]
    · intro A _
      rw [type_at]
      by_cases hx : x ∈ A <;> by_cases hy : y ∈ A <;>
        simp [rawPairProfile,classAt,hx,hy]
    · have heq : positionType (twoVertices x y hne) (positionsAt v a b ha hab hb) =
          classAt a b x y := funext (type_at ha hab hb x y hne)
      rw [heq]
      intro t ht
      simp only [rawPairProfile,List.mem_cons,List.not_mem_nil,or_false] at ht
      have counts := two_counts_lambda H edges34 x y
      have h0 := fiber_at_eq hab H x y 0
      have h1 := fiber_at_eq hab H x y 1
      have h2 := fiber_at_eq hab H x y 2
      have h3 := fiber_at_eq hab H x y 3
      simp only [Matrix.cons_val_zero,Matrix.cons_val_one,Matrix.cons_val_two,
        Matrix.cons_val_three,Matrix.head_cons,Matrix.tail_cons] at h0 h1 h2 h3
      rcases ht with rfl | rfl | rfl | rfl
      · exact h0.trans counts.1
      · exact h1.trans counts.2.1
      · exact h2.trans counts.2.2.1
      · exact h3.trans counts.2.2.2

/-- Degree and codegree data only, not an arbitrary hypergraph certificate. -/
structure PairCase where
  d : ℕ
  e : ℕ
  l : ℕ
  a : ℕ
  b : ℕ
  deriving DecidableEq

def highCases : List PairCase :=
  [⟨8,9,1,7,8⟩,⟨8,10,1,7,8⟩,
   ⟨8,8,3,1,11⟩,⟨8,8,4,1,11⟩,⟨8,8,5,1,11⟩,
   ⟨8,8,6,1,11⟩,⟨8,8,7,1,11⟩,⟨8,8,8,1,11⟩]

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem high_certificates : ∀ c ∈ highCases,
    1 ≤ c.a ∧ c.a < c.b ∧ c.b ≤ 19 ∧
    Numeric.validProfile (pairProfile 19 c.a c.b c.d c.e c.l []) 34 ∧
    Numeric.totalBound (pairProfile 19 c.a c.b c.d c.e c.l []) < 1 := by
  unfold Numeric.validProfile
  decide +kernel

/-- High codegree is handled directly by the uncorrected real profile. -/
theorem propertyB_of_high_pair (H : Simple5Hypergraph (Fin 19))
    (edges34 : H.edges.card = 34) (x y : Fin 19) (hne : x ≠ y)
    (c : PairCase) (hc : c ∈ highCases)
    (dx : H.degree x = c.d) (dy : H.degree y = c.e) (hl : H.codegree x y = c.l) :
    PropertyB H := by
  obtain ⟨ha,hab,hb,hvalid,hstrict⟩ := high_certificates c hc
  have hvalid' : Numeric.validProfile
      (pairProfile 19 c.a c.b (H.degree x) (H.degree y) (H.codegree x y) []) 34 := by
    simpa only [dx,dy,hl] using hvalid
  have real := realizes_pair_profile H edges34 ha hab hb x y hne [] hvalid'
  rw [dx,dy,hl] at real
  exact ProfileApplication.propertyB_of_uncorrected_profile H
    (twoVertices x y hne) (positionsAt 19 c.a c.b ha hab hb)
    (pairProfile 19 c.a c.b c.d c.e c.l []) real rfl rfl hstrict


end Aris4Math.ThirtyFour.NineteenPairs
#print axioms Aris4Math.ThirtyFour.NineteenPairs.propertyB_of_high_pair
