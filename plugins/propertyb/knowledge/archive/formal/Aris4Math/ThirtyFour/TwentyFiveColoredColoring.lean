import Aris4Math.ThirtyFour.TwentyFiveLowColorPruning
import Aris4Math.ThirtyFour.TwentyFiveInventorySupport

/-! Direct actual coloring from explicit classified rows. Numeric witnesses are
proved once per target family, then named proofs are reused. No finite-table
lookup is performed inside a row's arithmetic check. -/
namespace Aris4Math.ThirtyFour.TwentyFiveColoredColoring
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitCounts
open TwentyFiveColoredActual
variable {n v : ℕ}

def Safe (degree : Fin n → ℕ) (big : Finset (Finset (Fin n))) : Prop :=
  ∀ (H : Simple5Hypergraph (Fin 25)),H.edges.card=34 →
    ∀ f : Fin n↪Fin 25,Unit H f →
      (∀ i,H.degree (f i)=degree i) → large H f=big → PropertyB H

theorem of_counts (degree : Fin n → ℕ) (big : Finset (Finset (Fin n)))
    (μ : Finset (Fin n) → ℕ)
    (recovered : ∀ T,inventory 34 degree (pairCompletion big) T=μ T)
    (colorable : ∀ (H : Simple5Hypergraph (Fin 25)) (f : Fin n↪Fin 25),
      (∀ T,count H f T=μ T) → PropertyB H) : Safe degree big := by
  intro H edges f unit degrees large_eq
  apply colorable H f
  have actual := (actual_inventory H f unit degree degrees).1
  rw [edges,large_eq] at actual
  intro T
  exact (actual T).trans (recovered T)

structure Row (n : ℕ) where
  target : Finset (Finset (Fin n))
  data : TwentyFiveColoredRows.Row n 1

def source (r : Row n) := TwentyFiveColoredRows.source r.data

def Check (q : ℕ) (r : Row n) : Prop :=
  TwentyFiveColoredRows.Check q (fun _ => r.target) r.data
instance (q : ℕ) (r : Row n) : Decidable (Check q r) := by unfold Check; infer_instance

theorem row_safe (q : ℕ) (r : Row n) (checked : Check q r)
    (target_safe : Safe (standard q) r.target) : Safe (colors r.data.low) r.data.listed.toFinset := by
  intro H edges f unit degrees large_eq
  have feasible := (actual_inventory H f unit (colors r.data.low) degrees).2
  rw [edges,large_eq] at feasible
  obtain ⟨τ,moves,family⟩ := TwentyFiveColoredRows.sound q (fun _ => r.target) r.data checked feasible
  let g := τ.symm.toEmbedding.trans f
  apply target_safe H edges g (unit_relabel H f unit τ.symm)
  · intro i
    change H.degree (f (τ.symm i))=standard q i
    rw [degrees]
    simpa using (moves (τ.symm i)).symm
  · rw [show g=τ.symm.toEmbedding.trans f from rfl,large_relabel,large_eq]
    exact family

theorem from_rows (q : ℕ) (big : Finset (Finset (Fin n)))
    (lows : List (Finset (Fin n))) (rows : List (Row n))
    (complete : rows.map source=lows.map (fun low => (big,low)))
    (checked : rows.all (fun r => decide (Check q r))=true)
    (safe : ∀ r∈rows,Safe (standard q) r.target)
    (low : Finset (Fin n)) (mem : low∈lows) : Safe (colors low) big := by
  have member : (big,low)∈rows.map source := by
    rw [complete]
    exact List.mem_map.mpr ⟨low,mem,rfl⟩
  obtain ⟨r,inRows,same⟩ := List.mem_map.mp member
  have largeEq : r.data.listed.toFinset=big := congrArg Prod.fst same
  have lowEq : r.data.low=low := congrArg Prod.snd same
  have valid := of_decide_eq_true (List.all_eq_true.mp checked r inRows)
  simpa only [largeEq,lowEq] using row_safe q r valid (safe r inRows)

theorem pruned_table {m : ℕ} (base : Fin m → Finset (Finset (Fin n)))
    (families : List (TwentyFiveLowColorPruning.Family n))
    (covers : families.map (fun r => r.listed.toFinset)=List.ofFn base)
    (q : ℕ) (checked : families.all (fun r => decide (TwentyFiveLowColorPruning.Check q r))=true)
    (safe : ∀ r∈families,∀ low∈r.lows,Safe (colors low) r.listed.toFinset)
    (c : Fin m) (low : Finset (Fin n)) (card : low.card=q)
    (feasible : Feasible 34 (colors low) (pairCompletion (base c))) :
    Safe (colors low) (base c) := by
  obtain ⟨r,member,same,lowMember⟩ := TwentyFiveLowColorPruning.complete base
    families covers q checked c low card feasible
  simpa only [same] using safe r member low lowMember

/-- The actual theorem only needs a complete uncolored catalogue and each
feasible degree-colored input's coloring theorem. -/
theorem actual {m : ℕ} (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (f : Fin n↪Fin 25) (unit : Unit H f) (q : ℕ)
    (degrees : ∀ i,H.degree (f i)=standard q i)
    (size : (Finset.univ.filter fun i : Fin n => i.val<q).card=q)
    (base : Fin m → Finset (Finset (Fin n))) (covers : Covers base)
    (table : ∀ c (low : Finset (Fin n)),low.card=q →
      Feasible 34 (colors low) (pairCompletion (base c)) → Safe (colors low) (base c)) :
    PropertyB H := by
  obtain ⟨c,σ,family⟩ := covers H f unit
  let g := σ.toEmbedding.trans f
  have gu := unit_relabel H f unit σ
  have gd (i : Fin n) : H.degree (g i)=colors (lowSet q σ) i := by
    change H.degree (f (σ i))=colors (lowSet q σ) i
    rw [degrees]
    simp only [standard,colors,mem_lowSet]
  have feasible := (actual_inventory H g gu (colors (lowSet q σ)) gd).2
  rw [edges,show large H g=base c from family] at feasible
  exact table c (lowSet q σ) (lowSet_card q σ size) feasible H edges g gu gd family

end Aris4Math.ThirtyFour.TwentyFiveColoredColoring
