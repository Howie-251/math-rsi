import DegreeDiameter.Portfolio.OppositeGQ35SpreadFastTables
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

/-- Check just the384 positive line incidences, rather than64*96 membership
implications repeatedly in each projection row. -/
theorem pointLine_inverse : ∀ l i, ∃ j, fastPointLine (fastLinePoint l i) j = l := by decide

theorem pointLine_covers_literal : ∀ p l, Inc p l → ∃ i, pointLine p i = l := by
  rintro p l ⟨i,rfl⟩
  simpa only [linePoint_eq_fast,pointLine_eq_fast] using pointLine_inverse l i

/-- Each of the64 points in the16 vertical rows has the stated owner. -/
theorem spread_owner_on_rows : ∀ j i, spreadOwner (fastLinePoint (spread j) i) = j := by decide

theorem spread_unique_literal : ∀ p j, Inc p (spread j) → j = spreadOwner p := by
  rintro p j ⟨i,rfl⟩
  rw [linePoint_eq_fast]
  exact (spread_owner_on_rows j i).symm
#print axioms pointLine_covers_literal
#print axioms spread_unique_literal
end DegreeDiameter.Portfolio.OppositeGQ35Spread
