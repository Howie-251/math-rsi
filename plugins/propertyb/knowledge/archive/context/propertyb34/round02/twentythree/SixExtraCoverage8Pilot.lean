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
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def pilotRows : List (List ℕ × (Degree → Witness)) := [
([0,0,0,0,0,0,0,0,0,0,0],![(17,100),(17,100)]),
([0,0,0,0,0,0,0,0,0,0,1],![(13,0),(13,0)]),
([0,0,0,0,0,0,0,0,0,1,0],![(11,100),(11,100)]),
([0,0,0,0,0,0,0,0,1,0,0],![(11,104),(11,104)]),
([0,0,0,0,0,0,0,1,0,0,0],![(11,110),(11,110)]),
([0,0,0,0,0,0,1,0,0,0,0],![(11,121),(11,121)]),
([0,0,0,0,0,0,1,0,1,0,0],![(7,51),(7,51)]),
([0,0,0,0,0,0,1,1,0,0,0],![(7,73),(7,73)])
]
theorem pilot : pilotRows.all (fun r => decide (∀ d : Degree, Matched d (some 0) r.1 (r.2 d)))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
