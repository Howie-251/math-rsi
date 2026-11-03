import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputData
import DegreeDiameter.Portfolio.OppositeGQ35SpreadIncidence
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- Three supplied incidence indices avoid repeated existential searches.
The checks remain equalities about the original projection point and line. -/
def ProjectionIndexCheck (p : Point) (ix : Line → Fin 4 × Fin 4 × Fin 4) : Prop :=
  ∀ l, fastLinePoint l (ix l).1 = projectionPoint p l ∧
    fastLinePoint (projectionLine p l) (ix l).2.1 = p ∧
    fastLinePoint (projectionLine p l) (ix l).2.2 = projectionPoint p l

theorem inputRow_of_checks (p : Point) (ix : Line → Fin 4 × Fin 4 × Fin 4)
    (h : ProjectionIndexCheck p ix) : InputRow p := by
  refine ⟨?_,pointLine_covers_literal p,spread_unique_literal p⟩
  intro l
  exact ⟨⟨(ix l).1,(linePoint_eq_fast _ _).trans (h l).1⟩,
    ⟨(ix l).2.1,(linePoint_eq_fast _ _).trans (h l).2.1⟩,
    ⟨(ix l).2.2,(linePoint_eq_fast _ _).trans (h l).2.2⟩⟩
end DegreeDiameter.Portfolio.OppositeGQ35Spread
