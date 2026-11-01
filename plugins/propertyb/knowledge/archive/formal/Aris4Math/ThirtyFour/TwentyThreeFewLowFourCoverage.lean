import Aris4Math.ThirtyFour.TwentyThreeFewLowFourNumeric
namespace Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.LockExtension
open Aris4Math.ThirtyFour.PromotionCatalog
open Aris4Math.ThirtyFour.PromotionReconstruction
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 1000

namespace OneLow
open TwentyThreeFewLowBase (Case oneLow)
theorem entries_distinct : ∀ c, ((entries c).map Prod.fst).Nodup := by decide +kernel
theorem entries_values (c : Case) (e : Finset (Fin 3) × ℕ) (mem : e∈entries c) : e.2=oneLow c e.1 := by
  have h : ∀ c, (entries c).all (fun e => decide (e.2=oneLow c e.1))=true := by decide +kernel
  exact of_decide_eq_true (List.all_eq_true.mp (h c) e mem)
theorem entries_support : ∀ c, ∀ T : Finset (Fin 3),
  T≠∅ → T∉(entries c).map Prod.fst → oneLow c T=0 := by decide +kernel

attribute [local irreducible] covered

/-- Match an abstract promotion vector before inserting the actual H counts. -/
theorem actual_of_covered (H : Simple5Hypergraph (Fin 23)) (f : Fin 4 ↪ Fin 23)
    (c : Case) (values : List ℕ) (matched : covered c values)
    (pos : positive c values) (actual : ∀ T, count H f T=newCounts c values T) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 4),
      (∀ i, (σ i).val<1 ↔ i.val<1) ∧
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  unfold covered at matched
  let chosen := choose (code c values)
  refine ⟨chosen.1,perm chosen.2,perm_preserves_roles chosen.2,?_⟩
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched pos T

theorem actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (f : Fin 4 ↪ Fin 23) (c : Case)
    (old : ∀ T, count H (restrict f) T=oneLow c T)
    (degree : H.degree (f 3)=7)
    (pairs : ∀ i : Fin 3, H.codegree (f i.castSucc) (f 3)≤cap (some i)) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 4),
      (∀ i, (σ i).val<1 ↔ i.val<1) ∧
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  let values := (entries c).map (fun e => promotion H f e.1)
  have capacity (j : Option (Fin 3)) : actualCap H f j≤cap j := by
    cases j with
    | none => simpa [actualCap,cap] using degree.le
    | some i => exact pairs i
  have member : values∈catalogue c := by
    apply actual_mem_of_old H f (entries c) cap (entries_distinct c) ?_ capacity
    intro e he
    rw [old,entries_values c e he]
  have prom (T : Finset (Fin 3)) (ne : T≠∅) : vector c values T=promotion H f T := by
    apply decode_nonempty H f (entries c) ?_ T ne
    intro S nonempty absent
    have bound := promotion_le_old H f S
    rw [old,entries_support c S nonempty absent] at bound
    omega
  have pos : positive c values := by
    intro i
    have eq : (∑ T : Finset (Fin 3), if i∈T then vector c values T else 0) =
        ∑ T : Finset (Fin 3), if i∈T then promotion H f T else 0 := by
      apply Finset.sum_congr rfl
      intro T _
      by_cases hi : i∈T
      · rw [if_pos hi,if_pos hi,prom T (by intro empty; simpa [empty] using hi)]
      · simp [hi]
    rw [eq,sum_promotion_codegree]
    exact H.one_le_codegree cover (f.injective.ne (Fin.castSucc_ne_last i))
  have eq (T : Finset (Fin 4)) : count H f T=newCounts c values T :=
    extend_actual H f (oneLow c) (vector c values) 7 old prom degree T
  have matched : covered c values := by exact coverage c values member
  exact actual_of_covered H f c values matched pos eq
end OneLow

namespace TwoLow
open TwentyThreeFewLowBase (Case twoLow)
theorem entries_distinct : ∀ c, ((entries c).map Prod.fst).Nodup := by decide +kernel
theorem entries_values (c : Case) (e : Finset (Fin 3) × ℕ) (mem : e∈entries c) : e.2=twoLow c e.1 := by
  have h : ∀ c, (entries c).all (fun e => decide (e.2=twoLow c e.1))=true := by decide +kernel
  exact of_decide_eq_true (List.all_eq_true.mp (h c) e mem)
theorem entries_support : ∀ c, ∀ T : Finset (Fin 3),
  T≠∅ → T∉(entries c).map Prod.fst → twoLow c T=0 := by decide +kernel

attribute [local irreducible] covered

/-- Match an abstract promotion vector before inserting the actual H counts. -/
theorem actual_of_covered (H : Simple5Hypergraph (Fin 23)) (f : Fin 4 ↪ Fin 23)
    (c : Case) (values : List ℕ) (matched : covered c values)
    (pos : positive c values) (actual : ∀ T, count H f T=newCounts c values T) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 4),
      (∀ i, (σ i).val<2 ↔ i.val<2) ∧
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  unfold covered at matched
  let chosen := choose (code c values)
  refine ⟨chosen.1,perm chosen.2,perm_preserves_roles chosen.2,?_⟩
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched pos T

theorem actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (f : Fin 4 ↪ Fin 23) (c : Case)
    (old : ∀ T, count H (restrict f) T=twoLow c T)
    (degree : H.degree (f 3)=7)
    (pairs : ∀ i : Fin 3, H.codegree (f i.castSucc) (f 3)≤cap (some i)) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 4),
      (∀ i, (σ i).val<2 ↔ i.val<2) ∧
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  let values := (entries c).map (fun e => promotion H f e.1)
  have capacity (j : Option (Fin 3)) : actualCap H f j≤cap j := by
    cases j with
    | none => simpa [actualCap,cap] using degree.le
    | some i => exact pairs i
  have member : values∈catalogue c := by
    apply actual_mem_of_old H f (entries c) cap (entries_distinct c) ?_ capacity
    intro e he
    rw [old,entries_values c e he]
  have prom (T : Finset (Fin 3)) (ne : T≠∅) : vector c values T=promotion H f T := by
    apply decode_nonempty H f (entries c) ?_ T ne
    intro S nonempty absent
    have bound := promotion_le_old H f S
    rw [old,entries_support c S nonempty absent] at bound
    omega
  have pos : positive c values := by
    intro i
    have eq : (∑ T : Finset (Fin 3), if i∈T then vector c values T else 0) =
        ∑ T : Finset (Fin 3), if i∈T then promotion H f T else 0 := by
      apply Finset.sum_congr rfl
      intro T _
      by_cases hi : i∈T
      · rw [if_pos hi,if_pos hi,prom T (by intro empty; simpa [empty] using hi)]
      · simp [hi]
    rw [eq,sum_promotion_codegree]
    exact H.one_le_codegree cover (f.injective.ne (Fin.castSucc_ne_last i))
  have eq (T : Finset (Fin 4)) : count H f T=newCounts c values T :=
    extend_actual H f (twoLow c) (vector c values) 7 old prom degree T
  have matched : covered c values := by exact coverage c values member
  exact actual_of_covered H f c values matched pos eq
end TwoLow
end Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage.OneLow.actual
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage.TwoLow.actual
