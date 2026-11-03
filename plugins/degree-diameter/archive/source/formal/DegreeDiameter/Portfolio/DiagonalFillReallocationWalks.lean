import DegreeDiameter.Portfolio.DiagonalFillReallocationDefinitions
namespace DegreeDiameter.Portfolio.DiagonalFillReallocation
open SimpleGraph
variable {V J C P L : Type*}

def emptyHom (e : V ≃ P × L) (Inc : P → L → Prop) :
    OppositeGQSpread.graph e Inc (Empty.elim : Empty → L) →g rawGraph e Inc where
  toFun := Sum.elim id Empty.elim
  map_rel' := by
    intro x y h
    cases x with
    | inl x => cases y with
      | inl y => exact h
      | inr y => cases y
    | inr x => cases x
theorem raw_diameter_three (e : V ≃ P × L) (Inc : P → L → Prop)
    (project : ∀ p l,∃q m,Inc q l ∧ Inc p m ∧ Inc q m) :
    DiameterAtMost (rawGraph e Inc) 3 := by
  have h := OppositeGQSpread.diameter_three e Inc (Empty.elim : Empty → L)
    project (by intro j; cases j)
  intro u v
  obtain ⟨p,hp⟩ := h (.inl u) (.inl v)
  exact ⟨p.map (emptyHom e Inc),by simpa using hp⟩

theorem diameter_three (U : SimpleGraph V) (H : SimpleGraph (V ⊕ J)) (center : C → V)
    (compat : ∀ u v,H.Adj (.inl u) (.inl v) ↔ U.Adj u v)
    (hH : DiameterAtMost H 3) (hU : DiameterAtMost U 3)
    (hne : ∀ v,∃w,U.Adj v w)
    (fillroute : ∀ j c,∃v,∃p:H.Walk (.inr j) (.inl v),p.length≤2 ∧ U.Adj v (center c))
    (flagroute : ∀ v,∃j w,H.Adj (.inr j) (.inl w) ∧ U.Adj w v) :
    DiameterAtMost (graph U H center) 3 := by
  have hK := FullNeighborhoodClones.diameterAtMost U center 3 (by decide) hU hne
  have rawpair (x y : V ⊕ C) :
      ∃p:(graph U H center).Walk ((rawCloneHom U H center compat) x)
        ((rawCloneHom U H center compat) y),p.length≤3 := by
    obtain ⟨p,hp⟩ := hK x y
    exact ⟨p.map (rawCloneHom U H center compat),by simpa using hp⟩
  have fillcopy (j : J) (c : C) :
      ∃p:(graph U H center).Walk (old (.inr j)) (copied c),p.length≤3 := by
    obtain ⟨v,p,hp,hv⟩ := fillroute j c
    refine ⟨(p.map (oldHom U H center)).append
      (Walk.cons (show (graph U H center).Adj (old (.inl v)) (copied c) from hv) Walk.nil),?_⟩
    simp only [Walk.length_append,Walk.length_map,Walk.length_cons,Walk.length_nil]
    omega
  have pair (x y : (V ⊕ J) ⊕ C) :
      ∃p:(graph U H center).Walk (.inl x) (.inl y),p.length≤3 := by
    cases x with
    | inl x => cases y with
      | inl y =>
        obtain ⟨p,hp⟩ := hH x y
        exact ⟨p.map (oldHom U H center),by simpa using hp⟩
      | inr c => cases x with
        | inl v => exact rawpair (.inl v) (.inr c)
        | inr j => exact fillcopy j c
    | inr c => cases y with
      | inl y => cases y with
        | inl v => exact rawpair (.inr c) (.inl v)
        | inr j =>
          obtain ⟨p,hp⟩ := fillcopy j c
          exact ⟨p.reverse,by simpa using hp⟩
      | inr d => exact rawpair (.inr c) (.inr d)
  have huball (x : Vertex V J C) :
      ∃p:(graph U H center).Walk hub x,p.length≤3 := by
    cases x with
    | inl x => cases x with
      | inl x => cases x with
        | inl v =>
          obtain ⟨j,w,hj,hw⟩ := flagroute v
          refine ⟨Walk.cons (show (graph U H center).Adj hub (old (.inr j)) from trivial)
            (Walk.cons (show (graph U H center).Adj (old (.inr j)) (old (.inl w)) from hj)
            (Walk.cons (show (graph U H center).Adj (old (.inl w)) (old (.inl v)) from (compat _ _).mpr hw) Walk.nil)),?_⟩
          simp
        | inr j =>
          exact ⟨Walk.cons (show (graph U H center).Adj hub (old (.inr j)) from trivial) Walk.nil,by simp⟩
      | inr c =>
        obtain ⟨j,w,hj,hw⟩ := flagroute (center c)
        refine ⟨Walk.cons (show (graph U H center).Adj hub (old (.inr j)) from trivial)
          (Walk.cons (show (graph U H center).Adj (old (.inr j)) (old (.inl w)) from hj)
          (Walk.cons (show (graph U H center).Adj (old (.inl w)) (copied c) from hw) Walk.nil)),?_⟩
        simp
    | inr u => cases u; exact ⟨Walk.nil,by simp⟩
  intro x y
  cases x with
  | inl x => cases y with
    | inl y => exact pair x y
    | inr u => cases u; obtain ⟨p,hp⟩ := huball (.inl x); exact ⟨p.reverse,by simpa using hp⟩
  | inr u => cases u; exact huball y
#print axioms raw_diameter_three
#print axioms diameter_three
end DegreeDiameter.Portfolio.DiagonalFillReallocation
