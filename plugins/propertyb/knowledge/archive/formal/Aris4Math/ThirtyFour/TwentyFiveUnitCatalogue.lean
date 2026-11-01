import Aris4Math.ThirtyFour.TwentyFiveUnitExtension
import Aris4Math.ThirtyFour.LockLiftRelabel
import Mathlib.Data.List.Forall2

/-! The actual-input spine for the 6 → 7 → 8 → 9 unit-lock catalogue.
Finite data certify only the explicitly generated local extensions and their
actual permutations. All arbitrary hypergraph inputs are handled here. -/
namespace Aris4Math.ThirtyFour.TwentyFiveUnitCatalogue

open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.K6Classification
open Aris4Math.ThirtyFour.TwentyFiveUnitExtension
open Aris4Math.ThirtyFour.LockExtension (restrict)

variable {n v m : ℕ}

theorem large_relabel (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (σ : Equiv.Perm (Fin n)) :
    large H (σ.symm.toEmbedding.trans f) =
      (large H f).image (fun T => T.map σ.toEmbedding) := by
  ext T
  constructor
  · intro ht
    refine Finset.mem_image.mpr ⟨T.map σ.symm.toEmbedding, ?_, ?_⟩
    · obtain ⟨card, pos⟩ := (mem_large H _ T).mp ht
      apply (mem_large H f _).mpr
      rw [LockRelabel.count_comp_perm] at pos
      exact ⟨by simpa using card, pos⟩
    · ext i
      simp
  · intro ht
    obtain ⟨U, hU, rfl⟩ := Finset.mem_image.mp ht
    obtain ⟨card, pos⟩ := (mem_large H f U).mp hU
    apply (mem_large H _ _).mpr
    rw [LockRelabel.count_comp_perm]
    have same : (U.map σ.toEmbedding).map σ.symm.toEmbedding=U := by
      ext i
      simp
    simpa only [same, Finset.card_map] using And.intro card pos

def Covers (catalogue : Fin m → Finset (Finset (Fin n))) : Prop :=
  ∀ {v}, ∀ H : Simple5Hypergraph (Fin v), ∀ f : Fin n ↪ Fin v, Unit H f →
    ∃ c : Fin m, ∃ σ : Equiv.Perm (Fin n), large H (σ.toEmbedding.trans f)=catalogue c

theorem six_covers : Covers representative := by
  intro v H f unit
  obtain ⟨c, _, σ, same⟩ := classify_six (by simp : Fintype.card (Fin 6)=6)
    (blocks H f) (fun T hT => blocks_size H f hT) (blocks_linear H f unit)
  refine ⟨c, σ.symm, ?_⟩
  rw [large_relabel]
  exact same

theorem unit_relabel (H : Simple5Hypergraph (Fin v)) (f : Fin n ↪ Fin v)
    (unit : Unit H f) (σ : Equiv.Perm (Fin n)) : Unit H (σ.toEmbedding.trans f) := by
  intro i j ne
  exact unit (σ i) (σ j) (σ.injective.ne ne)

/-- A checked local extension table lifts complete coverage by one lock.
The same actual new vertex is kept while old labels are normalized. -/
theorem covers_succ {a b : ℕ}
    (old : Fin a → Finset (Finset (Fin n)))
    (new : Fin b → Finset (Finset (Fin (n+1))))
    (candidates : Fin a → List (Finset (Fin n)))
    (old_covers : Covers old)
    (complete : ∀ c T, T ∈ pairCompletion (old c) → T.card ≤ 4 → T ∈ candidates c)
    (checked : ∀ c chosen, chosen ∈ choices (candidates c) ∅ →
      ∃ d : Fin b, ∃ σ : Equiv.Perm (Fin (n+1)),
        (extend (old c) chosen).image (fun T => T.map σ.toEmbedding)=new d) :
    Covers new := by
  intro v H f unit
  obtain ⟨c, σ, old_eq⟩ := old_covers H (restrict f) (unit_restrict H f unit)
  let τ := LockLiftRelabel.lift σ
  let g := τ.toEmbedding.trans f
  have gUnit : Unit H g := unit_relabel H f unit τ
  have gOld : large H (restrict g)=old c := by
    rw [show restrict g=σ.toEmbedding.trans (restrict f) from
      LockLiftRelabel.restrict_lift_trans σ f]
    exact old_eq
  have member : selected H g ∈ choices (candidates c) ∅ := by
    apply actual_selected_in_choices H g gUnit
    rw [gOld]
    exact complete c
  obtain ⟨d, ρ, same⟩ := checked c (selected H g) member
  refine ⟨d, ρ.symm.trans τ, ?_⟩
  change large H (ρ.symm.toEmbedding.trans g)=new d
  rw [large_relabel, actual_extend H g gUnit, gOld]
  exact same

/-- Finite permutation witness. Its injectivity is checked, not assumed. -/
structure Witness (n m : ℕ) where
  target : Fin m
  permutation : Fin n → Fin n

def Checks (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n)))
    (chosen : Finset (Finset (Fin n))) (w : Witness (n+1) m) : Prop :=
  Function.Injective w.permutation ∧
    (extend big chosen).image (fun T => T.image w.permutation)=catalogue w.target

instance (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (big chosen : Finset (Finset (Fin n))) (w : Witness (n+1) m) :
    Decidable (Checks catalogue big chosen w) := by unfold Checks; infer_instance

theorem checked_choice (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (generated : List (Finset (Finset (Fin n))))
    (witnesses : List (Witness (n+1) m))
    (checked : List.Forall₂ (Checks catalogue big) generated witnesses)
    (chosen : Finset (Finset (Fin n))) (member : chosen ∈ generated) :
    ∃ d : Fin m, ∃ σ : Equiv.Perm (Fin (n+1)),
      (extend big chosen).image (fun T => T.map σ.toEmbedding)=catalogue d := by
  induction checked with
  | nil => simp at member
  | @cons head w rest ws checked tail ih =>
    rcases List.mem_cons.mp member with rfl | mem
    · let σ := Equiv.ofBijective w.permutation
        ⟨checked.1, Finite.surjective_of_injective checked.1⟩
      refine ⟨w.target, σ, ?_⟩
      simpa only [Finset.map_eq_image] using checked.2
    · exact ih mem

end Aris4Math.ThirtyFour.TwentyFiveUnitCatalogue

#print axioms Aris4Math.ThirtyFour.TwentyFiveUnitCatalogue.six_covers
#print axioms Aris4Math.ThirtyFour.TwentyFiveUnitCatalogue.covers_succ
