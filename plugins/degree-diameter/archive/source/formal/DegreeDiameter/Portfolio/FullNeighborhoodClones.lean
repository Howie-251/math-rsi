import DegreeDiameter.Portfolio.SingleExtension
import Mathlib.Data.Fintype.Sum

namespace DegreeDiameter.Portfolio.FullNeighborhoodClones
open SimpleGraph
variable {V J : Type*}

def graph (G : SimpleGraph V) (center : J → V) : SimpleGraph (V ⊕ J) where
  Adj
    | Sum.inl v, Sum.inl w => G.Adj v w
    | Sum.inl v, Sum.inr j => G.Adj v (center j)
    | Sum.inr j, Sum.inl v => G.Adj (center j) v
    | Sum.inr _, Sum.inr _ => False
  symm := by
    intro u v h
    cases u <;> cases v
    · exact G.symm h
    · exact G.symm h
    · exact G.symm h
    · exact h
  loopless := by
    intro u h
    cases u
    · exact G.loopless _ h
    · exact h

def collapse (center : J → V) : V ⊕ J → V := Sum.elim id center

def oldHom (G : SimpleGraph V) (center : J → V) : G →g graph G center where
  toFun := Sum.inl
  map_rel' := by intro u v h; exact h

def collapseHom (G : SimpleGraph V) (center : J → V) : graph G center →g G where
  toFun := collapse center
  map_rel' := by
    intro u v h
    cases u <;> cases v
    · exact h
    · exact h
    · exact h
    · exact False.elim h

theorem edge_to_old (G : SimpleGraph V) (center : J → V) (s : V ⊕ J) (v : V)
    (h : G.Adj (collapse center s) v) : (graph G center).Adj s (.inl v) := by
  cases s <;> exact h

theorem edge_from_old (G : SimpleGraph V) (center : J → V) (s : V ⊕ J) (v : V)
    (h : G.Adj v (collapse center s)) : (graph G center).Adj (.inl v) s := by
  cases s <;> exact h

/-- Collapsing clones and retaining all old edges preserve every old-old walk bound. -/
theorem old_walk_bound_iff (G : SimpleGraph V) (center : J → V) (u v : V) (n : Nat) :
    (∃ p : (graph G center).Walk (.inl u) (.inl v), p.length ≤ n) ↔
      ∃ p : G.Walk u v, p.length ≤ n := by
  constructor
  · rintro ⟨p,hp⟩
    exact ⟨p.map (collapseHom G center), by simpa using hp⟩
  · rintro ⟨p,hp⟩
    exact ⟨p.map (oldHom G center), by simpa using hp⟩

theorem lift_from (G : SimpleGraph V) (center : J → V) (s : V ⊕ J) (v : V)
    (p : G.Walk (collapse center s) v) (h : 0 < p.length) :
    ∃ q : (graph G center).Walk s (.inl v), q.length = p.length := by
  cases p with
  | nil => simp at h
  | @cons a b c hab tail =>
    exact ⟨Walk.cons (edge_to_old G center s b hab) (tail.map (oldHom G center)), by simp⟩

theorem exists_cons_of_pos (G : SimpleGraph V) {u v : V} (p : G.Walk u v) (h : 0 < p.length) :
    ∃ (w : V) (ha : G.Adj u w) (tail : G.Walk w v), p = Walk.cons ha tail := by
  cases p with
  | nil => simp at h
  | cons ha tail => exact ⟨_,ha,tail,rfl⟩

theorem lift_both (G : SimpleGraph V) (center : J → V) (s t : V ⊕ J)
    (p : G.Walk (collapse center s) (collapse center t)) (h : 2 ≤ p.length) :
    ∃ q : (graph G center).Walk s t, q.length = p.length := by
  obtain ⟨b,hab,tail,heq⟩ := exists_cons_of_pos G p (by omega)
  rw [heq] at h ⊢
  have ht : 0 < tail.reverse.length := by simpa using (show 0 < tail.length by simpa using h)
  obtain ⟨q,hq⟩ := lift_from G center t b tail.reverse ht
  refine ⟨Walk.cons (edge_to_old G center s b hab) q.reverse, ?_⟩
  simp only [Walk.length_cons, Walk.length_reverse, hq, Walk.length_reverse]

/-- Full old-neighborhood cloning preserves D≥3 when the source has no isolated vertex. -/
theorem diameterAtMost (G : SimpleGraph V) (center : J → V) (D : Nat)
    (hD : 3 ≤ D) (hG : DegreeDiameter.Portfolio.DiameterAtMost G D)
    (hne : ∀ v, ∃ w, G.Adj v w) : DegreeDiameter.Portfolio.DiameterAtMost (graph G center) D := by
  intro s t
  obtain ⟨p,hp⟩ := hG (collapse center s) (collapse center t)
  by_cases h0 : p.length = 0
  · have heq := Walk.eq_of_length_eq_zero h0
    obtain ⟨w,hw⟩ := hne (collapse center s)
    have ht : G.Adj w (collapse center t) := by rw [← heq]; exact G.symm hw
    exact ⟨Walk.cons (edge_to_old G center s w hw)
      (Walk.cons (edge_from_old G center t w ht) Walk.nil), by change 2 ≤ D; omega⟩
  · by_cases h1 : p.length = 1
    · have he := Walk.adj_of_length_eq_one h1
      exact ⟨Walk.cons (edge_to_old G center s (collapse center t) he)
        (Walk.cons (show (graph G center).Adj (.inl (collapse center t)) (.inl (collapse center s)) from G.symm he)
          (Walk.cons (edge_from_old G center t (collapse center s) he) Walk.nil)), by change 3 ≤ D; exact hD⟩
    · obtain ⟨q,hq⟩ := lift_both G center s t p (by omega)
      exact ⟨q, hq ▸ hp⟩

theorem not_diameterAtMost (G : SimpleGraph V) (center : J → V) (D : Nat)
    (h : ¬DegreeDiameter.Portfolio.DiameterAtMost G D) :
    ¬DegreeDiameter.Portfolio.DiameterAtMost (graph G center) D := by
  intro he
  apply h
  intro u v
  exact (old_walk_bound_iff G center u v D).mp (he (.inl u) (.inl v))

instance (G : SimpleGraph V) (center : J → V) [DecidableRel G.Adj] :
    DecidableRel (graph G center).Adj := by
  intro u v
  cases u with
  | inl u => cases v with
    | inl v => exact inferInstanceAs (Decidable (G.Adj u v))
    | inr j => exact inferInstanceAs (Decidable (G.Adj u (center j)))
  | inr j => cases v with
    | inl v => exact inferInstanceAs (Decidable (G.Adj (center j) v))
    | inr k => exact isFalse id

section Degree
variable [Fintype V] [Fintype J] (G : SimpleGraph V) (center : J → V) [DecidableRel G.Adj]

def load (v : V) : Nat := Fintype.card {j : J // G.Adj v (center j)}

def oldNeighborEquiv (v : V) : (graph G center).neighborSet (.inl v) ≃
    G.neighborSet v ⊕ {j : J // G.Adj v (center j)} where
  toFun x := match x with
    | ⟨.inl w,h⟩ => .inl ⟨w,h⟩
    | ⟨.inr j,h⟩ => .inr ⟨j,h⟩
  invFun x := match x with
    | .inl ⟨w,h⟩ => ⟨.inl w,h⟩
    | .inr ⟨j,h⟩ => ⟨.inr j,h⟩
  left_inv := by rintro ⟨x,h⟩; cases x <;> rfl
  right_inv := by intro x; cases x <;> rfl

def newNeighborEquiv (j : J) : (graph G center).neighborSet (.inr j) ≃ G.neighborSet (center j) where
  toFun x := match x with
    | ⟨.inl v,h⟩ => ⟨v,h⟩
    | ⟨.inr _,h⟩ => False.elim h
  invFun x := ⟨.inl x.val,x.property⟩
  left_inv := by rintro ⟨x,h⟩; cases x <;> first | rfl | exact False.elim h
  right_inv := by intro x; rfl

theorem degree_old (v : V) : (graph G center).degree (.inl v) = G.degree v + load G center v := by
  rw [← SimpleGraph.card_neighborSet_eq_degree, Fintype.card_congr (oldNeighborEquiv G center v), Fintype.card_sum]
  rw [SimpleGraph.card_neighborSet_eq_degree]
  rfl

theorem degree_new (j : J) : (graph G center).degree (.inr j) = G.degree (center j) := by
  rw [← SimpleGraph.card_neighborSet_eq_degree, Fintype.card_congr (newNeighborEquiv G center j), SimpleGraph.card_neighborSet_eq_degree]

theorem degree_le (δ k : Nat) (hdeg : ∀ v, G.degree v ≤ δ) (hload : ∀ v, load G center v ≤ k) :
    ∀ u, (graph G center).degree u ≤ δ+k := by
  intro u
  cases u with
  | inl v => rw [degree_old]; exact Nat.add_le_add (hdeg v) (hload v)
  | inr j => rw [degree_new]; exact (hdeg (center j)).trans (Nat.le_add_right _ _)
end Degree
#print axioms diameterAtMost
#print axioms old_walk_bound_iff
#print axioms degree_le
end DegreeDiameter.Portfolio.FullNeighborhoodClones
