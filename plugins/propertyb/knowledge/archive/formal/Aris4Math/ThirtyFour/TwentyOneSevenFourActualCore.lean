import Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogueData
import Aris4Math.ThirtyFour.TwentyOneSevenQuads
import Aris4Math.ThirtyFour.LockLiftRelabel
import Aris4Math.ThirtyFour.TwentyOneSevenSelection

namespace Aris4Math.ThirtyFour.TwentyOneSevenFourActualCore
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (threeVertices)
open LockExtension PromotionCatalog PromotionReconstruction
open TwentyOneSevenManyCatalogue (entries)
open TwentyOneSevenQuadCoverage (Residue residueμ)
set_option maxHeartbeats 800000
set_option maxRecDepth 100000
def cap : Option (Fin 4) → ℕ | none => 8 | some _ => 2
def catalogue (r : Residue) := BoundedAllocations.enumerate cost (entries r) cap
def vector (r : Residue) (values : List ℕ) := BoundedAllocations.decode (entries r) values
def μ (r : Residue) (values : List ℕ) := extend (residueμ r) (vector r values) 8
def Valid (r : Residue) (values : List ℕ) : Prop :=
  (∀ T, fillEmpty (vector r values) 8 T ≤ residueμ r T) ∧
  (∀ i : Fin 4, 1 ≤ ∑ T : Finset (Fin 4), if i ∈ T then vector r values T else 0)
instance (r : Residue) (values : List ℕ) : Decidable (Valid r values) := by
  unfold Valid; infer_instance

private theorem entries_nodup : ∀r : Residue,((entries r).map Prod.fst).Nodup := by
  decide +kernel
private theorem entries_values : ∀r : Residue,∀e∈entries r,e.2=residueμ r e.1 := by
  decide +kernel
private theorem entries_support : ∀r : Residue,∀T : Finset (Fin 4),
    T≠∅→T∉(entries r).map Prod.fst→ residueμ r T=0 := by
  decide +kernel

/-- Actual four-seven/one-eight inputs reduce to the complete promotion catalogue. -/
theorem propertyB_of_four_sevens_and_eight (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34) (f : Fin 5↪Fin 21)
    (oldDegrees : ∀ i : Fin 4, H.degree (f i.castSucc)=7)
    (newDegree : H.degree (f (Fin.last 4))=8)
    (covered : ∀(r : Residue) (values : List ℕ),
      values∈catalogue r → Valid r values →
      ∀ g : Fin 5 ↪ Fin 21, (∀ T, count H g T=μ r values T) → PropertyB H) : PropertyB H := by
  classical
  by_contra noB
  obtain ⟨r,p,old⟩ := TwentyOneSevenQuads.residual H cover size noB
    (restrict f) oldDegrees
  let σ := TwentyOneSevenQuadCoverage.perm p
  let g : Fin 5↪Fin 21 := (LockLiftRelabel.lift σ).toEmbedding.trans f
  have oldDegree (i : Fin 4) : H.degree (g i.castSucc)=7 := by
    change H.degree (f (LockLiftRelabel.lift σ i.castSucc))=7
    rw [LockLiftRelabel.lift_castSucc]
    exact oldDegrees _
  have lastDegree : H.degree (g (Fin.last 4))=8 := by
    simpa only [g,LockLiftRelabel.new_vertex_lift_trans] using newDegree
  have oldActual (T) : count H (restrict g) T=residueμ r T := by
    dsimp only [g]
    rw [LockLiftRelabel.restrict_lift_trans]
    exact old T
  have third : ∀ i : Fin 4, ∃ j : Fin 4, i≠j := by decide
  have pairs (i : Fin 4) : H.codegree (g i.castSucc) (g (Fin.last 4))≤2 := by
    obtain ⟨j,ij⟩ := third i
    let t := threeVertices (g i.castSucc) (g j.castSucc) (g (Fin.last 4))
      (g.injective.ne (by exact Fin.castSucc_inj.ne.mpr ij))
      (g.injective.ne (Fin.castSucc_ne_last i))
      (g.injective.ne (Fin.castSucc_ne_last j))
    have td : ∀z,H.degree (t z)=(![7,7,8] : Fin 3→ℕ) z := by
      intro z;fin_cases z <;> simp [t,threeVertices,oldDegree]
      exact lastDegree
    exact (TwentyOneSevenTriples.residual778 H cover size noB t td).2.1
  let values := (entries r).map (fun e=>promotion H g e.1)
  have capacity (j : Option (Fin 4)) : actualCap H g j≤cap j := by
    cases j with
    | none => exact lastDegree.le
    | some i => exact pairs i
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
  have filled (T) : fillEmpty (vector r values) 8 T=promotion H g T :=
    fillEmpty_actual H g (vector r values) 8 promotions lastDegree T
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
    extend_actual H g (residueμ r) (vector r values) 8 oldActual promotions
      lastDegree T
  exact noB (covered r values member valid g actual)
/-- Select the four actual seven-degree vertices and any actual eight-degree
vertex. Only the finite catalogue obligation remains explicit. -/
theorem propertyB_of_four_sevens (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34)
    (minimum : ∀ x, 7≤H.degree x)
    (four : (TwentyOneSevenSelection.sevens H).card=4)
    (covered : ∀ (r : Residue) (values : List ℕ),
      values∈catalogue r → Valid r values →
      ∀ g : Fin 5 ↪ Fin 21, (∀ T, count H g T=μ r values T) → PropertyB H) :
    PropertyB H := by
  classical
  let S := TwentyOneSevenSelection.sevens H
  let e : ↥S ≃ Fin 4 := Fintype.equivFinOfCardEq (by simpa [S] using four)
  let old : Fin 4 ↪ Fin 21 :=
    ⟨fun i => (e.symm i).val, Subtype.val_injective.comp e.symm.injective⟩
  have oldDegree (i : Fin 4) : H.degree (old i)=7 :=
    (Finset.mem_filter.mp (e.symm i).property).2
  have budget := TwentyOneSevenSelection.degree_count_budget H size minimum
  rw [four] at budget
  have pos : 0 < (TwentyOneSevenSelection.eights H).card := by omega
  obtain ⟨y,hy⟩ := Finset.card_pos.mp pos
  have yd : H.degree y=8 := (Finset.mem_filter.mp hy).2
  have outside : y∉Set.range old := by
    rintro ⟨i,rfl⟩
    have := oldDegree i
    omega
  let f : Fin 5 ↪ Fin 21 :=
    ⟨Fin.snoc old y,Fin.snoc_injective_of_injective old.injective outside⟩
  apply propertyB_of_four_sevens_and_eight H cover size f ?_ ?_ covered
  · intro i
    simpa [f] using oldDegree i
  · simpa [f] using yd

end Aris4Math.ThirtyFour.TwentyOneSevenFourActualCore
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenFourActualCore.propertyB_of_four_sevens_and_eight

#print axioms Aris4Math.ThirtyFour.TwentyOneSevenFourActualCore.propertyB_of_four_sevens
