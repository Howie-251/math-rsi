import DegreeDiameter.Portfolio.FullNeighborhoodClones
import DegreeDiameter.Portfolio.OppositeGQ35SpreadWalks
import DegreeDiameter.Portfolio.OppositeGQ35SpreadLowerGeneric
namespace DegreeDiameter.Portfolio.DiagonalFillReallocation
open SimpleGraph
variable {V J C : Type*}
abbrev Vertex (V J C : Type*) := ((V ⊕ J) ⊕ C) ⊕ Unit
def old (x : V ⊕ J) : Vertex V J C := .inl (.inl x)
def copied (c : C) : Vertex V J C := .inl (.inr c)
def hub : Vertex V J C := .inr ()
def graph (U : SimpleGraph V) (H : SimpleGraph (V ⊕ J)) (center : C → V) :
    SimpleGraph (Vertex V J C) where
  Adj
    | .inl x,.inl y => match x,y with
      | .inl x,.inl y => H.Adj x y
      | .inl x,.inr c => match x with
        | .inl v => U.Adj v (center c)
        | .inr _ => False
      | .inr c,.inl y => match y with
        | .inl v => U.Adj (center c) v
        | .inr _ => False
      | .inr _,.inr _ => False
    | .inl x,.inr _ => match x with
      | .inl x => match x with
        | .inl _ => False
        | .inr _ => True
      | .inr _ => False
    | .inr _,.inl y => match y with
      | .inl y => match y with
        | .inl _ => False
        | .inr _ => True
      | .inr _ => False
    | .inr _,.inr _ => False
  symm := by
    intro x y h
    cases x with
    | inl x => cases x with
      | inl x => cases x with
        | inl x => cases y with
          | inl y => cases y with
            | inl y => exact H.symm h
            | inr c => exact U.symm h
          | inr y => exact h
        | inr j => cases y with
          | inl y => cases y with
            | inl y => exact H.symm h
            | inr c => exact h
          | inr y => trivial
      | inr c => cases y with
        | inl y => cases y with
          | inl y => cases y with
            | inl v => exact U.symm h
            | inr j => exact h
          | inr d => exact h
        | inr y => exact h
    | inr x => cases y with
      | inl y => cases y with
        | inl y => cases y with
          | inl v => exact h
          | inr j => trivial
        | inr c => exact h
      | inr y => exact h
  loopless := by
    intro x h
    cases x with
    | inl x => cases x with
      | inl x => exact H.loopless x h
      | inr c => exact h
    | inr u => exact h
instance (U : SimpleGraph V) (H : SimpleGraph (V ⊕ J)) (center : C → V)
    [DecidableRel U.Adj] [DecidableRel H.Adj] : DecidableRel (graph U H center).Adj := by
  intro x y
  cases x with
  | inl x => cases x with
    | inl x => cases x with
      | inl v => cases y with
        | inl y => cases y with
          | inl y => exact inferInstanceAs (Decidable (H.Adj (.inl v) y))
          | inr c => exact inferInstanceAs (Decidable (U.Adj v (center c)))
        | inr u => exact isFalse id
      | inr j => cases y with
        | inl y => cases y with
          | inl y => exact inferInstanceAs (Decidable (H.Adj (.inr j) y))
          | inr c => exact isFalse id
        | inr u => exact isTrue trivial
    | inr c => cases y with
      | inl y => cases y with
        | inl y => cases y with
          | inl v => exact inferInstanceAs (Decidable (U.Adj (center c) v))
          | inr j => exact isFalse id
        | inr d => exact isFalse id
      | inr u => exact isFalse id
  | inr u => cases y with
    | inl y => cases y with
      | inl y => cases y with
        | inl v => exact isFalse id
        | inr j => exact isTrue trivial
      | inr c => exact isFalse id
    | inr u => exact isFalse id

def rawGraph {P L : Type*} (e : V ≃ P × L) (Inc : P → L → Prop) : SimpleGraph V where
  Adj u v := u ≠ v ∧ Inc (e u).1 (e v).2 ∧ Inc (e v).1 (e u).2
  symm := by intro u v h; exact ⟨Ne.symm h.1,h.2.2,h.2.1⟩
  loopless := by intro v h; exact h.1 rfl
instance {P L : Type*} (e : V ≃ P × L) (Inc : P → L → Prop)
    [DecidableEq V] [DecidableRel Inc] : DecidableRel (rawGraph e Inc).Adj := by
  intro u v
  exact inferInstanceAs (Decidable (u ≠ v ∧ Inc (e u).1 (e v).2 ∧ Inc (e v).1 (e u).2))

def oldHom (U : SimpleGraph V) (H : SimpleGraph (V ⊕ J)) (center : C → V) :
    H →g graph U H center where
  toFun := old
  map_rel' := by intro x y h; exact h
def rawCloneHom (U : SimpleGraph V) (H : SimpleGraph (V ⊕ J)) (center : C → V)
    (compat : ∀ u v,H.Adj (.inl u) (.inl v) ↔ U.Adj u v) :
    FullNeighborhoodClones.graph U center →g graph U H center where
  toFun
    | .inl v => old (.inl v)
    | .inr c => copied c
  map_rel' := by
    intro x y h
    cases x <;> cases y
    · exact (compat _ _).mpr h
    · exact h
    · exact h
    · exact h
end DegreeDiameter.Portfolio.DiagonalFillReallocation
