import DegreeDiameter.Portfolio.DiagonalFillReallocationDefinitions
namespace DegreeDiameter.Portfolio.DiagonalFillReallocation
open SimpleGraph
variable {V J C : Type*} [Fintype V] [Fintype J] [Fintype C]
variable (U : SimpleGraph V) (H : SimpleGraph (V ⊕ J)) (center : C → V)
variable [DecidableRel U.Adj] [DecidableRel H.Adj]
def oldUNeighborEquiv (v : V) :
    (graph U H center).neighborSet (old (.inl v)) ≃
      H.neighborSet (.inl v) ⊕ {c:C // U.Adj v (center c)} where
  toFun x := match x with
    | ⟨.inl (.inl y),h⟩ => .inl ⟨y,h⟩
    | ⟨.inl (.inr c),h⟩ => .inr ⟨c,h⟩
    | ⟨.inr _,h⟩ => False.elim h
  invFun x := match x with
    | .inl ⟨y,h⟩ => ⟨old y,h⟩
    | .inr ⟨c,h⟩ => ⟨copied c,h⟩
  left_inv := by
    rintro ⟨x,h⟩
    cases x with
    | inl x => cases x <;> rfl
    | inr u => exact False.elim h
  right_inv := by intro x; cases x <;> rfl
def oldFNeighborEquiv (j : J) :
    (graph U H center).neighborSet (old (.inr j)) ≃ H.neighborSet (.inr j) ⊕ Unit where
  toFun x := match x with
    | ⟨.inl (.inl y),h⟩ => .inl ⟨y,h⟩
    | ⟨.inl (.inr _),h⟩ => False.elim h
    | ⟨.inr u,_⟩ => .inr u
  invFun x := match x with
    | .inl ⟨y,h⟩ => ⟨old y,h⟩
    | .inr u => ⟨.inr u,trivial⟩
  left_inv := by
    rintro ⟨x,h⟩
    cases x with
    | inl x => cases x with
      | inl y => rfl
      | inr c => exact False.elim h
    | inr u => rfl
  right_inv := by intro x; cases x <;> rfl
def copyNeighborEquiv (c : C) :
    (graph U H center).neighborSet (copied c) ≃ U.neighborSet (center c) where
  toFun x := match x with
    | ⟨.inl (.inl (.inl v)),h⟩ => ⟨v,h⟩
    | ⟨.inl (.inl (.inr _)),h⟩ => False.elim h
    | ⟨.inl (.inr _),h⟩ => False.elim h
    | ⟨.inr _,h⟩ => False.elim h
  invFun x := ⟨old (.inl x.val),x.property⟩
  left_inv := by
    rintro ⟨x,h⟩
    cases x with
    | inl x => cases x with
      | inl x => cases x with
        | inl v => rfl
        | inr j => exact False.elim h
      | inr d => exact False.elim h
    | inr u => exact False.elim h
  right_inv := by intro x;rfl
def hubNeighborEquiv : (graph U H center).neighborSet hub ≃ J where
  toFun x := match x with
    | ⟨.inl (.inl (.inr j)),_⟩ => j
    | ⟨.inl (.inl (.inl _)),h⟩ => False.elim h
    | ⟨.inl (.inr _),h⟩ => False.elim h
    | ⟨.inr _,h⟩ => False.elim h
  invFun j := ⟨old (.inr j),trivial⟩
  left_inv := by
    rintro ⟨x,h⟩
    cases x with
    | inl x => cases x with
      | inl x => cases x with
        | inl v => exact False.elim h
        | inr j => rfl
      | inr c => exact False.elim h
    | inr u => exact False.elim h
  right_inv := by intro j;rfl

theorem raw_degree_le (compat : ∀ u v,H.Adj (.inl u) (.inl v) ↔ U.Adj u v) (v : V) :
    U.degree v ≤ H.degree (.inl v) := by
  let f : U.neighborSet v → H.neighborSet (.inl v) :=
    fun x => ⟨.inl x.val,(compat _ _).mpr x.property⟩
  have hi : Function.Injective f := by
    intro x y h
    apply Subtype.ext
    exact Sum.inl.inj (congrArg Subtype.val h)
  have hc := Fintype.card_le_of_injective f hi
  simpa only [SimpleGraph.card_neighborSet_eq_degree] using hc
theorem degree_le (delta : Nat)
    (compat : ∀ u v,H.Adj (.inl u) (.inl v) ↔ U.Adj u v)
    (hH : ∀x,H.degree x≤delta)
    (hload : ∀v,FullNeighborhoodClones.load U center v≤1)
    (hJ : Fintype.card J≤delta+1) :
    ∀x,(graph U H center).degree x≤delta+1 := by
  intro x
  cases x with
  | inl x => cases x with
    | inl x => cases x with
      | inl v =>
        rw [←SimpleGraph.card_neighborSet_eq_degree]
        change Fintype.card ((graph U H center).neighborSet (old (.inl v))) ≤ delta+1
        calc
          _ = Fintype.card (H.neighborSet (.inl v) ⊕ {c:C // U.Adj v (center c)}) := Fintype.card_congr (oldUNeighborEquiv U H center v)
          _ = H.degree (.inl v)+FullNeighborhoodClones.load U center v := by
            rw [Fintype.card_sum,SimpleGraph.card_neighborSet_eq_degree];rfl
          _ ≤ delta+1 := Nat.add_le_add (hH (.inl v)) (hload v)
      | inr j =>
        rw [←SimpleGraph.card_neighborSet_eq_degree]
        change Fintype.card ((graph U H center).neighborSet (old (.inr j))) ≤ delta+1
        calc
          _ = Fintype.card (H.neighborSet (.inr j) ⊕ Unit) := Fintype.card_congr (oldFNeighborEquiv U H center j)
          _ = H.degree (.inr j)+1 := by rw [Fintype.card_sum,Fintype.card_unit,SimpleGraph.card_neighborSet_eq_degree]
          _ ≤ delta+1 := Nat.add_le_add_right (hH (.inr j)) 1
    | inr c =>
      rw [←SimpleGraph.card_neighborSet_eq_degree]
      change Fintype.card ((graph U H center).neighborSet (copied c)) ≤ delta+1
      calc
        _ = Fintype.card (U.neighborSet (center c)) := Fintype.card_congr (copyNeighborEquiv U H center c)
        _ = U.degree (center c) := SimpleGraph.card_neighborSet_eq_degree _ _
        _ ≤ delta+1 := (raw_degree_le U H compat (center c)).trans ((hH (.inl (center c))).trans (Nat.le_add_right _ _))
  | inr u =>
    cases u
    rw [←SimpleGraph.card_neighborSet_eq_degree]
    change Fintype.card ((graph U H center).neighborSet hub) ≤ delta+1
    exact (Fintype.card_congr (hubNeighborEquiv U H center)).trans_le hJ
#print axioms degree_le
end DegreeDiameter.Portfolio.DiagonalFillReallocation
