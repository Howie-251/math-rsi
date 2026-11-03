import DegreeDiameter.Portfolio.OppositeGQ35SpreadSlots
namespace DegreeDiameter.Portfolio.OppositeIncidenceSpread
open SimpleGraph
variable {P L V J : Type*} {a b : Nat}

/-- Incidence is exactly membership in the supplied finite line-point list.
No geometry existence assertion is part of this definition. -/
def Inc (linePoint : L → Fin a → P) (p : P) (l : L) : Prop :=
  ∃ i, linePoint l i = p
instance (linePoint : L → Fin a → P) [DecidableEq P] :
    DecidableRel (Inc linePoint) := fun p l =>
  inferInstanceAs (Decidable (∃ i, linePoint l i = p))

/-- Keep the old labels through the explicit equivalence e. The new vertex j
is joined to precisely the old flags whose point is on spread j. -/
def graph (e : V ≃ P × L) (linePoint : L → Fin a → P) (spread : J → L) :
    SimpleGraph (V ⊕ J) := OppositeGQSpread.graph e (Inc linePoint) spread
instance (e : V ≃ P × L) (linePoint : L → Fin a → P) (spread : J → L)
    [DecidableEq V] [DecidableEq P] : DecidableRel (graph e linePoint spread).Adj :=
  inferInstanceAs (DecidableRel (OppositeGQSpread.graph e (Inc linePoint) spread).Adj)

def forward [DecidableEq V] (e : V ≃ P × L) (linePoint : L → Fin a → P)
    (pointLine : P → Fin b → L) (spread : J → L) (spreadOwner : P → J)
    (u : V ⊕ J) (i : Fin (a*b)) : V ⊕ J :=
  OppositeGQSpread.slot e spread spreadOwner linePoint pointLine u
    ((finProdFinEquiv (m:=a) (n:=b)).symm i)

/-- The actual incidence list must be covered by the b through-point slots.
The spread-owner condition concerns each actual spread incidence, including
repeated candidate spread labels. Neither property is assumed by graph itself. -/
theorem forward_covers [DecidableEq V]
    (e : V ≃ P × L) (linePoint : L → Fin a → P)
    (pointLine : P → Fin b → L) (spread : J → L) (spreadOwner : P → J)
    (hline : ∀ p l, Inc linePoint p l → ∃ i, pointLine p i = l)
    (howner : ∀ p j, Inc linePoint p (spread j) → j = spreadOwner p) :
    ∀ u v, (graph e linePoint spread).Adj u v →
      ∃ i, forward e linePoint pointLine spread spreadOwner u i = v := by
  intro u v h
  obtain ⟨ij,hij⟩ := OppositeGQSpread.slot_covers e (Inc linePoint) spread spreadOwner linePoint pointLine
    (fun _ _ h => h) hline howner u v h
  exact ⟨finProdFinEquiv ij,by simpa only [forward,Equiv.symm_apply_apply] using hij⟩

theorem degree_le [Fintype V] [Fintype J] [DecidableEq V] [DecidableEq P]
    (e : V ≃ P × L) (linePoint : L → Fin a → P)
    (pointLine : P → Fin b → L) (spread : J → L) (spreadOwner : P → J)
    (hline : ∀ p l, Inc linePoint p l → ∃ i, pointLine p i = l)
    (howner : ∀ p j, Inc linePoint p (spread j) → j = spreadOwner p) :
    ∀ u, (graph e linePoint spread).degree u ≤ a*b := by
  simpa only [Fintype.card_fin] using OppositeGQSpread.degree_le_of_cover
    (graph e linePoint spread) (forward e linePoint pointLine spread spreadOwner)
    (forward_covers e linePoint pointLine spread spreadOwner hline howner)
#print axioms forward_covers
#print axioms degree_le
end DegreeDiameter.Portfolio.OppositeIncidenceSpread
