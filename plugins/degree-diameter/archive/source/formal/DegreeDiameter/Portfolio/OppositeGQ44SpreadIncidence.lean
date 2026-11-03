import DegreeDiameter.Portfolio.OppositeGQ44SpreadDefinitions
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- Only the425 positive line-point incidences need through-line coverage. -/
theorem pointLine_inverse : ∀ l i, ∃ j, pointLine (linePoint l i) j = l := by decide
theorem pointLine_covers : ∀ p l, Inc p l → ∃ i, pointLine p i = l := by
  rintro p l ⟨i,rfl⟩
  exact pointLine_inverse l i
/-- Positive through-line entries allow projection rows to use one equality. -/
theorem pointLine_sound : ∀ p j, Inc p (pointLine p j) := by
  unfold Inc OppositeIncidenceSpread.Inc
  decide
theorem spread_owner_on_rows : ∀ j i, spreadOwner (linePoint (spread j) i) = j := by decide
theorem spread_unique : ∀ p j, Inc p (spread j) → j = spreadOwner p := by
  rintro p j ⟨i,rfl⟩
  exact (spread_owner_on_rows j i).symm
#print axioms pointLine_covers
#print axioms pointLine_sound
#print axioms spread_unique
end DegreeDiameter.Portfolio.OppositeGQ44Spread
