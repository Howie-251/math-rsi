import Aris4Math.ThirtyFour.TwentyFourSixLowUnitFiveBlock
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage0
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage2
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage4
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitActual

namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitStrict
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFourSixLowUnitData

theorem five_block_counts : ∀T,
    TwentyFourSixLowUnitFiveBlockData.μ 0 T=μ 6 T := by decide +kernel

/-- The five strict canonical types use their actual coloring callers. -/
theorem propertyB_of_strict_type (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (f : Fin 6↪Fin 24) (i : Case)
    (actual : ∀T,count H f T=μ i T)
    (degrees : ∀j,H.degree (f j)=6)
    (unit : ∀j k,j≠k→H.codegree (f j) (f k)=1)
    (strict : i=0 ∨ i=2 ∨ i=4 ∨ i=6 ∨ i=7) : PropertyB H := by
  rcases strict with rfl | rfl | rfl | rfl | rfl
  · exact TwentyFourSixLowUnitAverage0.propertyB_of_counts H cover f actual degrees unit
  · exact TwentyFourSixLowUnitAverage2.propertyB_of_counts H cover f actual degrees unit
  · exact TwentyFourSixLowUnitAverage4.propertyB_of_counts H cover f actual degrees unit
  · apply TwentyFourSixLowUnitFiveBlock.propertyB_of_counts H f 0
    intro T
    rw [five_block_counts]
    exact actual T
  · exact TwentyFourSixLowUnitAverage7.propertyB_of_counts H cover f actual degrees unit

theorem actual_residual (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (size : H.edges.card=34) (f : Fin 6↪Fin 24)
    (degrees : ∀j,H.degree (f j)=6)
    (unit : ∀j k,j≠k→H.codegree (f j) (f k)=1) (noB : ¬PropertyB H) :
    ∃i : Case,∃σ : Equiv.Perm (Fin 6),
      (i=1 ∨ i=3 ∨ i=5 ∨ i=8) ∧
      ∀T,count H (σ.toEmbedding.trans f) T=μ i T := by
  obtain ⟨i,σ,actual⟩ := TwentyFourSixLowUnitActual.actual_classification H size f degrees unit
  refine ⟨i,σ,?_,actual⟩
  by_contra outside
  have strict : i=0 ∨ i=2 ∨ i=4 ∨ i=6 ∨ i=7 := by
    fin_cases i <;> simp_all
  exact noB (propertyB_of_strict_type H cover (σ.toEmbedding.trans f) i actual
    (fun j=>degrees (σ j)) (fun j k ne=>unit (σ j) (σ k) (σ.injective.ne ne)) strict)
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitStrict
