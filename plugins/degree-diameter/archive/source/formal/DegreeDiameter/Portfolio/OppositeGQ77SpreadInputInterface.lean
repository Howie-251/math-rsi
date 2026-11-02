import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidence
namespace DegreeDiameter.Portfolio.OppositeGQ77Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

/-- Three actual Fin8 positions. First and second incidences come from membership
and shared soundness; the remaining equality is discharged in each concrete row. -/
def ProjectionIndexCheck (p : Point) (ix : Line → Fin 8 × Fin 8 × Fin 8) : Prop :=
  ∀ l, linePoint (pointLine p (ix l).2.1) (ix l).2.2 = linePoint l (ix l).1
def ProjectionRow (p : Point) : Prop := ∀ l, ∃ q m, Inc q l ∧ Inc p m ∧ Inc q m
theorem projection_row_of_check (p : Point) (ix : Line → Fin 8 × Fin 8 × Fin 8)
    (h : ProjectionIndexCheck p ix) : ProjectionRow p := by
  intro l
  exact ⟨linePoint l (ix l).1,pointLine p (ix l).2.1,
    ⟨(ix l).1,rfl⟩,pointLine_sound p (ix l).2.1,⟨(ix l).2.2,h l⟩⟩
#print axioms projection_row_of_check
end DegreeDiameter.Portfolio.OppositeGQ77Spread
