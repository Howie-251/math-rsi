import DegreeDiameter.Portfolio.OppositeGQ44SpreadIncidence
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- Three Fin5 indices: q in target l; m in pointLine(p); q in m.
The first two incidences follow from definitions and pointLine_sound; only
this equality is checked per projection. -/
def ProjectionIndexCheck (p : Point) (ix : Line → Fin 5 × Fin 5 × Fin 5) : Prop :=
  ∀ l, linePoint (pointLine p (ix l).2.1) (ix l).2.2 = linePoint l (ix l).1

def ProjectionRow (p : Point) : Prop := ∀ l, ∃ q m, Inc q l ∧ Inc p m ∧ Inc q m

theorem projection_row_of_check (p : Point) (ix : Line → Fin 5 × Fin 5 × Fin 5)
    (h : ProjectionIndexCheck p ix) : ProjectionRow p := by
  intro l
  exact ⟨linePoint l (ix l).1,pointLine p (ix l).2.1,
    ⟨(ix l).1,rfl⟩,pointLine_sound p (ix l).2.1,⟨(ix l).2.2,h l⟩⟩
#print axioms projection_row_of_check
end DegreeDiameter.Portfolio.OppositeGQ44Spread
