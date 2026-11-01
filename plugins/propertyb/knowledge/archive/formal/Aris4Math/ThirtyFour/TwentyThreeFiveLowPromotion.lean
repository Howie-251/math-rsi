import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionNumeric
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open LockExtension PromotionCatalog PromotionReconstruction
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option synthInstance.maxSize 2000

theorem entries_distinct : ∀ c, ((entries c).map Prod.fst).Nodup := by decide +kernel

theorem entries_values (c : OldCase) (e : Finset (Fin 4) × ℕ) (mem : e∈entries c) :
    e.2=oldCounts c e.1 := by
  have h : ∀ c, (entries c).all (fun e => decide (e.2=oldCounts c e.1))=true := by decide +kernel
  exact of_decide_eq_true (List.all_eq_true.mp (h c) e mem)

theorem entries_support : ∀ c, ∀ T : Finset (Fin 4),
    T≠∅ → T∉(entries c).map Prod.fst → oldCounts c T=0 := by decide +kernel

theorem old_actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (g : Fin 4 ↪ Fin 23)
    (degrees : ∀ i, H.degree (g i)=6) (notB : ¬ PropertyB H) :
    OldResidual (count H g) := by
  obtain ⟨r, σ, actual⟩ := TwentyThreeFourLowClassified.actual_residual H cover edges g degrees notB
  refine ⟨r,?_⟩
  intro k p
  exact (TwentyThreeTraceShape.cardMoment_of_relabelled_counts H g σ (oldCounts r) actual k (p.val+1)).trans
    (expected_correct r k p)

attribute [local irreducible] covered

theorem actual_of_covered (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 5 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H)
    (c : OldCase) (values : List ℕ) (matched : covered c values)
    (actual : ∀ T, count H f T=newCounts c values T) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 5),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  have feasible := TwentyThreeLowPromotionBase.feasible_actual H cover f degrees
    (newCounts c values) actual
  unfold covered at matched
  obtain ⟨choice,matched⟩ := matched
  have projection : ∀ T, projected choice.1 (newCounts c values) T =
      count H ((deletion choice.1).trans f) T := by
    intro T
    rw [LockProjection.count_comp]
    simp only [projected,actual]
  have old := old_actual H cover edges ((deletion choice.1).trans f)
    (fun i => degrees ((deletion choice.1) i)) notB
  have residual : OldResidual (projected choice.1 (newCounts c values)) := by
    simpa only [show projected choice.1 (newCounts c values)=
      count H ((deletion choice.1).trans f) from funext projection] using old
  unfold rowCovered at matched
  refine ⟨choice.2.1,newPerm choice.2.2,?_⟩
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched feasible residual T

/-- Complete actual extension from one canonical old inventory. Every
rejected projection is classified on the same original H. -/
theorem actual_extension (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 5 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H)
    (c : OldCase) (old : ∀ T, count H (restrict f) T=oldCounts c T) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 5),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  let values := (entries c).map (fun e => promotion H f e.1)
  have member : values∈catalogue c := by
    apply TwentyThreeLowPromotionBase.actual_mem H cover f degrees (entries c) (entries_distinct c)
    intro e he
    rw [old,entries_values c e he]
  have prom (T : Finset (Fin 4)) (ne : T≠∅) : vector c values T=promotion H f T := by
    apply decode_nonempty H f (entries c) ?_ T ne
    intro S nonempty absent
    have bound := promotion_le_old H f S
    rw [old,entries_support c S nonempty absent] at bound
    omega
  have actual (T : Finset (Fin 5)) : count H f T=newCounts c values T :=
    extend_actual H f (oldCounts c) (vector c values) 6 old prom (degrees _) T
  exact actual_of_covered H cover edges f degrees notB c values (coverage c values member) actual

/-- Every original low-lock choice is covered: first normalize its old
subset, then lift that same permutation while fixing the newly added point. -/
theorem actual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 5 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 5),
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  obtain ⟨c,σ,hc⟩ := TwentyThreeFourLowClassified.actual_residual H cover edges (restrict f)
    (fun i => degrees i.castSucc) notB
  let lift := LockLiftRelabel.lift σ
  let g := lift.toEmbedding.trans f
  have old : ∀ T, count H (restrict g) T=oldCounts c T := by
    intro T
    rw [show restrict g=σ.toEmbedding.trans (restrict f) from
      LockLiftRelabel.restrict_lift_trans σ f]
    exact hc T
  obtain ⟨q,τ,ht⟩ := actual_extension H cover edges g (fun i => degrees (lift i)) notB c old
  exact ⟨q,τ.trans lift,ht⟩

end Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
#print axioms Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion.actual
