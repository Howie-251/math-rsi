import DegreeDiameter.Portfolio.DiagonalFillReallocationDefinitions
namespace DegreeDiameter.Portfolio.DiagonalFillReallocation
open SimpleGraph
variable {V J C : Type*}
theorem hub_neighbor (U : SimpleGraph V) (H : SimpleGraph (V ⊕ J)) (center : C → V)
    (x : Vertex V J C) (h : (graph U H center).Adj hub x) : ∃j,x=old (.inr j) := by
  cases x with
  | inl x => cases x with
    | inl x => cases x with
      | inl v => exact False.elim h
      | inr j => exact ⟨j,rfl⟩
    | inr c => exact False.elim h
  | inr u => exact False.elim h
theorem not_diameterAtMost_two (U : SimpleGraph V) (H : SimpleGraph (V ⊕ J))
    (center : C → V) (c : C) : ¬DiameterAtMost (graph U H center) 2 := by
  intro hD
  obtain ⟨p,hp⟩ := hD hub (copied c)
  have hn : (hub : Vertex V J C) ≠ copied c := by intro h; cases h
  obtain ⟨w,hw,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne hn p
  obtain ⟨j,rfl⟩ := hub_neighbor U H center w hw
  have ht : tail.length≤1 := by
    rw [heq] at hp
    simp only [Walk.length_cons] at hp
    omega
  have hn2 : (old (.inr j) : Vertex V J C) ≠ copied c := by intro h;cases h
  have hz : tail.length≠0 := by intro h;exact hn2 (Walk.eq_of_length_eq_zero h)
  have h1 : tail.length=1 := by omega
  have ha := Walk.adj_of_length_eq_one h1
  exact ha
#print axioms not_diameterAtMost_two
end DegreeDiameter.Portfolio.DiagonalFillReallocation
