import Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase

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
