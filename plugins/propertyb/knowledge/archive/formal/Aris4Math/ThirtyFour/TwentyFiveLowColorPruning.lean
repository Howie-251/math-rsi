import Aris4Math.ThirtyFour.TwentyFiveColoredRows

/-! Completeness of degree-based pruning before colored classification.
A family with eight blocks through one lock is impossible for every coloring.
Otherwise every six-degree lock lies in the exact eligible set. -/
namespace Aris4Math.ThirtyFour.TwentyFiveLowColorPruning
open Aris4Math.K6Classification TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveDegreeObstruction TwentyFiveConditionalRows TwentyFiveColoredRows
variable {n : ℕ}

structure Family (n : ℕ) where
  listed : List (Finset (Fin n))
  full : List (Finset (Fin n))
  eligible : Finset (Fin n)
  lows : List (Finset (Fin n))
  rejection : Option (Rejection n)

def Check (q : ℕ) (r : Family n) : Prop :=
  match r.rejection with
  | some no => r.listed.toFinset=no.listed.toFinset ∧ no.incident.Nodup ∧
      7<no.incident.length ∧
      no.incident.all (fun T => decide (no.vertex∈T) && blockCheck no.listed T)=true
  | none => TwentyFiveSparseCompletion.Check r.listed r.full=true ∧
      r.eligible=Finset.univ.filter (fun i => (r.full.toFinset.filter fun T => i∈T).card≤6) ∧
      r.lows.toFinset=r.eligible.powersetCard q

instance (q : ℕ) (r : Family n) : Decidable (Check q r) := by
  unfold Check
  split <;> infer_instance

theorem low_mem (q : ℕ) (r : Family n) (checked : Check q r)
    (low : Finset (Fin n)) (card : low.card=q)
    (feasible : Feasible 34 (colors low) (pairCompletion r.listed.toFinset)) :
    low∈r.lows := by
  unfold Check at checked
  split at checked
  · rename_i no eq
    rcases checked with ⟨same,nodup,enough,valid⟩
    rw [same] at feasible
    have degree : colors low no.vertex≤7 := by unfold colors; split <;> omega
    exact False.elim (not_feasible (colors low) no.listed no.incident no.vertex
      nodup (lt_of_le_of_lt degree enough) valid feasible)
  · rcases checked with ⟨complete,eligible,lows⟩
    rw [TwentyFiveSparseCompletion.complete r.listed r.full complete] at feasible
    apply List.mem_toFinset.mp
    rw [lows]
    apply Finset.mem_powersetCard.mpr
    refine ⟨?_,card⟩
    intro i member
    rw [eligible]
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_univ _,?_⟩
    have bound := feasible.1 i
    simpa only [colors,if_pos member] using bound

/-- Every feasible coloring of any original family occurs in the pruned list.
Both equalities are exact sets/lists, not one-way validity checks. -/
theorem complete {m : ℕ} (base : Fin m → Finset (Finset (Fin n)))
    (families : List (Family n))
    (covers : families.map (fun r => r.listed.toFinset)=List.ofFn base)
    (q : ℕ) (checked : families.all (fun r => decide (Check q r))=true)
    (c : Fin m) (low : Finset (Fin n)) (card : low.card=q)
    (feasible : Feasible 34 (colors low) (pairCompletion (base c))) :
    ∃ r∈families,r.listed.toFinset=base c ∧ low∈r.lows := by
  have member : base c∈families.map (fun r => r.listed.toFinset) := by
    rw [covers]
    exact List.mem_ofFn.mpr ⟨c,rfl⟩
  obtain ⟨r,mem,same⟩ := List.mem_map.mp member
  refine ⟨r,mem,same,?_⟩
  apply low_mem q r (of_decide_eq_true (List.all_eq_true.mp checked r mem)) low card
  simpa only [same] using feasible

end Aris4Math.ThirtyFour.TwentyFiveLowColorPruning
