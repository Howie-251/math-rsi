import Aris4Math.ThirtyFour.TwentyFiveUnitConditional
import Aris4Math.ThirtyFour.TwentyFiveSelection


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
namespace EightLowFrameProbe
open Aris4Math Aris4Math.ThirtyFour Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveColoredActual
open LockExtension (restrict)
def base : Fin 2 → Fin 840 := ![0,10]
theorem residue_group (c : Fin 840) (residue : c=0 ∨ c=10) :
    ∃ g : Fin 2,base g=c := by
  rcases residue with rfl | rfl
  · exact ⟨0,rfl⟩
  · exact ⟨1,rfl⟩

theorem close (bigCatalogue : Fin 840 → Finset (Finset (Fin 9)))
    (μ : Fin 840 → Finset (Fin 9) → ℕ)
    (classified : ∀ H : Simple5Hypergraph (Fin 25),H.edges.card=34 →
      ∀ f : Fin 9↪Fin 25,Unit H f → (∀ i,H.degree (f i)=standard 8 i) →
      ∃ c : Fin 840,∃ σ : Equiv.Perm (Fin 9),
        large H (σ.toEmbedding.trans f)=bigCatalogue c ∧
        (∀ i,H.degree ((σ.toEmbedding.trans f) i)=standard 8 i) ∧
        (∀ T,count H (σ.toEmbedding.trans f) T=μ c T))
    (strict : ∀ H : Simple5Hypergraph (Fin 25),∀ f : Fin 9↪Fin 25,
      ∀ c : Fin 840,(∀ T,count H f T=μ c T) → c=0∨c=10∨PropertyB H)
    (tenth : ∀ H : Simple5Hypergraph (Fin 25),H.edges.card=34 →
      ∀ f : Fin 10↪Fin 25,Unit H f → ∀ g : Fin 2,
      (∀ i,H.degree (f i)=standard 8 i) →
      large H (restrict f)=bigCatalogue (base g) → PropertyB H)
    (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (selection : TwentyFiveSelection.MixedLocks H 8 2) : PropertyB H := by
  by_contra notB
  obtain ⟨f,degrees,unit⟩ := selection
  have firstUnit : Unit H (restrict f) := unit_restrict H f unit
  have firstDegree (i : Fin 9) : H.degree ((restrict f) i)=standard 8 i :=
    degrees i.castSucc
  obtain ⟨c,σ,big,newFirstDegree,counts⟩ := classified H edges (restrict f)
    firstUnit firstDegree
  have split := strict H
    (σ.toEmbedding.trans (restrict f)) c counts
  have residue : c=0 ∨ c=10 := by
    rcases split with h | h | done
    · exact Or.inl h
    · exact Or.inr h
    · exact (notB done).elim
  obtain ⟨g,baseEq⟩ := residue_group c residue
  let τ := LockLiftRelabel.lift σ
  let new := τ.toEmbedding.trans f
  have newUnit : Unit H new := unit_relabel H f unit τ
  have newOld : large H (restrict new)=bigCatalogue (base g) := by
    rw [show restrict new=σ.toEmbedding.trans (restrict f) from
      LockLiftRelabel.restrict_lift_trans σ f]
    simpa only [baseEq] using big
  have newDegrees (i : Fin 10) : H.degree (new i)=standard 8 i := by
    refine Fin.lastCases ?_ (fun j => ?_) i
    · change H.degree (f (LockLiftRelabel.lift σ (Fin.last 9)))=standard 8 (Fin.last 9)
      rw [LockLiftRelabel.lift_last]
      exact degrees (Fin.last 9)
    · change H.degree (f (LockLiftRelabel.lift σ j.castSucc))=standard 8 j.castSucc
      rw [LockLiftRelabel.lift_castSucc]
      exact newFirstDegree j
  exact notB (tenth H edges new newUnit g newDegrees newOld)

#print axioms close
end EightLowFrameProbe
