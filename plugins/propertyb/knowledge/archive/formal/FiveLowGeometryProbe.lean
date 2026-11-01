import Aris4Math.ThirtyFour.CachedCoefficients16
import Aris4Math.ThirtyFour.TwentyFiveConditionalRows
import Aris4Math.ThirtyFour.TwentyFiveSparseCompletion
import Aris4Math.ThirtyFour.TwentyFiveInventorySupport
import Aris4Math.ThirtyFour.CachedSparseApplication

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

/-! A fixed certificate selects one valid A/B/C upper bound per position.
Only the selected expression has to be evaluated in each finite strict check. -/
namespace Aris4Math.ThirtyFour.CachedChosenRows
open CachedRows
open scoped BigOperators

def selected (a b c : ℚ) (choice : Fin 3) : ℚ :=
  if choice=0 then a else if choice=1 then b else c

theorem min_le_selected (a b c : ℚ) (choice : Fin 3) :
    min a (min b c) ≤ selected a b c choice := by
  fin_cases choice
  · exact min_le_left _ _
  · exact (min_le_right _ _).trans (min_le_left _ _)
  · exact (min_le_right _ _).trans (min_le_right _ _)

def bound {v : ℕ} (p : Numeric.Profile) (choices : Fin v → Fin 3) : ℚ :=
  ∑ k,selected (cachedA p (k.val+1) true) (cachedA p (k.val+1) false)
    (cachedC p (k.val+1)) (choices k)

theorem strict {v : ℕ} (p : Numeric.Profile) (choices : Fin v → Fin 3)
    (less : bound p choices<1) :
    (∑ k : Fin v,min (cachedA p (k.val+1) true)
      (min (cachedA p (k.val+1) false) (cachedC p (k.val+1))))<1 := by
  apply lt_of_le_of_lt _ less
  exact Finset.sum_le_sum (fun k _ => min_le_selected _ _ _ _)
end Aris4Math.ThirtyFour.CachedChosenRows
namespace Aris4Math.ThirtyFour.FiveLowFamilyPilot
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case2153
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2,3},{0,4},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{4,5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1,2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],7⟩,⟨[11,12,13,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[15,16,17],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2153
namespace Case2153
def locked (k : Fin 25) : Bool := decide (k.val+1 ∈ computed.positions)
def leftSlots (k : Fin 25) : Fin 17 :=
  ⟨Numeric.leftCount computed (k.val+1),by fin_cases k <;> decide +kernel⟩
def rightSlots (k : Fin 25) : Fin 17 :=
  ⟨Numeric.rightCount computed (k.val+1),by fin_cases k <;> decide +kernel⟩
def tableA (k : Fin 25) (last : Bool) (r : Fin 6) : ℚ :=
  CachedCoefficients16.edgeTable
    (CachedCoefficients16.index (locked k) (if last then leftSlots k else rightSlots k)) r
def tableC (k : Fin 25) (r q : Fin 6) : ℚ :=
  CachedCoefficients16.pairTable (CachedCoefficients16.index (locked k) (leftSlots k)) r q

theorem aCoeff_eq (k : Fin 25) (last : Bool) (r : Fin 6) :
    aCoeff computed (k.val+1) last r = tableA k last r := by
  unfold tableA
  rw [← CachedCoefficients16.edgeTable_eq]
  cases last <;> rfl

theorem cCoeff_eq (k : Fin 25) (r q : Fin 6) :
    cCoeff computed (k.val+1) r q = tableC k r q := by
  have geometry : Numeric.rightCount computed (k.val+1) =
      (if locked k then 16 else 15)-(leftSlots k).val := by fin_cases k <;> decide +kernel
  unfold tableC
  rw [← CachedCoefficients16.pairTable_eq]
  unfold cCoeff
  rw [geometry]
  rfl

end Case2153

end Aris4Math.ThirtyFour.FiveLowFamilyPilot
