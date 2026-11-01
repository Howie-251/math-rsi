import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogueNumeric
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
  obtain ⟨w,matched⟩ := coverage b values member d normalized
  refine ⟨w.1,newPerm w.2,?_⟩
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched T

/-- Six transitive automorphisms of the actual residual inventory. -/
def normalizer (i : Fin 6) : Equiv.Perm (Fin 6) :=
  TwentyFourPermutation.perm (![0,301,260,111,4,5] i)

theorem normalizer_preserves : ∀ i : Fin 6, ∀ T : Finset (Fin 6),
    oldCounts (T.map (normalizer i).toEmbedding)=oldCounts T := by decide +kernel

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
  | none => exact actual_normalized_extension H f d none (Or.inl rfl) old pairs newDegree
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
    obtain ⟨q,τ,profile⟩ := actual_normalized_extension H g d (some 0) (Or.inr rfl) oldg pairsg deg
    exact ⟨q,τ.trans ρ,profile⟩

end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
#print axioms Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue.actual_extension
