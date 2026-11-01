import Aris4Math.ThirtyFour.TwentyThreeHighPromotion

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
