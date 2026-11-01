import Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified
import Aris4Math.ThirtyFour.TwentyThreeLowUnitSelection
import Aris4Math.ThirtyFour.TwentyThreeStrongCodegree

/-! Role-preserving actual inputs for the one/two-low continuation. The
first r labels are low; the rest are actual common-unit degree-seven locks. -/
namespace Aris4Math.ThirtyFour.TwentyThreeFewLowActualBase
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open Aris4Math.ThirtyThree.TwentyThreeSelection
variable {n m : ℕ}

structure Input (H : Simple5Hypergraph (Fin 23)) (r : ℕ) (f : Fin n↪Fin 23) : Prop where
  degrees : ∀ i, H.degree (f i)=if i.val<r then 6 else 7
  unit : ∀ i j, i.val<r → ¬j.val<r → H.codegree (f i) (f j)=1

theorem Input.comp {H : Simple5Hypergraph (Fin 23)} {r : ℕ} {f : Fin n↪Fin 23}
    (h : Input H r f) (g : Fin m↪Fin n) (roles : ∀ i, (g i).val<r ↔ i.val<r) :
    Input H r (g.trans f) where
  degrees i := by simpa only [Function.Embedding.trans_apply,roles i] using h.degrees (g i)
  unit i j low high := h.unit (g i) (g j) ((roles i).mpr low)
    (fun bad => high ((roles j).mp bad))

theorem Input.restrict {H : Simple5Hypergraph (Fin 23)} {r : ℕ}
    {f : Fin (n+1)↪Fin 23} (h : Input H r f) : Input H r (LockExtension.restrict f) :=
  h.comp Fin.castSuccEmb (fun _ => Iff.rfl)

theorem Input.codegree_le_three {H : Simple5Hypergraph (Fin 23)} {r : ℕ}
    {f : Fin n↪Fin 23} (h : Input H r f) (cover : H.PairCovering)
    (edges : H.edges.card=34) (many : 3≤(sevenVertices H).card) (noB : ¬PropertyB H)
    (i j : Fin n) (apart : i≠j) : H.codegree (f i) (f j)≤3 := by
  by_cases lowi : i.val<r
  · exact six_codegree_le_three H cover (Fintype.card_fin 23)
      (by simpa only [if_pos lowi] using h.degrees i) (f.injective.ne apart)
  by_cases lowj : j.val<r
  · rw [H.codegree_comm]
    exact six_codegree_le_three H cover (Fintype.card_fin 23)
      (by simpa only [if_pos lowj] using h.degrees j) (f.injective.ne apart.symm)
  exact TwentyThreeStrongCodegree.codegree_le H cover edges many noB (f i) (f j)
    (f.injective.ne apart) (by simpa only [if_neg lowi] using h.degrees i)
    (by simpa only [if_neg lowj] using h.degrees j)

/-- Reuse the already-checked 48 four-lock types and 29 strict exclusions. -/
theorem two_low_four (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (many : 3≤(sevenVertices H).card) (noB : ¬PropertyB H)
    (f : Fin 4↪Fin 23) (h : Input H 2 f) :
    ∃ q : TwentyThreeFewLowFourCoverage.TwoLow.NewCase, ∃ σ : Equiv.Perm (Fin 4),
      (∀ i, (σ i).val<2 ↔ i.val<2) ∧
      q∈TwentyThreeFewLowFourClassified.TwoLow.residual ∧
      ∀ T, count H (σ.toEmbedding.trans f) T=TwentyThreeFewLowFourCoverage.TwoLow.μ q T := by
  have old := h.restrict
  obtain ⟨c,actual⟩ := TwentyThreeFewLowBase.actual_twoLow H cover edges
    (LockExtension.restrict f)
    (by simpa using old.degrees 0) (by simpa using old.degrees 1)
    (by simpa using old.degrees 2)
    (old.codegree_le_three cover edges many noB 0 1 (by decide))
    (old.unit 0 2 (by decide) (by decide)) (old.unit 1 2 (by decide) (by decide))
  apply TwentyThreeFewLowFourClassified.TwoLow.actual_residual H cover f c actual
    (by simpa using h.degrees 3) ?_ noB
  intro i
  fin_cases i
  · change H.codegree (f 0) (f 3)≤1
    rw [h.unit 0 3 (by decide) (by decide)]
  · change H.codegree (f 1) (f 3)≤1
    rw [h.unit 1 3 (by decide) (by decide)]
  · exact h.codegree_le_three cover edges many noB 2 3 (by decide)

end Aris4Math.ThirtyFour.TwentyThreeFewLowActualBase
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowActualBase.two_low_four
