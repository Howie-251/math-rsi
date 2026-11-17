import ES7ClosureFrame

namespace ES7ClosureConstruction
open ES7ActualState ES7NamedGeometry ES7BalancedEndpoints ES8BalancedGeometry ES7StateUniverse
open ES7JointRealization ES7ClosureFrame

/-- Extend actual chronology to inactive names without fixing incomparable
active states. Used with actual tail states and the fixed core catalogue. -/
noncomputable def baseModel (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point))
    (states : Nat→Finset Label) (active : Finset Nat) (owner : Nat→Nat)
    (activeBound : ∀i∈active,i < 40) (ownerBound : ∀i∈active,owner i < 50)
    (ownerInj : Set.InjOn owner ↑active)
    (actual : ∀i∈active,incoming c.cup (owner i)=states i)
    (size : ∀i < 40,(states i).card ≤ 16) : ES7NamedGeometry.Model c 40 states where
  active := active
  active_bound := activeBound
  owner := owner
  owner_bound := ownerBound
  key := ES7JointRealization.key c states
  key_injective := key_inj c states
  actual_order := by
    intro i hi j hj
    have a := cut_actual c noSix states (ownerBound i hi) (actual i hi)
    have b := cut_actual c noSix states (ownerBound j hj) (actual j hj)
    have ib := activeBound i hi
    have jb := activeBound j hj
    have ci := size i ib
    have cj := size j jb
    constructor
    · intro lt
      by_contra bad
      by_cases eq : owner i=owner j
      · have ij := ownerInj hi hj eq
        subst j
        exact (lt_irrefl _ lt)
      · unfold ES7JointRealization.key at lt
        omega
    · intro lt
      unfold ES7JointRealization.key
      omega
  actual_state := by
    intro i hi q
    rw [←actual i hi]
    exact mem_incoming c noSix (ownerBound i hi)
  inclusion_order := fun i j ih jh=>key_inclusion c states ih jh
  noSix := noSix
  noGon := noH

noncomputable def name (c : Configuration 50) (v : Fin 50) : Nat := (ES7BalancedNamed.nameIndex c.cup v.val).val
noncomputable def activeCore (c : Configuration 50) : Finset Nat := (starters c true).image (name c)
noncomputable def coreOwner (c : Configuration 50) (i : Nat) : Fin 50 := by
  classical
  exact if h : ∃v∈starters c true,name c v=i then Classical.choose h else 0

theorem name_bound (c : Configuration 50) (v : Fin 50) : name c v < 35 := (ES7BalancedNamed.nameIndex c.cup v.val).isLt

theorem coreOwner_spec (c : Configuration 50) (hi : i∈activeCore c) :
    coreOwner c i∈starters c true ∧ name c (coreOwner c i)=i := by
  classical
  obtain ⟨v,hv,eq⟩ := Finset.mem_image.mp hi
  have h : ∃v∈starters c true,name c v=i := ⟨v,hv,eq⟩
  simp only [coreOwner,dif_pos h]
  exact Classical.choose_spec h

theorem activeCore_bound (c : Configuration 50) (hi : i∈activeCore c) : i < 35 := by
  obtain ⟨v,_,rfl⟩ := Finset.mem_image.mp hi
  exact name_bound c v

theorem coreOwner_name (c : Configuration 50) (noSix : NoSix c.cup (Finset.range 50))
    (v : Fin 50) (hv : v∈starters c true) : coreOwner c (name c v)=v := by
  have hi : name c v∈activeCore c := Finset.mem_image.mpr ⟨v,hv,rfl⟩
  have spec := coreOwner_spec c hi
  apply ES7BalancedNamed.core_index_injective c noSix spec.1 hv
  exact Fin.ext spec.2

theorem coreStates_actual (c : Configuration 50) (noSix : NoSix c.cup (Finset.range 50))
    (v : Fin 50) (hv : v∈starters c true) :
    incoming c.cup v.val=coreStates (name c v) := by
  classical
  ext q
  simp only [coreStates,dif_pos (name_bound c v)]
  have eq : (⟨name c v,name_bound c v⟩ : Fin 35)=ES7BalancedNamed.nameIndex c.cup v.val := rfl
  rw [eq,ES7BalancedNamed.nameIndex_spec,mem_incoming c noSix v.isLt]
  constructor
  · intro h
    let cell := cellOf q ⟨h.1,h.2.1⟩ (ES7BalancedAmbient.starter_incoming_bounds c noSix v hv h)
    have same : cellLabel cell=q := cellOf_label _ _ _
    exact Finset.mem_image.mpr ⟨cell,(mem_state c.cup v.val cell).mpr (same.symm ▸ h),same⟩
  · rintro h
    obtain ⟨cell,hc,rfl⟩ := Finset.mem_image.mp h
    exact (mem_state c.cup v.val cell).mp hc

theorem coreStates_size (i : Nat) : (coreStates i).card ≤ 16 := by
  unfold coreStates
  split
  next h =>
    have a := Finset.card_image_le (s:=ES7BalancedNamed.named ⟨i,h⟩) (f:=cellLabel)
    have b := ES7BalancedNamed.named_size ⟨i,h⟩
    omega
  next h => simp

theorem incoming_size (cup : Nat→Nat→Nat→Bool) (v : Nat) : (incoming cup v).card ≤ 16 := by
  classical
  have sub : incoming cup v⊆grid := Finset.filter_subset _ _
  have size : grid.card=16 := by decide
  have h := Finset.card_le_card sub
  omega
noncomputable def selectedOwner (c : Configuration 50) (tail : Fin 4→Fin 50) (i : Nat) : Nat :=
  if i < 35 then (coreOwner c i).val else (tail ⟨(i-35)%4,Nat.mod_lt _ (by omega)⟩).val
noncomputable def selectedActive (c : Configuration 50) := activeCore c ∪ Finset.Ico 35 39
noncomputable def selectedStates (c : Configuration 50) (tail : Fin 4→Fin 50) (i : Nat) : Finset Label :=
  if i < 35 then coreStates i else incoming c.cup (selectedOwner c tail i)

theorem selectedOwner_core (c : Configuration 50) (tail : Fin 4→Fin 50) (hi : i < 35) :
    selectedOwner c tail i=(coreOwner c i).val := by simp [selectedOwner,hi]

theorem selectedOwner_tail (c : Configuration 50) (tail : Fin 4→Fin 50) (i : Fin 4) :
    selectedOwner c tail (35+i.val)=(tail i).val := by
  simp only [selectedOwner,show ¬35+i.val < 35 by omega,if_false,Nat.add_sub_cancel_left,
    Nat.mod_eq_of_lt i.isLt]

theorem selectedActive_bound (c : Configuration 50) (hi : i∈selectedActive c) : i < 39 := by
  rcases Finset.mem_union.mp hi with h|h
  · have := activeCore_bound c h; omega
  · exact (Finset.mem_Ico.mp h).2

theorem selectedOwner_bound (c : Configuration 50) (tail : Fin 4→Fin 50) (i : Nat) : selectedOwner c tail i < 50 := by
  unfold selectedOwner
  split <;> exact Fin.isLt _

theorem selected_tail_order (c : Configuration 50) (tail : Fin 4→Fin 50) (mono : StrictMono tail)
    (last : Fin 50) (lastMax : ∀v∈starters c true,v ≤ last) (after : last < tail 0)
    (hi : i∈selectedActive c) (hj : j∈selectedActive c) (oneTail : 35 ≤ i ∨ 35 ≤ j) :
    i < j ↔ selectedOwner c tail i < selectedOwner c tail j := by
  have ib := selectedActive_bound c hi
  have jb := selectedActive_bound c hj
  have later : ∀u∈activeCore c,∀t : Fin 4,(coreOwner c u).val < (tail t).val := by
    intro u hu t
    have a := lastMax _ (coreOwner_spec c hu).1
    have b := mono.monotone (show (0 : Fin 4) ≤ t by exact Fin.zero_le t)
    exact lt_of_le_of_lt a (after.trans_le b)
  by_cases ic : i < 35
  · have it : i∈activeCore c := (Finset.mem_union.mp hi).resolve_right (by intro h; have := (Finset.mem_Ico.mp h).1; omega)
    have jt : 35 ≤ j := by omega
    let t : Fin 4 := ⟨j-35,by omega⟩
    have jeq : j=35+t.val := by dsimp [t]; omega
    rw [jeq,selectedOwner_core c tail ic,selectedOwner_tail]
    exact iff_of_true (by omega) (later i it t)
  · have it : 35 ≤ i := by omega
    let t : Fin 4 := ⟨i-35,by omega⟩
    have ieq : i=35+t.val := by dsimp [t]; omega
    by_cases jc : j < 35
    · have ja : j∈activeCore c := (Finset.mem_union.mp hj).resolve_right (by intro h; have := (Finset.mem_Ico.mp h).1; omega)
      rw [ieq,selectedOwner_core c tail jc,selectedOwner_tail]
      have late := later j ja t
      exact iff_of_false (by omega) (by omega)
    · let s : Fin 4 := ⟨j-35,by omega⟩
      have jeq : j=35+s.val := by dsimp [s]; omega
      rw [ieq,jeq,selectedOwner_tail,selectedOwner_tail]
      change 35+t.val < 35+s.val ↔ tail t < tail s
      rw [mono.lt_iff_lt]
      change 35+t.val < 35+s.val ↔ t.val < s.val
      omega

theorem selectedOwner_inj (c : Configuration 50) (tail : Fin 4→Fin 50) (mono : StrictMono tail)
    (last : Fin 50) (lastMax : ∀v∈starters c true,v ≤ last) (after : last < tail 0) :
    Set.InjOn (selectedOwner c tail) ↑(selectedActive c) := by
  intro i hi j hj eq
  by_cases ic : i < 35
  · by_cases jc : j < 35
    · have ai : i∈activeCore c := (Finset.mem_union.mp hi).resolve_right (by intro h; have := (Finset.mem_Ico.mp h).1; omega)
      have aj : j∈activeCore c := (Finset.mem_union.mp hj).resolve_right (by intro h; have := (Finset.mem_Ico.mp h).1; omega)
      rw [selectedOwner_core c tail ic,selectedOwner_core c tail jc] at eq
      have same : coreOwner c i=coreOwner c j := Fin.ext eq
      exact (coreOwner_spec c ai).2.symm.trans ((congrArg (name c) same).trans (coreOwner_spec c aj).2)
    · have order := selected_tail_order c tail mono last lastMax after hi hj (Or.inr (by omega))
      omega
  · have a := selected_tail_order c tail mono last lastMax after hi hj (Or.inl (by omega))
    have b := selected_tail_order c tail mono last lastMax after hj hi (Or.inr (by omega))
    omega

noncomputable def selectedBase (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point))
    (tail : Fin 4→Fin 50) (mono : StrictMono tail)
    (last : Fin 50) (lastMax : ∀v∈starters c true,v ≤ last) (after : last < tail 0) :
    ES7NamedGeometry.Model c 40 (selectedStates c tail) :=
  baseModel c noSix noH (selectedStates c tail) (selectedActive c) (selectedOwner c tail)
    (fun i hi=>lt_trans (selectedActive_bound c hi) (by omega))
    (fun i _=>selectedOwner_bound c tail i) (selectedOwner_inj c tail mono last lastMax after)
    (by
      intro i hi
      by_cases core : i < 35
      · have ai : i∈activeCore c := (Finset.mem_union.mp hi).resolve_right (by intro h; have := (Finset.mem_Ico.mp h).1; omega)
        have spec := coreOwner_spec c ai
        simp only [selectedStates,if_pos core,selectedOwner_core c tail core]
        exact (coreStates_actual c noSix _ spec.1).trans (congrArg coreStates spec.2)
      · simp [selectedStates,core])
    (by
      intro i hi
      unfold selectedStates
      split
      · exact coreStates_size i
      · exact incoming_size c.cup _)

noncomputable def frame (c : Configuration 50)
    (noSix : NoSix c.cup (Finset.range 50))
    (noH : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point)) (normal : c.cup 0 1 2=true)
    (tail : Fin 4→Fin 50) (mono : StrictMono tail)
    (last : Fin 50) (lastIn : last∈starters c true)
    (lastMax : ∀v∈starters c true,v ≤ last) (after : last < tail 0)
    (terminal : (ES8ActualRanks.colorConfig c.cup true).Cup [last.val,(tail 0).val,(tail 1).val,(tail 2).val,(tail 3).val]) :
    ES7ClosureFrame.Model c (selectedStates c tail) where
  base := selectedBase c noSix noH tail mono last lastMax after
  active_bound := fun i hi=>selectedActive_bound c hi
  core_states := by intro i hi; simp [selectedStates,hi]
  tail_active := fun i lo hi=>Finset.mem_union_right _ (Finset.mem_Ico.mpr ⟨lo,hi⟩)
  tail_order := fun i hi j hj=>selected_tail_order c tail mono last lastMax after hi hj
  core_starts := by
    intro i hi core
    have ai : i∈activeCore c := (Finset.mem_union.mp hi).resolve_right (by intro h; have := (Finset.mem_Ico.mp h).1; omega)
    change StartsFive c.cup true _ (selectedOwner c tail i)
    rw [selectedOwner_core c tail core]
    exact (mem_starters c true _).mp (coreOwner_spec c ai).1
  core_cover := by
    intro v hv
    refine ⟨name c v,name_bound c v,Finset.mem_union_left _ (Finset.mem_image.mpr ⟨v,hv,rfl⟩),?_⟩
    change selectedOwner c tail (name c v)=v.val
    rw [selectedOwner_core c tail (name_bound c v),coreOwner_name c noSix v hv]
  normalized := normal
  last := name c last
  last_active := Finset.mem_union_left _ (Finset.mem_image.mpr ⟨last,lastIn,rfl⟩)
  last_core := name_bound c last
  last_max := by
    intro i hi core
    have ai : i∈activeCore c := (Finset.mem_union.mp hi).resolve_right (by intro h; have := (Finset.mem_Ico.mp h).1; omega)
    change selectedOwner c tail i ≤ selectedOwner c tail (name c last)
    rw [selectedOwner_core c tail core,selectedOwner_core c tail (name_bound c last),coreOwner_name c noSix last lastIn]
    exact lastMax _ (coreOwner_spec c ai).1
  terminal := by
    change (ES8ActualRanks.colorConfig c.cup true).Cup [selectedOwner c tail (name c last),selectedOwner c tail 35,selectedOwner c tail 36,selectedOwner c tail 37,selectedOwner c tail 38]
    rw [selectedOwner_core c tail (name_bound c last),coreOwner_name c noSix last lastIn]
    have a := selectedOwner_tail c tail 0
    have b := selectedOwner_tail c tail 1
    have d := selectedOwner_tail c tail 2
    have e := selectedOwner_tail c tail 3
    simp only [show 35+(0 : Fin 4).val=35 by rfl,show 35+(1 : Fin 4).val=36 by rfl,
      show 35+(2 : Fin 4).val=37 by rfl,show 35+(3 : Fin 4).val=38 by rfl] at a b d e
    rw [a,b,d,e]
    exact terminal
end ES7ClosureConstruction
