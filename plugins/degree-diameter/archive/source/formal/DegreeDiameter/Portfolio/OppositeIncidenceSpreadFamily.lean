import DegreeDiameter.Portfolio.OppositeIncidenceSpreadSlots
import DegreeDiameter.Portfolio.OppositeGQ35SpreadWalks
import DegreeDiameter.Portfolio.OppositeGQ35SpreadLowerGeneric
namespace DegreeDiameter.Portfolio.OppositeIncidenceSpread
open SimpleGraph
variable {P L V J : Type*} {a b : Nat}

/-- A supplied old-label equivalence gives the stated order independently of
any incidence, projection or degree hypotheses. -/
theorem card_family [Fintype P] [Fintype L] [Fintype V] [Fintype J]
    (e : V ≃ P × L) : Fintype.card (V ⊕ J) = Fintype.card P * Fintype.card L + Fintype.card J := by
  rw [Fintype.card_sum,Fintype.card_congr e,Fintype.card_prod]

theorem diameterAtMost_three (e : V ≃ P × L)
    (linePoint : L → Fin a → P) (spread : J → L) (ha : 0 < a)
    (project : ∀ p l, ∃ q m, Inc linePoint q l ∧ Inc linePoint p m ∧ Inc linePoint q m) :
    DiameterAtMost (graph e linePoint spread) 3 := by
  apply OppositeGQSpread.diameter_three e (Inc linePoint) spread project
  intro j
  exact ⟨linePoint (spread j) ⟨0,ha⟩,⟨0,ha⟩,rfl⟩

/-- With more than the k-step radius-two endpoint capacity, the same neighbor
cover proves a lower bound for actual Walk distance. No geometry existence or
uniqueness assertion is hidden in this interface. -/
theorem not_diameterAtMost_two [Fintype P] [Fintype L] [Fintype V] [Fintype J]
    [DecidableEq V] [DecidableEq P]
    (e : V ≃ P × L) (linePoint : L → Fin a → P)
    (pointLine : P → Fin b → L) (spread : J → L) (spreadOwner : P → J)
    (hline : ∀ p l, Inc linePoint p l → ∃ i, pointLine p i = l)
    (howner : ∀ p j, Inc linePoint p (spread j) → j = spreadOwner p)
    (hlarge : 1+a*b+(a*b)^2 < Fintype.card P * Fintype.card L + Fintype.card J) :
    ¬DiameterAtMost (graph e linePoint spread) 2 := by
  have hcard := card_family e (J:=J)
  have hpos : 0 < Fintype.card (V ⊕ J) := by rw [hcard]; omega
  letI : Nonempty (V ⊕ J) := Fintype.card_pos_iff.mp hpos
  intro hD
  have hsmall := OppositeGQSpread.diameter_two_card_le (graph e linePoint spread) (a*b)
    (forward e linePoint pointLine spread spreadOwner)
    (forward_covers e linePoint pointLine spread spreadOwner hline howner) hD
  rw [hcard] at hsmall
  have hlarge' : 1+a*b+(a*b)*(a*b) < Fintype.card P * Fintype.card L + Fintype.card J := by
    simpa only [pow_two] using hlarge
  exact (Nat.not_le_of_gt hlarge') hsmall

/-- Conditional family interface: concrete callers must construct and prove
all listed finite inputs. This theorem does not assert that such geometries
exist for arbitrary a,b,or field size. -/
theorem order_degree_and_exact_D3 [Fintype P] [Fintype L] [Fintype V] [Fintype J]
    [DecidableEq V] [DecidableEq P]
    (e : V ≃ P × L) (linePoint : L → Fin a → P)
    (pointLine : P → Fin b → L) (spread : J → L) (spreadOwner : P → J)
    (ha : 0 < a)
    (hline : ∀ p l, Inc linePoint p l → ∃ i, pointLine p i = l)
    (howner : ∀ p j, Inc linePoint p (spread j) → j = spreadOwner p)
    (project : ∀ p l, ∃ q m, Inc linePoint q l ∧ Inc linePoint p m ∧ Inc linePoint q m)
    (hlarge : 1+a*b+(a*b)^2 < Fintype.card P * Fintype.card L + Fintype.card J) :
    Fintype.card (V ⊕ J) = Fintype.card P * Fintype.card L + Fintype.card J ∧
      (∀ u, (graph e linePoint spread).degree u ≤ a*b) ∧
      DiameterAtMost (graph e linePoint spread) 3 ∧ ¬DiameterAtMost (graph e linePoint spread) 2 := by
  exact ⟨card_family e,degree_le e linePoint pointLine spread spreadOwner hline howner,
    diameterAtMost_three e linePoint spread ha project,
    not_diameterAtMost_two e linePoint pointLine spread spreadOwner hline howner hlarge⟩
#print axioms card_family
#print axioms diameterAtMost_three
#print axioms not_diameterAtMost_two
#print axioms order_degree_and_exact_D3
end DegreeDiameter.Portfolio.OppositeIncidenceSpread
