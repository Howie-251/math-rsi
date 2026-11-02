import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceChunk0
import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceChunk1
import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceChunk2
import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceChunk3
import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceChunk4
import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceChunk5
import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceChunk6
import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidenceChunk7
import Mathlib.Tactic.FinCases
namespace DegreeDiameter.Portfolio.OppositeGQ77Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
theorem incidence_chunks : ∀ k, IncidenceChunkCheck k := by
  intro k
  fin_cases k
  · exact incidence_chunk_0
  · exact incidence_chunk_1
  · exact incidence_chunk_2
  · exact incidence_chunk_3
  · exact incidence_chunk_4
  · exact incidence_chunk_5
  · exact incidence_chunk_6
  · exact incidence_chunk_7
theorem pointLine_inverse (l : Line) (i : Fin 8) :
    pointLine (linePoint l i) (lpPosition l i) = l := by
  let kr := (finProdFinEquiv (m:=8) (n:=50)).symm l
  have h := (incidence_chunks kr.1).1 kr.2 i
  simpa only [blockIndex,kr,Prod.mk.eta,Equiv.apply_symm_apply] using h
theorem pointLine_covers : ∀ p l, Inc p l → ∃ i, pointLine p i = l := by
  rintro p l ⟨i,rfl⟩
  exact ⟨lpPosition l i,pointLine_inverse l i⟩
theorem pointLine_sound (p : Point) (j : Fin 8) : Inc p (pointLine p j) := by
  let kr := (finProdFinEquiv (m:=8) (n:=50)).symm p
  have h := (incidence_chunks kr.1).2 kr.2 j
  refine ⟨plPosition p j,?_⟩
  simpa only [blockIndex,kr,Prod.mk.eta,Equiv.apply_symm_apply] using h
theorem spread_owner_on_rows : ∀ j i, spreadOwner (linePoint (spread j) i) = j := by decide
theorem spread_unique : ∀ p j, Inc p (spread j) → j = spreadOwner p := by
  rintro p j ⟨i,rfl⟩
  exact (spread_owner_on_rows j i).symm
#print axioms pointLine_covers
#print axioms pointLine_sound
#print axioms spread_unique
end DegreeDiameter.Portfolio.OppositeGQ77Spread
