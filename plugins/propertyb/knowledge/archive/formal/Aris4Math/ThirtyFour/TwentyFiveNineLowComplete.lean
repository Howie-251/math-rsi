import Aris4Math.ThirtyFour.TwentyFiveNineLowClassified
import Aris4Math.ThirtyFour.TwentyFiveNineLowNumeric
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthComplete
import Aris4Math.ThirtyFour.TwentyFiveSelection

/-! The full nine-low selection branch, with the actual tenth lock retained
through every relabeling and all three exceptional nine-lock families. -/
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowComplete

open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue
open LockExtension (restrict)
open TwentyFiveNineLowTenthCoverage

theorem residue_group (c : Fin 147) (residue : c=0 ∨ c=3 ∨ c=6)
    (d : ℕ) (last : d=6 ∨ d=7) :
    ∃ g : Fin 6, base g=c ∧ lastDegree g=d := by
  rcases residue with rfl | rfl | rfl <;> rcases last with rfl | rfl
  · exact ⟨0,rfl,rfl⟩
  · exact ⟨1,rfl,rfl⟩
  · exact ⟨2,rfl,rfl⟩
  · exact ⟨3,rfl,rfl⟩
  · exact ⟨4,rfl,rfl⟩
  · exact ⟨5,rfl,rfl⟩

theorem propertyB (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (selection : TwentyFiveSelection.NineLowExtension H) : PropertyB H := by
  by_contra notB
  obtain ⟨f,low,last,unit⟩ := selection
  have firstUnit : Unit H (restrict f) := unit_restrict H f unit
  have firstDegree (i : Fin 9) : H.degree ((restrict f) i)=6 :=
    low i.castSucc i.isLt
  obtain ⟨c,σ,big,counts⟩ := TwentyFiveNineLowClassified.actual H edges (restrict f)
    firstUnit firstDegree
  have split := TwentyFiveNineLowNumeric.strict_or_residue H
    (σ.toEmbedding.trans (restrict f)) c counts
  have residue : c=0 ∨ c=3 ∨ c=6 := by
    rcases split with h | h | h | done
    · exact Or.inl h
    · exact Or.inr (Or.inl h)
    · exact Or.inr (Or.inr h)
    · exact (notB done).elim
  obtain ⟨g,baseEq,degreeEq⟩ := residue_group c residue (H.degree (f 9)) last
  let τ := LockLiftRelabel.lift σ
  let new := τ.toEmbedding.trans f
  have newUnit : Unit H new := unit_relabel H f unit τ
  have newOld : large H (restrict new)=oldBig g := by
    rw [show restrict new=σ.toEmbedding.trans (restrict f) from
      LockLiftRelabel.restrict_lift_trans σ f]
    simpa only [oldBig,baseEq] using big
  have newDegrees (i : Fin 10) : H.degree (new i)=degrees g i := by
    refine Fin.lastCases ?_ (fun j => ?_) i
    · change H.degree (f (LockLiftRelabel.lift σ (Fin.last 9)))=degrees g (Fin.last 9)
      rw [LockLiftRelabel.lift_last]
      simpa only [degrees,Fin.val_last,lt_self_iff_false,if_false] using degreeEq.symm
    · change H.degree (f (LockLiftRelabel.lift σ j.castSucc))=degrees g j.castSucc
      rw [LockLiftRelabel.lift_castSucc]
      rw [low (σ j).castSucc (σ j).isLt]
      change 6=if j.val<9 then 6 else lastDegree g
      rw [if_pos j.isLt]
  exact notB (TwentyFiveNineLowTenthComplete.propertyB_of_group H edges new newUnit g newDegrees newOld)

end Aris4Math.ThirtyFour.TwentyFiveNineLowComplete

#print axioms Aris4Math.ThirtyFour.TwentyFiveNineLowComplete.propertyB
