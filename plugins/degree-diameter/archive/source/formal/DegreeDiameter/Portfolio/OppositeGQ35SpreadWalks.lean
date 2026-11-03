import DegreeDiameter.Portfolio.OppositeGQ35SpreadGeneric
namespace DegreeDiameter.Portfolio.OppositeGQSpread
open SimpleGraph
variable {P L V J : Type*}

private theorem short_step {W : Type*} (G : SimpleGraph W) {u v : W}
    (h : u = v ∨ G.Adj u v) : ∃ w : G.Walk u v, w.length ≤ 1 := by
  rcases h with rfl | h
  · exact ⟨Walk.nil,by simp⟩
  · exact ⟨Walk.cons h Walk.nil,by simp⟩

private theorem short_three {W : Type*} (G : SimpleGraph W) {a b c d : W}
    (h₁ : a = b ∨ G.Adj a b) (h₂ : b = c ∨ G.Adj b c)
    (h₃ : c = d ∨ G.Adj c d) : ∃ w : G.Walk a d, w.length ≤ 3 := by
  obtain ⟨w₁,h₁⟩ := short_step G h₁
  obtain ⟨w₂,h₂⟩ := short_step G h₂
  obtain ⟨w₃,h₃⟩ := short_step G h₃
  exact ⟨w₁.append (w₂.append w₃),by simp only [Walk.length_append]; omega⟩

variable (e : V ≃ P × L) (Inc : P → L → Prop) (spread : J → L)
private def atOld (p : P) (l : L) : V ⊕ J := .inl (e.symm (p,l))

private theorem weak_old (p q : P) (l m : L) (hp : Inc p m) (hq : Inc q l) :
    atOld (J:=J) e p l = atOld e q m ∨ (graph e Inc spread).Adj (atOld e p l) (atOld e q m) := by
  classical
  by_cases h : e.symm (p,l) = e.symm (q,m)
  · exact Or.inl (congrArg Sum.inl h)
  · exact Or.inr ⟨h,by simpa only [Equiv.apply_symm_apply] using hp,
      by simpa only [Equiv.apply_symm_apply] using hq⟩

/-- A point-line projection gives actual paths in the augmented opposite graph.
Projection uniqueness and disjointness of the spread are unnecessary for this
upper bound; finite input callers still prove every existence obligation. -/
theorem diameter_three
    (project : ∀ p l, ∃ q m, Inc q l ∧ Inc p m ∧ Inc q m)
    (line_nonempty : ∀ j, ∃ p, Inc p (spread j)) :
    DiameterAtMost (graph e Inc spread) 3 := by
  have oldnew : ∀ (i : J) (p : P) (l : L),
      ∃ w : (graph e Inc spread).Walk (.inr i) (atOld e p l), w.length ≤ 3 := by
    intro i p l
    obtain ⟨a,n,ha,hpn,han⟩ := project p (spread i)
    obtain ⟨q,b,hql,hab,hqb⟩ := project a l
    apply short_three (graph e Inc spread)
      (b:=atOld e a b) (c:=atOld e q n)
    · exact Or.inr ⟨by simpa only [Equiv.apply_symm_apply] using hab,
        by simpa only [Equiv.apply_symm_apply] using ha⟩
    · exact weak_old e Inc spread a q b n han hqb
    · exact weak_old e Inc spread q p n l hql hpn
  have parts (v : V) : atOld (J:=J) e (e v).1 (e v).2 = .inl v := by
    change Sum.inl (e.symm (e v)) = Sum.inl v
    rw [e.symm_apply_apply]
  intro u v
  cases u with
  | inl u =>
    cases v with
    | inl v =>
      let p := (e u).1
      let l := (e u).2
      let q := (e v).1
      let m := (e v).2
      obtain ⟨a,k,hal,hqk,hak⟩ := project q l
      obtain ⟨b,n,hbm,hpn,hbn⟩ := project p m
      have h := short_three (graph e Inc spread)
        (weak_old e Inc spread p a l n hpn hal)
        (weak_old e Inc spread a b n k hak hbn)
        (weak_old e Inc spread b q k m hbm hqk)
      change ∃ w : (graph e Inc spread).Walk (atOld e (e u).1 (e u).2) (atOld e (e v).1 (e v).2), w.length ≤ 3 at h
      rw [parts u,parts v] at h
      exact h
    | inr j =>
      obtain ⟨w,hw⟩ := oldnew j (e u).1 (e u).2
      have h := (show ∃ z : (graph e Inc spread).Walk (atOld e (e u).1 (e u).2) (.inr j), z.length ≤ 3 from ⟨w.reverse,by simpa using hw⟩)
      rw [parts u] at h
      exact h
  | inr i =>
    cases v with
    | inl v =>
      have h := oldnew i (e v).1 (e v).2
      rw [parts v] at h
      exact h
    | inr j =>
      obtain ⟨a,ha⟩ := line_nonempty i
      obtain ⟨c,b,hc,hab,hcb⟩ := project a (spread j)
      apply short_three (graph e Inc spread) (b:=atOld e a b) (c:=atOld e c b)
      · exact Or.inr ⟨by simpa only [Equiv.apply_symm_apply] using hab,
          by simpa only [Equiv.apply_symm_apply] using ha⟩
      · exact weak_old e Inc spread a c b b hab hcb
      · exact Or.inr ⟨by simpa only [Equiv.apply_symm_apply] using hcb,
          by simpa only [Equiv.apply_symm_apply] using hc⟩
#print axioms diameter_three
end DegreeDiameter.Portfolio.OppositeGQSpread
