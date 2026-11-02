import DegreeDiameter.Portfolio.EvenQ8SourceDefinitions
namespace DegreeDiameter.Portfolio.EvenQ8Source
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
namespace Derived
/-- All 640 point/line pairs at actual point 511,with two checked equalities
and the first incidence given by qSlot itself. -/
theorem complete_last_projection_row_certificate : ∀ l : Line,
    linePoint (connector l) (pSlot l) = lastPoint ∧
    linePoint (connector l) (qConnectorSlot l) = linePoint l (qSlot l) := by decide
theorem complete_last_projection_row : ∀ l : Line,
    ∃ q m, Inc q l ∧ Inc lastPoint m ∧ Inc q m := by
  intro l
  refine ⟨linePoint l (qSlot l),connector l,⟨qSlot l,rfl⟩,?_,?_⟩
  · exact ⟨pSlot l,(complete_last_projection_row_certificate l).1⟩
  · exact ⟨qConnectorSlot l,(complete_last_projection_row_certificate l).2⟩
theorem representative_hline_certificate : ∀ i : Fin 8,
    pointLine (linePoint lastLine i) (lastLineInverseSlot i) = lastLine := by decide
theorem representative_hline : ∀ p, Inc p lastLine → ∃ i, pointLine p i = lastLine := by
  intro p h
  obtain ⟨i,hi⟩ := h
  refine ⟨lastLineInverseSlot i,?_⟩
  rw [←hi]
  exact representative_hline_certificate i
theorem representative_howner_certificate : ∀ i : Fin 8,
    spreadOwner (linePoint (spread lastSpread) i) = lastSpread := by decide
theorem representative_howner : ∀ p, Inc p (spread lastSpread) → lastSpread = spreadOwner p := by
  intro p h
  obtain ⟨i,hi⟩ := h
  rw [←hi]
  exact (representative_howner_certificate i).symm
#check complete_last_projection_row
#print axioms complete_last_projection_row
#print axioms representative_hline
#print axioms representative_howner
end Derived
namespace Balanced
/-- All 585 point/line pairs at actual point 584,with two checked equalities
and the first incidence given by qSlot itself. -/
theorem complete_last_projection_row_certificate : ∀ l : Line,
    linePoint (connector l) (pSlot l) = lastPoint ∧
    linePoint (connector l) (qConnectorSlot l) = linePoint l (qSlot l) := by decide
theorem complete_last_projection_row : ∀ l : Line,
    ∃ q m, Inc q l ∧ Inc lastPoint m ∧ Inc q m := by
  intro l
  refine ⟨linePoint l (qSlot l),connector l,⟨qSlot l,rfl⟩,?_,?_⟩
  · exact ⟨pSlot l,(complete_last_projection_row_certificate l).1⟩
  · exact ⟨qConnectorSlot l,(complete_last_projection_row_certificate l).2⟩
theorem representative_hline_certificate : ∀ i : Fin 9,
    pointLine (linePoint lastLine i) (lastLineInverseSlot i) = lastLine := by decide
theorem representative_hline : ∀ p, Inc p lastLine → ∃ i, pointLine p i = lastLine := by
  intro p h
  obtain ⟨i,hi⟩ := h
  refine ⟨lastLineInverseSlot i,?_⟩
  rw [←hi]
  exact representative_hline_certificate i
theorem representative_howner_certificate : ∀ i : Fin 9,
    spreadOwner (linePoint (spread lastSpread) i) = lastSpread := by decide
theorem representative_howner : ∀ p, Inc p (spread lastSpread) → lastSpread = spreadOwner p := by
  intro p h
  obtain ⟨i,hi⟩ := h
  rw [←hi]
  exact (representative_howner_certificate i).symm
#check complete_last_projection_row
#print axioms complete_last_projection_row
#print axioms representative_hline
#print axioms representative_howner
end Balanced
end DegreeDiameter.Portfolio.EvenQ8Source
