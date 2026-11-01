import Aris4Math.ThirtyFour.TwentyFiveUnitCatalogue
import Aris4Math.ThirtyFour.TwentyFiveUnitCounts

/-! Degree-aware final extensions. An impossible local family is discarded
only using feasibility already proved for the actual H. All retained families
carry explicit bijections and preserve the individual lock degrees. -/
namespace Aris4Math.ThirtyFour.TwentyFiveUnitConditional

open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.K6Classification
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitCounts
open LockExtension (restrict)

variable {n m v : ℕ}

def Checks (degree : Fin (n+1) → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (targetDegree : Fin m → Fin (n+1) → ℕ)
    (big chosen : Finset (Finset (Fin n))) (w : Witness (n+1) m) : Prop :=
  Feasible 34 degree (pairCompletion (extend big chosen)) →
    Function.Injective w.permutation ∧
      (∀ i, targetDegree w.target (w.permutation i)=degree i) ∧
      (extend big chosen).image (fun T => T.image w.permutation)=catalogue w.target

instance (degree : Fin (n+1) → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (targetDegree : Fin m → Fin (n+1) → ℕ)
    (big chosen : Finset (Finset (Fin n))) (w : Witness (n+1) m) :
    Decidable (Checks degree catalogue targetDegree big chosen w) := by
  unfold Checks
  infer_instance

theorem checked_choice (degree : Fin (n+1) → ℕ)
    (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (targetDegree : Fin m → Fin (n+1) → ℕ)
    (big : Finset (Finset (Fin n))) (generated : List (Finset (Finset (Fin n))))
    (witnesses : List (Witness (n+1) m))
    (checked : List.Forall₂ (Checks degree catalogue targetDegree big) generated witnesses)
    (chosen : Finset (Finset (Fin n))) (member : chosen∈generated)
    (feasible : Feasible 34 degree (pairCompletion (extend big chosen))) :
    ∃ d : Fin m, ∃ σ : Equiv.Perm (Fin (n+1)),
      (∀ i, targetDegree d (σ i)=degree i) ∧
      (extend big chosen).image (fun T => T.map σ.toEmbedding)=catalogue d := by
  induction checked with
  | nil => simp at member
  | @cons head w rest ws checked tail ih =>
    rcases List.mem_cons.mp member with rfl | mem
    · obtain ⟨inj, degrees, family⟩ := checked feasible
      let σ := Equiv.ofBijective w.permutation ⟨inj,Finite.surjective_of_injective inj⟩
      exact ⟨w.target,σ,degrees,by simpa only [Finset.map_eq_image] using family⟩
    · exact ih mem

/-- The final local table is applied to the actual chosen promotions and all
recovered multiplicities of the same underlying hypergraph. -/
theorem actual (H : Simple5Hypergraph (Fin v)) (edges : H.edges.card=34)
    (f : Fin (n+1) ↪ Fin v) (unit : Unit H f)
    (degree : Fin (n+1) → ℕ) (degrees : ∀ i,H.degree (f i)=degree i)
    (big : Finset (Finset (Fin n))) (old : large H (restrict f)=big)
    (candidates : List (Finset (Fin n)))
    (complete : ∀ T∈pairCompletion big,T.card≤4→T∈candidates)
    (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (targetDegree : Fin m → Fin (n+1) → ℕ)
    (witnesses : List (Witness (n+1) m))
    (checked : List.Forall₂ (Checks degree catalogue targetDegree big)
      (choices candidates ∅) witnesses) :
    ∃ c : Fin m, ∃ σ : Equiv.Perm (Fin (n+1)), ∀ T,
      count H (σ.toEmbedding.trans f) T=inventory 34 (targetDegree c) (pairCompletion (catalogue c)) T := by
  have member : selected H f∈choices candidates ∅ := by
    apply actual_selected_in_choices H f unit
    rw [old]
    exact complete
  have feasible := (actual_inventory H f unit degree degrees).2
  rw [edges,actual_extend H f unit,old] at feasible
  obtain ⟨c,σ,moves,family⟩ := checked_choice degree catalogue targetDegree big _ witnesses checked
    (selected H f) member feasible
  let g := σ.symm.toEmbedding.trans f
  have gUnit : Unit H g := unit_relabel H f unit σ.symm
  have gDegree (i : Fin (n+1)) : H.degree (g i)=targetDegree c i := by
    change H.degree (f (σ.symm i))=targetDegree c i
    rw [degrees]
    simpa using (moves (σ.symm i)).symm
  have gLarge : large H g=catalogue c := by
    change large H (σ.symm.toEmbedding.trans f)=catalogue c
    rw [large_relabel,actual_extend H f unit,old]
    exact family
  refine ⟨c,σ.symm,?_⟩
  have counts := (actual_inventory H g gUnit (targetDegree c) gDegree).1
  rw [edges,gLarge] at counts
  exact counts

end Aris4Math.ThirtyFour.TwentyFiveUnitConditional

#print axioms Aris4Math.ThirtyFour.TwentyFiveUnitConditional.actual
