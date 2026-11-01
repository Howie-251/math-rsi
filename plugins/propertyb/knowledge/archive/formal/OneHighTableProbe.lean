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
namespace Aris4Math.ThirtyFour.TwentyFiveOneHighTable
open Aris4Math.K6Classification TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredRows
variable {m t : ℕ}

def sources (base : Fin m → Finset (Finset (Fin 9))) :=
  (List.ofFn base).flatMap fun big => List.ofFn fun h : Fin 9 => (big,Finset.univ.erase h)

theorem low_eq (low : Finset (Fin 9)) (card : low.card=8) :
    ∃ h : Fin 9, low=Finset.univ.erase h := by
  have one : lowᶜ.card=1 := by rw [Finset.card_compl,Fintype.card_fin,card]
  obtain ⟨h,same⟩ := Finset.card_eq_one.mp one
  refine ⟨h,?_⟩
  have eq := congrArg (fun s : Finset (Fin 9) => sᶜ) same
  simpa only [compl_compl,Finset.compl_singleton] using eq

theorem table (base : Fin m → Finset (Finset (Fin 9)))
    (target : Fin t → Finset (Finset (Fin 9)))
    (rows : List (Row 9 t)) (complete : rows.map source=sources base)
    (checked : rows.all (fun r => decide (Check 8 target r))=true)
    (c : Fin m) (low : Finset (Fin 9)) (card : low.card=8)
    (feasible : Feasible 34 (colors low) (pairCompletion (base c))) :
    ∃ d : Fin t, ∃ τ : Equiv.Perm (Fin 9),
      (∀ i,standard 8 (τ i)=colors low i) ∧
      (base c).image (fun T => T.map τ.toEmbedding)=target d := by
  obtain ⟨h,rfl⟩ := low_eq low card
  have mem : (base c,Finset.univ.erase h)∈rows.map source := by
    rw [complete]
    exact List.mem_flatMap.mpr ⟨base c,List.mem_ofFn.mpr ⟨c,rfl⟩,
      List.mem_ofFn.mpr ⟨h,rfl⟩⟩
  obtain ⟨r,member,same⟩ := List.mem_map.mp mem
  have bigEq : r.listed.toFinset=base c := congrArg Prod.fst same
  have lowEq : r.low=Finset.univ.erase h := congrArg Prod.snd same
  have valid := of_decide_eq_true (List.all_eq_true.mp checked r member)
  have rf : Feasible 34 (colors r.low) (pairCompletion r.listed.toFinset) := by
    simpa only [bigEq,lowEq] using feasible
  obtain ⟨τ,moves,family⟩ := sound 8 target r valid rf
  refine ⟨r.witness.target,τ,?_,?_⟩
  · simpa only [lowEq] using moves
  · simpa only [bigEq] using family

end Aris4Math.ThirtyFour.TwentyFiveOneHighTable
#print axioms Aris4Math.ThirtyFour.TwentyFiveOneHighTable.table
