import Aris4Math.ThirtyFour.TwentyFiveEightLowClassified
import Aris4Math.ThirtyFour.TwentyFiveEightLowNumeric
import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthComplete
import Aris4Math.ThirtyFour.TwentyFiveSelection
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowComplete
open Aris4Math.ThirtyThree.MultiLockRecovery TwentyFiveUnitExtension TwentyFiveUnitCatalogue
open TwentyFiveColoredActual TwentyFiveEightLowTenthCoverage
open LockExtension (restrict)

theorem residue_group (c : Fin 840) (residue : c=0 ∨ c=10) :
    ∃ g : Fin 2,base g=c := by
  rcases residue with rfl | rfl
  · exact ⟨0,rfl⟩
  · exact ⟨1,rfl⟩

theorem propertyB (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (selection : TwentyFiveSelection.MixedLocks H 8 2) : PropertyB H := by
  by_contra notB
  obtain ⟨f,degrees,unit⟩ := selection
  have firstUnit : Unit H (restrict f) := unit_restrict H f unit
  have firstDegree (i : Fin 9) : H.degree ((restrict f) i)=standard 8 i :=
    degrees i.castSucc
  obtain ⟨c,σ,big,newFirstDegree,counts⟩ := TwentyFiveEightLowClassified.actual H edges (restrict f)
    firstUnit firstDegree
  have split := TwentyFiveEightLowNumeric.strict_or_residue H
    (σ.toEmbedding.trans (restrict f)) c counts
  have residue : c=0 ∨ c=10 := by
    rcases split with h | h | done
    · exact Or.inl h
    · exact Or.inr h
    · exact (notB done).elim
  obtain ⟨g,baseEq⟩ := residue_group c residue
  let τ := LockLiftRelabel.lift σ
  let new := τ.toEmbedding.trans f
  have newUnit : Unit H new := unit_relabel H f unit τ
  have newOld : large H (restrict new)=oldBig g := by
    rw [show restrict new=σ.toEmbedding.trans (restrict f) from
      LockLiftRelabel.restrict_lift_trans σ f]
    simpa only [oldBig,baseEq] using big
  have newDegrees (i : Fin 10) : H.degree (new i)=standard 8 i := by
    refine Fin.lastCases ?_ (fun j => ?_) i
    · change H.degree (f (LockLiftRelabel.lift σ (Fin.last 9)))=standard 8 (Fin.last 9)
      rw [LockLiftRelabel.lift_last]
      exact degrees (Fin.last 9)
    · change H.degree (f (LockLiftRelabel.lift σ j.castSucc))=standard 8 j.castSucc
      rw [LockLiftRelabel.lift_castSucc]
      exact newFirstDegree j
  exact notB (TwentyFiveEightLowTenthComplete.propertyB_of_group H edges new newUnit g newDegrees newOld)
end Aris4Math.ThirtyFour.TwentyFiveEightLowComplete
#print axioms Aris4Math.ThirtyFour.TwentyFiveEightLowComplete.propertyB
