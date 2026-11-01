import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraSelection
import Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase
import Aris4Math.ThirtyFour.TwentyFourPermutation

/-! Recover singleton promotions from exact new/old codegrees. This reduces
an extension catalogue to old traces of size at least two. -/
namespace Aris4Math.ThirtyFour.TwentyThreeHighPromotion
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LockExtension PromotionCatalog PromotionReconstruction
variable {n v : ℕ}

def higher (p : Finset (Fin n) → ℕ) (i : Fin n) : ℕ :=
  ∑ U ∈ supers {i} 2, p U

def complete (p : Finset (Fin n) → ℕ) (lam : Fin n → ℕ)
    (T : Finset (Fin n)) : ℕ :=
  if 2≤T.card then p T else ∑ i∈T, (lam i-higher p i)

theorem promotion_singleton_add_higher (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (i : Fin n) :
    promotion H f {i}+higher (promotion H f) i =
      H.codegree (f i.castSucc) (f (Fin.last n)) := by
  have family : Finset.univ.filter (fun T : Finset (Fin n) => i∈T)=
      insert {i} (supers {i} 2) := by
    ext T
    simp only [Finset.mem_filter,Finset.mem_univ,true_and,Finset.mem_insert,
      supers,Finset.singleton_subset_iff]
    constructor
    · intro present
      by_cases same : T={i}
      · exact Or.inl same
      · right
        have small : 2≤T.card := by
          have positive := Finset.card_pos.mpr ⟨i,present⟩
          by_contra bad
          have one : T.card=1 := by omega
          obtain ⟨j,hj⟩ := Finset.card_eq_one.mp one
          have equal : i=j := by simpa [hj] using present
          exact same (by simpa [equal] using hj)
        exact ⟨present,small⟩
    · rintro (rfl | h)
      · simp
      · exact h.1
  have absent : ({i} : Finset (Fin n))∉supers {i} 2 := by simp [supers]
  have total := sum_promotion_codegree H f i
  rw [← Finset.sum_filter,family,Finset.sum_insert absent] at total
  exact total

/-- No singleton promotion is an independent catalogue variable once all
higher promotions and new/old codegrees are known. -/
theorem complete_actual (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (p : Finset (Fin n) → ℕ) (lam : Fin n → ℕ)
    (high : ∀ T, 2≤T.card → p T=promotion H f T)
    (pairs : ∀ i, lam i=H.codegree (f i.castSucc) (f (Fin.last n)))
    (T : Finset (Fin n)) (nonempty : T≠∅) : complete p lam T=promotion H f T := by
  by_cases large : 2≤T.card
  · rw [complete,if_pos large]
    exact high T large
  have one : T.card=1 := by
    have positive := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr nonempty)
    omega
  obtain ⟨i,rfl⟩ := Finset.card_eq_one.mp one
  have higher_eq : higher p i=higher (promotion H f) i := by
    apply Finset.sum_congr rfl
    intro U hU
    exact high U (Finset.mem_filter.mp hU).2.2
  have sum := promotion_singleton_add_higher H f i
  simp only [complete,Finset.card_singleton,show ¬2≤(1:ℕ) by omega,if_false,
    Finset.sum_singleton,higher_eq,pairs]
  omega

theorem extend_actual_of_high (H : Simple5Hypergraph (Fin v))
    (f : Fin (n+1) ↪ Fin v) (mu p : Finset (Fin n) → ℕ) (lam : Fin n → ℕ) (d : ℕ)
    (old : ∀ T, count H (restrict f) T=mu T)
    (high : ∀ T, 2≤T.card → p T=promotion H f T)
    (pairs : ∀ i, lam i=H.codegree (f i.castSucc) (f (Fin.last n)))
    (degree : H.degree (f (Fin.last n))=d) (T : Finset (Fin (n+1))) :
    count H f T=extend mu (complete p lam) d T :=
  extend_actual H f mu (complete p lam) d old
    (complete_actual H f p lam high pairs) degree T

def oneDouble (b : Option (Fin n)) (i : Fin n) : ℕ := if b=some i then 2 else 1

/-- A positive integer vector with total excess at most one is all ones,
or has one specified entry equal to two. -/
theorem exists_oneDouble (lam : Fin n → ℕ) (positive : ∀ i, 1≤lam i)
    (budget : (∑ i, (lam i-1))≤1) : ∃ b : Option (Fin n), ∀ i, lam i=oneDouble b i := by
  classical
  by_cases allOne : ∀ i, lam i=1
  · exact ⟨none,by simpa [oneDouble] using allOne⟩
  obtain ⟨i,notOne⟩ := not_forall.mp allOne
  let ex : Fin n → ℕ := fun j => lam j-1
  have lower : 1≤ex i := by dsimp [ex];have := positive i;omega
  have total := Finset.sum_erase_add (s := Finset.univ) ex (Finset.mem_univ i)
  have eraseZero : (∑ j ∈ Finset.univ.erase i, ex j)=0 := by
    change (∑ j,ex j)≤1 at budget
    omega
  have value : lam i=2 := by
    have := Finset.single_le_sum (fun j (_ : j∈(Finset.univ : Finset (Fin n))) => Nat.zero_le (ex j)) (Finset.mem_univ i)
    dsimp [ex] at *
    have := positive i
    omega
  refine ⟨some i,?_⟩
  intro j
  by_cases same : j=i
  · subst j;simp [oneDouble,value]
  · have zero : ex j=0 := by
      have mem : j∈(Finset.univ : Finset (Fin n)).erase i := by simp [same]
      have h := Finset.single_le_sum (fun k (_ : k∈(Finset.univ : Finset (Fin n)).erase i) => Nat.zero_le (ex k)) mem
      rw [eraseZero] at h
      omega
    have val : lam j=1 := by have := positive j;dsimp [ex] at zero;omega
    simp [oneDouble,show i≠j from Ne.symm same,val]

end Aris4Math.ThirtyFour.TwentyThreeHighPromotion
#print axioms Aris4Math.ThirtyFour.TwentyThreeHighPromotion.complete_actual
#print axioms Aris4Math.ThirtyFour.TwentyThreeHighPromotion.extend_actual_of_high

/-! Exact recovery of a sparse higher-promotion inventory. Finite formulas
sum over actual possible traces rather than the full Boolean algebra. -/
namespace Aris4Math.ThirtyFour.TwentyThreeSparsePromotion
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyThreeHighPromotion PromotionReconstruction
variable {n : ℕ}

theorem decode_zero_of_not_mem {α : Type*} [DecidableEq α]
    (entries : List (α×ℕ)) (values : List ℕ) (x : α)
    (absent : x∉entries.map Prod.fst) : BoundedAllocations.decode entries values x=0 := by
  induction entries generalizing values with
  | nil => simp [BoundedAllocations.decode]
  | cons e es ih =>
    cases values with
    | nil => rfl
    | cons k ks =>
      have noHead : x≠e.1 := by
        intro eq
        exact absent (by simp [eq])
      have noTail : x∉es.map Prod.fst := by
        intro present
        exact absent (by simp [present])
      simp only [BoundedAllocations.decode,if_neg noHead]
      exact ih ks noTail

def higherSparse (S : Finset (Finset (Fin n))) (p : Finset (Fin n)→ℕ) (i : Fin n) :=
  ∑ T∈S, if i∈T then p T else 0

theorem higherSparse_eq (S : Finset (Finset (Fin n))) (p : Finset (Fin n)→ℕ)
    (large : ∀ T∈S, 2≤T.card) (support : ∀ T, T∉S → p T=0) (i : Fin n) :
    higherSparse S p i=higher p i := by
  unfold higherSparse higher
  simp only [supers,Finset.singleton_subset_iff,Finset.sum_filter]
  calc
    (∑ T∈S, if i∈T then p T else 0) =
        ∑ T∈S, if i∈T ∧ 2≤T.card then p T else 0 := by
      apply Finset.sum_congr rfl
      intro T hT
      simp [large T hT]
    _ = _ := by
      apply Finset.sum_subset (Finset.subset_univ S)
      intro T _ absent
      simp [support T absent]

def fullSupport (S : Finset (Finset (Fin n))) :=
  S ∪ Finset.univ.image (fun i : Fin n => ({i} : Finset (Fin n)))

def completeSparse (S : Finset (Finset (Fin n))) (p : Finset (Fin n)→ℕ)
    (lam : Fin n→ℕ) (T : Finset (Fin n)) :=
  if 2≤T.card then p T else ∑ i∈T, (lam i-higherSparse S p i)

theorem completeSparse_eq (S : Finset (Finset (Fin n))) (p : Finset (Fin n)→ℕ)
    (lam : Fin n→ℕ) (large : ∀ T∈S, 2≤T.card) (support : ∀ T, T∉S → p T=0) :
    completeSparse S p lam=complete p lam := by
  funext T
  simp only [completeSparse,complete,higherSparse_eq S p large support]

theorem sum_complete_support (S : Finset (Finset (Fin n))) (p : Finset (Fin n)→ℕ)
    (lam : Fin n→ℕ) (large : ∀ T∈S, 2≤T.card) (support : ∀ T, T∉S → p T=0) :
    (∑ T∈fullSupport S, complete p lam T)=
      ∑ T∈(Finset.univ : Finset (Finset (Fin n))).erase ∅, complete p lam T := by
  apply Finset.sum_subset
  · intro T hT
    have nonempty : T≠∅ := by
      rcases Finset.mem_union.mp hT with high | single
      · have h := large T high
        intro eq
        simp [eq] at h
      · obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp single
        simp
    simp [nonempty]
  · intro T hT absent
    have noHigh : T∉S := fun h => absent (Finset.mem_union_left _ h)
    have two : 2≤T.card := by
      have nonempty := (Finset.mem_erase.mp hT).1
      have pos := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr nonempty)
      by_contra small
      have one : T.card=1 := by omega
      obtain ⟨i,rfl⟩ := Finset.card_eq_one.mp one
      exact absent (Finset.mem_union_right _ (Finset.mem_image.mpr ⟨i,Finset.mem_univ _,rfl⟩))
    simp [complete,two,support T noHigh]

def fillSparse (S : Finset (Finset (Fin n))) (p : Finset (Fin n)→ℕ)
    (lam : Fin n→ℕ) (d : ℕ) (T : Finset (Fin n)) :=
  if T=∅ then d-∑ U∈fullSupport S, completeSparse S p lam U
  else completeSparse S p lam T

def extendSparse (S : Finset (Finset (Fin n))) (mu p : Finset (Fin n)→ℕ)
    (lam : Fin n→ℕ) (d : ℕ) (T : Finset (Fin (n+1))) :=
  if Fin.last n∈T then fillSparse S p lam d (oldTrace T)
  else mu (oldTrace T)-fillSparse S p lam d (oldTrace T)

theorem extendSparse_eq (S : Finset (Finset (Fin n))) (mu p : Finset (Fin n)→ℕ)
    (lam : Fin n→ℕ) (d : ℕ) (large : ∀ T∈S, 2≤T.card)
    (support : ∀ T, T∉S → p T=0) :
    extendSparse S mu p lam d=extend mu (complete p lam) d := by
  funext T
  simp only [extendSparse,extend,fillSparse,fillEmpty,
    completeSparse_eq S p lam large support,sum_complete_support S p lam large support]

end Aris4Math.ThirtyFour.TwentyThreeSparsePromotion
#print axioms Aris4Math.ThirtyFour.TwentyThreeSparsePromotion.extendSparse_eq
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowClassified
abbrev Residue := Fin 1
def residualCounts (r : Residue) : Finset (Fin 6) → ℕ := (fun T => if T=∅ then 11 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else 0)
end Aris4Math.ThirtyFour.TwentyThreeSixLowClassified

namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
open scoped BigOperators
open LockExtension PromotionReconstruction TwentyThreeHighPromotion TwentyThreeSparsePromotion
abbrev Degree := Fin 2
abbrev NewCase := Fin 18
abbrev Pattern := Option (Fin 6)
abbrev PermIndex := Fin 137
def degree (d : Degree) : ℕ := 7+d.val
def oldCounts := TwentyThreeSixLowClassified.residualCounts 0
def μ : Degree → NewCase → Finset (Fin 7) → ℕ := ![![(fun T => if T=∅ then 6 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 5 else if T={1,2,3,6} then 1 else if T={0,4,5,6} then 1 else 0),(fun T => if T=∅ then 7 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 4 else if T={0,6} then 1 else if T={1,2,3,6} then 1 else if T={0,4,5,6} then 1 else 0),(fun T => if T=∅ then 7 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={2,3,6} then 1 else if T={1,4,6} then 1 else if T={0,5,6} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={1,4,6} then 1 else if T={0,5,6} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={3,4,6} then 1 else if T={1,5,6} then 1 else if T={2,5,6} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,4,6} then 1 else if T={4,5,6} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={2,5,6} then 1 else 0),(fun T => if T=∅ then 9 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 2 else 0),(fun T => if T=∅ then 9 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={2,5,6} then 1 else 0),(fun T => if T=∅ then 9 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={3,5,6} then 1 else 0),(fun T => if T=∅ then 9 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,5,6} then 1 else 0),(fun T => if T=∅ then 10 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 2 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,5,6} then 1 else 0),(fun T => if T=∅ then 9 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={0,4,5,6} then 1 else 0),(fun T => if T=∅ then 10 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={3,5,6} then 1 else 0),(fun T => if T=∅ then 9 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,4,6} then 1 else if T={5,6} then 2 else 0),(fun T => if T=∅ then 10 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else 0),(fun T => if T=∅ then 11 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 2 else 0)],![(fun T => if T=∅ then 5 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 6 else if T={1,2,3,6} then 1 else if T={0,4,5,6} then 1 else 0),(fun T => if T=∅ then 6 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 5 else if T={0,6} then 1 else if T={1,2,3,6} then 1 else if T={0,4,5,6} then 1 else 0),(fun T => if T=∅ then 6 else if T={0} then 2 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 5 else if T={2,3,6} then 1 else if T={1,4,6} then 1 else if T={0,5,6} then 1 else 0),(fun T => if T=∅ then 7 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={1,4,6} then 1 else if T={0,5,6} then 1 else 0),(fun T => if T=∅ then 7 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 4 else if T={0,6} then 1 else if T={3,4,6} then 1 else if T={1,5,6} then 1 else if T={2,5,6} then 1 else 0),(fun T => if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 4 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,4,6} then 1 else if T={4,5,6} then 1 else 0),(fun T => if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 4 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={2,5,6} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 2 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={2,5,6} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={3,5,6} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,5,6} then 1 else 0),(fun T => if T=∅ then 9 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 2 else 0),(fun T => if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 4 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,5,6} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={0,4,5,6} then 1 else 0),(fun T => if T=∅ then 9 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={3,5,6} then 1 else 0),(fun T => if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,4,6} then 1 else if T={5,6} then 2 else 0),(fun T => if T=∅ then 9 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else 0),(fun T => if T=∅ then 10 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 2 else 0)]]
def entries : List (Finset (Fin 6) × ℕ) := [({0,1},1),({0,2},1),({0,3},1),({1,2,3},1),({1,4},1),({2,4},1),({3,4},1),({1,5},1),({2,5},1),({3,5},1),({0,4,5},1)]
def permCode : PermIndex → Fin 720 := ![0,360,120,600,480,240,30,390,180,690,540,330,6,366,42,402,198,714,558,354,36,396,12,372,156,66,18,672,516,426,378,151,61,301,571,511,421,661,211,608,248,45,322,698,338,592,308,578,675,225,292,539,112,449,668,218,315,585,163,79,319,595,523,439,679,235,626,266,328,260,506,291,537,227,448,113,620,146,651,177,73,169,589,325,433,529,229,685,350,566,111,447,677,293,710,206,471,87,603,4,365,244,693,34,395,334,10,371,717,46,407,358,40,401,16,377,521,431,383,243,364,5,604,333,394,35,694,370,11,357,406,47,718,400,41,376,17]
def oldPerm (p : PermIndex) : Equiv.Perm (Fin 6) := TwentyFourPermutation.perm (permCode p)
noncomputable def newPerm (p : PermIndex) : Equiv.Perm (Fin 7) := LockLiftRelabel.lift (oldPerm p)
def cost (T : Finset (Fin 6)) (i : Fin 6) : ℕ := if i∈T then 1 else 0
def catalogue (b : Pattern) := BoundedAllocations.enumerate cost entries (oneDouble b)
def vector (values : List ℕ) := BoundedAllocations.decode entries values
def highSupport : Finset (Finset (Fin 6)) := (entries.map Prod.fst).toFinset
theorem highSupport_large : ∀ T∈highSupport, 2≤T.card := by decide +kernel
theorem vector_support (values : List ℕ) (T : Finset (Fin 6)) (absent : T∉highSupport) : vector values T=0 := by
  apply decode_zero_of_not_mem
  simpa only [highSupport,List.mem_toFinset] using absent
def newCounts (d : Degree) (b : Pattern) (values : List ℕ) :=
  extendSparse highSupport oldCounts (vector values) (oneDouble b) (degree d)
theorem newCounts_eq (d : Degree) (b : Pattern) (values : List ℕ) :
    newCounts d b values=extend oldCounts (complete (vector values) (oneDouble b)) (degree d) :=
  extendSparse_eq highSupport oldCounts (vector values) (oneDouble b) (degree d)
    highSupport_large (vector_support values)
abbrev Witness := NewCase × PermIndex
def Matched (d : Degree) (b : Pattern) (values : List ℕ) (w : Witness) : Prop :=
  ∀ T, newCounts d b values (T.map (newPerm w.2).toEmbedding)=μ d w.1 T
noncomputable instance (d b values w) : Decidable (Matched d b values w) := by
  unfold Matched
  infer_instance
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LockExtension PromotionCatalog PromotionReconstruction TwentyThreeHighPromotion
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem entries_distinct : (entries.map Prod.fst).Nodup := by decide +kernel

theorem entries_values : ∀ e∈entries, e.2=oldCounts e.1 := by decide +kernel

theorem entries_high_support : ∀ T : Finset (Fin 6),
    2≤T.card → T∉entries.map Prod.fst → oldCounts T=0 := by decide +kernel

variable (checkedCoverage : ∀ b values, values∈catalogue b → ∀ d, (b=none ∨ b=some 0) → ∃ w : Witness, Matched d b values w)
include checkedCoverage

/-- The seven-lock input is fully determined by the exact higher promotions.
Neither singleton nor empty promotions are free catalogue variables. -/
theorem actual_normalized_extension (H : Simple5Hypergraph (Fin 23)) (f : Fin 7↪Fin 23)
    (d : Degree) (b : Pattern) (normalized : b=none ∨ b=some 0)
    (old : ∀ T, count H (restrict f) T=oldCounts T)
    (pairs : ∀ i, oneDouble b i=H.codegree (f i.castSucc) (f (Fin.last 6)))
    (newDegree : H.degree (f (Fin.last 6))=degree d) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 7),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ d q T := by
  let values := entries.map (fun e => promotion H f e.1)
  have member : values∈catalogue b := by
    apply BoundedAllocations.mem_enumerate cost entries (oneDouble b) (promotion H f)
    · intro e he
      have bound := promotion_le_old H f e.1
      rw [old,← entries_values e he] at bound
      exact bound
    · intro i
      have bound := listed_budget H f entries entries_distinct (some i)
      rw [pairs i]
      simpa only [cost,PromotionCatalog.cost,actualCap] using bound
  have high (T : Finset (Fin 6)) (large : 2≤T.card) :
      vector values T=promotion H f T := by
    change BoundedAllocations.decode entries (entries.map (fun e => promotion H f e.1)) T=_
    rw [BoundedAllocations.decode_map]
    by_cases present : T∈entries.map Prod.fst
    · rw [if_pos present]
    · rw [if_neg present]
      have bound := promotion_le_old H f T
      rw [old,entries_high_support T large present] at bound
      omega
  have actual (T : Finset (Fin 7)) : count H f T=newCounts d b values T := by
    rw [newCounts_eq]
    exact extend_actual_of_high H f oldCounts (vector values) (oneDouble b) (degree d)
      old high pairs newDegree T
  obtain ⟨w,matched⟩ := checkedCoverage b values member d normalized
  refine ⟨w.1,newPerm w.2,?_⟩
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched T

/-- Six transitive automorphisms of the actual residual inventory. -/
def normalizer (i : Fin 6) : Equiv.Perm (Fin 6) :=
  TwentyFourPermutation.perm (![0,301,260,111,4,5] i)

omit checkedCoverage in
theorem normalizer_preserves : ∀ i : Fin 6, ∀ T : Finset (Fin 6),
    oldCounts (T.map (normalizer i).toEmbedding)=oldCounts T := by decide +kernel

omit checkedCoverage in
theorem normalizer_pairs : ∀ i j : Fin 6,
    oneDouble (some i) (normalizer i j)=oneDouble (some 0) j := by decide +kernel

/-- Normalize the only possible double-codegree position by an old-inventory
automorphism. The seventh vertex and its degree remain literally fixed. -/
theorem actual_extension (H : Simple5Hypergraph (Fin 23)) (f : Fin 7↪Fin 23)
    (d : Degree) (b : Pattern)
    (old : ∀ T, count H (restrict f) T=oldCounts T)
    (pairs : ∀ i, oneDouble b i=H.codegree (f i.castSucc) (f (Fin.last 6)))
    (newDegree : H.degree (f (Fin.last 6))=degree d) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 7),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ d q T := by
  cases b with
  | none => exact actual_normalized_extension checkedCoverage H f d none (Or.inl rfl) old pairs newDegree
  | some i =>
    let ρ := LockLiftRelabel.lift (normalizer i)
    let g := ρ.toEmbedding.trans f
    have oldg (T : Finset (Fin 6)) : count H (restrict g) T=oldCounts T := by
      rw [LockLiftRelabel.restrict_lift_trans,LockRelabel.count_comp_perm,old,normalizer_preserves]
    have pairsg (j : Fin 6) : oneDouble (some 0) j=H.codegree (g j.castSucc) (g (Fin.last 6)) := by
      change oneDouble (some 0) j=H.codegree (f (ρ j.castSucc)) (f (ρ (Fin.last 6)))
      rw [LockLiftRelabel.lift_castSucc,LockLiftRelabel.lift_last,← pairs]
      exact (normalizer_pairs i j).symm
    have deg : H.degree (g (Fin.last 6))=degree d := by
      simpa only [g,LockLiftRelabel.new_vertex_lift_trans] using newDegree
    obtain ⟨q,τ,profile⟩ := actual_normalized_extension checkedCoverage H g d (some 0) (Or.inr rfl) oldg pairsg deg
    exact ⟨q,τ.trans ρ,profile⟩

end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
#print axioms Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue.actual_extension

namespace Aris4Math.ThirtyFour.TwentyThreeExactlySixLowComplete
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open TwentyThreeHighPromotion
open TwentyThreeSixLowExtraCatalogue

variable
  (checkedCoverage : ∀ b values, values∈catalogue b → ∀ d, (b=none ∨ b=some 0) → ∃ w : Witness, Matched d b values w)
  (classify : ∀ (H : Simple5Hypergraph (Fin 23)), H.PairCovering → H.edges.card=34 →
    ∀ f : Fin 6↪Fin 23, (∀ i, H.degree (f i)=6) → ¬PropertyB H →
    ∃ r : TwentyThreeSixLowClassified.Residue, ∃ σ : Equiv.Perm (Fin 6),
      ∀ T, count H (σ.toEmbedding.trans f) T=TwentyThreeSixLowClassified.residualCounts r T)
  (closeProfile : ∀ (H : Simple5Hypergraph (Fin 23)) (f : Fin 7↪Fin 23)
    (d : Degree) (q : NewCase), (∀ T, count H f T=μ d q T) → PropertyB H)
include checkedCoverage classify closeProfile

/-- The exact-six branch starts with the original hypergraph; both the
six-lock residual and all seven-lock representatives are derived internally. -/
theorem propertyB (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (six : H.sixVertices.card=6) : PropertyB H := by
  classical
  by_contra notB
  let e : ↥H.sixVertices ≃ Fin 6 := Fintype.equivFinOfCardEq (by simpa using six)
  let f : Fin 6↪Fin 23 :=
    ⟨fun i => (e.symm i).val, Subtype.val_injective.comp e.symm.injective⟩
  have low (i : Fin 6) : H.degree (f i)=6 :=
    (Finset.mem_filter.mp (e.symm i).property).2
  obtain ⟨r,σ,actual⟩ := classify H cover edges f low notB
  have only : r=0 := Subsingleton.elim _ _
  subst r
  let g := σ.toEmbedding.trans f
  have gLow (i : Fin 6) : H.degree (g i)=6 := low (σ i)
  obtain ⟨z,zd,outside,budget⟩ :=
    TwentyThreeSixLowExtraSelection.exists_seventh H cover edges six g gLow
  have absent : z∉Set.range g := by
    rintro ⟨i,hi⟩
    exact outside i hi
  let h : Fin 7↪Fin 23 := ⟨Fin.snoc g z, Fin.snoc_injective_of_injective g.injective absent⟩
  have restrict_eq : LockExtension.restrict h=g := by
    ext i
    simp [LockExtension.restrict,h]
  have hlast : h (Fin.last 6)=z := @Fin.snoc_last 6 (fun _ => Fin 23) z g
  have hcast (i : Fin 6) : h i.castSucc=g i := by simp [h]
  have positive (i : Fin 6) : 1≤H.codegree (g i) z := H.one_le_codegree cover (outside i)
  obtain ⟨b,hb⟩ := exists_oneDouble (fun i => H.codegree (g i) z) positive budget
  have pairValues (i : Fin 6) : oneDouble b i=H.codegree (h i.castSucc) (h (Fin.last 6)) := by
    rw [hcast,hlast]
    exact (hb i).symm
  have old : ∀ T, count H (LockExtension.restrict h) T=oldCounts T := by
    rw [restrict_eq]
    exact actual
  have someDegree : ∃ d : Degree, H.degree (h (Fin.last 6))=degree d := by
    rcases zd with seven | eight
    · exact ⟨0,by simpa [hlast,degree] using seven⟩
    · exact ⟨1,by simpa [hlast,degree] using eight⟩
  obtain ⟨d,degree_eq⟩ := someDegree
  obtain ⟨q,τ,profile⟩ := actual_extension checkedCoverage H h d b old pairValues degree_eq
  exact notB (closeProfile H (τ.toEmbedding.trans h) d q profile)

end Aris4Math.ThirtyFour.TwentyThreeExactlySixLowComplete
#print axioms Aris4Math.ThirtyFour.TwentyThreeExactlySixLowComplete.propertyB