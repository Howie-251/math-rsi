import Aris4Math.ThirtyFour.TwentyFiveUnitConditional
import Aris4Math.ThirtyFour.TwentyFiveDegreeObstruction

/-! Each checked row carries its selected blocks and its actual witness.
The full recursive choice set is bound once to the row projections. -/
namespace Aris4Math.ThirtyFour.TwentyFiveConditionalRows
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitConditional
open TwentyFiveDegreeObstruction
variable {n m : ℕ}

structure Rejection (n : ℕ) where
  listed : List (Finset (Fin n))
  incident : List (Finset (Fin n))
  vertex : Fin n

structure Row (n m : ℕ) where
  selected : Finset (Finset (Fin n))
  witness : Witness (n+1) m
  rejection : Option (Rejection (n+1))

def QuickCheck (degree : Fin (n+1) → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (targetDegree : Fin m → Fin (n+1) → ℕ)
    (big : Finset (Finset (Fin n))) (r : Row n m) : Prop :=
  match r.rejection with
  | none => Function.Injective r.witness.permutation ∧
      (∀ i, targetDegree r.witness.target (r.witness.permutation i)=degree i) ∧
      (extend big r.selected).image (fun T => T.image r.witness.permutation)=catalogue r.witness.target
  | some no => extend big r.selected=no.listed.toFinset ∧ no.incident.Nodup ∧
      degree no.vertex<no.incident.length ∧
      no.incident.all (fun T => decide (no.vertex∈T) && blockCheck no.listed T)=true

instance (degree : Fin (n+1) → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (targetDegree : Fin m → Fin (n+1) → ℕ)
    (big : Finset (Finset (Fin n))) (r : Row n m) :
    Decidable (QuickCheck degree catalogue targetDegree big r) := by
  unfold QuickCheck
  split <;> infer_instance

theorem quick_sound (degree : Fin (n+1) → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (targetDegree : Fin m → Fin (n+1) → ℕ)
    (big : Finset (Finset (Fin n))) (r : Row n m)
    (quick : QuickCheck degree catalogue targetDegree big r) :
    Checks degree catalogue targetDegree big r.selected r.witness := by
  intro feasible
  unfold QuickCheck at quick
  split at quick
  · exact quick
  · rename_i no eq
    rcases quick with ⟨same,nodup,enough,checked⟩
    rw [same] at feasible
    exact False.elim (not_feasible degree no.listed no.incident no.vertex nodup enough checked feasible)

theorem checked_rows (degree : Fin (n+1) → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (targetDegree : Fin m → Fin (n+1) → ℕ)
    (big : Finset (Finset (Fin n))) (rows : List (Row n m))
    (checked : rows.all (fun r => decide (QuickCheck degree catalogue targetDegree big r))=true) :
    List.Forall₂ (Checks degree catalogue targetDegree big)
      (rows.map Row.selected) (rows.map Row.witness) := by
  induction rows with
  | nil => exact .nil
  | cons r rest ih =>
    simp only [List.all_cons,Bool.and_eq_true,decide_eq_true_eq] at checked
    exact .cons (quick_sound degree catalogue targetDegree big r checked.1) (ih checked.2)

structure FamilyRow (n m : ℕ) where
  source : Finset (Finset (Fin n))
  target : Fin m
  rejection : Option (Rejection n)

def FamilyCheck (degree : Fin n → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin n))) (r : FamilyRow n m) : Prop :=
  match r.rejection with
  | none => r.source=catalogue r.target
  | some no => r.source=no.listed.toFinset ∧ no.incident.Nodup ∧
      degree no.vertex<no.incident.length ∧
      no.incident.all (fun T => decide (no.vertex∈T) && blockCheck no.listed T)=true

instance (degree : Fin n → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin n))) (r : FamilyRow n m) :
    Decidable (FamilyCheck degree catalogue r) := by
  unfold FamilyCheck
  split <;> infer_instance

theorem family_sound (degree : Fin n → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin n))) (r : FamilyRow n m)
    (checked : FamilyCheck degree catalogue r)
    (feasible : TwentyFiveUnitCounts.Feasible 34 degree
      (Aris4Math.K6Classification.pairCompletion r.source)) : r.source=catalogue r.target := by
  unfold FamilyCheck at checked
  split at checked
  · exact checked
  · rename_i no eq
    rcases checked with ⟨same,nodup,enough,valid⟩
    rw [same] at feasible
    exact False.elim (not_feasible degree no.listed no.incident no.vertex nodup enough valid feasible)

end Aris4Math.ThirtyFour.TwentyFiveConditionalRows
