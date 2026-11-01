import Aris4Math.ThirtyThree.TwentyFourMixedFacts
import Aris4Math.ThirtyThree.TwentyFourSelection

namespace Aris4Math.ThirtyThree.TwentyFourMixed
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TwentyFourMixedData
open Aris4Math.ThirtyThree.TwentyFourMixedFacts
open Aris4Math.ThirtyThree.TwentyFourMixedFacts

theorem propertyB_of_mixed_locks (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (mixed : TwentyFourSelection.MixedLocks H)  : ∃ vertices : Fin 5 ↪ Fin 24,
    (∀ j, H.degree (vertices j) = degreeData j) ∧
    (∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1) ∧
    (∀ j : Fin 2, ∀ P ∈ H.badLinkPairs (vertices (j.castLE (by omega))),
      ∃ E ∈ P, Disjoint E (({2,3,4} : Finset (Fin 5)).image vertices)) := by
  obtain ⟨x,y,z,u,v,hcard,dx,dy,dz,du,dv,unit,avoidX,avoidY⟩ := mixed
  let fn : Fin 5 → Fin 24 := ![x,y,z,u,v]
  have imageAll : Finset.univ.image fn = ({x,y,z,u,v} : Finset (Fin 24)) := by
    have univ5 : (Finset.univ : Finset (Fin 5)) = {0,1,2,3,4} := by decide
    rw [univ5]
    simp [fn]
  have inj : Function.Injective fn := by
    have hinj : Set.InjOn fn (Finset.univ : Finset (Fin 5)) :=
      Finset.card_image_iff.mp (by rw [imageAll,hcard]; rfl)
    exact fun a b h => hinj (Finset.mem_univ a) (Finset.mem_univ b) h
  let vertices : Fin 5 ↪ Fin 24 := ⟨fn,inj⟩
  have inSet (j : Fin 5) : vertices j ∈ ({x,y,z,u,v} : Finset (Fin 24)) := by
    rw [← imageAll]
    exact Finset.mem_image.mpr ⟨j,Finset.mem_univ j,rfl⟩
  have degrees : ∀ j, H.degree (vertices j) = degreeData j := by
    intro j
    fin_cases j
    · exact dx
    · exact dy
    · exact dz
    · exact du
    · exact dv
  have unit' : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1 :=
    fun i j hij => unit _ (inSet i) _ (inSet j) (vertices.injective.ne hij)
  have imageHigh : (({2,3,4} : Finset (Fin 5)).image vertices) = {z,u,v} := by
    simp [vertices,fn]
  refine ⟨vertices,degrees,unit',?_⟩
  intro j P hP
  rw [imageHigh]
  fin_cases j
  · exact avoidX P hP
  · exact avoidY P hP

end Aris4Math.ThirtyThree.TwentyFourMixed
