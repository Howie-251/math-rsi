import Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue
import Aris4Math.ThirtyFour.TwentyOneSevenUniqueLocal
import Aris4Math.ThirtyFour.LockRelabel
namespace Aris4Math.ThirtyFour.TwentyOneSevenUniqueActual
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyOneSevenUniqueCatalogue
set_option maxHeartbeats 400000
set_option maxRecDepth 100000
attribute [local irreducible] Matched

/-- Dispatch a symbolic local inventory before substituting the actual edge counts. -/
theorem propertyB_of_matched (H : Simple5Hypergraph (Fin 21)) (f : Fin 6↪Fin 21)
    (values : List ℕ) (matched : Matched values)
    (actual : ∀T,count H f T=μ values T) : PropertyB H := by
  classical
  cases chosen : choose (code values) with
  | inl cp =>
    have exactCounts : ∀T,μ values (T.map (perm cp.2).toEmbedding)=targetμ cp.1 T := by
      simpa only [Matched,chosen] using matched
    apply TwentyOneSevenUniqueLocal.propertyB_of_counts H ((perm cp.2).toEmbedding.trans f) cp.1
    intro T
    rw [LockRelabel.count_comp_perm,actual]
    exact exactCounts T
  | inr cp =>
    have exactCounts : ∀T,(∑U : Finset (Fin 6),
        if LockProjection.project (project cp.2) U=T then μ values U else 0)=targetFive cp.1 T := by
      simpa only [Matched,chosen] using matched
    apply TwentyOneSevenUniqueLocal.propertyB_of_five_counts H ((project cp.2).trans f) cp.1
    intro T
    rw [LockProjection.count_comp]
    simp only [actual]
    exact exactCounts T

/-- Complete finite local allocation membership plus actual trace recovery
provides a coloring for these selected six actual vertices. -/
theorem propertyB_of_locks (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (f : Fin 6↪Fin 21)
    (degrees : ∀i,H.degree (f i)=if i=5 then 7 else 8)
    (pairs : ∀i j,i≠j→H.codegree (f i) (f j)=if i=5 ∨ j=5 then 1 else 2)
    (promotions : ∀T : Finset (Fin 5),LockExtension.promotion H f T=
      if T=∅ then 4 else if T={0,1} ∨ T={2,3} ∨ T={4} then 1 else 0) : PropertyB H := by
  classical
  let g:=LockExtension.restrict f
  have neLast (i : Fin 5) : i.castSucc≠(5 : Fin 6) := by
    change i.castSucc≠Fin.last 5
    exact Fin.castSucc_ne_last i
  have ds (i : Fin 5) : H.degree (g i)=8 := by
    have h:=degrees i.castSucc
    simpa [g,LockExtension.restrict,neLast] using h
  have ps (i j : Fin 5) (ij : i≠j) : H.codegree (g i) (g j)=2 := by
    have h:=pairs i.castSucc j.castSucc (fun eq=>ij (Fin.castSucc_inj.mp eq))
    simpa [g,LockExtension.restrict,neLast] using h
  let values:=entries.map (fun e=>count H g e.1)
  have allHigh : ∀e∈entries,2≤e.1.card := by decide +kernel
  have bounds : ∀e∈entries,count H g e.1≤e.2 := by
    intro e he
    have two : e.2=2 := by
      have finite : ∀e∈entries,e.2=2 := by decide +kernel
      exact finite e he
    rw [two]
    exact ActualAllocations.count_le_of_pairs H g 2 (fun i j ij=>(ps i j ij).le) e.1 (allHigh e he)
  have capacity (j : Fin 10) : upperCount H g (pair j)≤2 := by
    have data : ∀j : Fin 10,∃i k : Fin 5,i≠k ∧ pair j={i,k} := by decide +kernel
    obtain ⟨i,k,ik,eq⟩:=data j
    rw [eq,upper_pair,ps i k ik]
  have mem : values∈catalogue :=
    ActualAllocations.mem_enumerate H g entries entries_nodup pair (fun _=>2) bounds capacity
  have lowActual : ∀T,T.card≤2→upperCount H g T=low T := by
    apply upper_eq_of_low_data H g low
    · simp [low,size]
    · intro i;simp [low,ds]
    · intro i j ij;simp [low,ij,ps i j ij]
  have highActual : ∀T,3≤T.card→count H g T=high values T := by
    intro T hT
    have support : ∀T : Finset (Fin 5),3≤T.card→T∈entries.map Prod.fst := by decide +kernel
    unfold high values
    rw [BoundedAllocations.decode_map,if_pos (support T hT)]
  have oldActual (T) : count H g T=oldμ values T :=
    actual_recovered H g low (high values) lowActual highActual T
  have filled : ∀T : Finset (Fin 5),PromotionReconstruction.fillEmpty promotion 7 T=
      if T=∅ then 4 else if T={0,1} ∨ T={2,3} ∨ T={4} then 1 else 0 := by decide +kernel
  have valid : Valid values := by
    intro T
    rw [filled,←promotions,←oldActual]
    exact LockExtension.promotion_le_old H f T
  have actual (T) : count H f T=μ values T := by
    apply PromotionReconstruction.extend_actual H f (oldμ values) promotion 7 oldActual
    · intro U nonempty
      rw [promotions,if_neg nonempty]
      rfl
    · exact degrees 5
  have matched : Matched values := by exact coverage values mem valid
  exact propertyB_of_matched H f values matched actual
end Aris4Math.ThirtyFour.TwentyOneSevenUniqueActual
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenUniqueActual.propertyB_of_locks
