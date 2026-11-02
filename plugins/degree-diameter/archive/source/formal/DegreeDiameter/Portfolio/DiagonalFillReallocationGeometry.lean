import DegreeDiameter.Portfolio.DiagonalFillReallocationWalks
namespace DegreeDiameter.Portfolio.DiagonalFillReallocation
open SimpleGraph
variable {P L V J I : Type*}

theorem flag_neighbor (e : V ≃ P × L) (Inc : P → L → Prop) (spread : J → L)
    (owner : P → J) (cover : ∀p,Inc p (spread (owner p)))
    (two : ∀l,∃a b,Inc a l ∧ Inc b l ∧ a≠b)
    (project : ∀p l,∃q m,Inc q l ∧ Inc p m ∧ Inc q m) :
    ∀v,∃j w,(OppositeGQSpread.graph e Inc spread).Adj (.inr j) (.inl w) ∧
      (rawGraph e Inc).Adj w v := by
  classical
  intro v
  by_cases hf : Inc (e v).1 (e v).2
  · have make (q : P) (hq : Inc q (e v).2) (hne : q≠(e v).1) :
        ∃j w,(OppositeGQSpread.graph e Inc spread).Adj (.inr j) (.inl w) ∧
          (rawGraph e Inc).Adj w v := by
      let w := e.symm (q,(e v).2)
      have hw : w≠v := by
        intro he
        apply hne
        have h := congrArg (fun x => (e x).1) he
        simpa only [w,Equiv.apply_symm_apply] using h
      refine ⟨owner q,w,?_,?_⟩
      · change Inc (e w).1 (e w).2 ∧ Inc (e w).1 (spread (owner q))
        simpa only [w,Equiv.apply_symm_apply] using And.intro hq (cover q)
      · exact ⟨hw,by simpa only [w,Equiv.apply_symm_apply] using hq,
          by simpa only [w,Equiv.apply_symm_apply] using hf⟩
    obtain ⟨a,b,ha,hb,hab⟩ := two (e v).2
    by_cases he : a=(e v).1
    · exact make b hb (by intro h; exact hab (he.trans h.symm))
    · exact make a ha he
  · obtain ⟨q,m,hql,hpm,hqm⟩ := project (e v).1 (e v).2
    let w := e.symm (q,m)
    have hflag : Inc (e w).1 (e w).2 := by
      simpa only [w,Equiv.apply_symm_apply] using hqm
    have hw : w≠v := by intro he; rw [he] at hflag; exact hf hflag
    refine ⟨owner q,w,?_,?_⟩
    · change Inc (e w).1 (e w).2 ∧ Inc (e w).1 (spread (owner q))
      exact ⟨hflag,by simpa only [w,Equiv.apply_symm_apply] using cover q⟩
    · exact ⟨hw,by simpa only [w,Equiv.apply_symm_apply] using hql,
        by simpa only [w,Equiv.apply_symm_apply] using hpm⟩

private theorem weak_raw (e : V ≃ P × L) (Inc : P → L → Prop)
    (p q : P) (l m : L) (hp : Inc p m) (hq : Inc q l) :
    e.symm (p,l)=e.symm (q,m) ∨ (rawGraph e Inc).Adj (e.symm (p,l)) (e.symm (q,m)) := by
  classical
  by_cases h : e.symm (p,l)=e.symm (q,m)
  · exact Or.inl h
  · exact Or.inr ⟨h,by simpa only [Equiv.apply_symm_apply] using hp,
      by simpa only [Equiv.apply_symm_apply] using hq⟩

theorem filler_route (e : V ≃ P × L) (Inc : P → L → Prop) (spread : J → L)
    (ovoid : I → P) (owner : P → J) (cover : ∀p,Inc p (spread (owner p)))
    (two : ∀l,∃a b,Inc a l ∧ Inc b l ∧ a≠b)
    (hS : ∀p j k,Inc p (spread j) → Inc p (spread k) → j=k)
    (project : ∀p l,∃q m,Inc q l ∧ Inc p m ∧ Inc q m) :
    ∀j (c:I×J),∃w,∃path:(OppositeGQSpread.graph e Inc spread).Walk (.inr j) (.inl w),
      path.length≤2 ∧ (rawGraph e Inc).Adj w (e.symm (ovoid c.1,spread c.2)) := by
  classical
  intro j c
  let p := ovoid c.1
  let l := spread c.2
  let cv := e.symm (p,l)
  obtain ⟨a,n,ha,hpn,han⟩ := project p (spread j)
  obtain ⟨q,b,hql,hab,hqb⟩ := project a l
  let av := e.symm (a,b)
  let bv := e.symm (q,n)
  have hfa : (OppositeGQSpread.graph e Inc spread).Adj (.inr j) (.inl av) := by
    exact ⟨by simpa only [av,Equiv.apply_symm_apply] using hab,
      by simpa only [av,Equiv.apply_symm_apply] using ha⟩
  have hab' : av=bv ∨ (rawGraph e Inc).Adj av bv := weak_raw e Inc a q b n han hqb
  have hbc : bv=cv ∨ (rawGraph e Inc).Adj bv cv := weak_raw e Inc q p n l hql hpn
  by_cases hac : av=cv
  · have hfc : (OppositeGQSpread.graph e Inc spread).Adj (.inr j) (.inl cv) := by rw [←hac]; exact hfa
    have hpj : Inc p (spread j) := by simpa only [cv,Equiv.apply_symm_apply] using hfc.2
    have hpl : Inc p (spread c.2) := by simpa only [cv,l,Equiv.apply_symm_apply] using hfc.1
    have hjc : j=c.2 := hS p j c.2 hpj hpl
    obtain ⟨k,w,hkw,hw⟩ := flag_neighbor e Inc spread owner cover two project cv
    have hwc : Inc (e w).1 (spread c.2) := by
      simpa only [cv,l,Equiv.apply_symm_apply] using hw.2.1
    have hkc : k=c.2 := hS (e w).1 k c.2 hkw.2 hwc
    have hjw : (OppositeGQSpread.graph e Inc spread).Adj (.inr j) (.inl w) := by
      simpa only [hjc,hkc] using hkw
    exact ⟨w,Walk.cons hjw Walk.nil,by simp,hw⟩
  · rcases hbc with hbc | hbc
    · have habc : (rawGraph e Inc).Adj av cv := by
        rcases hab' with he | he
        · exact False.elim (hac (he.trans hbc))
        · rw [hbc] at he
          exact he
      exact ⟨av,Walk.cons hfa Walk.nil,by simp,habc⟩
    · rcases hab' with hab' | hab'
      · have hfb : (OppositeGQSpread.graph e Inc spread).Adj (.inr j) (.inl bv) := by
          rw [←hab'];exact hfa
        exact ⟨bv,Walk.cons hfb Walk.nil,by simp,hbc⟩
      · have habH : (OppositeGQSpread.graph e Inc spread).Adj (.inl av) (.inl bv) := hab'
        exact ⟨bv,Walk.cons hfa (Walk.cons habH Walk.nil),by simp,hbc⟩
#print axioms flag_neighbor
#print axioms filler_route
end DegreeDiameter.Portfolio.DiagonalFillReallocation
