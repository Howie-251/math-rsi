import Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogueData
import Aris4Math.ThirtyFour.TwentyOneSevenQuads
import Aris4Math.ThirtyFour.LockLiftRelabel

namespace Aris4Math.ThirtyFour.TwentyOneSevenManyActualCore
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (threeVertices)
open LockExtension PromotionCatalog PromotionReconstruction
open TwentyOneSevenManyCatalogue
open TwentyOneSevenQuadCoverage (Residue residueμ)
set_option maxHeartbeats 800000
set_option maxRecDepth 100000
attribute [local irreducible] Matched

private theorem entries_nodup : ∀r : Residue,((entries r).map Prod.fst).Nodup := by
  decide +kernel
private theorem entries_values : ∀r : Residue,∀e∈entries r,e.2=residueμ r e.1 := by
  decide +kernel
private theorem entries_support : ∀r : Residue,∀T : Finset (Fin 4),
    T≠∅→T∉(entries r).map Prod.fst→ residueμ r T=0 := by
  decide +kernel

private theorem propertyB_of_matched (H : Simple5Hypergraph (Fin 21))
    (g : Fin 5↪Fin 21) (r : Residue) (values : List ℕ)
    (actual : ∀T,count H g T=μ r values T)
    (matched : Matched r values) : PropertyB H := by
  classical
  cases chosen : choose r values with
  | inl cp =>
    have exactCounts : ∀T,μ r values (T.map (perm cp.2).toEmbedding)=
        TwentyOneSevenFive77777Data.μ cp.1 T := by
      simpa only [Matched,chosen] using matched
    apply TwentyOneSevenFive77777.propertyB_of_counts H ((perm cp.2).toEmbedding.trans g) cp.1
    intro T
    rw [LockRelabel.count_comp_perm,actual]
    exact exactCounts T
  | inr cp =>
    have exactCounts : ∀T,(∑U : Finset (Fin 5),
        if LockProjection.project (project cp.2) U=T then μ r values U else 0)=
          TwentyOneSevenQuadCoverage.μ ⟨cp.1.val,by omega⟩ T := by
      simpa only [Matched,chosen] using matched
    apply TwentyOneSevenQuadCoverage.propertyB_of_counts H ((project cp.2).trans g)
      ⟨cp.1.val,by omega⟩ cp.1.isLt
    intro T
    rw [LockProjection.count_comp]
    simp only [actual]
    exact exactCounts T

/-- Every five actual degree-seven vertices force a strict local coloring
bound, including all promotions of the nine four-lock residual profiles. -/
theorem propertyB_of_five_sevens (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34) (f : Fin 5↪Fin 21)
    (degrees : ∀i,H.degree (f i)=7)
    (covered : ∀(r : Residue) (values : List ℕ),
      values∈catalogue r → Valid r values → Matched r values) : PropertyB H := by
  classical
  by_contra noB
  obtain ⟨r,p,old⟩ := TwentyOneSevenQuads.residual H cover size noB
    (restrict f) (fun i=>degrees i.castSucc)
  let σ := TwentyOneSevenQuadCoverage.perm p
  let g : Fin 5↪Fin 21 := (LockLiftRelabel.lift σ).toEmbedding.trans f
  have ds (i : Fin 5) : H.degree (g i)=7 := degrees _
  have oldActual (T) : count H (restrict g) T=residueμ r T := by
    dsimp only [g]
    rw [LockLiftRelabel.restrict_lift_trans]
    exact old T
  have third : ∀i j : Fin 5,i≠j→∃k,k≠i ∧ k≠j := by decide
  have pairs (i j : Fin 5) (ij : i≠j) : H.codegree (g i) (g j)≤2 := by
    obtain ⟨k,ki,kj⟩ := third i j ij
    let t := threeVertices (g i) (g j) (g k) (g.injective.ne ij)
      (g.injective.ne ki.symm) (g.injective.ne kj.symm)
    have td : ∀z,H.degree (t z)=(![7,7,7] : Fin 3→ℕ) z := by
      intro z;fin_cases z <;> simp [t,threeVertices,ds]
    exact (TwentyOneSevenTriples.residual777 H cover size noB t td).1
  let values := (entries r).map (fun e=>promotion H g e.1)
  have capacity (j : Option (Fin 4)) : actualCap H g j≤cap j := by
    cases j with
    | none => exact (ds (Fin.last 4)).le
    | some i => exact pairs i.castSucc (Fin.last 4) (Fin.castSucc_ne_last i)
  have member : values∈catalogue r := by
    apply actual_mem_of_old H g (entries r) cap (entries_nodup r) ?_ capacity
    intro e he
    rw [oldActual,entries_values r e he]
  have promotions (T : Finset (Fin 4)) (nonempty : T≠∅) :
      vector r values T=promotion H g T := by
    apply decode_nonempty H g (entries r) ?_ T nonempty
    intro U ne absent
    have le := promotion_le_old H g U
    rw [oldActual,entries_support r U ne absent] at le
    omega
  have filled (T) : fillEmpty (vector r values) 7 T=promotion H g T :=
    fillEmpty_actual H g (vector r values) 7 promotions (ds (Fin.last 4)) T
  have valid : Valid r values := by
    constructor
    · intro T
      rw [filled,←oldActual]
      exact promotion_le_old H g T
    · intro i
      have sums : (∑T : Finset (Fin 4),if i∈T then vector r values T else 0)=
          ∑T : Finset (Fin 4),if i∈T then promotion H g T else 0 := by
        apply Finset.sum_congr rfl
        intro T _
        by_cases present : i∈T
        · rw [if_pos present,if_pos present,promotions T (by intro h;simpa [h] using present)]
        · rw [if_neg present,if_neg present]
      rw [sums,sum_promotion_codegree]
      exact H.one_le_codegree cover (g.injective.ne (Fin.castSucc_ne_last i))
  have actual (T) : count H g T=μ r values T :=
    extend_actual H g (residueμ r) (vector r values) 7 oldActual promotions
      (ds (Fin.last 4)) T
  have matched : Matched r values := covered r values member valid
  exact noB (propertyB_of_matched H g r values actual matched)
end Aris4Math.ThirtyFour.TwentyOneSevenManyActualCore
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenManyActualCore.propertyB_of_five_sevens
