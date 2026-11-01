import Aris4Math.ThirtyFour.PromotionReconstruction
import Aris4Math.ThirtyFour.LockLiftRelabel
import Aris4Math.ThirtyFour.LockRelabel
import Aris4Math.ThirtyThree.TwentyThreeSelection

/-! Actual incidence bounds for adding a degree-six lock on 23 points.
The extra resource bounds all old/new pair incidences together, so catalogue
pruning uses the full new-center excess budget, not just separate pair caps. -/
namespace Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.LockExtension PromotionCatalog
variable {n : ℕ}

def incidenceCost (T : Finset (Fin n)) : Option (Option (Fin n)) → ℕ
  | none => T.card
  | some q => cost T q

def incidenceCap : Option (Option (Fin n)) → ℕ
  | none => n+2
  | some none => 6
  | some (some _) => 3

theorem new_incidence_budget (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (f : Fin (n+1) ↪ Fin 23)
    (degree : H.degree (f (Fin.last n))=6) :
    (∑ i : Fin n, H.codegree (f i.castSucc) (f (Fin.last n))) ≤ n+2 := by
  have bound := ThirtyThree.TwentyThreeSelection.indexed_six_excess_le_two
    H cover (Fintype.card_fin 23) f f.injective (Fin.last n) degree
  let ex : Fin (n+1) → ℕ := fun j => H.codegree (f (Fin.last n)) (f j)-1
  have erase : (∑ j ∈ Finset.univ.erase (Fin.last n), ex j) =
      ∑ i : Fin n, ex i.castSucc := by
    have whole := Finset.sum_erase_add (s := Finset.univ) ex (Finset.mem_univ (Fin.last n))
    rw [Fin.sum_univ_castSucc] at whole
    omega
  change (∑ j ∈ Finset.univ.erase (Fin.last n), ex j) ≤ 2 at bound
  rw [erase] at bound
  have total : (∑ i : Fin n, H.codegree (f i.castSucc) (f (Fin.last n))) =
      (∑ i : Fin n, ex i.castSucc)+n := by
    have each (i : Fin n) : H.codegree (f i.castSucc) (f (Fin.last n)) = ex i.castSucc+1 := by
      have pos := H.one_le_codegree cover (f.injective.ne (Fin.castSucc_ne_last i))
      dsimp [ex]
      rw [H.codegree_comm (f (Fin.last n)) (f i.castSucc)]
      omega
    calc
      _ = ∑ i : Fin n, (ex i.castSucc+1) := Finset.sum_congr rfl (fun i _ => each i)
      _ = _ := by rw [Finset.sum_add_distrib]; simp
  rw [total]
  omega

theorem sum_promotion_trace_size (H : Simple5Hypergraph (Fin 23))
    (f : Fin (n+1) ↪ Fin 23) :
    (∑ T : Finset (Fin n), promotion H f T * T.card) =
      ∑ i : Fin n, H.codegree (f i.castSucc) (f (Fin.last n)) := by
  calc
    _ = ∑ T : Finset (Fin n), ∑ i : Fin n, if i∈T then promotion H f T else 0 := by
      apply Finset.sum_congr rfl
      intro T _
      simp [Nat.mul_comm]
    _ = ∑ i : Fin n, ∑ T : Finset (Fin n), if i∈T then promotion H f T else 0 :=
      Finset.sum_comm
    _ = _ := Finset.sum_congr rfl (fun i _ => sum_promotion_codegree H f i)

/-- Every genuine promotion is in the stronger incidence-pruned catalogue. -/
theorem actual_mem (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (f : Fin (n+1) ↪ Fin 23) (degrees : ∀ i, H.degree (f i)=6)
    (entries : List (Finset (Fin n) × ℕ)) (distinct : (entries.map Prod.fst).Nodup)
    (bounds : ∀ e∈entries, count H (restrict f) e.1 ≤ e.2) :
    entries.map (fun e => promotion H f e.1) ∈
      BoundedAllocations.enumerate incidenceCost entries incidenceCap := by
  apply BoundedAllocations.mem_enumerate incidenceCost entries incidenceCap (promotion H f)
  · intro e he
    exact (promotion_le_old H f e.1).trans (bounds e he)
  · intro q
    cases q with
    | none =>
      calc
        _ = ((entries.map Prod.fst).map (fun T => promotion H f T*T.card)).sum := by
          simp only [incidenceCost,List.map_map,Function.comp_def]
        _ = ∑ T ∈ (entries.map Prod.fst).toFinset, promotion H f T*T.card :=
          (List.sum_toFinset _ distinct).symm
        _ ≤ ∑ T : Finset (Fin n), promotion H f T*T.card :=
          Finset.sum_le_sum_of_subset (Finset.subset_univ _)
        _ = ∑ i : Fin n, H.codegree (f i.castSucc) (f (Fin.last n)) :=
          sum_promotion_trace_size H f
        _ ≤ n+2 := new_incidence_budget H cover f (degrees _)
    | some q =>
      have bound := listed_budget H f entries distinct q
      cases q with
      | none => simpa [incidenceCost,incidenceCap,actualCap,degrees] using bound
      | some i =>
        have pair := ThirtyThree.TwentyThreeSelection.six_codegree_le_three
          H cover (Fintype.card_fin 23) (degrees i.castSucc)
          (f.injective.ne (Fin.castSucc_ne_last i))
        exact bound.trans pair

/-- Pair counts reconstructed from all actual trace multiplicities. -/
def co (μ : Finset (Fin n) → ℕ) (i j : Fin n) : ℕ :=
  ∑ T : Finset (Fin n), if i∈T ∧ j∈T then μ T else 0

def Feasible (μ : Finset (Fin n) → ℕ) : Prop :=
  (∀ i j, i≠j → 1≤co μ i j) ∧
  (∀ i, (∑ j ∈ Finset.univ.erase i, (co μ i j-1))≤2)

instance (μ : Finset (Fin n) → ℕ) : Decidable (Feasible μ) := by
  unfold Feasible
  infer_instance

theorem feasible_actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (f : Fin n ↪ Fin 23) (degrees : ∀ i, H.degree (f i)=6)
    (μ : Finset (Fin n) → ℕ) (actual : ∀ T, count H f T=μ T) : Feasible μ := by
  have same (i j : Fin n) : co μ i j=H.codegree (f i) (f j) := by
    unfold co
    simp_rw [← actual]
    rw [← Finset.sum_filter]
    have h := sum_counts H f (Finset.univ.filter fun T => i∈T ∧ j∈T)
    simpa only [Finset.mem_filter,Finset.mem_univ,true_and,
      Aris4Math.TypeCounting.mem_lockSignature,Simple5Hypergraph.codegree] using h
  constructor
  · intro i j ij
    rw [same]
    exact H.one_le_codegree cover (f.injective.ne ij)
  · intro i
    simp_rw [same]
    exact ThirtyThree.TwentyThreeSelection.indexed_six_excess_le_two
      H cover (Fintype.card_fin 23) f f.injective i (degrees i)

end Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase
#print axioms Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase.actual_mem
#print axioms Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase.feasible_actual
