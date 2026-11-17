import ES7BalancedNamed

namespace ES7BalancedSelection
open ES8Geometry ES8BalancedGeometry ES8ActualRanks ES7Geometry
open ES7BalancedEndpoints ES7BalancedPopulations ES7BalancedEquality ES7BalancedNamed

theorem reflected_noSix {n} (c : Configuration n) (noSix : NoSix c.cup (Finset.range n)) :
    NoSix (ES7Reflection.reflect c).cup (Finset.range n) := by
  intro b h
  exact noSix (!b) (ES7Reflection.hasCup_reflect c b 6 _ (fun _ h=>h) h)

/-- Normalize the whole ambient configuration. Starter membership is then
defined afresh in that configuration, rather than transported by assumption. -/
theorem exists_normalized (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬HasConvexHeptagon (Set.range c.point)) :
    ∃ d : Configuration 50, NoSix d.cup (Finset.range 50) ∧
      ¬HasConvexHeptagon (Set.range d.point) ∧ d.cup 0 1 2=true := by
  cases h : c.cup 0 1 2 with
  | true => exact ⟨c,noSix,noH,h⟩
  | false =>
    refine ⟨ES7Reflection.reflect c,reflected_noSix c noSix,ES7Reflection.reflect_no_heptagon c noH,?_⟩
    rw [ES7Reflection.reflect_cup c 0 1 2 (by omega) (by omega) (by omega),h]
    rfl

/-- Choose all four tail vertices from one actual five-cup at the actual
last core point. The witnesses are not independent existential extensions. -/
theorem exists_terminal (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬HasConvexHeptagon (Set.range c.point)) :
    ∃ v a b d e : Fin 50, v∈starters c true ∧
      (∀ u∈starters c true,u≤v) ∧ v<a ∧ a<b ∧ b<d ∧ d<e ∧
      (colorConfig c.cup true).Cup [v.val,a.val,b.val,d.val,e.val] := by
  classical
  have nonempty : (starters c true).Nonempty := by
    apply Finset.card_pos.mp
    rw [starter_card c true noSix noH]
    omega
  let v := (starters c true).max' nonempty
  have mem : v∈starters c true := Finset.max'_mem _ _
  have last : ∀ u∈starters c true,u≤v := fun u hu=>Finset.le_max' _ u hu
  obtain ⟨a,b,d,e,chain,inside⟩ := (mem_starters c true v).mp mem
  have an : a<50 := Finset.mem_range.mp (inside a (by simp))
  have bn : b<50 := Finset.mem_range.mp (inside b (by simp))
  have dn : d<50 := Finset.mem_range.mp (inside d (by simp))
  have en : e<50 := Finset.mem_range.mp (inside e (by simp))
  have order := chain
  simp only [Config.Cup.cons3,Config.Cup.pair,colorConfig] at order
  exact ⟨v,⟨a,an⟩,⟨b,bn⟩,⟨d,dn⟩,⟨e,en⟩,mem,last,order.1,order.2.2.1,
    order.2.2.2.2.1,order.2.2.2.2.2.2,chain⟩

theorem terminal_selection_card (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬HasConvexHeptagon (Set.range c.point))
    (v a b d e : Fin 50) (last : ∀ u∈starters c true,u≤v)
    (va : v<a) (ab : a<b) (bd : b<d) (de : d<e) :
    (starters c true ∪ {a,b,d,e}).card=29 := by
  classical
  have ac : a<d := ab.trans bd
  have ae : a<e := ac.trans de
  have be : b<e := bd.trans de
  have disj : Disjoint (starters c true) {a,b,d,e} := by
    apply Finset.disjoint_left.mpr
    intro u hu member
    have uv:=last u hu
    simp only [Finset.mem_insert,Finset.mem_singleton] at member
    rcases member with rfl|rfl|rfl|rfl <;> omega
  rw [Finset.card_union_of_disjoint disj,starter_card c true noSix noH]
  have tail : ({a,b,d,e} : Finset (Fin 50)).card=4 := by
    simp [ne_of_lt ab,ne_of_lt ac,ne_of_lt ae,ne_of_lt bd,ne_of_lt be,ne_of_lt de]
  omega

/-- The completed geometric input to the remaining source interpretation.
No population bound, rank label, or core order is postulated. -/
theorem normalized_core_and_tail (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬HasConvexHeptagon (Set.range c.point)) :
    ∃ d : Configuration 50, NoSix d.cup (Finset.range 50) ∧
      ¬HasConvexHeptagon (Set.range d.point) ∧ d.cup 0 1 2=true ∧
      (starters d true).card=25 ∧ (active d).card=25 ∧
      (∀ u : Fin 50,u.val<5 → u∈starters d true) ∧
      ∃ v a b f g : Fin 50, v∈starters d true ∧
        (∀ u∈starters d true,u≤v) ∧ v<a ∧ a<b ∧ b<f ∧ f<g ∧
        (colorConfig d.cup true).Cup [v.val,a.val,b.val,f.val,g.val] ∧
        (starters d true ∪ {a,b,f,g}).card=29 := by
  obtain ⟨d,dSix,dH,initial⟩ := exists_normalized c noSix noH
  obtain ⟨v,a,b,f,g,hv,last,va,ab,bf,fg,chain⟩ := exists_terminal d dSix dH
  exact ⟨d,dSix,dH,initial,starter_card d true dSix dH,active_card d dSix dH,
    first_five_start d dSix dH initial,v,a,b,f,g,hv,last,va,ab,bf,fg,chain,
    terminal_selection_card d dSix dH v a b f g last va ab bf fg⟩

#print axioms normalized_core_and_tail
end ES7BalancedSelection
