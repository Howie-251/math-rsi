import Aris4Math.ThirtyFour.TwentyFiveConditionalRows
import Aris4Math.ThirtyFour.TwentyFiveSparseCompletion


/-! Bind a degree-colored local catalogue to the original ordered locks.
Uncolored normalization may permute low-degree vertices; their actual set is
transported explicitly before the degree-colored classification is applied. -/
namespace Aris4Math.ThirtyFour.TwentyFiveColoredActual
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitCounts
variable {n m t v : ℕ}

def standard (q : ℕ) (i : Fin n) : ℕ := if i.val<q then 6 else 7
def colors (low : Finset (Fin n)) (i : Fin n) : ℕ := if i∈low then 6 else 7
def lowSet (q : ℕ) (σ : Equiv.Perm (Fin n)) : Finset (Fin n) :=
  (Finset.univ.filter fun i : Fin n => i.val<q).map σ.symm.toEmbedding

@[simp] theorem mem_lowSet (q : ℕ) (σ : Equiv.Perm (Fin n)) (i : Fin n) :
    i∈lowSet q σ ↔ (σ i).val<q := by
  simp [lowSet]

theorem lowSet_card (q : ℕ) (σ : Equiv.Perm (Fin n))
    (size : (Finset.univ.filter fun i : Fin n => i.val<q).card=q) :
    (lowSet q σ).card=q := by simpa only [lowSet,Finset.card_map] using size

/-- The finite colored table is the only remaining local hypothesis. Its
permutation preserves every actual low/high degree and transports the exact
large-block family. The output retains an actual permutation for later lifts. -/
theorem actual (H : Simple5Hypergraph (Fin v)) (edges : H.edges.card=34)
    (f : Fin n↪Fin v) (unit : Unit H f) (q : ℕ)
    (degrees : ∀ i,H.degree (f i)=standard q i)
    (size : (Finset.univ.filter fun i : Fin n => i.val<q).card=q)
    (base : Fin m → Finset (Finset (Fin n))) (base_covers : Covers base)
    (target : Fin t → Finset (Finset (Fin n)))
    (table : ∀ c (low : Finset (Fin n)), low.card=q →
      Feasible 34 (colors low) (pairCompletion (base c)) →
      ∃ d : Fin t, ∃ τ : Equiv.Perm (Fin n),
        (∀ i,standard q (τ i)=colors low i) ∧
        (base c).image (fun T => T.map τ.toEmbedding)=target d) :
    ∃ d : Fin t, ∃ σ : Equiv.Perm (Fin n),
      large H (σ.toEmbedding.trans f)=target d ∧
      (∀ i,H.degree ((σ.toEmbedding.trans f) i)=standard q i) ∧
      (∀ T,count H (σ.toEmbedding.trans f) T=
        inventory 34 (standard q) (pairCompletion (target d)) T) := by
  obtain ⟨c,σ,base_eq⟩ := base_covers H f unit
  let g := σ.toEmbedding.trans f
  have gu : Unit H g := unit_relabel H f unit σ
  have gd (i : Fin n) : H.degree (g i)=colors (lowSet q σ) i := by
    change H.degree (f (σ i))=colors (lowSet q σ) i
    rw [degrees]
    simp only [standard,colors,mem_lowSet]
  have feasible := (actual_inventory H g gu (colors (lowSet q σ)) gd).2
  rw [edges,show large H g=base c from base_eq] at feasible
  obtain ⟨d,τ,moves,family⟩ := table c (lowSet q σ) (lowSet_card q σ size) feasible
  let ρ := τ.symm.trans σ
  let new := ρ.toEmbedding.trans f
  have new_eq : new=τ.symm.toEmbedding.trans g := by rfl
  have nu : Unit H new := unit_relabel H f unit ρ
  have nd (i : Fin n) : H.degree (new i)=standard q i := by
    change H.degree (g (τ.symm i))=standard q i
    rw [gd]
    simpa using (moves (τ.symm i)).symm
  have nf : large H new=target d := by
    rw [new_eq,large_relabel,show large H g=base c from base_eq]
    exact family
  refine ⟨d,ρ,nf,nd,?_⟩
  have counts := (actual_inventory H new nu (standard q) nd).1
  rw [edges,nf] at counts
  exact counts

end Aris4Math.ThirtyFour.TwentyFiveColoredActual

/-! Direct degree-colored rows, with either a real label bijection or a short
explicit impossibility certificate. The budget alternative is needed only
for the 252 degree-feasible q=5 labels whose recovered edge count is too large. -/
namespace Aris4Math.ThirtyFour.TwentyFiveColoredRows
open Aris4Math.K6Classification TwentyFiveUnitCatalogue TwentyFiveUnitCounts
open TwentyFiveDegreeObstruction TwentyFiveColoredActual TwentyFiveConditionalRows
variable {n m : ℕ}

structure Row (n m : ℕ) where
  listed : List (Finset (Fin n))
  low : Finset (Fin n)
  witness : Witness n m
  rejection : Option (Sum (Rejection n) (List (Finset (Fin n))))

def source (r : Row n m) := (r.listed.toFinset,r.low)

def Check (q : ℕ) (catalogue : Fin m → Finset (Finset (Fin n))) (r : Row n m) : Prop :=
  match r.rejection with
  | none => Function.Injective r.witness.permutation ∧
      (∀ i,standard q (r.witness.permutation i)=colors r.low i) ∧
      r.listed.toFinset.image (fun T => T.image r.witness.permutation)=catalogue r.witness.target
  | some (.inl no) => r.listed.toFinset=no.listed.toFinset ∧ no.incident.Nodup ∧
      colors r.low no.vertex<no.incident.length ∧
      no.incident.all (fun T => decide (no.vertex∈T) && blockCheck no.listed T)=true
  | some (.inr full) => TwentyFiveSparseCompletion.Check r.listed full=true ∧
      ¬ Feasible 34 (colors r.low) full.toFinset

instance (q : ℕ) (catalogue : Fin m → Finset (Finset (Fin n))) (r : Row n m) :
    Decidable (Check q catalogue r) := by
  unfold Check
  split <;> infer_instance

theorem direct_sound (q : ℕ) (catalogue : Fin m → Finset (Finset (Fin n))) (r : Row n m)
    (checked : Check q catalogue r)
    (feasible : Feasible 34 (colors r.low) (pairCompletion r.listed.toFinset)) :
    Function.Injective r.witness.permutation ∧
      (∀ i,standard q (r.witness.permutation i)=colors r.low i) ∧
      r.listed.toFinset.image (fun T => T.image r.witness.permutation)=catalogue r.witness.target := by
  unfold Check at checked
  split at checked
  · exact checked
  · rename_i no eq
    rcases checked with ⟨same,nodup,enough,valid⟩
    rw [same] at feasible
    exact False.elim (not_feasible (colors r.low) no.listed no.incident no.vertex nodup enough valid feasible)
  · rename_i full eq
    rw [TwentyFiveSparseCompletion.complete r.listed full checked.1] at feasible
    exact False.elim (checked.2 feasible)

theorem sound (q : ℕ) (catalogue : Fin m → Finset (Finset (Fin n))) (r : Row n m)
    (checked : Check q catalogue r)
    (feasible : Feasible 34 (colors r.low) (pairCompletion r.listed.toFinset)) :
    ∃ τ : Equiv.Perm (Fin n),
      (∀ i,standard q (τ i)=colors r.low i) ∧
      r.listed.toFinset.image (fun T => T.map τ.toEmbedding)=catalogue r.witness.target := by
  unfold Check at checked
  split at checked
  · obtain ⟨inj,degrees,family⟩ := checked
    let τ := Equiv.ofBijective r.witness.permutation ⟨inj,Finite.surjective_of_injective inj⟩
    exact ⟨τ,degrees,by simpa only [Finset.map_eq_image] using family⟩
  · rename_i no eq
    rcases checked with ⟨same,nodup,enough,valid⟩
    rw [same] at feasible
    exact False.elim (not_feasible (colors r.low) no.listed no.incident no.vertex nodup enough valid feasible)
  · rename_i full eq
    rw [TwentyFiveSparseCompletion.complete r.listed full checked.1] at feasible
    exact False.elim (checked.2 feasible)

end Aris4Math.ThirtyFour.TwentyFiveColoredRows

/-! Some degree-feasible tenth-lock extensions exceed the total edge budget.
These rows use the same exact inventory rejection as the colored catalogue. -/
namespace Aris4Math.ThirtyFour.TwentyFiveConditionalBudgetRows
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveColoredActual
variable {n m : ℕ}
structure Row (n m : ℕ) where
  selected : Finset (Finset (Fin n))
  colored : TwentyFiveColoredRows.Row (n+1) m

def Check (q : ℕ) (target : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (r : Row n m) : Prop :=
  extend big r.selected=r.colored.listed.toFinset ∧
    (∀ i,colors r.colored.low i=standard q i) ∧ TwentyFiveColoredRows.Check q target r.colored

instance (q : ℕ) (target : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (r : Row n m) : Decidable (Check q target big r) := by
  unfold Check
  infer_instance

theorem sound (q : ℕ) (target : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (r : Row n m) (checked : Check q target big r) :
    TwentyFiveUnitConditional.Checks (standard q) target (fun _ => standard q)
      big r.selected r.colored.witness := by
  intro feasible
  obtain ⟨same,degrees,valid⟩ := checked
  have degreeEq : colors r.colored.low=standard q := funext degrees
  rw [same,← degreeEq] at feasible
  obtain ⟨inj,moves,family⟩ := TwentyFiveColoredRows.direct_sound q target r.colored valid feasible
  refine ⟨inj,?_,?_⟩
  · simpa only [degreeEq] using moves
  · simpa only [same] using family

theorem checked_rows (q : ℕ) (target : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (rows : List (Row n m))
    (checked : rows.all (fun r => decide (Check q target big r))=true) :
    List.Forall₂ (TwentyFiveUnitConditional.Checks (standard q) target (fun _ => standard q) big)
      (rows.map Row.selected) (rows.map (fun r => r.colored.witness)) := by
  induction rows with
  | nil => exact .nil
  | cons r rest ih =>
    simp only [List.all_cons,Bool.and_eq_true,decide_eq_true_eq] at checked
    exact .cons (sound q target big r checked.1) (ih checked.2)
end Aris4Math.ThirtyFour.TwentyFiveConditionalBudgetRows
#print axioms Aris4Math.ThirtyFour.TwentyFiveConditionalBudgetRows.sound
