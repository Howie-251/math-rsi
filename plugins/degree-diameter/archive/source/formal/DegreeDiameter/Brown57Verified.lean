import DegreeDiameter.Moore

namespace DegreeDiameter

/-- The normalized projective representatives, in the generator's exact order. -/
def brownCoords (v : Fin 57) : ℕ × ℕ × ℕ :=
  if v.val < 49 then (1, v.val / 7, v.val % 7)
  else if v.val < 56 then (0, 1, v.val - 49)
  else (0, 0, 1)

/-- Dot product in F₇, implemented by exact natural arithmetic modulo seven. -/
def brownDot (u v : Fin 57) : ℕ :=
  ((brownCoords u).1 * (brownCoords v).1 +
    (brownCoords u).2.1 * (brownCoords v).2.1 +
    (brownCoords u).2.2 * (brownCoords v).2.2) % 7

/-- The complete adjacency rule, with self-loops explicitly excluded. -/
def brownAdj (u v : Fin 57) : Prop := u ≠ v ∧ brownDot u v = 0

instance brownAdjDecidable : DecidableRel brownAdj := fun _ _ =>
  inferInstanceAs (Decidable (_ ≠ _ ∧ _ = (0 : ℕ)))

/-- The actual 57-vertex graph, rather than an assumed certificate. -/
def brown57 : SimpleGraph (Fin 57) where
  Adj := brownAdj
  symm := by
    intro u v h
    exact ⟨Ne.symm h.1, by simpa [brownDot, Nat.mul_comm] using h.2⟩
  loopless := by intro v h; exact h.1 rfl

instance : DecidableRel brown57.Adj := brownAdjDecidable

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
/-- Exhaustively checks the actual degree of each of the 57 vertices. -/
theorem brown57_computable_degree : ∀ v, brown57.degree v ≤ 8 := by
  decide

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
/-- Exhaustively checks every ordered pair against the genuine path condition. -/
theorem brown57_diameter : diameterAtMostTwo brown57 := by
  unfold diameterAtMostTwo
  decide

end DegreeDiameter
