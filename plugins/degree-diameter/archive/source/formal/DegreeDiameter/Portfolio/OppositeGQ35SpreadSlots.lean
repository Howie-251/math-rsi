import DegreeDiameter.Portfolio.OppositeGQ35SpreadGeneric
import Mathlib.Logic.Equiv.Fin.Basic
namespace DegreeDiameter.Portfolio.OppositeGQSpread
open SimpleGraph
variable {P L V J : Type*} {a b : Nat}
variable (e : V ≃ P × L) (Inc : P → L → Prop) (spread : J → L)
variable (owner : P → J) (points : L → Fin a → P) (lines : P → Fin b → L)

/-- An old self slot is used for the unique spread vertex. Other slots give the
raw opposite-incidence neighbor. This function need only cover all neighbors. -/
def slot [DecidableEq V] (u : V ⊕ J) (ij : Fin a × Fin b) : V ⊕ J :=
  match u with
  | .inl v =>
    let q := points (e v).2 ij.1
    let m := lines (e v).1 ij.2
    let w := e.symm (q,m)
    if w = v then .inr (owner (e v).1) else .inl w
  | .inr j =>
    let p := points (spread j) ij.1
    .inl (e.symm (p,lines p ij.2))

theorem slot_covers [DecidableEq V]
    (hpoints : ∀ p l, Inc p l → ∃ i, points l i = p)
    (hlines : ∀ p l, Inc p l → ∃ i, lines p i = l)
    (howner : ∀ p j, Inc p (spread j) → j = owner p) :
    ∀ u v, (graph e Inc spread).Adj u v →
      ∃ ij, slot e spread owner points lines u ij = v := by
  have parts (v : V) : e.symm ((e v).1,(e v).2) = v := e.symm_apply_apply v
  intro u v h
  cases u with
  | inl u =>
    cases v with
    | inl v =>
      obtain ⟨i,hi⟩ := hpoints (e v).1 (e u).2 h.2.2
      obtain ⟨j,hj⟩ := hlines (e u).1 (e v).2 h.2.1
      refine ⟨(i,j),?_⟩
      simp only [slot,hi,hj,parts]
      rw [if_neg (Ne.symm h.1)]
    | inr j =>
      obtain ⟨i,hi⟩ := hpoints (e u).1 (e u).2 h.1
      obtain ⟨k,hk⟩ := hlines (e u).1 (e u).2 h.1
      refine ⟨(i,k),?_⟩
      simp only [slot,hi,hk,parts,ite_true]
      rw [howner (e u).1 j h.2]
  | inr j =>
    cases v with
    | inl v =>
      obtain ⟨i,hi⟩ := hpoints (e v).1 (spread j) h.2
      obtain ⟨k,hk⟩ := hlines (e v).1 (e v).2 h.1
      exact ⟨(i,k),by simp only [slot,hi,hk,parts]⟩
    | inr k => exact False.elim h

/-- Neighbor coverage by a finite domain gives a degree bound without proving
an exact degree formula or enumerating pairs of graph vertices. -/
theorem degree_le_of_cover {W A : Type*} [Fintype W] [Fintype A]
    (G : SimpleGraph W) [DecidableRel G.Adj] (f : W → A → W)
    (cover : ∀ u v, G.Adj u v → ∃ i, f u i = v) :
    ∀ u, G.degree u ≤ Fintype.card A := by
  classical
  intro u
  let index (v : G.neighborSet u) : A := Classical.choose (cover u v.val v.property)
  have hi (v : G.neighborSet u) : f u (index v) = v.val := Classical.choose_spec (cover u v.val v.property)
  have inj : Function.Injective index := by
    intro v w h
    apply Subtype.ext
    rw [← hi v,← hi w,h]
  rw [← SimpleGraph.card_neighborSet_eq_degree]
  exact Fintype.card_le_of_injective index inj
#print axioms slot_covers
#print axioms degree_le_of_cover
end DegreeDiameter.Portfolio.OppositeGQSpread
