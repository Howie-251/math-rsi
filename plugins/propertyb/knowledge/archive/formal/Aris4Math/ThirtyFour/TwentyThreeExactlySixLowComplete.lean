import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraChecked
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraSelection

namespace Aris4Math.ThirtyFour.TwentyThreeExactlySixLowComplete
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open TwentyThreeHighPromotion
open TwentyThreeSixLowExtraCatalogue

/-- The exact-six branch starts with the original hypergraph; both the
six-lock residual and all seven-lock representatives are derived internally. -/
theorem propertyB (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (six : H.sixVertices.card=6) : PropertyB H := by
  classical
  by_contra notB
  let e : ↥H.sixVertices ≃ Fin 6 := Fintype.equivFinOfCardEq (by simpa using six)
  let f : Fin 6↪Fin 23 :=
    ⟨fun i => (e.symm i).val, Subtype.val_injective.comp e.symm.injective⟩
  have low (i : Fin 6) : H.degree (f i)=6 :=
    (Finset.mem_filter.mp (e.symm i).property).2
  obtain ⟨r,σ,actual⟩ := TwentyThreeSixLowClassified.actual_residual H cover edges f low notB
  have only : r=0 := Subsingleton.elim _ _
  subst r
  let g := σ.toEmbedding.trans f
  have gLow (i : Fin 6) : H.degree (g i)=6 := low (σ i)
  obtain ⟨z,zd,outside,budget⟩ :=
    TwentyThreeSixLowExtraSelection.exists_seventh H cover edges six g gLow
  have absent : z∉Set.range g := by
    rintro ⟨i,hi⟩
    exact outside i hi
  let h : Fin 7↪Fin 23 := ⟨Fin.snoc g z, Fin.snoc_injective_of_injective g.injective absent⟩
  have restrict_eq : LockExtension.restrict h=g := by
    ext i
    simp [LockExtension.restrict,h]
  have hlast : h (Fin.last 6)=z := @Fin.snoc_last 6 (fun _ => Fin 23) z g
  have hcast (i : Fin 6) : h i.castSucc=g i := by simp [h]
  have positive (i : Fin 6) : 1≤H.codegree (g i) z := H.one_le_codegree cover (outside i)
  obtain ⟨b,hb⟩ := exists_oneDouble (fun i => H.codegree (g i) z) positive budget
  have pairValues (i : Fin 6) : oneDouble b i=H.codegree (h i.castSucc) (h (Fin.last 6)) := by
    rw [hcast,hlast]
    exact (hb i).symm
  have old : ∀ T, count H (LockExtension.restrict h) T=oldCounts T := by
    rw [restrict_eq]
    exact actual
  have someDegree : ∃ d : Degree, H.degree (h (Fin.last 6))=degree d := by
    rcases zd with seven | eight
    · exact ⟨0,by simpa [hlast,degree] using seven⟩
    · exact ⟨1,by simpa [hlast,degree] using eight⟩
  obtain ⟨d,degree_eq⟩ := someDegree
  obtain ⟨q,τ,profile⟩ := actual_extension H h d b old pairValues degree_eq
  exact notB (TwentyThreeSixLowExtraChecked.propertyB_of_counts H (τ.toEmbedding.trans h) d q profile)

end Aris4Math.ThirtyFour.TwentyThreeExactlySixLowComplete
#print axioms Aris4Math.ThirtyFour.TwentyThreeExactlySixLowComplete.propertyB
