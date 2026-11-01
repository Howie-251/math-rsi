import Aris4Math.ThirtyFour.TwentyFiveUnitConditional

/-! A failed degree budget needs only a short list of distinct incident blocks.
The list checker never constructs the full pair completion. -/
namespace Aris4Math.ThirtyFour.TwentyFiveDegreeObstruction
open Aris4Math.K6Classification TwentyFiveUnitCounts
variable {n : ℕ}

def blockCheck (listed : List (Finset (Fin n))) (T : Finset (Fin n)) : Bool :=
  listed.contains T || (decide (T.card=2) && listed.all (fun B => decide (¬ T⊆B)))

theorem block_mem (listed : List (Finset (Fin n))) (T : Finset (Fin n))
    (checked : blockCheck listed T=true) : T∈pairCompletion listed.toFinset := by
  simp only [blockCheck,Bool.or_eq_true,Bool.and_eq_true,List.contains_iff,
    decide_eq_true_eq] at checked
  rcases checked with mem | ⟨size,none⟩
  · exact Finset.mem_union_left _ (List.mem_toFinset.mpr mem)
  · apply Finset.mem_union_right
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _,size⟩,?_⟩
    intro B mem
    exact of_decide_eq_true (List.all_eq_true.mp none B (List.mem_toFinset.mp mem))

theorem not_feasible (degree : Fin n → ℕ) (listed bad : List (Finset (Fin n)))
    (i : Fin n) (nodup : bad.Nodup) (enough : degree i<bad.length)
    (checked : bad.all (fun T => decide (i∈T) && blockCheck listed T)=true) :
    ¬ Feasible 34 degree (pairCompletion listed.toFinset) := by
  intro feasible
  have subset : bad.toFinset⊆(pairCompletion listed.toFinset).filter (fun T => i∈T) := by
    intro T mem
    have h := List.all_eq_true.mp checked T (List.mem_toFinset.mp mem)
    simp only [Bool.and_eq_true] at h
    rcases h with ⟨through,valid⟩
    exact Finset.mem_filter.mpr ⟨block_mem listed T valid,of_decide_eq_true through⟩
  have lower := Finset.card_le_card subset
  rw [List.toFinset_card_of_nodup nodup] at lower
  exact (not_lt_of_ge (le_trans lower (feasible.1 i))) enough

end Aris4Math.ThirtyFour.TwentyFiveDegreeObstruction


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

end Aris4Math.ThirtyFour.TwentyFiveConditionalRows